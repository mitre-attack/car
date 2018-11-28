---
title: Data Model
---

The Data Model, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object on can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` acts like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

## Summary

|Object|Actions|Fields|
|---|---|---|
|**[driver](driver)**|`load`<br />`unload`|`base_address`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`module_name`<br />`sha1_hash`<br />`sha256_hash`<br />`signer`|
|**[file](file)**|`create`<br />`delete`<br />`modify`<br />`read`<br />`timestomp`<br />`write`|`company`<br />`creation_time`<br />`file_name`<br />`file_path`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`pid`<br />`ppid`<br />`previous_creation_time`<br />`sha1_hash`<br />`sha256_hash`<br />`signer`<br />`user`|
|**[flow](flow)**|`end`<br />`message`<br />`start`|`content`<br />`dest_fqdn`<br />`dest_hostname`<br />`dest_ip`<br />`dest_port`<br />`end_time`<br />`exe`<br />`flags`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`packet_count`<br />`pid`<br />`ppid`<br />`proto_info`<br />`protocol`<br />`src_fqdn`<br />`src_hostname`<br />`src_ip`<br />`src_port`<br />`start_time`<br />`user`|
|**[module](module)**|`load`<br />`unload`|`base_address`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`module_name`<br />`module_path`<br />`pid`<br />`sha1_hash`<br />`sha256_hash`<br />`signer`<br />`tid`|
|**[process](process)**|`create`<br />`terminate`|`command_line`<br />`exe`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`parent_exe`<br />`parent_image_path`<br />`pid`<br />`ppid`<br />`sha1_hash`<br />`sha256_hash`<br />`sid`<br />`signer`<br />`user`|
|**[registry](registry)**|`add`<br />`edit`<br />`remove`|`data`<br />`fqdn`<br />`hive`<br />`hostname`<br />`image_path`<br />`key`<br />`pid`<br />`type`<br />`user`<br />`value`|
|**[service](service)**|`create`<br />`delete`<br />`pause`<br />`start`<br />`stop`|`command_line`<br />`exe`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`name`<br />`pid`<br />`ppid`<br />`user`|
|**[thread](thread)**|`create`<br />`remote_create`<br />`suspend`<br />`terminate`|`hostname`<br />`src_pid`<br />`src_tid`<br />`stack_base`<br />`stack_limit`<br />`start_address`<br />`start_function`<br />`start_module`<br />`start_module_name`<br />`subprocess_tag`<br />`tgt_pid`<br />`tgt_tid`<br />`user`<br />`user_stack_base`<br />`user_stack_limit`|
|**[user_session](user_session)**|`interactive`<br />`local`<br />`lock`<br />`login`<br />`logout`<br />`rdp`<br />`reconnect`<br />`remote`<br />`unlock`|`dest_ip`<br />`dest_port`<br />`hostname`<br />`logon_id`<br />`src_ip`<br />`src_port`<br />`user`|

## What is the data model?

### Objects
In the Data Model an *object* is much like an [object in computer science](https://en.wikipedia.org/wiki/Object_(computer_science)). These are the items that data actually represent, such as hosts, files, connections, etc. Objects are the nouns of the Data Model vocabulary.

### Actions
An *action* refers to a state change or event that happens on an object, such as an object's creation, destruction, or modification. These are the verbs that describe that an object can do, and what can happen to an object. However, there are cases where sensors do not monitor actions in objects but merely scan for and check the presence of an object. Each action is represented in a coverage matrix (the 2D table). The actions are on the y-axis.

### Fields
A *field* refers to the observable properties of an object. These properties may contain flags, identifiers, data elements, or even references to other objects. In terms of vocabulary, fields are like the adjectives. They describe properties about an object. A [sensor](../Glossary#Sensor) monitors fields in the context of an object, and outputs these in some form of structured data. Once the data is ingested into a [SIEM](https://en.wikipedia.org/wiki/SIEM), the logs can be queried by forcing restrictions or patterns upon one or more objects, such as in an [analytic](../Glossary#Analytic). On the coverage matrix fields are on the x-axis.

### Coverage
In order to gauge the usefulness of a sensor with respect to analytics, its output must be mapped into the Data Model. For each object that a sensor measures, it captures state. Some sensors periodically scan for objects, instead of monitoring for state changes. In these cases, state may be inferred by looking for changes in the properties of an object.

A summary of data model coverage is [here](data_model_with_sensors).