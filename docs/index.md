---
title: Welcome to the Cyber Analytics Repository
---

The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by [MITRE](https://www.mitre.org) based on the [MITRE ATT&CK](https://attack.mitre.org/) adversary model.

If you want to start exploring, try viewing the [Full Analytic List](analytics) or use the [CAR Exploration Tool (CARET)](https://mitre-attack.github.io/caret/#/). Also, check out the new [ATT&CK Navigator Layer](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) that captures the current set of ATT&CK tactics and techniques covered by CAR.

Analytics stored in CAR contain the following information:
* a *hypothesis* which explains the idea behind the analytic
* the *information domain* or the primary domain the analytic is designed to operate within (e.g. host, network, process, external)
* references to [ATT&CK](https://attack.mitre.org/) Techniques and Tactics that the analytic detects
* the [Glossary](Glossary)
* a pseudocode description of how the analytic might be implemented
* a unit test which can be run to trigger the analytic

In addition to the analytics, CAR also contains a [data model](data_model) for observable data used to run the analytics and [sensors](sensors) that are used to collect that data.

## News
Information about the latest CAR updates and changes can be found in this section.

### February 2020
* Added [OSQuery 4.1.2](/sensors/osquery_4.1.2)) sensor with data model mappings and CAR analytic coverage.

### January 2020
* Added [Sysmon 10.4](/sensors/sysmon_10.4) sensor with data model mappings and CAR analytic coverage.

### December 2019
* Added true positives (examples of real events that the analytic should successfully detect) to:
  * [CAR-2013-10-002: DLL Injection via LoadLibrary](/analytics/CAR-2013-10-002)
  * [CAR-2014-04-003: Powershell Execution](/analytics/CAR-2014-04-003)
  * [CAR-2016-03-001: Host Discovery Commands](/analytics/CAR-2016-03-001)
  * [CAR-2019-08-001: Credential Dumping via Window Task Manager](/analytics/CAR-2019-08-001) 
  
### August 2019
* New analytics added
  * [CAR-2019-08-001: Credential Dumping via Windows Task Manager](/analytics/CAR-2019-08-001)
  * [CAR-2019-08-002: Active Directory Dumping via NTDSUtil](/analytics/CAR-2019-08-002)
    
### July 2019
* Added Splunk/Sysmon implementations to several analytics
* Added [EQL](https://eqllib.readthedocs.io/en/latest/index.html) implementations to several analytics
* Added corresponding [Sigma](https://github.com/Neo23x0/sigma) rule references to several analytics
* New analytics added
  * [CAR-2019-07-001: Access Permission Modification](/analytics/CAR-2019-07-001)
  * [CAR-2019-07-002: Lsass Process Dump via Procdump](/analytics/CAR-2019-07-002)


### May 2019
* All CAR analytics have been converted to YAML; the YAML versions can be found [here](https://github.com/mitre-attack/car/tree/master/analytics).
* Added an [ATT&CK Navigator Layer](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) for capturing the current set of ATT&CK tactics/techniques covered by CAR analytics.

### April 2019
* Four new analytics were added
  * [CAR-2019-04-001: UAC Bypass](/analytics/CAR-2019-04-001)
  * [CAR-2019-04-002: Generic Regsvr32](/analytics/CAR-2019-04-002)
  * [CAR-2019-04-003: Squiblydoo](/analytics/CAR-2019-04-003)
  * [CAR-2019-04-004: Credential Dumping via Mimikatz](/analytics/CAR-2019-04-004)
* Three new fields were added to the [Process object](/data_model/process)
  * `integrity_level`
  * `parent_command_line`
  * `current_working_directory`

## Methodology
CAR analytics were developed to detect the adversary behaviors in [ATT&CK](https://attack.mitre.org/). Development of an analytic is based upon the following activities: 
* identifying and prioritizing adversary behaviors from the ATT&CK adversary model 
* identifying the data necessary to detect the adversary behavior
* identification or creation of a sensor to collect the necessary data
* the actual creation of the analytic to detect the identified behaviors

CAR is intended to be shared with cyber-defenders throughout the community.

## CAR and ATT&CK

It's important to remember that ATT&CK and CAR are separate projects for good reason. It's critical to keep how we articulate threats with ATT&CK separate from a set of possible ways to detect them with the analytics. We don't want the defender content in ATT&CK to be overly prescriptive about how someone can defend against ATT&CK techniques because there could be many different ways, and it's up to the organization implementing them to determine what works best for their environment and the threats they face. This is why we didn't put the analytics in ATT&CK to begin with. CAR is a good starting point for many organizations and can be a great platform for open analytic collaboration - but it isn't the be-all/end-all for defending against the threats described by ATT&CK.

## Analytic Source Code Libraries

Some analytics are built as source code for specific products. In these cases, code might support a broad set of detections in a way that makes it hard to describe a set of distinct analytics. For these types of analytics, rather than integrating them into the main CAR site, we've collected them under a library of implementations. Currently, the only library is [BZAR](https://github.com/mitre-attack/car/tree/master/implementations/bzar), a collection of Zeek (Bro) scripts looking primarily at SMB and RPC traffic.

## Contributing

We would love your contributions! Please see the [Contribution Guidance]({{ site.contributing }}) for more information.
