---
title: Updates
---
## News
Information about the latest CAR updates and changes can be found in this section.

### February 2022
* Updated [analytic coverage](/coverage) page, now with separate ATT&CK navigator layers for each repository.
* New analytics added
  * [CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify](/analytics/CAR-2021-11-002)
  * [CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths](/analytics/CAR-2021-12-001)
  * [CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key "Common Startup"](/analytics/CAR-2021-12-002)

### January 2022
* New analytics added
  * [CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0](/analytics/CAR-2021-11-001)

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
* Updated [ATT&CK Navigator layer](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) to incorporate sub-technique mappings for all CAR analytics.
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
