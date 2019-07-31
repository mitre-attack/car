---
title: "CAR-2016-03-001: Host Discovery Commands"
layout: analytic
submission_date: 2016/03/24
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

When entering on a host for the first time, an adversary may try to [discover](https://attack.mitre.org/tactics/TA0007) information about the host. There are several built-in Windows commands that can be used to learn about the software configurations, active users, administrators, and networking configuration. These commands should be monitored to identify when an adversary is learning information about the system and environment. The information returned may impact choices an adversary can make when [establishing persistence](https://attack.mitre.org/tactics/TA0003), [escalating privileges](https://attack.mitre.org/tactics/TA0004), or [moving laterally](https://attack.mitre.org/tactics/TA0008).

Because these commands are built in, they may be run frequently by power users or even by normal users. Thus, an analytic looking at this information should have well-defined white- or blacklists, and should consider looking at an anomaly detection approach, so that this information can be learned dynamically.

Within the built-in Windows Commands:

-   `hostname`
-   `ipconfig`
-   `net`
-   `quser`
-   `qwinsta`
-   `sc` with flags `query`, `queryex`, `qc`
-   `systeminfo`
-   `tasklist`
-   `dsquery`
-   `whoami`

**Note** `dsquery` is only pre-existing on Windows servers.


#### ATT&CK Detection
|Technique |Tactic |Level of Coverage |
|---|---|---|
|[Account Discovery](https://attack.mitre.org/techniques/T1087/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Information Discovery](https://attack.mitre.org/techniques/T1082/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Owner/User Discovery](https://attack.mitre.org/techniques/T1033/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Process Discovery](https://attack.mitre.org/techniques/T1057/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Service Discovery](https://attack.mitre.org/techniques/T1007/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|

#### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |


#### Implementations

### Pseudocode

To be effective in deciphering malicious and benign activity, the full command line is essential. Similarly, having information about the parent process can help with making decisions and tuning to an environment.


```
process = search Process:Create
info_command = filter process where (
 exe == "hostname.exe" or 
 exe == "ipconfig.exe" or 
 exe == "net.exe" or 
 exe == "quser.exe" or 
 exe == "qwinsta.exe" or
 exe == "sc" and (command_line match " query" or command_line match " qc")) or
 exe == "systeminfo.exe" or 
 exe == "tasklist.exe" or 
 exe == "whoami.exe"
)
output info_command
```


### Splunk

Splunk version of the above pseudocode search.


```
index=__your_sysmon_index__ EventCode=1 (Image="C:\\Windows\\*\\hostname.exe" OR Image="C:\\Windows\\*\\ipconfig.exe" OR Image="C:\\Windows\\*\\net.exe" OR Image="C:\\Windows\\*\\quser.exe" OR Image="C:\\Windows\\*\\qwinsta.exe" OR (Image="C:\\Windows\\*\\sc.exe" AND (CommandLine="* query *" OR CommandLine="* qc *")) OR Image="C:\\Windows\\*\\systeminfo.exe" OR Image="C:\\Windows\\*\\tasklist.exe" OR Image="C:\\Windows\\*\\whoami.exe")|stats values(Image) as "Images" values(CommandLine) as "Command Lines" by ComputerName
```


### Eql

EQL version of the above pseudocode search.


```
process where subtype.create and
  (process_name == "hostname.exe" or process_name == "ipconfig.exe" or process_name == "net.exe" or process_name == "quser.exe" process_name == "qwinsta.exe" or process_name == "systeminfo.exe" or process_name == "tasklist.exe" or process_name == "whoami.exe" or (process_name == "sc.exe" and (command_line == "* query *" or command_line == "* qc *")))
```


