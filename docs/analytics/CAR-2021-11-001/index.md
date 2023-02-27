---
title: "CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0"
layout: analytic
submission_date: 2021/11/24
information_domain: Host
subtypes: Process, Registry
analytic_type: TTP
contributors: Lucas Heiligenstein
applicable_platforms: Windows
---
<br><br>
Detection of creation of registry key HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode. The key SafeDllSearchMode, if set to 0, will block the Windows mechanism for the search DLL order and adversaries may execute their own malicious dll.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|[DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Medium|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Medium|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[registry](/data_model/registry) | [add](/data_model/registry#add) | [key](/data_model/registry#key) |



### Implementations

#### Creation of SafeDllSearchMode (Pseudocode, CAR native)


This detects SafeDllSearchMode creation, either via a new process (command line) or direct registry manipulation.


```
processes = search Process:create
safe_dll_search_processes = filter processes where command_line CONTAINS("*SafeDllSearchMode*") AND ((command_line CONTAINS("*reg*") AND command_line CONTAINS("*add*") AND command_line CONTAINS("*/d*")) OR (command_line CONTAINS("*Set-ItemProperty*") AND command_line CONTAINS(*-value*)) OR ((command_line CONTAINS("*00000000*") AND command_line CONTAINS(*0*)))
reg_keys = search Registry:value_edit
safe_dll_reg_keys = filter reg_keys where value="SafeDllSearchMode" AND value_data="0"
output safe_dll_search_processes, safe_dll_reg_keys

```


#### Splunk Search - Creation of SafeDllSearchMode (Splunk, Win. Eventlog/Sysmon native)


This is a Splunk representation of the above pseudocode.


```
(source="WinEventLog:*" ((((EventCode="4688" OR EventCode="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) (CommandLine="*00000000*" OR CommandLine="*0*") CommandLine="*SafeDllSearchMode*") OR ((EventCode="4657") ObjectValueName="SafeDllSearchMode" value="0")) OR ((EventCode="13") EventType="SetValue" TargetObject="*SafeDllSearchMode" Details="DWORD (0x00000000)")))

```


#### Elastic Search - Creation of SafeDllSearchMode (Elastic, Win. Eventlog/Sysmon native)


This is an Elastic representation of the above pseudocode.


```
(((EventCode:("4688" OR "1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:*Set\-ItemProperty* AND process.command_line:*\-value*)) AND process.command_line:(*00000000* OR *0*) AND process.command_line:*SafeDllSearchMode*) OR (EventCode:"4657" AND winlog.event_data.ObjectValueName:"SafeDllSearchMode" AND value:"0")) OR (EventCode:"13" AND winlog.event_data.EventType:"SetValue" AND winlog.event_data.TargetObject:*SafeDllSearchMode AND winlog.event_data.Details:"DWORD\ \(0x00000000\)"))

```


#### LogPoint Search - Creation of SafeDllSearchMode (Logpoint, Win. Eventlog/Sysmon native)


This is a LogPoint representation of the above pseudocode.


```
(((EventCode IN ["4688", "1"] ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) CommandLine IN ["*00000000*", "*0*"] CommandLine="*SafeDllSearchMode*") OR (EventCode IN "4657" ObjectValueName="SafeDllSearchMode" value="0")) OR (EventCode IN "13" EventType="SetValue" TargetObject="*SafeDllSearchMode" Details="DWORD (0x00000000)"))

```



### Unit Tests

#### Test Case 1

Execute command with cmd

```
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode /d 0
```

#### Test Case 2

Execute command with powershell

```
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Session Manager" -Name SafeDllSearchMode -Value 0
```


