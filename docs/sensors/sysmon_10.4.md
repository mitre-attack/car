---
title: "Sysmon (10.4)"
---

- Manufacturer: Microsoft
- Version: 10.4
- Website: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon


## Description
Sysmon is a freely available program from Microsoft that is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.



## Data Model Coverage

### [thread](../data_model/thread)

| | `hostname` | `src_pid` | `src_tid` | `stack_base` | `stack_limit` | `start_address` | `start_function` | `start_module` | `start_module_name` | `tgt_pid` | `tgt_tid` | `uid` | `user` | `user_stack_base` | `user_stack_limit` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓|✓| | | |✓|✓|✓| |✓|✓| | | | |
| `remote_create` | ✓|✓| | | |✓|✓|✓| |✓|✓| | | | |
| `suspend` |  | | | | | | | | | | | | | | |
| `terminate` |  | | | | | | | | | | | | | | |

### [flow](../data_model/flow)

| | `application_protocol` | `content` | `dest_fqdn` | `dest_hostname` | `dest_ip` | `dest_port` | `end_time` | `exe` | `fqdn` | `hostname` | `image_path` | `in_bytes` | `network_direction` | `out_bytes` | `packet_count` | `pid` | `ppid` | `proto_info` | `src_fqdn` | `src_hostname` | `src_ip` | `src_port` | `start_time` | `tcp_flags` | `transport_protocol` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `end` |  | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `message` |  | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `start` |  | | |✓|✓|✓| | | | |✓| | | | |✓| | | |✓|✓|✓|✓| | | |✓|

### [process](../data_model/process)

| | `access_level` | `call_trace` | `command_line` | `current_working_directory` | `env_vars` | `exe` | `fqdn` | `guid` | `hostname` | `image_path` | `integrity_level` | `md5_hash` | `parent_command_line` | `parent_exe` | `parent_guid` | `parent_image_path` | `pid` | `ppid` | `sha1_hash` | `sha256_hash` | `sid` | `signature_valid` | `signer` | `target_address` | `target_guid` | `target_name` | `target_pid` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `access` |  | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓|✓| | |✓| | |✓|✓|✓|✓| | |✓|✓|✓|✓|✓| | | | | | | | |✓|
| `terminate` |  | | | | | |✓| | |✓| | | | | | |✓| | | | | | | | | | | | |

### [registry](../data_model/registry)

| | `data` | `fqdn` | `hive` | `hostname` | `image_path` | `key` | `new_content` | `pid` | `type` | `user` | `value` |
|---|---|---|---|---|---|---|---|---|---|---|
| `add` |  |✓|✓| |✓|✓| |✓| | |✓|
| `key_edit` |  | | | | | | | | | | |
| `remove` |  |✓|✓| |✓|✓| |✓| | |✓|
| `value_edit` |  | | | | | | | | | | |

### [file](../data_model/file)

| | `company` | `content` | `creation_time` | `file_extension` | `file_gid` | `file_group` | `file_name` | `file_path` | `file_uid` | `file_user` | `fqdn` | `hostname` | `image_path` | `link_target` | `md5_hash` | `mime_type` | `mode` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `acl_modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓| | | |✓| | | |✓| |✓| | | | |✓| | | | | | | | |
| `delete` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `read` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `timestomp` |  | |✓| | | |✓| | | |✓| |✓| | | | |✓| |✓| | | | | | |
| `write` |  | | | | | | | | | | | | | | | | | | | | | | | | | |

### [driver](../data_model/driver)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `pid` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` |
|---|---|---|---|---|---|---|---|---|---|---|
| `load` |  |✓| |✓|✓| | |✓|✓| |✓|
| `unload` |  | | | | | | | | | | |




## Analytic Coverage

 - [CAR-2019-04-004: Credential Dumping via Mimikatz](../analytics/CAR-2019-04-004)
 - [CAR-2020-11-001: Boot or Logon Initialization Scripts](../analytics/CAR-2020-11-001)
 - [CAR-2020-11-003: DLL Injection with Mavinject](../analytics/CAR-2020-11-003)
 - [CAR-2020-11-005: Clear Powershell Console Command History](../analytics/CAR-2020-11-005)
 - [CAR-2020-11-006: Local Permission Group Discovery](../analytics/CAR-2020-11-006)
 - [CAR-2020-11-007: Network Share Connection Removal](../analytics/CAR-2020-11-007)
 - [CAR-2020-11-008: MSBuild and msxsl](../analytics/CAR-2020-11-008)
 - [CAR-2020-11-011: CMSTP](../analytics/CAR-2020-11-011)
