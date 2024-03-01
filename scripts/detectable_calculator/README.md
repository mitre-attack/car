# Detectable techniques calculator

This script queries four open-source detection repositories to calculate known and likely detectable MITRE ATT&CK techniques. It's inspired by and attempts to improve CAR's [coverage comparison website](https://car.mitre.org/coverage/). 

Key differences:

- Split per-technique detection results by operating system (Windows and Linux only for now)
- Focuses on detections in "active" library content (a Github term search will match on content like [this deprecated Sigma rule](https://github.com/SigmaHQ/sigma/blob/eb2f82cbc35909a9657aada437a59a70b5610818/deprecated/windows/proc_creation_win_lolbin_rdrleakdiag.yml#L13), and it seems like CAR is including these results)
- Can be run anytime instead of depending on a CAR coverage update (last update as of writing was `December 30, 2022`)
- Outputs a conservative list of "likely detectable" techniques and subtechniques using the conditions above and a configurable threshold (`UNIQUE_DETECTION_THRESHOLD`).

## Usage

Run the code with `python detectable_calculator.py`

## Setup directions

1. Install Python 3 (this code was validated on Python 3.11.5).
2. Install required libraries to permit detection rule parsing: `pip install -r requirements.txt`
3. Optional: In the code, configure the `ROOT_SEARCH_PATH` if you want the detection libraries to be somewhere other than your current working directory
4. Optional: In the code, configure the `UNIQUE_DETECTION_THRESHOLD` (5 by default) if you think more or fewer detections should be required for a technique to be counted as "likely detectable" per-operating-system.
5. Optional: If having trouble with the script's detection repo download, manually download the four detection libraries by unzipping these files in the `ROOT_SEARCH_PATH`:
    - https://github.com/mitre-attack/car/archive/refs/heads/master.zip
    - https://github.com/SigmaHQ/sigma/archive/refs/heads/master.zip
    - https://github.com/splunk/security_content/archive/refs/heads/develop.zip
    - https://github.com/elastic/detection-rules/archive/refs/heads/main.zip
