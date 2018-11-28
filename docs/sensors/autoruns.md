---
title: Autoruns
---

- Manufacturer: Microsoft Corporation
- Version: 13.2
- Website: https://technet.microsoft.com/en-us/sysinternals/bb963902.aspx

## Description
This utility shows the user what programs are configured to run during system bootup or login, and/or on execution of various built-in Windows applications like Internet Explorer, Explorer and media players. These programs and drivers include ones in your startup folder, Run, RunOnce, and other Registry keys. Autoruns reports Explorer shell extensions, toolbars, browser helper objects, Winlogon notifications, auto-start services, etc.

## Data Model Coverage

### [file](../data_model/file)

| | `company` | `creation_time` | `file_name` | `file_path` | `fqdn` | `hostname` | `image_path` | `md5_hash` | `pid` | `ppid` | `previous_creation_time` | `sha1_hash` | `sha256_hash` | `signer` | `user` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓ | ✓ | ✓ | | ✓ | ✓ | | ✓ | | | | | | | |
| `delete` | | | | | | | | | | | | | | | |
| `modify` | ✓ | ✓ | ✓ | | ✓ | ✓ | | ✓ | | | | ✓ | ✓ | ✓ | |
| `read` | | | | | | | | | | | | | | | |
| `timestomp` | | | | | | | | | | | | | | | |
| `write` | | | | | | | | | | | | | | | |


### [registry](../data_model/registry)

| | `data` | `fqdn` | `hive` | `hostname` | `image_path` | `key` | `pid` | `type` | `user` | `value` |
|---|---|---|---|---|---|---|---|---|---|---|
| `add` | ✓ | | ✓ | ✓ | | ✓ | | ✓ | | ✓ |
| `edit` | ✓ | | ✓ | ✓ | | ✓ | | ✓ | | ✓ |
| `remove` | | | | | | | | | | |


### [service](../service)

| | `command_line` | `exe` | `fqdn` | `hostname` | `image_path` | `name` | `pid`| `ppid` | `user` |
|---|---|---|---|---|---|---|---|---|---|
| `create` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| `delete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| `pause` | | | | | | | | | |
| `start` | | | | | | | | | |
| `stop` | | | | | | | | | |


## Analytic Coverage

 - [CAR-2013-01-002: Autorun Differences](../analytics/CAR-2013-01-002)

