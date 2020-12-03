---
title: "CAR-2020-12-002:Unusual Child Process For Spoolsv.Exe Or Connhost.Exe"
layout: analytic
submission_date: 2020/12/03
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyware Labs
applicable_platforms: Windows
---

After gaining initial access to a system, threat actors attempt to escalate privileges as they may be operating within a lower privileged process which does not allow them to access protected information or carry out tasks which require higher permissions. A common way of escalating privileges in a system is by externally invoking and exploiting spoolsv or connhost executables, both of which are legitimate Windows applications. This query searches for an invocation of either of these executables by a user, thus alerting us of any potentially malicious activity.

### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)|None|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004 )|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |

### Implementations

#### Splunk search - Unusual Child Process For Spoolsv.exe Or Connhost.exe

This query looks for processes spawned by spoolsv.exe or connhost.exe externally, thus alerting us of potentially malicious activity.

```
index=* EventCode=1 (spoolsv.exe Image=*spoolsv.exe*) OR (connhost.exe Image=*connhost.exe*) ParentImage = "*cmd.exe*" |table _time host Image ProcessId ParentImage ParentProcessId
```
