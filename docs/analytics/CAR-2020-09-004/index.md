---
title: "CAR-2020-09-004: Credentials in Files & Registry"
layout: analytic
submission_date: 2020/09/10
information_domain: Host
subtypes: Process, Registry
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may search the Windows Registry on compromised systems for insecurely stored credentials for credential access. This can be accomplished using the query functionality of the reg.exe system utility, by looking for keys and values that contain strings such as "password". In addition, adversaries may use toolkits such as [PowerSploit](https://powersploit.readthedocs.io/en/latest/) in order to dump credentials from various applications such as IIS.Accordingly, this analytic looks for invocations of reg.exe in this capacity as well as that of several powersploit modules with similar functionality.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Unsecured Credentials](https://attack.mitre.org/techniques/T1552/)|[Credentials In Files](https://attack.mitre.org/techniques/T1552/001/), [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Pseudocode - reg.exe password search & powersploit modules (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
  cred_processes = filter processes where (
  command_line = "*reg* query HKLM /f password /t REG_SZ /s*" OR
  command_line = "reg* query HKCU /f password /t REG_SZ /s" OR
  command_line = "*Get-UnattendedInstallFile*" OR
  command_line = "*Get-Webconfig*" OR
  command_line = "*Get-ApplicationHost*" OR
  command_line = "*Get-SiteListPassword*" OR
  command_line = "*Get-CachedGPPPassword*" OR
  command_line = "*Get-RegistryAutoLogon*")
output cred_processes

```


#### Splunk Search - reg.exe password search & powersploit modules (Splunk, Sysmon native)


This Splunk search looks for command lines of reg.exe used to search for passwords, as well as those of powersploit modules for the same purpose.


```
((index=__your_sysmon_index__ EventCode=1) OR (index=__your_win_syslog_index__ EventCode=4688)) (CommandLine="*reg* query HKLM /f password /t REG_SZ /s*" OR CommandLine="reg* query HKCU /f password /t REG_SZ /s" OR CommandLine="*Get-UnattendedInstallFile*" OR CommandLine="*Get-Webconfig*" OR CommandLine="*Get-ApplicationHost*" OR CommandLine="*Get-SiteListPassword*" OR CommandLine="*Get-CachedGPPPassword*" OR CommandLine="*Get-RegistryAutoLogon*")

```


#### LogPoint search - reg.exe password search & powersploit modules (Logpoint, LogPoint native)


This LogPoint search looks for command lines of reg.exe used to search for passwords, as well as those of powersploit modules for the same purpose.


```
norm_id=WindowsSysmon event_id=1 command IN ["*reg* query HKLM /f password /t REG_SZ /s*", "reg* query HKCU /f password /t REG_SZ /s", "*Get-UnattendedInstallFile*", "*Get-Webconfig*", "*Get-ApplicationHost*", "*Get-SiteListPassword*", "*Get-CachedGPPPassword*", "*Get-RegistryAutoLogon*"]

```




