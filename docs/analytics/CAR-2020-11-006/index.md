---
title: "CAR-2020-11-006: Local Permission Group Discovery"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Cyber actors frequently enumerate local or domain permissions groups. The net utility is usually used for this purpose. This analytic looks for any instances of net.exe, which is not normally used for benign purposes, although system administrator actions may trigger false positives.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|[Local Groups](https://attack.mitre.org/techniques/T1069/001/), [Domain Groups](https://attack.mitre.org/techniques/T1069/002/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Pseudocode - net.exe instances (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
net_processes = filter processes where (
  exe = "net.exe" AND (
  command_line="*net* user*" OR
  command_line="*net* group*" OR
  command_line="*net* localgroup*" OR
  command_line="*get-localgroup*" OR
  command_line="*get-ADPrincipalGroupMembership*" )
output net_processes

```


#### Splunk Search - net.exe instances (Splunk, Sysmon native)


Look for instances of net.exe


```
(index=__your_sysmon_index__ EventCode=1) Image="C:\\Windows\\System32\\net.exe" AND (CommandLine="* user*" OR CommandLine="* group*" OR CommandLine="* localgroup*" OR CommandLine="*get-localgroup*" OR CommandLine="*get-ADPrincipalGroupMembership*")

```


#### LogPoint Search - net.exe instances (Logpoint, LogPoint native)


Look for instances of net.exe


```
norm_id=WindowsSysmon event_id=1 image="C:\Windows\System32\net.exe" (command="* user*" OR command="* group*" OR command="* localgroup*" OR command="*get-localgroup*" OR command="*get-ADPrincipalGroupMembership*")

```




