#
# File: bzar_smb.bro
# Created: 20180701
# Updated: 20190225
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

module BZAR;

export
{
	# ATT&CK - Lateral Movement Techniques
	#
	# Windows Admin File Shares (eg, ADMIN$ or C$) used for
	# Lateral Movement onto the remote system
	#
	# Relevant ATT&CK Technique(s):
	#    T1077 Windows Admin Shares [File Shares Only]
	#    T1105 Remote File Copy
	#

	const smb_admin_file_shares : set[string] = 
	{
		"admin$",
		"ADMIN$",
		"c$",
		"C$",
	} &redef;


	# Add these details about SMB::FILE_WRITE actions to smb_files.log
	# in case an existing file is overwritten, rather than a new file
	# being created.  These details would show if the existing file is
	# overwritten in its entirety, or just a smaller sub-section is
	# overwritten, which would be an interesting diagnostic to detect.

	redef SMB::logged_file_actions	+= { SMB::FILE_WRITE, } &redef;

	redef record SMB::FileInfo	+= 
	{
		# Keep track of how many bytes written for
		# SMB:FILE_WRITE request and response.
		#
		# This could be an interesting diagnostic for 
		# SMB::FILE_READ too, but not implemented yet.

		data_offset_req	: count &optional &log; # File offset to first byte to write/read
		data_len_req	: count &optional &log; # How many bytes to write/read
		data_len_rsp	: count &optional &log; # How many bytes written/read
	};
}
#end export


#
# Helper Functions
#

function smb_admin_file_share_test ( s : SMB::State ) : bool
{
	local tree_name : string;

	if ( s?$current_file && s$current_file?$path )
	{
		tree_name = s$current_file$path;
	}
	else if ( s$current_cmd?$referenced_file && s$current_cmd$referenced_file?$path )
	{
		tree_name = s$current_cmd$referenced_file$path;
	}
	else if ( s?$current_tree && s$current_tree?$path )
	{
		tree_name = s$current_tree$path;
	}
	else if ( s$current_cmd?$referenced_tree && s$current_cmd$referenced_tree?$path )
	{
		tree_name = s$current_cmd$referenced_tree$path;
	}
	else {
		tree_name = "";
	}	

	local tree_parts = split_string(tree_name, /\\/);

	local a = 0;
	local b = |tree_parts|;

	local match = F;

	while ( a < b )
	{
		if ( tree_parts[a] in BZAR::smb_admin_file_shares)
			match = T;
		++a;
	}

	return match;
}

function smb_full_path_and_file_name ( s : SMB::State ) : string
{
	local file_tree = "";
	local file_name = "";

	if ( s$current_file?$path )
		file_tree = s$current_file$path;

	if ( s$current_file?$name )
		file_name = s$current_file$name;

	return fmt("%s%s", file_tree, file_name);
}


#
# SMB1 Event Handlers
#

event smb1_tree_connect_andx_request(c: connection, hdr: SMB1::Header, path: string, service: string) &priority=3
{
	# Check if SMB Tree Path is an Admin File Share

	if ( BZAR::smb_admin_file_share_test(c$smb_state) &&
	     c$id$orig_h !in BZAR::ignore_orig_h )
	{
		# ATT&CK Technique - T1077 Windows Admin Share (File Shares Only)
		# Set Observation
		SumStats::observe("attack_t1077",
		 	  SumStats::Key($host=c$id$orig_h),
			  SumStats::Observation($num=1)
		);
	}
}

event smb1_nt_create_andx_request(c: connection, hdr: SMB1::Header, file_name: string) &priority=3
{
	# Copied this snippet from Bro default handler:
	# policy/protocols/smb/smb1-main.bro#smb1_write_andx_request.
	# It is important to know the full file path at SMB::FILE_OPEN time,
	# so the smb_files.log is consistent with smb_cmd.log.
	# Let's do this now, during smb1_nt_create_andx_request.

	if ( c$smb_state$current_tree?$path && !c$smb_state$current_file?$path ) 
		c$smb_state$current_file$path = c$smb_state$current_tree$path; 
}


event smb1_write_andx_request(c: connection, hdr: SMB1::Header, file_id: count, offset: count, data_len: count) &priority=3
{ 
	# Keep track of the number of bytes in the Write Request.
	# priority==3 ... We want to execute before writing to smb_files.log

	c$smb_state$current_file$data_offset_req = offset;
	c$smb_state$current_file$data_len_req    = data_len;
}

event smb1_write_andx_response(c: connection, hdr: SMB1::Header, written_bytes: count) &priority=3
{
	# Copied this snippet from Bro default handler:
	# policy/protocols/smb/smb1-main.bro#smb1_write_andx_request.
	# Can't hurt to double-check this.

	if ( c$smb_state$current_tree?$path && !c$smb_state$current_file?$path ) 
		c$smb_state$current_file$path = c$smb_state$current_tree$path; 

	# Keep track of the number of bytes in the Write Response. 
	# priority==3 ... We want to execute before writing to smb_files.log

	c$smb_state$current_file$data_len_rsp = written_bytes;


	# Check if SMB Tree Path is an Admin File Share

	if ( BZAR::smb_admin_file_share_test(c$smb_state) &&
	     c$id$resp_h !in BZAR::ignore_resp_h )
	{
		# ATT&CK Technique - T1105 Remote File Copy  &&
		# ATT&CK Technique - T1077 Windows Admin Share (File Shares Only)

		local fname = BZAR::smb_full_path_and_file_name(c$smb_state);

		# Raise Notice
		NOTICE([$note=ATTACK::Lateral_Movement,
			$msg="SMB::FILE_WRITE to admin file share",
			$sub=fname,
			$conn=c]
		);

		# Set Observation, Score == 1 for SMB::FILE_WRITE
		SumStats::observe("attack_lm_ex",
				  SumStats::Key($host=c$id$resp_h),
				  SumStats::Observation($num=1)
		);
	}
}

event smb1_write_andx_response(c: connection, hdr: SMB1::Header, written_bytes: count) &priority=-5
{
	# Write to smb_files.log
	SMB::write_file_log(c$smb_state);
}


#
# SMB2 Event Handlers
#

event smb2_message(c: connection, hdr: SMB2::Header, is_orig: bool) &priority=3
{
	# Copied this snippet from Bro default handler:
	# policy/protocols/smb/smb1-main.bro#smb1_message.
	# The smb_cmd.log was inconsistent with the .$tree field
	# for SMB1 (populated) and SMB2 (was not populated).

	if ( c$smb_state$current_tree?$path )
		c$smb_state$current_cmd$tree = c$smb_state$current_tree$path; 
}


event smb2_tree_connect_request(c: connection, hdr: SMB2::Header, path: string) &priority=3
{
	# Copied this snippet from Bro default handler:
	# policy/protocols/smb/smb1-main.bro#smb1_tree_connect_andx_request.
	# The smb_cmd.log was inconsistent with certain fields
	# for SMB1 (populated) and SMB2 (was not populated).

	local tmp_tree = SMB::TreeInfo($ts=network_time(), $uid=c$uid, $id=c$id, $path=path); 

	c$smb_state$current_cmd$referenced_tree = tmp_tree; 
	c$smb_state$current_cmd$argument = path;


	# Check if SMB Tree Path is an Admin File Share

	if ( BZAR::smb_admin_file_share_test(c$smb_state) &&
	     c$id$orig_h !in BZAR::ignore_orig_h )
	{
		# ATT&CK Technique - T1077 Windows Admin Share (File Shares Only)
		# Set Observation
		SumStats::observe("attack_t1077",
				  SumStats::Key($host=c$id$orig_h),
				  SumStats::Observation($num=1)
		);
	}
}

event smb2_create_request(c: connection, hdr: SMB2::Header, request: SMB2::CreateRequest) &priority=3
{
	# Copied this snippet from Bro default handler:
	# policy/protocols/smb/smb1-main.bro#smb1_write_andx_request.
	# It is important to know the full file path at SMB::FILE_OPEN time,
	# so the smb_files.log is consistent with smb_cmd.log.
	# Let's do this now, during smb2_create_request.

	if ( c$smb_state$current_tree?$path && !c$smb_state$current_file?$path ) 
		c$smb_state$current_file$path = c$smb_state$current_tree$path; 
}

event smb2_write_request(c: connection, hdr: SMB2::Header, file_id: SMB2::GUID, offset: count, length: count) &priority=3
{ 
	# Keep track of the number of bytes in the Write Response. 
	# priority==3 ... We want to execute before writing to smb_files.log

	c$smb_state$current_file$data_offset_req = offset;
	c$smb_state$current_file$data_len_req    = length;
} 

event smb2_write_request(c: connection, hdr: SMB2::Header, file_id: SMB2::GUID, offset: count, length: count)
{
	# NOTE: Preference would be to detect 'smb2_write_response' 
	#       event (instead of 'smb2_write_request'), because it 
	#       would confirm the file was actually written to the 
	#       remote destination.  Unfortuantely, Bro/Zeek does 
	#       not have an event for that SMB message-type yet.

	# Check if SMB Tree Path is an Admin File Share

	if ( BZAR::smb_admin_file_share_test(c$smb_state) &&
	     c$id$resp_h !in BZAR::ignore_resp_h )
	{
		# ATT&CK Technique - T1105 Remote File Copy  &&
		# ATT&CK Technique - T1077 Windows Admin Share (File Shares Only)

		local fname = BZAR::smb_full_path_and_file_name(c$smb_state);

		# Raise Notice
		NOTICE([$note=ATTACK::Lateral_Movement,
			$msg="SMB::FILE_WRITE to admin file share",
			$sub=fname,
			$conn=c]
		);

		# Set Observation, Score == 1 for SMB::FILE_WRITE
		SumStats::observe("attack_lm_ex",
				  SumStats::Key($host=c$id$resp_h),
				  SumStats::Observation($num=1)
		);
	}
}


# #
# # WARNING: No event generated for SMB2_WRITE_RESPONSE
# #
#event smb2_write_response(c: connection, hdr: SMB2::Header, file_id: SMB2::GUID, written_bytes: count) &priority=3
#{
#	# Keep track of the number of bytes in the Write Response. 
#	# priority==3 ... We want to execute before writing to smb_files.log
#	c$smb_state$current_file$data_len_rsp = written_bytes;
#}

#event smb2_write_response(c: connection, hdr: SMB2::Header, file_id: SMB2::GUID, written_bytes: count) &priority=-5
#{
#	SMB::write_file_log(c$smb_state); 
#}

#end bzar_smb.bro
