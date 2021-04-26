import argparse
import yaml
from pyattck import Attck

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

    print(detection_yaml)

if __name__ == "__main__":

    # grab arguments
    parser = argparse.ArgumentParser(description="Generates CAR analytics file from Splunk Security Content Detections")
    parser.add_argument("-p", "--path", required=True, help="path to security_content detection, example: security_content/detections/endpoint/suspicious_mshta_child_process.yml")
    parser.add_argument("-o", "--output", required=True, help="path to the output directory for the docs")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="prints verbose output")

    # parse them
    args = parser.parse_args()
    DETECTION_PATH = args.path
    OUTPUT_DIR = args.output
    VERBOSE = args.verbose

    ANALYTICS_TEMPLATE_PATH = 'scripts/analytic_template.md'

    if VERBOSE:
        print("getting mitre enrichment data from cti")
    attack = Attck()

    generate_car_analytics(DETECTION_PATH, OUTPUT_DIR, ANALYTICS_TEMPLATE_PATH, attack, VERBOSE)
    print("finished successfully!")
