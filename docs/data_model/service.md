---
title: "Service"
---
Services, or a service application, can be started automatically at system boot, by a user through the services control panel applet, or by an application that uses service functions. Services can execute even when no user is logged into the system.

## Actions
|Action|Description|
|---|---|
|create|The event corresponding to the act of creating a new service.|
|delete|The event corresponding to the act of deleting a service.|
|pause|The event corresponding to the act of pausing a currently running service.|
|start|The event corresponding to the act of starting a new service.|
|stop|The event corresponding to the act of stopping a service that is currently running.|

## Fields
|Field|Description|Example|
|---|---|---|
command_line|The command line that service is started with.|C:\windows\system32\svchost.exe -k rpcss
exe|The executable for the service.|svchost.exe
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|HOST1.EXAMPLE_DOMAIN.COM
hostname|The hostname of the host, without the domain.|HOST1
image_path|Where in the file system the service executable is located.|C:\path\to\example.exe
name|The name of the service.|RpcSs
pid|The process ID for the process of the service, represented in decimal notation.|718
ppid|The process ID of the process’s parent or the service, represented in decimal notation. In the parent process, this will be the pid field.|1860
uid|The ID of SID of the user who acted on the service|S-1-5-18
user|The user token that service was created with.|HOST1\LOCALUSER

## Coverage Map
<table>
  <tr>
    <th />
    <th>command_line</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>name</th>
    <th>pid</th>
    <th>ppid</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>create</th>
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
    <th>delete</th>
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
    <th>pause</th>
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
    <th>start</th>
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
    <th>stop</th>
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