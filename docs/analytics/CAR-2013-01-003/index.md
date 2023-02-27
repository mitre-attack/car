---
title: "CAR-2013-01-003: SMB Events Monitoring"
layout: analytic
submission_date: 2013/01/25
information_domain: Network
subtypes: PCAP
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: N/A
---
<br><br>
[Server Message Block](https://en.wikipedia.org/wiki/Server_Message Block) (SMB) is used by Windows to allow for file, pipe, and printer sharing over port 445/tcp. It allows for enumerating, and reading from and writing to file shares for a remote computer. Although it is heavily used by Windows servers for legitimate purposes and by users for file and printer sharing, many adversaries also use SMB to achieve [Lateral Movement](https://attack.mitre.org/tactics/TA0008). Looking at this activity more closely to obtain an adequate sense of situational awareness may make it possible to detect adversaries moving between hosts in a way that deviates from normal activity. Because SMB traffic is heavy in many environments, this analytic may be difficult to turn into something that can be used to quickly detect an APT. In some cases, it may make more sense to run this analytic in a forensic fashion. Looking through and filtering its output after an intrusion has been discovered may be helpful in identifying the scope of compromise.

### Output Description

The source, destination, content, and time of each event.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Data from Network Shared Drive](https://attack.mitre.org/techniques/T1039/)|N/A|[Collection](https://attack.mitre.org/tactics/TA0009/)|Moderate|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-IPCTA | [IPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:IPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [dest_port](/data_model/flow#dest_port) |
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [proto_info](/data_model/flow#proto_info) |



### Implementations

#### Pseudocode

Although there may be more native ways to detect detailed SMB events on the host, they can be extracted out of network traffic. With the right protocol decoders, port 445 traffic can be filtered and even the file path (relative to the share) can be retrieved.


```
flow = search Flow:Message
smb_events = filter flow where (dest_port == "445" and protocol == "smb")
smb_events.file_name = smb_events.proto_info.file_name
output smb_write

```




