---
title: "CAR-2021-05-012: Create Service In Suspicious File Path"
layout: analytic
submission_date: 2021/05/11
update_date: 2021/04/05
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
This detection is to identify a creation of "user mode service" where the service file path is located in non-common service folder in windows.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Services](https://attack.mitre.org/techniques/T1569/)|[Launchctl](https://attack.mitre.org/techniques/T1569/001/), [Service Execution](https://attack.mitre.org/techniques/T1569/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[service](/data_model/service) | [create](/data_model/service#create) | [image_path](/data_model/service#image_path) |



### Implementations

#### Pseudocode – Service in Suspicious File Path (Pseudocode, CAR native)


Pseudocode implementation of the Splunk search below.


```
services = search Service:create
suspicious_services = filter services where image_path = "*\.exe" AND image_path does not contain ["C:\\Windows\\*", "%windir%\\*", "C:\\Program File*", "C:\\Programdata\\*", "%systemroot%\\*"] )
output suspicious_services

```


#### Splunk code (Splunk, Endpoint)


To successfully implement this search, you need to be ingesting logs with the Service name, Service File Name Service Start type, and Service Type from your endpoints.


```
 `wineventlog_system` EventCode=7045  Service_File_Name = "*\.exe" NOT (Service_File_Name IN ("C:\\Windows\\*", "%windir%\\*", "C:\\Program File*", "C:\\Programdata\\*", "%systemroot%\\*")) Service_Type = "user mode service" | stats count min(_time) as firstTime max(_time) as lastTime by EventCode Service_File_Name Service_Name Service_Start_Type Service_Type
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/malware/clop/clop_a/windows-system.log) using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

execute the atomic test [T1569.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1569.001) against a Windows target.

```
Invoke-AtomicTest T1569.001
```


