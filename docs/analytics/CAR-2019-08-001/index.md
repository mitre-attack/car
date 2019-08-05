---
title: "CAR-2019-08-001: Credential Dumping via Windows Task Manager"
layout: analytic
submission_date: 2019/08/05
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Tony Lambert/Red Canary
---

The Windows Task Manager may be used to dump the memory space of `lsass.exe` to disk for processing with a credential access tool such as Mimikatz. This is performed by launching Task Manager as a privileged user, selecting `lsass.exe`, and clicking "Create dump file". This saves a dump file to disk with the process's name in the file name.

This requires filesystem data to determine whether files have been created.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [file_name](/data_model/file#file_name) |
|[file](/data_model/file) | [create](/data_model/file#create) | [image_path](/data_model/file#image_path) |


### Implementations

#### Procdump - File Create (Pseudocode)


This base pseudocode looks for file create events where a file with a name similar to lsass.dmp is created by the Windows task manager process.


```
files = search File:Create
lsass_dump = filter files where (
  file_name = "lsass*.dmp"  and
  image_path = "C:\Windows\*\taskmgr.exe")
output lsass_dump
```


#### Procdump - File Create (Splunk, Sysmon native)


A Splunk/Sysmon version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=11 TargetFilename="*lsass*.dmp" Image="C:\\Windows\\*\\taskmgr.exe"
```


#### Procdump - File Create (Eql, EQL native)


An EQL version of the above pseudocode.


```
file where file_name == "lsass*.dmp" and process_name == "taskmgr.exe"
```



### Unit Tests

#### Test Case 1

1. Open Windows Task Manager as Administrator
2. Select lsass.exe
3. Right-click on lsass.exe and select "Create dump file".
