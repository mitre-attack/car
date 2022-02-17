---
title: "CAR-2013-07-002: RDP Connection Detection"
layout: analytic
submission_date: 2013/07/24
information_domain: Analytic, Network
subtypes: Map building, Anomaly, Hostflow
analytic_type: Situational Awareness, TTP
contributors: MITRE
applicable_platforms: N/A
---
<br><br>
The [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) (RDP), built in to Microsoft operating systems, allows a user to remotely log in to the desktop of another host. It allows for interactive access of the running windows, and forwards key presses, mouse clicks, etc. Network administrators, power users, and end-users may use RDP for day-to-day operations. From an adversary's perspective, RDP provides a means to [laterally move](https://attack.mitre.org/tactics/TA0008) to a new host. Determining which RDP connections correspond to adversary activity can be a difficult problem in highly dynamic environments, but will be useful in identifying the scope of a compromise.

Remote Desktop can be detected in several ways

-   Network connections to port 3389/tcp (assuming use of the default port)
-   Packet capture analysis
-   Windows security logs (Event ID 4624, 4634, 4647, 4778)
-   Detecting network connections from `mstsc.exe`
-   Execution of the process `rdpclip.exe`
-   Runs as the clipboard manager on the RDP target if clipboard sharing is enabled

### Output Description

The time of the Connection, the source, the destination, and the user name used


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Medium|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTSD | [Remote Terminal Session Detection](https://d3fend.mitre.org/technique/d3f:RemoteTerminalSessionDetection)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [end](/data_model/flow#end) | [dest_port](/data_model/flow#dest_port) |
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_ip](/data_model/flow#dest_ip) |
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_port](/data_model/flow#dest_port) |
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [src_ip](/data_model/flow#src_ip) |



### Implementations

#### Pseudocode


```
flow_start = search Flow:Start
flow_end = search Flow:End
rdp_start = filter flow_start where (port == "3389")
rdp_end = filter flow_start where (port == "3389")
rdp = group flow_start, flow_end by src_ip, src_port, dest_ip, dest_port
output rdp
```


#### Sigma (Localhost Login) (Sigma)


[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_rdp_localhost_login.yml) rule, focusing on RDP localhost login.





