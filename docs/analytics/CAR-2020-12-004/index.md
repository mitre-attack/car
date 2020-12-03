---
 title: "CAR-2020-12-004: Unusual Child Process spawned using DDE exploit"
 layout: analytic
 submission_date: 2020/12/03
 information_domain: Host
 subtypes: Process
 analytic_type: TTP
 contributors: Cyware Labs
 applicable_platforms: Windows
 ---

 Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between             applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links               (duplications of changes to a data item), and requests for command execution.


 ### ATT&CK Detection

 |Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
 |---|---|---|---|
 |[Inter-Process Communication](https://attack.mitre.org/techniques/T1559/)|[Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002/)|[Execution](https://attack.mitre.org/tactics/TA0002/     )|Low|

 ### Data Model References

 |Object|Action|Field|
 |---|---|---|
 |[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [parent_image_path](/data_model/process#parent_image_path) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [integrity_level](/data_model/process#integrity_level) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [user](/data_model/process#user) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [parent_command_line](/data_model/process#parent_command_line) |


 ### Implementations

 #### Splunk, Sysmon native

 This Splunk query looks for any executable invocations from an Excel file.


 ```
 index = * ParentImage="*excel.exe*" Image="*.exe" | table _raw, ParentImage, Image
 ```


 #### Pseudocode, CAR

 This is a pseudocode version of the above Splunk query.


 ```
 processes = search Process:Create
 possible_exploit = filter processes where (
   ParentImage = 'excel.exe'
   and
   ChildProcess = '*.exe'
 )
 output possible_exfiltration
 ```
