---
title: "{{sensor['sensor_name']}} ({{sensor['sensor_version']}})"
---

- Manufacturer: {{sensor['sensor_developer']}}
- Version: {{sensor['sensor_version']}}
- Website: {{sensor['sensor_url']}}

{% if 'sensor_description' in sensor %}
## Description
{{ sensor['sensor_description']}}
{% endif %}

{% if 'data_model_coverage' in sensor %}
## Data Model Coverage
{% for coverage in sensor['data_model_coverage'] %}
{{coverage}}
{%- endfor %}
{% endif %}

{% if 'analytic_coverage' in sensor %}
## Analytic Coverage
{% for analytic in sensor['analytic_coverage'] %}
 - [{{analytic['full_title']}}](../analytics/{{analytic['id']}})
{%- endfor %}
{% endif %}
