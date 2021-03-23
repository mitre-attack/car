---
title: "CAR-2021-01-006: Unusual Child Process spawned using DDE exploit"
layout: analytic
submission_date: 2020/12/03
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Inter-Process Communication](https://attack.mitre.org/techniques/T1559/)|[Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Implementations

#### Splunk search - Unusual Child Process spawned using DDE exploit (Splunk, Sysmon native)


This Splunk query looks for any executable invocations from an Excel file.


```
index = __sysmon__index__ (ParentImage="*excel.exe" OR ParentImage="*word.exe" OR ParentImage="*outlook.exe") Image="*.exe"
```


#### Splunk search - Unusual Child Process spawned using DDE exploit (Pseudocode)


This Splunk query looks for any executable invocations from an Excel file.


```
processes = search Process:Create
target_processes = filter processes where (
     (parent_image="*excel.exe" OR parent_image="*word.exe" OR parent_image="*outlook.exe")
     AND image="*.exe"
     )
```




