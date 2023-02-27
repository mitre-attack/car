---
title: "CAR-2020-11-008: MSBuild and msxsl"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Trusted developer utilities such as MSBuild may be leveraged to run malicious code with elevated privileges. This analytic looks for any instances of msbuild.exe, which will execute any C# code placed within a given XML document; and msxsl.exe, which processes xsl transformation specifications for XML files and will execute a variaty of scripting languages contained within the XSL file. Both of these executables are rarely used outside of Visual Studio.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127/)|[MSBuild](https://attack.mitre.org/techniques/T1127/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|High|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |



### Implementations

#### Pseudocode - msbuild (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
target_processes = filter processes where (
  (exe="C:\Program Files (x86)\Microsoft Visual Studio\*\bin\MSBuild.exe" OR exe="C:\Windows\Microsoft.NET\Framework*\msbuild.exe" OR exe="C:\users\*\appdata\roaming\microsoft\msxsl.exe") AND
  image_path!="*Microsoft Visual Studio*")
output target_processes

```


#### Splunk Search - msbuild (Splunk, Sysmon native)


Looks for all instances of msbuild.exe or msxsl.exe


```
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Program Files (x86)\\Microsoft Visual Studio\\*\\bin\\MSBuild.exe" OR Image="C:\\Windows\\Microsoft.NET\\Framework*\\msbuild.exe" OR Image="C:\\users\\*\\appdata\\roaming\\microsoft\\msxsl.exe") ParentImage!="*\\Microsoft Visual Studio*")

```


#### LogPoint Search - msbuild (Logpoint, LogPoint native)


Looks for all instances of msbuild.exe or msxsl.exe


```
norm_id=WindowsSysmon event_id=1 (image IN ["C:\Program Files (x86)\Microsoft Visual Studio\*\bin\MSBuild.exe", "C:\Windows\Microsoft.NET\Framework*\msbuild.exe", "C:\Users\*\appdata\roaming\microsoft\msxsl.exe") -parent_image="*\Microsoft Visual Studio*")

```




