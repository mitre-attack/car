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
data|The content of `value`, typically a text string.|<code>\%SystemRoot%\system32\svchost.exe -k rpcss</code>
fqdn|The fully qualified domain name for the host on which the registry access took place.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
hive|The logical group of keys, subkeys, and values in the registry.|<code>HKEY_CURRENT_USER</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|Inherited from the [process](https://car.mitre.org/data_model/process) that made the registry access.|<code>C:\path\to\example.exe</code>
key|The registry key of the event. Similar to a folder in a traditional file system.|<code>HKLM\SYSTEM\CurrentControlSet\services\RpcSs</code>
new_content|The data within the new value, or the new name of a key, after an edit event.|<code>\%SystemRoot%\system32\svchost.exe, HKLM\SYSTEM\CurrentControlSet\services\RpcSs</code>
pid|Inherited from the [process](https://car.mitre.org/data_model/process) that made the registry access.|<code>738</code>
type|The type of data being stored in `value`. Types include binary data, 32 bit numbers, strings, etc.|<code>REG_BINARY</code>
user|The user in the context of the process that performed the action on the registry key.|<code>HOST1\LOCALUSER</code>
value|The descriptive name for the data being stored.|<code>InstalledVersion</code>

## Coverage Map
<table>
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
  <tr>
    <th>add</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
  </tr>
  <tr>
    <th>key_edit</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
  <tr>
    <th>remove</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>value_edit</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
  </tr>
</table>