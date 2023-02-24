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
data|The content of `value`, typically a text string.|\%SystemRoot%\system32\svchost.exe -k rpcss
fqdn|The fully qualified domain name for the host on which the registry access took place.|HOST1.EXAMPLE_DOMAIN.COM
hive|The logical group of keys, subkeys, and values in the registry.|HKEY_CURRENT_USER
hostname|The hostname of the host, without the domain.|HOST1
image_path|Inherited from the [process](https://car.mitre.org/data_model/process) that made the registry access.|C:\path\to\example.exe
key|The registry key of the event. Similar to a folder in a traditional file system.|HKLM\SYSTEM\CurrentControlSet\services\RpcSs
new_content|The data within the new value, or the new name of a key, after an edit event.|\%SystemRoot%\system32\svchost.exe, HKLM\SYSTEM\CurrentControlSet\services\RpcSs
pid|Inherited from the [process](https://car.mitre.org/data_model/process) that made the registry access.|738
type|The type of data being stored in `value`. Types include binary data, 32 bit numbers, strings, etc.|REG_BINARY
user|The user in the context of the process that performed the action on the registry key.|HOST1\LOCALUSER
value|The descriptive name for the data being stored.|InstalledVersion

## Coverage Map
<table>
  <thead>
    <tr>
      <th />
      <th>data</th>
      <th>fqdn</th>
      <th>hive</th>
      <th>hostname</th>
      <th>image_path</th>
      <th>key</th>
      <th>new_content</th>
      <th>pid</th>
      <th>type</th>
      <th>user</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    
    <tr>
      <td>add</td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
    </tr>
    
    <tr>
      <td>key_edit</td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
    </tr>
    
    <tr>
      <td>remove</td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
    </tr>
    
    <tr>
      <td>value_edit</td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
      <td style="white-space: pre-wrap;"></td>
    </tr>
    
  </tbody>
</table>