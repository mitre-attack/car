---
title: "CAR-2014-11-003: Debuggers for Accessibility Applications"
layout: analytic
submission_date: 2014/11/21
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
The Windows Registry location `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` allows for parameters to be set for applications during execution. One feature used by malicious actors is the "Debugger" option. When a key has this value enabled, a Debugging command line can be specified. Windows will launch the Debugging command line, and pass the original command line in as an argument. Adversaries can set a Debugger for [Accessibility Applications](https://attack.mitre.org/techniques/T1546/008). The analytic looks for the original command line as an argument to the Debugger. When the strings "sethc.exe", "utilman.exe", "osk.exe", "narrator.exe", and "Magnify.exe" are detected in the arguments, but not as the main executable, it is very likely that a Debugger is set.

This analytic could depend on the possibility of the known strings used as arguments for other applications used in the day-to-day environment. Although the chance of the string "sethc.exe" being used as an argument for another application is unlikely, it still is a possibility.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Event Triggered Execution](https://attack.mitre.org/techniques/T1546/)|[Accessibility Features](https://attack.mitre.org/techniques/T1546/008/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode

One simple way to implement this technique is to note that in a default Windows configuration there are no spaces in the path to the `system32` folder. If the accessibility programs are ever run with a Debugger set, then Windows will launch the Debugger process and append the command line to the accessibility program. As a result, a space is inserted in the command line before the path. Looking for any instances of a space in the command line before the name of an accessibility program will help identify when Debuggers are set.


```
process = search Process:Create
debuggers = filter process where (command_line match "$.* .*(sethc{{pipe}}utilman{{pipe}}osk{{pipe}}narrator{{pipe}}magnify)\.exe")
output debuggers

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 command IN ["$* *sethc.exe", "$* *utilman.exe", "$* *osk.exe", "$* *narrator.exe", "$* *magnify.exe"]

```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Although it does not actually utilize the Debugging command line, an easy way to test this analytic to run cmd.exe from a command window, supplying one of the strings as arguments.

```
cmd.exe Magnify.exe
```


