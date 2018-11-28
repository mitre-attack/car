# Data Model: process
A process is a running program on a computer.

## Actions

|Action|Description|
|---|---|
|create|The event corresponding to a process creation in Windows. In the kernel, these are often captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx).|
|terminate|The event corresponding to a process destruction in Windows. In the kernel, these are also captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx), but with point to a NULL structure.|

## Fields

|Field|Description|Example|
|---|---|---|
|command_line|The command line string contains all arguments passed to the process upon execution.|`example arg1 arg2`, `example.exe`, `C:\path\example.exe /flag1`|
|exe|The basename of the `image_path`.|`example.exe`
|fqdn|The fully qualified domain name of the host in which the process ran. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`
|hostname|The hostname of the host, without the domain.|`HOST1`
|image_path|The file path of the executable associated with this process. This may act as a pivot to [`file:file_path`](https://car.mitre.org/wiki/Data_Model/file#file_path).|`C:\path\to\example.exe`
|md5_hash|The MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|`5eb63bbbe01eeed093cb22bb8f5acdc3`
|parent_exe|The `exe` field of the parent process. This is a substring of `parent_image_path`|`example_parent.exe`
|parent_image_path|The `image_path` field of the parent process.|`C:\path\to\example_parent.exe`
|pid|The process ID for the process, represented in decimal notation.|`738`
|ppid|The process ID for the process's parent, represented in decimal notation. In the parent process, this will be the `pid` field.|`1860`
|sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|`2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`
|sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|`68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728`
|sid|The security identifier of the `user` token that the process is running under.|`S-1-5-18`
|signer|The company that signed the file.
|user|The user token that process was created with. May be a local, domain or SYSTEM user. Formatted with "\<DOMAIN>\\\<USER>". Individual threads in the process may gain more privilege or change tokens, so the active token in any thread is not necessarily the one the process was created under.|`HOST1\LOCALUSER`
## Coverage Map

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **md5_hash** | **parent_exe** | **parent_image_path** | **pid** | **ppid** | **sha1_hash** | **sha256_hash** | **sid** | **signer** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |
| **terminate** | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) | | | | | | [Sysmon (2.0)]( ../sensors/sysmon_2.0.md) [Sysmon (3.1)]( ../sensors/sysmon_3.1.md) [Sysmon (3.2)]( ../sensors/sysmon_3.2.md) |

