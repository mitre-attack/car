"""This script generates the ATT&CK navigator layer from the YAML analytics files.
"""

import json
import glob
import yaml
import sys
from os import path

# Static ATT&CK Navigator layer JSON fields
VERSION = "2.1"
NAME = "CAR ATT&CK"
DESCRIPTION = "CAR Analytics ATT&CK Coverage"
DOMAIN = "mitre-enterprise"

# Base ATT&CK Navigator layer
layer_json = {
        "version": VERSION,
        "name": NAME,
        "description": DESCRIPTION,
        "domain": DOMAIN,
        "techniques": []
}    

# Get all analytics and load as list of dicts
analytics_files = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "*.yaml"))
analytics = [yaml.load(open(analytic_file).read()) for analytic_file in analytics_files]


# Build up the mappings
attack_mappings = {}
for analytic in analytics:
    title = analytic['title']
    id = analytic['id']
    name = "{0}: {1}".format(id, title)
    if 'coverage' in analytic and len(analytic['coverage']) > 0:
        for coverage in analytic['coverage']:
            technique = coverage['technique']
            if technique not in attack_mappings:
                attack_mappings[technique] = []
                attack_mappings[technique].append(name)
            elif technique in attack_mappings:
                car_entries = attack_mappings[technique]
                if name not in car_entries:
                    attack_mappings[technique].append(name)

# Add the ATT&CK techniques/CAR analytics to the layer
for k,v in attack_mappings.items():
    car_str = ""
    # Build up the CAR analytics string
    for car_a in sorted(v):
        car_str += car_a
        car_str += " | "
    car_str = car_str.rstrip(" | ")

    technique = {"techniqueID": k,
                 "color": "#c6dbef",
                 "comment": car_str,
                 "enabled": True}
    layer_json["techniques"].append(technique)

# output JSON
json.dump(layer_json, sys.stdout, indent=4)