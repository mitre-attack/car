# This script creates a SPL saved search configuration file from the current set of CAR analytics
# Usage: python3 generate_splunk_savedsearches.py
# Creates a savedsearches.conf file in the /scripts directory
import yaml, sys, os

# Template for use in generating the saved Searches 
search_template = '''[{0}]
action.email.useNSSubject = 1
alert.track = 0
description = "{1}"
display.general.type = statistics
display.page.search.tab = statistics
display.visualizations.show = 0
display.visualizations.type = custom
request.ui_dispatch_app = search
request.ui_dispatch_view = search
search = {2}

'''

# This assumes that this script is executed directly from its parent 'scripts' directory
yamlDir = "../analytics/"
out_file = open("savedsearches.conf", "w")
for root, dirs, files in os.walk(yamlDir):
    for file in files:
        if file.endswith(".yaml"):
            print('Generating saved search for {0}...'.format(file))
            yaml_file = open(os.path.join(root, file), 'r')
            car_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            # File name has the correct formatting so use that for the name of the saved search
            name = "{0} - {1}".format(car_data["id"],car_data["title"])
            # Determine if the analytic has a Splunk implementation
            splunk_search = ""
            if "implementations" in car_data:
                for impl in car_data["implementations"]:
                    if impl["type"] == "Splunk":
                        splunk_search = impl["code"]
            # Write it to the file
            if splunk_search:
                out_file.write(search_template.format(name, car_data["description"], splunk_search))
            else:
                print("No Splunk implementation found, skipping...")
print("Wrote to: {0}".format(out_file.name))
out_file.flush()
out_file.close()