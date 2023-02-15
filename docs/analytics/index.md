---
title: "Analytics"
permalink: /analytics/
---
<div class="analytics-table"></div> 

## Analytic List (sortable)
<script type="text/javascript" src="/assets/sort-table.js"></script>

<table class="js-sort-table" id="analytics-sort">
    <thead>
        <tr>
            <th style="white-space:nowrap;">ID</th>
            <th style="white-space:nowrap;">Name</th>
            <th style="white-space:nowrap;" class="js-sort-date">Submission Date</th>
            <th style="white-space:nowrap;">ATT&CK Techniques</th>
            <th style="white-space:nowrap;">Implementations</th>
            <th style="white-space:nowrap;">Applicable Platforms</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-01-002/">CAR-2013-01-002</a></td>
                <td>Autorun Differences</td>
                <td style="white-space:nowrap;">January 25 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1543/">Create or Modify System Process</a></li><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td></td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-01-003/">CAR-2013-01-003</a></td>
                <td>SMB Events Monitoring</td>
                <td style="white-space:nowrap;">January 25 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1039/">Data from Network Shared Drive</a></li><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Pseudocode</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-02-003/">CAR-2013-02-003</a></td>
                <td>Processes Spawning cmd.exe</td>
                <td style="white-space:nowrap;">February 05 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-02-008/">CAR-2013-02-008</a></td>
                <td>Simultaneous Logins on a Host</td>
                <td style="white-space:nowrap;">February 18 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1078/">Valid Accounts</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-02-012/">CAR-2013-02-012</a></td>
                <td>User Logged in to Multiple Hosts</td>
                <td style="white-space:nowrap;">February 27 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1078/">Valid Accounts</a></li></ul></td>
                <td></td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-03-001/">CAR-2013-03-001</a></td>
                <td>Reg.exe called from Command Shell</td>
                <td style="white-space:nowrap;">March 28 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1012/">Query Registry</a></li><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Dnif, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-04-002/">CAR-2013-04-002</a></td>
                <td>Quick execution of a series of suspicious commands</td>
                <td style="white-space:nowrap;">April 11 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1087/">Account Discovery</a></li><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode, Sigma</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-05-002/">CAR-2013-05-002</a></td>
                <td>Suspicious Run Locations</td>
                <td style="white-space:nowrap;">May 07 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1036/">Masquerading</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode, Sigma</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-05-003/">CAR-2013-05-003</a></td>
                <td>SMB Write Request</td>
                <td style="white-space:nowrap;">May 13 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1570/">Lateral Tool Transfer</a></li><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-05-004/">CAR-2013-05-004</a></td>
                <td>Execution with AT</td>
                <td style="white-space:nowrap;">May 13 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Dnif, Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-05-005/">CAR-2013-05-005</a></td>
                <td>SMB Copy and Execution</td>
                <td style="white-space:nowrap;">May 13 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li><li><a href="https://attack.mitre.org/techniques/T1078/">Valid Accounts</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-05-009/">CAR-2013-05-009</a></td>
                <td>Running executables with same hash and different names</td>
                <td style="white-space:nowrap;">May 23 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1036/">Masquerading</a></li></ul></td>
                <td>Dnif, Logpoint, Sigma, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-07-001/">CAR-2013-07-001</a></td>
                <td>Suspicious Arguments</td>
                <td style="white-space:nowrap;">July 05 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Dnif, Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-07-002/">CAR-2013-07-002</a></td>
                <td>RDP Connection Detection</td>
                <td style="white-space:nowrap;">July 24 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Pseudocode, Sigma</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-07-005/">CAR-2013-07-005</a></td>
                <td>Command Line Usage of Archiving Software</td>
                <td style="white-space:nowrap;">July 31 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1560/">Archive Collected Data</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-08-001/">CAR-2013-08-001</a></td>
                <td>Execution with schtasks</td>
                <td style="white-space:nowrap;">August 07 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-09-003/">CAR-2013-09-003</a></td>
                <td>SMB Session Setups</td>
                <td style="white-space:nowrap;">September 12 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1187/">Forced Authentication</a></li></ul></td>
                <td>Pseudocode</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-09-005/">CAR-2013-09-005</a></td>
                <td>Service Outlier Executables</td>
                <td style="white-space:nowrap;">September 23 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1543/">Create or Modify System Process</a></li></ul></td>
                <td>Logpoint, Pseudocode, Sigma</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-10-001/">CAR-2013-10-001</a></td>
                <td>User Login Activity Monitoring</td>
                <td style="white-space:nowrap;">October 03 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li><li><a href="https://attack.mitre.org/techniques/T1078/">Valid Accounts</a></li></ul></td>
                <td>Dnif, Pseudocode, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2013-10-002/">CAR-2013-10-002</a></td>
                <td>DLL Injection via Load Library</td>
                <td style="white-space:nowrap;">October 07 2013</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1055/">Process Injection</a></li><li><a href="https://attack.mitre.org/techniques/T1548/">Abuse Elevation Control Mechanism</a></li></ul></td>
                <td>Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-02-001/">CAR-2014-02-001</a></td>
                <td>Service Binary Modifications</td>
                <td style="white-space:nowrap;">February 14 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1543/">Create or Modify System Process</a></li><li><a href="https://attack.mitre.org/techniques/T1574/">Hijack Execution Flow</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-03-001/">CAR-2014-03-001</a></td>
                <td>SMB Write Request - NamedPipes</td>
                <td style="white-space:nowrap;">March 03 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1570/">Lateral Tool Transfer</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-03-005/">CAR-2014-03-005</a></td>
                <td>Remotely Launched Executables via Services</td>
                <td style="white-space:nowrap;">March 18 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1543/">Create or Modify System Process</a></li><li><a href="https://attack.mitre.org/techniques/T1569/">System Services</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-03-006/">CAR-2014-03-006</a></td>
                <td>RunDLL32.exe monitoring</td>
                <td style="white-space:nowrap;">March 28 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1218/">System Binary Proxy Execution</a></li></ul></td>
                <td>Dnif, Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-04-003/">CAR-2014-04-003</a></td>
                <td>Powershell Execution</td>
                <td style="white-space:nowrap;">April 11 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li></ul></td>
                <td>Dnif, Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-05-001/">CAR-2014-05-001</a></td>
                <td>RPC Activity</td>
                <td style="white-space:nowrap;">May 01 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-05-002/">CAR-2014-05-002</a></td>
                <td>Services launching Cmd</td>
                <td style="white-space:nowrap;">May 05 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1543/">Create or Modify System Process</a></li></ul></td>
                <td>Dnif, Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-07-001/">CAR-2014-07-001</a></td>
                <td>Service Search Path Interception</td>
                <td style="white-space:nowrap;">July 17 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1574/">Hijack Execution Flow</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-002/">CAR-2014-11-002</a></td>
                <td>Outlier Parents of Cmd</td>
                <td style="white-space:nowrap;">November 06 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-003/">CAR-2014-11-003</a></td>
                <td>Debuggers for Accessibility Applications</td>
                <td style="white-space:nowrap;">November 21 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-004/">CAR-2014-11-004</a></td>
                <td>Remote PowerShell Sessions</td>
                <td style="white-space:nowrap;">November 19 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-005/">CAR-2014-11-005</a></td>
                <td>Remote Registry</td>
                <td style="white-space:nowrap;">November 19 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-006/">CAR-2014-11-006</a></td>
                <td>Windows Remote Management (WinRM)</td>
                <td style="white-space:nowrap;">November 19 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-007/">CAR-2014-11-007</a></td>
                <td>Remote Windows Management Instrumentation (WMI) over RPC</td>
                <td style="white-space:nowrap;">November 19 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1047/">Windows Management Instrumentation</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-11-008/">CAR-2014-11-008</a></td>
                <td>Command Launched from WinLogon</td>
                <td style="white-space:nowrap;">November 19 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2014-12-001/">CAR-2014-12-001</a></td>
                <td>Remotely Launched Executables via WMI</td>
                <td style="white-space:nowrap;">December 02 2014</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1047/">Windows Management Instrumentation</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2015-04-001/">CAR-2015-04-001</a></td>
                <td>Remotely Scheduled Tasks via AT</td>
                <td style="white-space:nowrap;">April 29 2015</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2015-04-002/">CAR-2015-04-002</a></td>
                <td>Remotely Scheduled Tasks via Schtasks</td>
                <td style="white-space:nowrap;">April 29 2015</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2015-07-001/">CAR-2015-07-001</a></td>
                <td>All Logins Since Last Boot</td>
                <td style="white-space:nowrap;">July 17 2015</td>
                <td></td>
                <td>Pseudocode</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-03-001/">CAR-2016-03-001</a></td>
                <td>Host Discovery Commands</td>
                <td style="white-space:nowrap;">March 24 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1087/">Account Discovery</a></li><li><a href="https://attack.mitre.org/techniques/T1069/">Permission Groups Discovery</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-03-002/">CAR-2016-03-002</a></td>
                <td>Create Remote Process via WMIC</td>
                <td style="white-space:nowrap;">March 28 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1047/">Windows Management Instrumentation</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-04-002/">CAR-2016-04-002</a></td>
                <td>User Activity from Clearing Event Logs</td>
                <td style="white-space:nowrap;">April 14 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal</a></li></ul></td>
                <td>Logpoint, Pseudocode, Sigma, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-04-003/">CAR-2016-04-003</a></td>
                <td>User Activity from Stopping Windows Defensive Services</td>
                <td style="white-space:nowrap;">April 15 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1562/">Impair Defenses</a></li></ul></td>
                <td>Logpoint, Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-04-004/">CAR-2016-04-004</a></td>
                <td>Successful Local Account Login</td>
                <td style="white-space:nowrap;">April 18 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1550/">Use Alternate Authentication Material</a></li></ul></td>
                <td>Pseudocode</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2016-04-005/">CAR-2016-04-005</a></td>
                <td>Remote Desktop Logon</td>
                <td style="white-space:nowrap;">April 19 2016</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1021/">Remote Services</a></li></ul></td>
                <td>Logpoint, Pseudocode, Sigma</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-04-001/">CAR-2019-04-001</a></td>
                <td>UAC Bypass</td>
                <td style="white-space:nowrap;">April 19 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1548/">Abuse Elevation Control Mechanism</a></li></ul></td>
                <td>Logpoint, Pseudocode, Sigma, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-04-002/">CAR-2019-04-002</a></td>
                <td>Generic Regsvr32</td>
                <td style="white-space:nowrap;">April 24 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1218/">System Binary Proxy Execution</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-04-003/">CAR-2019-04-003</a></td>
                <td>Squiblydoo</td>
                <td style="white-space:nowrap;">April 24 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1218/">System Binary Proxy Execution</a></li></ul></td>
                <td>Eql, Logpoint, Psuedocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-04-004/">CAR-2019-04-004</a></td>
                <td>Credential Dumping via Mimikatz</td>
                <td style="white-space:nowrap;">April 29 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Logpoint, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-07-001/">CAR-2019-07-001</a></td>
                <td>Access Permission Modification</td>
                <td style="white-space:nowrap;">July 08 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1222/">File and Directory Permissions Modification</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows, Linux, macOS</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-07-002/">CAR-2019-07-002</a></td>
                <td>Lsass Process Dump via Procdump</td>
                <td style="white-space:nowrap;">July 29 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Sigma, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-08-001/">CAR-2019-08-001</a></td>
                <td>Credential Dumping via Windows Task Manager</td>
                <td style="white-space:nowrap;">August 05 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2019-08-002/">CAR-2019-08-002</a></td>
                <td>Active Directory Dumping via NTDSUtil</td>
                <td style="white-space:nowrap;">August 13 2019</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Eql, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-04-001/">CAR-2020-04-001</a></td>
                <td>Shadow Copy Deletion</td>
                <td style="white-space:nowrap;">April 10 2020</td>
                <td></td>
                <td></td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-05-001/">CAR-2020-05-001</a></td>
                <td>MiniDump of LSASS</td>
                <td style="white-space:nowrap;">May 04 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Logpoint, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-05-003/">CAR-2020-05-003</a></td>
                <td>Rare LolBAS Command Lines</td>
                <td style="white-space:nowrap;">May 04 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1012/">Query Registry</a></li><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-08-001/">CAR-2020-08-001</a></td>
                <td>NTFS Alternate Data Stream Execution - System Utilities</td>
                <td style="white-space:nowrap;">August 03 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1564/">Hide Artifacts</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-08-002/">CAR-2020-08-002</a></td>
                <td>NTFS Alternate Data Stream Execution - LOLBAS</td>
                <td style="white-space:nowrap;">August 03 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1564/">Hide Artifacts</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-09-001/">CAR-2020-09-001</a></td>
                <td>Scheduled Task - FileAccess</td>
                <td style="white-space:nowrap;">September 10 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-09-002/">CAR-2020-09-002</a></td>
                <td>Component Object Model Hijacking</td>
                <td style="white-space:nowrap;">September 10 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-09-003/">CAR-2020-09-003</a></td>
                <td>Indicator Blocking - Driver Unloaded</td>
                <td style="white-space:nowrap;">September 10 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1562/">Impair Defenses</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-09-004/">CAR-2020-09-004</a></td>
                <td>Credentials in Files & Registry</td>
                <td style="white-space:nowrap;">September 10 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1552/">Unsecured Credentials</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-09-005/">CAR-2020-09-005</a></td>
                <td>AppInit DLLs</td>
                <td style="white-space:nowrap;">September 10 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-001/">CAR-2020-11-001</a></td>
                <td>Boot or Logon Initialization Scripts</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1037/">Boot or Logon Initialization Scripts</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-002/">CAR-2020-11-002</a></td>
                <td>Local Network Sniffing</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1040/">Network Sniffing</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-003/">CAR-2020-11-003</a></td>
                <td>DLL Injection with Mavinject</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1055/">Process Injection</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-004/">CAR-2020-11-004</a></td>
                <td>Processes Started From Irregular Parent</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1055/">Process Injection</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-005/">CAR-2020-11-005</a></td>
                <td>Clear Powershell Console Command History</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-006/">CAR-2020-11-006</a></td>
                <td>Local Permission Group Discovery</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1069/">Permission Groups Discovery</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-007/">CAR-2020-11-007</a></td>
                <td>Network Share Connection Removal</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-008/">CAR-2020-11-008</a></td>
                <td>MSBuild and msxsl</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1127/">Trusted Developer Utilities Proxy Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-009/">CAR-2020-11-009</a></td>
                <td>Compiled HTML Access</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1218/">System Binary Proxy Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-010/">CAR-2020-11-010</a></td>
                <td>CMSTP</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1218/">System Binary Proxy Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2020-11-011/">CAR-2020-11-011</a></td>
                <td>Registry Edit from Screensaver</td>
                <td style="white-space:nowrap;">November 30 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1546/">Event Triggered Execution</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-001/">CAR-2021-01-001</a></td>
                <td>Identifying Port Scanning Activity</td>
                <td style="white-space:nowrap;">October 23 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1046/">Network Service Discovery</a></li></ul></td>
                <td>Splunk</td>
                <td>Windows, Linux</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-002/">CAR-2021-01-002</a></td>
                <td>Unusually Long Command Line Strings</td>
                <td style="white-space:nowrap;">November 27 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1059/">Command and Scripting Interpreter</a></li></ul></td>
                <td>Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-003/">CAR-2021-01-003</a></td>
                <td>Clearing Windows Logs with Wevtutil</td>
                <td style="white-space:nowrap;">December 02 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1070/">Indicator Removal</a></li></ul></td>
                <td>Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-004/">CAR-2021-01-004</a></td>
                <td>Unusual Child Process for Spoolsv.Exe or Connhost.Exe</td>
                <td style="white-space:nowrap;">December 03 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1068/">Exploitation for Privilege Escalation</a></li></ul></td>
                <td>Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-006/">CAR-2021-01-006</a></td>
                <td>Unusual Child Process spawned using DDE exploit</td>
                <td style="white-space:nowrap;">December 03 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1559/">Inter-Process Communication</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-007/">CAR-2021-01-007</a></td>
                <td>Detecting Tampering of Windows Defender Command Prompt</td>
                <td style="white-space:nowrap;">December 11 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1562/">Impair Defenses</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-008/">CAR-2021-01-008</a></td>
                <td>Disable UAC</td>
                <td style="white-space:nowrap;">December 11 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1548/">Abuse Elevation Control Mechanism</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-01-009/">CAR-2021-01-009</a></td>
                <td>Detecting Shadow Copy Deletion or Resize</td>
                <td style="white-space:nowrap;">December 11 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1490/">Inhibit System Recovery</a></li></ul></td>
                <td>Elastic, Logpoint, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-02-001/">CAR-2021-02-001</a></td>
                <td>Webshell-Indicative Process Tree</td>
                <td style="white-space:nowrap;">November 29 2020</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1505/">Server Software Component</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-02-002/">CAR-2021-02-002</a></td>
                <td>Get System Elevation</td>
                <td style="white-space:nowrap;">January 15 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1548/">Abuse Elevation Control Mechanism</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-04-001/">CAR-2021-04-001</a></td>
                <td>Common Windows Process Masquerading</td>
                <td style="white-space:nowrap;">February 12 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1036/">Masquerading</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-001/">CAR-2021-05-001</a></td>
                <td>Attempt To Add Certificate To Untrusted Store</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1553/">Subvert Trust Controls</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-002/">CAR-2021-05-002</a></td>
                <td>Batch File Write to System32</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1204/">User Execution</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-003/">CAR-2021-05-003</a></td>
                <td>BCDEdit Failure Recovery Modification</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1490/">Inhibit System Recovery</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-004/">CAR-2021-05-004</a></td>
                <td>BITS Job Persistence</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1197/">BITS Jobs</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-005/">CAR-2021-05-005</a></td>
                <td>BITSAdmin Download File</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1197/">BITS Jobs</a></li><li><a href="https://attack.mitre.org/techniques/T1105/">Ingress Tool Transfer</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-006/">CAR-2021-05-006</a></td>
                <td>CertUtil Download With URLCache and Split Arguments</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1105/">Ingress Tool Transfer</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-007/">CAR-2021-05-007</a></td>
                <td>CertUtil Download With VerifyCtl and Split Arguments</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1105/">Ingress Tool Transfer</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-008/">CAR-2021-05-008</a></td>
                <td>Certutil exe certificate extraction</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1606/">Forge Web Credentials</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-009/">CAR-2021-05-009</a></td>
                <td>CertUtil With Decode Argument</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1140/">Deobfuscate/Decode Files or Information</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-010/">CAR-2021-05-010</a></td>
                <td>Create local admin accounts using net exe</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1136/">Create Account</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-011/">CAR-2021-05-011</a></td>
                <td>Create Remote Thread into LSASS</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1003/">OS Credential Dumping</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-05-012/">CAR-2021-05-012</a></td>
                <td>Create Service In Suspicious File Path</td>
                <td style="white-space:nowrap;">May 11 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1569/">System Services</a></li></ul></td>
                <td>Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-11-001/">CAR-2021-11-001</a></td>
                <td>Registry Edit with Creation of SafeDllSearchMode Key Set to 0</td>
                <td style="white-space:nowrap;">November 24 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1574/">Hijack Execution Flow</a></li><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Elastic, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-11-002/">CAR-2021-11-002</a></td>
                <td>Registry Edit with Modification of Userinit, Shell or Notify</td>
                <td style="white-space:nowrap;">November 28 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1547/">Boot or Logon Autostart Execution</a></li><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Elastic, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-12-001/">CAR-2021-12-001</a></td>
                <td>Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths</td>
                <td style="white-space:nowrap;">December 04 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1053/">Scheduled Task/Job</a></li></ul></td>
                <td>Elastic, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2021-12-002/">CAR-2021-12-002</a></td>
                <td>Modification of Default Startup Folder in the Registry Key 'Common Startup'</td>
                <td style="white-space:nowrap;">December 06 2021</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1547/">Boot or Logon Autostart Execution</a></li><li><a href="https://attack.mitre.org/techniques/T1112/">Modify Registry</a></li></ul></td>
                <td>Elastic, Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
            <tr>
                <td style="white-space:nowrap;"><a href="/analytics/CAR-2022-03-001/">CAR-2022-03-001</a></td>
                <td>Disable Windows Event Logging</td>
                <td style="white-space:nowrap;">March 14 2022</td>
                <td><ul><li><a href="https://attack.mitre.org/techniques/T1562/">Impair Defenses</a></li></ul></td>
                <td>Logpoint, Pseudocode, Splunk</td>
                <td>Windows</td>
            </tr>
      </tbody>
</table>