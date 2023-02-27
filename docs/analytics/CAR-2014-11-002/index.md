---
title: "CAR-2014-11-002: Outlier Parents of Cmd"
layout: analytic
submission_date: 2014/11/06
information_domain: Host
subtypes: Process
analytic_type: Anomaly, TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Many programs create command prompts as part of their normal operation including malware used by attackers. This analytic attempts to identify suspicious programs spawning `cmd.exe` by looking for programs that do not normally create `cmd.exe`.

While this analytic does not take the user into account, doing so could generate further interesting results.
It is very common for some programs to spawn cmd.exe as a subprocess, for example to run batch files or windows commands. However many process don’t routinely launch a command prompt – for example Microsoft Outlook. A command prompt being launched from a process that normally doesn’t launch command prompts could be the result of malicious code being injected into that process, or of an attacker replacing a legitimate program with a malicious one.


### Output Description

The time and host the new process was started as well as its parent



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[Windows Command Shell](https://attack.mitre.org/techniques/T1059/003/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode

Create a baseline of parents of `cmd.exe` seen over the last 30 days and a list of parents of `cmd.exe` seen today. Remove parents in the baseline from parents seen today, leaving a list of new parents.


```
processes = search Process:Create
cmd = filter processes where (exe == "cmd.exe")
cmd = from cmd select parent_exe
historic_cmd = filter cmd (where timestamp < now - 1 day AND timestamp > now - 1 day)
current_cmd = filter cmd (where timestamp >= now - 1 day)
new_cmd = historic_cmd - current_cmd
output new_cmd

```




