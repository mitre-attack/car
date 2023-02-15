---
title: "CAR-2021-01-001: Identifying Port Scanning Activity"
layout: analytic
submission_date: 2020/10/23
information_domain: Network
subtypes: Flow
analytic_type: Situational Awareness
contributors: Cyware Labs
applicable_platforms: Windows, Linux
---
<br><br>
After compromising an initial machine, adversaries commonly attempt to laterally move across the network. The first step to attempt the lateral movement often involves conducting host identification, port and service scans on the internal network via the compromised machine using tools such as Nmap, Cobalt Strike, etc.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Network Service Discovery](https://attack.mitre.org/techniques/T1046/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-CAA | [Connection Attempt Analysis](https://d3fend.mitre.org/technique/d3f:ConnectionAttemptAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_ip](/data_model/flow#dest_ip) |



### Implementations

#### Splunk search - Identifying Internal hosts and services for lateral movement (Splunk, Sysmon native)


It should be noted that when a host/ port/ service scan is performed from a compromised machine, a single machine makes multiple calls to other hosts in the network to identify live hosts and services. This can be detected using the following query


```
sourcetype='firewall_logs' dest_ip = 'internal_subnet' | stats dc(dest_port) as pcount by src_ip | where pcount >5
```




