---
title: "CAR-2021-04-001: Common Windows Process Masquerading"
layout: analytic
submission_date: 2021/02/12
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Sebastien Damaye
applicable_platforms: Windows
---
<br><br>
[Masquerading (T1036)](https://attack.mitre.org/techniques/T1036/) is defined by ATT&CK as follows:

"Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names."

Malware authors often use this technique to hide malicious executables behind legitimate Windows executable names (e.g. `lsass.exe`, `svchost.exe`, etc).

There are several sub-techniques, but this analytic focuses on [Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005/) only.

**Analytic Methodology**

With process monitoring, hunt for processes matching these criteria:

* process name is `svchost.exe`, `smss.exe`, `wininit.exe`, `taskhost.exe`, etc.
* process path is not `C:\Windows\System32\` or `C:\Windows\SysWow64\`

Examples (true positive):

`C:\Users\administrator\svchost.exe`

To make sure the rule doesn't miss cases where the executable would be started from a sub-folder of these locations, the entire path is checked for the process path. The below example should be considered as suspicious:

`C:\Windows\System32\srv\svchost.exe`



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Masquerading](https://attack.mitre.org/techniques/T1036/)|[Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [access](/data_model/process#access) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [access](/data_model/process#access) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [terminate](/data_model/process#terminate) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [terminate](/data_model/process#terminate) | [image_path](/data_model/process#image_path) |



### Implementations

#### Pseudocode - Common Windows Process Masquerading (Pseudocode, CAR native)


Looks for mismatches between process names and their image paths.


```
processes = search Process:*
suspicious_processes = filter processes where (
  (exe=svchost.exe AND (image_path!="C:\\Windows\\System32\\svchost.exe" OR process_path!="C:\\Windows\\SysWow64\\svchost.exe"))
  OR (exe=smss.exe AND image_path!="C:\\Windows\\System32\\smss.exe")
  OR (exe=wininit.exe AND image_path!="C:\\Windows\\System32\\wininit.exe")
  OR (exe=taskhost.exe AND image_path!="C:\\Windows\\System32\\taskhost.exe")
  OR (exe=lasass.exe AND image_path!="C:\\Windows\\System32\\lsass.exe")
  OR (exe=winlogon.exe AND image_path!="C:\\Windows\\System32\\winlogon.exe")
  OR (exe=csrss.exe AND image_path!="C:\\Windows\\System32\\csrss.exe")
  OR (exe=services.exe AND image_path!="C:\\Windows\\System32\\services.exe")
  OR (exe=lsm.exe AND image_path!="C:\\Windows\\System32\\lsm.exe")
  OR (exe=explorer.exe AND image_path!="C:\\Windows\\explorer.exe")
  )
output suspicious_processes

```


#### Splunk Search - Common Windows Process Masquerading (Splunk, Sysmon native)


Splunk search version of the above pseudocode.


```
index=__your_sysmon_index__ source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" AND (
(process_name=svchost.exe AND NOT (process_path="C:\\Windows\\System32\\svchost.exe" OR process_path="C:\\Windows\\SysWow64\\svchost.exe"))
OR (process_name=smss.exe AND NOT process_path="C:\\Windows\\System32\\smss.exe")
OR (process_name=wininit.exe AND NOT process_path="C:\\Windows\\System32\\wininit.exe")
OR (process_name=taskhost.exe AND NOT process_path="C:\\Windows\\System32\\taskhost.exe")
OR (process_name=lasass.exe AND NOT process_path="C:\\Windows\\System32\\lsass.exe")
OR (process_name=winlogon.exe AND NOT process_path="C:\\Windows\\System32\\winlogon.exe")
OR (process_name=csrss.exe AND NOT process_path="C:\\Windows\\System32\\csrss.exe")
OR (process_name=services.exe AND NOT process_path="C:\\Windows\\System32\\services.exe")
OR (process_name=lsm.exe AND NOT process_path="C:\\Windows\\System32\\lsm.exe")
OR (process_name=explorer.exe AND NOT process_path="C:\\Windows\\explorer.exe")
)

```




