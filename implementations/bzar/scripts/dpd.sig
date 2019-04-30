#
# File: dpd.sig
# Created: 20180701
# Updated: 20190225
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

signature dpd_smb3 { 
	ip-proto == tcp 
	payload /^....[\xfd]SMB/ 
	enable "smb" 
} 

#end dpd.sig
