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

## Data Model Coverage


{% if 'analytic_coverage' in sensor %}
## Analytic Coverage
{% for analytic in sensor['analytic_coverage'] %}
 - [{{analytic['full_title']}}](../analytics/{{analytic['id']}})
{%- endfor %}
{% endif %}
