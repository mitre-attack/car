---
title: "CAR-2021-05-002: Batch File Write to System32"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
While batch files are not inherently malicious, it is uncommon to see them created after OS installation, especially in the Windows directory. This analytic looks for the suspicious activity of a batch file being created within the C:\Windows\System32 directory tree. There will be only occasional false positives due to administrator actions.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[User Execution](https://attack.mitre.org/techniques/T1204/)|[Malicious File](https://attack.mitre.org/techniques/T1204/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [extension](/data_model/file#extension) |
|[file](/data_model/file) | [create](/data_model/file#create) | [file_path](/data_model/file#file_path) |



### Implementations

#### Pseudocode – Batch file created in the Windows system32 directory tree (Pseudocode, CAR native)


Pseudocode implementation of the Splunk search below


```
files = search File:create
batch_files = filter files where (
  extension =".bat" AND file_path = "C:\Windows\system32*" )
output batch_files

```


#### Splunk code (Splunk, Endpoint)


You must be ingesting data that records the file-system activity from your hosts to populate the Endpoint file-system data-model node. If you are using Sysmon, you will need a Splunk Universal Forwarder on each endpoint from which you want to collect data.


```
| tstats count min(_time) as firstTime max(_time) as lastTime values(Filesystem.dest) as dest values(Filesystem.file_name) as file_name values(Filesystem.user) as user from datamodel=Endpoint.Filesystem by Filesystem.file_path   | rex field=file_name "(?<file_extension>\.[^\.]+)$" | search file_path=*system32* AND file_extension=.bat
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1204.002/batch_file_in_system32/windows-sysmon.log) using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1204.002](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1204.002) against a Windows target.

```
Invoke-AtomicTest T1204.002
```


