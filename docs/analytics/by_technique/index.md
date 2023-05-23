---
title: "Analytics (by technique)"
permalink: /analytics/by_technique
---
<div class="tech-analytics-table"></div>

<table>
    <thead>
        <tr>
            <th style="white-space:nowrap;">ATT&CK Technique</th>
            <th style="white-space:nowrap;">ATT&CK Sub-technique(s)</th>
            <th style="white-space:nowrap;">CAR Analytic(s)</th>
        </tr>
    </thead>
    <tbody>
       <tr>
            <td rowspan="4"><a href="https://attack.mitre.org/techniques/T1003/">T1003: OS Credential Dumping</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1003/001/">T1003.001: LSASS Memory</a></td>
            <td><ul><li><a href="CAR-2013-07-001">CAR-2013-07-001: Suspicious Arguments</a></li><li><a href="CAR-2019-04-004">CAR-2019-04-004: Credential Dumping via Mimikatz</a></li><li><a href="CAR-2019-07-002">CAR-2019-07-002: Lsass Process Dump via Procdump</a></li><li><a href="CAR-2019-08-001">CAR-2019-08-001: Credential Dumping via Windows Task Manager</a></li><li><a href="CAR-2021-05-011">CAR-2021-05-011: Create Remote Thread into LSASS</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1003/003/">T1003.003: NTDS</a></td>
            <td><ul><li><a href="CAR-2019-08-002">CAR-2019-08-002: Active Directory Dumping via NTDSUtil</a></li><li><a href="CAR-2020-05-001">CAR-2020-05-001: MiniDump of LSASS</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1003/002/">T1003.002: Security Account Manager</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1007/">T1007: System Service Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1010/">T1010: Application Window Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1012/">T1012: Query Registry</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-03-001">CAR-2013-03-001: Reg.exe called from Command Shell</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2020-05-003">CAR-2020-05-003: Rare LolBAS Command Lines</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1016/">T1016: System Network Configuration Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1018/">T1018: Remote System Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="5"><a href="https://attack.mitre.org/techniques/T1021/">T1021: Remote Services</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-07-001">CAR-2013-07-001: Suspicious Arguments</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1021/002/">T1021.002: SMB/Windows Admin Shares</a></td>
            <td><ul><li><a href="CAR-2013-01-003">CAR-2013-01-003: SMB Events Monitoring</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2013-05-003">CAR-2013-05-003: SMB Write Request</a></li><li><a href="CAR-2013-05-005">CAR-2013-05-005: SMB Copy and Execution</a></li><li><a href="CAR-2014-05-001">CAR-2014-05-001: RPC Activity</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1021/003/">T1021.003: Distributed Component Object Model</a></td>
            <td><ul><li><a href="CAR-2014-05-001">CAR-2014-05-001: RPC Activity</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1021/006/">T1021.006: Windows Remote Management</a></td>
            <td><ul><li><a href="CAR-2014-05-001">CAR-2014-05-001: RPC Activity</a></li><li><a href="CAR-2014-11-004">CAR-2014-11-004: Remote PowerShell Sessions</a></li><li><a href="CAR-2014-11-006">CAR-2014-11-006: Windows Remote Management (WinRM)</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1021/001/">T1021.001: Remote Desktop Protocol</a></td>
            <td><ul><li><a href="CAR-2013-07-002">CAR-2013-07-002: RDP Connection Detection</a></li><li><a href="CAR-2013-10-001">CAR-2013-10-001: User Login Activity Monitoring</a></li><li><a href="CAR-2016-04-005">CAR-2016-04-005: Remote Desktop Logon</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1029/">T1029: Scheduled Transfer</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1033/">T1033: System Owner/User Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1036/">T1036: Masquerading</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-05-002">CAR-2013-05-002: Suspicious Run Locations</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1036/003/">T1036.003: Rename System Utilities</a></td>
            <td><ul><li><a href="CAR-2013-05-009">CAR-2013-05-009: Running executables with same hash and different names</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1036/005/">T1036.005: Match Legitimate Name or Location</a></td>
            <td><ul><li><a href="CAR-2021-04-001">CAR-2021-04-001: Common Windows Process Masquerading</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1037/">T1037: Boot or Logon Initialization Scripts</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1037/001/">T1037.001: Logon Script (Windows)</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2020-11-001">CAR-2020-11-001: Boot or Logon Initialization Scripts</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1039/">T1039: Data from Network Shared Drive</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-01-003">CAR-2013-01-003: SMB Events Monitoring</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1040/">T1040: Network Sniffing</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2020-11-002">CAR-2020-11-002: Local Network Sniffing</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1046/">T1046: Network Service Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2021-01-001">CAR-2021-01-001: Identifying Port Scanning Activity</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1047/">T1047: Windows Management Instrumentation</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2014-11-007">CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC</a></li><li><a href="CAR-2014-12-001">CAR-2014-12-001: Remotely Launched Executables via WMI</a></li><li><a href="CAR-2016-03-002">CAR-2016-03-002: Create Remote Process via WMIC</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1049/">T1049: System Network Connections Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1053/">T1053: Scheduled Task/Job</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1053/005/">T1053.005: Scheduled Task</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2013-08-001">CAR-2013-08-001: Execution with schtasks</a></li><li><a href="CAR-2015-04-002">CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks</a></li><li><a href="CAR-2020-09-001">CAR-2020-09-001: Scheduled Task - FileAccess</a></li><li><a href="CAR-2021-12-001">CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1053/002/">T1053.002: At</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2013-05-004">CAR-2013-05-004: Execution with AT</a></li><li><a href="CAR-2015-04-001">CAR-2015-04-001: Remotely Scheduled Tasks via AT</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1055/">T1055: Process Injection</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1055/001/">T1055.001: Dynamic-link Library Injection</a></td>
            <td><ul><li><a href="CAR-2013-10-002">CAR-2013-10-002: DLL Injection via Load Library</a></li><li><a href="CAR-2020-11-003">CAR-2020-11-003: DLL Injection with Mavinject</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1055/012/">T1055.012: Process Hollowing</a></td>
            <td><ul><li><a href="CAR-2020-11-004">CAR-2020-11-004: Processes Started From Irregular Parent</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1057/">T1057: Process Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="4"><a href="https://attack.mitre.org/techniques/T1059/">T1059: Command and Scripting Interpreter</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-01-002">CAR-2021-01-002: Unusually Long Command Line Strings</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1059/003/">T1059.003: Windows Command Shell</a></td>
            <td><ul><li><a href="CAR-2013-02-003">CAR-2013-02-003: Processes Spawning cmd.exe</a></li><li><a href="CAR-2014-11-002">CAR-2014-11-002: Outlier Parents of Cmd</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1059/001/">T1059.001: PowerShell</a></td>
            <td><ul><li><a href="CAR-2014-04-003">CAR-2014-04-003: Powershell Execution</a></li><li><a href="CAR-2014-11-004">CAR-2014-11-004: Remote PowerShell Sessions</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1059/005/">T1059.005: Visual Basic</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1068/">T1068: Exploitation for Privilege Escalation</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-01-004">CAR-2021-01-004: Unusual Child Process for Spoolsv.Exe or Connhost.Exe</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1069/">T1069: Permission Groups Discovery</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1069/001/">T1069.001: Local Groups</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li><li><a href="CAR-2020-11-006">CAR-2020-11-006: Local Permission Group Discovery</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1069/002/">T1069.002: Domain Groups</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li><li><a href="CAR-2020-11-006">CAR-2020-11-006: Local Permission Group Discovery</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="4"><a href="https://attack.mitre.org/techniques/T1070/">T1070: Indicator Removal</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1070/001/">T1070.001: Clear Windows Event Logs</a></td>
            <td><ul><li><a href="CAR-2016-04-002">CAR-2016-04-002: User Activity from Clearing Event Logs</a></li><li><a href="CAR-2021-01-003">CAR-2021-01-003: Clearing Windows Logs with Wevtutil</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1070/005/">T1070.005: Network Share Connection Removal</a></td>
            <td><ul><li><a href="CAR-2020-11-007">CAR-2020-11-007: Network Share Connection Removal</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1070/003/">T1070.003: Clear Command History</a></td>
            <td><ul><li><a href="CAR-2020-11-005">CAR-2020-11-005: Clear Powershell Console Command History</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1078/">T1078: Valid Accounts</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1078/002/">T1078.002: Domain Accounts</a></td>
            <td><ul><li><a href="CAR-2013-02-008">CAR-2013-02-008: Simultaneous Logins on a Host</a></li><li><a href="CAR-2013-02-012">CAR-2013-02-012: User Logged in to Multiple Hosts</a></li><li><a href="CAR-2013-05-003">CAR-2013-05-003: SMB Write Request</a></li><li><a href="CAR-2013-05-005">CAR-2013-05-005: SMB Copy and Execution</a></li><li><a href="CAR-2013-10-001">CAR-2013-10-001: User Login Activity Monitoring</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1078/003/">T1078.003: Local Accounts</a></td>
            <td><ul><li><a href="CAR-2013-02-008">CAR-2013-02-008: Simultaneous Logins on a Host</a></li><li><a href="CAR-2013-02-012">CAR-2013-02-012: User Logged in to Multiple Hosts</a></li><li><a href="CAR-2013-05-003">CAR-2013-05-003: SMB Write Request</a></li><li><a href="CAR-2013-05-005">CAR-2013-05-005: SMB Copy and Execution</a></li><li><a href="CAR-2013-10-001">CAR-2013-10-001: User Login Activity Monitoring</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1082/">T1082: System Information Discovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1087/">T1087: Account Discovery</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1087/001/">T1087.001: Local Account</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1087/002/">T1087.002: Domain Account</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-03-001">CAR-2016-03-001: Host Discovery Commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1098/">T1098: Account Manipulation</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1105/">T1105: Ingress Tool Transfer</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-07-001">CAR-2013-07-001: Suspicious Arguments</a></li><li><a href="CAR-2021-05-005">CAR-2021-05-005: BITSAdmin Download File</a></li><li><a href="CAR-2021-05-006">CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments</a></li><li><a href="CAR-2021-05-007">CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1112/">T1112: Modify Registry</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2013-03-001">CAR-2013-03-001: Reg.exe called from Command Shell</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2014-11-005">CAR-2014-11-005: Remote Registry</a></li><li><a href="CAR-2020-05-003">CAR-2020-05-003: Rare LolBAS Command Lines</a></li><li><a href="CAR-2021-11-001">CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0</a></li><li><a href="CAR-2021-11-002">CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify</a></li><li><a href="CAR-2021-12-002">CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1127/">T1127: Trusted Developer Utilities Proxy Execution</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1127/001/">T1127.001: MSBuild</a></td>
            <td><ul><li><a href="CAR-2020-11-008">CAR-2020-11-008: MSBuild and msxsl</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1136/">T1136: Create Account</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1136/001/">T1136.001: Local Account</a></td>
            <td><ul><li><a href="CAR-2021-05-010">CAR-2021-05-010: Create local admin accounts using net exe</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1140/">T1140: Deobfuscate/Decode Files or Information</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-05-009">CAR-2021-05-009: CertUtil With Decode Argument</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1187/">T1187: Forced Authentication</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-09-003">CAR-2013-09-003: SMB Session Setups</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1197/">T1197: BITS Jobs</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-05-004">CAR-2021-05-004: BITS Job Persistence</a></li><li><a href="CAR-2021-05-005">CAR-2021-05-005: BITSAdmin Download File</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1204/">T1204: User Execution</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1204/002/">T1204.002: Malicious File</a></td>
            <td><ul><li><a href="CAR-2021-05-002">CAR-2021-05-002: Batch File Write to System32</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="5"><a href="https://attack.mitre.org/techniques/T1218/">T1218: System Binary Proxy Execution</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1218/010/">T1218.010: Regsvr32</a></td>
            <td><ul><li><a href="CAR-2019-04-002">CAR-2019-04-002: Generic Regsvr32</a></li><li><a href="CAR-2019-04-003">CAR-2019-04-003: Squiblydoo</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1218/003/">T1218.003: CMSTP</a></td>
            <td><ul><li><a href="CAR-2020-11-010">CAR-2020-11-010: CMSTP</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1218/001/">T1218.001: Compiled HTML File</a></td>
            <td><ul><li><a href="CAR-2020-11-009">CAR-2020-11-009: Compiled HTML Access</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1218/011/">T1218.011: Rundll32</a></td>
            <td><ul><li><a href="CAR-2014-03-006">CAR-2014-03-006: RunDLL32.exe monitoring</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1222/">T1222: File and Directory Permissions Modification</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1222/001/">T1222.001: Windows File and Directory Permissions Modification</a></td>
            <td><ul><li><a href="CAR-2019-07-001">CAR-2019-07-001: Access Permission Modification</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1222/002/">T1222.002: Linux and Mac File and Directory Permissions Modification</a></td>
            <td><ul><li><a href="CAR-2019-07-001">CAR-2019-07-001: Access Permission Modification</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1490/">T1490: Inhibit System Recovery</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-01-009">CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize</a></li><li><a href="CAR-2021-05-003">CAR-2021-05-003: BCDEdit Failure Recovery Modification</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1505/">T1505: Server Software Component</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1505/003/">T1505.003: Web Shell</a></td>
            <td><ul><li><a href="CAR-2021-02-001">CAR-2021-02-001: Webshell-Indicative Process Tree</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1518/">T1518: Software Discovery</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1518/001/">T1518.001: Security Software Discovery</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1543/">T1543: Create or Modify System Process</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1543/003/">T1543.003: Windows Service</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2013-09-005">CAR-2013-09-005: Service Outlier Executables</a></li><li><a href="CAR-2014-02-001">CAR-2014-02-001: Service Binary Modifications</a></li><li><a href="CAR-2014-03-005">CAR-2014-03-005: Remotely Launched Executables via Services</a></li><li><a href="CAR-2014-05-002">CAR-2014-05-002: Services launching Cmd</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="7"><a href="https://attack.mitre.org/techniques/T1546/">T1546: Event Triggered Execution</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/008/">T1546.008: Accessibility Features</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2014-11-003">CAR-2014-11-003: Debuggers for Accessibility Applications</a></li><li><a href="CAR-2014-11-008">CAR-2014-11-008: Command Launched from WinLogon</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/002/">T1546.002: Screensaver</a></td>
            <td><ul><li><a href="CAR-2020-11-011">CAR-2020-11-011: Registry Edit from Screensaver</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/010/">T1546.010: AppInit DLLs</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2020-09-005">CAR-2020-09-005: AppInit DLLs</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/001/">T1546.001: Change Default File Association</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/003/">T1546.003: Windows Management Instrumentation Event Subscription</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1546/015/">T1546.015: Component Object Model Hijacking</a></td>
            <td><ul><li><a href="CAR-2020-09-002">CAR-2020-09-002: Component Object Model Hijacking</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="4"><a href="https://attack.mitre.org/techniques/T1547/">T1547: Boot or Logon Autostart Execution</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1547/001/">T1547.001: Registry Run Keys / Startup Folder</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2013-03-001">CAR-2013-03-001: Reg.exe called from Command Shell</a></li><li><a href="CAR-2020-05-003">CAR-2020-05-003: Rare LolBAS Command Lines</a></li><li><a href="CAR-2021-12-002">CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1547/004/">T1547.004: Winlogon Helper DLL</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2021-11-002">CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1547/010/">T1547.010: Port Monitors</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="2"><a href="https://attack.mitre.org/techniques/T1548/">T1548: Abuse Elevation Control Mechanism</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2021-02-002">CAR-2021-02-002: Get System Elevation</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1548/002/">T1548.002: Bypass User Account Control</a></td>
            <td><ul><li><a href="CAR-2013-10-002">CAR-2013-10-002: DLL Injection via Load Library</a></li><li><a href="CAR-2019-04-001">CAR-2019-04-001: UAC Bypass</a></li><li><a href="CAR-2021-01-008">CAR-2021-01-008: Disable UAC</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1550/">T1550: Use Alternate Authentication Material</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1550/002/">T1550.002: Pass the Hash</a></td>
            <td><ul><li><a href="CAR-2016-04-004">CAR-2016-04-004: Successful Local Account Login</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1552/">T1552: Unsecured Credentials</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1552/001/">T1552.001: Credentials In Files</a></td>
            <td><ul><li><a href="CAR-2020-09-004">CAR-2020-09-004: Credentials in Files & Registry</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1552/002/">T1552.002: Credentials in Registry</a></td>
            <td><ul><li><a href="CAR-2020-09-004">CAR-2020-09-004: Credentials in Files & Registry</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1553/">T1553: Subvert Trust Controls</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1553/004/">T1553.004: Install Root Certificate</a></td>
            <td><ul><li><a href="CAR-2021-05-001">CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1559/">T1559: Inter-Process Communication</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1559/002/">T1559.002: Dynamic Data Exchange</a></td>
            <td><ul><li><a href="CAR-2021-01-006">CAR-2021-01-006: Unusual Child Process spawned using DDE exploit</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1560/">T1560: Archive Collected Data</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1560/001/">T1560.001: Archive via Utility</a></td>
            <td><ul><li><a href="CAR-2013-07-005">CAR-2013-07-005: Command Line Usage of Archiving Software</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="4"><a href="https://attack.mitre.org/techniques/T1562/">T1562: Impair Defenses</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1562/006/">T1562.006: Indicator Blocking</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2020-09-003">CAR-2020-09-003: Indicator Blocking - Driver Unloaded</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1562/002/">T1562.002: Disable Windows Event Logging</a></td>
            <td><ul><li><a href="CAR-2022-03-001">CAR-2022-03-001: Disable Windows Event Logging</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1562/001/">T1562.001: Disable or Modify Tools</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2016-04-003">CAR-2016-04-003: User Activity from Stopping Windows Defensive Services</a></li><li><a href="CAR-2021-01-007">CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1564/">T1564: Hide Artifacts</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1564/004/">T1564.004: NTFS File Attributes</a></td>
            <td><ul><li><a href="CAR-2020-08-001">CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities</a></li><li><a href="CAR-2020-08-002">CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="3"><a href="https://attack.mitre.org/techniques/T1569/">T1569: System Services</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1569/002/">T1569.002: Service Execution</a></td>
            <td><ul><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2014-02-001">CAR-2014-02-001: Service Binary Modifications</a></li><li><a href="CAR-2014-03-005">CAR-2014-03-005: Remotely Launched Executables via Services</a></li><li><a href="CAR-2021-05-012">CAR-2021-05-012: Create Service In Suspicious File Path</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1569/001/">T1569.001: Launchctl</a></td>
            <td><ul><li><a href="CAR-2021-05-012">CAR-2021-05-012: Create Service In Suspicious File Path</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="1"><a href="https://attack.mitre.org/techniques/T1570/">T1570: Lateral Tool Transfer</a></td>
            <td>(N/A - technique only)</td>
            <td><ul><li><a href="CAR-2013-05-003">CAR-2013-05-003: SMB Write Request</a></li><li><a href="CAR-2013-05-005">CAR-2013-05-005: SMB Copy and Execution</a></li><li><a href="CAR-2014-03-001">CAR-2014-03-001: SMB Write Request - NamedPipes</a></li></ul></td>
        </tr>
       <tr>
            <td rowspan="7"><a href="https://attack.mitre.org/techniques/T1574/">T1574: Hijack Execution Flow</a></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/010/">T1574.010: Services File Permissions Weakness</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2014-02-001">CAR-2014-02-001: Service Binary Modifications</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/009/">T1574.009: Path Interception by Unquoted Path</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2014-07-001">CAR-2014-07-001: Service Search Path Interception</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/011/">T1574.011: Services Registry Permissions Weakness</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li><li><a href="CAR-2013-03-001">CAR-2013-03-001: Reg.exe called from Command Shell</a></li><li><a href="CAR-2013-04-002">CAR-2013-04-002: Quick execution of a series of suspicious commands</a></li><li><a href="CAR-2020-05-003">CAR-2020-05-003: Rare LolBAS Command Lines</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/007/">T1574.007: Path Interception by PATH Environment Variable</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/008/">T1574.008: Path Interception by Search Order Hijacking</a></td>
            <td><ul><li><a href="CAR-2013-01-002">CAR-2013-01-002: Autorun Differences</a></li></ul></td>
        </tr>
       <tr>
            <td><a href="https://attack.mitre.org/techniques/T1574/001/">T1574.001: DLL Search Order Hijacking</a></td>
            <td><ul><li><a href="CAR-2021-11-001">CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0</a></li></ul></td>
        </tr>
       <tr>
            <td ><a href="https://attack.mitre.org/techniques/T1606/">T1606: Forge Web Credentials</a></td>
            <td><a href="https://attack.mitre.org/techniques/T1606/002/">T1606.002: SAML Tokens</a></td>
            <td><ul><li><a href="CAR-2021-05-008">CAR-2021-05-008: Certutil exe certificate extraction</a></li></ul></td>
        </tr>
      </tbody>
</table>