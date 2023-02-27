---
title: "CAR-2020-11-003: DLL Injection with Mavinject"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Injecting a malicious DLL into a process is a common adversary TTP. Although the ways of doing this are numerous, mavinject.exe is a commonly used tool for doing so because it roles up many of the necessary steps into one, and is available within Windows. Attackers may rename the executable, so we also use the common argument "INJECTRUNNING" as a related signature here. Whitelisting certain applications may be necessary to reduce noise for this analytic.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Process Injection](https://attack.mitre.org/techniques/T1055/)|[Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


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

#### Pseudocode - mavinject process and its common argument (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
mavinject_processes = filter processes where (
  exe = "C:\\Windows\\SysWOW64\\mavinject.exe" OR Image="C:\\Windows\\System32\\mavinject.exe" OR command_line = "*/INJECTRUNNING*"
output mavinject_processes

```


#### Splunk Search - mavinject (Splunk, Sysmon native)


Search for instances of mavinject.exe or mavinject32.exe


```
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Windows\\SysWOW64\\mavinject.exe" OR Image="C:\\Windows\\System32\\mavinject.exe" OR CommandLine="*\INJECTRUNNING*")

```


#### LogPoint Search - mavinject (Logpoint, LogPoint native)


Search for instances of mavinject.exe or mavinject32.exe


```
norm_id=WindowsSysmon event_id=1 (image="C:\Windows\SysWOW64\mavinject.exe" OR image="C:\Windows\System32\mavinject.exe" OR command="*\INJECTRUNNING*")

```




