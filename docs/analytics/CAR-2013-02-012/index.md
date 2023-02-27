---
title: "CAR-2013-02-012: User Logged in to Multiple Hosts"
layout: analytic
submission_date: 2013/02/27
information_domain: Host
subtypes: Login
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
Most users use only one or two machines during the normal course of business. User accounts that log in to multiple machines, especially over a short period of time, may be compromised. Remote logins among multiple machines may be an indicator of [Lateral Movement](https://attack.mitre.org/tactics/TA0008).

Certain users will likely appear as being logged into several machines and may need to be "whitelisted." Such users would include network admins or user names that are common to many hosts.

### Output Description

User Name, Machines logged into, the earliest and latest times in which users were logged into the host, the type of logon, and logon ID.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Valid Accounts](https://attack.mitre.org/techniques/T1078/)|[Domain Accounts](https://attack.mitre.org/techniques/T1078/002/), [Local Accounts](https://attack.mitre.org/techniques/T1078/003/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-ANET | [Authentication Event Thresholding](https://d3fend.mitre.org/technique/d3f:AuthenticationEventThresholding)| 






