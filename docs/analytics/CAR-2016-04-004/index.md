---
title: "CAR-2016-04-004: Successful Local Account Login"
layout: analytic
submission_date: 2016/04/18
information_domain: Host
subtypes: Login
analytic_type: Situational Awareness
contributors: MITRE/NSA
---

The successful use of [Pass The Hash](https://attack.mitre.org/techniques/T1075/) for lateral movement between workstations would trigger event ID 4624, with an event level of Information, from the security log. This behavior would be a LogonType of 3 using NTLM authentication where it is not a domain logon and not the ANONYMOUS LOGON account.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Pass the Hash](https://attack.mitre.org/techniques/T1075/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### Implementations

#### Pseudocode

This analytic will look for remote logins, using a non domain login, from one host to another, using NTL authentication where the account is not "ANONYMOUS LOGON" 


```
EventCode == 4624 and [target_user_name] != "ANONYMOUS LOGON" and
[authentication_package_name] == "NTLM"
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

As an adminstrator, create a new user. Then, logon to the host with that new user. This is generate the event.

```
net user 'test' 'test' /add
```
