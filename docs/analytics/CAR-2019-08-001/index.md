---
title: "CAR-2019-08-001: Credential Dumping via Windows Task Manager"
layout: analytic
submission_date: 2019/08/05
information_domain: Host
subtypes: File
analytic_type: TTP
contributors: Tony Lambert/Red Canary
applicable_platforms: Windows
---
<br><br>
The Windows Task Manager may be used to dump the memory space of `lsass.exe` to disk for processing with a credential access tool such as Mimikatz. This is performed by launching Task Manager as a privileged user, selecting `lsass.exe`, and clicking "Create dump file". This saves a dump file to disk with a deterministic name that includes the name of the process being dumped.

This requires filesystem data to determine whether files have been created.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-FCA | [File Creation Analysis](https://d3fend.mitre.org/technique/d3f:FileCreationAnalysis)| 



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


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=11 file="*lsass*.dmp" source_image="C:\Windows\*\taskmgr.exe"

```



### Unit Tests

#### Test Case 1

1. Open Windows Task Manager as Administrator
2. Select lsass.exe
3. Right-click on lsass.exe and select "Create dump file".




### True Positives

#### Mordor (sysmon)

Sysmon event from the Mordor [Interactive Task Manager lsass dump dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/credential_access/credential_dumping_T1003/interactive_taskmngr_lsass_dump.md).


##### [Full Event](/true_positives/CAR-2019-08-001-mordor-01.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-10-27T05:45:39.851Z",
	"@file_date_creation": "2019-10-27T05:45:39.851Z",
	"@timestamp": "2019-10-27T05:45:39.858Z",
	"@version": "1",
	"action": "filecreate",
	"event_id": 11,
	"file_name": "c:\\\\users\\\\pgustavo\\\\appdata\\\\local\\\\temp\\\\lsass.dmp",
	"host_name": "it001.shire.com",
	"level": "information",
	"log_ingest_timestamp": "2019-10-27T05:45:39.858Z",
	"log_name": "Microsoft-Windows-Sysmon/Operational",
	"meta_user_reporter_name_is_machine": "false",
	"opcode": "Info",
	"process_guid": "a158f72c-2ef4-5db5-0000-00100fb48f00",
	"process_id": "2408",
	"process_name": "taskmgr.exe",
	"process_path": "c:\\\\windows\\\\system32\\\\taskmgr.exe",
	"provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
	"record_number": 258042,
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "File created (rule: FileCreate)",
	"thread_id": 3760,
	"type": "wineventlog",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User",
	"version": 2
}
```

