---
title: "CAR-2014-11-004: Remote PowerShell Sessions"
layout: analytic
submission_date: 2014/11/19
information_domain: Host, Network
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
According to [ATT&CK](https://attack.mitre.org/), [PowerShell](https://attack.mitre.org/techniques/T1059/001) can be used over WinRM to remotely run commands on a host. When a remote PowerShell session starts, svchost.exe executes wsmprovhost.exe

For this to work, certain registry keys must be set, and the WinRM service must be enabled. The PowerShell command `Enter-PSSession -ComputerName \<RemoteHost\>` creates a remote PowerShell session.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[PowerShell](https://attack.mitre.org/techniques/T1059/001/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[Windows Remote Management](https://attack.mitre.org/techniques/T1021/006/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode


```
process = search Process:Create
wsmprovhost = filter process where (exe == "wsmprovhost.exe" and parent_exe == "svchost.exe")

```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "wsmprovhost.exe" and parent_process_name == "svchost.exe")

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\wsmprovhost.exe" parent_image="*\svchost.exe"

```




