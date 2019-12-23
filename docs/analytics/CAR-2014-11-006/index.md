---
title: "CAR-2014-11-006: Windows Remote Management (WinRM)"
layout: analytic
submission_date: 2014/11/19
information_domain: Host, Network
subtypes: Network, Netflow
analytic_type: Situational Awareness
contributors: MITRE
---

When a [Windows Remote Management](https://attack.mitre.org/techniques/T1028/) connection is opened, the client sends HTTP requests to port 5985 for HTTP or 5986 for HTTPS on the target host. Each HTTP(S) request to the URI "/wsman" is called, and other information is set in the headers. Depending on the operation, the HTTP method may vary (i.e., GET, POST, etc.). This analytic would detect Remote PowerShell, as well as other communications that rely on WinRM. Additionally, it outputs the executable on the client host, the connection information, and the hostname of the target host.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Windows Remote Management](https://attack.mitre.org/techniques/T1028/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|High|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_port](/data_model/flow#dest_port) |


### Implementations

#### Pseudocode

Look for network connections to port 5985 and 5986. To really decipher what is going on, these outputs should be fed into something that can do packet analysis. 


```
flow = search Flow:Start
winrm = filter flow where (dest_port == 5985)
winrm_s = filter flow where (dest_port == 5986)
output winrm, winrm_s
```




