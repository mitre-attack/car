#
# File: bzar_dce-rpc.bro
# Created: 20180701
# Updated: 20190225
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

module BZAR;

export
{
	# ATT&CK - Credential Access Techniques
	#
	# Windows DCE-RPC functions (endpoint::operation) used for
	# Credential Access on the remote system
	# 
	# Relevant ATT&CK Technique(s):
	#    T1003 Credential Dumping

	const rpc_credential_access : set[string] =
	{
	    # ATT&CK Technique - T1003 Credential Dumping
		["drsuapi::DRSReplicaSync"],
		["drsuapi::DRSGetNCChanges"],
	} &redef;


	# ATT&CK - Defense Evasion Techniques
	#
	# Windows DCE-RPC functions (endpoint::operation) used for
	# Defense Evasion on the remote system
	# 
	# Relevant ATT&CK Technique(s):
	#    T1070 Indicator Removal on Host
	#

	const rpc_defense_evasion : set[string] =
	{
	    # ATT&CK Technique - T1070 Indicator Removal on Host
	    # Clear Event Logs
		["eventlog::ElfrClearELFW"],
		["eventlog::ElfrClearELFA"],
		["IEventService::EvtRpcClearLog"],

	    # ATT&CK Technique - T1070 Indicator Removal on Host
	    # Force System Shutdown or Reboot
		["winreg::BaseInitiateSystemShutdown"],
		["winreg::BaseInitiateSystemShutdownEx"],
		["InitShutdown::BaseInitiateShutdown"],
		["InitShutdown::BaseInitiateShutdownEx"],
		["WindowsShutdown::WsdrInitiateShutdown"],
		["winstation_rpc::RpcWinStationShutdownSystem"],
		["samr::SamrShutdownSamServer"], # MSDN says not used on the wire
	} &redef;


	# ATT&CK - Discovery Techniques
	#
	# Windows DCE-RPC functions (endpoint::operation) used for
	# Discovery of users, hosts, files, shares, networks, time
	#
	# Relevant ATT&CK Technique(s):
	#    T1016 System Network Configuration Discovery
	#    T1018 Remote System Discovery 
	#    T1033 System Owner/User Discovery 
	#    T1049 System Network Connections Discovery
	#    T1069 Permission Groups Discovery 
	#    T1082 System Information Discovery
	#    T1083 File & Directory Discovery
	#    T1087 Account Discovery
	#    T1124 System Time Discovery
	#    T1135 Network Share Discovery

	const rpc_discovery : set[string] =
	{
	    # ATT&CK Technique - T1033 System Owner/User Discovery 
	    # ATT&CK Technique - T1069 Permission Groups Discovery 
	    # ATT&CK Technique - T1087 Account Discovery
		["lsarpc::LsarEnumerateAccounts"],
		["lsarpc::LsarEnumerateAccountRights"],
		["lsarpc::LsarEnumerateAccountsWithUserRight"],
		["lsarpc::LsarEnumeratePrivileges"],
		["lsarpc::LsarEnumeratePrivilegesAccount"],
		["lsarpc::LsarEnumerateTrustedDomainsEx"],

		["lsarpc::LsarGetUserName"],
		["lsarpc::LsarGetSystemAccessAccount"],

		["lsarpc::LsarQueryDomainInformationPolicy"],
		["lsarpc::LsarQueryInfoTrustedDomain"],
		["lsarpc::LsarQueryInformationPolicy"],
		["lsarpc::LsarQueryInformationPolicy2"],
		["lsarpc::LsarQueryTrustedDomainInfo"],
		["lsarpc::LsarQueryTrustedDomainInfoByName"],

		["lsarpc::LsarLookupNames"],
		["lsarpc::LsarLookupNames2"],
		["lsarpc::LsarLookupNames3"],
		["lsarpc::LsarLookupNames4"],
		["lsarpc::LsarLookupSids"],
		["lsarpc::LsarLookupSids2"],
		["lsarpc::LsarLookupSids3"],

		["lsarpc::LsarLookupPrivilegeValue"],
		["lsarpc::LsarLookupPrivilegeName"],
		["lsarpc::LsarLookupPrivilegeDisplayName"],

		["samr::SamrLookupNamesInDomain"],
		["samr::SamrLookupIdsInDomain"],
		["samr::SamrLookupDomainInSamServer"],

		["samr::SamrGetGroupsForUser"],
		["samr::SamrGetAliasMembership"],
		["samr::SamrGetMembersInAlias"],
		["samr::SamrGetMembersInGroup"],
		["samr::SamrGetUserDomainPasswordInformation"],

		["samr::SamrEnumerateAliasesInDomain"],
		["samr::SamrEnumerateUsersInDomain"],
		["samr::SamrEnumerateGroupsInDomain"],
		["samr::SamrEnumerateDomainsInSamServer"],

		["samr::SamrQueryInformationAlias"],
		["samr::SamrQueryInformationDomain"],
		["samr::SamrQueryInformationDomain2"],
		["samr::SamrQueryInformationGroup"],
		["samr::SamrQueryInformationUser"],
		["samr::SamrQueryInformationUser2"],

		["samr::SamrQueryDisplayInformation"],
		["samr::SamrQueryDisplayInformation2"],
		["samr::SamrQueryDisplayInformation3"],

		["wkssvc::NetrWkstaUserEnum"],

	    # ATT&CK Technique - T1016 System Network Configuration Discovery
	    # ATT&CK Technique - T1018 Remote System Discovery 
		["srvsvc::NetrServerTransportEnum"],
		["wkssvc::NetrWkstaTransportEnum"],

	    # ATT&CK Technique - T1049 System Network Connections Discovery
	    # ATT&CK Technique - T1018 Remote System Discovery 
		["srvsvc::NetrConnectionEnum"],
		["srvsvc::NetrSessionEnum"],

	    # ATT&CK Technique - T1083 File & Directory Discovery
		["srvsvc::NetrFileEnum"],

	    # ATT&CK Technique - T1135 Network Share Discovery
		["srvsvc::NetrShareEnum"],
		["srvsvc::NetrShareGetInfo"],

	    # ATT&CK Technique - T1082 System Information Discovery
	    # ATT&CK Technique - T1018 Remote System Discovery 
		["srvsvc::NetrServerGetInfo"],
		["srvsvc::NetrServerAliasEnum"],
		["wkssvc::NetrWkstaGetInfo"],

	    # ATT&CK Technique - T1124 System Time Discovery
		["srvsvc::NetrRemoteTOD"],

	} &redef;


	# ATT&CK - Execution Techniques
	#
	# Windows DCE-RPC functions (endpoint::operation) used for 
	# Execution on the remote system
	# 
	# Relevant ATT&CK Technique(s):
	#    T1035 Service Execution
	#    T1047 Windows Management Instrumentation
	#    T1053 Scheduled Tasks
	#

	const rpc_execution : set[string] = 
	{
	    # ATT&CK Technique - T1035 Service Execution
		["svcctl::CreateServiceW"],
		["svcctl::CreateServiceA"],
		["svcctl::StartServiceW"],
		["svcctl::StartServiceA"],

	    # ATT&CK Technique - T1047 Windows Management Instrumentation
		["IWbemServices::ExecMethod"],
		["IWbemServices::ExecMethodAsync"],

	    # ATT&CK Technique - T1053 Scheduled Tasks
		["atsvc::JobAdd"],
		["ITaskSchedulerService::SchRpcRegisterTask"],
		["ITaskSchedulerService::SchRpcRun"],
		["ITaskSchedulerService::SchRpcEnableTask"],
	} &redef;


	# ATT&CK - Persistence Techniques
	#
	# Windows DCE-RPC functions (endpoint::operation) used for
	# Persistence on the remote system
	# 
	# Relevant ATT&CK Technique(s):
	#    T1004 Winlogon Helper DLL
	#    T1013 Port Monitors
	#

	const rpc_persistence : set[string] = 
	{
	    # ATT&CK Technique - T1004 Winlogon Helper DLL
		["ISecLogon::SeclCreateProcessWithLogonW"],
		["ISecLogon::SeclCreateProcessWithLogonExW"],

	    # ATT&CK Technique - T1013 Port Monitors
		["spoolss::RpcAddMonitor"],		# aka winspool | spoolss
		["spoolss::RpcAddPrintProcessor"],	# aka winspool | spool
		["IRemoteWinspool::RpcAsyncAddMonitor"],
		["IRemoteWinspool::RpcAsyncAddPrintProcessor"],
	} &redef;
}
#end export

event dce_rpc_response(c: connection, fid: count, ctx_id: count, opnum: count, stub_len: count) &priority=3
{
	# priority==3 ... We want to execute before writing to dce_rpc.log
	# because default Bro script deletes 'c$dce_rpc' after writing to log

	local rpc = "";

	if ( c?$dce_rpc && c$dce_rpc?$endpoint && c$dce_rpc?$operation )
	{
		# Get UUID and OpNum, by Name (endpoint::operation)
		rpc = fmt("%s::%s", c$dce_rpc$endpoint, c$dce_rpc$operation);
	}

	if ( rpc in BZAR::rpc_credential_access )
	{
		# Looks like DCE-RPC Credential Access
		# Raise Notice
		NOTICE([$note=ATTACK::Credential_Access,
			$msg=rpc,
			$conn=c]
		);
	}

	if ( rpc in BZAR::rpc_defense_evasion )
	{
		# Looks like DCE-RPC Defense Evasion
		# Raise Notice
		NOTICE([$note=ATTACK::Defense_Evasion,
			$msg=rpc,
			$conn=c]
		);
	}

	if ( rpc in BZAR::rpc_discovery &&
	     c$id$orig_h !in BZAR::ignore_orig_h )
	{
		# Looks like DCE-RPC Discovery
		# Set Observation
		SumStats::observe("attack_discovery",
				  SumStats::Key($host=c$id$orig_h),
				  SumStats::Observation($num=1)
		);
	}

	if ( rpc in BZAR::rpc_execution &&
	     c$id$resp_h !in BZAR::ignore_resp_h )
	{
		# Looks like DCE-RPC Remote Execution
		# Raise Notice
		NOTICE([$note=ATTACK::Execution,
			$msg=rpc,
		#	$sub="", # it would be great if we had the filename
			$conn=c]
		);

		# Set Observation, Score == 1000 for RPC_EXEC
		SumStats::observe("attack_lm_ex",
				  SumStats::Key($host=c$id$resp_h),
				  SumStats::Observation($num=1000)
		);
	}

	if ( rpc in BZAR::rpc_persistence )
	{
		# Looks like DCE-RPC Persistence
		# Raise Notice
		NOTICE([$note=ATTACK::Persistence,
			$msg=rpc,
			$conn=c]
		);
	}
}

#end bzar_dce-rpc.bro
