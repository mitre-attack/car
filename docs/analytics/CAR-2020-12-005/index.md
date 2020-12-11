---
title: "CAR-2020-12-005:Detecting Tampering of Windows Defender Command Prompt"
layout: analytic
submission_date: 2020/12/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---

In an attempt to avoid detection after compromising a machine, threat actors often try to disable Windows Defender. This is often done using “sc” (service control), a legitimate tool provided by Microsoft for managing services. This action interferes with event detection and may lead to a security event going undetected, thereby potentially leading to further compromise of the network.

### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Impair Defenses](https://attack.mitre.org/techniques/T1562/)|[Disable or modify tools](https://attack.mitre.org/techniques/T1562/001/)|[Defense evasion](https://attack.mitre.org/tactics/TA0005 )|Medium|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |

### Implementations

#### Splunk search - Detecting Tampering of Windows Defender Command Prompt

This query looks for the specific use of service control for querying or trying to stop Windows Defender.

```
index=* EventCode=1 Image = *sc.exe* CommandLine="*stop WinDefend*" OR CommandLine="*config WinDefend*" OR CommandLine="*query WinDefend*"
| table _time host Image CommandLine
```
