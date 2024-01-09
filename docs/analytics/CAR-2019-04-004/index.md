---
title: "CAR-2019-04-004: Credential Dumping via Mimikatz"
layout: analytic
submission_date: 2019/04/29
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Credential dumpers like Mimikatz can be loaded into memory and from there read data from another processes. This analytic looks for instances where processes are requesting specific permissions to read parts of the LSASS process in order to detect when credential dumping is occurring. One weakness is that all current implementations are “overtuned” to look for common access patterns used by Mimikatz.

*This requires information about process access, e.g. Sysmon Event ID 10. That currently doesn’t have a CAR data model mapping, since we currently lack any open/access actions for Processes. If this changes, we will update the data model requirements.*


#### References
Credit to [Cyb3rWard0g](https://github.com/Cyb3rWard0g/ThreatHunter-Playbook/blob/master/playbooks/windows/06_credential_access/credential_dumping_T1003/credentials_from_memory/mimikatz_logonpasswords.md), dim0x69 (blog.3or.de), and Mark Russinovich for providing much of the information used to construct these analytics.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 





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


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=10 image="C:\Windows\system32\lsass.exe" (access="0x1410" OR access="0x1010" OR access="0x1438" OR access="0x143a" OR access="0x1418") call_trace="C:\windows\SYSTEM32\ntdll.dll+*|C:\windows\System32\KERNELBASE.dll+20edd|UNKNOWN(*)"
| fields log_ts, host, user, source_image, access

```




