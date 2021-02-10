---
title: "Sysmon (13.0)"
---

- Manufacturer: Microsoft
- Version: 13.0
- Website: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon


## Description
Sysmon is a freely available program from Microsoft that is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.



## Data Model Coverage

### [driver](../data_model/driver)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `pid` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` |
|---|---|---|---|---|---|---|---|---|---|---|
| `load` |  |✓| |✓|✓| | |✓|✓|✓|✓|
| `unload` |  | | | | | | | | | | |

### [file](../data_model/file)

| | `company` | `content` | `creation_time` | `file_extension` | `file_gid` | `file_group` | `file_name` | `file_path` | `file_uid` | `file_user` | `fqdn` | `hostname` | `image_path` | `link_target` | `md5_hash` | `mime_type` | `mode` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `acl_modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓| | | | |✓| | |✓| |✓| | | | |✓| | | | | | | | |
| `delete` |  | | | | | | |✓| | |✓| |✓| |✓| | |✓| | |✓|✓| | |✓|✓|
| `modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `read` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `timestomp` |  | |✓| | | | |✓| | |✓| |✓| | | | |✓| |✓| | | | | | |
| `write` |  | | | | | | | | | | | | | | | | | | | | | | | | | |

### [flow](../data_model/flow)

| | `application_protocol` | `content` | `dest_fqdn` | `dest_hostname` | `dest_ip` | `dest_port` | `end_time` | `exe` | `fqdn` | `hostname` | `image_path` | `in_bytes` | `network_direction` | `out_bytes` | `packet_count` | `pid` | `ppid` | `proto_info` | `sid` | `src_fqdn` | `src_hostname` | `src_ip` | `src_port` | `start_time` | `tcp_flags` | `transport_protocol` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `end` |  | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `message` |  | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `start` |  | |✓| |✓|✓| | |✓| |✓| | | | |✓| | | |✓| |✓|✓|✓| | |✓|

### [process](../data_model/process)

| | `access_level` | `call_trace` | `command_line` | `current_working_directory` | `env_vars` | `exe` | `fqdn` | `guid` | `hostname` | `image_path` | `integrity_level` | `md5_hash` | `parent_command_line` | `parent_exe` | `parent_guid` | `parent_image_path` | `pid` | `ppid` | `sha1_hash` | `sha256_hash` | `sid` | `signature_valid` | `signer` | `target_address` | `target_guid` | `target_name` | `target_pid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `access` |  | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓|✓| | |✓| | |✓|✓|✓|✓| | |✓|✓|✓| |✓|✓| | | | | | |✓|
| `terminate` |  | | | | | |✓| | |✓| | | | | | |✓| | | | | | | | | | | |

### [registry](../data_model/registry)

| | `data` | `fqdn` | `hive` | `hostname` | `image_path` | `key` | `new_content` | `pid` | `type` | `user` | `value` |
|---|---|---|---|---|---|---|---|---|---|---|
| `add` | ✓|✓|✓| |✓|✓| |✓| | |✓|
| `key_edit` |  |✓|✓| |✓|✓|✓|✓| | |✓|
| `remove` |  |✓|✓| |✓|✓| |✓| | |✓|
| `value_edit` |  |✓|✓| |✓|✓|✓|✓| | |✓|

### [thread](../data_model/thread)

| | `hostname` | `src_pid` | `src_tid` | `stack_base` | `stack_limit` | `start_address` | `start_function` | `start_module` | `start_module_name` | `tgt_pid` | `tgt_tid` | `uid` | `user` | `user_stack_base` | `user_stack_limit` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓|✓| | | |✓|✓|✓| |✓|✓|✓| | | |
| `remote_create` | ✓|✓| | | |✓|✓|✓| |✓|✓|✓| | | |
| `suspend` |  | | | | | | | | | | | | | | |
| `terminate` |  | | | | | | | | | | | | | | |




## Analytic Coverage

 - [CAR-2013-03-001: Reg.exe called from Command Shell](../analytics/CAR-2013-03-001)
 - [CAR-2013-04-002: Quick execution of a series of suspicious commands](../analytics/CAR-2013-04-002)
 - [CAR-2013-05-002: Suspicious Run Locations](../analytics/CAR-2013-05-002)
 - [CAR-2013-05-004: Execution with AT](../analytics/CAR-2013-05-004)
 - [CAR-2013-05-005: SMB Copy and Execution](../analytics/CAR-2013-05-005)
 - [CAR-2013-05-009: Running executables with same hash and different names](../analytics/CAR-2013-05-009)
 - [CAR-2013-07-001: Suspicious Arguments](../analytics/CAR-2013-07-001)
 - [CAR-2013-07-002: RDP Connection Detection](../analytics/CAR-2013-07-002)
 - [CAR-2013-07-005: Command Line Usage of Archiving Software](../analytics/CAR-2013-07-005)
 - [CAR-2013-08-001: Execution with schtasks](../analytics/CAR-2013-08-001)
 - [CAR-2013-09-005: Service Outlier Executables](../analytics/CAR-2013-09-005)
 - [CAR-2013-10-002: DLL Injection via Load Library](../analytics/CAR-2013-10-002)
 - [CAR-2014-02-001: Service Binary Modifications](../analytics/CAR-2014-02-001)
 - [CAR-2014-03-001: SMB Write Request - NamedPipes](../analytics/CAR-2014-03-001)
 - [CAR-2014-03-005: Remotely Launched Executables via Services](../analytics/CAR-2014-03-005)
 - [CAR-2014-03-006: RunDLL32.exe monitoring](../analytics/CAR-2014-03-006)
 - [CAR-2014-05-001: RPC Activity](../analytics/CAR-2014-05-001)
 - [CAR-2014-07-001: Service Search Path Interception](../analytics/CAR-2014-07-001)
 - [CAR-2014-11-003: Debuggers for Accessibility Applications](../analytics/CAR-2014-11-003)
 - [CAR-2014-11-006: Windows Remote Management (WinRM)](../analytics/CAR-2014-11-006)
 - [CAR-2014-12-001: Remotely Launched Executables via WMI](../analytics/CAR-2014-12-001)
 - [CAR-2016-03-001: Host Discovery Commands](../analytics/CAR-2016-03-001)
 - [CAR-2016-03-002: Create Remote Process via WMIC](../analytics/CAR-2016-03-002)
 - [CAR-2019-04-001: UAC Bypass](../analytics/CAR-2019-04-001)
 - [CAR-2019-04-002: Generic Regsvr32](../analytics/CAR-2019-04-002)
 - [CAR-2019-04-003: Squiblydoo](../analytics/CAR-2019-04-003)
 - [CAR-2019-04-004: Credential Dumping via Mimikatz](../analytics/CAR-2019-04-004)
 - [CAR-2019-07-002: Lsass Process Dump via Procdump](../analytics/CAR-2019-07-002)
 - [CAR-2019-08-001: Credential Dumping via Windows Task Manager](../analytics/CAR-2019-08-001)
 - [CAR-2019-08-002: Active Directory Dumping via NTDSUtil](../analytics/CAR-2019-08-002)
 - [CAR-2020-04-001: Shadow Copy Deletion](../analytics/CAR-2020-04-001)
 - [CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities](../analytics/CAR-2020-08-001)
 - [CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS](../analytics/CAR-2020-08-002)
 - [CAR-2020-09-001: Scheduled Task - FileAccess](../analytics/CAR-2020-09-001)
 - [CAR-2020-09-002: Component Object Model Hijacking](../analytics/CAR-2020-09-002)
 - [CAR-2020-09-003: Indicator Blocking - Driver Unloaded](../analytics/CAR-2020-09-003)
 - [CAR-2020-09-004: Credentials in Files & Registry](../analytics/CAR-2020-09-004)
 - [CAR-2020-09-005: AppInit DLLs](../analytics/CAR-2020-09-005)
 - [CAR-2020-11-001: Boot or Logon Initialization Scripts](../analytics/CAR-2020-11-001)
 - [CAR-2020-11-003: DLL Injection with Mavinject](../analytics/CAR-2020-11-003)
 - [CAR-2020-11-005: Clear Powershell Console Command History](../analytics/CAR-2020-11-005)
 - [CAR-2020-11-006: Local Permission Group Discovery](../analytics/CAR-2020-11-006)
 - [CAR-2020-11-007: Network Share Connection Removal](../analytics/CAR-2020-11-007)
 - [CAR-2020-11-008: MSBuild and msxsl](../analytics/CAR-2020-11-008)
 - [CAR-2020-11-011: Registry Edit from Screensaver](../analytics/CAR-2020-11-011)
 - [CAR-2021-01-001: Identifying Port scanning activity](../analytics/CAR-2021-01-001)
 - [CAR-2021-01-002: Unusually long command line strings](../analytics/CAR-2021-01-002)
