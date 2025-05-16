---
title: "Autoruns (13.98)"
---

- Manufacturer: Microsoft
- Version: 13.98
- Website: https://technet.microsoft.com/en-us/sysinternals/bb963902.aspx


## Description
Autoruns reports Explorer shell extensions, toolbars, browser helper objects, Winlogon notifications, auto-start services, etc.at is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.



## Data Model Coverage

### [file](../data_model/file)

| | `company` | `content` | `creation_time` | `extension` | `file_name` | `file_path` | `fqdn` | `gid` | `group` | `hostname` | `image_path` | `link_target` | `md5_hash` | `mime_type` | `mode` | `owner` | `owner_uid` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signature_valid` | `signer` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `acl_modify` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `create` | ✓| |✓| |✓|✓|✓| | |✓|✓| |✓| | | | | | | |✓|✓| |✓| | |
| `delete` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `modify` | ✓| |✓| |✓|✓|✓| | |✓|✓| |✓| | | | | | | |✓|✓| |✓| | |
| `read` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `timestomp` |  | | | | | | | | | | | | | | | | | | | | | | | | | |
| `write` |  | | | | | | | | | | | | | | | | | | | | | | | | | |

### [registry](../data_model/registry)

| | `data` | `fqdn` | `hive` | `hostname` | `image_path` | `key` | `new_content` | `pid` | `type` | `user` | `value` |
|---|---|---|---|---|---|---|---|---|---|---|
| `add` | ✓|✓|✓|✓| |✓| | |✓| |✓|
| `key_edit` | ✓|✓|✓|✓| |✓|✓| |✓| |✓|
| `remove` |  | | | | | | | | | | |
| `value_edit` | ✓|✓|✓|✓| |✓|✓| |✓| |✓|

### [service](../data_model/service)

| | `command_line` | `exe` | `fqdn` | `hostname` | `image_path` | `name` | `pid` | `ppid` | `uid` | `user` |
|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓|✓|✓|✓|✓|✓| | | | |
| `delete` | ✓|✓|✓|✓|✓|✓| | | | |
| `pause` |  | | | | | | | | | |
| `start` |  | | | | | | | | | |
| `stop` |  | | | | | | | | | |




## Analytic Coverage

 - [CAR-2013-01-002: Autorun Differences](../analytics/CAR-2013-01-002)
 - [CAR-2014-02-001: Service Binary Modifications](../analytics/CAR-2014-02-001)
 - [CAR-2019-08-001: Credential Dumping via Windows Task Manager](../analytics/CAR-2019-08-001)
 - [CAR-2019-08-002: Active Directory Dumping via NTDSUtil](../analytics/CAR-2019-08-002)
 - [CAR-2020-09-001: Scheduled Task - FileAccess](../analytics/CAR-2020-09-001)
 - [CAR-2020-09-002: Component Object Model Hijacking](../analytics/CAR-2020-09-002)
 - [CAR-2020-09-005: AppInit DLLs](../analytics/CAR-2020-09-005)
 - [CAR-2020-11-001: Boot or Logon Initialization Scripts](../analytics/CAR-2020-11-001)
 - [CAR-2020-11-011: Registry Edit from Screensaver](../analytics/CAR-2020-11-011)
 - [CAR-2021-02-002: Get System Elevation](../analytics/CAR-2021-02-002)
 - [CAR-2021-05-002: Batch File Write to System32](../analytics/CAR-2021-05-002)
 - [CAR-2021-05-012: Create Service In Suspicious File Path](../analytics/CAR-2021-05-012)
 - [CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0](../analytics/CAR-2021-11-001)
 - [CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify](../analytics/CAR-2021-11-002)
 - [CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'](../analytics/CAR-2021-12-002)
 - [CAR-2022-03-001: Disable Windows Event Logging](../analytics/CAR-2022-03-001)
