---
title: "CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
Adversaries may add their own root certificate to the certificate store, to cause the web browser to trust that certificate and not display a security warning when it encounters the previously unseen certificate. This action may be the precursor to malicious activity.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Subvert Trust Controls](https://attack.mitre.org/techniques/T1553/)|[Install Root Certificate](https://attack.mitre.org/techniques/T1553/004/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


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

#### Splunk code (Splunk, Endpoint)


You must be ingesting data that records process activity from your hosts to populate the Endpoint data model in the Processes node. You must also be ingesting logs with both the process name and command line from your endpoints. The command-line arguments are mapped to the "process" field in the Endpoint data model.


```
| tstats count min(_time) as firstTime values(Processes.process) as process max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=*certutil* (Processes.process=*-addstore*) by Processes.parent_process Processes.process_name Processes.user
```


#### Pseudocode – detect attempts to add a certificate to a certificate store (Pseudocode, CAR native)


Pseudocode implementation of the splunk search below


```
processes = search Process:Create
addstore_commands = filter processes where (
  exe =”C:\Windows\System32\certutil.exe” AND command_line="*-addstore*” )
output addstore_commands

```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1553.004/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1553.004](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1553.004) against a Windows target.

```
Invoke-AtomicTest T1553.004
```


