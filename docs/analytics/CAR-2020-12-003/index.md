---
 title: "CAR-2020-12-003: Non Standard User Agent Strings used to make outbound connections"
 layout: analytic
 submission_date: 2020/12/03
 information_domain: Host
 subtypes: Process
 analytic_type: TTP
 contributors: Cyware Labs
 applicable_platforms: Windows
 ---

 Adversaries may steal data by exfiltrating it over an existing command and control (C2) channel. They may try to use existing tools or custom scripts to exfiltrate data to a C2 channel. Such scripts may  use non standard user agent strings while establishing the C2 communication. This analytics tries to detect the non-standard user agent strings used to make C2 communications.


 ### ATT&CK Detection

 |Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
 |---|---|---|---|
 |[Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/)|N/A|[Exfiltration](https://attack.mitre.org/tactics/TA0010/)|Low|

 ### Data Model References

 |Object|Action|Field|
 |---|---|---|
 |[process](/data_model/process) | [create](/data_model/process#create) | [image_path](/data_model/process#image_path) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [parent_image_path](/data_model/process#parent_image_path) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [integrity_level](/data_model/process#integrity_level) |
 |[process](/data_model/process) | [create](/data_model/process#create) | [parent_command_line](/data_model/process#parent_command_line) |


 ### Implementations

 #### Splunk, Sysmon native

 This Splunk query looks for unusual or non standard user agent strings used to make outbound communications.


 ```
 index=__proxy_logs__  | table clientip, useragent | lookup user_agent.csv user_agent as useragent outputnew user_agent as user_agent | fillnull value=NULL user_agent| where user_agent="NULL" | stats      count,values(useragent) as useragents by clientip | where count > 15
 ```


 #### Pseudocode, CAR

 This is a pseudocode version of the above Splunk query.

 ```
 processes = search Process:Create
 possible_exfiltration = filter user_agents where (
   user_agent not in user_agent.csv
   and
   count > 10
 )
 output possible_exfiltration
 ```
