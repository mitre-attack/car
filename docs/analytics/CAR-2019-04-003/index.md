---
title: "CAR-2019-04-003: Squiblydoo"
layout: analytic
submission_date: 2019/04/24
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Squiblydoo is a specific usage of regsvr32.dll to load a COM scriptlet directly from the internet and execute it in a way that bypasses application whitelisting. It can be seen by looking for regsvr32.exe executions that load the scrobj.dll (which execute the COM scriptlet) or, if that is too noisy, those that also load content directly via HTTP or HTTPS.

Squiblydoo was first written up by Casey Smith at Red Canary, though that blog post is no longer accessible.


#### References
As usual, credit to Roberto Rodriguez and the [ThreatHunter Playbook](https://github.com/Cyb3rWard0g/ThreatHunter-Playbook/blob/master/playbooks/platforms/windows/05_defense_evasion/regsvr32/variants/bypass_whitelisting_regsvr32.md).


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|[Regsvr32](https://attack.mitre.org/techniques/T1218/010/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


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

#### Splunk, Sysmon native

This looks for any and all usage of the scrobj DLL, which is what is used to run COM scriptlets, so it'll detect both loading from network as well as filesystem. This will have almost zero false positives so is suitable for alerting.


```
index=__your_sysmon_events__ EventCode=1 regsvr32.exe scrobj.dll | search Image="*regsvr32.exe"

```


#### Eql, EQL native

EQL version of the above Splunk search.


```
process where subtype.create and
  (process_path == "*regsvr32.exe" and command_line == "*scrobj.dll")

```


#### Psuedocode, CAR

Pseudocode version of the above Splunk search.


```
processes = search Process:Create
squiblydoo_processes = filter processes where (
  image_path == "*regsvr32.exe" and command_line == "*scrobj.dll"
  )
output squiblydoo_processes

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\regsvr32.exe" command="*scrobj.dll"

```



### Unit Tests

#### Test Case 1

The [Atomic Red Team test for Squiblydoo](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1117/T1117.md#atomic-test-2---regsvr32-remote-com-scriptlet-execution) is a good test case for this.



