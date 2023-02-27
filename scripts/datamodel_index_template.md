---
title: Data Model
---

The Data Model, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object on can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` acts like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

## Summary

|Object|Actions|Fields|
|---|---|---|{% for model_name, model in datamodels.items()|sort(attribute='0') %}
|**[{{ model_name }}]({{ model_name }})**|{{ model['actions']|sort(attribute='name')|map(attribute='name')|map('backtick')|join('<br />') }}|{{ model['fields']|sort(attribute='name')|map(attribute='name')|map('backtick')|join('<br />') }}|{% endfor %}

## What is the data model?

### Objects
In the Data Model an *object* is much like an [object in computer science](https://en.wikipedia.org/wiki/Object_(computer_science)). These are the items that data actually represent, such as hosts, files, connections, etc. Objects are the nouns of the Data Model vocabulary.

### Actions
An *action* refers to a state change or event that happens on an object, such as an object's creation, destruction, or modification. These are the verbs that describe that an object can do, and what can happen to an object. However, there are cases where sensors do not monitor actions in objects but merely scan for and check the presence of an object. Each action is represented in a coverage matrix (the 2D table). The actions are on the y-axis.

### Fields
A *field* refers to the observable properties of an object. These properties may contain flags, identifiers, data elements, or even references to other objects. In terms of vocabulary, fields are like the adjectives. They describe properties about an object. A [sensor](../resources/glossary#Sensor) monitors fields in the context of an object, and outputs these in some form of structured data. Once the data is ingested into a [SIEM](https://en.wikipedia.org/wiki/SIEM), the logs can be queried by forcing restrictions or patterns upon one or more objects, such as in an [analytic](../resources/glossary#Analytic). On the coverage matrix fields are on the x-axis.

### Coverage
In order to gauge the usefulness of a sensor with respect to analytics, its output must be mapped into the Data Model. For each object that a sensor measures, it captures state. Some sensors periodically scan for objects, instead of monitoring for state changes. In these cases, state may be inferred by looking for changes in the properties of an object.

A summary of data model coverage is [here](data_model_with_sensors).
