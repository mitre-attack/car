---
title: "CAR-2020-11-004: Processes Started From Irregular Parent"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may start legitimate processes and then use their memory space to run malicious code. This analytic looks for common Windows processes that have been abused this way in the past; when the processes are started for this purpose they may not have the standard parent that we would expect. This list is not exhaustive, and it is possible for cyber actors to avoid this discepency. These signatures only work if Sysmon reports the parent process, which may not always be the case if the parent dies before sysmon processes the event.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Process Injection](https://attack.mitre.org/techniques/T1055/)|[Process Hollowing](https://attack.mitre.org/techniques/T1055/012/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode - common processes that do not have the correct parent (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
mismatch_processes = filter processes where ( parent_exe exists AND
  (exe="smss.exe" AND (parent_exe!="smss.exe" AND parent_exe!="System") OR
  (exe="csrss.exe" AND (parent_exe!="smss.exe" AND parent_exe!="svchost.exe")) OR
  (exe="wininit.exe" AND parent_exe!="smss.exe") OR
  (exe="winlogon.exe" AND parent_exe!="smss.exe") OR
  (exe="lsass.exe" AND (parent_exe!="wininit.exe" AND parent_exe!="winlogon.exe")) OR
  (exe="LogonUI.exe" AND (parent_exe!="winlogon.exe" AND parent_exe!="wininit.exe")) OR
  (exe="services.exe" AND parent_exe!="wininit.exe") OR
  (exe="spoolsv.exe" AND parent_exe!="services.exe") OR
  (exe="taskhost.exe" AND (parent_exe!="services.exe" AND parent_exe!="svchost.exe")) OR
  (exe="taskhostw.exe" AND (parent_exe!="services.exe" AND parent_exe!="svchost.exe")) OR
  (exe="userinit.exe" AND (parent_exe!="dwm.exe" AND parent_exe!="winlogon.exe"))
output mismatch_processes

```


#### Splunk Search - parent/child mismatch (Splunk, Sysmon native)


Looks for processes that do not have the expected parent. Common Splunk forwarder applications that break these rules are whitelisted; unique environments may require additional whitelist items.


```
(index=__your_sysmon_index__ EventCode=1) AND ParentImage!="?" AND ParentImage!="C:\\Program Files\\SplunkUniversalForwarder\\bin\\splunk-regmon.exe" AND ParentImage!="C:\\Program Files\\SplunkUniversalForwarder\\bin\\splunk-powershell.exe" AND
((Image="C:\\Windows\System32\\smss.exe" AND (ParentImage!="C:\\Windows\\System32\\smss.exe" AND ParentImage!="System")) OR
(Image="C:\\Windows\\System32\\csrss.exe" AND (ParentImage!="C:\\Windows\\System32\\smss.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\\System32\\wininit.exe" AND ParentImage!="C:\\Windows\\System32\\smss.exe") OR
(Image="C:\\Windows\\System32\\winlogon.exe" AND ParentImage!="C:\\Windows\\System32\\smss.exe") OR
(Image="C:\\Windows\\System32\\lsass.exe" and ParentImage!="C:\\Windows\\System32\\wininit.exe") OR
(Image="C:\\Windows\\System32\\LogonUI.exe" AND (ParentImage!="C:\\Windows\\System32\\winlogon.exe" AND ParentImage!="C:\\Windows\\System32\\wininit.exe")) OR
(Image="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\wininit.exe") OR
(Image="C:\\Windows\\System32\\spoolsv.exe" AND ParentImage!="C:\\Windows\\System32\\services.exe") OR
(Image="C:\\Windows\\System32\\taskhost.exe" AND (ParentImage!="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\\System32\\taskhostw.exe" AND (ParentImage!="C:\\Windows\\System32\\services.exe" AND ParentImage!="C:\\Windows\\System32\\svchost.exe")) OR
(Image="C:\\Windows\System32\\userinit.exe" AND (ParentImage!="C:\\Windows\\System32\\dwm.exe" AND ParentImage!="C:\\Windows\\System32\\winlogon.exe")))

```


#### LogPoint Search - parent/child mismatch (Logpoint, LogPoint native)


Looks for processes that do not have the expected parent. Unique environments may require additional whitelist items.


```
norm_id=WindowsSysmon event_id=1 -parent_image="?" ((image="*\smss.exe" (-parent_image="*\smss.exe" -parent_image="*\System")) OR
(image="*\csrss.exe" (-parent_image="*\smss.exe" -parent_image="*\svchost.exe")) OR (image="*\wininit.exe" -parent_image="*\smss.exe") OR
(image="*\winlogon.exe" -parent_image="*\smss.exe") OR (image="*\lsass.exe"  (-parent_image="*\wininit.exe"  -parent_image="*\winlogon.exe")) OR
(image="*\LogonUI.exe"  (-parent_image="*\winlogon.exe"  -parent_image="*\wininit.exe")) OR (image="*\services.exe"  -parent_image="*\wininit.exe") OR
(image="*\spoolsv.exe"  -parent_image="*\services.exe") OR (image="*\taskhost.exe"  (-parent_image="*\services.exe"  -parent_image="*\svchost.exe")) OR
(image="*\taskhostw.exe"  (-parent_image="*\services.exe"  -parent_image="*\svchost.exe")) OR
(image="*\userinit.exe"  (-parent_image="*\dwm.exe"  -parent_image="*\winlogon.exe")))

```




