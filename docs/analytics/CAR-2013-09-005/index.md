---
title: "CAR-2013-09-005: Service Outlier Executables"
layout: analytic
submission_date: 2013/09/23
information_domain: Host
subtypes: Process
analytic_type: Detection
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
New executables that are started as a service are suspicious. This analytic looks for anomalous service executables.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Create or Modify System Process](https://attack.mitre.org/techniques/T1543/)|[Windows Service](https://attack.mitre.org/techniques/T1543/003/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_image_path](/data_model/process#parent_image_path) |



### Implementations

#### Pseudocode

Create a baseline of services seen over the last 30 days and a list of services seen today. Remove services in the baseline from services seen today, leaving a list of new services.


```
processes = search Process:Create
services = filter processes where (parent_image_path == "C:\Windows\System32\services.exe")
historic_services = filter services (where timestamp < now - 1 day AND timestamp > now - 1 day)
current_services = filter services (where timestamp >= now - 1 day)
new_services = historic_services - current_services
output new_services
```


#### Sigma (Windows Event Log) (Sigma)


[Sigma/Windows Event Log](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_rare_service_installs.yml) rule with similar logic to the above pseudocode



#### Logpoint, LogPoint native

LogPoint version of the above sigma rule.


```
norm_id=WinServer event_id=7045
| chart count() as cnt by file
| search cnt < 5
```




