---
title: "CAR-2013-02-003: Processes Spawning cmd.exe"
layout: analytic
submission_date: 2013/02/05
information_domain: Host
subtypes: Process
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
The Windows [Command Prompt](https://en.wikipedia.org/wiki/cmd.exe) (`cmd.exe`) is a utility that provides a command line interface to Windows operating systems. It provides the ability to run additional programs and also has several built-in commands such as `dir`, `copy`, `mkdir`, and `type`, as well as batch scripts (`.bat`). Typically, when a user runs a command prompt, the parent process is `explorer.exe` or another instance of the prompt. There may be automated programs, logon scripts, or administrative tools that launch instances of the command prompt in order to run scripts or other built-in commands. Spawning the process `cmd.exe` from certain parents may be more indicative of malice. For example, if Adobe Reader or Outlook launches a command shell, this may suggest that a malicious document has been loaded and should be investigated. Thus, by looking for abnormal parent processes of `cmd.exe`, it may be possible to detect adversaries.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[Windows Command Shell](https://attack.mitre.org/techniques/T1059/003/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode


```
process = search Process:Create
cmd = filter process where (exe == "cmd.exe")
output cmd
```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*cmd\.exe.*)i limit 100
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\cmd.exe"
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Within a command prompt or powershell, run cmd.exe


