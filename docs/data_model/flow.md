---
title: "Flow"
---

A sequence of packets from a source computer to a destination, which may be another host, a multicast group, or a broadcast domain. This may be captured at network or host level.

## Actions

|Action|Description|
| ---| ---|
|start|The event corresponding to the beginning of collection of flow data in a given time period.
|end|The event corresponding to the ending of collection of flow data in a given time period.
|message|A flow message pertains to any event between start and end when content is sent over the connection (may imply TCP). This often implies use of traffic content collected via PCAP or a similar mechanism.

## Fields

|Field|Description|Example|
| ---| ---| ---|
|content|The ASCII printable characters of the flow. This corresponds to content from PCAC data or similar formats.|`GET https://www.google.com/ HTTP/1.1`
|dest_ip|The destination IP address of the flow.|`192.168.1.5`
|dest_port|The destination port of the flow.|`1900`
|end_time|The datetime stamp, in UTC, when the flow ended.|`5/15/2015 03:59:53.176 AM`
|exe|The basename of the `image_path`. This will need to be collected from the host.|`Chrome.exe`
|flags|TCP flags.|`SYN, ACK, PSH`
|fqdn|The fully qualified domain name of the host. Contains the hostname appended with the domain.|`HOST1.EXAMPLE_DOMAIN.COM`
|hostname|The hostname of the active host, without the domain.|`HOST1`
|image_path|The file system path of the process that opened the flow. This will need to be collected from the host.|`C:\path\to\example.exe`
|packet_count|The total packet count seen at time of logging.|`4`
|pid|The process ID of the process that owns the socket responsible for the flow, represented in decimal notation. This will need to be collected from the host.|`738`
|ppid|The process ID for the process's parent that owns the socket responsible for the flow, represented in decimal notation. This will need to be collected from the host.|`1860`
|proto_info|A text decoded version of traffic in the flow specific to the protocol. The application layer information from the flow parsed according to the protocol in question. For instance, SMB information or HTTP headers and content.|`SMB2 Write Request Len:165 Off:0 Fileusername\private\filename.pptx`, `SRVSVC NetShareGetInfo response`
|protocol|The application layer protocol for the flow.|`SMB`, `HTTP`
|src_ip|The source IP address of the flow.|`10.0.0.54`
|src_port|The source port of the flow packet.|`50438`
|start_time|The starting time date stamp, in UTC, of the flow data.|`05/14/2015 11:59:59 PM`
|user|The user that ran the process.|`HOST1\LOCALUSER`
|src_fqdn|The fully qualified domain name that corresponds to `src_ip`.|`src_domain.example.com`
|src_hostname|The hostname that corresponds to `src_ip`.|`src_example`
|dest_fqdn|The fully qualified domain name that corresponds to `dest_ip`.|`dest_example.example.com`
|dest_hostname|The hostname that corresponds to `dest_ip`|`dest_example`

## Coverage Map

| | **content** | **dest_fqdn** | **dest_hostname** | **dest_ip** | **dest_port** | **end_time** | **exe** | **flags** | **fqdn** | **hostname** | **image_path** | **packet_count** | **pid** | **ppid** | **proto_info** | **protocol** | **src_fqdn** | **src_hostname** | **src_ip** | **src_port** | **start_time** | **user** |
| ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| ---|---|---|---|---|
| **end** | | | | | | | | | | | | | | | | | | | | | | |
| **message** | | | | | | | | | | | | | | | | | | | | | | |
| **start** | | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | | | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) | [Sysmon (2.0)](../sensors/sysmon_2.0)<br />[Sysmon (3.1)](../sensors/sysmon_3.1)<br />[Sysmon (3.2)](../sensors/sysmon_3.2) |