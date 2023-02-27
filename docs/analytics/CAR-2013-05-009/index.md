---
title: "CAR-2013-05-009: Running executables with same hash and different names"
layout: analytic
submission_date: 2013/05/23
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
Executables are generally not renamed, thus a given hash of an executable should only have ever one name. Identifying instances where multiple process names share the same hash may find cases where tools are copied by attackers to different folders or hosts to [avoid detection](https://attack.mitre.org/tactics/TA0005).

Although this analytic was initially based on MD5 hashes, it is equally applicable to any hashing convention.

### Output Description

A list of hashes and the different executables associated with each one


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Masquerading](https://attack.mitre.org/techniques/T1036/)|[Rename System Utilities](https://attack.mitre.org/techniques/T1036/003/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SBV | [Service Binary Verification](https://d3fend.mitre.org/technique/d3f:ServiceBinaryVerification)|  
|D3-SFA | [System File Analysis](https://d3fend.mitre.org/technique/d3f:SystemFileAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [md5_hash](/data_model/process#md5_hash) |



### Implementations

#### Basic Query (Splunk, Sysmon native)


This is a basic Splunk search that will output all of the sysmon-reported process images and their respective hashes, for cases where an image has more than one set of hashes. Thus, this will output a large amount of data and should be filtered by the analyst in order to make the results more useful.


```
index=__your_sysmon_index__ EventCode=1|stats dc(Hashes) as Num_Hashes values(Hashes) as "Hashes" by Image|where Num_Hashes > 1
```


#### Sigma/Sysmon (Sigma)


[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_renamed_binary.yml) a Sysmon-specific rule for detecting this, using the OriginalFilename field.



#### Sigma (renamed powershell) (Sigma)


[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_powershell_renamed_ps.yml) a rule specifically for detecting instances of Powershell being renamed.



#### Sigma (renamed paexec) (Sigma)


[Sigma includes](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_renamed_paexec.yml) a rule specifically for detecting instances of paexec being renamed.



#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 group count_unique $App, $HashMD5 limit 100
>>_agg count_unique $HashMD5
>>_checkif int_compare count_unique > 1 include
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1
| chart distinct_count(hash) as cnt by image
| search cnt > 1
```




