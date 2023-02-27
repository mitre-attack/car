---
title: "CAR-2019-07-002: Lsass Process Dump via Procdump"
layout: analytic
submission_date: 2019/07/29
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Kaushal Parikh/Cyware Labs, Tony Lambert/Red Canary, MITRE
applicable_platforms: Windows
---
<br><br>
[ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) is a sysinternal command-line utility whose primary purpose is monitoring an application for CPU spikes and generating crash dumps during a spike that an administrator or developer can use to determine the cause of the spike.

ProcDump may be used to dump the memory space of lsass.exe to disk for processing with a credential access tool such as Mimikatz. This is performed by launching procdump.exe as a privileged user with command line options indicating that lsass.exe should be dumped to a file with an arbitrary name.

Note - the CAR data model currently does not support process access actions, so the pseudocode implementation is based around process creates.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


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

#### Procdump - Process Create (Pseudocode)


This base pseudocode looks for process create events where an instance of procdump is executed that references lsass in the command-line.


```
processes = search Process:Create
procdump_lsass = filter processes where (
  exe = "procdump*.exe"  and
  command_line = "*lsass*")
output procdump_lsass

```


#### Procdump - Process Create (Splunk, Sysmon native)


A Splunk/Sysmon version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="*\\procdump*.exe" CommandLine="*lsass*"

```


#### Procdump - Process Create (Eql)


An [EQL Version](https://eqllib.readthedocs.io/en/latest/analytics/1e1ef6be-12fc-11e9-8d76-4d6bb837cda4.html) of the above pseudocode.



#### Procdump - Process Access (Splunk, Sysmon native)


A related Splunk search, which instead of looking for process create events looks for process access events that target lsass.exe.


```
index=__your_sysmon_index__ EventCode=10 TargetImage="C:\\WINDOWS\\system32\\lsass.exe" GrantedAccess="0x1FFFFF" ("procdump")

```


#### Procdump - Process Access (Sigma)


A [Sigma Version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_lsass_memdump.yml) of the above Splunk search, with some more stringent criteria around calltrace.



#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\procdump*.exe" command="*lsass*"

```



### Unit Tests

#### Test Case 1

1. Open a Windows Command Prompt or PowerShell instance.
2. Navigate to folder containing ProcDump.
3. Execute procdump.exe -ma lsass.exe lsass_dump



