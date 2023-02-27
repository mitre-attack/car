---
title: "CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS"
layout: analytic
submission_date: 2020/08/03
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
NTFS Alternate Data Streams (ADSs) may be used by adversaries as a means of evading security tools by storing malicious data or binaries in file attribute metadata. ADSs are also powerful because their contents can be directly executed by various Windows tools; accordingly, this analytic looks at common ways of executing ADSs using Living off the Land Binaries and Scripts (LOLBAS).

#### References
The [LOLBAS project](https://lolbas-project.github.io/) is an amazing resource and was used as the basis for many of these analytics.
Oddvar Moe has created an excellent NTFS ADS execution reference [here on github](https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f).


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Hide Artifacts](https://attack.mitre.org/techniques/T1564/)|[NTFS File Attributes](https://attack.mitre.org/techniques/T1564/004/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### NTFS ADS - pseudocode (Pseudocode, CAR native)


This is generic pseudocode that lines up with the below Splunk queries.


```
processes = search Process:Create
ads_processes = filter processes where (
exe == "control.exe OR appvlp.exe OR cmd.exe OR ftp.exe OR bash.exe OR mavinject.exe OR bitsadmin.exe" and command_line.matches("__some_regex__")
)
output ads_processes
```


#### NTFS ADS - control (Splunk, Sysmon native)


This Splunk query looks for invocations of control.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\System32\\control.exe OR Image=C:\\Windows\SysWOW64\\control.exe) | regex CommandLine="(\w+(\.\w+)?):(\w+\.dll)"
```


#### NTFS ADS - appvlp (Splunk, Sysmon native)


This Splunk query looks for invocations of appvlp.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image="C:\\Program Files\\Microsoft Office\\root\\Client\\AppVLP.exe" OR Image="C:\\Program Files (x86)\\Microsoft Office\\root\\Client\\AppVLP.exe") | regex CommandLine="(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - cmd (Splunk, Sysmon native)


This Splunk query looks for invocations of cmd.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\cmd.exe OR Image=C:\\Windows\\SysWOW64\\cmd.exe) | regex CommandLine="-\s+<.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - ftp (Splunk, Sysmon native)


This Splunk query looks for invocations of ftp.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\ftp.exe OR Image=C:\\Windows\\SysWOW64\\ftp.exe) | regex CommandLine="-s:(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - bash (Splunk, Sysmon native)


This Splunk query looks for invocations of bash.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\bash.exe OR C:\\Windows\\SysWOW64\\bash.exe) | regex CommandLine="-c.*(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - mavinject (Splunk, Sysmon native)


This Splunk query looks for invocations of mavinject.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\mavinject.exe OR C:\\Windows\\SysWOW64\\mavinject.exe) | regex CommandLine="\d+\s+\/INJECTRUNNING.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - bitsadmin (Splunk, Sysmon native)


This Splunk query looks for invocations of bitsadmin.exe used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\System32\\bitsadmin.exe OR C:\\Windows\\SysWOW64\\bitsadmin.exe) | regex CommandLine="\/create.*\/addfile.*\/SetNotifyCmdLine.*\b(\w+\.\w+):(\w+(\.\w+)?)"
```




