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
base_address|A hex address indicating where the module is loaded into the process’s virtual address space.|18446735277684027392
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|HOST1.EXAMPLE_DOMAIN.COM
hostname|The hostname of the host, without the domain.|HOST1
image_path|The file system location of the process image.|C:\path\to\example.exe
md5_hash|The MD5 hash of the contents of the file located at `module_path`. The field is in hex notation, without the 0x prefix.|5eb63bbbe01eeed093cb22bb8f5acdc3
module_name|The name of the file where the module is loaded on disk. This is also the string that is used internally by the program to lookup information about the module.|kernel32.exe
module_path|The full file system path to the module loaded into the memory space of the process.|C:\windows\system32\kernel32.exe
pid|Process ID of the process in which the module is loaded (or unloaded).|738
sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728
signature_valid|Boolean indicator of whether the signature is current and not revoked|True
signer|The name of the organization which signed the module.|Microsoft Corporation
tid|The thread ID of the thread responsible for the load or unload event.|50

## Coverage Map
<table>
  <thead>
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
  </thead>
  <tbody>
    
    <tr>
      <th>load</th>
      
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
    
  </tbody>
</table>