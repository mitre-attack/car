"""This script generates the sensor portion of the site, including coverage,
for each YAML sensor mapping file.

TBD: generate automatic data model coverage in MD. Right now this is manual,
and is waiting on the YAMLization of the data model before this can happen.
"""

import json
import glob
import yaml
from os import path, makedirs
from jinja2 import Template
from operator import itemgetter


# Get all analytics and load as list of dicts
analytics_files = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "*.yaml"))
analytics = [yaml.load(open(analytic_file).read()) for analytic_file in analytics_files]

# Get all sensor mappings and load as a list of dicts
mapping_files = glob.glob(path.join(path.dirname(__file__), "..", "docs", "sensors", "*.yaml"))
mappings = [yaml.load(open(mapping_file).read()) for mapping_file in mapping_files]

# Parse each analytic to find its data model references (if any)
analytics_refs = {}
for analytic in analytics:
  if 'data_model_references' in analytic:
    analytic_tag = analytic['id'] + ": " + analytic['title']
    analytics_refs[analytic_tag] = analytic['data_model_references']

# Parse each mapping and build up the "simplified" string representation
# e.g., process/create/parent_exe
sensor_mappings = {}
for sensor in mappings:
    sensor_tag = sensor['sensor_name'] + " " + str(sensor['sensor_version'])
    simplified_mappings = []
    for mapping in sensor['mappings']:
      mapping_str = mapping['object'] + "/" + mapping["action"] + "/{0}"
      for field in mapping['fields']:
        simplified_mappings.append(mapping_str.format(field))
    sensor['simplified_mappings'] = simplified_mappings

# Compare the analytic data model refs to the sensor mappings
# to find the coverage of each sensor
for sensor in mappings:
  if 'simplified_mappings' in sensor:
    analytic_coverage = []
    for analytic, refs in analytics_refs.items():
      intersection = list(set(sensor['simplified_mappings']) & set(refs))
      if intersection:
        analytic_dict = {'id': analytic.split(':')[0],
                         'full_title': analytic}
        analytic_coverage.append(analytic_dict)
    if analytic_coverage:
      if 'other_coverage' in sensor:
          for coverage in sensor['other_coverage']:
               analytic_dict = {'id': coverage.split(':')[0],
                                'full_title': coverage}
               analytic_coverage.append(analytic_dict)
      newlist = sorted(analytic_coverage, key=itemgetter('id'))
      sensor['analytic_coverage'] = newlist

# Get the template file for the sensor page. Note that this is a markdown template which will be rendered by GH Pages.
sensor_template = Template(open('sensor_template.md').read())

# Generate the sensor page for each sensor
for sensor in mappings:
  sensor_tag = sensor['sensor_name'] + "_" + str(sensor['sensor_version'])
  # Generate the markdown
  markdown = sensor_template.render(sensor=sensor)
  # Save to the sensors directory
  open('../docs/sensors/{}.md'.format(sensor_tag.lower()), 'w').write(markdown)