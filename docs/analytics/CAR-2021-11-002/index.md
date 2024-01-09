---
title: "CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify"
layout: analytic
submission_date: 2021/11/28
information_domain: Host
subtypes: Process, Registry
analytic_type: TTP
contributors: Lucas Heiligenstein
applicable_platforms: Windows
---
<br><br>
Detection of modification of the registry key values of `Notify`, `Userinit`, and `Shell` located in `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\` and `HKEY_LOCAL_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\`. When a user logs on, the Registry key values of `Notify`, `Userinit` and `Shell` are used to load dedicated Windows component. Attackers may insert malicious payload following the legitimate value to launch a malicious payload.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)|[Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Medium|
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

#### Userinit/Shell/Notify Registry Modifications (Pseudocode, CAR native)


This detects logon registry key modification, either via a new process (command line) or direct registry manipulation.


```
processes = search Process:create
logon_reg_processes = filter processes where command_line CONTAINS("*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*") AND (command_line CONTAINS("*Userinit*") OR command_line CONTAINS("*Shell*") OR command_line CONTAINS("*Notify*")) AND (((command_line CONTAINS("*reg*") OR command_line CONTAINS("*add*") OR command_line CONTAINS("*/d*")) OR (command_line CONTAINS("*Set-ItemProperty*") OR command_line CONTAINS("*New-ItemProperty*") OR command_line CONTAINS("*-value*"))))
reg_keys = search Registry:value_edit
logon_reg_keys = filter reg_keys where (value="Userinit" OR value="Shell" OR value="Notify")
output logon_reg_processes, logon_reg_keys

```


#### Splunk Search - Modification of Userinit, Shell or Notify (Splunk)


This is a Splunk representation of the above pseudocode.


```
(((((EventCode="4688" OR EventCode="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR ((CommandLine="*Set-ItemProperty*" OR CommandLine="*New-ItemProperty*") CommandLine="*-value*")) CommandLine="*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*" (CommandLine="*Userinit*" OR CommandLine="*Shell*" OR CommandLine="*Notify*")) OR ((EventCode="4657") (ObjectValueName="Userinit" OR ObjectValueName="Shell" OR ObjectValueName="Notify"))) OR ((EventCode="13") (TargetObject="*Userinit" OR TargetObject="*Shell" OR TargetObject="*Notify"))))

```


#### Elastic Search - Modification of Userinit, Shell or Notify (Elastic)


This is an ElasticSearch representation of the above pseudocode.


```
(((EventCode:("4688" OR "1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:(*Set\-ItemProperty* OR *New\-ItemProperty*) AND process.command_line:*\-value*)) AND process.command_line:*\\Microsoft\\Windows\ NT\\CurrentVersion\\Winlogon* AND process.command_line:(*Userinit* OR *Shell* OR *Notify*)) OR (EventCode:"4657" AND winlog.event_data.ObjectValueName:("Userinit" OR "Shell" OR "Notify"))) OR (EventCode:"13" AND winlog.event_data.TargetObject:(*Userinit OR *Shell OR *Notify)))

```


#### LogPoint Search - Modification of Userinit, Shell or Notify (Logpoint)


This is a LogPoint representation of the above pseudocode.


```
(((EventCode IN ["4688", "1"] ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine IN ["*Set-ItemProperty*", "*New-ItemProperty*"] CommandLine="*-value*")) CommandLine="*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*" CommandLine IN ["*Userinit*", "*Shell*", "*Notify*"]) OR (EventCode IN "4657" ObjectValueName IN ["Userinit", "Shell", "Notify"])) OR (EventCode IN "13" TargetObject IN ["*Userinit", "*Shell", "*Notify"]))

```



### Unit Tests

#### Test Case 1

Modification on Registry Key with cmd. Calc.exe will be launched when user will login

```
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d C:\Windows\system32\userinit.exe,C:\Windows\system32\calc.exe
```

#### Test Case 2

Modification on Registry Key with Powershell. Calc.exe will be launched when user will login

```
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name Userinit -Value C:\Windows\system32\userinit.exe,C:\Windows\system32\calc.exe
```


