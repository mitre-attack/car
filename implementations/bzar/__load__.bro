#
# File: __load__.bro
# Created: 20180701
# Updated: 20190225
#
# Copyright 2018 The MITRE Corporation.  All Rights Reserved.
# Approved for public release.  Distribution unlimited.  Case number 18-2489.
#

@load ./main.bro
@load ./bzar_dce-rpc_consts.bro
@load ./bzar_dce-rpc.bro
@load ./bzar_smb.bro
@load ./bzar_files.bro

@load-sigs ./dpd.sig

#end __load__.bro
