---
title: "osquery (4.1.2)"
---

- Manufacturer: osquery project
- Version: 4.1.2
- Website: https://osquery.io/


## Description
osquery exposes an operating system as a high-performance relational database. This allows you to write SQL-based queries to explore operating system data.



## Data Model Coverage

### [flow](../data_model/flow)

| | `application_protocol` | `content` | `dest_fqdn` | `dest_hostname` | `dest_ip` | `dest_port` | `end_time` | `exe` | `fqdn` | `hostname` | `image_path` | `in_bytes` | `network_direction` | `out_bytes` | `packet_count` | `pid` | `ppid` | `proto_info` | `src_fqdn` | `src_hostname` | `src_ip` | `src_port` | `start_time` | `tcp_flags` | `transport_protocol` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `end` |  | | | |✓|✓| | | | |✓| | | | |✓| | | | |✓|✓|✓| | | |✓|
| `message` |  | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `start` |  | | | |✓|✓| | | | |✓| | | | |✓| | | | |✓|✓|✓| | | |✓|

### [file](../data_model/file)

| | `company` | `content` | `creation_time` | `extension` | `file_name` | `file_path` | `fqdn` | `gid` | `group` | `hostname` | `image_path` | `link_target` | `md5_hash` | `mime_type` | `mode` | `owner` | `owner_uid` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `acl_modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓| |✓|✓| | | | |✓| |✓| | | | |✓|✓| |✓|✓| | | |✓|
| `delete` |  | |✓| |✓|✓| | | | |✓| |✓| | | | |✓|✓| |✓|✓| | | |✓|
| `modify` |  | |✓| |✓|✓| | | | |✓| |✓| | | | |✓|✓| |✓|✓| | | |✓|
| `read` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `timestomp` |  | |✓| |✓|✓| | | | |✓| |✓| | | | |✓|✓| |✓|✓| | | |✓|
| `write` |  | |✓| |✓|✓| | | | |✓| |✓| | | | |✓|✓| |✓|✓| | | |✓|

### [process](../data_model/process)

| | `access_level` | `call_trace` | `command_line` | `current_working_directory` | `env_vars` | `exe` | `fqdn` | `guid` | `hostname` | `image_path` | `integrity_level` | `md5_hash` | `parent_command_line` | `parent_exe` | `parent_guid` | `parent_image_path` | `pid` | `ppid` | `sha1_hash` | `sha256_hash` | `sid` | `signature_valid` | `signer` | `target_address` | `target_guid` | `target_name` | `target_pid` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `access` |  | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` |  | |✓|✓| |✓| | | |✓| |✓| | | | |✓|✓|✓|✓| | | | | | | | |✓|
| `terminate` |  | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

### [driver](../data_model/driver)

| | `base_address` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `module_name` | `pid` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` |
|---|---|---|---|---|---|---|---|---|---|---|
| `load` |  | | |✓|✓|✓| |✓|✓| | |
| `unload` |  | | | | | | | | | | |




## Analytic Coverage

 - [CAR-2013-02-003: Processes Spawning cmd.exe](../analytics/CAR-2013-02-003)
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
 - [CAR-2014-02-001: Service Binary Modifications](../analytics/CAR-2014-02-001)
 - [CAR-2014-03-001: SMB Write Request - NamedPipes](../analytics/CAR-2014-03-001)
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
 - [CAR-2014-12-001: Remotely Launched Executables via WMI](../analytics/CAR-2014-12-001)
 - [CAR-2016-03-001: Host Discovery Commands](../analytics/CAR-2016-03-001)
 - [CAR-2016-03-002: Create Remote Process via WMIC](../analytics/CAR-2016-03-002)
 - [CAR-2016-04-002: User Activity from Clearing Event Logs](../analytics/CAR-2016-04-002)
 - [CAR-2019-04-001: UAC Bypass](../analytics/CAR-2019-04-001)
 - [CAR-2019-04-002: Generic Regsvr32](../analytics/CAR-2019-04-002)
 - [CAR-2019-04-003: Squiblydoo](../analytics/CAR-2019-04-003)
 - [CAR-2019-07-002: Lsass Process Dump via Procdump](../analytics/CAR-2019-07-002)
 - [CAR-2019-08-001: Credential Dumping via Windows Task Manager](../analytics/CAR-2019-08-001)
 - [CAR-2019-08-002: Active Directory Dumping via NTDSUtil](../analytics/CAR-2019-08-002)
 - [CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities](../analytics/CAR-2020-08-001)
 - [CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS](../analytics/CAR-2020-08-002)
 - [CAR-2020-09-001: Scheduled Task - FileAccess](../analytics/CAR-2020-09-001)
 - [CAR-2020-09-002: Component Object Model Hijacking](../analytics/CAR-2020-09-002)
 - [CAR-2020-09-003: Indicator Blocking - Driver Unloaded](../analytics/CAR-2020-09-003)
 - [CAR-2020-09-004: Credentials in Files & Registry](../analytics/CAR-2020-09-004)
 - [CAR-2020-09-005: AppInit DLLs](../analytics/CAR-2020-09-005)
 - [CAR-2020-11-001: Boot or Logon Initialization Scripts](../analytics/CAR-2020-11-001)
 - [CAR-2020-11-002: Local Network Sniffing](../analytics/CAR-2020-11-002)
 - [CAR-2020-11-003: DLL Injection with Mavinject](../analytics/CAR-2020-11-003)
 - [CAR-2020-11-004: Processes Started From Irregular Parent](../analytics/CAR-2020-11-004)
 - [CAR-2020-11-005: Clear Powershell Console Command History](../analytics/CAR-2020-11-005)
 - [CAR-2020-11-006: Local Permission Group Discovery](../analytics/CAR-2020-11-006)
 - [CAR-2020-11-007: Network Share Connection Removal](../analytics/CAR-2020-11-007)
 - [CAR-2020-11-008: MSBuild and msxsl](../analytics/CAR-2020-11-008)
 - [CAR-2020-11-009: Compiled HTML Access](../analytics/CAR-2020-11-009)
 - [CAR-2020-11-010: CMSTP](../analytics/CAR-2020-11-010)
 - [CAR-2020-11-011: Registry Edit from Screensaver](../analytics/CAR-2020-11-011)
 - [CAR-2021-01-001: Identifying Port Scanning Activity](../analytics/CAR-2021-01-001)
 - [CAR-2021-01-002: Unusually Long Command Line Strings](../analytics/CAR-2021-01-002)
 - [CAR-2021-01-003: Clearing Windows Logs with Wevtutil](../analytics/CAR-2021-01-003)
 - [CAR-2021-01-004: Unusual Child Process for Spoolsv.Exe or Connhost.Exe](../analytics/CAR-2021-01-004)
 - [CAR-2021-01-006: Unusual Child Process spawned using DDE exploit](../analytics/CAR-2021-01-006)
 - [CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt](../analytics/CAR-2021-01-007)
 - [CAR-2021-01-008: Disable UAC](../analytics/CAR-2021-01-008)
 - [CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize](../analytics/CAR-2021-01-009)
 - [CAR-2021-02-001: Webshell-Indicative Process Tree](../analytics/CAR-2021-02-001)
 - [CAR-2021-02-002: Get System Elevation](../analytics/CAR-2021-02-002)
 - [CAR-2021-04-001: Common Windows Process Masquerading](../analytics/CAR-2021-04-001)
 - [CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store](../analytics/CAR-2021-05-001)
 - [CAR-2021-05-002: Batch File Write to System32](../analytics/CAR-2021-05-002)
 - [CAR-2021-05-003: BCDEdit Failure Recovery Modification](../analytics/CAR-2021-05-003)
 - [CAR-2021-05-004: BITS Job Persistence](../analytics/CAR-2021-05-004)
 - [CAR-2021-05-005: BITSAdmin Download File](../analytics/CAR-2021-05-005)
 - [CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments](../analytics/CAR-2021-05-006)
 - [CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments](../analytics/CAR-2021-05-007)
 - [CAR-2021-05-008: Certutil exe certificate extraction](../analytics/CAR-2021-05-008)
 - [CAR-2021-05-009: CertUtil With Decode Argument](../analytics/CAR-2021-05-009)
 - [CAR-2021-05-010: Create local admin accounts using net exe](../analytics/CAR-2021-05-010)
 - [CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0](../analytics/CAR-2021-11-001)
 - [CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify](../analytics/CAR-2021-11-002)
 - [CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths](../analytics/CAR-2021-12-001)
 - [CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'](../analytics/CAR-2021-12-002)
 - [CAR-2022-03-001: Disable Windows Event Logging](../analytics/CAR-2022-03-001)
 - [N/A](../analytics/N/A)
