---
title: "CAR-2021-05-004: BITS Job Persistence"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
The following query identifies Microsoft Background Intelligent Transfer Service utility `bitsadmin.exe` scheduling a BITS job to persist on an endpoint. The query identifies the parameters used to create, resume or add a file to a BITS job. Typically seen combined in a oneliner or ran in sequence. If identified, review the BITS job created and capture any files written to disk. It is possible for BITS to be used to upload files and this may require further network data analysis to identify. You can use `bitsadmin /list /verbose` to list out the jobs during investigation.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[BITS Jobs](https://attack.mitre.org/techniques/T1197/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


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

#### Pseudocode – detect a BITS job being scheduled (Pseudocode, CAR native)


Pseudocode implementation of the splunk search below


```
processes = search Process:Create
bitsadmin_commands = filter processes where (
  exe ="C:\Windows\System32\bitsadmin.exe" AND command_line includes one of [*create*, *addfile*, *setnotifyflags*, *setnotifycmdline*, *setminretrydelay*, *setcustomheaders*,*resume*])
output bitsadmin_commands

```


#### Splunk code (Splunk, Endpoint)


To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.


```
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=bitsadmin.exe Processes.process IN (*create*, *addfile*, *setnotifyflags*, *setnotifycmdline*, *setminretrydelay*, *setcustomheaders*, *resume* ) by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1197/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1197](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1197) against a Windows target.

```
Invoke-AtomicTest T1197
```


