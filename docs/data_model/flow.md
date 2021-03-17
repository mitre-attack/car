---
title: "Flow"
---

A sequence of packets from a source computer to a destination, which may be another host, a multicast group, or a broadcast domain. This may be captured at network or host level.

## Actions

|Action|Description|
|---|---|
|start|The event corresponding to the beginning of collection of flow data in a given time period.
|end|The event corresponding to the ending of collection of flow data in a given time period.
|message|A flow message pertains to any event between start and end when content is sent over the connection (may imply TCP). This often implies use of traffic content collected via PCAP or a similar mechanism.

## Fields

|Field|Description|Example|
|---|---|---|
|application_protocol|Name of the layer 7 protocol contained within the flow.|`HTTP`
|content|The ASCII printable characters of the flow. This corresponds to content from PCAC data or similar formats.|`GET https://www.google.com/ HTTP/1.1`
|dest_ip|The destination IP address of the flow.|`192.168.1.5`
|dest_port|The destination port of the flow.|`1900`
|dest_fqdn|The fully qualified domain name that corresponds to `dest_ip`.|`dest_example.example.com`
|dest_hostname|The hostname that corresponds to `dest_ip`|`dest_example`
|end_time|The datetime stamp, in UTC, when the flow ended.|`5/15/2015 03:59:53.176 AM`
|exe|The basename of the `image_path`. This will need to be collected from the host.|`Chrome.exe`
|fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`
|hostname|The hostname of the active host, without the domain.|`HOST1`
|image_path|The file system path of the process that opened the flow. This will need to be collected from the host.|`C:\path\to\example.exe`
|in_bytes|Integer value of total number of bytes received.|`13200`
|out_bytes|Integer value of total number of bytes sent.|`1337`
|network_direction|Direction of the original packet of the flow initiator, relative to network perimeter.|`in (flow originated outside the network and was directed into it)`
|packet_count|The total packet count seen at time of logging.|`4`
|pid|The process ID of the process that owns the socket responsible for the flow, represented in decimal notation. This will need to be collected from the host.|`738`
|ppid|The process ID for the process's parent that owns the socket responsible for the flow, represented in decimal notation. This will need to be collected from the host.|`1860`
|proto_info|A text decoded version of traffic in the flow specific to the protocol. The application layer information from the flow parsed according to the protocol in question. For instance, SMB information or HTTP headers and content.|`SMB2 Write Request Len:165 Off:0 Fileusername\private\filename.pptx`, `SRVSVC NetShareGetInfo response`
|src_ip|The source IP address of the flow.|`10.0.0.54`
|src_port|The source port of the flow packet.|`50438`
|src_fqdn|The fully qualified domain name that corresponds to `src_ip`.|`src_domain.example.com`
|src_hostname|The hostname that corresponds to `src_ip`.|`src_example`
|start_time|The starting time date stamp, in UTC, of the flow data.|`05/14/2015 11:59:59 PM`
|tcp_flags|TCP flags.|`SYN, ACK, PSH`
|transport_protocol|Lyaer 4 protocol contained within the flow|`TCP`
|uid|User ID or SID of the flow-handling entity|`S-1-5-18`
|user|The user that ran the process.|`HOST1\LOCALUSER`



## Coverage Map

| | **application_protocol** | **content** | **dest_fqdn** | **dest_hostname** | **dest_ip** | **dest_port** | **end_time** | **exe** | **fqdn** | **hostname** | **image_path** | **in_bytes** | **out_bytes** | **network_direction** | **packet_count** | **pid** | **ppid** | **proto_info** | **src_fqdn** | **src_hostname** | **src_ip** | **src_port** | **start_time** | **tcp_flags** | **transport_protocol** | **uid** | **user** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **end** | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **message** | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **start** | | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13)| [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | | | | [Sysmon](../sensors/sysmon_13) | | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | [Sysmon](../sensors/sysmon_13) | 
