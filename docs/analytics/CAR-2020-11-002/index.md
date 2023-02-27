---
title: "CAR-2020-11-002: Local Network Sniffing"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: Situational Awareness
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may use a variety of tools to gain visibility on the current status of things on the network: which processes are listening on which ports, which services are running on other hosts, etc. This analytic looks for the names of the most common network sniffing tools. While this may be noisy on networks where sysadmins are using any of these tools on a regular basis, in most networks their use is noteworthy.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Network Sniffing](https://attack.mitre.org/techniques/T1040/)|N/A|[Credential Access](https://attack.mitre.org/tactics/TA0006/), [Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|


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

#### Pseudocode - commands containing known network sniffing application names (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
sniffer_processes = filter processes where (
  exe = "tshark.exe" OR
  exe = "windump.exe" OR
  (exe = "logman.exe" AND parent_exe exists AND parent_exe!="C:\Program Files\Windows Event Reporting\Core\EventReporting.AgentService.exe") OR
  exe = "tcpdump.exe" OR
  exe = "wprui.exe" OR
  exe = "wpr.exe" )
output sniffer_processes

```


#### Splunk Search - common network traffic sniffing apps being run (Splunk, Sysmon native)


look for common network traffic sniffing apps being run


```
(index=__your_sysmon_index__ EventCode=1) (Image="*tshark.exe" OR Image="*windump.exe" OR (Image="*logman.exe" AND ParentImage!="?" AND ParentImage!="C:\\Program Files\\Windows Event Reporting\\Core\\EventReporting.AgentService.exe") OR Image="*tcpdump.exe" OR Image="*wprui.exe" OR Image="*wpr.exe")

```


#### LogPoint Search - common network traffic sniffing apps being run (Logpoint, LogPoint native)


look for common network traffic sniffing apps being run


```
norm_id=WindowsSysmon event_id=1 (image="*\tshark.exe" OR image="*\windump.exe" OR (image="*\logman.exe" -parent_image="?" -parent_image="C:\Program Files\Windows Event Reporting\Core\EventReporting.AgentService.exe") OR image="*\tcpdump.exe" OR image="*\wprui.exe" OR image="*\wpr.exe")

```




