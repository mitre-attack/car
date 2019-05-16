---
title: "CAR-2014-04-003: Powershell Execution"
layout: analytic
submission_date: 2014/04/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

[PowerShell](https://attack.mitre.org/techniques/T1086/) is a scripting environment included with Windows that is used by both attackers and administrators. Execution of PowerShell scripts in most Windows versions is opaque and not typically secured by antivirus which makes using PowerShell an easy way to circumvent security measures. This analytic detects execution of PowerShell scripts.

Powershell can be used to hide monitored command line execution such as:
-   `net use`
-   `sc start`

## ATT&CK Detection

|Technique |Tactic |Level of Coverage |
|---|---|---|
|[PowerShell](https://attack.mitre.org/techniques/T1086/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|High|
|[Scripting](https://attack.mitre.org/techniques/T1064/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|

## Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |


## Implementations

### Pseudocode

Look for versions of `PowerShell` that were not launched interactively.

```
process = search Process:Create
powershell = filter process where (exe == "powershell.exe" AND parent_exe != "explorer.exe" )
output powershell
```

