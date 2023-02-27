---
title: "CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize"
layout: analytic
submission_date: 2020/12/11
update_date: 2022/02/03
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs, Lucas Heiligenstein
applicable_platforms: Windows
---
<br><br>
After compromising a network of systems, threat actors often try to delete/resize Shadow Copy in an attempt to prevent administrators from restoring the systems to versions present before the attack. This is often done via vssadmin, a legitimate Windows tool to interact with shadow copies. This action is often employed by ransomware, may lead to a failure in recovering systems after an attack. The pseudo code detection focus on Windows Security and Sysmon process creation (4688 and 1). The use of wmic to delete shadow copy generates WMI-Activity Operationnal 5857 event and could generate 5858 (if the operation fails). These 2 EventIDs could be interesting when attackers use wmic without process creation and/or for forensics.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)|N/A|[Impact](https://attack.mitre.org/tactics/TA0040/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Splunk Search - Detecting Shadow Copy Deletion or Resize (Splunk)


This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.


```
((EventCode="4688" OR EventCode="1") (CommandLine="*vssadmin* *delete* *shadows*" OR CommandLine="*wmic* *shadowcopy* *delete*" OR CommandLine="*vssadmin* *resize* *shadowstorage*")) OR (EventCode="5857" ProviderName="MSVSS__PROVIDER") OR (EventCode="5858" Operation="*Win32_ShadowCopy*")

```


#### Elastic Search - Detecting Shadow Copy Deletion or Resize (Elastic)


This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.


```
(EventCode:("4688" OR "1") AND process.command_line:(*vssadmin*\ *delete*\ *shadows* OR *wmic*\ *shadowcopy*\ *delete* OR *vssadmin*\ *resize*\ *shadowstorage*)) OR (EventCode:"5857" AND ProviderName:"MSVSS__PROVIDER") OR (EventCode:"5858" AND Operation:*Win32_ShadowCopy*)

```


#### LogPoint Search - Detecting Shadow Copy Deletion or Resize (Logpoint)


This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.


```
(EventCode IN ["4688", "1"] CommandLine IN ["*vssadmin* *delete* *shadows*", "*wmic* *shadowcopy* *delete*", "*vssadmin* *resize* *shadowstorage*"]) OR (EventCode IN "5857" ProviderName IN "MSVSS__PROVIDER") OR (EventCode IN "5858" Operation IN "*Win32_ShadowCopy*")

```



### Unit Tests

#### Test Case 1

Shadow copy deletion with vssadmin

```
vssadmin.exe delete shadows /all /quiet
```

#### Test Case 2

Shadow copy deletion with wmic

```
wmic shadowcopy delete
```

#### Test Case 3

Shadow copy resize with vssadmin

```
vssadmin resize shadowstorage /for=c: /on=c: /maxsize=401MB
```


