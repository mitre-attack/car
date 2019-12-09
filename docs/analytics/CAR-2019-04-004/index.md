---
title: "CAR-2019-04-004: Credential Dumping via Mimikatz"
layout: analytic
submission_date: 2019/04/29
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

Credential dumpers like Mimikatz can be loaded into memory and from there read data from another processes. This analytic looks for instances where processes are requesting specific permissions to read parts of the LSASS process in order to detect when credential dumping is occurring. One weakness is that all current implementations are “overtuned” to look for common access patterns used by Mimikatz.

*This requires information about process access, e.g. Sysmon Event ID 10. That currently doesn’t have a CAR data model mapping, since we currently lack any open/access actions for Processes. If this changes, we will update the data model requirements.*

#### References
Credit to [Cyb3rWard0g](https://github.com/Cyb3rWard0g/ThreatHunter-Playbook/blob/master/playbooks/windows/06_credential_access/credential_dumping_T1003/credentials_from_memory/mimikatz_logonpasswords.md), dim0x69 (blog.3or.de), and Mark Russinovich for providing much of the information used to construct these analytics.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### Implementations

#### Common Mimikatz GrantedAccess Patterns (Splunk, Sysmon native)


This is specific to the way Mimikatz works currently, and thus is fragile to both future updates and non-default configurations of Mimikatz.


```
index=__your_sysmon_data__ EventCode=10 
TargetImage="C:\\WINDOWS\\system32\\lsass.exe"
(GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418)
CallTrace="C:\\windows\\SYSTEM32\\ntdll.dll+*|C:\\windows\\System32\\KERNELBASE.dll+20edd|UNKNOWN(*)" 
| table _time hostname user SourceImage GrantedAccess
```


#### Outliers (Splunk, Sysmon native)


This is an outlier version of the above without including the specific call trace. This should work in more (but not all) situations however runs more slowly and will have more false positives - typically installers.


```
earliest=-d@d latest=now() index=__your_sysmon_data__
  EventCode=10
  TargetImage="C:\\WINDOWS\\system32\\lsass.exe"
  (GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418) 
| search NOT [ search earliest=-7d@d latest=-2d@d index=__your_sysmon_data__ EventCode=10 TargetImage="C:\\WINDOWS\\system32\\lsass.exe" (GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418) 
  | dedup SourceImage 
  | fields SourceImage ]
| table  _time hostname user SourceImage GrantedAccess
```





### True Positives

#### Mordor (sysmon)

Sysmon event from the Mordor [Interactive Task Manager lsass dump dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/credential_access/credential_dumping_T1003/interactive_taskmngr_lsass_dump.md). Note: the dumping is actually done by `taskmgr` in this case, though the data is still relevant.


##### [Full Event](/true_positives/CAR-2019-04-004-mordor-01.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-10-27T05:45:25.226Z",
	"@timestamp": "2019-10-27T05:45:25.245Z",
	"@version": "1",
	"action": "processaccess",
	"event_id": 10,
	"opcode": "Info",
	"process_call_trace": "C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9c524|C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2730e|C:\\\\Windows\\\\system32\\\\taskmgr.exe+2e47e|C:\\\\Windows\\\\system32\\\\taskmgr.exe+7abcc|C:\\\\Windows\\\\system32\\\\taskmgr.exe+7b2e9|C:\\\\Windows\\\\system32\\\\taskmgr.exe+78653|C:\\\\Windows\\\\system32\\\\taskmgr.exe+7768e|C:\\\\Windows\\\\system32\\\\taskmgr.exe+38da8|C:\\\\Windows\\\\system32\\\\taskmgr.exe+3a14d|C:\\\\Windows\\\\System32\\\\KERNEL32.DLL+17944|C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+6ce71",
	"process_granted_access": 5136,
	"process_guid": "a158f72c-2ef4-5db5-0000-00100fb48f00",
	"process_id": "2408",
	"process_name": "taskmgr.exe",
	"process_path": "c:\\\\windows\\\\system32\\\\taskmgr.exe",
	"process_target_guid": "a158f72c-0aba-5db5-0000-00105d6c0000",
	"process_target_id": "808",
	"process_target_name": "lsass.exe",
	"process_target_path": "c:\\\\windows\\\\system32\\\\lsass.exe",
	"provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
	"record_number": 256899,
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "Process accessed (rule: ProcessAccess)",
	"thread_id": "9380",
	"type": "wineventlog",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User"
}
```

