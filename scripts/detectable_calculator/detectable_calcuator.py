"""Module providing verified technique extraction from open-source detection libraries"""
# pylint: disable=C0206

import os
import re
import json
import tomllib
from datetime import datetime
from urllib.request import urlretrieve
from pathlib import Path
from zipfile import ZipFile
import yaml

def list_files(path, extensions):
    """Function listing filenames in a path with a specific extension."""
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            for extension in extensions:
                if file.endswith(extension):
                    temp_path = Path(root, file)
                    results.append(temp_path)
    return results

def create_or_append(key_name, value, target_dict):
    """Helper function to add or append to a key-based list within a dictionary."""
    if key_name in target_dict:
        target_dict[key_name].append(value)
    else:
        target_dict[key_name] = [value]

def download_library(library_name, repo_url, root_path):
    """Downloads detection libraries from Github if not present on disk."""
    library_path = Path(root_path,library_name)
    library_zip = Path(root_path, f"{library_name}.zip")

    # only download if the folder does not exist at target path
    if os.path.exists(library_path):
        print(f"{library_name} already present, skipping download")
    else:
        urlretrieve(repo_url, library_zip)

        # extract zip
        with ZipFile(library_zip, 'r') as zobject:
            zobject.extractall(root_path)

        # cleanup
        os.remove(library_zip)
        print(f"{library_name} downloaded")

# optional - location where detection libraries will be downloaded
ROOT_SEARCH_PATH = ""
UNIQUE_DETECTION_THRESHOLD = 5
DETECTION_LIBRARIES = {
    "car": {
        "search_path": Path("car-master","analytics"),
        "file_types": [".yaml"],
        "repo_url": "https://github.com/mitre-attack/car/archive/refs/heads/master.zip",
        "repo_name": "car-master"
    },
    "sigma_windows": {
        "search_path": Path("sigma-master","rules","windows"),
        "file_types": [".yml"],
        "repo_url": "https://github.com/SigmaHQ/sigma/archive/refs/heads/master.zip",
        "repo_name": "sigma-master"
    },
    "sigma_linux": {
        "search_path": Path("sigma-master","rules","linux"),
        "file_types": [".yml"],
        "repo_url": "https://github.com/SigmaHQ/sigma/archive/refs/heads/master.zip",
        "repo_name": "sigma-master"
    },
    "splunk": {
        "search_path": Path("security_content-develop","detections","endpoint"),
        "file_types": [".yml"],
        "repo_url": "https://github.com/splunk/security_content/archive/refs/heads/develop.zip",
        "repo_name": "security_content-develop"
    },
    "elastic_windows": {
        "search_path": Path("detection-rules-main","rules","windows"),
        "file_types": [".toml"],
        "repo_url": "https://github.com/elastic/detection-rules/archive/refs/heads/main.zip",
        "repo_name": "detection-rules-main"
    },
    "elastic_linux": {
        "search_path": Path("detection-rules-main","rules","linux"),
        "file_types": [".toml"],
        "repo_url": "https://github.com/elastic/detection-rules/archive/refs/heads/main.zip",
        "repo_name": "detection-rules-main"
    }
}

spl_sourcetype_maps = {
    "xmlwineventlog": "windows",
    "sysmon_linux": "linux",
    "WinEventLog": "windows",
    "xmlwineventlog;WinEventLog": "windows"
}

extracted_techniques = {"windows": {}, "linux": {}}
skipped = {}

if not ROOT_SEARCH_PATH:
    ROOT_SEARCH_PATH = "."

for library in DETECTION_LIBRARIES:
    print(f"--- Parsing {library} ---")
    skipped[library] = {}
    search_path = Path(ROOT_SEARCH_PATH,DETECTION_LIBRARIES[library]["search_path"])

    download_library(DETECTION_LIBRARIES[library]["repo_name"],
                     DETECTION_LIBRARIES[library]["repo_url"], ROOT_SEARCH_PATH)

    for file_path in list_files(search_path, extensions=DETECTION_LIBRARIES[library]["file_types"]):
        file_basename = os.path.basename(file_path)
        temp_results = {"name": file_basename, "source": library}
        PLATFORM = ""
        if library in ["car","sigma_windows","sigma_linux","splunk"]:
            with open(file_path, 'r', encoding="utf-8") as f:
                content = yaml.safe_load(f)
                if library == "car":
                    if "platforms" in content:
                        raw_platform = content["platforms"]
                        for platform_element in raw_platform:
                            if platform_element in ["Windows","Linux"]:
                                PLATFORM = platform_element.lower()
                                if "coverage" in content:
                                    for coverage_item in content["coverage"]:
                                        technique = coverage_item["technique"]
                                        create_or_append(technique, temp_results,
                                                         extracted_techniques[PLATFORM])
                                        if "subtechniques" in coverage_item:
                                            for sub_t in coverage_item["subtechniques"]:
                                                create_or_append(sub_t, temp_results,
                                                                 extracted_techniques[PLATFORM])
                                else:
                                    create_or_append("no coverage in content", file_basename,
                                                     skipped[library])
                    else:
                        create_or_append("no platforms in content", file_basename, skipped[library])
                    if not PLATFORM:
                        create_or_append("platforms present, but no win/linux", file_basename,
                                         skipped[library])
                elif library in ["sigma_windows","sigma_linux"]:
                    PLATFORM = library.split("_")[1]
                    if "tags" in content:
                        MATCH_MADE = False
                        for raw_tag in content["tags"]:
                            match = re.search(r"\.(?P<technique>t\d+(\.\d+)?)$", raw_tag)
                            if match:
                                create_or_append(match.group("technique").upper(),temp_results,
                                                 extracted_techniques[PLATFORM])
                                MATCH_MADE = True
                        if not MATCH_MADE:
                            create_or_append("no techniques found in tags",
                                             file_basename, skipped[library])
                    else:
                        create_or_append("no tags in content", file_basename, skipped[library])
                elif library == "splunk":
                    splunk_tags = []
                    if "tags" in content:
                        if "mitre_attack_id" in content["tags"]:
                            splunk_tags = content["tags"]["mitre_attack_id"]
                        else:
                            create_or_append("no attack ids in tags", file_basename,
                                             skipped[library])
                    else:
                        create_or_append("no tags in content", file_basename, skipped[library])

                    if "tests" in content:
                        for test in content["tests"]:
                            if "attack_data" in test:
                                for attack_data in test["attack_data"]:
                                    if attack_data["sourcetype"] in spl_sourcetype_maps:
                                        splunk_os = spl_sourcetype_maps[attack_data["sourcetype"]]
                                        for splunk_tag in splunk_tags:
                                            create_or_append(splunk_tag.upper(), temp_results,
                                                             extracted_techniques[splunk_os])
                            else:
                                create_or_append("no attack_data in test", file_basename,
                                                 skipped[library])
                    else:
                        create_or_append("no tests in content", file_basename, skipped[library])
        elif library in ["elastic_windows", "elastic_linux"]:
            with open(file_path, 'rb') as toml_f:
                toml_content = tomllib.load(toml_f)
                MATCH_MADE = False
                if "tags" in toml_content["rule"]:
                    for toml_tag in toml_content["rule"]["tags"]:
                        os_match = re.search(r"^OS:\s(?P<platform>.+)$", toml_tag)
                        if os_match:
                            PLATFORM = os_match.group("platform").lower()
                else:
                    create_or_append("no tags in content", file_basename, skipped[library])

                if "threat" in toml_content["rule"]:
                    for threat_item in toml_content["rule"]["threat"]:
                        if "technique" in threat_item:
                            for technique_item in threat_item["technique"]:
                                technique_match = re.search(r"(?P<technique>[Tt]\d+)$",
                                                            technique_item["id"])
                                if technique_match:
                                    create_or_append(technique_match.group("technique"),
                                                     temp_results,extracted_techniques[PLATFORM])
                                    MATCH_MADE = True

                                if "subtechnique" in technique_item:
                                    for toml_subt in technique_item["subtechnique"]:
                                        subt_match = re.search(r"(?P<technique>[Tt]\d+\.\d+)$",
                                                               toml_subt["id"])
                                        if subt_match:
                                            create_or_append(subt_match.group("technique"),
                                                             temp_results,
                                                             extracted_techniques[PLATFORM])
                                            MATCH_MADE = True
                else:
                    create_or_append("no threat in content", file_basename, skipped[library])

            if not PLATFORM:
                create_or_append("no platform (OS:) in tags", file_basename, skipped[library])

            if not MATCH_MADE:
                create_or_append("no techniques matching regex pattern found in threat section",
                                 file_basename, skipped[library])

print("--- Printing results and outputting to disk ---")

filename_time = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
for os in extracted_techniques:
    techniques = list(extracted_techniques[os].keys())
    technique_count = len(techniques)
    detect_techs = {}
    for ex_tech in extracted_techniques[os]:
        rule_count = len(extracted_techniques[os][ex_tech])
        if rule_count >= UNIQUE_DETECTION_THRESHOLD:
            detect_techs[ex_tech] = rule_count
    print(f"{technique_count} techniques found for {os}: {techniques}")
    print(f"{len(detect_techs.keys())} likely detectable techniques found for {os} {detect_techs}")

export_filename_success = f"{filename_time}_parsed-technique-map.json"
with open(export_filename_success, 'w', encoding="utf-8") as job_success:
    json.dump(extracted_techniques, job_success)

for error_library in skipped:
    for error_type in skipped[error_library]:
        error_files = skipped[error_library][error_type]
        error_count = len(error_files)
        print(f"{error_count} errors found for {error_library} - error type {error_type}: {error_files}")

export_filename_skips = f"{filename_time}_skips.json"
with open(export_filename_skips, 'w', encoding="utf-8") as job_skips:
    json.dump(skipped, job_skips)
