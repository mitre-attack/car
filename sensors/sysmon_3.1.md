# Sysmon (3.1)
 - Manufacturer: Microsoft Corporation
 - Version: 3.1
 - Website: https://technet.microsoft.com/en-us/sysinternals/sysmon

## Description
Sysmon is a freely available program from Microsoft that is provided as part of the Windows Sysinternals suite of tools. It collects system information while running in the background and supports storing it in the Windows Event Log.

## Data Model Coverage
### [driver](../data_model/driver.md)

| | [**base_address**](../data_model/driver.md#base_address) | [**fqdn**](../data_model/driver.md#fqdn) | [**hostname**](../data_model/driver.md#hostname) | [**image_path**](../data_model/driver.md#image_path) |[**md5_hash**](../data_model/driver.md#md5_hash) | [**module_name**](../data_model/driver.md#module_name) | [**sha1_hash**](../data_model/driver.md#sha1_hash) | [**sha256_hash**](../data_model/driver.md#sha256_hash) |[**signer**](../data_model/driver.md#signer) |
|---|---|---|---|---|---|---|---|---|---|
| [**load**](../data_model/driver.md#load) | |heavy_check_mark|heavy_check_mark: |heavy_check_mark: |heavy_check_mark|heavy_check_mark|heavy_check_mark|heavy_check_mark| |
| [**unload**](../data_model/driver.md#unload) | | | | | | | | | |




### [file](../data_model/file.md)

| | [**company**](../data_model/file.md#company) | [**creation_time**](../data_model/file.md#creation_time) | [**file_name**](../data_model/file.md#file_name) | [**file_path**](../data_model/file.md#file_path) | [**fqdn**](../data_model/file.md#fqdn) | [**hostname**](../data_model/file.md#hostname) | [**image_path**](../data_model/file.md#image_path) | [**md5_hash**](../data_model/file.md#md5_hash) | [**pid**](../data_model/file.md#pid) | [**ppid**](../data_model/file.md#ppid) | [**previous_creation_time**](../data_model/file.md#previous_creation_time) | [**sha1_hash**](../data_model/file.md#previous_creation_time) | [**sha256_hash**](../data_model/file.md#sha256_hash) | [**signer**](../data_model/file.md#signer) | [**user**](../data_model/file.md#user) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**create**](../data_model/file.md#create) | | | | | | | | | | | | | | | |
| [**delete**](../data_model/file.md#delete) | | | | | | | | | | | | | | | |
| [**modify**](../data_model/file.md#modify) | | | | | | | | | | | | | | | |
| [**read**](../data_model/file.md#read) | | | | | | | | | | | | | | | |
| [**timestomp**](../data_model/file.md#timestomp) | | :heavy_check_mark: | :heavy_check_mark: | | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | :heavy_check_mark: | | | | :heavy_check_mark|
| [**write**](../data_model/file.md#write) | | | | | | | | | | | | | | | |



### [flow](../data_model/flow.md)

| | [**content**](../data_model/flow.md#content) | [**dest_fqdn**](../data_model/flow.md#dest_fqdn) | [**dest_hostname**](../data_model/flow.md#dest_hostname) | [**dest_ip**](../data_model/flow.md#dest_ip) | [**dest_port**](../data_model/flow.md#dest_port) | [**end_time**](../data_model/flow.md#end_time) | [**exe**](../data_model/flow.md#exe) | [**flags**](../data_model/flow.md#flags) | [**fqdn**](../data_model/flow.md#fqdn) | [**hostname**](../data_model/flow.md#hostname) | [**image_path**](../data_model/flow.md#image_path) | [**packet_count**](../data_model/flow.md#packet_count) | [**pid**](../data_model/flow.md#pid) | [**ppid**](../data_model/flow.md#ppid) | [**proto_info**](../data_model/flow.md#proto_info) | [**protocol**](../data_model/flow.md#protocol) | [**src_fqdn**](../data_model/flow.md#src_fqdn) | [**src_hostname**](../data_model/flow.md#src_hostname) | [**src_ip**](../data_model/flow.md#src_ip) | [**src_port**](../data_model/flow.md#src_port) | [**start_time**](../data_model/flow.md#start_time) | [**user**](../data_model/flow.md#user) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**end**](../data_model/flow.md#end) | | | | | | | | | | | | | | | | | | | | | | |
| [**message**](../data_model/flow.md#message) | | | | | | | | | | | | | | | | | | | | | | |
| [**start**](../data_model/flow.md#start) | | | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | | :heavy_check_mark: | | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


### [module](../data_model/module.md)

| | [**base_address**](../data_model/module.md#base_address) | [**fqdn**](../data_model/module.md#fqdn) | [**hostname**](../data_model/module.md#hostname) | [**image_path**](../data_model/module.md#image_path) | [**md5_hash**](../data_model/module.md#md5_hash) | [**module_name**](../data_model/module.md#module_name) | [**module_path**](../data_model/module.md#module_path) | [**pid**](../data_model/module.md#pid) | [**sha1_hash**](../data_model/module.md#sha1_hash) | [**sha256_hash**](../data_model/module.md#sha256_hash) | [**signer**](../data_model/module.md#signer) | [**tid**](../data_model/module.md#tid) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**load**](../data_model/module.md#load) | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | |
| [**unload**](../data_model/module.md#unload) | | | | | | | | | | | | |



### [process](../data_model/process.md)

| |[ **command_line**](../data_model/process.md#command_line) | [**exe**](../data_model/process.md#exe) | [**fqdn**](../data_model/process.md#fqdn) | [**hostname**](../data_model/process.md#hostname) | [**image_path**](../data_model/process.md#image_path) | [**md5_hash**](../data_model/process.md#md5_hash) | [**parent_exe**](../data_model/process.md#parent_exe) | [**parent_image_path**](../data_model/process.md#parent_image_path) | [**pid**](../data_model/process.md#pid) | [**ppid**](../data_model/process.md#ppid) | [**sha1_hash**](../data_model/module.md#sha1_hash) | [**sha256_hash**](../data_model/process.md#sha256_hash) | [**sid**](../data_model/process.md#sid) | [**signer**](../data_model/process.md#signer) | [**user**](../data_model/process.md#user) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**create**](../data_model/process.md#create) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | | :heavy_check_mark: |
| [**terminate**](../data_model/process.md#terminate) | | | :heavy_check_mark: | :heavy_check_mark: | | | | | :heavy_check_mark: | | | | | | :heavy_check_mark: |


### [thread](../data_model/thread.md)

| | [**hostname**](../data_model/thread.md#hostname) | [**src_pid**](../data_model/thread.md#src_pid) | [**src_tid**](../data_model/thread.md#src_tid) | [**stack_base**](../data_model/thread.md#stack_base) | [**stack_limit**](../data_model/thread.md#stack_limit) | [**start_address**](../data_model/thread.md#start_address) | [**start_function**](../data_model/thread.md#start_function) | [**start_module**](../data_model/thread.md#start_module) | [**start_module_name**](../data_model/thread.md#start_module_name) | [**subprocess_tag**](../data_model/thread.md#subprocess_tag) | [**tgt_pid**](../data_model/thread.md#tgt_pid) | [**tgt_tid**](../data_model/thread.md#tgt_tid) | [**user**](../data_model/thread.md#user) | [**user_stack_base**](../data_model/thread.md#user_stack_base) | [**user_stack_limit**](../data_model/thread.md#user_stack_limit) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**create**](../data_model/thread.md#create) | | | | | | | | | | | | | | | |
| [**remote_create**](../data_model/thread.md#remote_create) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | |
| [**suspend**](../data_model/thread.md#suspend) | | | | | | | | | | | | | | | |
| [**terminate**](../data_model/thread.md#terminate) | | | | | | | | | | | | | | | |

## Analytic Coverage

 - [CAR-2013-02-003: Processes Spawning cmd.exe](../analytics/CAR-2013-02-003.md)
 - [CAR-2013-03-001: Reg.exe called from Command Shell](../analytics/CAR-2013-03-001.md)
 - [CAR-2013-04-002: Quick execution of a series of suspicious commands](../analytics/CAR-2013-04-002.md)
 - [CAR-2013-05-002: Suspicious Run Locations](../analytics/CAR-2013-05-002.md)
 - [CAR-2013-05-004: Execution with AT](../analytics/CAR-2013-05-004.md)
 - [CAR-2013-05-009: Running executables with same hash and different names](../analytics/CAR-2013-05-009.md)
 - [CAR-2013-07-001: Suspicious Arguments](../analytics/CAR-2013-07-001.md)
 - [CAR-2013-07-005: Command Line Usage of Archiving Software](../analytics/CAR-2013-07-005.md)
 - [CAR-2013-08-001: Execution with schtasks](../analytics/CAR-2013-08-001.md)
 - [CAR-2013-09-005: Service Outlier Executables](../analytics/CAR-2013-09-005.md)
 - [CAR-2013-10-002: DLL Injection via Load Library](../analytics/CAR-2013-10-002.md)
 - [CAR-2014-03-005: Remotely Launched Executables via Services](../analytics/CAR-2014-03-005.md)
 - [CAR-2014-03-006: RunDLL32.exe monitoring](../analytics/CAR-2014-03-006.md)
 - [CAR-2014-04-003: Powershell Execution](../analytics/CAR-2014-04-003.md)
 - [CAR-2014-05-001: RPC Activity](../analytics/CAR-2014-05-001.md)
 - [CAR-2014-05-002: Services launching Cmd](../analytics/CAR-2014-05-002.md)
 - [CAR-2014-07-001: Service Search Path Interception](../analytics/CAR-2014-07-001.md)
 - [CAR-2014-11-002: Outlier Parents of Cmd](../analytics/CAR-2014-11-002.md)
 - [CAR-2014-11-003: Debuggers for Accessibility Applications](../analytics/CAR-2014-11-003.md)
 - [CAR-2014-11-004: Remote PowerShell Sessions](../analytics/CAR-2014-11-004.md)
 - [CAR-2014-11-006: Windows Remote Management (WinRM)](../analytics/CAR-2014-11-006.md)
 - [CAR-2014-11-008: Command Launched from WinLogon](../analytics/CAR-2014-11-008.md)
 - [CAR-2016-03-001: Host Discovery Commands](../analytics/CAR-2016-03-001.md)
 - [CAR-2016-03-002: Create Remote Process via WMIC](../analytics/CAR-2016-03-002.md)