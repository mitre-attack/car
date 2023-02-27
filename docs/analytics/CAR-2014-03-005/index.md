---
title: "CAR-2014-03-005: Remotely Launched Executables via Services"
layout: analytic
submission_date: 2014/03/18
information_domain: Host, Network
subtypes: Network Process, Hostflow
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
There are several ways to cause code to [execute](https://attack.mitre.org/tactics/TA0002) on a remote host. One of the most common methods is via the Windows [Service Control Manager](https://en.wikipedia.org/wiki/Service_Control_Manager) (SCM), which allows authorized users to remotely create and modify services. Several tools, such as [PsExec](https://attack.mitre.org/software/S0029), use this functionality.

When a client remotely communicates with the Service Control Manager, there are two observable behaviors. First, the client connects to the [RPC Endpoint Mapper](../CAR-2014-05-001) over 135/tcp. This handles authentication, and tells the client what port the endpoint—in this case the SCM—is listening on. Then, the client connects directly to the listening port on `services.exe`. If the request is to start an existing service with a known command line, the the SCM process will run the corresponding command.

This compound behavior can be detected by looking for `services.exe` receiving a network connection and immediately spawning a child process.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Create or Modify System Process](https://attack.mitre.org/techniques/T1543/)|[Windows Service](https://attack.mitre.org/techniques/T1543/003/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[System Services](https://attack.mitre.org/techniques/T1569/)|[Service Execution](https://attack.mitre.org/techniques/T1569/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTA | [RPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:RPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [pid](/data_model/flow#pid) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [pid](/data_model/process#pid) |



### Implementations

#### Pseudocode

Look for processes launched from `services.exe` within 1 second of services.exe receiving a network connection.


```
process = search Process:Create
flow = search Flow:Start
service = filter process where (parent_exe == "services.exe")
remote_start = join (flow, service ) where (
 flow.hostname == service.hostname and
 flow.pid == service.pid and
 (flow.time < service.time < flow.time + 1 second)
)
output remote_start

```




