"""
This script generates the data model portion of the site for each YAML data model mapping file.
"""
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from yaml import safe_load

def parse_yaml():
    datamodel_files = (Path(__file__).parents[1] / "data_model").glob("*.yaml")
    datamodels = {}
    for file in datamodel_files:
        with open(file, encoding="utf-8") as f:
            datamodels[file.stem] = safe_load(f.read())
    return datamodels

def cached_load_sensor():
  sensors = {}
  def load_sensor(filename):
      if filename not in sensors:
          sensor_file = Path(__file__).parents[1] / "sensors" / f"{filename}.yaml"
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

def create_jinja_environment():
    def backtick_wrapper_filter(value):
        return f'`{value}`'

    # autoescape set to false since it's needed to have the html links be generated properly and cause the templates / input data are controlled by us
    jinja_env = Environment(loader=FileSystemLoader('.'), autoescape=False)
    jinja_env.filters['backtick'] = backtick_wrapper_filter

    return jinja_env

def generate_markdown(datamodels, jinja_env):
    datamodel_template = jinja_env.get_template('datamodel_template.md')
    for model in datamodels:
        with open(f'../docs/data_model/{model}.md', 'w', encoding='utf-8') as f:
            f.write(datamodel_template.render(datamodel=datamodels[model]))

def generate_index(datamodels, jinja_env):
    index_template = jinja_env.get_template('datamodel_index_template.md')
    with open('../docs/data_model/index.md', 'w', encoding='utf-8') as f:
        f.write(index_template.render(datamodels=datamodels))

def generate_index_with_sensors(datamodels, jinja_env):
    index_template = jinja_env.get_template('datamodel_index_with_sensors_template.md')
    with open('../docs/data_model/data_model_with_sensors.md', 'w', encoding='utf-8') as f:
        f.write(index_template.render(datamodels=datamodels))

def main():
    datamodels = parse_yaml()
    replace_sensor_names_with_html(datamodels, cached_load_sensor())
    Path('../docs/data_model').mkdir(exist_ok=True)
    jinja_env = create_jinja_environment()
    generate_markdown(datamodels, jinja_env)
    generate_index(datamodels, jinja_env)
    generate_index_with_sensors(datamodels, jinja_env)

if __name__ == "__main__":
    main()
