# BZAR (Bro/Zeek ATT&CK-based Analytics and Reporting)

## Introduction

The BZAR project uses the Bro/Zeek Network Security Monitor to detect ATT&CK-based 
adversarial activity.

[MITRE ATT&CK](https://attack.mitre.org/) is a 
publicly-available, curated knowledge base for cyber adversary behavior, reflecting 
the various phases of the adversary lifecycle and the platforms they are known to 
target. The ATT&CK model includes behaviors of numerous threats groups.

BZAR is a set of Bro/Zeek scripts utilizing the SMB and DCE-RPC protocol analyzers 
and the File Extraction Framework to detect ATT&CK-like activity, raise notices, and 
write to the Notice Log.

## Complex Analytics for Detecting ATT&CK-like Activity

The BZAR analytics use the Bro/Zeek Summary Statistics (SumStats) Framework to 
combine two or more simple indicators in SMB and DCE-RPC traffic to detect 
ATT&CK-like activity with a greater degree of confidence.  Three (3) BZAR 
analytics are described below.

### SumStats Analytics for ATT&CK Lateral Movement and Execution

Use SumStats to raise a Bro/Zeek Notice event if an SMB Lateral Movement 
indicator (e.g., SMB File Write to a Windows Admin File Share: ADMIN$ or 
C$ only) is observed together with a DCE-RPC Execution indicator against 
the same (targeted) host, within a specified period of time.

#### Relevant ATT&CK Techniques
* [T1077 Windows Admin Shares](https://attack.mitre.org/techniques/T1077/) (file shares only, not named pipes)
* [T1105 Remote File Copy](https://attack.mitre.org/techniques/T1105/) and one of
  * [T1035 Service Execution](https://attack.mitre.org/techniques/T1035/)
  * [T1047 Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)
  * [T1053 Scheduled Task](https://attack.mitre.org/techniques/T1053/)

#### Relevant Indicators Detected by Bro/Zeek
* `smb1_write_andx_response::c$smb_state$path` contains `ADMIN$` or `C$`
* `smb2_write_request::c$smb_state$path` contains `ADMIN$` or `C$ *`
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
    * `svcctl::CreateServiceW`
    * `svcctl::CreateServiceA`
    * `svcctl::StartServiceW`
    * `svcctl::StartServiceA`
    * `IWbemServices::ExecMethod`
    * `IWbemServices::ExecMethodAsync`
    * `atsvc::JobAdd`
    * `ITaskSchedulerService::SchRpcRegisterTask`
    * `ITaskSchedulerService::SchRpcRun`
    * `ITaskSchedulerService::SchRpcEnableTask`

**NOTE:** Preference would be to detect smb2_write_response event (instead of smb2_write_request), because it would confirm the file was actually written to the remote destination. Unfortunately, Bro/Zeek does not have an event for that SMB message-type yet.

### SumStats Analytics for ATT&CK Lateral Movement (Multiple Attempts)

Use SumStats to raise a Bro/Zeek Notice event if multiple SMB Lateral 
Movement indicators (e.g., multiple attempts to connect to a Windows Admin
File Share: ADMIN$ or C$ only) are observed originating from the same host, 
regardless of write-attempts and regardless of whether or not any connection
is successful --just connection attempts-- within a specified period of time.

#### Relevant ATT&CK Techniques
* [T1077 Windows Admin Shares](https://attack.mitre.org/techniques/T1077/) (file shares only, not named pipes)

#### Indicators detected by Bro/Zeek
* `smb1_tree_connect_andx_request::c$smb_state$path` contains `ADMIN$` or `C$`
* `smb2_tree_connect_request::c$smb_state$path` contains `ADMIN$` or `C$`

### SumStats Analytics for ATT&CK Discovery

Use SumStats to raise a Bro/Zeek Notice event if multiple instances of 
DCE-RPC Discovery indicators are observed originating from the same host, 
within a specified period of time.

#### Relevant ATT&CK Techniques
* [T1016 System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016/)
* [T1018 Remote System Discovery ](https://attack.mitre.org/techniques/T1018/)
* [T1033 System Owner/User Discovery ](https://attack.mitre.org/techniques/T1033/)
* [T1069 Permission Groups Discovery ](https://attack.mitre.org/techniques/T1069/)
* [T1082 System Information Discovery](https://attack.mitre.org/techniques/T1082/)
* [T1083 File & Directory Discovery](https://attack.mitre.org/techniques/T1083/)
* [T1087 Account Discovery](https://attack.mitre.org/techniques/T1087/)
* [T1124 System Time Discovery](https://attack.mitre.org/techniques/T1124/)
* [T1135 Network Share Discovery](https://attack.mitre.org/techniques/T1135/)

#### Relevant Indicator(s) Detected by Bro/Zeek
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
  * `lsarpc::LsarEnumerateAccounts`
  * `lsarpc::LsarEnumerateAccountRights`
  * `lsarpc::LsarEnumerateAccountsWithUserRight`
  * `lsarpc::LsarEnumeratePrivileges`
  * `lsarpc::LsarEnumeratePrivilegesAccount`
  * `lsarpc::LsarEnumerateTrustedDomainsEx`
  * `lsarpc::LsarGetSystemAccessAccount`
  * `lsarpc::LsarGetUserName`
  * `lsarpc::LsarLookupNames`
  * `lsarpc::LsarLookupNames2`
  * `lsarpc::LsarLookupNames3`
  * `lsarpc::LsarLookupNames4`
  * `lsarpc::LsarLookupPrivilegeDisplayName`
  * `lsarpc::LsarLookupPrivilegeName`
  * `lsarpc::LsarLookupPrivilegeValue`
  * `lsarpc::LsarLookupSids`
  * `lsarpc::LsarLookupSids2`
  * `lsarpc::LsarLookupSids3`
  * `lsarpc::LsarQueryDomainInformationPolicy`
  * `lsarpc::LsarQueryInfoTrustedDomain`
  * `lsarpc::LsarQueryInformationPolicy`
  * `lsarpc::LsarQueryInformationPolicy2`
  * `lsarpc::LsarQueryTrustedDomainInfo`
  * `lsarpc::LsarQueryTrustedDomainInfoByName`
  * `samr::SamrLookupNamesInDomain`
  * `samr::SamrLookupIdsInDomain`
  * `samr::SamrLookupDomainInSamServer`
  * `samr::SamrGetGroupsForUser`
  * `samr::SamrGetAliasMembership`
  * `samr::SamrGetMembersInAlias`
  * `samr::SamrGetMembersInGroup`
  * `samr::SamrGetUserDomainPasswordInformation`
  * `samr::SamrEnumerateAliasesInDomain`
  * `samr::SamrEnumerateUsersInDomain`
  * `samr::SamrEnumerateGroupsInDomain`
  * `samr::SamrEnumerateDomainsInSamServer`
  * `samr::SamrQueryInformationAlias`
  * `samr::SamrQueryInformationDomain`
  * `samr::SamrQueryInformationDomain2`
  * `samr::SamrQueryInformationGroup`
  * `samr::SamrQueryInformationUser`
  * `samr::SamrQueryInformationUser2`
  * `samr::SamrQueryDisplayInformation`
  * `samr::SamrQueryDisplayInformation2`
  * `samr::SamrQueryDisplayInformation3`
  * `srvsvc::NetrConnectionEnum`
  * `srvsvc::NetrFileEnum`
  * `srvsvc::NetrRemoteTOD`
  * `srvsvc::NetrServerAliasEnum`
  * `srvsvc::NetrServerGetInfo`
  * `srvsvc::NetrServerTransportEnum`
  * `srvsvc::NetrSessionEnum`
  * `srvsvc::NetrShareEnum`
  * `srvsvc::NetrShareGetInfo`
  * `wkssvc::NetrWkstaGetInfo`
  * `wkssvc::NetrWkstaTransportEnum`
  * `wkssvc::NetrWkstaUserEnum`


## Simple Indicators for Detecting ATT&CK-like Activity

In addition to the analytics described above, BZAR uses simple indicators 
within SMB and DCE-RPC traffic to detect ATT&CK-like activity, although with 
a lesser degree of confidence than detection via the SumStats analytics. 
The BZAR indicators are grouped into six (6) categories, as described below.

### Indicators for ATT&CK Lateral Movement

Raise a Bro/Zeek Notice event if a single instance of an SMB Lateral 
Movement indicator (e.g., SMB File Write to a Windows Admin File Share: 
ADMIN$ or C$ only) is observed, which indicates ATT&CK-like activity.

#### Relevant ATT&CK Techniques

* [T1077 Windows Admin Shares](https://attack.mitre.org/techniques/T1077/) (file shares only, not named pipes)
* [T1105 Remote File Copy](https://attack.mitre.org/techniques/T1105/)

#### Relevant Indicator(s) Detected by Bro/Zeek

* `smb1_write_andx_response::c$smb_state$path` contains `ADMIN$` or `C$`
* `smb2_write_request::c$smb_state$path` contains `ADMIN$` or `C$ *`

**NOTE:** Preference would be to detect smb2_write_response event (instead of smb2_write_request), because it would confirm the file was actually written to the remote destination. Unfortunately, Bro/Zeek does not have an event for that SMB message-type yet.

### Indicators for File Extraction Framework

Launch the Bro/Zeek File Extraction Framework to save a copy of the file 
associated with ATT&CK-like Lateral Movement onto a remote system.  Raise 
a Bro Notice event for the Lateral Movement Extracted File.

#### Relevant ATT&CK Techniques

* [T1077 Windows Admin Shares](https://attack.mitre.org/techniques/T1077/) (file shares only, not named pipes)
* [T1105 Remote File Copy](https://attack.mitre.org/techniques/T1105/)

#### Relevant Indicator(s) Detected by Bro/Zeek

* `smb1_write_andx_response::c$smb_state$path` contains `ADMIN$` or `C$`
* `smb2_write_request::c$smb_state$path` contains `ADMIN$` or `C$ *`

**NOTE:** Preference would be to detect smb2_write_response event (instead of smb2_write_request), because it would confirm the file was actually written to the remote destination. Unfortunately, Bro/Zeek does not have an event for that SMB message-type yet.

### Indicators for ATT&CK Credential Access

Raise a Bro/Zeek Notice event if a single instance of any of the following 
Windows DCE-RPC functions (endpoint::operation) is observed, which 
indicates ATT&CK-like Credential Access techniques on the remote system. 

#### Relevant ATT&CK Technique(s)
* [T1003 Credential Dumping](https://attack.mitre.org/techniques/T1003/)

#### Relevant Indicator(s) Detected by Bro/Zeek
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
  * `drsuapi::DRSReplicaSync`
  * `drsuapi::DRSGetNCChanges`

### Indicators for ATT&CK Defense Evasion

Raise a Bro/Zeek Notice event if a single instance of any of the following  
Windows DCE-RPC functions (endpoint::operation) is observed, which 
indicates ATT&CK-like Defense Evasion techniques on the remote system.

#### Relevant ATT&CK Techniques
* [T1070 Indicator Removal on Host](https://attack.mitre.org/techniques/T1070/)
   
#### Relevant Indicator(s) Detected by Bro/Zeek
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
    * `eventlog::ElfrClearELFW`
    * `eventlog::ElfrClearELFA`
    * `IEventService::EvtRpcClearLog`
    * `InitShutdown::BaseInitiateShutdown`
    * `InitShutdown::BaseInitiateShutdownEx`
    * `WindowsShutdown::WsdrInitiateShutdown`
    * `winreg::BaseInitiateSystemShutdown`
    * `winreg::BaseInitiateSystemShutdownEx`
    * `winstation_rpc::RpcWinStationShutdownSystem`
    * `samr::SamrShutdownSamServer` # MSDN says not used on the wire

### Indicators for ATT&CK Execution

Raise a Bro/Zeek Notice event if a single instance of any of the following
Windows DCE-RPC functions (endpoint::operation) is observed, which 
indicates ATT&CK-like Execution techniques on the remote system.

#### Relevant ATT&CK Technique(s)
* [T1035 Service Execution](https://attack.mitre.org/techniques/T1035/)
* [T1047 Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)
* [T1053 Scheduled Tasks](https://attack.mitre.org/techniques/T1053/)

#### Relevant Indicator(s) Detected by Bro/Zeek
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
    * `atsvc::JobAdd`
    * `ITaskSchedulerService::SchRpcEnableTask`
    * `ITaskSchedulerService::SchRpcRegisterTask`
    * `ITaskSchedulerService::SchRpcRun`
    * `IWbemServices::ExecMethod`
    * `IWbemServices::ExecMethodAsync`
    * `svcctl::CreateServiceA"   `
    * `svcctl::CreateServiceW`
    * `svcctl::StartServiceA`
    * `svcctl::StartServiceW`

### Indicators for ATT&CK Persistence
Raise a Bro/Zeek Notice event if a single instance of any of the following
Windows DCE-RPC functions (endpoint::operation) is observed, which 
indicates ATT&CK-like Persistence techniques on the remote system.

#### Relevant ATT&CK Technique(s):
* [T1004 Winlogon Helper DLL](https://attack.mitre.org/techniques/T1004/)
* [T1013 Port Monitors](https://attack.mitre.org/techniques/T1013/)

#### Relevant Indicator(s) Detected by Bro/Zeek
* `dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation` contains any of the following:
    * `spoolss::RpcAddMonitor` # a.k.a. winspool | spoolss
    * `spoolss::RpcAddPrintProcessor` # a.k.a. winspool | spoolss
    * `IRemoteWinspool::RpcAsyncAddMonitor`
    * `IRemoteWinspool::RpcAsyncAddPrintProcessor`
    * `ISecLogon::SeclCreateProcessWithLogonW`
    * `ISecLogon::SeclCreateProcessWithLogonExW`


### Additional DCE-RPC Interfaces and Methods

The BZAR project adds 144 more Microsoft DCE-RPC Interface UUIDs
(a.k.a. "endpoints") to the Bro/Zeek DCE_RPC::uuid_endpoint_map.

The BZAR project also adds 1,145 Microsoft DCE-RPC Interface Methods 
(a.k.a. "operations") to the Bro/Zeek DCE_RPC::operations.

## References
1. Microsoft Developer Network (MSDN) Library. MSDN Library > Open Specifications > Protocols > Windows Protocols > Technical Documents. https://msdn.microsoft.com/en-us/library/jj712081.aspx
2. Marchand, "Windows Network Services Internals". 2006. http://index-of.es/Windows/win_net_srv.pdf

## Contributing

Contributions are welcome. This code is licensed under the same terms as the CAR repository. See the [LICENSE](/LICENSE.txt) and Developer Certificate of Origin certification in the [CONTRIBUTING](/CONTRIBUTING.md) file in the root of the repository.

*Copyright 2018 The MITRE Corporation.  All Rights Reserved.  
Approved for public release.  Distribution unlimited.  Case number 18-2489.*
