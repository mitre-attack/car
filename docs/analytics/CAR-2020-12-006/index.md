---
title: "CAR-2020-12-006:Detect disabling of UAC via reg.exe"
layout: analytic
submission_date: 2020/12/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---

Threat actors often, after compromising a machine, try to disable User Access Control (UAC) to escalate privileges. This is often done by changing the registry key for system policies using “reg.exe”, a legitimate tool provided by Microsoft for modifying the registry via command prompt or scripts. This action interferes with UAC and may enable a threat actor to escalate privileges on the compromised system, thereby allowing further exploitation of the system.

### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)|[Bypass User Account Control](https://attack.mitre.org/techniques/T1562/002/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004 )|Medium|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |

### Implementations

#### Splunk search - Detect disabling of UAC via reg.exe

This query looks for the specific use of reg.exe in correlation to commands aimed at disabling UAC

```
index = * ParentImage = *cmd* CommandLine ="*reg.exe*" AND CommandLine = "*REG_DWORD*" AND CommandLine = "*/d 0*" "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" | table _time host User CommandLine
```
