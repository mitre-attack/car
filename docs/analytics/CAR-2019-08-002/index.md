---
title: "CAR-2019-08-002: Active Directory Dumping via NTDSUtil"
layout: analytic
submission_date: 2019/08/13
information_domain: Host
subtypes: File
analytic_type: TTP
contributors: Tony Lambert/Red Canary
applicable_platforms: Windows
---
<br><br>
The NTDSUtil tool may be used to dump a Microsoft Active Directory database to disk for processing with a credential access tool such as Mimikatz. This is performed by launching `ntdsutil.exe` as a privileged user with command line arguments indicating that media should be created for offline Active Directory installation and specifying a folder path. This process will create a copy of the Active Directory database, `ntds.dit`, to the specified folder path.

This requires filesystem data to determine whether files have been created.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[NTDS](https://attack.mitre.org/techniques/T1003/003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [file_name](/data_model/file#file_name) |
|[file](/data_model/file) | [create](/data_model/file#create) | [image_path](/data_model/file#image_path) |



### Implementations

#### NTDSUtil - File Create (Pseudocode)


This base pseudocode looks for file create events where a file with a name of ntds.dit is created by the ntdsutil process.


```
files = search File:Create
ntds_dump = filter files where (
  file_name = "ntds.dit"  and
  image_path = "*ntdsutil.exe")
output ntds_dump

```


#### NTDSUtil - File Create (Splunk, Sysmon native)


A Splunk/Sysmon version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=11 TargetFilename="*ntds.dit" Image="*ntdsutil.exe"

```


#### NTDSUtil - File Create (Eql, EQL native)


An EQL version of the above pseudocode.


```
file where file_name == "ntds.dit" and process_name == "ntdsutil.exe"

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=11 file="*ntds.dit" source_image="*ntdsutil.exe"

```



### Unit Tests

#### Test Case 1

1. Open a Windows Command Prompt or PowerShell instance as Administrator
2. Execute `ntdsutil.exe “ac i ntds” “ifm” “create full c:\temp” q q`



