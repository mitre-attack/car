---
title: "CAR-2016-04-003: User Activity from Stopping Windows Defensive Services"
layout: analytic
submission_date: 2016/04/15
information_domain: Host
subtypes: Process
analytic_type: Situational Awareness
contributors: MITRE/NSA
applicable_platforms: Windows
---
<br><br>
Spyware and malware remain a serious problem and Microsoft developed security services, Windows Defender and Windows Firewall, to combat this threat. In the event Windows Defender or Windows Firewall is turned off, administrators should correct the issue immediately to prevent the possibility of infection or further infection and investigate to determine if caused by crash or user manipulation.

Stopping services events are Windows Event Code 7036.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Impair Defenses](https://attack.mitre.org/techniques/T1562/)|[Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SDM | [System Daemon Monitoring](https://d3fend.mitre.org/technique/d3f:SystemDaemonMonitoring)| 





### Implementations

#### Pseudocode

Windows Event code 7036 from the System log identifies if a service has stopped or started. This analytic looks for "Windows Defender" or "Windows Firewall" that has stopped.


```
log_name == "System" AND
event_code == "7036"
param1 in ["Windows Defender", "Windows Firewall"] AND
param2 == "stopped"

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WinServer channel="System" event_id=7036 param1 in ["Windows Defender", "Windows Firewall"] param2="stopped"

```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

From an administrative user powershell console, run the Stop-Service command.

```
Stop-Service -displayname "Windows Firewall"
Stop-Service -displayname "Windows Defender"
```


