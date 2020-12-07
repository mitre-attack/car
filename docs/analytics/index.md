---
title: "Analytics"
permalink: /analytics/
---
<div class="analytics-table"></div> 

## Analytic List (by date added)

|Analytic|ATT&CK Techniques|Implementations|Applicable Platform(s)|
|---|---|---|---|
|[CAR-2020-11-001: Boot or Logon Initialization Scripts](CAR-2020-11-001)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1037/">Boot or Logon Initialization Scripts</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-002: Local Network Sniffing](CAR-2020-11-002)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1040/">Network Sniffing</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-003: DLL Injection with Mavinject](CAR-2020-11-003)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1055/">Process Injection</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-004: Processes Started From Irregular Parent](CAR-2020-11-004)||Pseudocode, Splunk|Windows|
|[CAR-2020-11-005: Clear Powershell Console Command History](CAR-2020-11-005)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal on Host</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-006: Local Permission Group Discovery](CAR-2020-11-006)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1069/">Permission Groups Discovery</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-007: Network Share Connection Removal](CAR-2020-11-007)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal on Host</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-008: MSBuild and msxsl](CAR-2020-11-008)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1127/">Trusted Developer Utilities Proxy Execution</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-009: Compiled HTML Access](CAR-2020-11-009)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1218/">Signed Binary Proxy Execution</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-010: CMSTP](CAR-2020-11-010)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1218/">Signed Binary Proxy Execution</a></li></ul>{:/}|Pseudocode, Splunk|Windows|
|[CAR-2020-11-011: CMSTP](CAR-2020-11-011)|{::nomarkdown}<ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul>{:/}|Pseudocode, Splunk|Windows|

---
## Analytic List (by technique/sub-technique coverage)

|ATT&CK Technique|ATT&CK Sub-technique(s)|CAR Analytic(s)|
|---|---|---|
|[Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037/)|[Logon Script (Windows)](https://attack.mitre.org/techniques/T1037/001/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-001">CAR-2020-11-001: Boot or Logon Initialization Scripts</a></li></ul>{:/}|
|[Process Injection](https://attack.mitre.org/techniques/T1055/)|[Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-003">CAR-2020-11-003: DLL Injection with Mavinject</a></li></ul>{:/}|
|[Indicator Removal on Host](https://attack.mitre.org/techniques/T1070/)|(N/A - see below)|(N/A - see below)|
|...|[Clear Command History](https://attack.mitre.org/techniques/T1070/003/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-005">CAR-2020-11-005: Clear Powershell Console Command History</a></li></ul>{:/}|
|...|[Network Share Connection Removal](https://attack.mitre.org/techniques/T1070/005/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-007">CAR-2020-11-007: Network Share Connection Removal</a></li></ul>{:/}|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|(N/A - see below)|(N/A - see below)|
|...|[Local Groups](https://attack.mitre.org/techniques/T1069/001/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-006">CAR-2020-11-006: Local Permission Group Discovery</a></li></ul>{:/}|
|...|[Domain Groups](https://attack.mitre.org/techniques/T1069/002/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-006">CAR-2020-11-006: Local Permission Group Discovery</a></li></ul>{:/}|
|[Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127/)|[MSBuild](https://attack.mitre.org/techniques/T1127/001/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-008">CAR-2020-11-008: MSBuild and msxsl</a></li></ul>{:/}|
|[Signed Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)|(N/A - see below)|(N/A - see below)|
|...|[Compiled HTML File](https://attack.mitre.org/techniques/T1218/001/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-009">CAR-2020-11-009: Compiled HTML Access</a></li></ul>{:/}|
|...|[CMSTP](https://attack.mitre.org/techniques/T1218/003/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-010">CAR-2020-11-010: CMSTP</a></li></ul>{:/}|
|[Event Triggered Execution](https://attack.mitre.org/techniques/T1546/)|[Screensaver](https://attack.mitre.org/techniques/T1546/002/)|{::nomarkdown}<ul><li><a href="CAR-2020-11-011">CAR-2020-11-011: CMSTP</a></li></ul>{:/}|
