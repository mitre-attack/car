---
title: "CAR-2021-01-009: Detecting Shadow Copy Deletion via Vssadmin.exe"
layout: analytic
submission_date: 2020/12/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---

After compromising a network of systems, threat actors often try to delete Shadow Copy in an attempt to prevent administrators from restoring the systems to versions present before the attack. This is often done via vssadmin, a legitimate Windows tool to interact with shadow copies. This non-detection of this technique, which is often employed by ransomware strains such as “Olympic Destroyer”, may lead to a failure in recovering systems after an attack.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)|N/A|[Impact](https://attack.mitre.org/tactics/TA0040/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Implementations

#### Splunk query for Detecting Shadow Copy Deletion via vssadmin.exe (Splunk, Sysmon native)


This query looks for the specific use of vssadmin in correlation to a deleting function, alerting us of attempts to delete shadow copies that possibly indicate malicious activity.


```
index=__your_win_event_log_index__ EventType=4688 CommandLine:"delete" OriginalFileName:"VSSADMIN.EXE"
```




