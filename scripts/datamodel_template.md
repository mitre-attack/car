---
title: "{{ datamodel['name'] }}"
---
{{ datamodel['description'] }}

## Actions
|Action|Description|
|---|---|{% for action in datamodel['actions']|sort(attribute='name') %}
|{{ action['name'] }}|{{ action['description'] }}|{% endfor %}

## Fields
|Field|Description|Example|
|---|---|---|{% for field in datamodel['fields']|sort(attribute='name') %}
{{ field['name'] }}|{{ field['description'] }}|{% if 'example' in field %}{{ field['example'] }}{% endif %}{% endfor %}

## Coverage Map
<table>
  <tr>
    <th />{% for field in datamodel['fields']|sort(attribute='name') %}
    <th>{{ field['name'] }}</th>{% endfor %}
  </tr>{% for action in datamodel['actions']|sort(attribute='name') %}
  <tr>
    <td>{{ action['name'] }}</td>{% for field in datamodel['fields']|sort(attribute='name') %}
    <td style="white-space: pre-wrap;">{% if 'coverage_map' in datamodel and 'action' in datamodel['coverage_map'] and 'field' in datamodel['coverage_map']['action'] %}{{ datamodel['coverage_map'][action][field]|join('&#10') }}{% endif %}</td>{% endfor %}
  </tr>{% endfor %}
</table>
