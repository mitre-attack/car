---
title: "Registry"
---

The registry is a system-defined database in which applications and system components store and retrieve configuration data. The data stored in the registry varies according to the version of Microsoft Windows. Applications use the registry API to retrieve, modify, or delete registry data.

## Actions

|Action|Description|
|---|---|
|add|The event corresponding to the act of adding a registry key, hive, type, or value.|
|key_edit|The event corresponding to the act of editing the name of an existing registry key.|
|remove|The event corresponding to the act of deleting an existing registry key, hive, type, or value.|
|value_edit|The event corresponding to the act of editing the content of an existing registry value.|

## Fields

|Field|Description|Example|
|---|---|---|
|data|The content, typically a text string.|`%SystemRoot%\system32\svchost.exe -k rpcss`|
|fqdn|The fully qualified domain name for the host on which the registry access took place.| |
|hostname|The hostname of the host, without the domain.|`HOST1`|
|hive|The logical group of keys, subkeys, and values in the registry.|`HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE`
|key|The registry key of the event. Similar to a folder in a traditional file system,|`HKLM\SYSTEM\CurrentControlSet\services\RpcSs`|
|image_path|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.| |
|new_content|The data within the new value, or the new name of a key, after an edit event.|`\%SystemRoot%\system32\svchost.exe, HKLM\SYSTEM\CurrentControlSet\services\RpcSs`|
|pid|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.| |
|type|Registry value types indicate the type of data being stored. Types include binary data, 32 bit numbers, strings, etc.|`REG_SZ`,`REG_MULTI_SZ`,`REG_DWORD`,`REG_BINARY`,`REG_QWORD`,`REG_EXPAND_SZ`|
|user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.| |
|value|The descriptive name for the data being stored.|`InstalledVersion`|

## Coverage Map

| | **data** | **fqdn** | **hostname** | **hive** | **key** | **image_path** | **new_content** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) |
| **key_edit** | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | |
| **remove** | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) |
| **value_edit** | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) |
