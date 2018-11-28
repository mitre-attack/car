---
title: "Data Model with Sensors"
---

The **Data Model**, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object on can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` act like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

Compare the data model's use in analytics that map to [ATT&CK](https://attack.mitre.org/).

## [driver](driver)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **sha1_hash** | **sha256_hash** | **signer** |
|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | |
| **unload** | | | | | | | | | |

## [file](file)

| | **company** | **creation_time** | **file_name** | **file_path** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **pid** | **ppid** | **previous_creation_time** | **sha1_hash** | **sha256_hash** | **signer** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | | | | |
| **delete** | | | | | | | | | | | | | | | |
| **modify** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | |
| **read** | | | | | | | | | | | | | | | |
| **timestomp** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) |
| **write** | | | | | | | | | | | | | | | |

## [flow](flow)

| | **content** | **dest_fqdn** | **dest_hostname** | **dest_ip** | **dest_port** | **end_time** | **exe** | **flags** | **fqdn** | **hostname** | **image_path** | **packet_count** | **pid** | **ppid** | **proto_info** | **protocol** | **src_fqdn** | **src_hostname** | **src_ip** | **src_port** | **start_time** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **end** | | | | | | | | | | | | | | | | | | | | | | |
| **message** | | | | | | | | | | | | | | | | | | | | | | |
| **start** | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) |

## [module](module)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **module_path** | **pid** | **sha1_hash** | **sha256_hash** | **signer** | **tid** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | |
| **unload** | | | | | | | | | | | | |

## [process](process)

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **parent_exe** | **parent_image_path** | **pid** | **ppid** | **sha1_hash** | **sha256_hash** | **sid** | **signer** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) |
| **terminate** | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0) [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) |



## [registry](registry)

| | **data** | **fqdn** | **hive** | **hostname** | **image_path** | **key** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) |
| **edit** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) |
| **remove** | | | | | | | | | | |

## [service](service)

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **name** | **pid** | **ppid** | **user** |
|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | | |
| **delete** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | | |
| **pause** | | | | | | | | | |
| **start** | | | | | | | | | |
| **stop** | | | | | | | | | |

## [thread](thread)

| | **hostname** | **src_pid** | **src_tid** | **stack_base** | **stack_limit** | **start_address** | **start_function** | **start_module** | **start_module_name** | **subprocess_tag** | **tgt_pid** | **tgt_tid** | **user** | **user_stack_base** | **user_stack_limit** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | | | | | | | | | | | | | | | |
| **remote_create** | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | [Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | |[Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) |[Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2)|[Sysmon (3.1)]( ../sensors/sysmon_3.1) [Sysmon (3.2)]( ../sensors/sysmon_3.2) | | |
| **suspend** | | | | | | | | | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | |

## [user_session](user_session)

| | **dest_ip** | **dest_port** | **hostname** | **logon_id** | **src_ip** | **src_port** | **user** |
|---|---|---|---|---|---|---|---|
| **interactive** | | | | | | | |
| **local** | | | | | | | |
| **lock** | | | | | | | |
| **login** | | | | | | | |
| **logout** | | | | | | | |
| **rdp** | | | | | | | |
| **reconnect** | | | | | | | |
| **remote** | | | | | | | |
| **unlock** | | | | | | | |