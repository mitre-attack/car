---
title: "CAR-2019-07-002: Access Permission Modification"
layout: analytic
submission_date: 2019/07/29
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Kaushal Parikh, MITRE
---

[ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) is a sysinternal command-line utility whose primary purpose is monitoring an application for CPU spikes and generating crash dumps during a spike that an administrator or developer can use to determine the cause of the spike. 

Procdump is also used by attackers for malicious purposes such as dumping process memory from lsass and using this dump for credential harvesting. Tools like Mimikatz can be further used to parse/read the credentials from the procdump files of lsass.exe. 

This process of credential dumping as performed by an attacker consists of two steps.
  1. Performing the procdump of the lsass process
  2. Running tools like Mimikatz to get credentials from the dump
In this analytic we are trying to detect the first step of the above process.

Note - the CAR data model currently does not support process access actions, so there is no pseudocode implementation for this analytic.

## ATT&CK Detection

|Technique |Tactic |Level of Coverage |
|---|---|---|
|[Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


## Implementations

### Common Procdump Lsass Access Pattern (Splunk)


A Splunk search that looks for process access events that target lsass.exe.


```
index=__your_sysmon_data__ EventCode=10 TargetImage="C:\\WINDOWS\\system32\\lsass.exe" GrantedAccess="0x1FFFFF" ("procdump")
```


### Common Procdump Lsass Access Pattern (Eql)


An [EQL Version](https://eqllib.readthedocs.io/en/latest/analytics/1e1ef6be-12fc-11e9-8d76-4d6bb837cda4.html), similar to the above Splunk search, but one that looks for process create events around procdump that contain lsass in the command line.



### Common Procdump Lsass Access Pattern (Sigma)


A [Sigma Version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_lsass_memdump.yml) of the above Splunk search, with some more stringent criteria around calltrace.



