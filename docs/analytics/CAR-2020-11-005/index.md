---
title: "CAR-2020-11-005: Clear Powershell Console Command History"
layout: analytic
submission_date: 2020/11/30
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Olaf Hartong
applicable_platforms: Windows
---
<br><br>
Adversaries may attempt to conceal their tracks by deleting the history of commands run within the Powershell console, or turning off history saving to begin with. This analytic looks for several commands that would do this. This does not capture the event if it is done within the console itself; only commandline-based commands are detected. Note that the command to remove the history file directly may very a bit if the history file is not saved in the default path on a particular system.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Indicator Removal](https://attack.mitre.org/techniques/T1070/)|[Clear Command History](https://attack.mitre.org/techniques/T1070/003/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |



### Implementations

#### Pseudocode - clear or disable Powershell console history via commandline (Pseudocode, CAR native)


This is a pseudocode representation of the below splunk search.


```
processes = search Process:Create
clear_commands = filter processes where (
  command_line ="*rm (Get-PSReadlineOption).HistorySavePath*" OR command_line="*del (Get-PSReadlineOption).HistorySavePath*" OR command_line="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR command_line="*Remove-Item (Get-PSReadlineOption).HistorySavePath*")  OR command_linee="del*Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt")
output clear_commands

```


#### Splunk Search - clear command history via Powershell (Splunk, Sysmon native)


Look for powershell commands that would clear command history


```
(index=__your_sysmon_index__ EventCode=1) (CommandLine="*rm (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="*del (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR CommandLine="*Remove-Item (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="del*Microsoft\\Windows\\Powershell\\PSReadline\\ConsoleHost_history.txt")

```


#### LogPoint Search - clear command history via Powershell (Logpoint, LogPoint native)


Look for powershell commands that would clear command history


```
norm_id=WindowsSysmon event_id=1 (command="*rm (Get-PSReadlineOption).HistorySavePath*" OR command="*del (Get-PSReadlineOption).HistorySavePath*" OR command="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR command="*Remove-Item (Get-PSReadlineOption).HistorySavePath*" OR command="del*Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt")

```




