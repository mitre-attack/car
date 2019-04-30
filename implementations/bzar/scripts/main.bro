#
# File: main.bro
# Created: 20180701
# Updated: 20190403
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

@if ((Version::info$major == 2) && (Version::info$minor <= 5))

# Use this syntax for Bro v2.5.x and below
@load policy/protocols/smb

@else

# Use this syntax for Bro v2.6.x and above
@load base/protocols/smb

@endif

@load base/protocols/dce-rpc
@load base/frameworks/files
@load base/frameworks/notice
@load base/frameworks/sumstats

module BZAR;

export
{
	# NOTICE - Raise Notices for these ATT&CK Tactic Categories
	redef enum Notice::Type +=
	{
		ATTACK::Credential_Access,
		ATTACK::Defense_Evasion,
		ATTACK::Discovery,
		ATTACK::Execution,
		ATTACK::Lateral_Movement,
		ATTACK::Lateral_Movement_and_Execution,
		ATTACK::Lateral_Movement_Extracted_File,
		ATTACK::Persistence,
	};

	#
	# BZAR Analytics - Use SumStats to correlate ATT&CK Techniques
	#

	# 1- SumStats Analytics for ATT&CK Lateral Movement and Execution
	const bzar1_epoch = 10min &redef;
	const bzar1_limit = 1001.0 &redef; # SMB_WRITE == 1; RPC_EXEC == 1000;

	# 2- SumStats Analytics for ATTACK Lateral Movement (Multiple Attempts)
	# Use threshold vector for greater fidelity and to assist in tuning the
	# threshold for each unique environment.
	const bzar2_epoch = 5min &redef;
	const bzar2_limit = vector(5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 100.0) &redef;

	# 3- SumStats Analytics for ATTACK Discovery
	# Use threshold vector for greater fidelity and to assist in tuning the
	# threshold for each unique environment.
	const bzar3_epoch = 5min &redef;
	const bzar3_limit = vector(5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 100.0) &redef;

	# Ignore Activity from these Originating IP Addresses
	const ignore_orig_h : set[addr] = {127.0.0.1,} &redef;

	# Ignore Activity to these Responding IP Addresses
	const ignore_resp_h : set[addr] = {127.0.0.1,} &redef;

	# Enable/Disable File Extraction
	const file_extract_option = T &redef; 
}
#end export


event bro_init()
{
	# 1- SumStats Analytics for ATT&CK Lateral Movement and Execution
	#
	# Description:
	#    Use SumStats to raise a Bro/Zeek Notice event if an SMB Lateral Movement 
	#    indicator (e.g., SMB File Write to a Windows Admin File Share: ADMIN$ or 
	#    C$ only) is observed together with a DCE-RPC Execution indicator against 
	#    the same (targeted) host, within a specified period of time.
	#
	# Relevant ATT&CK Technique(s):
	#    T1077 Windows Admin Shares (file shares only, not named pipes) &&
	#    T1105 Remote File Copy && (T1035 Service Execution || T1047 WMI || T1053 Scheduled Task)
	#
	# Relevant Indicator(s) Detected by Bro/Zeek:
	#    (a) smb1_write_andx_response::c$smb_state$path contains ADMIN$ or C$
	#    (b) smb2_write_request::c$smb_state$path contains ADMIN$ or C$ *
	#    (c) dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation contains 
	#        any of the following: (see BZAR::rpc_execution set).
	# 
	# NOTE: Preference would be to detect 'smb2_write_response' 
	#       event (instead of 'smb2_write_request'), because it 
	#       would confirm the file was actually written to the 
	#       remote destination.  Unfortuantely, Bro/Zeek does 
	#       not have an event for that SMB message-type yet.
	#
	# Globals (defined in main.bro above):
	#    bzar1_epoch
	#    bzar1_limit

	local bzar1 = SumStats::Reducer(
		$stream="attack_lm_ex",
		$apply=set(SumStats::SUM, SumStats::MAX, SumStats::MIN)
	);

	SumStats::create([
		$name = "attack_lm_ex_notice",
		$reducers  = set(bzar1),
		$epoch     = bzar1_epoch,
		$threshold = bzar1_limit,
		$threshold_val (key:SumStats::Key, result:SumStats::Result) =
		{
			return result["attack_lm_ex"]$sum;
		},
		$threshold_crossed(key:SumStats::Key, result:SumStats::Result) = 
		{
			local r = result["attack_lm_ex"];

			# Ensure at least one RPC_EXEC was observed and
			# at least one SMB_WRITE was observed

			if ( r$max == 1000 && r$min == 1 )
			{ 
				local s = fmt("Detected activity against host %s, total score %.0f within timeframe %s", key$host, r$sum, bzar1_epoch);

				# Raise Notice
				NOTICE([$note=ATTACK::Lateral_Movement_and_Execution,
					$msg=s]
				);
			}
		}
	]);


	# 2- SumStats Analytics for ATTACK Lateral Movement (Multiple Attempts)
	#
	# Description:
	#    Use SumStats to raise a Bro/Zeek Notice event if multiple SMB Lateral 
	#    Movement indicators (e.g., multiple attempts to connect to a Windows Admin
	#    File Share: ADMIN$ or C$ only) are observed originating from the same host, 
	#    regardless of write-attempts and regardless of whether or not any connection
	#    is successful --just connection attempts-- within a specified period of time.
	#
	# Relevant ATT&CK Technique(s):
	#    T1077 Windows Admin Shares (file shares only, not named pipes)
	#
	# Relevant Indicator(s) Detected by Bro/Zeek:
	#    (a) smb1_tree_connect_andx_request::c$smb_state$path contains ADMIN$ or C$
	#    (b) smb2_tree_connect_request::c$smb_state$path contains ADMIN$ or C$
	#
	# Globals (defined in main.bro above):
	#    bzar2_epoch
	#    bzar2_limit

	local bzar2 = SumStats::Reducer(
		$stream="attack_t1077",
		$apply=set(SumStats::SUM)
	);

	SumStats::create([
		$name = "attack_t1077_notice",
		$reducers  = set(bzar2),
		$epoch     = bzar2_epoch,
		$threshold_series = bzar2_limit,
		$threshold_val (key:SumStats::Key, result:SumStats::Result) =
		{
			return result["attack_t1077"]$sum;
		},
		$threshold_crossed(key:SumStats::Key, result:SumStats::Result) = 
		{
			local s = fmt("Detected T1077 Admin File Share activity from host %s, total attempts %.0f within timeframe %s", key$host, result["attack_t1077"]$sum, bzar2_epoch);

			# Raise Notice
			NOTICE([$note=ATTACK::Lateral_Movement,
				$msg=s]
			);
		}
	]);


	# 3- SumStats Analytics for ATTACK Discovery
	#
	# Description:
	#    Use SumStats to raise a Bro/Zeek Notice event if multiple instances of 
	#    DCE-RPC Discovery indicators are observed originating from the same host, 
	#    within a specified period of time.
	#
	# Relevant ATT&CK Technique(s):
	#    T1016 System Network Configuration Discovery
	#    T1018 Remote System Discovery 
	#    T1033 System Owner/User Discovery 
	#    T1069 Permission Groups Discovery 
	#    T1082 System Information Discovery
	#    T1083 File & Directory Discovery
	#    T1087 Account Discovery
	#    T1124 System Time Discovery
	#    T1135 Network Share Discovery
	#
	# Relevant Indicator(s) Detected by Bro/Zeek:
	#    (a) dce_rpc_response::c$dce_rpc$endpoint + c$dce_rpc$operation contains 
	#        any of the following: (see BZAR::rpc_dicsovery set).
	# 
	# Globals (defined in main.bro above):
	#    bzar3_epoch
	#    bzar3_limit

	local bzar3 = SumStats::Reducer(
		$stream="attack_discovery",
		$apply=set(SumStats::SUM)
	);

	SumStats::create([
		$name = "attack_discovery_notice",
		$reducers  = set(bzar3),
		$epoch     = bzar3_epoch,
		$threshold_series = bzar3_limit,
		$threshold_val (key:SumStats::Key, result:SumStats::Result) =
		{
			return result["attack_discovery"]$sum;
		},
		$threshold_crossed(key:SumStats::Key, result:SumStats::Result) = 
		{
			local s = fmt("Detected activity from host %s, total attempts %.0f within timeframe %s", key$host, result["attack_discovery"]$sum, bzar3_epoch);

			# Raise Notice
			NOTICE([$note=ATTACK::Discovery,
				$msg=s]
			);
		}
	]);
}

#end main.bro
