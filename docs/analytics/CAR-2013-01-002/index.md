---
title: "CAR-2013-01-002: Autorun Differences"
layout: analytic
submission_date: 2013/01/25
information_domain: Analytic, Host
subtypes: Registry
analytic_type: Situational Awareness, TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
The Sysinternals tool [Autoruns](../sensors/autoruns) checks the registry and file system for known identify persistence mechanisms. It will output any tools identified, including built-in or added-on Microsoft functionality and third party software. Many of these locations are known by adversaries and used to obtain [Persistence](https://attack.mitre.org/tactics/TA0003). Running Autoruns periodically in an environment makes it possible to collect and monitor its output for differences, which may include the removal or addition of persistent tools. Depending on the persistence mechanism and location, legitimate software may be more likely to make changes than an adversary tool. Thus, this analytic may result in significant noise in a highly dynamic environment. While Autoruns is a convenient method to scan for programs using persistence mechanisms its scanning nature does not conform well to streaming based analytics. This analytic could be replaced with one that draws from sensors that collect registry and file information if streaming analytics are desired.

Utilizes the Sysinternals autoruns tool (ignoring validated Microsoft entries). Primarily not a detection analytic by itself but through analysis of results by an analyst can be used for such. Building another analytic on top of this one identifying unusual entries would likely be a beneficial alternative.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Create or Modify System Process](https://attack.mitre.org/techniques/T1543/)|[Windows Service](https://attack.mitre.org/techniques/T1543/003/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)|[Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)|[Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/), [Port Monitors](https://attack.mitre.org/techniques/T1547/010/), [Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|[Path Interception by PATH Environment Variable](https://attack.mitre.org/techniques/T1574/007/), [Path Interception by Search Order Hijacking](https://attack.mitre.org/techniques/T1574/008/), [Path Interception by Unquoted Path](https://attack.mitre.org/techniques/T1574/009/), [Services File Permissions Weakness](https://attack.mitre.org/techniques/T1574/010/), [Services Registry Permissions Weakness](https://attack.mitre.org/techniques/T1574/011/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Event Triggered Execution](https://attack.mitre.org/techniques/T1546/)|[Change Default File Association](https://attack.mitre.org/techniques/T1546/001/), [Windows Management Instrumentation Event Subscription](https://attack.mitre.org/techniques/T1546/003/), [Accessibility Features](https://attack.mitre.org/techniques/T1546/008/), [AppInit DLLs](https://attack.mitre.org/techniques/T1546/010/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|N/A|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037/)|[Logon Script (Windows)](https://attack.mitre.org/techniques/T1037/001/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SICA | [System Init Config Analysis](https://d3fend.mitre.org/technique/d3f:SystemInitConfigAnalysis)| 






