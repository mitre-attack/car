---
title: "CAR-2020-09-002: Component Object Model Hijacking"
layout: analytic
submission_date: 2020/09/10
information_domain: Host
subtypes: Registry
analytic_type: Situational Awareness
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may establish persistence or escalate privileges by executing malicious content triggered by hijacked references to Component Object Model (COM) objects. This is typically done by replacing COM object registry entries under the HKEY_CURRENT_USER\Software\Classes\CLSID or HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID keys. Accordingly, this analytic looks for any changes under these keys.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Event Triggered Execution](https://attack.mitre.org/techniques/T1546/)|[Component Object Model Hijacking](https://attack.mitre.org/techniques/T1546/015/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SICA | [System Init Config Analysis](https://d3fend.mitre.org/technique/d3f:SystemInitConfigAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[registry](/data_model/registry) | [add](/data_model/registry#add) | [key](/data_model/registry#key) |
|[registry](/data_model/registry) | [remove](/data_model/registry#remove) | [key](/data_model/registry#key) |
|[registry](/data_model/registry) | [edit](/data_model/registry#edit) | [key](/data_model/registry#key) |



### Implementations

#### Pseudocode - COM object registry entry modification (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
registry_keys = search (Registry:Create AND Registry:Remove AND Registry:Edit)
clsid_keys = filter registry_keys where (
  key = "*\Software\Classes\CLSID\*")
output clsid_keys

```


#### Splunk search - COM object registry entry modification (Splunk, Sysmon native)


This Splunk search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows COM Object registry key.


```
index=__your_sysmon_index__ (EventCode=12 OR EventCode=13 OR EventCode=14) TargetObject="*\\Software\\Classes\\CLSID\\*"

```


#### LogPoint search - COM object registry entry modification (Logpoint, LogPoint native)


This LogPoint search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows COM Object registry key.


```
norm_id=WindowsSysmon event_id IN [12, 13, 14] target_object="*\Software\Classes\CLSID\*"

```




