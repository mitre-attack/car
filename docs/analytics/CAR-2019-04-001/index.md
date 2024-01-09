---
title: "CAR-2019-04-001: UAC Bypass"
layout: analytic
submission_date: 2019/04/19
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Bypassing user account control (UAC Bypass) is generally done by piggybacking on a system process that has auto-escalate privileges. This analytic looks to detect those cases as described by the open-source [UACME](https://github.com/hfiref0x/UACME) tool.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)|[Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_image_path](/data_model/process#parent_image_path) |
|[process](/data_model/process) | [create](/data_model/process#create) | [integrity_level](/data_model/process#integrity_level) |
|[process](/data_model/process) | [create](/data_model/process#create) | [user](/data_model/process#user) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_command_line](/data_model/process#parent_command_line) |



### Implementations

#### Splunk, Sysmon native

This Splunk query looks for specific invocations of UACME, representing different ways to bypass user account control.


```
index=_your_sysmon_index_ EventCode=1 IntegrityLevel=High|search (ParentCommandLine="\"c:\\windows\\system32\\dism.exe\"*""*.xml" AND Image!="c:\\users\\*\\appdata\\local\\temp\\*\\dismhost.exe") OR ParentImage=c:\\windows\\system32\\fodhelper.exe OR (CommandLine="\"c:\\windows\\system32\\wusa.exe\"*/quiet*" AND User!=NOT_TRANSLATED AND CurrentDirectory=c:\\windows\\system32\\ AND ParentImage!=c:\\windows\\explorer.exe) OR CommandLine="*.exe\"*cleanmgr.exe /autoclean*" OR (ParentImage="c:\\windows\\*dccw.exe" AND Image!="c:\\windows\\system32\\cttune.exe") OR Image="c:\\program files\\windows media player\\osk.exe" OR ParentImage="c:\\windows\\system32\\slui.exe"|eval PossibleTechniques=case(like(lower(ParentCommandLine),"%c:\\windows\\system32\\dism.exe%"), "UACME #23", like(lower(Image),"c:\\program files\\windows media player\\osk.exe"), "UACME #32", like(lower(ParentImage),"c:\\windows\\system32\\fodhelper.exe"),  "UACME #33", like(lower(CommandLine),"%.exe\"%cleanmgr.exe /autoclean%"), "UACME #34", like(lower(Image),"c:\\windows\\system32\\wusa.exe"), "UACME #36", like(lower(ParentImage),"c:\\windows\\%dccw.exe"), "UACME #37", like(lower(ParentImage),"c:\\windows\\system32\\slui.exe"), "UACME #45")

```


#### Pseudocode, CAR

This is a pseudocode version of the above Splunk query.


```
processes = search Process:Create
possible_uac_bypass = filter processes where (
  integrity_level == "High" and
  (parent_image_path == "c:\windows\system32\fodhelper.exe") or
  (command_line == "*.exe\"*cleanmgr.exe /autoclean*") or
  (image_path == "c:\program files\windows media player\osk.exe") or
  (parent_image_path == "c:\windows\system32\slui.exe") or
  (parent_command_line == '"c:\windows\system32\dism.exe"*""*.xml"' and image_path != "c:\users\*\appdata\local\temp\*\dismhost.exe") or
  (command_line == '"c:\windows\system32\wusa.exe"*/quiet*' and user != "NOT_TRANSLATED" and current_working_directory == "c:\windows\system32\" and parent_image_path != "c:\windows\explorer.exe") or
  (parent_image_path == "c:\windows\*dccw.exe" and image_path != "c:\windows\system32\cttune.exe")
)
output possible_uac_bypass

```


#### Sigma/Sysmon (Eventvwr) (Sigma)


[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_uac_bypass_eventvwr.yml) rule for detecting eventvwr-based UAC bypass.



#### Sigma/Sysmon (sdclt) (Sigma)


[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_uac_bypass_sdclt.yml) rule for detecting sdclt-based UAC bypass.



#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 integrity_level="High" ((parent_image="c:\windows\system32\fodhelper.exe" OR command='*.exe"*cleanmgr.exe /autoclean*' OR image="c:\program files\windows media player\osk.exe" OR parent_image="c:\windows\system32\slui.exe") OR (parent_command='"c:\windows\system32\dism.exe"*""*.xml"' -image="c:\users\*\appdata\local\temp\*\dismhost.exe") OR (parent_image="c:\windows\*dccw.exe" -image="c:\windows\system32\cttune.exe") OR (command='"c:\windows\system32\wusa.exe"*/quiet*' -user="NOT_TRANSLATED" path="c:\windows\system32\" -parent_image="c:\windows\explorer.exe"))

```




