---
title: "CAR-2014-05-001: RPC Activity"
layout: analytic
submission_date: 2014/05/01
information_domain: Network
subtypes: Netflow
analytic_type: TTP, Situational Awareness
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Microsoft Windows uses its implementation of [Distributed Computing Environment/Remote Procedure Call](https://en.wikipedia.org/wiki/DCE/RPC) (DCE/RPC), which it calls [Microsoft RPC](https://en.wikipedia.org/wiki/Microsoft_RPC), to call certain APIs remotely.

A Remote Procedure Call is initiated by communicating to the RPC Endpoint Mapper, which exists as the Windows service RpcEptMapper and listens on the port 135/tcp. The endpoint mapper resolves a requested endpoint/interface and responds to the client with the port that the service is listening on. Since the RPC endpoints are assigned ports when the services start, these ports are dynamically assigned from 49152 to 65535. The connection to the endpoint mapper then terminates and the client program can communicate directly with the requested service.

RPC is a legitimate functionality of Windows that allows remote interaction with a variety of services. For a Windows environment to be properly configured, several programs use RPC to communicate legitimately with servers. The background and benign RPC activity may be enormous, but must be learned, especially peer-to-peer RPC between workstations, which is often indicative of [Lateral Movement](https://attack.mitre.org/tactics/TA0008).

According to ATT&CK, adversaries frequently use RPC connections to remotely

-   [Create/modify](https://attack.mitre.org/techniques/T1543/003) and [execute](https://attack.mitre.org/techniques/T1569/002) services ([CAR-2014-03-005](CAR-2014-03-005))
-   [Schedule Tasks](https://attack.mitre.org/techniques/T1053) ([CAR-2015-04-002](../CAR-2015-04-002))
-   Query ([CAR-2014-11-007](../CAR-2014-11-007)) and Invoke ([CAR-2014-12-001](../CAR-2014-12-001)) - [Windows Management Instrumentation (WMI)](https://attack.mitre.org/techniques/T1047)

Additional endpoints are detailed at [here](http://www.hsc.fr/ressources/articles/win_net_srv/well_known_named_pipes.html).


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002/), [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003/), [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTA | [RPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:RPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [dest_port](/data_model/flow#dest_port) |
|[flow](/data_model/flow) | [start](/data_model/flow#start) | [src_port](/data_model/flow#src_port) |



### Implementations

#### Pseudocode

Traffic to the RPC Endpoint Mapper will always have the destination port of 135. Assuming success, RPC traffic will continue to the endpoint. The endpoint and the client both bind to dynamically assigned ports (on Windows, this is typically greater than 49152). The traffic between the client and endpoint can be detected by looking at traffic to 135 followed by traffic where the source and destination ports are at least 49152. 


```
flows = search Flow:Start
rpc_mapper = filter flows where (dest_port == 135)
rpc_endpoint = filter flows where (dest_port >= 49152 and src_port >= 49152)
rpc = join rpc_mapper, rpc_endpoint where (
 (rpc_mapper.time < rpc_endpoint.time < rpc_mapper.time + 2 seconds) and
 (rpc_mapper.src_ip == rpc_endpoint.src_ip and rpc_mapper.dest_ip == rpc_endpoint.dest_ip)
)
output rpc
```




