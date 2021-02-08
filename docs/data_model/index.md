---
title: Data Model
---

The Data Model, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object on can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` acts like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

## Summary

|Object|Actions|Fields|
|---|---|---|
|**[authentication](driver)**|`error`<br />`failure`<br />`success`|`ad_domain`<br />`app_name`<br />`auth_service`<br />`auth_target`<br />`decision_reason`<br />`fqdn`<br />`hostname`<br />`fqdn`<br />`method`<br />`response_time`<br />`target_ad_domain`<br />`target_uid`<br />`target_user`<br />`target_user_role`<br />`target_user_type`<br />`uid`br />`user`<br />`user_agent`<br />`user_role`|
|**[driver](driver)**|`load`<br />`unload`|`base_address`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`module_name`<br />`pid`>br />`sha1_hash`<br />`sha256_hash`<br />`signer`<br />`signature_valid`|
|**[email](email)**|`block`<br />`delete`<br />`deliver`<br />`redirect`<br />`quarantine`|`action_reason`<br />`attachment_mime_type`<br />`attachment_name`<br />`attachment_size`<br />`date`<br />`dest_address`<br />`dest_ip`<br />`dest_port`<br />`from`<br />`message_body`<br />`message_links`<br />`message_type`<br />`return_address`<br />`server_relay`<br />`smtp_uid`<br />`src_address`<br />`src_domain`br />`src_ip`<br />`src_port`<br />`subject`<br />`to`<br />`target_type`|
|**[file](file)**|`acl_modify`<br />`create`<br />`delete`<br />`modify`<br />`read`<br />`timestomp`<br />`write`|`content`<br />`company`<br />`creation_time`<br />`file_name`<br />`file_path`<br />`file_uid`<br />`file_user`<br />`file_extension`<br />`file_gid`<br />`file_gid`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`link_target`<br />`md5_hash`<br />`mime_type`<br />`pid`<br />`ppid`<br />`previous_creation_time`<br />`sha1_hash`<br />`sha256_hash`<br />`signer`<br />`signature_valid`<br />`uid`<br />`user`|
|**[flow](flow)**|`end`<br />`message`<br />`start`|`application_protocol`<br />`content`<br />`dest_fqdn`<br />`dest_hostname`<br />`dest_ip`<br />`dest_port`<br />`end_time`<br />`exe`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`in_bytes`<br />`network_direction`<br />`out_bytes`<br />`packet_count`<br />`pid`<br />`ppid`<br />`proto_info`<br />`protocol`<br />`src_fqdn`<br />`src_hostname`<br />`src_ip`<br />`src_port`<br />`start_time`<br />`tcp_flags`<br />`transport_protocol`<br />`uid`<br />`user`|
|**[module](module)**|`load`<br />`unload`|`base_address`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`md5_hash`<br />`module_name`<br />`module_path`<br />`pid`<br />`sha1_hash`<br />`sha256_hash`<br />`signer`<br />`tid`<br />`signature_valid`|
|**[process](process)**|`access`<br />`create`<br />`current_working_directory`<br />`terminate`|`call_trace`<br />`command_line`<br />`env_vars`<br />`exe`<br />`fqdn`<br />`guid`<br />`hostname`<br />`integrity_level`<br />`image_path`<br />`md5_hash`<br />`parent_command_line`<br />`parent_exe`<br />`parent_guid`<br />`parent_image_path`<br />`pid`<br />`ppid`<br />`sha1_hash`<br />`sha256_hash`<br />`sid`<br />`signature_valid`<br />`signer`<br />`target_guid`<br />`target_pid`<br />`target_address`<br />`taget_name`<br />`uid`<br />`user`|
|**[registry](registry)**|`add`<br />`remove`<br />`key_edit`<br />`value_edit`|`data`<br />`fqdn`<br />`hive`<br />`hostname`<br />`image_path`<br />`key`<br />`pid`<br />`new_content`<br />`type`<br />`user`<br />`value`|
|**[service](service)**|`create`<br />`delete`<br />`pause`<br />`start`<br />`stop`|`command_line`<br />`exe`<br />`fqdn`<br />`hostname`<br />`image_path`<br />`name`<br />`pid`<br />`ppid`<br />`uid`<br />`user`|
|**[thread](thread)**|`create`<br />`remote_create`<br />`suspend`<br />`terminate`|`hostname`<br />`src_pid`<br />`src_tid`<br />`stack_base`<br />`stack_limit`<br />`start_address`<br />`start_function`<br />`start_module`<br />`start_module_name`<br />`subprocess_tag`<br />`tgt_pid`<br />`tgt_tid`<br />`uid`<br />`user`<br />`user_stack_base`<br />`user_stack_limit`|
|**[user_session](user_session)**|`lock`<br />`login`<br />`logout`<br />`reconnect`<br />`unlock`|`dest_ip`<br />`dest_port`<br />`hostname`<br />`login_type`<br />`logon_id`<br />`login_successful`<br />`src_ip`<br />`src_port`<br />`uid`<br />`user`|

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
