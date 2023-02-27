---
title: "CAR-2016-03-002: Create Remote Process via WMIC"
layout: analytic
submission_date: 2016/03/28
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Adversaries may use [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to move laterally, by launching executables remotely.The analytic [CAR-2014-12-001](../CAR-2014-12-001) describes how to detect these processes with network traffic monitoring and process monitoring on the target host. However, if the command line utility `wmic.exe` is used on the source host, then it can additionally be detected on an analytic. The command line on the source host is constructed into something like `wmic.exe /node:"\<hostname\>" process call create "\<command line\>"`. It is possible to also connect via IP address, in which case the string `"\<hostname\>"` would instead look like `IP Address`.

Although this analytic was created after [CAR-2014-12-001](../CAR-2014-12-001), it is a much simpler (although more limited) approach. Processes can be created remotely via WMI in a few other ways, such as more direct API access or the built-in utility [PowerShell](https://attack.mitre.org/T1059/001).



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)|N/A|[Execution](https://attack.mitre.org/tactics/TA0002/)|Low|


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

#### Pseudocode

Looks for instances of wmic.exe as well as the substrings in the command line:
* `process call create`
* `/node:`



```
processes = search Process:Create
wmic = filter processes where (exe == "wmic.exe" and command_line == "* process call create *" and command_line == "* /node:*")
output wmic

```


#### Splunk, Sysmon native

Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\wmic.exe" CommandLine="* process call create *"|search CommandLine="* /node:*"

```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "wmic.exe" and command_line == "* process call create ")
  |filter command_line == "* /node:*"

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="C:\\Windows\\*\\wmic.exe" command="* process call create *" command="* /node:*"

```




