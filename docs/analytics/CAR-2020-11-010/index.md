---
title: "CAR-2020-11-010: CMSTP"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong, MITRE
applicable_platforms: Windows
---
<br><br>
CMSTP.exe is the Microsoft Connection Manager Profile Installer, which can be leveraged to setup listeners that will receive and install malware from remote sources in trusted fashion.
When CMSTP.exe is seen in combination with an external connection, it is a good indication of this TTP.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|[CMSTP](https://attack.mitre.org/techniques/T1218/003/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|High|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [src_ip](/data_model/process#src_ip) |



### Implementations

#### Pseudocode - CMSTP (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
target_processes = filter processes where (
  exe="C:\Windows\System32\CMSTP.exe" AND
  src_ip NOT IN [10.0.0.0/8,192.168.0.0/16, 172.16.0.0/12] )
output target_processes

```


#### Splunk Search - CMSTP (Splunk, Sysmon native)


looks for instances of CMSTP.exe that are combined with external communication


```
(index=__your_sysmon_index__ EventCode=3) Image="C:\\Windows\\System32\\CMSTP.exe" | where ((!cidrmatch("10.0.0.0/8", SourceIp) AND !cidrmatch("192.168.0.0/16", SourceIp) AND !cidrmatch("172.16.0.0/12", SourceIp))

```


#### LogPoint Search - CMSTP (Logpoint, LogPoint native)


looks for instances of CMSTP.exe that are combined with external communication


```
norm_id=WindowsSysmon event_id=3 image="C:\Windows\System32\CMSTP.exe" -source_address IN HOMENET

```




