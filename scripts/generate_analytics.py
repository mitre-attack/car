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
from datetime import date
import copy

ATTACK_URL = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

# Get all analytics and load as list of dicts
analytics_files = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "*.yaml"))
analytics = []
for af in analytics_files:
    print("appending {}".format(af))
    analytics.append(yaml.load(open(af,encoding='utf-8').read()))
#analytics = [yaml.load(open(analytic_file).read()) for analytic_file in analytics_files]

# Load ATT&CK content, which is needed to get names for technique IDs
attack = requests.get(ATTACK_URL, verify =False).json()
techniques = {ap['external_references'][0]['external_id']: ap['name'] for ap in attack['objects'] if ap['type'] == 'attack-pattern'}
tactics = {ap['external_references'][0]['external_id']: ap['name'] for ap in attack['objects'] if ap['type'] == 'x-mitre-tactic'}

# Get the template file for the analytic page. Note that this is a markdown template which will be rendered by GH Pages.
env = Environment(loader=FileSystemLoader('../docs/true_positives'))
analytic_template = env.from_string(open('analytic_template.md').read())

# Generate the analytic page for each analytic
for analytic in analytics:

    print("generating page for {}".format(analytic['id']))
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
tr = """            <tr>
                <td style="white-space:nowrap;">{0}</td>
                <td>{1}</td>
                <td style="white-space:nowrap;">{2}</td>
                <td>{3}</td>
                <td>{4}</td>
                <td>{5}</td>
            </tr>\n"""

index_content = """---
title: "Analytics"
permalink: /analytics/
---
<div class="analytics-table"></div> 

## Analytic List (sortable)
<script type="text/javascript" src="/assets/sort-table.js"></script>

<table class="js-sort-table" id="analytics-sort">
    <thead>
        <tr>
            <th style="white-space:nowrap;">ID</th>
            <th style="white-space:nowrap;">Name</th>
            <th style="white-space:nowrap;" class="js-sort-date">Submission Date</th>
            <th style="white-space:nowrap;">ATT&CK Techniques</th>
            <th style="white-space:nowrap;">Implementations</th>
            <th style="white-space:nowrap;">Applicable Platforms</th>
        </tr>
    </thead>
    <tbody>
"""
table_footer = """      </tbody>\n</table>"""

tr_tech_template = '''       <tr>
            <td {0}>{1}</td>
        </tr>
'''

tr_template = '''       <tr>
            <td {0}>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>
'''

tr_sub_template = '''       <tr>
            <td>{0}</td>
            <td>{1}</td>
        </tr>
'''

subtechnique_table = """---
title: "Analytics (by technique)"
permalink: /analytics/by_technique
---
<div class="tech-analytics-table"></div>

<table>
    <thead>
        <tr>
            <th style="white-space:nowrap;">ATT&CK Technique</th>
            <th style="white-space:nowrap;">ATT&CK Sub-technique(s)</th>
            <th style="white-space:nowrap;">CAR Analytic(s)</th>
        </tr>
    </thead>
    <tbody>
"""

# Build the first (date-based) table
table_techniques = []
for analytic in sorted(analytics, key = lambda k: k['id']):
    print("building date-based table, including {}".format(analytic['id']))
    coverage = ""
    implementations = ""
    car_id = "<a href=\"/analytics/{}/\">{}</a>".format(analytic["id"], analytic["id"])
    title = analytic["title"]
    date_added = analytic["submission_date"]
    date_str = date.fromisoformat(date_added.replace("/","-")).strftime("%B %d %Y")
    if 'coverage' in analytic and len(analytic['coverage']) > 0:
        coverage += "<ul>"
        count = 0
        for cov in analytic['coverage']:
          # Only capture the first two techniques, to limit the size of the table
          if count < 2:
            coverage += "<li><a href=\"https://attack.mitre.org/techniques/{}/\">{}</a></li>".format(cov['technique'], techniques[cov['technique']]) 
            count += 1
          # Get all of the techniques seen in all analytics
          # This is for building the second (subtechniques based) table
          if cov['technique'] not in table_techniques:
              table_techniques.append(cov['technique'])
        coverage += "</ul>" 
    if 'implementations' in analytic and len(analytic['implementations']) > 0: 
        imp_list =  [str.capitalize(implementation['type']) for implementation in analytic['implementations']]
        implementations = ", ".join(sorted(set(imp_list)))
    if 'platforms' in analytic and len(analytic['platforms']) > 0: 
        applicable_platforms = ", ".join(analytic['platforms'])
    else:
        applicable_platforms = "N/A"
    table_row = tr.format(car_id, title, date_str, coverage, implementations, applicable_platforms)
    index_content += table_row
index_content += table_footer

# Build the second (subtechnique-based) table
for tid in sorted(table_techniques):
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
        none_str += "<ul>"
        for analytic in sorted(none_bucket, key = lambda k: k['id']):
            none_str += "<li><a href=\"{}\">{}: {}</a></li>".format(analytic['id'], analytic['id'], analytic['title'])
        none_str += "</ul>"
        none_sub_str = "(N/A - technique only)"
    else:
        none_str = "(N/A - see below)"
    if len(sub_bucket.keys()) > 1 or len(none_bucket) > 0:
      num_rows = len(sub_bucket.keys()) + 1
      tid_url = "https://attack.mitre.org/techniques/{0}/".format(tid)
      tid_link = '<a href="{0}">{1}: {2}</a>'.format(tid_url,tid,techniques[tid])
      rowspan = 'rowspan="{0}"'.format(num_rows)
      if none_sub_str == "(N/A - technique only)":
        subtechnique_table += tr_template.format(rowspan,tid_link,none_sub_str,none_str)
      else:
        subtechnique_table += tr_tech_template.format(rowspan,tid_link)
    # Write the subtechniques to the table
    if sub_bucket:
        for sub_tid, car_list in sub_bucket.items():
            sub_str = "<ul>"
            # Build the list of CAR analytics
            for analytic in sorted(car_list, key = lambda k: k['id']):
                sub_str += "<li><a href=\"{}\">{}: {}</a></li>".format(analytic['id'], analytic['id'], analytic['title'])
            sub_str += "</ul>"
            # Write the sub-technique entry to the table
            # Corner case where there is only one sub-technique and no technique-only analytics
            if not none_bucket and len(sub_bucket.keys()) == 1:
              tid_url = "https://attack.mitre.org/techniques/{0}/".format(tid)
              sub_url = "https://attack.mitre.org/techniques/{0}/{1}/".format(sub_tid.split(".")[0],sub_tid.split(".")[1])
              tid_link = '<a href="{0}">{1}: {2}</a>'.format(tid_url,tid,techniques[tid])
              sub_link = '<a href="{0}">{1}: {2}</a>'.format(sub_url,sub_tid,techniques[sub_tid])
              subtechnique_table += tr_template.format("",tid_link,sub_link,sub_str)
            elif len(sub_bucket.keys()) == 1:
              sub_url = "https://attack.mitre.org/techniques/{0}/{1}/".format(sub_tid.split(".")[0],sub_tid.split(".")[1])
              sub_link = '<a href="{0}">{1}: {2}</a>'.format(sub_url,sub_tid,techniques[sub_tid])
              subtechnique_table += tr_sub_template.format(sub_link,sub_str)
            else:
              sub_url = "https://attack.mitre.org/techniques/{0}/{1}/".format(sub_tid.split(".")[0],sub_tid.split(".")[1])
              sub_link = '<a href="{0}">{1}: {2}</a>'.format(sub_url,sub_tid,techniques[sub_tid])
              subtechnique_table += tr_sub_template.format(sub_link,sub_str)
subtechnique_table += table_footer

# Write the tables
index_file = open('../docs/analytics/index.md', 'w')
index_file.write(index_content)
index_file.flush()
index_file.close()
makedirs('../docs/analytics/by_technique', exist_ok=True)
tech_index_file = open('../docs/analytics/by_technique/index.md', 'w')
tech_index_file.write(subtechnique_table)
tech_index_file.flush()
tech_index_file.close()

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
