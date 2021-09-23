---
title: "CAR-2021-01-002: Unusually Long Command Line Strings"
layout: analytic
submission_date: 2020/11/27
information_domain: Host
subtypes: Process
analytic_type: Anomaly
contributors: Cyware Labs
applicable_platforms: Windows
---

Often, after a threat actor gains access to a system, they will attempt to run some kind of malware to further infect the victim machine. These malware often have long command line strings, which could be a possible indicator of attack. Here, we use sysmon and Splunk to first find the average command string length and search for command strings that stretch over multiple lines, thus identifying anomalies and possibly malicious commands.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|N/A|[Execution](https://attack.mitre.org/tactics/TA0002/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Applicable Sensors

- [osquery_4.1.2](/sensors/osquery_4.1.2)
- [osquery_4.6.0](/sensors/osquery_4.6.0)
- [Sysmon_10.4](/sensors/sysmon_10.4)
- [Sysmon_11.0](/sensors/sysmon_11.0)
- [Sysmon_13](/sensors/sysmon_13)

### Implementations

#### Splunk search - Identifying possible malware activity via unusually long command line strings (Splunk, Sysmon native)


This is a Splunk query that determines the average length of a command per user and searches for a command string that is multiple times longer than the average length


```
index=* sourcetype="xmlwineventlog" EventCode=4688  |eval cmd_len=len(CommandLine) | eventstats avg(cmd_len) as avg by host| stats max(cmd_len) as maxlen, values(avg) as avgperhost by host, CommandLine | where maxlen > 10*avgperhost
```




