---
title: "CAR-2020-11-009: Compiled HTML Access"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may hide malicious code in .chm compiled HTML files. When these files are read, Windows uses the HTML help executable named hh.exe, which is the signature for this analytic.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|[Compiled HTML File](https://attack.mitre.org/techniques/T1218/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|High|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode - instances of hh.exe (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
target_processes = filter processes where (exe="C:\Windows\syswow64\hh.exe" OR exe="C:\Windows\system32\hh.exe")
output target_processes

```


#### Splunk Search - hh.exe (Splunk, Sysmon native)


looks all instances of hh.exe


```
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Windows\\syswow64\\hh.exe" OR Image="C:\\Windows\\system32\\hh.exe")

```


#### LogPoint Search - hh.exe (Logpoint, LogPoint native)


looks all instances of hh.exe


```
norm_id=WindowsSysmon event_id=1 (image="C:\Windows\syswow64\hh.exe" OR image="C:\Windows\system32\hh.exe")

```




