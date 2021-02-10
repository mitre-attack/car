---
title: "Data Model with Sensors"
---

The **Data Model**, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` act like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

Compare the data model's use in analytics that map to [ATT&CK](https://attack.mitre.org/).

## [authentication](authentication)

| | **ad_domain** | **app_name** | **auth_service** | **auth_target** | **decision_reason** | **fqdn** | **hostname** | **method** | **response_time** | **target_ad_domain** | **target_uid** | **target_user** | **target_user_role** | **target_user_type** | **uid** | **user** | **user_agent** | **user_role** | **user_type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **failure** | | | | | | | | | | | | | | | | | | | |
| **error** | | | | | | | | | | | | | | | | | | | |
| **success** | | | | | | | | | | | | | | | | | | | |

## [driver](driver)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **pid** | **sha1_hash** | **sha256_hash** | **signature_valid** | **signer** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | |
| **unload**| | | | | | | | | | | |

## [email](email)

| | **action_reason** | **attachment_mime_type** | **attachment_name** | **attachment_size** | **date** | **dest_address** | **dest_ip** | **dest_port** | **from** | **message_body** | **message_links** | **message_type** | **return_address** | **server_relay** | **smtp_uid** | **src_address** | **src_domain** | **src_ip** | **src_port** | **subject** | **to** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--|--|
| **block** | | | | | | | | | | | | | | | | | | | | | |
| **delete** | | | | | | | | | | | | | | | | | | | | | |
| **deliver** | | | | | | | | | | | | | | | | | | | | | |
| **redirect** | | | | | | | | | | | | | | | | | | | | | |
| **quarantine** | | | | | | | | | | | | | | | | | | | | | |

## [file](file)

| | **company** | **content** | **creation_time** | **file_extension** | **file_gid** | **file_group** | **file_name** | **file_path** | **file_uid** | **file_user** | **fqdn** | **hostname** | **image_path** | **link_target** | **md5_hash** | **mime_type** | **mode** | **pid** | **ppid** | **previous_creation_time** | **sha1_hash** | **sha256_hash** | **signature_valid** | **signer** | **uid** | **user** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | | | | [Autoruns](../sensors/autoruns) | [Sysmon](../sensors/sysmon_13) | | | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns) | [Sysmon](../sensors/sysmon_13) | | [Autoruns](../sensors/autoruns) | | | [Sysmon](../sensors/sysmon_13) | | | | | | [Sysmon](../sensors/sysmon_13) | |
| **delete** | | | | | | | | | | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | | | | | | | [Sysmon](../sensors/sysmon_13) | |
| **modify** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | [Autoruns](../sensors/autoruns) | | | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | | [Autoruns](../sensors/autoruns) | | | | | | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | |
| **read** | | | | | | | | | | | | | | | | | | | | | | | | | |
| **timestomp** | | | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | |
| **write** | | | | | | | | | | | | | | | | | | | | | | | | | |
| **acl_modify** | | | | | | | | | | | | | | | | | | | | | | | | | |

## [flow](flow)

| | **content** | **dest_fqdn** | **dest_hostname** | **dest_ip** | **dest_port** | **end_time** | **exe** | **fqdn** | **hostname** | **image_path** | **in_bytes** | **out_bytes** | **network_direction** | **packet_count** | **pid** | **ppid** | **proto_info** | **protocol** | **src_fqdn** | **src_hostname** | **src_ip** | **src_port** | **start_time** | **tcp_flags** | **transport_protocol** | **uid** | **user** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **end** | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **message** | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **start** | | | | [Sysmon (2.0)](../sensors/sysmon_2.0)| [Sysmon (2.0)](../sensors/sysmon_2.0) | | [Sysmon (2.0)](../sensors/sysmon_2.0) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)| [Sysmon (2.0)](../sensors/sysmon_2.0)| | [Sysmon (2.0)](../sensors/sysmon_2.0) | | | [Sysmon (2.0)](../sensors/sysmon_2.0) | | | [Sysmon (2.0)](../sensors/sysmon_2.0) | [Sysmon (2.0)](../sensors/sysmon_2.0) | [Sysmon (2.0)](../sensors/sysmon_2.0) | [Sysmon (2.0)](../sensors/sysmon_2.0) | | | | | |

## [module](module)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **module_path** | **pid** | **sha1_hash** | **sha256_hash** | **signature_valid** | **signer** | **tid** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) | [Sysmon (2.0)]( ../sensors/sysmon_2.0)  | [Sysmon (2.0)]( ../sensors/sysmon_2.0)  | [Sysmon (2.0)]( ../sensors/sysmon_2.0) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) | [Sysmon (2.0)]( ../sensors/sysmon_2.0)  | [Sysmon (2.0)]( ../sensors/sysmon_2.0) | | | |
| **unload** | | | | | | | | | | | | | |

## [process](process)

| | **access_level** | **call_trace** | **command_line** | **current_working_directory** | **exe** | **env_vars** | **fqdn** | **guid** | **hostname** | **image_path** | **integrity_level** | **md5_hash** | **parent_command_line** | **parent_exe** | **parent_guid** | **parent_image_path** | **pid** | **ppid** | **sha1_hash** | **sha256_hash** | **sid** | **signer** | **signature_valid** | **target_address** | **target_guid** | **target_pid** | **target_name** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **access** | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | | | | | [Sysmon](../sensors/sysmon_13) | | | | [Sysmon](../sensors/sysmon_13) | | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | |
**create** | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | | | | | | | | | | | | | |


## [registry](registry)

| | **data** | **fqdn** | **hostname** | **hive** | **key** | **image_path** | **new_content** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns)| [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns) |
|
**key_edit** | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns)<br />[Sysmon](../sensors/sysmon_13) |
| **remove** | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | |
| **value_edit** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns)| [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns)| | [Autoruns](../sensors/autoruns) |

## [service](service)

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **name** | **pid** | **ppid** | **uid** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | | | |
| **delete** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | | | |
| **pause** | | | | | | | | | | |
| **start** | | | | | | | | | | |
| **stop** | | | | | | | | | | |

## [socket](socket)

| | **family** | **image_path** | **local_address** | **local_path** | **local_port** | **pid** | **protocol** | **remote_address** | **remote_port** | **success** |
|---|---|---|---|---|---|---|---|---|---|---|
| **bind** | osquery | os_query | osquery | | osquery | osquery | osquery | osquery | osquery | |
| **listen** | osquery | osquery | osquery | | osquery | osquery| osquery | osquery | osquery | |
| **close** | osquery | osquery | osquery | | osquery | osquery| osquery | osquery | osquery | |

## [thread](thread)

| | **hostname** | **src_pid** | **src_tid** | **stack_base** | **stack_limit** | **start_address** | **start_function** | **start_module** | **start_module_name** | **subprocess_tag** | **tgt_pid** | **tgt_tid** | **uid** | **user** | **user_stack_base** | **user_stack_limit** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | | | | | | | | | | | | | | | | |
| **remote_create** | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | |[Sysmon]( ../sensors/sysmon_13) |[Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | |
| **suspend** | | | | | | | | | | | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | | |

## [user_session](user_session)

| | **hostname** | **src_pid** | **src_tid** | **stack_base** | **stack_limit** | **start_address** | **start_function** | **start_module** | **start_module_name** | **subprocess_tag** | **tgt_pid** | **tgt_tid** | **uid** | **user** | **user_stack_base** | **user_stack_limit** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | | | | | | | | | | | | | | | | |
| **remote_create** | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | |[Sysmon]( ../sensors/sysmon_13) |[Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | |
| **suspend** | | | | | | | | | | | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | | |
