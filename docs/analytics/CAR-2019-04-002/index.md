---
title: "CAR-2019-04-002: Generic Regsvr32"
layout: analytic
submission_date: 2019/04/24
information_domain: Host
subtypes: Process
analytic_type: Situational Awareness
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Regsvr32 can be used to execute arbitrary code in the context of a Windows signed binary, which can be used to bypass application whitelisting. This analytic looks for suspicious usage of the tool. It's not likely that you'll get millions of hits, but it does occur during normal activity so some form of baselining would be necessary for this to be an alerting analytic. Alternatively, it can be used for hunt by looking for new or anomalous DLLs manually.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|[Regsvr32](https://attack.mitre.org/techniques/T1218/010/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [image](/data_model/process#image) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_image](/data_model/process#parent_image) |



### Implementations

#### Main Pattern (Splunk, Sysmon native)


This just looks for all executions of regsvr32.exe that have a parent of regsvr32.exe but are not regsvr32.exe themselves (which happens). This will have a very high FP rate, but likely not on the order of millions.


```
index=__your_sysmon_data__ EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*"

```


#### Main Pattern - pseudocode (Pseudocode, CAR)


This is a pseudocode version of the above main pattern.


```
processes = search Process:Create
regsvr_processes = filter processes where (
  parent_image_path == "*regsvr32.exe" and image_path != "*regsvr32.exe*"
 )
output regsvr_processes

```


#### New items since last month (Splunk, Sysmon native)


This uses the same logic as above, but adds lightweight baselining by ignoring all results that also showed up in the previous 30 days (it runs over 1 day).


```
index=__your_sysmon_data__ earliest=-d@d latest=now() EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*" | search NOT [
search index=__your_sysmon_data__ earliest=-60d@d latest=-30d@d EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*" | dedup CommandLine | fields CommandLine ]

```


#### Spawning child processes (Splunk, Sysmon native)


This looks for child processes that may be spawend by regsvr32, while attempting to eliminate some of the common false positives such as werfault (Windows Error Reporting).


```
index=__your_sysmon_data__ EventCode=1 (ParentImage="C:\\Windows\\System32\\regsvr32.exe" OR ParentImage="C:\\Windows\\SysWOW64\\regsvr32.exe") AND Image!="C:\\Windows\\System32\\regsvr32.exe" AND Image!="C:\\Windows\\SysWOW64\\regsvr32.exe" AND Image!="C:\\WINDOWS\\System32\\regsvr32.exe" AND Image!="C:\\WINDOWS\\SysWOW64\\regsvr32.exe" AND Image!="C:\\Windows\\SysWOW64\\WerFault.exe" AND Image!="C:\\Windows\\System32\\wevtutil.exe" AND Image!="C:\\Windows\\System32\\WerFault.exe"|stats values(ComputerName) as "Computer Name" values(ParentCommandLine) as "Parent Command Line" count(Image) as ImageCount by Image

```


#### Spawning child processes - pseudocode (Pseudocode, CAR)


This is a pseudocode version of the above Splunk query for spawning child processes.


```
processes = search Process:Create
regsvr_processes = filter processes where (
  (parent_image_path == "C:\Windows\System32\regsvr32.exe" or parent_image_path == "C:\Windows\SysWOW64\regsvr32.exe") and
  image_path != "C:\Windows\System32\regsvr32.exe" and
  image_path != "C:\Windows\SysWOW64\regsvr32.exe" and
  image_path != "C:\Windows\SysWOW64\WerFault.exe" and
  image_path != "C:\Windows\System32\WerFault.exe" and
  image_path != "C:\Windows\System32\wevtutil.exe"
 )
output regsvr_processes

```


#### Loading unsigned images (Splunk, Sysmon native)


This looks for unsigned images that may be loaded by regsvr32, while attempting to eliminate false positives stemming from Windows/Program Files binaries.


```
index=__your_sysmon_data__ EventCode=7 (Image="C:\\Windows\\System32\\regsvr32.exe" OR Image="C:\\Windows\\SysWOW64\\regsvr32.exe") Signed=false ImageLoaded!="C:\\Program Files*" ImageLoaded!="C:\\Windows\\*"|stats values(ComputerName) as "Computer Name" count(ImageLoaded) as ImageLoadedCount by ImageLoaded

```


#### Loading unsigned images - pseudocode (Pseudocode, CAR)


This is a pseudocode version of the above Splunk query for loading unsigned images.


```
modules = search Module:Load
unsigned_modules = filter modules where (
  (image_path == "C:\Windows\System32\regsvr32.exe" or image_path == "C:\Windows\SysWOW64\regsvr32.exe") and
  signer == null and
  module_path != "C:\Program Files*" and
  module_path != "C:\Windows\*"
)
output unsigned_modules

```



### Unit Tests

#### Test Case 1

Any of the [Atomic Red Team tests for regsvr32.exe](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1117/T1117.md) should trigger this.


