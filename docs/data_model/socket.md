---
title: "Socket"
---
Socket events are low-level events that may or may not result in a flow. Socket listenining events in particular can be helpful in detecting malicious activity.

## Actions
|Action|Description|
|---|---|
|bind|The event corresponding to a socket binding to a specific address|
|close|The event corresponding to a socket being closed.|
|listen|The event corresponding to a socket being opened into a listening status, usually on a specific local port.|

## Fields
|Field|Description|Example|
|---|---|---|
family|The type of socket in question|<code>AF_UNIX, AF_INET, AF_INET6</code>
image_path|Path to the executable that initiated the socket event.|<code>C:/user/adam/malware.exe</code>
local_address|IP address on which the socket will accept connections; does not include the port number.|<code>10.0.211.200</code>
local_path|In the case that a socket is used for local interprocess communication, the socket binds to a local filepath, and will usually be visible in the filesystem. This is the case with AF_UNIX type sockets.|<code>/tmp/foo</code>
local_port|Port number on which the socket is bound at the local end. This pertains to TCP and UDP sockets but not IP sockets.|<code>48777</code>
pid|ID of the process that acted on the socket|<code>3930</code>
protocol|The type of connection that was attempted on the socket|<code>TCP</code>
remote_address|IP address with which the socket is communicating on the remote end.|<code>199.121.21.20</code>
remote_port|Port number on which the socket is bound at the remote end.|<code>559</code>
success|Boolean indicator of whether the socket event was successful (e.g. the socket was created as requested)|<code>True</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>family</th>
    <th>image_path</th>
    <th>local_address</th>
    <th>local_path</th>
    <th>local_port</th>
    <th>pid</th>
    <th>protocol</th>
    <th>remote_address</th>
    <th>remote_port</th>
    <th>success</th>
  </tr>
  <tr>
    <th>bind</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>close</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>listen</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>