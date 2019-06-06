---
title: "CAR-2013-05-009: Running executables with same hash and different names"
layout: analytic
submission_date: 2013/05/23
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
---

Executables are generally not renamed, thus a given hash of an executable should only have ever one name. Identifying instances where multiple process names share the same hash may find cases where tools are copied by attackers to different folders or hosts to [avoid detection](https://attack.mitre.org/tactics/TA0005).

Although this analytic was initially based on MD5 hashes, it is equally applicable to any hashing convention.

### Output Description

A list of hashes and the different executables associated with each one

## ATT&CK Detection

|Technique |Tactic |Level of Coverage |
|---|---|---|
|[Masquerading](https://attack.mitre.org/techniques/T1036/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|

## Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [md5_hash](/data_model/process#md5_hash) |


## Implementations

### Basic Query (Splunk, Sysmon native)


This is a basic Splunk search that will output all of the sysmon-reported process images and their respective hashes, for cases where an image has more than one set of hashes. Thus, this will output a large amount of data and should be filtered by the analyst in order to make the results more useful.

```
index=__your_sysmon_index__ EventCode=1|stats dc(Hashes) as Num_Hashes values(Hashes) as "Hashes" by Image|where Num_Hashes > 1
```

