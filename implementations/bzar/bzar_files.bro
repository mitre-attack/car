#
# File: bzar_files.bro
# Created: 20180701
# Updated: 20190225
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

module BZAR;

event file_over_new_connection(f:fa_file, c:connection, is_orig:bool)
{
	# Check Option
	if ( !BZAR::file_extract_option ) { return; }

	# Check if SMB Tree Path is an Admin File Share
	if ( f?$source && f$source == "SMB" && c?$smb_state &&
	     BZAR::smb_admin_file_share_test(c$smb_state) &&
	     c$id$resp_h !in BZAR::ignore_resp_h )
	{
		# Check if SMB Write to an Admin File Share
		if ( c$smb_state?$current_file &&
		     c$smb_state$current_file?$action &&
		     c$smb_state$current_file$action == SMB::FILE_WRITE )
		{
			local smb_name = BZAR::smb_full_path_and_file_name(c$smb_state);
			local fname = fmt("%s_%s%s", c$uid, f$id, subst_string(smb_name, "\\", "_"));

			Files::add_analyzer(f, Files::ANALYZER_EXTRACT, Files::AnalyzerArgs($extract_filename=fname));
			Files::add_analyzer(f, Files::ANALYZER_MD5);
			Files::add_analyzer(f, Files::ANALYZER_SHA1);
			Files::add_analyzer(f, Files::ANALYZER_SHA256);
		}
	}
}


event file_state_remove(f:fa_file)
{
	# Check Option
	if ( !BZAR::file_extract_option ) { return; }

	local fname = "";

	if ( f?$source && f$source == "SMB" && f?$conns && f$info?$extracted )
	{
		fname = f$info$extracted;

		for ( x in f$conns )
		{
			local c = f$conns[x];

			# Check if SMB Tree Path is an Admin File Share
			if ( c?$smb_state && BZAR::smb_admin_file_share_test(c$smb_state) &&
			     c$id$resp_h !in BZAR::ignore_resp_h )
			{
				# Raise Notice
				NOTICE([$note=ATTACK::Lateral_Movement_Extracted_File,
					$msg="Saved a copy of the file written to SMB admin file share",
					$sub=fname,
					$f=f,
					$conn=c]
				);
			}
		}
	}
}

#end bzar_files.bro
