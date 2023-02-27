---
title: "CAR-2021-05-010: Create local admin accounts using net exe"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
This search looks for the creation of local administrator accounts using net.exe.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Create Account](https://attack.mitre.org/techniques/T1136/)|[Local Account](https://attack.mitre.org/techniques/T1136/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


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

#### Pseudocode – CertUtil certificate extraction (Pseudocode, CAR native)


Pseudocode implementation of the Splunk search below


```
processes = search Process:Create
certutil_downloads = filter processes where (
  (exe = C:\Windows\System32\net.exe OR exe = C:\Windows\System32\net1.exe ) AND command_line = * -exportPFX * )
output certutil_downloads

```


#### Splunk code (Splunk, Endpoint)


You must be ingesting data that records process activity from your hosts to populate the Endpoint data model in the Processes node. You must also be ingesting logs with both the process name and command line from your endpoints. The command-line arguments are mapped to the "process" field in the Endpoint data model.


```
| tstats count values(Processes.user) as user values(Processes.parent_process) as parent_process min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where (Processes.process_name=net.exe OR Processes.process_name=net1.exe) AND (Processes.process=*localgroup* OR Processes.process=*/add* OR Processes.process=*user*) by Processes.process Processes.process_name Processes.dest   |`create_local_admin_accounts_using_net_exe_filter`
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1136.001/atomic_red_team/windows-security.log)  using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1136.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1136.001) against a Windows target.

```
Invoke-AtomicTest T1136.001
```


