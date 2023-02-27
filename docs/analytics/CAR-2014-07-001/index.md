---
title: "CAR-2014-07-001: Service Search Path Interception"
layout: analytic
submission_date: 2014/07/17
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
According to [ATT&CK](https://attack.mitre.org/), an adversary may [escalate privileges](https://attack.mitre.org/tactics/TA0004) by [intercepting the search path](https://attack.mitre.org/techniques/T1579/009) for legitimately installed services. As a result, Windows will launch the target executable instead of the desired binary and command line. This can be done when there are spaces in the binary path and the path is unquoted. Search path interception should never happen legitimately and will likely be the result of an adversary abusing a system misconfiguration. With a few regular expressions, it is possible to identify the execution of services with intercepted search paths.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|[Path Interception by Unquoted Path](https://attack.mitre.org/techniques/T1574/009/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|High|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode

Look over all service creations that have a quoted path for the first argument. Assuming these still have an absolute path, look for cases in which the command line has a space, but the exe field is not part of the command line. This would indicate that a different process was intended, but the path was intercepted at an earlier space.


```
process = search Process:Create
services = filter processes where (parent_exe == "services.exe")
unquoted_services = filter services where (command_line != "\"*" and command_line == "* *")
intercepted_service = filter unquoted_service where (image_path != "* *" and exe not in command_line)
output intercepted_service
```




