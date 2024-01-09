---
title: "CAR-2013-04-002: Quick execution of a series of suspicious commands"
layout: analytic
submission_date: 2013/04/11
information_domain: Analytic, Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
Certain commands are frequently used by malicious actors and infrequently used by normal users. By looking for execution of these commands in short periods of time, we can not only see when a malicious user was on the system but also get an idea of what they were doing.

  Commands of interest:

-   arp.exe
-   at.exe
-   attrib.exe
-   cscript.exe
-   dsquery.exe
-   hostname.exe
-   ipconfig.exe
-   mimikatz.exe
-   nbstat.exe
-   net.exe
-   netsh.exe
-   nslookup.exe
-   ping.exe
-   quser.exe
-   qwinsta.exe
-   reg.exe
-   runas.exe
-   sc.exe
-   schtasks.exe
-   ssh.exe
-   systeminfo.exe
-   taskkill.exe
-   telnet.exe
-   tracert.exe
-   wscript.exe
-   xcopy.exe

### Output Description

The host on which the commands were executed, the time of execution, and what commands were executed


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Account Discovery](https://attack.mitre.org/techniques/T1087/)|[Local Account](https://attack.mitre.org/techniques/T1087/001/), [Domain Account](https://attack.mitre.org/techniques/T1087/002/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Security Account Manager](https://attack.mitre.org/techniques/T1003/002/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|[Local Groups](https://attack.mitre.org/techniques/T1069/001/), [Domain Groups](https://attack.mitre.org/techniques/T1069/002/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Process Discovery](https://attack.mitre.org/techniques/T1057/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|[SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Low|
|[Create or Modify System Process](https://attack.mitre.org/techniques/T1543/)|[Windows Service](https://attack.mitre.org/techniques/T1543/003/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Low|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|N/A|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|
|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|[Services Registry Permissions Weakness](https://attack.mitre.org/techniques/T1574/011/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Low|
|[Remote System Discovery](https://attack.mitre.org/techniques/T1018/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[System Services](https://attack.mitre.org/techniques/T1569/)|[Service Execution](https://attack.mitre.org/techniques/T1569/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Low|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[At](https://attack.mitre.org/techniques/T1053/002/), [Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Execution](https://attack.mitre.org/tactics/TA0002/)|Low|
|[Scheduled Transfer](https://attack.mitre.org/techniques/T1029/)|N/A|[Exfiltration](https://attack.mitre.org/tactics/TA0010/)|Low|
|[System Owner/User Discovery](https://attack.mitre.org/techniques/T1033/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[System Service Discovery](https://attack.mitre.org/techniques/T1007/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[System Information Discovery](https://attack.mitre.org/techniques/T1082/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[System Network Connections Discovery](https://attack.mitre.org/techniques/T1049/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Application Window Discovery](https://attack.mitre.org/techniques/T1010/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Software Discovery](https://attack.mitre.org/techniques/T1518/)|[Security Software Discovery](https://attack.mitre.org/techniques/T1518/001/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Network Service Discovery](https://attack.mitre.org/techniques/T1046/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|
|[Impair Defenses](https://attack.mitre.org/techniques/T1562/)|[Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/), [Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|
|[Account Manipulation](https://attack.mitre.org/techniques/T1098/)|N/A|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[Visual Basic](https://attack.mitre.org/techniques/T1059/005/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Query Registry](https://attack.mitre.org/techniques/T1012/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PLA | [Process Lineage Analysis](https://d3fend.mitre.org/technique/d3f:ProcessLineageAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [hostname](/data_model/process#hostname) |
|[process](/data_model/process) | [create](/data_model/process#create) | [ppid](/data_model/process#ppid) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode


```
processes = search Process:Create
reg_processes = filter processes where (exe == "arp.exe" or exe == "at.exe" or exe == "attrib.exe"
 or exe == "cscript.exe" or exe == "dsquery.exe" or exe == "hostname.exe"
 or exe == "ipconfig.exe" or exe == "mimikatz.exe" or exe == "nbstat.exe"
 or exe == "net.exe" or exe == "netsh.exe" or exe == "nslookup.exe"
 or exe == "ping.exe" or exe == "quser.exe" or exe == "qwinsta.exe"
 or exe == "reg.exe" or exe == "runas.exe" or exe == "sc.exe"
 or exe == "schtasks.exe" or exe == "ssh.exe" or exe == "systeminfo.exe"
 or exe == "taskkill.exe" or exe == "telnet.exe" or exe == "tracert.exe"
 or exe == "wscript.exe" or exe == "xcopy.exe")
reg_grouped = group reg by hostname, ppid where(max time between two events is 30 minutes)
output reg_grouped
```


#### Sigma

[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_multiple_suspicious_cli.yml) of the above pseudocode, with some modifications.



#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=regex(arp\.exe|at\.exe|attrib\.exe|cscript\.exe|dsquery\.exe|hostname\.exe|ipconfig\.exe|mimikatz.exe|nbstat\.exe|net\.exe|netsh\.exe|nslookup\.exe|ping\.exe|quser\.exe|qwinsta\.exe|reg\.exe|runas\.exe|sc\.exe|schtasks\.exe|ssh\.exe|systeminfo\.exe|taskkill\.exe|telnet\.exe|tracert\.exe|wscript\.exe|xcopy\.exe)i group count_unique $App limit 100
>>_agg count
>>_checkif int_compare Count > 1 include
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image IN ["*\arp.exe", "*\at.exe", "*\attrib.exe", "*\cscript.exe", "*\dsquery.exe", "*\hostname.exe", "*\ipconfig.exe", "*\mimikatz.exe", "*\nbstat.exe", "*\net.exe", "*\netsh.exe", "*\nslookup.exe", "*\ping.exe", "*\quser.exe", "*\qwinsta.exe", "*\reg.exe", "*\runas.exe", "*\sc.exe", "*\schtasks.exe", "*\ssh.exe", "*\systeminfo.exe", "*\taskkill.exe", "*\telnet.exe", "*\tracert.exe", "*\wscript.exe", "*\xcopy.exe"]
| chart count() as cnt by host
| search cnt > 1
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Within a command window, execute several of the commands in quick succession.

```
ipconfig /all
hostname
systeminfo
reg.exe Query HKLM\Software\Microsoft
```


