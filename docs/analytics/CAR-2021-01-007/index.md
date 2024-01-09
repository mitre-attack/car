---
title: "CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt"
layout: analytic
submission_date: 2020/12/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---
<br><br>
In an attempt to avoid detection after compromising a machine, threat actors often try to disable Windows Defender. This is often done using “sc” [service control], a legitimate tool provided by Microsoft for managing services. This action interferes with event detection and may lead to a security event going undetected, thereby potentially leading to further compromise of the network.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Impair Defenses](https://attack.mitre.org/techniques/T1562/)|[Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Medium|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Splunk search - Detecting Tampering of Windows Defender Command Prompt (Splunk, Sysmon native)


This query looks for the specific use of service control for querying or trying to stop Windows Defender.


```
index= __your_sysmon__index__ EventCode=1 Image = "C:\\Windows\\System32\\sc.exe"  | regex CommandLine="^sc\s*(config|stop|query)\sWinDefend$"

```


#### Splunk search - Detecting Tampering of Windows Defender Command Prompt (Pseudocode)


This query looks for the specific use of service control for querying or trying to stop Windows Defender.


```
processes = search Process:Create
target_processes = filter processes where (
                   (exe="C:\\Windows\\System32\\sc.exe") AND (command_line="sc *config*" OR command_line="sc *stop*" OR command_line="sc *query*")
                   )
output target_processes

```




