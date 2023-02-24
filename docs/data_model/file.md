---
title: "File"
---
A resource for storing information available to a computer program.

## Actions
|Action|Description|
|---|---|
|acl_modify|The event corresponding with changing permissions on a file.|
|create|The event corresponding to the creation of a file.|
|delete|The event corresponding to the deletion of a file.|
|modify|The event corresponding to the modification of a file or its metadata.|
|read|The event corresponding to the accessing of a file to be read.|
|timestomp|The modification of an attribute, such as creation time. The file metadata may change, but the contents of the file remain the same.|
|write|The event corresponding to the accessing of a file in order to write new instructions or information into a file.|

## Fields
|Field|Description|Example|
|---|---|---|
company|The name of the organization listed in the file located at `image_path`.|
content|The contents of the file.|<code>Hello World</code>
creation_time|The creation time of the file as described in UTC and including the date.|<code>05/14/2015 12:47:06</code>
extension|The file extension of the file.|<code>.docx</code>
file_name|The name of the file.|<code>MyWordDoc.docx</code>
file_path|The full path to the file on the file system.|<code>C:\users\fakeuser\documents\MyFile.</code>
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
gid|The group ID of the file.|<code>801</code>
group|The group owner of the file.|<code>admin</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|The file system location of the executable that is associated with the pid that generated this event.|<code>C:\Windows\system32\notepad.exe</code>
link_target|The target path of a symbolic link.|<code>C:\my_special_file.exe</code>
md5_hash|An MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|<code>5eb63bbbe01eeed093cb22bb8f5acdc3</code>
mime_type|The MIME type of the file.|<code>PE</code>
mode|The mode or permissions set of the file.|<code>0644 (linux) or NTFS ACL</code>
owner|The username of the owner of the file.|<code>adam</code>
owner_uid|The user ID of the owner of the file.|<code>501</code>
pid|The process ID for the process that generated this file event, represented in decimal notation.|<code>738</code>
ppid|The process ID of the parent process of the process associated with this file event, represented in decimal notation.|<code>1860</code>
previous_creation_time|The creation_time associated with the file before it was changed for this file event.|<code>05/14/2015 12:47:06</code>
sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|<code>2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</code>
sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|<code>68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728</code>
signature_valid|Boolean indicator of whether the signature is valid; empty if file is not signed.|<code>True</code>
signer|The company listed on the certificate of the program at `image_path` if that program is signed.|<code>Microsoft Corporation</code>
uid|The user ID or SID for the acting entity.|<code>S-1-5-18</code>
user|The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as <DOMAIN>\<USER>. Because threads are allowed to impersonate users, this may be different than the user context of the process.|<code>HOST1\LOCALUSER</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>company</th>
    <th>content</th>
    <th>creation_time</th>
    <th>extension</th>
    <th>file_name</th>
    <th>file_path</th>
    <th>fqdn</th>
    <th>gid</th>
    <th>group</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>link_target</th>
    <th>md5_hash</th>
    <th>mime_type</th>
    <th>mode</th>
    <th>owner</th>
    <th>owner_uid</th>
    <th>pid</th>
    <th>ppid</th>
    <th>previous_creation_time</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>acl_modify</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>create</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>delete</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>modify</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>read</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>timestomp</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>write</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>