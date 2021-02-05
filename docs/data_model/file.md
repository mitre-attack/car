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
|acl_modify|The event corresponding with changing permissions on a file.|

## Fields

|Field|Description|Example|
|---|---|---|
|company|The name of the organization listed in the file located at `image_path`.
|content|The contents of the file.|`Hello World`|
|creation_time|The creation time of the file as described in UTC and including the date.|`05/14/2015 12:47:06`|
|file_extension|The file extnsion of the file.|`docx`|
|file_name|The name of the file.|`MyWordDoc.docx`|
|file_path|The full path to the file.|`C:\users\fakeuser\documents\MyFile.docx`|
|file_gid|The group ID of the file|`801`|
|file_group|The group name of the file|`adam`|
|file_uid|The user ID or SID of the owner of the file.|`501`|
|file_user|The username of the owner of the file.|`adam`|
|fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`|
|hostname|The hostname of the host, without the domain.|`HOST1`|
|image_path|The file system location of the executable that is associated with the `pid` that generated this event.|`C:\Windows\system32\notepad.exe`|
|link_target|The target path of a symbolic link.|`C:\my_special_file.exe`|
|md5_hash|An MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|`5eb63bbbe01eeed093cb22bb8f5acdc3`|
|mime_type|The MIME type of the file.|`PE`|
|mode|The mode or permissions set of the file.|`0644 (linux) or NTFS ACL`|
|pid|The process ID for the process that generated this file event, represented in decimal notation.|`738`|
|ppid|The process ID of the parent process of the process associated with this file event, represented in decimal notation.|`1860`|
|previous_creation_time|The creation_time associated with the file before it was changed for this file event.|`05/14/2015 12:47:06`|
|sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|`2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`|
|sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|`68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728`|
|signer|The company listed on the certificate of the program at `image_path` if that program is signed.|`Microsoft |Corporation`
|signature_valid|Boolean indicator of whether the signature is valid; empty if file is not signed.|`True`|
|user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.|`HOST1\LOCALUSER`|
|uid|The user ID or SID for the acting entity.|`S-1-5-18`|

## Coverage Map

| | **company** | **content** | **creation_time** | **file_name** | **file_path** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **pid** | **ppid** | **previous_creation_time** | **sha1_hash** | **sha256_hash** | **signer** | **user** | **file_uid** | **file_gid** | **file_group** | **file_user** | **file_extension** | **link_target** | **mime_type** | **mode** | **signature_valid*** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | | | | | | | | | | | | | |
| **delete** | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **modify** | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | [Autoruns](../sensors/autoruns) | | | | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | [Autoruns](../sensors/autoruns) | | | | | | | | | | |
| **read** | | | | | | | | | | | | | | | | | | | | | | | | | |
| **timestomp** | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | | | | | | | | |
| **write** | | | | | | | | | | | | | | | | | | | | | | | | | |
| **acl_modify** | | | | | | | | | | | | | | | | | | | | | | | | | |
