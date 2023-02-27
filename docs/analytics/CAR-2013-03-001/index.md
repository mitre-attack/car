---
title: "CAR-2013-03-001: Reg.exe called from Command Shell"
layout: analytic
submission_date: 2013/03/28
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Registry modifications are often essential in establishing persistence via known Windows mechanisms. Many legitimate modifications are done graphically via `regedit.exe` or by using the corresponding channels, or even calling the Registry APIs directly. The built-in utility `reg.exe` provides a [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) to the registry, so that queries and modifications can be performed from a shell, such as `cmd.exe`. When a user is responsible for these actions, the parent of `cmd.exe` will likely be `explorer.exe`. Occasionally, power users and administrators write scripts that do this behavior as well, but likely from a different process tree. These background scripts must be learned so they can be tuned out accordingly.

### Output Description

The sequence of processes that resulted in `reg.exe` being started from a shell. That is, a hierarchy that looks like

-   `great-grand_parent.exe`
-   `grand_parent.exe`
-   `parent.exe`
-   `reg.exe`



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Query Registry](https://attack.mitre.org/techniques/T1012/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)|[Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|[Services Registry Permissions Weakness](https://attack.mitre.org/techniques/T1574/011/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [hostname](/data_model/process#hostname) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [pid](/data_model/process#pid) |
|[process](/data_model/process) | [create](/data_model/process#create) | [ppid](/data_model/process#ppid) |



### Implementations

#### Pseudocode

To gain better context, it may be useful to also get information about the cmd process to know its parent. This may be helpful when tuning the analytic to an environment, if this behavior happens frequently. This may also help to rule out instances of users running 


```
processes = search Process:Create
reg = filter processes where (exe == "reg.exe" and parent_exe == "cmd.exe")
cmd = filter processes where (exe == "cmd.exe" and parent_exe != "explorer.exe"")
reg_and_cmd = join (reg, cmd) where (reg.ppid == cmd.pid and reg.hostname == cmd.hostname)
output reg_and_cmd

```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*reg\.exe.*)i AND $ParentProcess=regex(.*cmd\.exe.*)i as #A limit 100
>>_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*cmd\.exe.*)i NOT $ParentProcess=regex(.*explorer\.exe.*)i as #B limit 100
>>_checkif sjoin #B.$PPID = #A.$CPID str_compare #B.$SystemName eq #A.$SystemName include

```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Execute reg.exe from cmd.exe. Note that the analytic joins back to the grandparent process, which in this case is explorer.exe. The query time window must include the user log on. For example, if you logged in at 8am and tested the analytic at 10am, the query needs to search from 8am to 10am, not just at 10am. Within a command window, run the command.

```
reg.exe QUERY HKLM\Software\Microsoft
```


