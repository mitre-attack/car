---
title: "CAR-2015-04-001: Remotely Scheduled Tasks via AT"
layout: analytic
submission_date: 2015/04/29
information_domain: Host, Network
subtypes: File API, PCAP
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
When AT.exe is used to remotely [schedule tasks](https://attack.mitre.org/techniques/T1053), Windows uses named pipes over [SMB](https://en.wikipedia.org/wiki/Server_Message_Block) to communicate with the API on the remote machine. After authentication over SMB, the Named Pipe "ATSVC" is opened, over which the JobAdd function is called. On the remote host, the job files are created by the Task Scheduler and follow the convention `C:\Windows\System32\AT<job\_id>`. Unlike [CAR-2013-05-004](../CAR-2013-05-004), this analytic specifically focuses on uses of AT that can be detected between hosts, indicating remotely gained [execution](https://attack.mitre.org/tactics/TA0002).

This pipe activity could be discovered with a network decoder, such as that in wireshark, that can inspect SMB traffic to identify the use of pipes. It could also be detected by looking for raw packet capture streams or from a custom sensor on the host that hooks the appropriate API functions. If no network or API level of visibility is possible, this traffic may inferred by looking at SMB connections over 445/tcp followed by the creation of files matching the pattern `C:\Windows\System32\AT\<job_id\>`.


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[At](https://attack.mitre.org/techniques/T1053/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-IPCTA | [IPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:IPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](/data_model/flow) | [message](/data_model/flow#message) | [proto_info](/data_model/flow#proto_info) |



### Implementations

#### Pseudocode

To detect AT via network traffic, a sensor is needed that has the ability to extract and decode PCAP information. Specifically, it needs to properly decode SMB and the functions that are implemented over it via NamedPipes. If a sensor meets these criteria, then the PCAP data needs to search for instances of the command `JobAdd` over the pipe `ATSVC`, which is all implemented over Windows SMB 445/tcp.


```
flows = search Flow:Message
at_proto = filter flows where (dest_port == 445 and proto_info.pipe == "ATSVC")
at_create = filter flows where (proto_info.function == "JobAdd")

output at_create
```




