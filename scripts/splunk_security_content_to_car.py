#!/usr/bin/python

'''
Author: Jose Hernandez <research@splunk.com>
Purpose: Convert Splunk Security Content detections to CAR analytics

'''

import argparse
import yaml
from datetime import datetime
from pyattck import Attck
from jinja2 import Environment, FileSystemLoader
from os import path

def generate_car_object(detection_yaml, car_id, DETECTION_PATH):
    print(detection_yaml)
    car_object = dict()
    car_object['id'] = car_id
    car_object['submission_date'] = datetime.now().strftime('%Y/%m/%d')
    car_object['information_domain'] = 'Analytic'
    car_object['analytic_type'] = 'TTP'
    car_object['contributors'] = ['Splunk Threat Research <research@splunk.com>']
    car_object['platforms'] = ['Windows']

    car_object['description'] = detection_yaml['description']

    # we should add the detection yaml or docs url as a ref as well
    references = detection_yaml['references']
    path_of_url = DETECTION_PATH.split('/')[-3:]
    detection_url = 'https://github.com/splunk/security_content/blob/develop/' + "/".join(path_of_url)
    references.append(detection_url)
    car_object['references'] = references

    implementation = []
    splunk_implementation = dict()
    splunk_implementation['name'] = 'Splunk'
    splunk_implementation['description'] = detection_yaml['how_to_implement']
    splunk_implementation['code'] = detection_yaml['search']
    implementation.append(splunk_implementation)
    car_object['implementation'] = implementation

    unit_tests = []
    unit_test = dict()
    unit_test['configurations'] = ['Using Splunk [Attack Range](https://github.com/splunk/attack_range)']
    unit_test['description'] = 'Replay the detection [dataset]({0})  using the Splunk attack range with the commands below'.format(detection_yaml['tags']['dataset'][0])
    unit_test['commands'] = ['python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]']
    unit_tests.append(unit_test)
    car_object['unit_tests'] = unit_tests

    return car_object

def mitre_attack_object(technique, attack):
    mitre_attack = dict()
    mitre_attack['technique_id'] = technique.id
    mitre_attack['technique'] = technique.name

    # process tactics
    tactics = []
    for tactic in technique.tactics:
        tactics.append(tactic.name)
    mitre_attack['tactic'] = tactics

    return mitre_attack

def get_mitre_enrichment_new(attack, mitre_attack_id):
    for technique in attack.enterprise.techniques:
        apt_groups = []
        if '.' in mitre_attack_id:
            for subtechnique in technique.subtechniques:
                if mitre_attack_id == subtechnique.id:
                    mitre_attack = mitre_attack_object(subtechnique, attack)
                    return mitre_attack

        elif mitre_attack_id == technique.id:
            mitre_attack = mitre_attack_object(technique, attack)
            return mitre_attack
    return []

def generate_car_analytics(DETECTION_PATH, OUTPUT_DIR, ANALYTICS_TEMPLATE_PATH, attack, VERBOSE):

    if VERBOSE:
        print("reading splunk security content detection: {0}".format(DETECTION_PATH))

    detection_yaml = dict()
    with open(DETECTION_PATH, 'r') as stream:
        try:
            object = list(yaml.safe_load_all(stream))[0]
        except yaml.YAMLError as exc:
            print(exc)
            print("Error reading {0}".format(manifest_file))
            sys.exit(1)

    detection_yaml = object

    # enrich the mitre object
    mitre_attacks = []
    if 'mitre_attack_id' in detection_yaml['tags']:
        for mitre_technique_id in detection_yaml['tags']['mitre_attack_id']:
            mitre_attack = get_mitre_enrichment_new(attack, mitre_technique_id)
            mitre_attacks.append(mitre_attack)
        detection_yaml['mitre_attacks'] = mitre_attacks

    date = datetime.now().strftime('%Y-%m')
    car_id = path.join( 'CAR-' + str(date) + '-001' )
    car_object = generate_car_object(detection_yaml, car_id, DETECTION_PATH)
    j2_env = Environment(loader=FileSystemLoader(ANALYTICS_TEMPLATE_PATH),
                             trim_blocks=False)
    # write markdown
    template = j2_env.get_template('analytic_template.md')

    output_path = path.join( OUTPUT_DIR + '/' + car_id + '.md' )
    output = template.render(analytic=car_object)
    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(output)

    print("splunk_security_content_to_car.py wrote CAR analytic to: {}".format(output_path))

if __name__ == "__main__":

    # grab arguments
    parser = argparse.ArgumentParser(description="Generates CAR analytics file from Splunk Security Content Detections")
    parser.add_argument("-p", "--path", required=True, help="path to security_content detection, example: security_content/detections/endpoint/suspicious_mshta_child_process.yml")
    parser.add_argument("-o", "--output", required=True, help="path to the car analytics")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="prints verbose output")

    # parse them
    args = parser.parse_args()
    DETECTION_PATH = args.path
    OUTPUT_DIR = args.output
    VERBOSE = args.verbose

    ANALYTICS_TEMPLATE_PATH = 'scripts/'

    if VERBOSE:
        print("getting mitre enrichment data from cti")
    attack = Attck()

    generate_car_analytics(DETECTION_PATH, OUTPUT_DIR, ANALYTICS_TEMPLATE_PATH, attack, VERBOSE)
    print("finished successfully!")
