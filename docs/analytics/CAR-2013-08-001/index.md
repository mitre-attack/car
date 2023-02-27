---
title: "CAR-2013-08-001: Execution with schtasks"
layout: analytic
submission_date: 2013/08/07
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
The Windows built-in tool `schtasks.exe` provides the creation, modification, and running of [scheduled tasks](https://attack.mitre.org/techniques/T1053) on a local or remote computer. It is provided as a more flexible alternative to `at.exe`, described in [CAR-2013-05-004](../CAR-2013-05-004). Although used by adversaries, the tool is also legitimately used by administrators, scripts, and software configurations. The scheduled tasks tool can be used to gain [Persistence](https://attack.mitre.org/tactics/TA0003) and can be used in combination with a [Lateral Movement](https://attack.mitre.org/tactics/TA0008) technique to remotely gain [execution](https://attack.mitre.org/tactics/TA0002). Additionally, the command has parameters to specify the user and password responsible for creating the task, as well as the user and password combination that the task will run as. The `/s` flag specifies the remote system on which the task should be scheduled, usually indicating [Lateral Movement](https://attack.mitre.org/tactics/TA0008).


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SJA | [Scheduled Job Analysis](https://d3fend.mitre.org/technique/d3f:ScheduledJobAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Pseudocode

Look for instances of `schtasks.exe` running as processes. The `command_line` field is necessary to disambiguate between types of schtasks commands. These include the flags `/create`, `/run`, `/query`, `/delete`, `/change`, and `/end`.


```
process = search Process:Create
schtasks = filter process where (exe == "schtasks.exe")
output schtasks

```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=schtasks.exe AND $Process=regex(.*(\/create|\/run|\/query|\/delete|\/change|\/end).*)i limit 100

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\schtasks.exe" command IN ["*/create*", "*/run*", "*/query*", "*/delete*", "*/change*", "*/end*"]

```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Create a new scheduled task with schtasks.exe and verify the analytic fires when the task executes.
* From an admin account, open Windows command prompt (right click, run as administrator)
* Execute `schtasks /Create /SC ONCE /ST 19:00 /TR C:\Windows\System32\calc.exe /TN calctask`, substituting a time in the near future for 19:00
* The program should respond with “SUCCESS: The scheduled task “calctask” has successfully been created.”
* The program should execute at the time specified. This is what the analytic should fire on.
* To remove the scheduled task, execute `schtasks /Delete /TN calctask`.
* The program should respond with “SUCCESS: The scheduled task “calctask” was successfully deleted.”


```
schtasks /Create /SC ONCE /ST 19:00 /TR C:\Windows\System32\calc.exe /TN calctask
schtasks /Delete /TN calctask
```


