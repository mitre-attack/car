---
title: "CAR-2016-04-002: User Activity from Clearing Event Logs"
layout: analytic
submission_date: 2016/04/14
information_domain: Host
subtypes: Event Records, Process
analytic_type: Anomaly
contributors: MITRE/NSA, Cyware Labs, Lucas Heiligenstein
applicable_platforms: Windows, Linux, macOS
---
<br><br>
It is unlikely that event log data would be cleared during normal operations, and it is likely that malicious attackers may try to cover their tracks by clearing an event log. When an event log gets cleared, it is suspicious. 1. This is often done using `wevtutil`, a legitimate tool provided by Microsoft. This action interferes with event collection and notification, and may lead to a security event going undetected, thereby potentially leading to further compromise of the network. 2. Alerting when a `Clear Event Log` is generated could point to this intruder technique. Centrally collecting events has the added benefit of making it much harder for attackers to cover their tracks. Event Forwarding permits sources to forward multiple copies of a collected event to multiple collectors, thus enabling redundant event collection. Using a redundant event collection model can minimize the single point of failure risk. 3. Attackers may set the option of the sources of events with `Limit-EventLog -LogName Security -OverflowAction DoNotOverwrite` to not delete old Evenlog when the .evtx is full. By default the Security Log size is configured with the minimum value of 20 480KB (~23 000 EventLog). So if this option is enabled, all the new EventLogs will be automatically deleted. We can detect this behavior with the Security EventLog 1104. 4. Attackers may delete .evtx with `del C:\Windows\System32\winevt\logs\Security.evtx` or `Remove-Item C:\Windows\System32\winevt\logs\Security.evtx` after having disabled and stopped the Eventlog service. As the EventLog service is disabled and stopped, the .evtx files are no longer used by this service and can be deleted. The new EventLog will be Unavailable until the configuration is reset. 5. Attackers may use the powershell command `Remove-EventLog -LogName Security` to unregister source of events that are part of Windows (Application, Security…). This command deletes the security EventLog (which also generates EventId 1102) but the new Eventlogs are still recorded until the system is rebooted . After the System is rebooted, the Security log is unregistered and doesn’t log any new Eventlog. However logs generated between the command and the reboot are still available in the .evtx file.

#### References
https://ptylu.github.io/content/report/report.html?report=26


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Indicator Removal](https://attack.mitre.org/techniques/T1070/)|[Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-RTA | [RPC Traffic Analysis](https://d3fend.mitre.org/technique/d3f:RPCTrafficAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### PseudoCode for dedicated EventID EventLog deletion (Pseudocode)


When an eventlog is cleared, a new event is created that alerts that the eventlog was cleared. For Security logs, its event code 1100 and 1102. For System logs, it is event code 104.


```
([log_name] == "Security" and [event_code] in [1100, 1102, 1104]) or
([log_name] == "System" and [event_code] == 104)

```


#### Sigma rule (System log) (Sigma)


[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_susp_eventlog_cleared.yml) of the above pseudocode, focusing only on the System log.



#### Sigma rule (Security log) (Sigma)


[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_susp_security_eventlog_cleared.yml) of the above pseudocode, focusing only on the Security log.



#### LogPoint version of the above pseudocode. (Logpoint, LogPoint native)


LogPoint version of the above pseudocode.


```
norm_id=WinServer ((channel="Security" event_id IN [1100,1102]) OR (channel="System" event_id=104))

```


#### Splunk search - Detecting log clearing with wevtutil (Splunk, Sysmon native)


This search query looks for  wevtutil, Clear-EventLog, Limit-EventLog, Remove-Item or Remove-EventLog inside a command that may cause the system to remove Windows Event logs.


```
index=__your_sysmon_index__ sourcetype= __your__windows__sysmon__sourcetype EventCode=1 (Image=*wevtutil* CommandLine=*cl* (CommandLine=*System* OR CommandLine=*Security* OR CommandLine=*Setup* OR CommandLine=*Application*) OR Clear-EventLog OR Limit-EventLog OR (Remove-Item AND .evtx) OR Remove-EventLog)

```



### Unit Tests

#### Test Case 1

You can use the powershell cmdlet “Clear-Eventlog” to clear event logs. Open Powershell as administrator and execute Clear-Eventlog `Clear-EventLog [-LogName] \<String[]\>`. [Additional information here](https://technet.microsoft.com/en-us/library/hh849789.aspx).

```
Clear-Eventlog Security
Clear-Eventlog System
```

#### Test Case 2

Command to not Overwrite old EventLog

```
Limit-EventLog -LogName Security -OverflowAction DoNotOverwrite
```

#### Test Case 3

Cmd and Powershell command to delete EventLog (only possible after turning off the EventLog service)

```
del C:\Windows\System32\winevt\logs\Security.evtx
Remove-Item C:\Windows\System32\winevt\logs\Security.evtx
```

#### Test Case 4

Unregister EventLog source

```
Remove-EventLog -LogName Security
```


