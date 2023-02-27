---
title: "CAR-2021-05-003: BCDEdit Failure Recovery Modification"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
This search looks for flags passed to bcdedit.exe modifications to the built-in Windows error recovery boot configurations. This is typically used by ransomware to prevent recovery.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)|N/A|[Impact](https://attack.mitre.org/tactics/TA0040/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)|  
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Pseudocode – detect attempts to add a certificate to a certificate store (Pseudocode, CAR native)


Pseudocode implementation of the splunk search below


```
processes = search Process:Create
bcdedit_commands = filter processes where (
  exe = "C:\Windows\System32\bcdedit.exe" AND command_line="*recoveryenabled*" )
output bcedit_commands

```


#### Splunk code (Splunk, Endpoint)


You must be ingesting endpoint data that tracks process activity, including parent-child relationships from your endpoints to populate the Endpoint data model in the Processes node. Tune based on parent process names.


```
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name = bcdedit.exe Processes.process="*recoveryenabled*" (Processes.process="* no*") by Processes.process_name Processes.process Processes.parent_process_name Processes.dest Processes.user
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1490/atomic_red_team/windows-sysmon.log)  using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1490](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1490) against a Windows target.

```
Invoke-AtomicTest T1490
```


