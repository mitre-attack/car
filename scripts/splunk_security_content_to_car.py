import argparse

def generate_car_analytics(DETECTION_PATH, OUTPUT_DIR, ANALYTICS_TEMPLATE_PATH, attack, messages, VERBOSE):

    if VERBOSE:
        print("reading splunk security content detection: {0}".format(DETECTION_PATH))

    detection_yaml = dict()

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

    generate_car_analytics(DETECTION_PATH, OUTPUT_DIR, ANALYTICS_TEMPLATE_PATH, attack, messages, VERBOSE)
    print("finished successfully!")
