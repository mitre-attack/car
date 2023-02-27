---
title: "CAR-2013-02-008: Simultaneous Logins on a Host"
layout: analytic
submission_date: 2013/02/18
information_domain: Host
subtypes: Login
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
Multiple users logged into a single machine at the same time, or even within the same hour, do not typically occur in networks we have observed.

Logon events are Windows Event Code 4624 for Windows Vista and above, 518 for pre-Vista. Logoff events are 4634 for Windows Vista and above, 538 for pre-Vista.
Logon types 2, 3, 9 and 10 are of interest. For more details see the Logon Types table on Microsoft's [Audit Logon Events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc787567(v=ws.10)) page.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Valid Accounts](https://attack.mitre.org/techniques/T1078/)|[Domain Accounts](https://attack.mitre.org/techniques/T1078/002/), [Local Accounts](https://attack.mitre.org/techniques/T1078/003/)|[Initial Access](https://attack.mitre.org/tactics/TA0001/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-ANET | [Authentication Event Thresholding](https://d3fend.mitre.org/technique/d3f:AuthenticationEventThresholding)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[user_session](/data_model/user_session) | [login](/data_model/user_session#login) | [user](/data_model/user_session#user) |
|[user_session](/data_model/user_session) | [login](/data_model/user_session#login) | [hostname](/data_model/user_session#hostname) |



### Implementations

#### Pseudocode


```
users_list = search UserSession:Login
users_grouped = group users_list by hostname
users_grouped = from users_grouped select min(time) as earliest_time, max(time) as latest_time count(user) as user_count
multiple_logins = filter users_grouped where (latest_time - earliest_time <= 1 hour and user_count > 1)
output multiple_logins

```




