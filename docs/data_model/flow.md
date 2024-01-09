---
title: "Flow"
---
A sequence of packets from a source computer to a destination, which may be another host, a multicast group, or a broadcast domain. This may be captured at network or host level.

## Actions
|Action|Description|
|---|---|
|end|The event corresponding to the ending of collection of flow data in a given time period.|
|message|A flow message pertains to any event between start and end when content is sent over the connection (may imply TCP). This often implies use of traffic content collected via PCAP or a similar mechanism.|
|start|The event corresponding to the beginning of collection of flow data in a given time period.|

## Fields
|Field|Description|Example|
|---|---|---|
application_protocol|Name of the layer 7 protocol contained within the flow.|<code>HTTP</code>
content|The ASCII printable characters of the flow. This corresponds to content from PCAP data or similar formats.|<code>GET https://www.google.com/ HTTP/1.1</code>
dest_fqdn|The fully qualified domain name that corresponds to `dest_ip`.|<code>dest_example.example.com</code>
dest_hostname|The hostname that corresponds to `dest_ip`.|<code>dest_example</code>
dest_ip|The destination IP address of the flow.|<code>192.168.1.5</code>
dest_port|The destination port of the flow.|<code>192.168.1.5</code>
end_time|The datetime stamp, in UTC, when the flow ended.|<code>05/15/2015 03:59:53.176 AM</code>
exe|The basename of the `image_path`. This will need to be collected from the host.|<code>Chrome.exe</code>
fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|<code>HOST1.EXAMPLE_DOMAIN.COM</code>
hostname|The hostname of the host, without the domain.|<code>HOST1</code>
image_path|The file system path of the process that opened the flow. This will need to be collected from the host.|<code>C:\path\to\example.exe</code>
in_bytes|Integer value of total number of bytes received.|<code>13200</code>
network_direction|Direction of the original of the flow initiator, relative to network perimiter.|<code>in (flow originated outside the network and was directed into it)</code>
out_bytes|Integer value of total number of bytes sent.|<code>1337</code>
packet_count|The total packet count seen at time of logging.|<code>4</code>
pid|The total packet count seen at time of logging.|<code>738</code>
ppid|The process ID for the process’s parent that owns the socket responsible for the flow, represented in decimal notation. This will need to be collected from the host.|<code>1860</code>
proto_info|A text decoded version of traffic in the flow specific to the protocol. The application layer information from the flow parsed according to the protocol in question. For instance, SMB information or HTTP headers and content.|<code>SMB2 Write Request Len:165 Off:0 Fileusername\private\filename.pptx, SRVSVC NetShareGetInfo response</code>
src_fqdn|The fully qualified domain name that corresponds to `src_ip`.|<code>src_domain.example.com</code>
src_hostname|The hostname that corresponds to `src_ip`.|<code>src_example</code>
src_ip|The source IP address of the flow.|<code>10.0.0.54</code>
src_port|The source port of the flow.|<code>50438</code>
start_time|The starting time date stamp, in UTC, of the flow data.|<code>05/14/2015 11:59:59 PM</code>
tcp_flags|flags turned on in the TCP header.|<code>ACK, PSH</code>
transport_protocol|Layer 4 protocol contained within the flow.|<code>TCP</code>
uid|User ID or SID of the flow-handling entity.|<code>S-1-5-18</code>
user|The user that ran the process.|<code>HOST1\LOCALUSER</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>application_protocol</th>
    <th>content</th>
    <th>dest_fqdn</th>
    <th>dest_hostname</th>
    <th>dest_ip</th>
    <th>dest_port</th>
    <th>end_time</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>in_bytes</th>
    <th>network_direction</th>
    <th>out_bytes</th>
    <th>packet_count</th>
    <th>pid</th>
    <th>ppid</th>
    <th>proto_info</th>
    <th>src_fqdn</th>
    <th>src_hostname</th>
    <th>src_ip</th>
    <th>src_port</th>
    <th>start_time</th>
    <th>tcp_flags</th>
    <th>transport_protocol</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>end</th>
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
  <tr>
    <th>message</th>
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
  <tr>
    <th>start</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
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
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
</table>