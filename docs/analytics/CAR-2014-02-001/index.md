---
title: "CAR-2014-02-001: Service Binary Modifications"
layout: analytic
submission_date: 2014/02/14
information_domain: Host
subtypes: Registry File Process
analytic_type: Situational Awareness, TTP
contributors: MITRE
---

Adversaries may modify the binary file for an existing service to achieve [Persistence](https://attack.mitre.org/tactics/TA0003) while potentially [evading defenses](https://attack.mitre.org/tactics/TA0005). If a newly created or modified runs as a service, it may indicate APT activity. However, services are frequently installed by legitimate software. A well-tuned baseline is essential to differentiating between benign and malicious service modifications.

### Output Description

The Service Name and approximate time in which changes occurred on each host


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[New Service](https://attack.mitre.org/techniques/T1050/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Modify Existing Service](https://attack.mitre.org/techniques/T1031/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[File System Permissions Weakness](https://attack.mitre.org/techniques/T1044/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Service Execution](https://attack.mitre.org/techniques/T1035/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [file_path](/data_model/file#file_path) |
|[file](/data_model/file) | [create](/data_model/file#create) | [image_path](/data_model/file#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |


### Implementations

#### Pseudocode

Look for events where a file was created and then later run as a service. In these cases, a new service has been created or the binary has been modified. Many programs, such as `msiexec.exe`, do these behaviors legitimately and can be used to help validate legitimate service creations/modifications.


```
legitimate_installers = ["C:\windows\system32\msiexec.exe", "C:\windows\syswow64\msiexec.exe", ...]

file_change = search File:Create,Modify
process = search Process:Create
service_process = filter processes where (parent_exe == "services.exe")
modified_service = join (search, filter) where (
 file_change.time < service_process.time and 
 file_change.file_path == service_process.image_path
)

modified_service = filter modified_service where (modified_service.file_change.image_path not in legitimate_installers)
output modified_service
```




