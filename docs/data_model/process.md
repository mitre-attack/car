---
title: "Process"
---
A process is a running program on a computer.

## Actions
|Action|Description|
|---|---|
|access|The vent corresponding to a process accessing the memory space of another process.|
|create|The event corresponding to a process creation in Windows. In the kernel, these are often captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx).|
|terminate|The event corresponding to a process destruction in Windows. In the kernel, these are also captured with the callback [PsSetCreateProcessNotifyRoutine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951%28v=vs.85%29.aspx), but with a pointer to a NULL structure.|

## Fields
|Field|Description|Example|
|---|---|---|
access_level|Permissions level at which the target process is accessed.|<code>64</code>
call_trace|Stack trace showing context of process open/access call.|
command_line|The command line string contains all arguments passed to the process upon execution.|<code>example.exe arg1 arg2</code>
current_working_directory|The absolute path to the current working directory of the process.|<code>c:\temp</code>
env_vars|The environment variables within a process's memory space, as a string.|<code>SHELL=/bin/zsh</code>
exe|The basename of the `image_path`.|<code>example.exe</code>
fqdn|The fully qualified domain name of the host in which the process ran. Contains the hostname appended with the domain.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
guid|Global unique identifier for the initiating process.|<code>{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|The file path of the executable associated with this process. This may act as a pivot to [file:file_path](https://car.mitre.org/wiki/Data_Model/file#file_path).|<code>C:\path\to\example.exe</code>
integrity_level|The Windows integrity level associated with the process. MUST be one of low, medium, high, or system.|<code>High</code>
md5_hash|The MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|<code>5eb63bbbe01eeed093cb22bb8f5acdc3</code>
parent_command_line|All of the arguments passed to the parent process upon execution.|<code>c:\windows\system32\dism.exe foo.xml</code>
parent_exe|The `exe` field of the parent process. This is a substring of `parent_image_path`.|<code>example_parent.exe</code>
parent_guid|Global unique identifier of the parent of the initiating process.|<code>{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}</code>
parent_image_path|The `image_path` field of the parent process.|<code>C:\path\to\example_parent.exe</code>
pid|The process ID for the process, represented in decimal notation.|<code>738</code>
ppid|The process ID for the process's parent, represented in decimal notation. In the parent process, this will be the `pid` field.|<code>1860</code>
sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|<code>2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</code>
sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|<code>68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728</code>
sid|The Windows security identifier of the `user` token that the process is running under.|<code>S-1-5-18</code>
signature_valid|Boolean indicator of whether signature is current and not revoked.|<code>True</code>
signer|The name of the company that signed the file.|<code>FooCorp</code>
target_address|Specific address range which is accessed by another process.|<code>08048000-0804c000</code>
target_guid|Global Unique Identifier for the target process (only for process access events).|
target_name|Name of the process that is accessed.|<code>C:\Windows\System32\winlogon.exe</code>
target_pid|ID of the target process (only for process access events).|
uid|User ID under which original process is running.|<code>509</code>
user|The user token that process was created with. May be a local, domain or SYSTEM user. Formatted with "<DOMAIN>\<USER>". Individual threads in the process may gain more privilege or change tokens, so the active token in any thread is not necessarily the one the process was created under.|<code>HOST1\LOCALUSER</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>access_level</th>
    <th>call_trace</th>
    <th>command_line</th>
    <th>current_working_directory</th>
    <th>env_vars</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>guid</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>integrity_level</th>
    <th>md5_hash</th>
    <th>parent_command_line</th>
    <th>parent_exe</th>
    <th>parent_guid</th>
    <th>parent_image_path</th>
    <th>pid</th>
    <th>ppid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>sid</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>target_address</th>
    <th>target_guid</th>
    <th>target_name</th>
    <th>target_pid</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>access</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
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
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>create</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
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
    <th>terminate</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>