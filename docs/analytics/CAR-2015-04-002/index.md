---
title: "CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks"
layout: analytic
submission_date: 2015/04/29
information_domain: Host, Network
subtypes: Network API RPC, PCAP
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
An adversary can [move laterally](https://attack.mitre.org/tactics/TA0008) using the `schtasks` command to remotely [schedule tasks/jobs](https://attack.mitre.org/techniques/T1053). Although these events can be detected with command line analytics [CAR-2013-08-001](../CAR-2013-08-001), it is possible for an adversary to use the API directly, via the Task Scheduler GUI or with a scripting language such as [PowerShell](https://attack.mitre.org/techniques/T1059/001). In this cases, an additional source of data becomes necessary to detect adversarial behavior. When scheduled tasks are created remotely, Windows uses RPC (135/tcp) to communicate with the Task Scheduler on the remote machine. Once an RPC connection is established ([CAR-2014-05-001](../CAR-2014-05-001)), the client communicates with the Scheduled Tasks endpoint, which runs within the service group netsvcs. With packet capture and the right packet decoders or byte-stream based signatures, remote invocations of these functions can be identified.

Certain strings can be identifiers of the schtasks, by looking up the interface UUID of ITaskSchedulerService in different formats

-   UUID `86d35949-83c9-4044-b424-db363231fd0c` (decoded)
-   Hex `49 59 d3 86 c9 83 44 40 b4 24 db 36 32 31 fd 0c` (raw)
-   ASCII `IYD@$621` (printable bytes only)

This identifier is present three times during the RPC request phase. Any sensor that has access to the byte code as raw, decoded, or ASCII could implement this analytic.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTA | [RPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:RPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [dest_port](/data_model/flow#dest_port) |
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [src_port](/data_model/flow#src_port) |
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [proto_info](/data_model/flow#proto_info) |



### Implementations

#### Pseudocode

Look for RPC traffic after being mapped, which implies a destination port of at least 49152. If network inspection is available via packet captures or a NIDS, then traffic through the `ITaskSchedulerService` interface can be detected. Microsoft has a list of the possible methods that are implemented for the `ITaskSchedulerService` interface, which may be useful in differentiating read and query operations from creations and modifications.


```
flows = search Flow:Message
schtasks_rpc = filter flows where (
 src_port >= 49152 and dest_port >= 49152 and
 proto_info.rpc_interface == "ITaskSchedulerService"
)

output schtasks_rpc
```




