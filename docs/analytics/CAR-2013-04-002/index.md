---
title: "CAR-2013-04-002: Quick execution of a series of suspicious commands"
layout: analytic
submission_date: 2013/04/11
information_domain: Analytic, Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

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

## ATT&CK Detection

|Technique |Tactic |Level of Coverage |
|---|---|---|
|[Account Discovery](https://attack.mitre.org/techniques/T1087/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Moderate|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Process Discovery](https://attack.mitre.org/techniques/T1057/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Windows Admin Shares](https://attack.mitre.org/techniques/T1077/)|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|
|[New Service](https://attack.mitre.org/techniques/T1050/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Modify Existing Service](https://attack.mitre.org/techniques/T1031/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Service Registry Permissions Weakness](https://attack.mitre.org/techniques/T1058/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Remote System Discovery](https://attack.mitre.org/techniques/T1018/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Service Execution](https://attack.mitre.org/techniques/T1035/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Scheduled Task](https://attack.mitre.org/techniques/T1053/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Scheduled Transfer](https://attack.mitre.org/techniques/T1029/)|[Exfiltration](https://attack.mitre.org/tactics/TA0010/)|Moderate|
|[System Owner/User Discovery](https://attack.mitre.org/techniques/T1033/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Service Discovery](https://attack.mitre.org/techniques/T1007/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Information Discovery](https://attack.mitre.org/techniques/T1082/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Network Connections Discovery](https://attack.mitre.org/techniques/T1049/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Application Window Discovery](https://attack.mitre.org/techniques/T1010/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Security Software Discovery](https://attack.mitre.org/techniques/T1063/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Network Service Scanning](https://attack.mitre.org/techniques/T1046/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Disabling Security Tools](https://attack.mitre.org/techniques/T1089/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Account Manipulation](https://attack.mitre.org/techniques/T1098/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Moderate|
|[Indicator Blocking](https://attack.mitre.org/techniques/T1054/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Command-Line Interface](https://attack.mitre.org/techniques/T1059/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Query Registry](https://attack.mitre.org/techniques/T1012/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|

## Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [hostname](/data_model/process#hostname) |
|[process](/data_model/process) | [create](/data_model/process#create) | [ppid](/data_model/process#ppid) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |


## Implementations

### Pseudocode

```
processes = search Process:Create
reg_processes = filter processes where (exe == "arp.exe" or exe == "at.exe" or exe == "attrib.exe" 
 or exe == "cscript.exe" or exe == "dsquery.exe" or exe == "hostname.exe" 
 or exe == "ipconfig.exe" or exe == "mimikatz.exe" or exe == "nbstat.exe" 
 or exe == "net.exe" or exe == "netsh.exe" or exe == "nslookup.exe" 
 or exe == "ping.exe" or exe == "quser.exe" or exe == "qwinsta.exe" 
 or exe == "reg.exe" or exe == "runas.exe" or exe == "sc.exe" 
 or exe == "schtasks.exe" or exe == "ssh.exe" or exe == "systeminfo.exe" 
 or exe == "taskkill.exe" or exe == "telnet.exe" or exe == tracert.exe" 
 or exe == "wscript.exe" or exe == "xcopy.exe")
reg_grouped = group reg by hostname, ppid where(max time between two events is 30 minutes)
output reg_grouped
```


## Unit Tests

### Test Case 1

**Configurations:** Windows 7

Within a command window, execute several of the commands in quick succession.

```
ipconfig /all
hostname
systeminfo
reg.exe Query HKLM\Software\Microsoft
```
