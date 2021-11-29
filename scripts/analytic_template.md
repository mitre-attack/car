---
title: "{{analytic['id']}}: {{analytic['title']}}"
layout: analytic
submission_date: {{analytic['submission_date']}}
information_domain: {{analytic['information_domain']}}
subtypes: {{analytic['subtypes']|join(', ')}}
analytic_type: {{analytic['analytic_types']|join(', ')}}
contributors: {{analytic['contributors']|join(', ')}}
{% if 'platforms' in analytic %}applicable_platforms: {{analytic['platforms']|join(', ')}}{% else %}applicable_platforms: N/A{% endif %}
---

{{analytic['description']}}
{% if 'references' in analytic %}
#### References
{{ analytic['references']|join("\n") }}
{% endif %}
{% if 'coverage' in analytic %}
### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|{% for coverage_item in analytic['coverage'] %}
|[{{techniques[coverage_item['technique']]}}](https://attack.mitre.org/techniques/{{coverage_item['technique']}}/)|{% if 'subtechniques' in coverage_item %}{% for subtechnique in coverage_item['subtechniques'] %}[{{techniques[subtechnique]}}](https://attack.mitre.org/techniques/{{subtechnique | replace(".","/")}}/){% if not loop.last %}, {% endif %}{% endfor %}{% else %}N/A{% endif %}|{% for tactic in coverage_item['tactics'] %}[{{tactics[tactic]}}](https://attack.mitre.org/tactics/{{tactic}}/){% if not loop.last %}, {% endif %}{% endfor %}|{{coverage_item['coverage']}}|{% endfor %}{% endif %}

{% if 'd3fend_mappings' in analytic %}
### D3FEND Techniques

|ID|Name|
|---|---|{% for dtech in analytic['d3fend_mappings'] %} 
|{{dtech.id}} | [{{dtech.label}}](https://d3fend.mitre.org/technique/{{dtech.iri}})| {% endfor %}
{% endif %}

{% if 'data_model_references' in analytic %}
### Data Model References

|Object|Action|Field|
|---|---|---|
{% for dmr in analytic['data_model_references'] %}|[{{dmr[0]}}](/data_model/{{dmr[0]}}) | [{{dmr[1]}}](/data_model/{{dmr[0]}}#{{dmr[1]}}) | [{{dmr[2]}}](/data_model/{{dmr[0]}}#{{dmr[2]}}) |
{% endfor %}{% endif %}
{% if 'implementations' in analytic %}

### Applicable Sensors


### Implementations
{% for impl in analytic['implementations'] %}
{% if 'name' in impl %}#### {{impl['name']}} ({{impl['type']|capitalize}}{% if 'data_model' in impl %}, {{impl['data_model']}}{% endif %})
{% else %}#### {{impl['type']|capitalize}}{% if 'data_model' in impl %}, {{impl['data_model']}}{% endif %}{% endif %}
{% if 'description' in impl %}
{{impl['description']}}
{% endif %}
{% if 'code' in impl %}
```
{{impl['code']}}
```
{% endif %}
{% endfor %}{% endif %}
{% if 'unit_tests' in analytic %}
### Unit Tests
{% for ut in analytic['unit_tests'] %}
#### Test Case {{loop.index}}
{% if 'configurations' in ut %}
**Configurations:** {{ut['configurations']|join(', ')}}
{% endif %}{% if 'description' in ut %}
{{ut['description']}}{% endif %}
{% if 'commands' in ut %}
```
{{ut['commands']|join("\n")}}
```
{% endif %}{% endfor %}{% endif %}

{% if 'true_positives' in analytic %}
### True Positives
{% for tp in analytic['true_positives'] %}
#### {{tp['source']|capitalize}}
{% if 'description' in tp %}
{{tp['description']}}
{% endif %}
{% if 'full_event' in tp %}
##### [Full Event](/true_positives/{{tp['full_event']}})
{% endif %}
{% if 'event_snippet' in tp %}
##### Event Snippet
```json
{% include tp['event_snippet'] %}
```
{% endif %}
{% endfor %}{% endif %}
