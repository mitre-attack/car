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

ATTACK_URL = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

# Get all analytics and load as list of dicts
analytics_files = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "*.yaml"))
analytics = [yaml.load(open(analytic_file).read()) for analytic_file in analytics_files]

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

|Analytic|ATT&CK Techniques|Implementations|
|---|---|---|
"""

for analytic in sorted(analytics, key = lambda k: k['id']):
    coverage = ""
    implementations = ""
    if 'coverage' in analytic and len(analytic['coverage']) > 0:
        coverage = ", ".join(["[{}](https://attack.mitre.org/techniques/{}/)".format(techniques[coverage['technique']], coverage['technique']) for coverage in analytic['coverage']])
    if 'implementations' in analytic and len(analytic['implementations']) > 0: 
        imp_list =  [str.capitalize(implementation['type']) for implementation in analytic['implementations']]
        implementations = ", ".join(sorted(set(imp_list)))
    index_content += "|[{}: {}]({})|{}|{}|\n".format(analytic['id'], analytic['title'], analytic['id'], coverage, implementations)

open('../docs/analytics/index.md', 'w').write(index_content)

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
