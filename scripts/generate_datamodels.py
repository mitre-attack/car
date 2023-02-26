"""
This script generates the data model portion of the site for each YAML data model mapping file.
"""
from glob import glob
from jinja2 import Template
from os import path
from pathlib import Path
from yaml import safe_load

def parse_yaml():
    datamodel_files = glob(path.join(path.dirname(__file__), "..", "data_model", "*.yaml"))
    datamodels = {}
    for file in datamodel_files:
        with open(file, encoding="utf-8") as f:
            datamodels[Path(file).stem] = safe_load(f.read())
    return datamodels

def cached_load_sensor():
  sensors = {}
  def load_sensor(filename):
      if filename not in sensors:
          sensor_file = path.join(path.dirname(__file__), "..", "sensors", f"{filename}.yaml")
          with open(sensor_file, encoding="utf-8") as f:
              sensors[filename] = safe_load(f.read())
      return sensors[filename]
  return load_sensor

def replace_sensor_names_with_html(datamodels, load_sensor):
    def replace_sensor_name_with_html(sensor_filename):
        return f"<a href='../sensors/{sensor_filename}'>{load_sensor(sensor_filename)['sensor_name']}</a>"

    for model in datamodels.values():
        if 'coverage_map' in model:
            for action in model['coverage_map']:
                for field, sensor_filenames in model['coverage_map'][action].items():
                    model['coverage_map'][action][field] = [replace_sensor_name_with_html(sensor_filename) for sensor_filename in sensor_filenames]

def generate_markdown(datamodels):
    with open('datamodel_template.md') as f:
        datamodel_template = Template(f.read())
    for model in datamodels:
        with open(f'../docs/data_model/{model}.md', 'w', encoding='utf-8') as f:
            f.write(datamodel_template.render(datamodel=datamodels[model]))

def main():
    datamodels = parse_yaml()
    load_sensor = cached_load_sensor()
    replace_sensor_names_with_html(datamodels, load_sensor)
    generate_markdown(datamodels)

if __name__ == "__main__":
    main()
