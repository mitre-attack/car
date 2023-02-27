---
title: "CAR-2020-11-001: Boot or Logon Initialization Scripts"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Registry, Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may schedule software to run whenever a user logs into the system; this is done to establish persistence and sometimes for lateral movement. This trigger is established through the registry key HKEY_CURRENT_USER\Environment*UserInitMprLogonScript*. This signature looks edits to existing keys or creation of new keys in that path. Users purposefully adding benign scripts to this path will result in false positives; that case is rare, however. There are other ways of running a script at startup or login that are not covered in this signature. Note that this signature overlaps with the Windows Sysinternals Autoruns tool, which would also show changes to this registry path.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037/)|[Logon Script (Windows)](https://attack.mitre.org/techniques/T1037/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SICA | [System Init Config Analysis](https://d3fend.mitre.org/technique/d3f:SystemInitConfigAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[registry](/data_model/registry) | [add](/data_model/registry#add) | [key](/data_model/registry#key) |
|[registry](/data_model/registry) | [edit](/data_model/registry#edit) | [key](/data_model/registry#key) |



### Implementations

#### Pseudocode - logon run script key added to registry using reg.exe on commandline, or new logon scipt keys in registry from any source. (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
logon_script_key_processes = filter processes where (
  command_line = "*reg*add*\Environment*UserInitMprLogonScript")
registry = search (Registry:Add OR Registry:Edit)
registry_logon_key_events = filter registry where (
  key = "*\Environment*UserInitMprLogonScript")
output (logon_script_key_processes, registry_logon_key_events)

```


#### Splunk Search -- logon scripts (Splunk, Sysmon native)


Look for commands for adding a logon script as a registry value, as well as direct registry events for the same thing.


```
(index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\System32\\reg.exe" CommandLine="*add*\\Environment*UserInitMprLogonScript") OR (index=__your_sysmon_index__ (EventCode=12 OR EventCode=14 OR EventCode=13) TargetObject="*\\Environment*UserInitMprLogonScript")

```


#### LogPoint Search -- logon scripts (Logpoint, LogPoint native)


Look for commands for adding a logon script as a registry value, as well as direct registry events for the same thing.


```
norm_id=WindowsSysmon ((event_id=1 image="C:\Windows\System32\reg.exe" command="*add*\Environment*UserInitMprLogonScript") OR (event_id IN [12, 13, 14] target_object="*\Environment*UserInitMprLogonScript"))

```




