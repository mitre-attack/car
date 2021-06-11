---
title: "CAR-2020-09-001: Scheduled Task - FileAccess"
layout: analytic
submission_date: 2020/09/10
information_domain: Host
subtypes: File
analytic_type: Situational Awareness
contributors: Olaf Hartong
applicable_platforms: Windows
---

In order to gain persistence, privilege escalation, or remote execution, an adversary may use the Windows Task Scheduler to schedule a command to be run at a specified time, date, and even host. Task Scheduler stores tasks as files in two locations - C:\Windows\Tasks (legacy) or C:\Windows\System32\Tasks. Accordingly, this analytic looks for the creation of task files in these two locations.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)|[Execution](https://attack.mitre.org/tactics/TA0002/), [Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [file_path](/data_model/file#file_path) |
|[file](/data_model/file) | [create](/data_model/file#create) | [image_path](/data_model/file#image_path) |


### Applicable Sensors

- [Autoruns_13.98](/sensors/Autoruns_13.98)
- [osquery_4.1.2](/sensors/osquery_4.1.2)
- [osquery_4.6.0](/sensors/osquery_4.6.0)
- [Sysmon_10.4](/sensors/Sysmon_10.4)
- [Sysmon_11.0](/sensors/Sysmon_11.0)
- [Sysmon_13](/sensors/Sysmon_13)

### Implementations

#### Pseudocode - Windows task file creation (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
files = search File:Create
task_files = filter files where (
  (file_path = "C:\Windows\System32\Tasks\*" or file_path = "C:\Windows\Tasks\*")  and
  image_path != "C:\WINDOWS\system32\svchost.exe")
output task_files
```


#### Splunk search - Windows task file creation (Splunk, Sysmon native)


This Splunk search looks for any files created under the Windows tasks directories.


```
index=__your_sysmon_index__ EventCode=11 Image!="C:\\WINDOWS\\system32\\svchost.exe" (TargetFilename="C:\\Windows\\System32\\Tasks\\
*" OR TargetFilename="C:\\Windows\\Tasks\\*")
```


#### LogPoint search - Windows task file creation (Logpoint, LogPoint native)


This LogPoint search looks for any files created under the Windows tasks directories.


```
norm_id=WindowsSysmon event_id=11 -source_image="C:\WINDOWS\system32\svchost.exe" (path="C:\Windows\System32\Tasks*" OR path="C:\Windows\Tasks*")
```




