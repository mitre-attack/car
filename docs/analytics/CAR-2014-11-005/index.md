---
title: "CAR-2014-11-005: Remote Registry"
layout: analytic
submission_date: 2014/11/19
information_domain: Host, Network
subtypes: Network Registry File, PCAP
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
An adversary can remotely [manipulate the registry](https://attack.mitre.org/techniques/T1112) of another machine if the RemoteRegistry service is enabled and valid credentials are obtained. While the registry is remotely accessed, it can be used to prepare a [Lateral Movement](https://attack.mitre.org/tactics/TA0008) technique, [discover](https://attack.mitre.org/tactics/TA0007) the configuration of a host, achieve [Persistence](https://attack.mitre.org/tactics/TA0003), or anything that aids an adversary in achieving the mission. Like most ATT&CK techniques, this behavior can be used legitimately, and the reliability of an analytic depends on the proper identification of the pre-existing legitimate behaviors. Although this behavior is disabled in many Windows configurations, it is possible to [remotely enable](https://attack.mitre.org/techniques/T1569/002) the RemoteRegistry service, which can be detected with [CAR-2014-03-005](../CAR-2014-03-005).

Remote access to the registry can be achieved via

-   Windows API function [RegConnectRegistry](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724840.aspx)
-   command line via `reg.exe`
-   graphically via `regedit.exe`

All of these behaviors call into the Windows API, which uses the NamedPipe `WINREG` over SMB to handle the protocol information. This network can be decoded with wireshark or a similar sensor, and can also be detected by hooking the API function.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


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


```
flows = search Flow:Message
winreg = filter flows where (dest_port == 445 and proto_info.pipe == "WINREG")
winreg_modify = filter flows where (proto_info.function == "Create*" or proto_info.function == "SetValue*")

output winreg_modify

```




