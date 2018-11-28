---
title: Sysmon (3.2)
---

- Manufacturer: Microsoft Corporation
- Version: 3.2
- Website: https://technet.microsoft.com/en-us/sysinternals/sysmon

## Description
Sysmon is a freely available program from Microsoft that is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.

## Data Model Coverage
### [driver](../data_model/driver)

| | `base_address` | `fqdn` | `hostname` | `image_path` |`md5_hash` | `module_name` | `sha1_hash` | `sha256_hash` |`signer` |
|---|---|---|---|---|---|---|---|---|---|
| `load` | |✓|✓ |✓ |✓|✓|✓|✓| |
| `unload` | | | | | | | | | |

### [file](../data_model/file)

| | `company` | `creation_time` | `file_name` | `file_path` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signer` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | | | | | | | | | | | | | | | |
| `delete` | | | | | | | | | | | | | | | |
| `modify` | | | | | | | | | | | | | | | |
| `read` | | | | | | | | | | | | | | | |
| `timestomp` | | ✓ | ✓ | | | ✓ | ✓ | | ✓ | | ✓ | | | | :✓|
| `write` | | | | | | | | | | | | | | | |

### [flow](../data_model/flow)

| | `content` | `dest_fqdn` | `dest_hostname` | `dest_ip` | `dest_port` | `end_time` | `exe` | `flags` | `fqdn` | `hostname` | `image_path` | `packet_count` | `pid` | `ppid` | `proto_info` | `protocol` | `src_fqdn` | `src_hostname` | `src_ip` | `src_port` | `start_time` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `end` | | | | | | | | | | | | | | | | | | | | | | |
| `message` | | | | | | | | | | | | | | | | | | | | | | |
| `start` | | | | ✓ | ✓ | | ✓ | | | ✓ | ✓ | | ✓ | | | ✓ | | | ✓ | ✓ | ✓ | ✓ |

### [module](../data_model/module)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `module_path` | `pid` | `sha1_hash` | `sha256_hash` | `signer` | `tid` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `load` | | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | | |
| `unload` | | | | | | | | | | | | |

### [process](../data_model/process)

| |`command_line` | `exe` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `parent_exe` | `parent_image_path` | `pid` | `ppid` | `sha1_hash` | `sha256_hash` | `sid` | `signer` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| `terminate` | | | ✓ | ✓ | | | | | ✓ | | | | | | ✓ |

### [thread](../data_model/thread)

| | `hostname` | `src_pid` | `src_tid` | `stack_base` | `stack_limit` | `start_address` | `start_function` | `start_module` | `start_module_name` | `subprocess_tag` | `tgt_pid` | `tgt_tid` | `user` | `user_stack_base` | `user_stack_limit` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | | | | | | | | | | | | | | | |
| `remote_create` | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | | |
| `suspend` | | | | | | | | | | | | | | | |
| `terminate` | | | | | | | | | | | | | | | |

## Analytic Coverage

 - [CAR-2013-02-003: Processes Spawning cmd.exe](../analytics/CAR-2013-02-003)
 - [CAR-2013-03-001: Reg.exe called from Command Shell](../analytics/CAR-2013-03-001)
 - [CAR-2013-04-002: Quick execution of a series of suspicious commands](../analytics/CAR-2013-04-002)
 - [CAR-2013-05-002: Suspicious Run Locations](../analytics/CAR-2013-05-002)
 - [CAR-2013-05-004: Execution with AT](../analytics/CAR-2013-05-004)
 - [CAR-2013-05-009: Running executables with same hash and different names](../analytics/CAR-2013-05-009)
 - [CAR-2013-07-001: Suspicious Arguments](../analytics/CAR-2013-07-001)
 - [CAR-2013-07-005: Command Line Usage of Archiving Software](../analytics/CAR-2013-07-005)
 - [CAR-2013-08-001: Execution with schtasks](../analytics/CAR-2013-08-001)
 - [CAR-2013-09-005: Service Outlier Executables](../analytics/CAR-2013-09-005)
 - [CAR-2013-10-002: DLL Injection via Load Library](../analytics/CAR-2013-10-002)
 - [CAR-2014-03-005: Remotely Launched Executables via Services](../analytics/CAR-2014-03-005)
 - [CAR-2014-03-006: RunDLL32.exe monitoring](../analytics/CAR-2014-03-006)
 - [CAR-2014-04-003: Powershell Execution](../analytics/CAR-2014-04-003)
 - [CAR-2014-05-001: RPC Activity](../analytics/CAR-2014-05-001)
 - [CAR-2014-05-002: Services launching Cmd](../analytics/CAR-2014-05-002)
 - [CAR-2014-07-001: Service Search Path Interception](../analytics/CAR-2014-07-001)
 - [CAR-2014-11-002: Outlier Parents of Cmd](../analytics/CAR-2014-11-002)
 - [CAR-2014-11-003: Debuggers for Accessibility Applications](../analytics/CAR-2014-11-003)
 - [CAR-2014-11-004: Remote PowerShell Sessions](../analytics/CAR-2014-11-004)
 - [CAR-2014-11-006: Windows Remote Management (WinRM)](../analytics/CAR-2014-11-006)
 - [CAR-2014-11-008: Command Launched from WinLogon](../analytics/CAR-2014-11-008)
 - [CAR-2016-03-001: Host Discovery Commands](../analytics/CAR-2016-03-001)
 - [CAR-2016-03-002: Create Remote Process via WMIC](../analytics/CAR-2016-03-002)