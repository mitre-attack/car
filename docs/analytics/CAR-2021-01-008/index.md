---
title: "CAR-2021-01-008: Disable UAC"
layout: analytic
submission_date: 2020/12/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---
<br><br>
Threat actors often, after compromising a machine, try to disable User Access Control (UAC) to escalate privileges. This is often done by changing the registry key for system policies using “reg.exe”, a legitimate tool provided by Microsoft for modifying the registry via command prompt or scripts. This action interferes with UAC and may enable a threat actor to escalate privileges on the compromised system, thereby allowing further exploitation of the system.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)|[Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Medium|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Detect disabling of UAC via reg.exe (Splunk, Sysmon native)


This query looks for the specific use of reg.exe in correlation to commands aimed at disabling UAC.


```
sourcetype = __your_sysmon_index__ ParentImage = "C:\\Windows\\System32\\cmd.exe" | where like(CommandLine,"reg.exe%HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System%REG_DWORD /d 0%")

```


#### Detect disabling of UAC via reg.exe (Pseudocode, Sysmon native)


This query looks for the specific use of reg.exe in correlation to commands aimed at disabling UAC.


```
processes = search Process:Create
cmd_processes = filter processes where (
                (parent_image = "C:\\Windows\\System32\\cmd.exe") AND (command_line = "reg.exe%HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System%REG_DWORD /d 0%")
                )

```




