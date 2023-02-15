---
title: "CAR-2013-05-004: Execution with AT"
layout: analytic
submission_date: 2013/05/13
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
In order to gain [persistence](https://attack.mitre.org/tactics/TA0003/), [privilege escalation](https://attack.mitre.org/tactics/TA0004/), or [remote execution](https://attack.mitre.org/tactics/TA0002/), an adversary may use the Windows built-in command AT (at.exe) to [schedule a command](https://attack.mitre.org/techniques/T1053/002) to be run at a specified time, date, and even host. This method has been used by adversaries and administrators alike. Its use may lead to detection of compromised hosts and compromised users if it is used to move laterally.
The built-in Windows tool schtasks.exe ([CAR-2013-08-001](../CAR-2013-08-001)) offers greater flexibility when creating, modifying, and enumerating tasks. For these reasons, schtasks.exe is more commonly used by administrators, tools/scripts, and power users.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[At](https://attack.mitre.org/techniques/T1053/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/), [Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SJA | [Scheduled Job Analysis](https://d3fend.mitre.org/technique/d3f:ScheduledJobAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode

Instances of the process `at.exe` running imply the querying or creation of tasks. Although the command_line is not essential for the analytic to run, it is critical when identifying the command that was scheduled.


```
process = search Process:Create
at = filter process where (exe == "at.exe")
output at
```


#### Splunk, Sysmon native

Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ Image="C:\\Windows\\*\\at.exe"|stats values(CommandLine) as "Command Lines" by ComputerName
```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and process_name == "at.exe"
```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=at.exe limit 100
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\at.exe"
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

-   From an admin account, open Windows command prompt (right click, run as administrator).
-   Execute "at 10:00 calc.exe," substituting a time in the near future for 10:00.
-   The program should respond with “Added a new job with job ID = 1” where the job ID is dependent on what tasks are scheduled.
-   The program should execute at the time specified. This is what the analytic should fire on.
-   To remove the scheduled task, execute "at 1 /delete" where you replace "1" with the job ID output in step 2a above.

```
at 10:00 calc.exe // returns a job number X
at X /delete
```


