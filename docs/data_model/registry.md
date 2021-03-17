---
title: "Registry"
---

The registry is a system-defined database in which applications and system components store and retrieve configuration data. The data stored in the registry varies according to the version of Microsoft Windows. Applications use the registry API to retrieve, modify, or delete registry data.

## Actions

|Action|Description|
|---|---|
|add|The event corresponding to the act of adding a registry key, hive, type, or value.|
|name_edit|The event corresponding to the act of editing the name of an existing registry key or value.|
|remove|The event corresponding to the act of deleting an existing registry key, hive, type, or value.|
|value_edit|The event corresponding to the act of editing the contents of an existing registry value.|

## Fields

|Field|Description|Example|
|---|---|---|
|fqdn|The fully qualified domain name for the host on which the registry access took place.|`host1.example.net`|
|hostname|The hostname of the host, without the domain.|`HOST1`|
|hive|The logical group of keys, subkeys, and values in the registry.|`HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE`
|key|The registry key specified in the event. Similar to a folder in a traditional file system,|`HKLM\SYSTEM\CurrentControlSet\services\RpcSs`|
|image_path|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.|`C:\Windows\System32\cmd.exe`|
|new_content|The data within the new value, or the new name of a key or value, after an edit event.|`\%SystemRoot%\system32\svchost.exe, HKLM\SYSTEM\CurrentControlSet\services\RpcSs`|
|pid|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.|`1337`|
|user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.| |
|value|The descriptive name for the data being stored in the key.|`InstalledVersion`|
|value_data|The contents of the value, typically a text string.|`%SystemRoot%\system32\svchost.exe -k rpcss`|
|value_type|The type of data being stored in the value. Types include binary data, 32 bit numbers, strings, etc.|`REG_SZ`,`REG_MULTI_SZ`,`REG_DWORD`,`REG_BINARY`,`REG_QWORD`,`REG_EXPAND_SZ`|

## Coverage Map

| | **data** | **fqdn** | **hostname** | **hive** | **key** | **image_path** | **new_content** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98)| [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98) | 
| 
**key_edit** | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98) | [Sysmon](../sensors/sysmon_13) | [Autoruns](../sensors/autoruns_13.98)< /br>[Sysmon](../sensors/sysmon_13) |
| **remove** | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | 
| **value_edit** | [Autoruns](../sensors/autoruns_13.98) | | [Autoruns](../sensors/autoruns_13.98)| [Autoruns](../sensors/autoruns_13.98) | [Autoruns](../sensors/autoruns_13.98) | | [Autoruns](../sensors/autoruns_13.98) | | [Autoruns](../sensors/autoruns_13.98)| | [Autoruns](../sensors/autoruns_13.98) | 
