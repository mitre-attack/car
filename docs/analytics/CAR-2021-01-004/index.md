---
title: "CAR-2021-01-004: Unusual Child Process for Spoolsv.Exe or Connhost.Exe"
layout: analytic
submission_date: 2020/12/03
information_domain: Host
subtypes: Process
analytic_type: Anomaly
contributors: Cyware Labs
applicable_platforms: Windows
---
<br><br>
After gaining initial access to a system, threat actors attempt to escalate privileges as they may be operating within a lower privileged process which does not allow them to access protected information or carry out tasks which require higher permissions. A common way of escalating privileges in a system is by externally invoking and exploiting spoolsv or connhost executables, both of which are legitimate Windows applications. This query searches for an invocation of either of these executables by a user, thus alerting us of any potentially malicious activity.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)|N/A|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Splunk search - Unusual Child Process For Spoolsv.exe Or Connhost.exe (Splunk, Sysmon native)


This query looks for processes spawned by spoolsv.exe or connhost.exe externally, thus alerting us of potentially malicious activity.


```
(index=__your_sysmon_index__ EventCode=1) (Image=C:\\Windows\\System32\\spoolsv.exe* OR Image=C:\\Windows\\System32\\conhost.exe) ParentImage = "C:\\Windows\\System32\\cmd.exe"

```




