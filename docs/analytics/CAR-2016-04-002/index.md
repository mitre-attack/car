---
title: "CAR-2016-04-002: User Activity from Clearing Event Logs"
layout: analytic
submission_date: 2016/04/14
information_domain: Host
subtypes: Event Records
analytic_type: Anomaly
contributors: MITRE/NSA
applicable_platforms: Windows, Linux, macOS
---

It is unlikely that event log data would be cleared during normal operations, and it is likely that malicious attackers may try to cover their tracks by clearing an event log. When an event log gets cleared, it is suspicious. Alerting when a "Clear Event Log" is generated could point to this intruder technique. Centrally collecting events has the added benefit of making it much harder for attackers to cover their tracks. Event Forwarding permits sources to forward multiple copies of a collected event to multiple collectors, thus enabling redundant event collection. Using a redundant event collection model can minimize the single point of failure risk.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Indicator Removal on Host](https://attack.mitre.org/beta/techniques/T1551/)|N/A|[Defense Evasion](https://attack.mitre.org/beta/tactics/TA0005/)|Moderate|


### Implementations

#### Pseudocode

When an eventlog is cleared, a new event is created that alerts that the eventlog was cleared. For Security logs, its event code 1100 and 1102. For System logs, it is event code 104.


```
([log_name] == "Security" and [event_code] in [1100, 1102]) or
([log_name] == "System" and [event_code] == 104)
```


#### Sigma rule (System log) (Sigma)


[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_susp_eventlog_cleared.yml) of the above pseudocode, focusing only on the System log.



#### Sigma rule (Security log) (Sigma)


[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_susp_security_eventlog_cleared.yml) of the above pseudocode, focusing only on the Security log.




### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

You can use the powershell cmdlet “Clear-Eventlog” to clear event logs. Open Powershell as administrator and execute Clear-Eventlog `Clear-EventLog [-LogName] \<String[]\>`. [Additional information here](https://technet.microsoft.com/en-us/library/hh849789.aspx).

```
Clear-Eventlog Security
Clear-Eventlog System
```


