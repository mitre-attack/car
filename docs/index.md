---
title: Welcome to the Cyber Analytics Repository
---
The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by [MITRE](https://www.mitre.org) based on the [MITRE ATT&CK](https://attack.mitre.org/) adversary model. CAR defines a data model that is leveraged in its pseudocode representations, but also includes implementations directly targeted at specific tools (e.g., Splunk, EQL) in its analytics. With respect to coverage, CAR is focused on providing a set of validated and well-explained analytics, in particular with regards to their operating theory and rationale.

If you want to start exploring, try viewing the [Full Analytic List](analytics). Also, check out the [ATT&CK Navigator layer](https://mitre-attack.github.io/attack-navigator/beta/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) that captures the current set of ATT&CK tactics and techniques covered by CAR.

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

### May 2021
* New analytics added - special thanks to the Splunk Threat Research team for working with us to incorporate these.
  * [CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store](/analytics/CAR-2021-05-001)
  * [CAR-2021-05-002: Batch File Write to System32](/analytics/CAR-2021-05-002)
  * [CAR-2021-05-003: BCDEdit Failure Recovery Modification](/analytics/CAR-2021-05-003)
  * [CAR-2021-05-004: BITS Job Persistence](/analytics/CAR-2021-05-004)
  * [CAR-2021-05-005: BITSAdmin Download File](/analytics/CAR-2021-05-005)
  * [CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments](/analytics/CAR-2021-05-006)
  * [CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments](/analytics/CAR-2021-05-007)
  * [CAR-2021-05-008: Certutil exe certificate extraction](/analytics/CAR-2021-05-008)
  * [CAR-2021-05-009: CertUtil With Decode Argument](/analytics/CAR-2021-05-009)
  * [CAR-2021-05-010: Create local admin accounts using net exe](/analytics/CAR-2021-05-010)
  * [CAR-2021-05-011: Create Remote Thread into LSASS](/analytics/CAR-2021-05-011)
  * [CAR-2021-05-012: Create Service In Suspicious File Path](/analytics/CAR-2021-05-012)

### April 2021
* New analytics added
  * [CAR-2021-04-001: Common Windows Process Masquerading](/analytics/CAR-2021-04-001)

### March 2021
* Added [Coverage Comparison](/coverage) page, which compares ATT&CK Technique/Sub-technique coverage across CAR, [Sigma](https://github.com/SigmaHQ/sigma), and [Elastic Detection](https://github.com/elastic/detection-rules) rules.
* New analytics added
  * [CAR-2021-01-006: Unusual Child Process Spawned using DDE Exploit](/analytics/CAR-2021-01-006)
  * [CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt](/analytics/CAR-2021-01-007)
  * [CAR-2021-01-008: Disable UAC](/analytics/CAR-2021-01-008)
  
### January-Feburary 2021
* New analytics added - special thanks to all of the submissions that we've received!
  * [CAR-2021-01-001: Identifying Port Scanning Activity](/analytics/CAR-2021-01-001)
  * [CAR-2021-01-002: Unusually Long Command Line Strings](/analytics/CAR-2021-01-002)
  * [CAR-2021-01-003: Clearing Windows Logs with Wevtutil](/analytics/CAR-2021-01-003)
  * [CAR-2021-01-004: Unusual Child Process For Spoolsv.Exe Or Connhost.Exe](/analytics/CAR-2021-01-004)
  * [CAR-2021-01-009: Detecting Shadow Copy Deletion via Vssadmin.exe](/analytics/CAR-2021-01-009)
  * [CAR-2021-02-001: Webshell-Indicative Process Tree](/analytics/CAR-2021-02-001)
  * [CAR-2021-02-002: Get System Elevation](/analytics/CAR-2021-02-002)

### November 2020
* Data Model update! We're excited to roll out these changes, and we think you will like the new capabilities.
  * [See the full new data model](data_model)
  * Added Authentication, Email, HTTP, and Socket objects
  * Updated other objects: 
    * Removed several unnecessary fields
    * Renamed some fields to make their intent more clear
    * Added several fields that have become necessary for modern analytics
    * Removed and added some Event types
* New analytics added
  * [CAR-2020-11-001: Boot or Logon Initialization Scripts](/analytics/CAR-2020-11-001)
  * [CAR-2020-11-002: Local Network Sniffing](/analytics/CAR-2020-11-002)
  * [CAR-2020-11-003: DLL Injection with Mavinject](/analytics/CAR-2020-11-003)
  * [CAR-2020-11-004: Processes Started From Irregular Parent](/analytics/CAR-2020-11-004)
  * [CAR-2020-11-005: Clear Powershell Console Command History](/analytics/CAR-2020-11-005)
  * [CAR-2020-11-006: Local Permission Group Discovery](/analytics/CAR-2020-11-006)
  * [CAR-2020-11-007: Network Share Connection Removal](/analytics/CAR-2020-11-007)
  * [CAR-2020-11-008: MSBuild and msxsl](/analytics/CAR-2020-11-008)
  * [CAR-2020-11-009: Compiled HTML Access](/analytics/CAR-2020-11-009)
  * [CAR-2020-11-010: CMSTP](/analytics/CAR-2020-11-010)
  * [CAR-2020-11-011: Registry Edit from Screensaver](/analytics/CAR-2020-11-011)
  
### September 2020
* New analytics added
  * [CAR-2020-09-001: Scheduled Task - File Access](/analytics/CAR-2020-09-001)
  * [CAR-2020-09-002: Component Object Model Hijacking](/analytics/CAR-2020-09-002)
  * [CAR-2020-09-003: Indicator Blocking - Driver Unloaded](/analytics/CAR-2020-09-003)
  * [CAR-2020-09-004: Credentials in Files & Registry](/analytics/CAR-2020-09-004)
  * [CAR-2020-09-005: AppInit DLLs](/analytics/CAR-2020-09-005)

### August 2020
* New analytics added
  * [CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities](/analytics/CAR-2020-08-001)
  * [CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS](/analytics/CAR-2020-08-002)
  
### July 2020
* Updated ATT&CK Detection for all analytics for [latest ATT&CK release](https://attack.mitre.org/resources/updates/updates-july-2020/).

### May 2020
* Updated [ATT&CK Navigator layer](https://mitre-attack.github.io/attack-navigator/beta/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) to incorporate sub-technique mappings for all CAR analytics.
* Added [Sysmon 11.0](/sensors/sysmon_11.0) sensor with data model mappings and CAR analytic coverage.
* Added one new field to the [Process object](/data_model/process)
  * `env_vars`
* New analytics added
  * [CAR-2020-05-001: MiniDump of LSASS](/analytics/CAR-2020-05-001)
  * [CAR-2020-05-003: Rare LolBAS Command Lines](/analytics/CAR-2020-05-003)

### April 2020
* All analytics have been updated to account for ATT&CK sub-techniques (wherever applicable). Check out the new sub-technique based coverage table [here](/analytics/index.html#analytic-list-by-techniquesub-technique-coverage).
* Added Applicable Platforms to all analytics. This captures the set of platforms the analytic may be applicable for; note that this does not necessarily mean that an implementation for a particular platform exists for a given analytic.
* Added YAML for [sensors](https://github.com/mitre-attack/car/tree/master/sensors) (those added recently) and [data models](https://github.com/mitre-attack/car/tree/master/data_model) on Github.
* New analytics added
  * [CAR-2020-04-001: Shadow Copy Deletion](/analytics/CAR-2020-04-001)

## Methodology
CAR analytics were developed to detect the adversary behaviors in [ATT&CK](https://attack.mitre.org/). Development of an analytic is based upon the following activities: 
* identifying and prioritizing adversary behaviors from the ATT&CK adversary model 
* identifying the data necessary to detect the adversary behavior
* identification or creation of a sensor to collect the necessary data
* the actual creation of the analytic to detect the identified behaviors

CAR is intended to be shared with cyber-defenders throughout the community.

[This](https://www.mitre.org/publications/technical-papers/ttp-based-hunting) white paper on TTP-based hunting provides some useful insight into many of these activities.

## CAR and ATT&CK

It's important to remember that ATT&CK and CAR are separate projects for good reason. It's critical to keep how we articulate threats with ATT&CK separate from a set of possible ways to detect them with the analytics. We don't want the defender content in ATT&CK to be overly prescriptive about how someone can defend against ATT&CK techniques because there could be many different ways, and it's up to the organization implementing them to determine what works best for their environment and the threats they face. This is why we didn't put the analytics in ATT&CK to begin with. CAR is a good starting point for many organizations and can be a great platform for open analytic collaboration - but it isn't the be-all/end-all for defending against the threats described by ATT&CK.

## Analytic Source Code Libraries

Some analytics are built as source code for specific products. In these cases, code might support a broad set of detections in a way that makes it hard to describe a set of distinct analytics. For these types of analytics, rather than integrating them into the main CAR site, we've collected them under a library of implementations. Currently, the only library is [BZAR](https://github.com/mitre-attack/bzar), a collection of Zeek (Bro) scripts looking primarily at SMB and RPC traffic.

## Contributing

We would love your contributions! Please see the [Contribution Guidance]({{ site.contributing }}) for more information.
