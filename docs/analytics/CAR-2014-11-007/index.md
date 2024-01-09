---
title: "CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC"
layout: analytic
submission_date: 2014/11/19
information_domain: Host, Network
subtypes: API RPC, PCAP, Hostflow
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
As described in ATT&CK, an adversary can use [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to view or manipulate objects on a remote host. It can be used to remotely edit configuration, start services, query files, and anything that can be done with a WMI class. When remote WMI requests are over RPC ([CAR-2014-05-001](../CAR-2014-05-001)), it connects to a DCOM interface within the RPC group netsvcs. To detect this activity, a sensor is needed at the network level that can decode RPC traffic or on the host where the communication can be detected more natively, such as [Event Tracing for Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968803.aspx). Using wireshark/tshark decoders, the WMI interfaces can be extracted so that WMI activity over RPC can be detected.

Although the description details how to detect remote WMI precisely, a decent estimate has been to look for the string RPCSS within the initial RPC connection on 135/tcp. It returns a superset of this activity, and will trigger on all DCOM-related services running within RPC, which is likely to also be activity that should be detected between hosts.
More about RPCSS at : [rpcss_dcom_interfaces.html](http://www.hsc.fr/ressources/articles/win_net_srv/rpcss_dcom_interfaces.html)

### Output Description

Identifies the connection in which WMI traffic is seen, as well as the process(es) responsible for owning the connection.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)|N/A|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTA | [RPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:RPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [proto_info](/data_model/flow#proto_info) |



### Implementations

#### Pseudocode

To detect WMI over RPC (using DCOM), a sensor needs to exist that has the insight into individual connections and can actually decode and make sense of RPC traffic. Specifically, WMI can be detected by looking at RPC traffic where the target interface matches that of WMI, which is IRemUnknown2. 


```
flows = search Flow:Message
wmi_flow = filter flows where (dest_port == 135 and proto_info.rpc_interface == "IRemUnknown2")
output wmi_flow

```




