---
title: "CAR-2014-03-006: RunDLL32.exe monitoring"
layout: analytic
submission_date: 2014/03/28
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Adversaries may find it necessary to use [Dyanamic-link Libraries](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682589.aspx) (DLLs) to [evade defenses](https://attack.mitre.org/tactics/TA0005). One way these DLLs can be "executed" is through the use of the built-in Windows utility [RunDLL32](https://attack.mitre.org/techniques/T1218.011), which allows a user to execute code in a DLL, providing the name and optional arguments to an exported entry point. Windows uses RunDll32 legitimately in its normal operation, but with a proper baseline and understanding of the environment, monitoring its usage could be fruitful.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|[Rundll32](https://attack.mitre.org/techniques/T1218/011/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


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

When looking for all instances of RunDLL32, it is imperative to also have the `command_line` information, which contains the DLL information, including the name, entry point, and optional arguments.


```
process = search Process:Create
rundll32 = filter process where (exe == "rundll32.exe")
output rundll32
```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=rundll32.exe limit 100
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\rundll32.exe"
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Execute rundll32.exe from a command window

```
c:\windows\syswow64\rundll32.exe
RUNDLL32.EXE SHELL32.DLL,Control_RunDLL desk.cpl,,0
```


