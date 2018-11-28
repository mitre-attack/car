# Data Model with Sensors
The **Data Model**, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object on can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` act like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

Compare the data model's use in analytics that map to [ATT&CK](https://attack.mitre.org/).

## [driver](driver.md)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **sha1_hash** | **sha256_hash** | **signer** |
|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | |
| **unload** | | | | | | | | | |

## [file](file.md)

| | **company** | **creation_time** | **file_name** | **file_path** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **pid** | **ppid** | **previous_creation_time** | **sha1_hash** | **sha256_hash** | **signer** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | | | | | | |
| **delete** | | | | | | | | | | | | | | | |
| **modify** | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | | | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | |
| **read** | | | | | | | | | | | | | | | |
| **timestomp** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |
| **write** | | | | | | | | | | | | | | | |

## [flow](flow.md)

| | **content** | **dest_fqdn** | **dest_hostname** | **dest_ip** | **dest_port** | **end_time** | **exe** | **flags** | **fqdn** | **hostname** | **image_path** | **packet_count** | **pid** | **ppid** | **proto_info** | **protocol** | **src_fqdn** | **src_hostname** | **src_ip** | **src_port** | **start_time** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **end** | | | | | | | | | | | | | | | | | | | | | | |
| **message** | | | | | | | | | | | | | | | | | | | | | | |
| **start** | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |

## [module](module.md)

| | **base_address** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **module_name** | **module_path** | **pid** | **sha1_hash** | **sha256_hash** | **signer** | **tid** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **load** | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | |
| **unload** | | | | | | | | | | | | |

## [process](process.md)

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **parent_exe** | **parent_image_path** | **pid** | **ppid** | **sha1_hash** | **sha256_hash** | **sid** | **signer** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |
| **terminate** | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |



## [registry](registry.md)

| | **data** | **fqdn** | **hive** | **hostname** | **image_path** | **key** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) |
| **edit** | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) | | [Autoruns](../sensors/autoruns.md) |
| **remove** | | | | | | | | | | |

## [service](service.md)

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **name** | **pid** | **ppid** | **user** |
|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | | |
| **delete** | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | [Autoruns](../sensors/autoruns.md) | | | |
| **pause** | | | | | | | | | |
| **start** | | | | | | | | | |
| **stop** | | | | | | | | | |

## [thread](thread.md)

| | **hostname** | **src_pid** | **src_tid** | **stack_base** | **stack_limit** | **start_address** | **start_function** | **start_module** | **start_module_name** | **subprocess_tag** | **tgt_pid** | **tgt_tid** | **user** | **user_stack_base** | **user_stack_limit** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | | | | | | | | | | | | | | | |
| **remote_create** | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | |[Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |[Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md)|[Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | |
| **suspend** | | | | | | | | | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | |

## [user_session](user_session.md)

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