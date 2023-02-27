---
title: "CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'"
layout: analytic
submission_date: 2021/12/06
information_domain: Host
subtypes: Process, Registry
analytic_type: TTP
contributors: Lucas Heiligenstein
applicable_platforms: Windows
---
<br><br>
Detection of the modification of the registry key `Common Startup` located in `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\`. When a user logs on, any files located in the Startup Folder are launched. Attackers may modify these folders with other files in order to evade detection set on these default folders. This detection focuses on EventIDs 4688 and 1 for process creation and EventID 4657 for the modification of the Registry Keys.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)|[Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Medium|
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

#### Common Startup Registry Key Modification (Pseudocode, CAR native)


This detects modification of the `Common Startup` registry key value, either via a new process (command line) or direct registry manipulation.


```
processes = search Process:create
logon_reg_processes = filter processes where (command_line CONTAINS("*reg*") AND command_line CONTAINS("*add*") AND command_line CONTAINS("*/d*") OR (command_line CONTAINS("*Set-ItemProperty*") AND command_line CONTAINS("*-value*")) AND command_line CONTAINS("*Common Startup*"))
reg_keys = search Registry:value_edit
logon_reg_keys = filter reg_keys where value="Common Startup"
output logon_reg_processes, logon_reg_keys

```


#### Splunk Search - Modification of default Startup Folder in the Registry Key "Common Startup" (Splunk)


This is a Splunk representation of the above pseudocode search.


```
(((EventCode="4688" OR EventCode="1") (CommandLine="*reg*" AND CommandLine="*add*" AND CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" AND CommandLine="*-value*") CommandLine="*Common Startup*") OR ((EventCode="4657" ObjectValueName="Common Startup") OR (EventCode="13" TargetObject="*Common Startup")))

```


#### Elastic Search - Modification of default Startup Folder in the Registry Key "Common Startup" (Elastic)


This is an ElasticSeearech representation of the above pseudocode search.


```
((EventLog:"Security" AND (winlog.event_id:"4688" OR winlog.event_id:"1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:*Set\-ItemProperty* AND process.command_line:*\-value*)) AND process.command_line:*Common\ Startup*) OR (winlog.event_id:"4657" AND winlog.event_data.ObjectValueName:"Common\ Startup") OR (winlog.event_id:"13" AND winlog.event_data.TargetObject:"*Common Startup"))

```


#### LogPoint Search - Modification of default Startup Folder in the Registry Key "Common Startup" (Logpoint)


This is a LogPoint representation of the above pseudocode search.


```
((EventLog="Security" (event_id="4688" OR event_id="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) CommandLine="*Common Startup*") OR (event_id="4657" ObjectValueName="Common Startup") OR (event_id="13" TargetObject="*Common Startup"))

```



### Unit Tests

#### Test Case 1

Modification on Registry Key with cmd. Files in new_malicious_startup_folder will be launched when user logon

```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v "Common Startup" /d "C:\Users\Lucas\Documents\new_malicious_startup_folder" /f
```

#### Test Case 2

Modification on Registry Key with Powershell. Files in new_malicious_startup_folder will be launched when user logon

```
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Common Startup" -Value C:\Users\Lucas\Documents\new_malicious_startup_folder
```


