---
title: "CAR-2021-05-008: Certutil exe certificate extraction"
layout: analytic
submission_date: 2021/05/11
information_domain: Analytic
subtypes: Process
analytic_type: TTP
contributors: Splunk Threat Research <research@splunk.com>
applicable_platforms: Windows
---
<br><br>
This search looks for arguments to certutil.exe indicating the manipulation or extraction of Certificate. This certificate can then be used to sign new authentication tokens specially inside Federated environments such as Windows ADFS.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Forge Web Credentials](https://attack.mitre.org/techniques/T1606/)|[SAML Tokens](https://attack.mitre.org/techniques/T1606/002/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Moderate|


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
  exe =”C:\Windows\System32\certutil.exe” AND command_line = * -exportPFX * )
output certutil_downloads

```


#### Splunk code (Splunk, Endpoint)


Splunk implementation


```
| tstats count min(_time) as firstTime values(Processes.process) as process max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=certutil.exe Processes.process = "* -exportPFX *" by Processes.parent_process Processes.process_name Processes.process Processes.user
```



### Unit Tests

#### Test Case 1

**Configurations:** Using Splunk [Attack Range](https://github.com/splunk/attack_range)

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/suspicious_behaviour/certutil_exe_certificate_extraction/windows-sysmon.log) using the Splunk attack range with the commands below

```
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

#### Test Case 2

**Configurations:** Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

Execute the atomic test [T1606.002](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1606.002) against a Windows target.

```
Invoke-AtomicTest T1606.002
```


