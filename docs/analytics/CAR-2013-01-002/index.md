---
title: "CAR-2013-01-002: Autorun Differences"
layout: analytic
submission_date: 2013/01/25
information_domain: Analytic, Host
subtypes: Registry
analytic_type: Situational Awareness, TTP
contributors: MITRE
---

The Sysinternals tool [Autoruns](../sensors/autorums) checks the registry and file system for known identify persistence mechanisms. It will output any tools identified, including built-in or added-on Microsoft functionality and third party software. Many of these locations are known by adversaries and used to obtain [Persistence](https://attack.mitre.org/tactics/TA0003). Running Autoruns periodically in an environment makes it possible to collect and monitor its output for differences, which may include the removal or addition of persistent tools. Depending on the persistence mechanism and location, legitimate software may be more likely to make changes than an adversary tool. Thus, this analytic may result in significant noise in a highly dynamic environment. While Autoruns is a convenient method to scan for programs using persistence mechanisms its scanning nature does not conform well to streaming based analytics. This analytic could be replaced with one that draws from sensors that collect registry and file information if streaming analytics are desired.

Utilizes the Sysinternals autoruns tool (ignoring validated Microsoft entries). Primarily not a detection analytic by itself but through analysis of results by an analyst can be used for such. Building another analytic on top of this one identifying unusual entries would likely be a beneficial alternative.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Modify Existing Service](https://attack.mitre.org/techniques/T1031/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[New Service](https://attack.mitre.org/techniques/T1050/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Scheduled Task](https://attack.mitre.org/techniques/T1053/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Port Monitors](https://attack.mitre.org/techniques/T1013/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1060/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Path Interception](https://attack.mitre.org/techniques/T1034/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|
|[Accessibility Features](https://attack.mitre.org/techniques/T1015/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Modify Registry](https://attack.mitre.org/techniques/T1112/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Service Registry Permissions Weakness](https://attack.mitre.org/techniques/T1058/)|[Persistence](https://attack.mitre.org/tactics/TA0003/), [Execution](https://attack.mitre.org/tactics/TA0002/)|Moderate|
|[Windows Management Instrumentation Event Subscription](https://attack.mitre.org/techniques/T1084/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[File System Permissions Weakness](https://attack.mitre.org/techniques/T1044/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/), [Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Change Default File Association](https://attack.mitre.org/techniques/T1042/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Logon Scripts](https://attack.mitre.org/techniques/T1037/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[Winlogon Helper DLL](https://attack.mitre.org/techniques/T1004/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|
|[AppInit DLLs](https://attack.mitre.org/techniques/T1103/)|[Persistence](https://attack.mitre.org/tactics/TA0003/)|Moderate|


