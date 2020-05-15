---
title: "Sysmon (11.0)"
---

- Manufacturer: Microsoft
- Version: 11.0
- Website: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon


## Description
Sysmon is a freely available program from Microsoft that is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.



## Data Model Coverage

### [thread](../data_model/thread)

| | `hostname` | `src_pid` | `src_tid` | `stack_base` | `stack_limit` | `start_address` | `start_function` | `start_module` | `start_module_name` | `tgt_pid` | `tgt_tid` | `user` | `user_stack_base` | `user_stack_limit` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓|✓| | | |✓|✓|✓| |✓|✓| | | |
| `remote_create` | ✓|✓| | | |✓|✓|✓| |✓|✓| | | |
| `suspend` |  | | | | | | | | | | | | | |
| `terminate` |  | | | | | | | | | | | | | |

### [registry](../data_model/registry)

| | `data` | `fqdn` | `hive` | `hostname` | `image_path` | `key` | `pid` | `type` | `user` | `value` |
|---|---|---|---|---|---|---|---|---|---|
| `add` |  |✓|✓| |✓|✓|✓| | |✓|
| `edit` |  |✓|✓| |✓|✓|✓| | |✓|
| `remove` |  |✓|✓| |✓|✓|✓| | |✓|

### [file](../data_model/file)

| | `company` | `creation_time` | `file_name` | `file_path` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signer` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` |  |✓| |✓|✓| |✓| |✓| | | | | | |
| `delete` |  | | |✓|✓| |✓|✓|✓| | |✓|✓| |✓|
| `modify` |  | | | | | | | | | | | | | | |
| `read` |  | | | | | | | | | | | | | | |
| `timestomp` |  |✓| |✓|✓| |✓| |✓| |✓| | | | |
| `write` |  | | | | | | | | | | | | | | |

### [driver](../data_model/driver)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `sha1_hash` | `sha256_hash` | `signer` |
|---|---|---|---|---|---|---|---|---|
| `load` |  |✓| |✓|✓| |✓|✓|✓|
| `unload` |  | | | | | | | | |

### [module](../data_model/module)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `module_path` | `pid` | `sha1_hash` | `sha256_hash` | `signer` | `signer` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `load` |  |✓| |✓|✓| |✓|✓|✓|✓|✓| |
| `unload` |  | | | | | | | | | | | |

### [flow](../data_model/flow)

| | `content` | `dest_fqdn` | `dest_hostname` | `dest_ip` | `dest_port` | `end_time` | `exe` | `flags` | `fqdn` | `hostname` | `image_path` | `packet_count` | `pid` | `ppid` | `proto_info` | `protocol` | `src_fqdn` | `src_hostname` | `src_ip` | `src_port` | `start_time` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `end` |  | | | | | | | | | | | | | | | | | | | | | |
| `message` |  | | | | | | | | | | | | | | | | | | | | | |
| `start` |  |✓| |✓|✓| | | |✓| |✓| |✓| | |✓|✓| |✓|✓|✓|✓|

### [process](../data_model/process)

| | `command_line` | `current_working_directory` | `exe` | `fqdn` | `hostname` | `image_path` | `integrity_level` | `md5_hash` | `parent_command_line` | `parent_exe` | `parent_image_path` | `pid` | `ppid` | `sha1_hash` | `sha256_hash` | `sid` | `signer` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓|✓| |✓| |✓|✓|✓|✓| |✓|✓|✓|✓|✓| |✓|✓|
| `terminate` |  | | |✓| |✓| | | | | |✓| | | | | | |




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
