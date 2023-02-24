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
{{ field['name'] }}|{{ field['description'] }}|{% if 'example' in field %}<code>{{ field['example'] }}</code>{% endif %}{% endfor %}

## Coverage Map
<table>
  <tr>
    <th />{% for field in datamodel['fields']|sort(attribute='name') %}
    <th>{{ field['name'] }}</th>{% endfor %}
  </tr>{% for action in datamodel['actions']|sort(attribute='name') %}
  <tr>
    <th>{{ action['name'] }}</th>{% for field in datamodel['fields']|sort(attribute='name') %}
    <td style="white-space: pre-wrap;">{% if 'coverage_map' in datamodel and action['name'] in datamodel['coverage_map'] and field['name'] in datamodel['coverage_map'][action['name']] %}{{ datamodel['coverage_map'][action['name']][field['name']]|join('&#10') }}{% endif %}</td>{% endfor %}
  </tr>{% endfor %}
</table>
