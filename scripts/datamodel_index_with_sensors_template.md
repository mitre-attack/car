---
title: "Data Model with Sensors"
---

The **Data Model**, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` act like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

Compare the data model's use in analytics that map to [ATT&CK](https://attack.mitre.org/).

{% for model_name, model in datamodels.items()|sort(attribute='0') %}
## [{{ model_name }}]({{ model_name }})

<table>
  <tr>
    <th />{% for field in model['fields']|sort(attribute='name') %}
    <th>{{ field['name'] }}</th>{% endfor %}
  </tr>{% for action in model['actions']|sort(attribute='name') %}
  <tr>
    <th>{{ action['name'] }}</th>{% for field in model['fields']|sort(attribute='name') %}
    <td style="white-space: pre-wrap;">{% if 'coverage_map' in model and action['name'] in model['coverage_map'] and field['name'] in model['coverage_map'][action['name']] %}{{ model['coverage_map'][action['name']][field['name']]|join('&#10') }}{% endif %}</td>{% endfor %}
  </tr>{% endfor %}
</table>
{% endfor %}
