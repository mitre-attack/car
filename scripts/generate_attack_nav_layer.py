"""This script generates the ATT&CK navigator layer from the YAML analytics files.
   Now incorporates sub-techniques.
"""

import json
import glob
import yaml
import sys
from os import path, makedirs

# Static ATT&CK Navigator layer JSON fields
VERSION = "3.0"
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
analytics = [yaml.load(open(analytic_file,encoding='utf-8').read()) for analytic_file in analytics_files]

def addMapping(technique, name, attack_mappings):
    if technique not in attack_mappings:
        attack_mappings[technique] = []
        attack_mappings[technique].append(name)
    elif technique in attack_mappings:
        car_entries = attack_mappings[technique]
        if name not in car_entries:
            attack_mappings[technique].append(name)

# Build up the mappings
attack_mappings = {}
for analytic in analytics:
    title = analytic['title']
    id = analytic['id']
    name = "{0}: {1}".format(id, title)
    if 'coverage' in analytic and len(analytic['coverage']) > 0:
        for coverage in analytic['coverage']:
            technique = coverage['technique']
            addMapping(technique, name, attack_mappings)
            if 'subtechniques' in coverage:
                for sub_technique in coverage['subtechniques']:
                    addMapping(sub_technique, name, attack_mappings)

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
    if "." not in k:
        technique["showSubtechniques"] = True
    layer_json["techniques"].append(technique)

# Output JSON to docs directory
makedirs('../docs/car_attack', exist_ok=True)
outfile = open("../docs/car_attack/car_attack.json","w")
json.dump(layer_json, outfile, indent=4)
outfile.close()
