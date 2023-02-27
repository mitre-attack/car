---
title: "CAR-2021-05-011: Create Remote Thread into LSASS"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
Actors may create a remote thread into the LSASS service as part of a workflow to dump credentials.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SCA | [System Call Analysis](https://d3fend.mitre.org/technique/d3f:SystemCallAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[thread](/data_model/thread) | [remote_create](/data_model/thread#remote_create) | [](/data_model/thread#) |



### Implementations

#### Pseudocode – Remote thread creation into LSASS (Pseudocode, CAR native)


Pseudocode implementation of the Splunk search below. The CAR data model does not currently contain a Target Image field, for remote thread creation, so this code Is somewhat inexact. See the Splunk implementation for a more precise search for the lsass image target.


```
remote_threads = search Thread:remote_create
lsass_remote_create = filter remote_threads where "lsass" in raw event
output lsass_remote_create

```


#### Splunk code (Splunk, )


This search needs Sysmon Logs with a Sysmon configuration, which includes EventCode 8 with lsass.exe. This search uses an input macro named `sysmon`. We strongly recommend that you specify your environment-specific configurations (index, source, sourcetype, etc.) for Windows Sysmon logs. Replace the macro definition with configurations for your Splunk environment. The search also uses a post-filter macro designed to filter out known false positives.



```
`sysmon` EventID=8 TargetImage=*lsass.exe | stats count min(_time) as firstTime max(_time) as lastTime by Computer, EventCode, TargetImage, TargetProcessId | rename Computer as dest
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1003.001/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below


```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1003.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1003.001) against a Windows target.

```
Invoke-AtomicTest T1003.001
```


