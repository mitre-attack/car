---
title: "CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities"
layout: analytic
submission_date: 2020/08/03
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---

NTFS Alternate Data Streams (ADSs) may be used by adversaries as a means of evading security tools by storing malicious data or binaries in file attribute metadata. ADSs are also powerful because they can be directly executed by various Windows tools; accordingly, this analytic looks at common ways of executing ADSs using system utilities such as powershell.

#### References
Oddvar Moe has created an excellent NTFS ADS execution reference [here on github](https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f), which was used as the basis for many of these analytics.
The [LOLBAS project](https://lolbas-project.github.io/) is an amazing resource for anything LOLBAS.


### ATT&CK Detection

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Hide Artifacts](https://attack.mitre.org/techniques/T1564/)|[NTFS File Attributes](https://attack.mitre.org/techniques/T1564/004/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|

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
exe == "powershell.exe OR rundll32.exe OR wmic.exe OR wscript.exe OR cscript.exe" and command_line.matches("__some_regex__")
)
output ads_processes
```


#### NTFS ADS - powershell (Splunk, Sysmon native)


This Splunk query looks for invocations of powershell used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 Image=C:\\Windows\\*\\powershell.exe|regex CommandLine="Invoke-CimMethod\s+-ClassName\s+Win32_Process\s+-MethodName\s+Create.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)|-ep bypass\s+-\s+<.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)|-command.*Get-Content.*-Stream.*Set-Content.*start-process .*(\w+(\.\w+)?)"
```


#### NTFS ADS - wmic (Splunk, Sysmon native)


This Splunk query looks for invocations of WMIC used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 Image=C:\\Windows\\*\\wmic.exe | regex CommandLine="process call create.*\"(\w+(\.\w+)?):(\w+(\.\w+)?)"
```


#### NTFS ADS - rundll32 (Splunk, Sysmon native)


This Splunk query looks for invocations of rundll32 used to execute NTFS alternate data streams.


```
index=__sysmon_index__  EventCode=1 Image=C:\\Windows\\*\\rundll32.exe | regex CommandLine="\"?(\w+(\.\w+)?):(\w+(\.\w+)?)?\"?,\w+\|(advpack\.dll\|ieadvpack\.dll),RegisterOCX\s+(\w+\.\w+):(\w+(\.\w+)?)\|(shdocvw\.dll\|ieframe\.dll),OpenURL.*(\w+\.\w+):(\w+(\.\w+)?)"
```


#### NTFS ADS - wscript/cscript (Splunk, Sysmon native)


This Splunk query looks for invocations of the windows scripting host used to execute NTFS alternate data streams.


```
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\*\\wscript.exe OR Image=C:\\Windows\\*\\cscript.exe) | regex CommandLine="(?<!\/)\b\w+(\.\w+)?:\w+(\.\w+)?$"
```




