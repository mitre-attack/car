---
title: "CAR-2021-02-001: Webshell-Indicative Process Tree"
layout: analytic
submission_date: 2020/11/29
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Nichols Jasper
applicable_platforms: Windows
---
<br><br>
A web shell is a web script placed on an openly accessible web server to allow an adversary to use the server as a gatway in a network. As the shell operates, commands will be issued from within the web application into the broader server operating system. This analytic looks for host enumeration executables initiated by any web service that would not normally be executed within that environment.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Server Software Component](https://attack.mitre.org/techniques/T1505/)|[Web Shell](https://attack.mitre.org/techniques/T1505/003/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode - Look for suspicious process tree beginning with web service (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
suspicious_processes = filter processes where (
  (parent_exe == "w3wp.exe" OR
   parent_exe == "httpd.exe" OR
   parent_exe == "tomcat*.exe" OR
   parent_exe == "nginx.exe" ) AND
  (exe == "cmd.exe" OR
   exe == "powershell.exe" OR
   exe == "net.exe" OR
   exe == "whoami.exe" OR
   exe == "hostname.exe" OR
   exe == "systeminfo.exe" OR
   exe == "ipconfig.exe) )
output suspicious_processes

```


#### Splunk Search - webshell-indicative process tree (Splunk, Sysmon native)


Look for host enumeration commands spawned by web services.


```
(index=__your_sysmon_index__ EventCode=1)
(ParentImage="C:\\Windows\\System32\\*w3wp.exe" OR ParentImage="*httpd.exe" OR ParentImage="*tomcat*.exe" OR ParentImage="*nginx.exe")
(Image="C:\\Windows\\System32\\cmd.exe OR Image="C:\\Windows\\SysWOW64\\cmd.exe" OR Image="C:\\Windows\\System32\\*\\powershell.exe OR Image="C:\\Windows\SysWOW64\\*\powershell.exe OR Image="C:\\Windows\\System32\\net.exe" OR Image="C:\\Windows\\System32\\hostname.exe" OR Image="C:\\Windows\\System32\\whoami.exe" OR Image="*systeminfo.exe OR Image="C:\\Windows\\System32\\ipconfig.exe")

```




