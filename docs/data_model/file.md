---
title: "File"
---

A resource for storing information available to a computer program.

## Actions

|Action|Description|
|---|---|
|timestomp|The modification of an attribute, such as creation time. The file metadata may change, but the contents of the file remain the same.|
|create|The event corresponding to the creation of a file.|
|delete|The event corresponding to the deletion of a file.|
|modify|The event corresponding to the modification of a file or its metadata.|
|read|The event corresponding to the accessing of a file to be read.|
|write|The event corresponding to the accessing of a file in order to write new instructions or information into a file.|

## Fields

|Field|Description|Example|
|---|---|---|
|creation_time|The creation time of the file as described in UTC and including the date.|`05/14/2015 12:47:06`|
|file_name|The name of the file.|`MyWordDoc.docx`|
|fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`|
|hostname|The hostname of the host, without the domain.|`HOST1`|
|image_path|The file system location of the executable that is associated with the `pid` that generated this event.|`C:\Windows\system32\notepad.exe`|
|md5_hash|An MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|`5eb63bbbe01eeed093cb22bb8f5acdc3`|
|pid|The process ID for the process that generated this file event, represented in decimal notation.|`738`|
|ppid|The process ID of the parent process of the process associated with this file event, represented in decimal notation.|`1860`|
|previous_creation_time|The creation_time associated with the file before it was changed for this file event.|`05/14/2015 12:47:06`|
|signer|The company listed on the certificate of the program at `image_path` if that program is signed.|`Microsoft |Corporation`
|sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|`2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`|
|sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|`68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728`|
|user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.|`HOST1\LOCALUSER`|
|company|The name of the organization listed in the file located at `image_path`.
|file_path|The full path to the file.|`C:\users\fakeuser\documents\MyFile.docx`|

## Coverage Map

| | **company** | **creation_time** | **file_name** | **file_path** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **pid** | **ppid** | **previous_creation_time** | **sha1_hash** | **sha256_hash** | **signer** | **user** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | | | | |
| **delete** | | | | | | | | | | | | | | | |
| **modify** | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | |
| **read** | | | | | | | | | | | | | | | |
| **timestomp** | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) |
| **write** | | | | | | | | | | | | | | | |
