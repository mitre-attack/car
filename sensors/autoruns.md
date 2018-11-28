# Autoruns
 - Manufacturer: Microsoft Corporation
 - Version: 13.2
 - Website: https://technet.microsoft.com/en-us/sysinternals/bb963902.aspx

## Description
This utility shows the user what programs are configured to run during system bootup or login, and/or on execution of various built-in Windows applications like Internet Explorer, Explorer and media players. These programs and drivers include ones in your startup folder, Run, RunOnce, and other Registry keys. Autoruns reports Explorer shell extensions, toolbars, browser helper objects, Winlogon notifications, auto-start services, etc.

## Data Model Coverage

### [file](../data_model/file.md)

| | [**company**](../data_model/file.md#company) | [**creation_time**](../data_model/file.md#creation_time) | [**file_name**](../data_model/file.md#file_name) | [**file_path**](../data_model/file.md#file_path) | [**fqdn**](../data_model/file.md#fqdn) | [**hostname**](../data_model/file.md#hostname) | [**image_path**](../data_model/file.md#image_path) | [**md5_hash**](../data_model/file.md#md5_hash) | [**pid**](../data_model/file.md#pid) | [**ppid**](../data_model/file.md#ppid) | [**previous_creation_time**](../data_model/file.md#previous_creation_time) | [**sha1_hash**](../data_model/file.md#previous_creation_time) | [**sha256_hash**](../data_model/file.md#sha256_hash) | [**signer**](../data_model/file.md#signer) | [**user**](../data_model/file.md#user) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**create**](../data_model/file.md#create) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | | | | | | |
| [**delete**](../data_model/file.md#delete) | | | | | | | | | | | | | | | |
| [**modify**](../data_model/file.md#modify) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| [**read**](../data_model/file.md#read) | | | | | | | | | | | | | | | |
| [**timestomp**](../data_model/file.md#timestomp) | | | | | | | | | | | | | | | |
| [**write**](../data_model/file.md#write) | | | | | | | | | | | | | | | |


### [registry](../data_model/registry.md)

| | [**data**](../data_model/registry.md#data) | [**fqdn**](../data_model/registry.md#fqdn) | [**hive**](../data_model/registry.md#hive) | [**hostname**](../data_model/registry.md#hostname) | [**image_path**](../data_model/registry.md#image_path) | [**key**](../data_model/registry.md#key) | [**pid**](../data_model/registry.md#pid) | [**type**](../data_model/registry.md#type) | [**user**](../data_model/registry.md#user) | [**value**](../data_model/registry.md#value) |
|---|---|---|---|---|---|---|---|---|---|---|
| [**add**](../data_model/registry.md#add) | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | :heavy_check_mark: | | :heavy_check_mark: |
| [**edit**](../data_model/registry.md#edit) | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | :heavy_check_mark: | | :heavy_check_mark: |
| [**remove**](../data_model/registry.md#remove) | | | | | | | | | | |


### [service](../service.md)

| | [**command_line**](../service.md#command_line) | [**exe**](../service.md#exe) | [**fqdn**](../service.md#fqdn) | [**hostname**](../service.md#hostname) | [**image_path**](../service.md#image_path) | [**name**](../service.md#name) | [**pid**](../service.md#pid)| [**ppid**](../service.md#ppid) | [**user**](../service.md#user) |
|---|---|---|---|---|---|---|---|---|---|
| [**create**](../service.md#create) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | | |
| [**delete**](../service.md#delete) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | | |
| [**pause**](../service.md#pause) | | | | | | | | | |
| [**start**](../service.md#start) | | | | | | | | | |
| [**stop**](../service.md#stop) | | | | | | | | | |


## Analytic Coverage

 - [CAR-2013-01-002: Autorun Differences](../analytics/CAR-2013-01-002.md)

