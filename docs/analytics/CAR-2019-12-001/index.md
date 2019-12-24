---
title: "CAR-2019-12-001: PowerShell PSAttack"
layout: analytic
submission_date: 2019/12/24
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Kaushal Parikh/Cyware Labs
---

[PSAttack](https://github.com/jaredhaight/PSAttack) is an open source, portable PowerShell console that combines the best projects from the security community into a self contained custom utility. The fun part is that this offensive PowerShell console does not rely on powershell.exe! Instead, it calls PowerShell directly through the .NET framework, which makes it harder for enterprises to block it’s execution. Secondly, the modules that are encompassed with the console are encrypted, which never touch the disk, making it for anti-virus evasion. They are decrypted in the system memory on the fly.

The ATT&CK Execution method is generally attempted by an attacker in 2 steps for this type of attack.
  1. First executing the [PSAttack](https://github.com/jaredhaight/PSAttack/) and
  2. Second invoking submodules like Mimikatz from the above script to escalate the user privileges and harvesting information.
In this CAR we are trying to detect the first step of the process mentioned above.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[PowerShell](https://attack.mitre.org/techniques/T1086)|[Execution](https://attack.mitre.org/tactics/TA0002/)|High|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Implementations

#### Common PSAttack Patterns (Splunk, Sysmon native)

```
index=__your_microsoft_windows_powershell_index__ EventCode=4103 ("PS ATTACK!!!")
```

```
index=__your_microsoft_windows_powershell_index__ EventCode=4103 ("PS ATTACK!!!") "Host Application = *\PSAttack.exe"
```


#### Procdump - Process Access (Sigma)


A [Sigma Version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/powershell/powershell_psattack.yml) of the above Splunk search.




### Unit Tests

#### Test Case 1

1. Open a Windows Command Prompt or PowerShell instance.
2. Navigate to folder containing PSAttack.
3. Execute PSAttack.exe
