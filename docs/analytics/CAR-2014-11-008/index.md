---
title: "CAR-2014-11-008: Command Launched from WinLogon"
layout: analytic
submission_date: 2014/11/19
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
An adversary can use [accessibility features](https://attack.mitre.org/techniques/T1546/008) (Ease of Access), such as StickyKeys or Utilman, to launch a command shell from the logon screen and gain SYSTEM access. Since an adversary does not have physical access to the machine, this technique must be run within [Remote Desktop](https://attack.mitre.org/techniques/T1021/001). To prevent an adversary from getting to the login screen without first authenticating, Network-Level Authentication (NLA) must be enabled. If a debugger is set up for one of the accessibility features, then it will intercept the process launch of the feature and instead execute a new command line. This analytic looks for instances of `cmd.exe` or `powershell.exe` launched directly from the logon process, `winlogon.exe`. It should be used in tandem with [CAR-2014-11-003](../CAR-2014-11-003), which detects the accessibility programs in the command line.

Several accessibility programs can be run using the Ease of Access center

-   `sethc.exe` handles StickyKeys
-   `utilman.exe` is the Ease of Access menu
-   `osk.exe` runs the On-Screen Keyboard
-   `narrator.exe` reads screen text over audio
-   `magnify.exe` magnifies the view of the screen near the cursor


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
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode

Look for instances of processes where the parent executable is winlogon.exe and the child is an instance of a command prompt. 


```
processes = search Process:Create
winlogon_cmd = filter processes where (parent_exe == "winlogon.exe" and exe == "cmd.exe")
output winlogon_cmd
```


#### Splunk, Sysmon native

Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 ParentImage="C:\\Windows\\*\\winlogon.exe" Image="C:\\Windows\\*\\cmd.exe"
```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "cmd.exe" and parent_process_name == "winlogon.exe")
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 parent_image="C:\Windows\System32\winlogon.exe" parent_image="C:\Windows\System32\cmd.exe"
```




