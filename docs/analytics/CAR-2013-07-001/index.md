---
title: "CAR-2013-07-001: Suspicious Arguments"
layout: analytic
submission_date: 2013/07/05
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
Malicious actors may rename built-in commands or external tools, such as those provided by SysInternals, to better [blend in](https://attack.mitre.org/tactics/TA0005) with the environment. In those cases, the file path name is arbitrary and may blend in well with the background. If the arguments are closely inspected, it may be possible to infer what tools are running and understand what an adversary is doing. When any legitimate software shares the same command lines, it must be whitelisted according to the expected parameters.

Any tool of interest with commonly known command line usage can be detecting by command line analysis. Known substrings of command lines include

-   PuTTY
-   port forwarding `-R * -pw`
-   secure copy (scp) `-pw * * *@*`
-   mimikatz `sekurlsa::`
-   RAR `* -hp *`
-   Archive`* a *`
    Additionally, it may be useful to find IP addresses in the command line
-   `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
    Logically this analytic makes use of [CAR-2014-03-005](../CAR-2014-03-005).


### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|
|[Remote Services](https://attack.mitre.org/techniques/T1021/)|N/A|[Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|
|[Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)|N/A|[Command and Control](https://attack.mitre.org/tactics/TA0011/), [Lateral Movement](https://attack.mitre.org/tactics/TA0008/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode

Identify process launches that contain substrings that belong to known tools and do not match the expected process names. These will help to indicate instances of tools that have been renamed. 


```
process = search Process:Create
port_fwd = filter process where (command_line match "-R .* -pw")
scp = filter process where (command_line match "-pw .* .* .*@.*"
mimikatz = filter process where (command_line match "sekurlsa")
rar = filter process where (command_line match " -hp ")
archive = filter process where (command_line match ".* a .*")
ip_addr = filter process where (command_line match \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})

output port_fwd, scp, mimikatz, rar, archive, ip_addr
```


#### Splunk, Sysmon native

Splunk version of the above pseudocode, excluding the IP address search.


```
index=__your_sysmon_index__ EventCode=1 (CommandLine="* -R * -pw*" OR CommandLine="* -pw * *@*" OR CommandLine="*sekurlsa*" OR CommandLine="* -hp *" OR CommandLine="* a *")
```


#### Eql, EQL native

EQL version of the above pseudocode, excluding the IP address search.


```
process where subtype.create and
  (command_line == "* -R * -pw*" or command_line == "* -pw * *@*" or command_line == "*sekurlsa*" or command_line == "* -hp *" or command_line == "* a *")
```


#### Splunk, Sysmon native

Splunk version of the above pseudocode, solely for the IP address search. Note that this will likely result in many false positives, since things like software version numbers can also be valid IPv4 addresses.


```
index=__your_sysmon_index__ EventCode=1 |regex CommandLine=".*\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b.*"
```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*(\-r.*\-pw|\-pw.*\@|sekurlsa|\-hp| a |\\d\{1\,3\}\\\.\\d\{1\,3\}\\\.\\d\{1\,3\}).*)i limit 100
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 (command="* -R * -pw*" OR command="* -pw * *@*" OR command="*sekurlsa*" OR command="* -hp *" OR command="* a *")
```



### Unit Tests

#### Test Case 1

**Configurations:** Windows 7

Download and run Putty from the command line to connect to an SSH server using remote port forwarding. Note that this requires specifying your remote system password on the command line, where it will be logged and visible. It is highly recommended that you specify an incorrect password and not complete the login, or use a temporary password.

```
putty.exe -pw <password> -R <port>:<host> <user>@<host>
```

#### Test Case 2

**Configurations:** Windows 7

Download 7zip or other archiving software you plan to monitor. Create an innocuous text file for testing, or substitute an existing file.

```
7z.exe a test.zip test.txt
```


