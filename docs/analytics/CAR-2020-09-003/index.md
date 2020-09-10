---
title: "CAR-2020-09-003: Indicator Blocking - Driver Unloaded"
layout: analytic
submission_date: 2020/09/10
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---

Adversaries may attempt to evade system defenses by unloading minifilter drivers used by host-based sensors such as Sysmon through the use of the fltmc command-line utility. Accordingly, this analytic looks for command-line invocations of this utility when used to unload minifilter drivers.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Impair Defenses](https://attack.mitre.org/techniques/T1562/)|[Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Implementations

#### Pseudocode - fltmc invocation (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
fltmc_processes = filter processes where (
  exe = "fltmc.exe" AND command_line = "*unload*")
output fltmc_processes
```


#### Splunk search - fltmc invocation (Splunk, Sysmon native)


This Splunk search looks for process create events for the fltmc.exe utility and the specific command line used to unload minifilter drivers.


```
index=client EventCode=1 CommandLine="*unload*" (Image="C:\\Windows\\SysWOW64\\fltMC.exe" OR Image="C:\\Windows\\System32\\fltMC.exe") 
```




