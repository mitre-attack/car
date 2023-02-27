---
title: "CAR-2020-11-007: Network Share Connection Removal"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may use network shares to exfliltrate date; they will then remove the shares to cover their tracks. This analytic looks for the removal of network shares via commandline, which is otherwise a rare event.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Indicator Removal](https://attack.mitre.org/techniques/T1070/)|[Network Share Connection Removal](https://attack.mitre.org/techniques/T1070/005/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|High|


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

#### Pseudocode - network shares being removed via the command line (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
target_processes = filter processes where (
  (exe="C:\\Windows\\System32\\net.exe" AND command_line="*delete*") OR
  command_line="*Remove-SmbShare*" OR
  comman_line="*Remove-FileShare*" )
output target_processes

```


#### Splunk Search - delete network shares (Splunk, Sysmon native)


looks network shares being deleted from the command line


```
(index=__your_sysmon_index__ EventCode=1) ((Image="C:\\Windows\\System32\\net.exe" AND CommandLine="*delete*") OR CommandLine="*Remove-SmbShare*" OR CommandLine="*Remove-FileShare*")

```


#### LogPoint Search - delete network shares (Logpoint, LogPoint native)


looks network shares being deleted from the command line


```
norm_id=WindowsSysmon event_id=1 ((image="C:\Windows\System32\net.exe" command="*delete*") OR command="*Remove-SmbShare*" OR command="*Remove-FileShare*")

```




