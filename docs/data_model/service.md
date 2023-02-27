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
command_line|The command line that service is started with.|<code>C:\windows\system32\svchost.exe -k rpcss</code>
exe|The executable for the service.|<code>svchost.exe</code>
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|Where in the file system the service executable is located.|<code>C:\path\to\example.exe</code>
name|The name of the service.|<code>RpcSs</code>
pid|The process ID for the process of the service, represented in decimal notation.|<code>718</code>
ppid|The process ID of the process’s parent or the service, represented in decimal notation. In the parent process, this will be the pid field.|<code>1860</code>
uid|The ID of SID of the user who acted on the service|<code>S-1-5-18</code>
user|The user token that service was created with.|<code>HOST1\LOCALUSER</code>

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
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>delete</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
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