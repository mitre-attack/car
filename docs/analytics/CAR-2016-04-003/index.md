---
title: "CAR-2016-04-003: User Activity from Stopping Windows Defensive Services"
layout: analytic
submission_date: 2016/04/15
information_domain: Host
subtypes: Process
analytic_type: Situational Awareness
contributors: MITRE/NSA
---

Spyware and malware remain a serious problem and Microsoft developed security services, Windows Defender and Windows Firewall, to combat this threat. In the event Windows Defender or Windows Firewall is turned off, administrators should correct the issue immediately to prevent the possibility of infection or further infection and investigate to determine if caused by crash or user manipulation.

Stopping services events are Windows Event Code 7036.


### ATT&CK Detection
|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Indicator Blocking](https://attack.mitre.org/techniques/T1054/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### Implementations

#### Pseudocode

Windows Event code 7036 from the System log identifies if a service has stopped or started. This analytic looks for "Windows Defender" or "Windows Firewall" that has stopped.


```
log_name == "System" AND
event_code == "7036"
param1 in ["Windows Defender", "Windows Firewall"] AND
param2 == "stopped"
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

From an administrative user powershell console, run the Stop-Service command.

```
Stop-Service -displayname "Windows Firewall"
Stop-Service -displayname "Windows Defender"
```
