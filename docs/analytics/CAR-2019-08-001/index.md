---
title: "CAR-2019-08-001: Credential Dumping via Windows Task Manager"
layout: analytic
submission_date: 2019/08/05
information_domain: Host
subtypes: File
analytic_type: TTP
contributors: Tony Lambert/Red Canary
---

The Windows Task Manager may be used to dump the memory space of `lsass.exe` to disk for processing with a credential access tool such as Mimikatz. This is performed by launching Task Manager as a privileged user, selecting `lsass.exe`, and clicking "Create dump file". This saves a dump file to disk with a deterministic name that includes the name of the process being dumped.

This requires filesystem data to determine whether files have been created.


### ATT&CK Detection

|Technique|Tactic|Level of Coverage|
|---|---|---|
|[Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|

### Data Model References

|Object|Action|Field|
|---|---|---|
|[file](/data_model/file) | [create](/data_model/file#create) | [file_name](/data_model/file#file_name) |
|[file](/data_model/file) | [create](/data_model/file#create) | [image_path](/data_model/file#image_path) |


### Implementations

#### Procdump - File Create (Pseudocode)


This base pseudocode looks for file create events where a file with a name similar to lsass.dmp is created by the Windows task manager process.


```
files = search File:Create
lsass_dump = filter files where (
  file_name = "lsass*.dmp"  and
  image_path = "C:\Windows\*\taskmgr.exe")
output lsass_dump
```


#### Procdump - File Create (Splunk, Sysmon native)


A Splunk/Sysmon version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=11 TargetFilename="*lsass*.dmp" Image="C:\\Windows\\*\\taskmgr.exe"
```


#### Procdump - File Create (Eql, EQL native)


An EQL version of the above pseudocode.


```
file where file_name == "lsass*.dmp" and process_name == "taskmgr.exe"
```



### Unit Tests

#### Test Case 1

1. Open Windows Task Manager as Administrator
2. Select lsass.exe
3. Right-click on lsass.exe and select "Create dump file".



### True Positives

#### Mordor (sysmon)

Sysmon event from the Mordor [Interactive Task Manager lsass dump dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/credential_access/credential_dumping_T1003/interactive_taskmngr_lsass_dump.md).


```json
{"_index": "logs-endpoint-winevent-sysmon-2019.10.27",
"_type": "_doc",
"_id": "4d45a9bde6a5ce765a7d9765b13e0446c44dd005",
"_score": 1,
"_source": {
    "process_guid": "a158f72c-2ef4-5db5-0000-00100fb48f00",
    "user_reporter_domain": "NT AUTHORITY",
    "log": {
    "level": "information"
    },
    "beat_version": "7.4.0",
    "user_reporter_type": "User",
    "log_name": "Microsoft-Windows-Sysmon/Operational",
    "ecs": {
    "version": "1.1.0"
    },
    "thread_id": 3760,
    "record_number": 258042,
    "log_ingest_timestamp": "2019-10-27T05:45:39.858Z",
    "@version": "1",
    "@event_date_creation": "2019-10-27T05:45:39.851Z",
    "type": "wineventlog",
    "level": "information",
    "user_reporter_name": "SYSTEM",
    "version": 2,
    "@timestamp": "2019-10-27T05:45:39.858Z",
    "z_logstash_pipeline": [
    "0098",
    "fingerprint-winlogbeats7",
    "winlogbeat_7-field_nest_cleanup",
    "winlogbeat_7-copy_to_originals",
    "1500",
    "1521",
    "1522",
    "1523_1",
    "1524_2",
    "1524_6",
    "1531",
    "1541_1",
    "1544_2",
    "1544_3",
    "1544_7",
    "winevent-hostname-cleanup",
    "winevent-user_reporter_name-is-machine-account",
    "copy-8802-001",
    "copy-8802-002"
    ],
    "opcode": "Info",
    "task": "File created (rule: FileCreate)",
    "agent": {
    "ephemeral_id": "81582c0c-9ac2-4a94-ad39-6e6f4ce9d096",
    "type": "winlogbeat",
    "hostname": "WECServer",
    "id": "72887cd5-18d3-415c-ada9-cfb237f9309f",
    "version": "7.4.0"
    },
    "source_name": "Microsoft-Windows-Sysmon",
    "process_id": "2408",
    "provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
    "event_id": 11,
    "@file_date_creation": "2019-10-27T05:45:39.851Z",
    "action": "filecreate",
    "meta_user_reporter_name_is_machine": "false",
    "process_name": "taskmgr.exe",
    "beat_hostname": "WECServer",
    "event": {
    "created": "2019-10-27T05:45:40.940Z",
    "code": 11,
    "action": "File created (rule: FileCreate)",
    "kind": "event"
    },
    "process_path": "c:\\\\windows\\\\system32\\\\taskmgr.exe",
    "user_reporter_sid": "S-1-5-18",
    "file_name": "c:\\\\users\\\\pgustavo\\\\appdata\\\\local\\\\temp\\\\lsass.dmp",
    "z_original_message": "File created:\\nRuleName: \\nUtcTime: 2019-10-27 05:45:39.851\\nProcessGuid: {a158f72c-2ef4-5db5-0000-00100fb48f00}\\nProcessId: 2408\\nImage: C:\\\\Windows\\\\system32\\\\taskmgr.exe\\nTargetFilename: C:\\\\Users\\\\pgustavo\\\\AppData\\\\Local\\\\Temp\\\\lsass.DMP\\nCreationUtcTime: 2019-10-27 05:45:39.851",
    "winlog": {
    "api": "wineventlog",
    "opcode": "Info",
    "task": "File created (rule: FileCreate)",
    "computer_name": "it001.shire.com",
    "provider_guid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
    "event_id": 11,
    "process": {
        "thread": {
        "id": 3760
        },
        "pid": 3168
    },
    "channel": "Microsoft-Windows-Sysmon/Operational",
    "record_id": 258042,
    "provider_name": "Microsoft-Windows-Sysmon",
    "version": 2
    },
    "user": {},
    "host_name": "it001.shire.com"
},
"fields": {
    "@file_date_creation": [
    "2019-10-27T05:45:39.851Z"
    ],
    "@timestamp": [
    "2019-10-27T05:45:39.858Z"
    ],
    "@event_date_creation": [
    "2019-10-27T05:45:39.851Z"
    ],
    "log_ingest_timestamp": [
    "2019-10-27T05:45:39.858Z"
    ]
    }
}
```

