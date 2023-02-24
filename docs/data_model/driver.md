---
title: "Driver"
---
A driver is software that runs in the operating system kernel. Drivers are generally used to allow a computer to communicate with hardware devices but have access to important kernel resources.

## Actions
|Action|Description|
|---|---|
|load|The event corresponding to the operating system kernel loading a driver into memory.|
|unload|The event corresponding to the operating system kernel unloading a driver from memory.|

## Fields
|Field|Description|Example|
|---|---|---|
base_address|A hex address indicating where the driver is loaded into the kernel.|18446735277684027392
fqdn|The fully qualified domain name of the host in which the process ran. Contains the hostname appended with the domain.|HOST1.EXAMPLE_DOMAIN.COM
hostname|The hostname of the host, without the domain.|HOST1
image_path|The file system location of the driver.|C:\Windows\System32\drivers\scsiport.sys
md5_hash|The MD5 hash of the contents of the file located at `image_path`. The field is in hex notation, without the 0x prefix.|5eb63bbbe01eeed093cb22bb8f5acdc3
module_name|The name of the driver or program.|NvStreamKms.sys
pid|The Process ID that loaded or unloaded the driver|1533
sha1_hash|The SHA1 hash of the contents of the file located at `image_path`.|2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
sha256_hash|The SHA256 hash of the contents of the file located at `image_path`.|68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728
signature_valid|Boolean indicator of whether the driver is signed and whether the signature is current and not revoked|True
signer|The name of the organization which signed the driver.|Microsoft Corporation

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
    <th>pid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
  </tr>
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
  </tr>
</table>