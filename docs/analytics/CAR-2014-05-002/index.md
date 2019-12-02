---
title: "CAR-2014-05-002: Services launching Cmd"
layout: analytic
submission_date: 2014/05/05
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

Windows runs the [Service Control Manager](https://en.wikipedia.org/wiki/Service_Control_Manager) (SCM) within the process `services.exe`. Windows launches services as independent processes or DLL loads within a [svchost.exe](https://en.wikipedia.org/wiki/svchost.exe) group. To be a legitimate service, a process (or DLL) must have the appropriate service entry point [SvcMain](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687414.aspx). If an application does not have the entry point, then it will timeout (default is 30 seconds) and the process will be killed.

To survive the timeout, [adversaries and red teams](https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf) can create services that direct to `cmd.exe` with the flag `/c`, followed by the desired command. The `/c` flag causes the command shell to run a command and immediately exit. As a result, the desired program will remain running and it will report an error starting the service. This analytic will catch that command prompt instance that is used to launch the actual malicious executable. Additionally, the children and descendants of services.exe will run as a SYSTEM user by default. Thus, services are a convenient way for an adversary to gain [Persistence](https://attack.mitre.org/tactics/TA0003) and [Privilege Escalation](https://attack.mitre.org/tactics/TA0004).


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[New Service](https://attack.mitre.org/techniques/T1050/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |


### Implementations

#### Pseudocode

Returns all processes named `cmd.exe` that have `services.exe` as a parent process. Because this should never happen, the `/c` flag is redundant in the search.


```
process = search Process:Create
cmd = filter process where (exe == "cmd.exe" and parent_exe == "services.exe")
output cmd
```


#### Splunk, Sysmon native

The Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\cmd.exe" ParentImage="C:\\Windows\\*\\services.exe"
```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "cmd.exe" and parent_process_name == "services.exe")
```




