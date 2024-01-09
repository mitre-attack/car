---
title: "Module"
---
Modules correspond to executable (and potentially non-executable) content, and are loaded as a contiguous region of memory into the address space of a process. Each process will have the main image loaded as a module and shared libraries (DLLs in Windows) and their dependencies.

## Actions
|Action|Description|
|---|---|
|load|A module load event occurs when a PE image (dll or exe) is loaded into a process.|
|unload|When the module is unloaded from memory, upon destruction of the process or by calling an API such as FreeLibrary, the unload event is triggered.|

## Fields
|Field|Description|Example|
|---|---|---|
base_address|A hex address indicating where the module is loaded into the process’s virtual address space.|<code>18446735277684027392</code>
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|The file system location of the process image.|<code>C:\path\to\example.exe</code>
md5_hash|The MD5 hash of the contents of the file located at `module_path`. The field is in hex notation, without the 0x prefix.|<code>5eb63bbbe01eeed093cb22bb8f5acdc3</code>
module_name|The name of the file where the module is loaded on disk. This is also the string that is used internally by the program to lookup information about the module.|<code>kernel32.exe</code>
module_path|The full file system path to the module loaded into the memory space of the process.|<code>C:\windows\system32\kernel32.exe</code>
pid|Process ID of the process in which the module is loaded (or unloaded).|<code>738</code>
sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|<code>2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</code>
sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|<code>68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728</code>
signature_valid|Boolean indicator of whether the signature is current and not revoked|<code>True</code>
signer|The name of the organization which signed the module.|<code>Microsoft Corporation</code>
tid|The thread ID of the thread responsible for the load or unload event.|<code>50</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>base_address</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>md5_hash</th>
    <th>module_name</th>
    <th>module_path</th>
    <th>pid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>tid</th>
  </tr>
  <tr>
    <th>load</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
  <tr>
    <th>unload</th>
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