---
title: "Process"
---

A process is a running program on a computer.

## Actions

|Action|Description|
|---|---|
|access|The event corresponding to a process accessing the memory space of another process.
|create|The event corresponding to a process creation in Windows. In the kernel, these are often captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx).|
|terminate|The event corresponding to a process destruction in Windows. In the kernel, these are also captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx), but with point to a NULL structure.|

## Fields

|Field|Description|Example|
|---|---|---|
|access_level|Permissions level at which the target process is accessed.|`0x40`|
|call_trace|The stack trace showing the context of a process open/access call.|`C:\Windows\SYSTEM32\ntdll.dll+a5594|C:\Windows\system32\KERNELBASE.dll+1e865`|
|command_line|The command line string contains all arguments passed to the process upon execution.|`example arg1 arg2`, `example.exe`, `C:\path\example.exe /flag1`|
|current_working_directory|The absolute path to the current working directory of the process.|`c:\windows\system32\`|
|exe|The basename of the `image_path`.|`example.exe`|
|env_vars|The environment variables within a process's memory space, as a string.|`SHELL=/bin/zsh`|
|fqdn|The fully qualified domain name of the host in which the process ran. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`|
|guid|Globally unique identifier for the process.|`{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`|
|hostname|The hostname of the host, without the domain.|`HOST1`|
|image_path|The file path of the executable associated with this process. This may act as a pivot to [`file:file_path`](https://car.mitre.org/wiki/Data_Model/file#file_path).|`C:\path\to\example.exe`|
|integrity_level|The Windows integrity level associated with the process. MUST be one of: low, medium, high, or system.|`high`|
|md5_hash|The MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|`5eb63bbbe01eeed093cb22bb8f5acdc3`|
|parent_command_line|All of the arguments passed to the parent process upon execution.|`c:\\windows\\system32\\dism.exe foo.xml`|
|parent_exe|The `exe` field of the parent process. This is a substring of `parent_image_path`|`example_parent.exe`|
|parent_guid|Globally unique identifier for the parent of the initiating process.|`{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`|
|parent_image_path|The `image_path` field of the parent process.|`C:\path\to\example_parent.exe`|
|pid|The process ID for the process, represented in decimal notation.|`738`|
|ppid|The process ID for the process's parent, represented in decimal notation. In the parent process, this will be the `pid` field.|`1860`|
|sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|`2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`|
|sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|`68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728`|
|sid|The security identifier or UID of the `user` token that the process is running under.|`S-1-5-18`|
|signer|The company that signed the file.|`True`|
|signature_valid|Boolean indicator of whether signature is current and not revoked.|`FooCorp`|
|target_address|Specific address range which is accessed by another process.|`08048000-0804c000`|
|target_guid|Global Unique Identifier for the target process (only for process access events).||
|target_pid|ID of the target process (only for process access events).||
|target_name|Name of the process that is accessed.|`C:\Windows\System32\winlogon.exe`|
|user|The user token that process was created with. May be a local, domain or SYSTEM user. Formatted with "\<DOMAIN>\\\<USER>". Individual threads in the process may gain more privilege or change tokens, so the active token in any thread is not necessarily the one the process was created under.|`HOST1\LOCALUSER`|

## Coverage Map

| | **access_level** | **call_trace** | **command_line** | **current_working_directory** | **exe** | **env_vars** | **fqdn** | **guid** | **hostname** | **image_path** | **integrity_level** | **md5_hash** | **parent_command_line** | **parent_exe** | **parent_guid** | **parent_image_path** | **pid** | **ppid** | **sha1_hash** | **sha256_hash** | **sid** | **signer** | **signature_valid** | **target_address** | **target_guid** | **target_pid** | **target_name** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **access** | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | | | | | | [Sysmon](../sensors/sysmon_13) | | | | [Sysmon](../sensors/sysmon_13) | | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | |
**create** | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | | | | | | | | | | | | | |
