"""This script generates the analytics portions of the site from the YAML in the analytics directory.

The following files are updated by this script, and should not be altered manually:
* docs/analytics/* (all CAR-NNNN-NN-NNN.md files and index.md)
* docs/data/analytics.json

"""

import json
import glob
import yaml
import requests
from jinja2 import Environment, Template, FileSystemLoader
from os import path, makedirs
import copy

ATTACK_URL = "https://raw.githubusercontent.com/mitre/cti/subtechniques/enterprise-attack/enterprise-attack.json"

# Get all analytics and load as list of dicts
analytics_files = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "*.yaml"))
analytics = []
for af in analytics_files:
    print("working on {}".format(af))
    analytics.append(yaml.load(open(af).read()))
#analytics = [yaml.load(open(analytic_file).read()) for analytic_file in analytics_files]

# Load ATT&CK content, which is needed to get names for technique IDs
attack = requests.get(ATTACK_URL).json()
techniques = {ap['external_references'][0]['external_id']: ap['name'] for ap in attack['objects'] if ap['type'] == 'attack-pattern'}
tactics = {ap['external_references'][0]['external_id']: ap['name'] for ap in attack['objects'] if ap['type'] == 'x-mitre-tactic'}

# Get the template file for the analytic page. Note that this is a markdown template which will be rendered by GH Pages.
env = Environment(loader=FileSystemLoader('../docs/true_positives'))
analytic_template = env.from_string(open('analytic_template.md').read())

# Generate the analytic page for each analytic
for analytic in analytics:

    # Do a bit of reformatting to make the template less ugly
    analytic_for_render = copy.deepcopy(analytic)
    if 'data_model_references' in analytic_for_render:
        analytic_for_render['data_model_references'] = [dmr.split('/') for dmr in analytic_for_render['data_model_references']]

    # Generate the markdown
    markdown = analytic_template.render(analytic=analytic_for_render, tactics=tactics, techniques=techniques)

    # Save to the analytic page
    makedirs('../docs/analytics/{}'.format(analytic['id']), exist_ok=True)
    open('../docs/analytics/{}/index.md'.format(analytic['id']), 'w').write(markdown)

# Generate the index.md file

# Note that the "analytics-table" div is used only by the CSS in order to get a reference to just the analytics table (see main.scss)

index_content = """---
title: "Analytics"
permalink: /analytics/
---
<div class="analytics-table"></div> 

## Analytic List (by date added)

|Analytic|ATT&CK Techniques|Implementations|Applicable Platform(s)|
|---|---|---|---|
"""

subtechnique_table = """---
## Analytic List (by technique/sub-technique coverage)

|ATT&CK Technique|ATT&CK Sub-technique(s)|CAR Analytic(s)|
|---|---|---|
"""

# Build the first (date-based) table
table_techniques = []
for analytic in sorted(analytics, key = lambda k: k['id']):
    coverage = ""
    implementations = ""
    if 'coverage' in analytic and len(analytic['coverage']) > 0:
        coverage += "{::nomarkdown}<ul>"
        for cov in analytic['coverage']:
          coverage += "<li><a href=\"https://attack.mitre.org/techniques/{}/\">{}</a></li>".format(cov['technique'], techniques[cov['technique']]) 
          # Get all of the techniques seen in all analytics
          # This is for building the second (subtechniques based) table
          if cov['technique'] not in table_techniques:
              table_techniques.append(cov['technique'])
        coverage += "</ul>{:/}" 
    if 'implementations' in analytic and len(analytic['implementations']) > 0: 
        imp_list =  [str.capitalize(implementation['type']) for implementation in analytic['implementations']]
        implementations = ", ".join(sorted(set(imp_list)))
    if 'platforms' in analytic and len(analytic['platforms']) > 0: 
        applicable_platforms = ", ".join(analytic['platforms'])
    else:
        applicable_platforms = "N/A"
    index_content += "|[{}: {}]({})|{}|{}|{}|\n".format(analytic['id'], analytic['title'], analytic['id'], coverage, implementations, applicable_platforms)

# Build the second (subtechnique-based) table
#print(table_techniques)
for tid in table_techniques:
    # Find all analytics with this technique
    none_bucket = []
    sub_bucket = {}
    for analytic in analytics:
        if "coverage" in analytic:
            for cov in analytic['coverage']:
                if cov["technique"] == tid:
                    if "subtechniques" not in cov:
                        none_bucket.append(analytic)
                    else:
                        for sub_tid in cov["subtechniques"]:
                            if sub_tid not in sub_bucket:
                                sub_bucket[sub_tid] = [analytic]
                            else:
                                sub_bucket[sub_tid].append(analytic)
                    break
    # Write the base technique to the table
    none_str = ""
    none_sub_str = "(N/A - see below)"
    if none_bucket:
        none_str += "{::nomarkdown}<ul>"
        for analytic in sorted(none_bucket, key = lambda k: k['id']):
            none_str += "<li><a href=\"{}\">{}: {}</a></li>".format(analytic['id'], analytic['id'], analytic['title'])
        none_str += "</ul>{:/}"
        none_sub_str = "(N/A - technique only)"
    else:
        none_str = "(N/A - see below)"
    if len(sub_bucket.keys()) > 1:
      subtechnique_table += "|[{}](https://attack.mitre.org/techniques/{}/)|{}|{}|\n".format(techniques[tid],tid,none_sub_str,none_str)
    # Write the subtechniques to the table
    if sub_bucket:
        for sub_tid, car_list in sub_bucket.items():
            sub_str = "{::nomarkdown}<ul>"
            # Build the list of CAR analytics
            for analytic in sorted(car_list, key = lambda k: k['id']):
                sub_str += "<li><a href=\"{}\">{}: {}</a></li>".format(analytic['id'], analytic['id'], analytic['title'])
            sub_str += "</ul>{:/}"
            # Write the sub-technique entry to the table
            # Corner case where there is only one sub-technique and no technique-only analytics
            if not none_bucket and len(sub_bucket.keys()) == 1:
              subtechnique_table += "|[{}](https://attack.mitre.org/techniques/{}/)|[{}](https://attack.mitre.org/techniques/{}/{}/)|{}|\n".format(techniques[tid],tid,techniques[sub_tid],sub_tid.split(".")[0],sub_tid.split(".")[1],sub_str)
            else:
              subtechnique_table += "|...|[{}](https://attack.mitre.org/techniques/{}/{}/)|{}|\n".format(techniques[sub_tid],sub_tid.split(".")[0],sub_tid.split(".")[1],sub_str)

# Write the tables
index_file = open('../docs/analytics/index.md', 'w')
index_file.write(index_content)
index_file.write("\n")
index_file.write(subtechnique_table)
index_file.close()

# Generate analytics.json
analytics = [
    {
        'shortName': analytic['title'],
        'name': analytic['id'],
        'fields': analytic['data_model_references'] if 'data_model_references' in analytic else [],
        'attack': [{'tactics': [tactics[t] for t in coverage['tactics']], 'technique': 'Technique/{}'.format(coverage['technique']), 'coverage': coverage['coverage']} for coverage in analytic['coverage']] if 'coverage' in analytic else []
    } for analytic in analytics
]

open('../docs/data/analytics.json', 'w').write(json.dumps({'analytics': analytics}))
