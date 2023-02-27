---
title: "User Session"
---
User sessions are the user activities undertaken on the computer in the course of conducting standard user actions.

## Actions
|Action|Description|
|---|---|
|lock|The event corresponding to the act of a user locking a machine such that they are still logged into the machine but unable to access it without re-entering credentials, effectively entering the machine into a locked state.|
|login|The event corresponding to the act of a user logging into a machine.|
|logout|The event corresponding to the act of a user logging out of a machine.|
|reconnect|The event corresponding to the act of a user reconnecting when an RDP session disconnects but the user is not logged off.|
|unlock|The event corresponding to the act of a user unlocking a machine currently in a locked state.|

## Fields
|Field|Description|Example|
|---|---|---|
dest_ip|The destination IP address of the user session. Only applicable to remote or RDP sessions.|<code>192.168.1.5</code>
dest_port|The destination port of the user session. Only applicable to remote or RDP sessions.|<code>1900</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
login_id|A hex value corresponding to the session. The logon id will persist until logout occurs.|<code>1008115</code>
login_successful|Boolean indicator of whether a login attempt was successful|<code>False</code>
login_type|The type of login that was accomplished or attempted|<code>interactive,local,rdp,remote</code>
src_ip|The source IP address of the user session. Only applicable to remote or RDP sessions.|<code>10.0.0.54</code>
src_port|The source port of the user session. Only applicable to remote or RDP sessions.|<code>50438</code>
uid|ID or SID of the user for which a session event ocurred|<code>S-1-5-18</code>
user|The user affiliated with the session. May be a local, domain or SYSTEM user.|<code>HOST1\LOCALUSER</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>dest_ip</th>
    <th>dest_port</th>
    <th>hostname</th>
    <th>login_id</th>
    <th>login_successful</th>
    <th>login_type</th>
    <th>src_ip</th>
    <th>src_port</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>lock</th>
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
    <th>login</th>
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
    <th>logout</th>
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
    <th>reconnect</th>
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
    <th>unlock</th>
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