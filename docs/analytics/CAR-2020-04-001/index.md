---
title: "CAR-2020-04-001: Shadow Copy Deletion"
layout: analytic
submission_date: 2020/04/10
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: 
applicable_platforms: Windows
---

The Windows [Volume Shadow Copy Service](https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) is a built-in OS feature that can be used to create backup copies of files and volumes.

Adversaries may delete these shadow copies, typically through the usage of system utilities such as vssadmin.exe or wmic.exe, in order prevent file and data recovery. This technique is commonly employed for this purpose by ransomware. 

#### References
This [Red Canary](https://redcanary.com/blog/its-all-fun-and-games-until-ransomware-deletes-the-shadow-copies/) blog post covers both vssadmin.exe and wmic.exe approaches as well as potential others.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Inhibit System Recovery](https://attack.mitre.org/beta/techniques/T1490/)|N/A|[Impact](https://attack.mitre.org/beta/tactics/TA0040/)|Medium|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |


### Implementations

#### Vssadmin.exe delete shadows (Pseudocode)


This pseudocode looks for process event creates around the vssadmin.exe utility with a specific set of command-line parameters for deleting shadow copies.


```
processes = search Process:Create
vssadmin_processes = filter processes where (
  command_line = "*delete shadows*"  and
  image_path = "C:\Windows\System32\vssadmin.exe")
output vssadmin_processes
```


#### WMIC shadowcopy delete (Pseudocode)


This pseudocode looks for process event creates around wmic.exe with a specific set of command-line parameters for deleting shadow copies.


```
processes = search Process:Create
wmic_processes = filter processes where (
  command_line = "*shadowcopy delete*"  and
  image_path = "C:\Windows\*\wmic.exe")
output wmic_processes
```


#### Vssadmin.exe delete shadows (Splunk, Sysmon native)


Splunk version of the CAR pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\System32\\vssadmin.exe" CommandLine="*delete shadows*"
```


#### WMIC shadowcopy delete (Splunk, Sysmon native)


Splunk version of the CAR pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\wmic.exe" CommandLine="*shadowcopy delete*"
```


#### Vssadmin.exe delete shadows (Eql, EQL native)


An [EQL](https://eqllib.readthedocs.io/en/latest/analytics/d3a327b6-c517-43f2-8e97-1f06b7370705.html) version of the CAR pseudocode.



#### WMIC shadowcopy delete (Eql, EQL native)


An [EQL](https://eqllib.readthedocs.io/en/latest/analytics/7163f069-a756-4edc-a9f2-28546dcb04b0.html) version of the CAR pseudocode.



#### Vssadmin.exe delete shadows & WMIC shadowcopy delete (Sigma, Sigma native)


A [Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_shadow_copies_deletion.yml) version of the CAR pseudocode for both vssadmin.exe and wmic.exe approaches.





