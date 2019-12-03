---
title: "CAR-2014-04-003: Powershell Execution"
layout: analytic
submission_date: 2014/04/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

[PowerShell](https://attack.mitre.org/techniques/T1086/) is a scripting environment included with Windows that is used by both attackers and administrators. Execution of PowerShell scripts in most Windows versions is opaque and not typically secured by antivirus which makes using PowerShell an easy way to circumvent security measures. This analytic detects execution of PowerShell scripts.

Powershell can be used to hide monitored command line execution such as:
-   `net use`
-   `sc start`


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[PowerShell](https://attack.mitre.org/techniques/T1086/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|High|
|[Scripting](https://attack.mitre.org/techniques/T1064/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |


### Implementations

#### Pseudocode

Look for versions of `PowerShell` that were not launched interactively.


```
process = search Process:Create
powershell = filter process where (exe == "powershell.exe" AND parent_exe != "explorer.exe" )
output powershell
```


#### Splunk, Sysmon native

Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\powershell.exe" ParentImage!="C:\\Windows\\explorer.exe"|stats values(CommandLine) as "Command Lines" values(ParentImage) as "Parent Images" by ComputerName
```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "powershell.exe" and parent_process_name != "explorer.exe")
```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=powershell.exe NOT $ParentProcess=regex(.*explorer.exe.*)i limit 30
```


