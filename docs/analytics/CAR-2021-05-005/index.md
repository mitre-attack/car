---
title: "CAR-2021-05-005: BITSAdmin Download File"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
The following query identifies Microsoft Background Intelligent Transfer Service utility `bitsadmin.exe` using the `transfer` parameter to download a remote object. In addition, look for `download` or `upload` on the command-line, the switches are not required to perform a transfer. Capture any files downloaded. Review the reputation of the IP or domain used. Typically once executed, a follow on command will be used to execute the dropped file. Note that the network connection or file modification events related will not spawn or create from `bitsadmin.exe`, but the artifacts will appear in a parallel process of `svchost.exe` with a command-line similar to `svchost.exe -k netsvcs -s BITS`. It's important to review all parallel and child processes to capture any behaviors and artifacts. In some suspicious and malicious instances, BITS jobs will be created. You can use `bitsadmin /list /verbose` to list out the jobs during investigation.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[BITS Jobs](https://attack.mitre.org/techniques/T1197/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)|N/A|[Command and Control](https://attack.mitre.org/tactics/TA0011/)|Moderate|


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

#### Pseudocode – detect BITS transfer jobs (Pseudocode, CAR native)


Pseudocode implementation of the Splunk search below


```
processes = search Process:Create
bitsadmin_commands = filter processes where (
  exe ="C:\Windows\System32\bitsadmin.exe" AND command_line = *transfer*)
output bitsadmin_commands

```


#### Splunk code (Splunk, Endpoint)


To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.


```
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=bitsadmin.exe Processes.process=*transfer* by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
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


