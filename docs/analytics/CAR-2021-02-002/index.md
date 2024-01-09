---
title: "CAR-2021-02-002: Get System Elevation"
layout: analytic
submission_date: 2021/01/15
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Sebastien Damaye
applicable_platforms: Windows
---
<br><br>
Cyber actors frequently escalate to the SYSTEM account after gaining entry to a Windows host, to enable them to carry out various attacks more effectively. Tools such as Meterpreter, Cobalt Strike, and Empire carry out automated steps to "Get System", which is the same as switching over to the System user account. Most of these tools utilize multiple techniques to try and attain SYSTEM: in the first technique, they create a named pipe and connects an instance of cmd.exe to it, which allows them to impersonate the security context of cmd.exe, which is SYSTEM. In the second technique, a malicious DLL is injected into a process that is running as SYSTEM; the injected DLL steals the SYSTEM token and applies it where necessary to escalate privileges. This analytic looks for both of these techniques.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)|N/A|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[service](/data_model/service) | [create](/data_model/service#create) | [command_line](/data_model/service#command_line) |



### Implementations

#### Pseudocode - Meterpreter and Cobalt Strike (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process
suspicious_processes = filter processes where (
  (parent_image_path == C:\Windows\System32\services.exe" AND
   image_path == "C:\Windows\System32\cmd.exe" AND
   command_line == "*echo*" AND
   command_line == "*\pipe\*") OR
  (image_path == "C:\Windows\System32\rundll32.exe" AND
   command_line == "*,a /p:*"))
output suspicious_processes

```


#### Splunk Search - Meterpreter and Cobalt Strike (Splunk, Sysmon native)


Look for instances GetSystem elevation performed by Meterpreter or Cobalt Strike


```
index=__your_sysmon_index__ (ParentImage="C:\\Windows\\System32\\services.exe" Image="C:\\Windows\\System32\\cmd.exe" (CommandLine="*echo*" AND CommandLine="*\\pipe\\*"))
OR (Image="C:\\Windows\\System32\\rundll32.exe" CommandLine="*,a /p:*")

```


#### Pseudocode - Empire and PoshC2 (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process
suspicious_processes = filter processes where (
  (image_path == "C:\Windows\System32\cmd.exe" OR
   command_line == "*%COMSPEC%*") AND
   command_line == "*echo*" AND
   command_line == "*\pipe\*"))
output suspicious_processes

```


#### Splunk Search - Empire and PoshC2 (Splunk, Sysmon native)


Look for instances GetSystem elevation performed by Empire or PoshC2


```
index=__your_sysmon_index__ (Image="C:\\Windows\\System32\\cmd.exe" OR CommandLine="*%COMSPEC%*") (CommandLine="*echo*" AND CommandLine="*\pipe\*")

```



### Unit Tests

#### Test Case 1

GetSystem in Meterpreter & Cobalt Strike’s Beacon

```
cmd.exe /c echo ba80ae80df9 > \\.\pipe\66bee3
cmd.exe /c echo fvxens > \\.\pipe\fvxens
rundll32.exe C:\Users\user\AppData\Local\Temp\fvxens.dll,a /p:fvxens
```

#### Test Case 2

GetSystem in Empire & PoshC2

```
cmd.exe /C start %COMSPEC% /C `"timeout /t 3 >nul&&echo TestSVC > \\.\pipe\TestSVC
```


