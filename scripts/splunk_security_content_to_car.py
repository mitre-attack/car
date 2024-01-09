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
import re
from os import path

def generate_car_object(detection_yaml, car_id, DETECTION_PATH):
    car_object = dict()
    car_object['title'] = detection_yaml['name']
    car_object['submission_date'] = datetime.now().strftime('%Y/%m/%d')
    car_object['information_domain'] = 'Analytic'
    car_object['platforms'] = ['Windows']
    car_object['subtypes'] = ['Process']
    car_object['analytic_types'] = ['TTP']
    car_object['contributors'] = ['Splunk Threat Research <research@splunk.com>']
    car_object['id'] = car_id
    car_object['description'] = detection_yaml['description']
    car_object['coverage'] = detection_yaml['mitre_attacks']

    implementation = []
    splunk_implementation = dict()
    splunk_implementation['description'] = detection_yaml['how_to_implement']

    # cleaning up unecessary macros from splunk
    search = re.sub('\s`security_content_summariesonly`', '', detection_yaml['search'])
    search = re.sub('\|(\s|)\`security_content_ctime\((\w+|\"\w+\")\)\`', '', search)
    search = re.sub('\|\s\`drop_dm_object_name\((\w+|\"\w+\")\)\`', '', search)
    search = re.sub('\|\s\`\w+_filter\`', '', search)

    splunk_implementation['code'] = search.rstrip()
    splunk_implementation['type'] = 'Splunk'
    if len(detection_yaml['datamodel']) > 0:
        splunk_implementation['data_model'] = detection_yaml['datamodel'][0]
    else:
        splunk_implementation['data_model'] = ''
    implementation.append(splunk_implementation)
    car_object['implementations'] = implementation

    unit_tests = []
    unit_test = dict()
    unit_test['configurations'] = ['Using Splunk [Attack Range](https://github.com/splunk/attack_range)']
    unit_test['description'] = 'Replay the detection [dataset]({0})  using the Splunk attack range with the commands below'.format(detection_yaml['tags']['dataset'][0])
    unit_test['commands'] = ['python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]']
    unit_tests.append(unit_test)
    unit_test = dict()
    unit_test['configurations'] = ['Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)']
    unit_test['description'] = 'execute the atomic test [{0}](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/{0}) against a Windows target.'.format(detection_yaml['mitre_attacks'][0]['technique'])
    unit_test['commands'] = ['Invoke-AtomicTest {0}'.format(detection_yaml['mitre_attacks'][0]['technique'])]
    unit_tests.append(unit_test)
    car_object['unit_tests'] = unit_tests

    return car_object

def mitre_attack_object(technique, attack):
    mitre_attack = dict()
    mitre_attack['technique'] = technique.external_references[0].external_id
    # process tactics
    tactics = []
    for tactic in technique.tactics:
        tactics.append(tactic.external_references[0].external_id)
    mitre_attack['tactics'] = tactics
    mitre_attack['coverage'] = 'Moderate'

    return mitre_attack

def get_mitre_enrichment_new(attack, mitre_attack_id):
    for technique in attack.enterprise.techniques:
        if '.' in mitre_attack_id:
            for subtechnique in technique.techniques:
                if mitre_attack_id == subtechnique.external_references[0].external_id:
                    mitre_attack = mitre_attack_object(subtechnique, attack)
                    return mitre_attack

        elif mitre_attack_id == technique.external_references[0].external_id:
            mitre_attack = mitre_attack_object(technique, attack)
            return mitre_attack
    return []

def generate_car_analytics(DETECTION_PATH, OUTPUT_FILE, attack, VERBOSE):

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
    car_id = OUTPUT_FILE.split('/')[1].replace('.yml','')
    car_object = generate_car_object(detection_yaml, car_id, DETECTION_PATH)

    # write yml
    with open(OUTPUT_FILE, 'w') as file:
            documents = yaml.dump(car_object, file, sort_keys=False)

    print("splunk_security_content_to_car.py wrote CAR analytic to: {}".format(OUTPUT_FILE))

if __name__ == "__main__":

    # grab arguments
    parser = argparse.ArgumentParser(description="Generates CAR analytics file from Splunk Security Content Detections")
    parser.add_argument("-p", "--path", required=True, help="path to security_content detection, example: security_content/detections/endpoint/suspicious_mshta_child_process.yml")
    parser.add_argument("-o", "--output", required=True, help="file to write to the car analytics to, eg analytics/CAR-2021-04-001.yml")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="prints verbose output")

    # parse them
    args = parser.parse_args()
    DETECTION_PATH = args.path
    OUTPUT_FILE = args.output
    VERBOSE = args.verbose

    if VERBOSE:
        print("getting mitre enrichment data from cti")
    attack = Attck()

    generate_car_analytics(DETECTION_PATH, OUTPUT_FILE, attack, VERBOSE)
    print("finished successfully!")
