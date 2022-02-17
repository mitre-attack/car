---
title: "CAR-2014-03-001: SMB Write Request - NamedPipes"
layout: analytic
submission_date: 2014/03/03
information_domain: Host, Network
subtypes: Process, Netflow
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
An SMB write can be an indicator of lateral movement, especially when combined with other information such as execution of that written file. Named pipes are a subset of SMB write requests. Named pipes such as msftewds may not be alarming; however others, such as lsarpc, may.

Monitoring SMB write requests still creates some noise, particulary with named pipes. As a result, SMB is now split between writing named pipes and writing other files.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570/)|N/A|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-IPCTA | [IPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:IPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [proto_info](/data_model/flow#proto_info) |
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_port](/data_model/flow#dest_port) |



### Implementations

#### Pseudocode

Look for SMB network connections over port 445. Using a sensor that can decode protocol information, extract out the name of the pipe and potentially other information. This happens legitimately so certain pipes, such as `spoolss` should be appropriately white-listed. Certain pipes do correspond to adversary activity, including:

* `WINREG` - Windows Remote Registry ([CAR-2014-11-005](../CAR-2014-11-005))
* `ATSVC` - Windows AT command ([CAR-2015-04-001](../CAR-2015-04-001))


```
flow = search Flow:Message
smb_write = filter flow where (dest_port == "445" and protocol == "smb.write_pipe")
smb_write.pipe_name = smb_write.proto_info.pipe_name
output smb_write
```




