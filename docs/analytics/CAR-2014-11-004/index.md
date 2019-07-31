---
title: "CAR-2014-11-004: Remote PowerShell Sessions"
layout: analytic
submission_date: 2014/11/19
information_domain: Host, Network
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

According to [ATT&CK](https://attack.mitre.org/), [PowerShell](https://attack.mitre.org/techniques/T1086/) can be used over WinRM to remotely run commands on a host. When a remote PowerShell session starts, svchost.exe executes wsmprovhost.exe

For this to work, certain registry keys must be set, and the WinRM service must be enabled. The PowerShell command `Enter-PSSession -ComputerName \<RemoteHost\>` creates a remote PowerShell session.

### ATT&CK Detection
|Technique |Tactic |Level of Coverage |
|---|---|---|
|[PowerShell](https://attack.mitre.org/techniques/T1086/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Windows Remote Management](https://attack.mitre.org/techniques/T1028/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|

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

Splunk version of the above pseudocode.


```
process where subtype.create and
  (process_name == "wsmprovhost.exe" and parent_process_name == "svchost.exe")    
```


