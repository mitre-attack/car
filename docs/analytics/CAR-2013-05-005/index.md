---
title: "CAR-2013-05-005: SMB Copy and Execution"
layout: analytic
submission_date: 2013/05/13
information_domain: Host, Network
subtypes: Network Process File, PCAP
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
An adversary needs to gain access to other hosts to move throughout an environment. In many cases, this is a twofold process. First, a file is remotely written to a host via an SMB share (detected by [CAR-2013-05-003](../CAR-2013-05-003)). Then, a variety of [Execution](https://attack.mitre.org/tactics/TA0002) techniques can be used to remotely establish execution of the file or script. To detect this behavior, look for files that are written to a host over SMB and then later run directly as a process or in the command line arguments. SMB File Writes and Remote Execution may happen normally in an environment, but the combination of the two behaviors is less frequent and more likely to indicate adversarial activity.

This can possibly extend to more copy protocols in order to widen its reach, or it could be tuned more finely to focus on specific program run locations (e.g. `%SYSTEMROOT%\system32`) to gain a higher detection rate.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|
|[Valid Accounts](https://attack.mitre.org/techniques/T1078/)|[Domain Accounts](https://attack.mitre.org/techniques/T1078/002/), [Local Accounts](https://attack.mitre.org/techniques/T1078/003/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570/)|N/A|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-IPCTA | [IPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:IPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [proto_info](/data_model/process#proto_info) |
|[process](/data_model/process) | [create](/data_model/process#create) | [hostname](/data_model/process#hostname) |



### Implementations

#### Pseudocode


```
process = search Process:Create
smb_write = run Analytic:CAR-2013-05-003
remote_start = join (smb_write, process) where (
 smb_write.hostname == process.hostname and
 smb_write.file_path == process.image_path
 (smb_write.time < process.time)
)
output remote_start
```




