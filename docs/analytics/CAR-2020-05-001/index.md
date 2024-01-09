---
title: "CAR-2020-05-001: MiniDump of LSASS"
layout: analytic
submission_date: 2020/05/04
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: Cyber National Mission Force (CNMF)
applicable_platforms: Windows
---
<br><br>
This analytic detects the minidump variant of credential dumping where a process opens lsass.exe in order to extract credentials using the Win32 API call [MiniDumpWriteDump](https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump). Tools like [SafetyKatz](https://github.com/GhostPack/SafetyKatz), [SafetyDump](https://github.com/m0rv4i/SafetyDump), and [Outflank-Dumpert](https://github.com/outflanknl/Dumpert) default to this variant and may be detected by this analytic, though keep in mind that not all options for using those tools will result in this specific behavior.

The analytic is based on a [Sigma analytic](https://github.com/NVISO-BE/sigma-public/blob/master/rules/windows/sysmon/sysmon_lsass_memdump.yml) contributed by Samir Bousseaden and written up in a [blog on MENASEC](https://blog.menasec.net/2019/02/threat-hunting-21-procdump-or-taskmgr.html). It looks for a call trace that includes either dbghelp.dll or dbgcore.dll, which export the relevant functions/permissions to perform the dump. It also detects using the Windows Task Manager (taskmgr.exe) to dump lsass, which is described in [CAR-2019-08-001](/analytics/CAR-2019-08-001/). In this iteration of the Sigma analytic, the `GrantedAccess` filter isn't included because it didn't seem to filter out any false positives and introduces the potential for evasion.

This analytic was tested both in a lab and in a production environment with a very low false-positive rate. werfault.exe and tasklist.exe, both standard Windows processes, showed up multiple times as false positives.

NOTE - this analytic has no corresponding pseudocode implementation because the CAR data model doesn't currently support process access events.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)|[NTDS](https://attack.mitre.org/techniques/T1003/003/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-SCA | [System Call Analysis](https://d3fend.mitre.org/technique/d3f:SystemCallAnalysis)| 





### Implementations

#### Lsass Process Access (Splunk, Sysmon native)


This Splunk query looks for process access events where lsass.exe is accessed with a specific call trace that indicates the use of MiniDumpWriteDump.


```
index=__your_sysmon_index__ EventCode=10 TargetImage="C:\\windows\\system32\\lsass.exe" (CallTrace="*dbghelp.dll*" OR CallTrace="*dbgcore.dll*")| table _time host SourceProcessId SourceImage
```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocodes.


```
norm_id=WindowsSysmon event_id=10 image="C:\Windows\system32\lsass.exe" call_trace IN ["*dbghelp.dll*", "*dbgcore.dll*"]
| fields log_ts host source_process_id source_image
```




