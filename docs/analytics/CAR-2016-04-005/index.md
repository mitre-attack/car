---
title: "CAR-2016-04-005: Remote Desktop Logon"
layout: analytic
submission_date: 2016/04/19
information_domain: Host
subtypes: Login
analytic_type: Situational Awareness
contributors: MITRE/NSA
applicable_platforms: Windows
---

A remote desktop logon, through [RDP](https://attack.mitre.org/beta/techniques/T1021/001), may be typical of a system administrator or IT support, but only from select workstations. Monitoring remote desktop logons and comparing to known/approved originating systems can detect lateral movement of an adversary.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### Implementations

#### Pseudocode

Look in the system logs for remote logons using RDP.


```
[EventCode] == 4624 and
[AuthenticationPackageName] == 'Negotiate' and
[Severity] == "Information" and
[LogonType] == 10
```


#### Sigma

[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_admin_rdp_login.yml) of the above pseudocode, with some modifications.





