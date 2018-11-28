---
title: "Registry"
---

The registry is a system-defined database in which applications and system components store and retrieve configuration data. The data stored in the registry varies according to the version of Microsoft Windows. Applications use the registry API to retrieve, modify, or delete registry data.

## Actions

|Action|Description|
|---|---|
|add|The event corresponding to the act of adding a registry key, hive, type, or value.|
|edit|The event corresponding to the act of modifying an existing registry key, hive, type, or value.
|remove|The event corresponding to the act of deleting an existing registry key, hive, type, or value.

## Fields

|Field|Description|Example|
|---|---|---|
|hostname|The hostname of the host, without the domain.|`HOST1`
|key|The registry key of the event. Similar to a folder in a traditional file system,|`HKLM\SYSTEM\CurrentControlSet\services\RpcSs`
|value|The descriptive name for the data being stored.|`InstalledVersion`
|data|The content, typically a text string.|`%SystemRoot%\system32\svchost.exe -k rpcss`
|type|Registry value types indicate the type of data being stored. Types include binary data, 32 bit numbers, strings, etc.|`REG_SZ`,`REG_MULTI_SZ`,`REG_DWORD`,`REG_BINARY`,`REG_QWORD`,`REG_EXPAND_SZ`
|hive|The logical group of keys, subkeys, and values in the registry.|`HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE`
|image_path|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.
|pid|Inherited from the [process](https://car.mitre.org/wiki/Data_Model/process) that made the registry access.
|fqdn|The fully qualified domain name for the host on which the registry access took place.
|user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.

## Coverage Map

| | **data** | **fqdn** | **hive** | **hostname** | **image_path** | **key** | **pid** | **type** | **user** | **value** |
|---|---|---|---|---|---|---|---|---|---|---|
| **add** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) |
| **edit** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | [Autoruns](https://car.mitre.org/wiki/Autoruns) |
| **remove** | | | | | | | | | | |