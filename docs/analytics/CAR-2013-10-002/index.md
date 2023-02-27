---
title: "CAR-2013-10-002: DLL Injection via Load Library"
layout: analytic
submission_date: 2013/10/07
information_domain: Host
subtypes: Process DLL
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
Microsoft Windows allows for processes to remotely create threads within other processes of the same privilege level. This functionality is provided via the Windows API [CreateRemoteThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682437.aspx). Both Windows and third-party software use this ability for legitimate purposes. For example, the Windows process [csrss.exe](https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem) creates threads in programs to send signals to registered callback routines. Both adversaries and host-based security software use this functionality to [inject DLLs](https://attack.mitre.org/techniques/T1055), but for very different purposes. An adversary is likely to inject into a program to [evade defenses](https://attack.mitre.org/tactics/TA0005) or [bypass User Account Control](https://attack.mitre.org/techniques/T1548/002), but a security program might do this to gain increased monitoring of API calls. One of the most common methods of [DLL Injection](https://attack.mitre.org/techniques/T1055) is through the Windows API [LoadLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684175.aspx).

-   Allocate memory in the target program with [VirtualAllocEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366890.aspx)
-   Write the name of the DLL to inject into this program with [WriteProcessMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681674.aspx)
-   Create a new thread and set its entry point to [LoadLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684175.aspx) using the API [CreateRemoteThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682437.aspx).

This behavior can be detected by looking for thread creations across processes, and resolving the entry point to determine the function name. If the function is `LoadLibraryA` or `LoadLibraryW`, then the intent of the remote thread is clearly to inject a DLL. When this is the case, the source process must be examined so that it can be ignored when it is both expected and a trusted process.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Process Injection](https://attack.mitre.org/techniques/T1055/)|[Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|
|[Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)|[Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)|[Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SCA | [System Call Analysis](https://d3fend.mitre.org/technique/d3f:SystemCallAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[thread](/data_model/thread) | [remote_create](/data_model/thread#remote_create) | [src_pid](/data_model/thread#src_pid) |
|[thread](/data_model/thread) | [remote_create](/data_model/thread#remote_create) | [start_function](/data_model/thread#start_function) |



### Implementations

#### Pseudocode

Search for remote thread creations that start at LoadLibraryA or LoadLibraryW. Depending on the tool, it may provide additional information about the DLL string that is an argument to the function. If there is any security software that legitimately injects DLLs, it must be carefully whitelisted. 


```
remote_thread = search Thread:RemoteCreate
remote_thread = filter (start_function == "LoadLibraryA" or start_function == "LoadLibraryW")
remote_thread = filter (src_image_path != "C:\Path\To\TrustedProgram.exe")

output remote_thread

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=8 start_function IN ["LoadLibraryA", "LoadLibraryW"] -source_image="C:\Path\To\TrustedProgram.exe"

```





### True Positives

#### Mordor (sysmon)

Sysmon event from the Mordor [Empire DLL Injection dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/defense_evasion/process_injection_T1055/empire_dll_injection.md).


##### [Full Event](/true_positives/CAR-2013-10-002-mordor-01.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-05-18T22:15:33.007Z",
	"@timestamp": "2019-05-18T22:15:33.697Z",
	"@version": "1",
	"action": "createremotethread",
	"event_id": 8,
	"log_ingest_timestamp": "2019-05-18T22:15:33.697Z",
	"log_name": "Microsoft-Windows-Sysmon/Operational",
	"opcode": "Info",
	"process_guid": "03ba39f5-50b2-5ce0-0000-00109995c501",
	"process_id": "5452",
	"process_name": "powershell.exe",
	"process_path": "c:\\\\windows\\\\system32\\\\windowspowershell\\\\v1.0\\\\powershell.exe",
	"process_target_guid": "03ba39f5-8320-5ce0-0000-00101ec72502",
	"process_target_id": "3124",
	"process_target_name": "notepad.exe",
	"process_target_path": "c:\\\\windows\\\\system32\\\\notepad.exe",
	"provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
	"record_number": "2273503",
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "CreateRemoteThread detected (rule: CreateRemoteThread)",
	"thread_id": 3144,
	"thread_new_id": "7940",
	"thread_start_address": "0x00007FFECED8F220",
	"thread_start_function": "LoadLibraryA",
	"thread_start_module": "C:\\\\Windows\\\\System32\\\\KERNEL32.DLL",
	"type": "wineventlog",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User"
}
```

