---
title: Analytic Coverage Comparison
---

Generated on: September 24, 2021

A cross-walk of CAR, [Sigma](https://github.com/SigmaHQ/sigma), [Elastic Detection](https://github.com/elastic/detection-rules), and [Splunk Security Content](https://github.com/splunk/security_content/tree/develop/detections) rules in terms of their coverage of ATT&CK Techniques and Sub-techniques. Note that some analytics may have coverage for multiple techniques, so there is not necessarily a 1:1 correlation between the number of hits in this table for a technique/sub-technique and the number of analytics in each repository. The below table is current as of the Generated On date at the top of this page.

* \# CAR: the number of CAR analytics that contain coverage for the technique/sub-technique.
* \# Sigma: the number of Sigma rules that contain coverage for the technique/sub-technique.
* \# ES: the number of ES detection rules that contain coverage for the technique/sub-technique.
* \# Splunk: the number of Splunk detections rules that contain coverage for the technique/sub-technique.
* \# Total: the total number of analytics between CAR/Sigma/ES/Splunk that contain coverage for the technique-sub-technique.

This table is sortable, so feel free to click on any column to sort by its values. Clicking on each of the CAR/Sigma/ES/Splunk results will search the corresponding repository for the analytics that contain coverage for the technique/sub-technique. 

This data is also available as:

* A [CSV file](/coverage/analytic_coverage_09_24_2021.csv).
* An [ATT&CK Navigator layer](https://mitre-attack.github.io/attack-navigator/#layerURL=https://raw.githubusercontent.com/mitre-attack/car/master/docs/coverage/analytic_coverage_09_24_2021.json).

<script type="text/javascript" src="/assets/sort-table.js"></script>
<table class="js-sort-table" id="coverage-sort">
        <thead>
        <tr>
            <th style="white-space:nowrap;">Technique ID</th>
            <th>Technique Name</th>
            <th>Sub-technique Name</th>
            <th style="white-space:nowrap;" class="js-sort-number"># CAR</th>
            <th style="white-space:nowrap;" class="js-sort-number"># Sigma</th>
            <th style="white-space:nowrap;" class="js-sort-number"># ES</th>
            <th style="white-space:nowrap;" class="js-sort-number"># Splunk</th>
            <th style="white-space:nowrap;" class="js-sort-number"># Total</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <td>T1001</td>
                <td>Data Obfuscation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1001.001</td>
                <td>Data Obfuscation</td>
                <td>Junk Data</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1001.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1001.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1001.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1001.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1001.002</td>
                <td>Data Obfuscation</td>
                <td>Steganography</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1001.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1001.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1001.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1001.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1001.003</td>
                <td>Data Obfuscation</td>
                <td>Protocol Impersonation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1001.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1001.003">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1001.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1001.003">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1003</td>
                <td>OS Credential Dumping</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003">64</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003">13</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003">14</a></td>
                <td>91</td>
            </tr>
            <tr>
                <td>T1003.001</td>
                <td>OS Credential Dumping</td>
                <td>LSASS Memory</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.001">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.001">44</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.001">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.001">8</a></td>
                <td>58</td>
            </tr>
            <tr>
                <td>T1003.002</td>
                <td>OS Credential Dumping</td>
                <td>Security Account Manager</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.002">23</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.002">8</a></td>
                <td>32</td>
            </tr>
            <tr>
                <td>T1003.003</td>
                <td>OS Credential Dumping</td>
                <td>NTDS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.003">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.003">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.003">7</a></td>
                <td>21</td>
            </tr>
            <tr>
                <td>T1003.004</td>
                <td>OS Credential Dumping</td>
                <td>LSA Secrets</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.004">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.004">0</a></td>
                <td>12</td>
            </tr>
            <tr>
                <td>T1003.005</td>
                <td>OS Credential Dumping</td>
                <td>Cached Domain Credentials</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.005">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.005">0</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1003.006</td>
                <td>OS Credential Dumping</td>
                <td>DCSync</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.006">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.006">0</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1003.007</td>
                <td>OS Credential Dumping</td>
                <td>Proc Filesystem</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.007">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.007">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1003.008</td>
                <td>OS Credential Dumping</td>
                <td>/etc/passwd and /etc/shadow</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1003.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1003.008">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1003.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1003.008">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1005</td>
                <td>Data from Local System</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1005">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1005">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1005">1</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1006</td>
                <td>Direct Volume Access</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1006">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1006">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1006">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1007</td>
                <td>System Service Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1007">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1007">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1007">2</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1008</td>
                <td>Fallback Channels</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1008">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1008">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1010</td>
                <td>Application Window Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1010">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1010">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1010">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1010">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1011</td>
                <td>Exfiltration Over Other Network Medium</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1011">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1011">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1011">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1011">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1011.001</td>
                <td>Exfiltration Over Other Network Medium</td>
                <td>Exfiltration Over Bluetooth</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1011.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1011.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1011.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1011.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1012</td>
                <td>Query Registry</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1012">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1012">11</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1012">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1012">1</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1014</td>
                <td>Rootkit</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1014">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1014">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1014">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1014">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1016</td>
                <td>System Network Configuration Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1016">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1016">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1016">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1016">1</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1018</td>
                <td>Remote System Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1018">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1018">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1018">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1018">15</a></td>
                <td>28</td>
            </tr>
            <tr>
                <td>T1020</td>
                <td>Automated Exfiltration</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1020">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1020">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1020">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1020">2</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1020.001</td>
                <td>Automated Exfiltration</td>
                <td>Traffic Duplication</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1020.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1020.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1020.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1020.001">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1021</td>
                <td>Remote Services</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021">28</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021">2</a></td>
                <td>36</td>
            </tr>
            <tr>
                <td>T1021.001</td>
                <td>Remote Services</td>
                <td>Remote Desktop Protocol</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.001">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.001">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.001">5</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1021.002</td>
                <td>Remote Services</td>
                <td>SMB/Windows Admin Shares</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.002">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.002">29</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.002">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.002">7</a></td>
                <td>46</td>
            </tr>
            <tr>
                <td>T1021.003</td>
                <td>Remote Services</td>
                <td>Distributed Component Object Model</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.003">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.003">0</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1021.004</td>
                <td>Remote Services</td>
                <td>SSH</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1021.005</td>
                <td>Remote Services</td>
                <td>VNC</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1021.006</td>
                <td>Remote Services</td>
                <td>Windows Remote Management</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1021.006">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1021.006">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1021.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1021.006">0</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1025</td>
                <td>Data from Removable Media</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1025">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1025">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1025">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1025">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1026</td>
                <td>Multiband Communication</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1026">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1026">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1026">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1026">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1027</td>
                <td>Obfuscated Files or Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027">62</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027">3</a></td>
                <td>70</td>
            </tr>
            <tr>
                <td>T1027.001</td>
                <td>Obfuscated Files or Information</td>
                <td>Binary Padding</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027.001">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027.001">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1027.002</td>
                <td>Obfuscated Files or Information</td>
                <td>Software Packing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1027.003</td>
                <td>Obfuscated Files or Information</td>
                <td>Steganography</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027.003">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027.003">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1027.004</td>
                <td>Obfuscated Files or Information</td>
                <td>Compile After Delivery</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027.004">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027.004">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1027.005</td>
                <td>Obfuscated Files or Information</td>
                <td>Indicator Removal from Tools</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1027.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1027.005">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1027.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1027.005">2</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1029</td>
                <td>Scheduled Transfer</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1029">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1029">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1029">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1029">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1030</td>
                <td>Data Transfer Size Limits</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1030">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1030">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1030">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1030">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1033</td>
                <td>System Owner/User Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1033">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1033">11</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1033">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1033">7</a></td>
                <td>24</td>
            </tr>
            <tr>
                <td>T1034</td>
                <td>Path Interception</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1034">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1034">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1034">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1034">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1036</td>
                <td>Masquerading</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036">34</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036">12</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036">3</a></td>
                <td>50</td>
            </tr>
            <tr>
                <td>T1036.001</td>
                <td>Masquerading</td>
                <td>Invalid Code Signature</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1036.002</td>
                <td>Masquerading</td>
                <td>Right-to-Left Override</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1036.003</td>
                <td>Masquerading</td>
                <td>Rename System Utilities</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.003">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.003">6</a></td>
                <td>19</td>
            </tr>
            <tr>
                <td>T1036.004</td>
                <td>Masquerading</td>
                <td>Masquerade Task or Service</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.004">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.004">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1036.005</td>
                <td>Masquerading</td>
                <td>Match Legitimate Name or Location</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.005">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.005">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.005">1</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1036.006</td>
                <td>Masquerading</td>
                <td>Space after Filename</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1036.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1036.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1036.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1036.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1037</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1037.001</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>Logon Script (Windows)</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037.001">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037.001">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1037.002</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>Logon Script (Mac)</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1037.003</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>Network Logon Script</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1037.004</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>Rc.common</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1037.005</td>
                <td>Boot or Logon Initialization Scripts</td>
                <td>Startup Items</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1037.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1037.005">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1037.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1037.005">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1039</td>
                <td>Data from Network Shared Drive</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1039">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1039">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1039">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1039">3</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1040</td>
                <td>Network Sniffing</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1040">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1040">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1040">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1040">0</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1041</td>
                <td>Exfiltration Over C2 Channel</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1041">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1041">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1041">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1041">1</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1043</td>
                <td>Commonly Used Port</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1043">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1043">15</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1043">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1043">0</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1046</td>
                <td>Network Service Scanning</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1046">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1046">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1046">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1046">2</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1047</td>
                <td>Windows Management Instrumentation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1047">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1047">33</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1047">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1047">7</a></td>
                <td>48</td>
            </tr>
            <tr>
                <td>T1048</td>
                <td>Exfiltration Over Alternative Protocol</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1048">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1048">17</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1048">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1048">3</a></td>
                <td>26</td>
            </tr>
            <tr>
                <td>T1048.001</td>
                <td>Exfiltration Over Alternative Protocol</td>
                <td>Exfiltration Over Symmetric Encrypted Non-C2 Protocol</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1048.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1048.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1048.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1048.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1048.002</td>
                <td>Exfiltration Over Alternative Protocol</td>
                <td>Exfiltration Over Asymmetric Encrypted Non-C2 Protocol</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1048.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1048.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1048.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1048.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1048.003</td>
                <td>Exfiltration Over Alternative Protocol</td>
                <td>Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1048.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1048.003">11</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1048.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1048.003">5</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1049</td>
                <td>System Network Connections Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1049">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1049">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1049">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1049">5</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1051</td>
                <td>Shared Webroot</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1051">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1051">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1051">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1051">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1052</td>
                <td>Exfiltration Over Physical Medium</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1052">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1052">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1052">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1052">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1052.001</td>
                <td>Exfiltration Over Physical Medium</td>
                <td>Exfiltration over USB</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1052.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1052.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1052.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1052.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1053</td>
                <td>Scheduled Task/Job</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053">24</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053">12</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053">7</a></td>
                <td>43</td>
            </tr>
            <tr>
                <td>T1053.001</td>
                <td>Scheduled Task/Job</td>
                <td>At (Linux)</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1053.002</td>
                <td>Scheduled Task/Job</td>
                <td>At (Windows)</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.002">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.002">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.002">0</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1053.003</td>
                <td>Scheduled Task/Job</td>
                <td>Cron</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.003">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.003">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.003">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1053.004</td>
                <td>Scheduled Task/Job</td>
                <td>Launchd</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1053.005</td>
                <td>Scheduled Task/Job</td>
                <td>Scheduled Task</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.005">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.005">17</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.005">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.005">6</a></td>
                <td>29</td>
            </tr>
            <tr>
                <td>T1053.006</td>
                <td>Scheduled Task/Job</td>
                <td>Systemd Timers</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1053.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1053.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1053.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1053.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055</td>
                <td>Process Injection</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055">21</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055">7</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055">18</a></td>
                <td>46</td>
            </tr>
            <tr>
                <td>T1055.001</td>
                <td>Process Injection</td>
                <td>Dynamic-link Library Injection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.001">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.001">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.001">0</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1055.002</td>
                <td>Process Injection</td>
                <td>Portable Executable Injection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1055.003</td>
                <td>Process Injection</td>
                <td>Thread Execution Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1055.004</td>
                <td>Process Injection</td>
                <td>Asynchronous Procedure Call</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.005</td>
                <td>Process Injection</td>
                <td>Thread Local Storage</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.008</td>
                <td>Process Injection</td>
                <td>Ptrace System Calls</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.008">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.008">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.009</td>
                <td>Process Injection</td>
                <td>Proc Memory</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.009">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.009">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.009">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.009">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.011</td>
                <td>Process Injection</td>
                <td>Extra Window Memory Injection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.011">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.011">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.011">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.011">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.012</td>
                <td>Process Injection</td>
                <td>Process Hollowing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.012">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.012">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.012">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.012">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1055.013</td>
                <td>Process Injection</td>
                <td>Process Doppelgänging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.013">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.013">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.013">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.013">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1055.014</td>
                <td>Process Injection</td>
                <td>VDSO Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1055.014">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1055.014">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1055.014">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1055.014">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1056</td>
                <td>Input Capture</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1056">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1056">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1056">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1056">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1056.001</td>
                <td>Input Capture</td>
                <td>Keylogging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1056.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1056.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1056.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1056.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1056.002</td>
                <td>Input Capture</td>
                <td>GUI Input Capture</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1056.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1056.002">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1056.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1056.002">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1056.003</td>
                <td>Input Capture</td>
                <td>Web Portal Capture</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1056.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1056.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1056.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1056.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1056.004</td>
                <td>Input Capture</td>
                <td>Credential API Hooking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1056.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1056.004">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1056.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1056.004">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1057</td>
                <td>Process Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1057">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1057">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1057">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1057">2</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1059</td>
                <td>Command and Scripting Interpreter</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059">32</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059">27</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059">7</a></td>
                <td>67</td>
            </tr>
            <tr>
                <td>T1059.001</td>
                <td>Command and Scripting Interpreter</td>
                <td>PowerShell</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.001">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.001">138</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.001">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.001">15</a></td>
                <td>162</td>
            </tr>
            <tr>
                <td>T1059.002</td>
                <td>Command and Scripting Interpreter</td>
                <td>AppleScript</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1059.003</td>
                <td>Command and Scripting Interpreter</td>
                <td>Windows Command Shell</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.003">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.003">15</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.003">4</a></td>
                <td>21</td>
            </tr>
            <tr>
                <td>T1059.004</td>
                <td>Command and Scripting Interpreter</td>
                <td>Unix Shell</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.004">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.004">0</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1059.005</td>
                <td>Command and Scripting Interpreter</td>
                <td>Visual Basic</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.005">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.005">17</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.005">1</a></td>
                <td>19</td>
            </tr>
            <tr>
                <td>T1059.006</td>
                <td>Command and Scripting Interpreter</td>
                <td>Python</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.006">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.006">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.006">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1059.007</td>
                <td>Command and Scripting Interpreter</td>
                <td>JavaScript/JScript</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.007">11</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.007">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.007">0</a></td>
                <td>13</td>
            </tr>
            <tr>
                <td>T1059.008</td>
                <td>Command and Scripting Interpreter</td>
                <td>Network Device CLI</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1059.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1059.008">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1059.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1059.008">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1061</td>
                <td>Graphical User Interface</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1061">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1061">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1061">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1061">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1062</td>
                <td>Hypervisor</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1062">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1062">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1062">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1062">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1064</td>
                <td>Scripting</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1064">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1064">18</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1064">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1064">0</a></td>
                <td>18</td>
            </tr>
            <tr>
                <td>T1068</td>
                <td>Exploitation for Privilege Escalation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1068">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1068">15</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1068">10</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1068">14</a></td>
                <td>40</td>
            </tr>
            <tr>
                <td>T1069</td>
                <td>Permission Groups Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1069">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1069">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1069">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1069">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1069.001</td>
                <td>Permission Groups Discovery</td>
                <td>Local Groups</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1069.001">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1069.001">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1069.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1069.001">11</a></td>
                <td>19</td>
            </tr>
            <tr>
                <td>T1069.002</td>
                <td>Permission Groups Discovery</td>
                <td>Domain Groups</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1069.002">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1069.002">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1069.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1069.002">18</a></td>
                <td>27</td>
            </tr>
            <tr>
                <td>T1069.003</td>
                <td>Permission Groups Discovery</td>
                <td>Cloud Groups</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1069.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1069.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1069.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1069.003">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1070</td>
                <td>Indicator Removal on Host</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070">10</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070">12</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070">3</a></td>
                <td>25</td>
            </tr>
            <tr>
                <td>T1070.001</td>
                <td>Indicator Removal on Host</td>
                <td>Clear Windows Event Logs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.001">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.001">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.001">6</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1070.002</td>
                <td>Indicator Removal on Host</td>
                <td>Clear Linux or Mac System Logs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1070.003</td>
                <td>Indicator Removal on Host</td>
                <td>Clear Command History</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.003">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.003">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1070.004</td>
                <td>Indicator Removal on Host</td>
                <td>File Deletion</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.004">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.004">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.004">2</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1070.005</td>
                <td>Indicator Removal on Host</td>
                <td>Network Share Connection Removal</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.005">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.005">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.005">1</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1070.006</td>
                <td>Indicator Removal on Host</td>
                <td>Timestomp</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1070.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1070.006">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1070.006">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1070.006">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1071</td>
                <td>Application Layer Protocol</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1071">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1071">18</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1071">8</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1071">0</a></td>
                <td>26</td>
            </tr>
            <tr>
                <td>T1071.001</td>
                <td>Application Layer Protocol</td>
                <td>Web Protocols</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1071.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1071.001">24</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1071.001">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1071.001">1</a></td>
                <td>28</td>
            </tr>
            <tr>
                <td>T1071.002</td>
                <td>Application Layer Protocol</td>
                <td>File Transfer Protocols</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1071.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1071.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1071.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1071.002">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1071.003</td>
                <td>Application Layer Protocol</td>
                <td>Mail Protocols</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1071.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1071.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1071.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1071.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1071.004</td>
                <td>Application Layer Protocol</td>
                <td>DNS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1071.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1071.004">16</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1071.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1071.004">2</a></td>
                <td>18</td>
            </tr>
            <tr>
                <td>T1072</td>
                <td>Software Deployment Tools</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1072">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1072">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1072">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1072">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1074</td>
                <td>Data Staged</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1074">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1074">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1074">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1074">1</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1074.001</td>
                <td>Data Staged</td>
                <td>Local Data Staging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1074.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1074.001">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1074.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1074.001">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1074.002</td>
                <td>Data Staged</td>
                <td>Remote Data Staging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1074.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1074.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1074.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1074.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1078</td>
                <td>Valid Accounts</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1078">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1078">13</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1078">24</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1078">25</a></td>
                <td>62</td>
            </tr>
            <tr>
                <td>T1078.001</td>
                <td>Valid Accounts</td>
                <td>Default Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1078.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1078.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1078.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1078.001">4</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1078.002</td>
                <td>Valid Accounts</td>
                <td>Domain Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1078.002">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1078.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1078.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1078.002">1</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1078.003</td>
                <td>Valid Accounts</td>
                <td>Local Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1078.003">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1078.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1078.003">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1078.003">1</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1078.004</td>
                <td>Valid Accounts</td>
                <td>Cloud Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1078.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1078.004">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1078.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1078.004">8</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1080</td>
                <td>Taint Shared Content</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1080">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1080">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1080">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1080">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1082</td>
                <td>System Information Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1082">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1082">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1082">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1082">3</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1083</td>
                <td>File and Directory Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1083">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1083">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1083">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1083">1</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1087</td>
                <td>Account Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1087">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1087">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1087">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1087">5</a></td>
                <td>21</td>
            </tr>
            <tr>
                <td>T1087.001</td>
                <td>Account Discovery</td>
                <td>Local Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1087.001">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1087.001">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1087.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1087.001">11</a></td>
                <td>20</td>
            </tr>
            <tr>
                <td>T1087.002</td>
                <td>Account Discovery</td>
                <td>Domain Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1087.002">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1087.002">10</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1087.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1087.002">17</a></td>
                <td>30</td>
            </tr>
            <tr>
                <td>T1087.003</td>
                <td>Account Discovery</td>
                <td>Email Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1087.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1087.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1087.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1087.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1087.004</td>
                <td>Account Discovery</td>
                <td>Cloud Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1087.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1087.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1087.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1087.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1090</td>
                <td>Proxy</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1090">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1090">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1090">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1090">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1090.001</td>
                <td>Proxy</td>
                <td>Internal Proxy</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1090.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1090.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1090.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1090.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1090.002</td>
                <td>Proxy</td>
                <td>External Proxy</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1090.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1090.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1090.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1090.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1090.003</td>
                <td>Proxy</td>
                <td>Multi-hop Proxy</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1090.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1090.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1090.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1090.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1090.004</td>
                <td>Proxy</td>
                <td>Domain Fronting</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1090.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1090.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1090.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1090.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1091</td>
                <td>Replication Through Removable Media</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1091">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1091">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1091">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1091">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1092</td>
                <td>Communication Through Removable Media</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1092">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1092">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1092">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1092">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1095</td>
                <td>Non-Application Layer Protocol</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1095">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1095">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1095">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1095">1</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1098</td>
                <td>Account Manipulation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1098">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1098">14</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1098">24</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1098">15</a></td>
                <td>54</td>
            </tr>
            <tr>
                <td>T1098.001</td>
                <td>Account Manipulation</td>
                <td>Additional Cloud Credentials</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1098.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1098.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1098.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1098.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1098.002</td>
                <td>Account Manipulation</td>
                <td>Exchange Email Delegate Permissions</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1098.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1098.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1098.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1098.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1098.003</td>
                <td>Account Manipulation</td>
                <td>Add Office 365 Global Administrator Role</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1098.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1098.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1098.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1098.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1098.004</td>
                <td>Account Manipulation</td>
                <td>SSH Authorized Keys</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1098.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1098.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1098.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1098.004">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1102</td>
                <td>Web Service</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1102">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1102">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1102">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1102">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1102.001</td>
                <td>Web Service</td>
                <td>Dead Drop Resolver</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1102.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1102.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1102.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1102.001">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1102.002</td>
                <td>Web Service</td>
                <td>Bidirectional Communication</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1102.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1102.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1102.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1102.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1102.003</td>
                <td>Web Service</td>
                <td>One-Way Communication</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1102.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1102.003">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1102.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1102.003">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1104</td>
                <td>Multi-Stage Channels</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1104">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1104">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1104">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1104">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1105</td>
                <td>Ingress Tool Transfer</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1105">4</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1105">24</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1105">9</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1105">5</a></td>
                <td>42</td>
            </tr>
            <tr>
                <td>T1106</td>
                <td>Native API</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1106">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1106">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1106">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1106">2</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1108</td>
                <td>Redundant Access</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1108">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1108">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1108">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1108">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1110</td>
                <td>Brute Force</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1110">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1110">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1110">8</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1110">2</a></td>
                <td>13</td>
            </tr>
            <tr>
                <td>T1110.001</td>
                <td>Brute Force</td>
                <td>Password Guessing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1110.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1110.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1110.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1110.001">1</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1110.002</td>
                <td>Brute Force</td>
                <td>Password Cracking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1110.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1110.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1110.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1110.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1110.003</td>
                <td>Brute Force</td>
                <td>Password Spraying</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1110.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1110.003">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1110.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1110.003">8</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1110.004</td>
                <td>Brute Force</td>
                <td>Credential Stuffing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1110.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1110.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1110.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1110.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1111</td>
                <td>Two-Factor Authentication Interception</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1111">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1111">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1111">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1111">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1112</td>
                <td>Modify Registry</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1112">5</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1112">42</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1112">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1112">3</a></td>
                <td>52</td>
            </tr>
            <tr>
                <td>T1113</td>
                <td>Screen Capture</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1113">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1113">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1113">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1113">1</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1114</td>
                <td>Email Collection</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1114">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1114">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1114">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1114">1</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1114.001</td>
                <td>Email Collection</td>
                <td>Local Email Collection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1114.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1114.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1114.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1114.001">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1114.002</td>
                <td>Email Collection</td>
                <td>Remote Email Collection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1114.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1114.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1114.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1114.002">3</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1114.003</td>
                <td>Email Collection</td>
                <td>Email Forwarding Rule</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1114.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1114.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1114.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1114.003">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1115</td>
                <td>Clipboard Data</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1115">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1115">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1115">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1115">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1119</td>
                <td>Automated Collection</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1119">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1119">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1119">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1119">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1120</td>
                <td>Peripheral Device Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1120">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1120">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1120">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1120">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1123</td>
                <td>Audio Capture</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1123">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1123">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1123">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1123">1</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1124</td>
                <td>System Time Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1124">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1124">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1124">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1124">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1125</td>
                <td>Video Capture</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1125">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1125">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1125">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1125">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1127</td>
                <td>Trusted Developer Utilities Proxy Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1127">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1127">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1127">8</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1127">2</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1127.001</td>
                <td>Trusted Developer Utilities Proxy Execution</td>
                <td>MSBuild</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1127.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1127.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1127.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1127.001">3</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1129</td>
                <td>Shared Modules</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1129">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1129">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1129">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1129">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1132</td>
                <td>Data Encoding</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1132">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1132">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1132">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1132">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1132.001</td>
                <td>Data Encoding</td>
                <td>Standard Encoding</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1132.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1132.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1132.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1132.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1132.002</td>
                <td>Data Encoding</td>
                <td>Non-Standard Encoding</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1132.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1132.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1132.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1132.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1133</td>
                <td>External Remote Services</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1133">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1133">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1133">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1133">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1134</td>
                <td>Access Token Manipulation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134">4</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1134.001</td>
                <td>Access Token Manipulation</td>
                <td>Token Impersonation/Theft</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134.001">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134.001">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1134.002</td>
                <td>Access Token Manipulation</td>
                <td>Create Process with Token</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134.002">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134.002">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1134.003</td>
                <td>Access Token Manipulation</td>
                <td>Make and Impersonate Token</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1134.004</td>
                <td>Access Token Manipulation</td>
                <td>Parent PID Spoofing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134.004">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1134.005</td>
                <td>Access Token Manipulation</td>
                <td>SID-History Injection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1134.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1134.005">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1134.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1134.005">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1135</td>
                <td>Network Share Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1135">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1135">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1135">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1135">3</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1136</td>
                <td>Create Account</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1136">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1136">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1136">7</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1136">0</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1136.001</td>
                <td>Create Account</td>
                <td>Local Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1136.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1136.001">10</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1136.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1136.001">3</a></td>
                <td>14</td>
            </tr>
            <tr>
                <td>T1136.002</td>
                <td>Create Account</td>
                <td>Domain Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1136.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1136.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1136.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1136.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1136.003</td>
                <td>Create Account</td>
                <td>Cloud Account</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1136.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1136.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1136.003">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1136.003">6</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1137</td>
                <td>Office Application Startup</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1137.001</td>
                <td>Office Application Startup</td>
                <td>Office Template Macros</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1137.002</td>
                <td>Office Application Startup</td>
                <td>Office Test</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1137.003</td>
                <td>Office Application Startup</td>
                <td>Outlook Forms</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1137.004</td>
                <td>Office Application Startup</td>
                <td>Outlook Home Page</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1137.005</td>
                <td>Office Application Startup</td>
                <td>Outlook Rules</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1137.006</td>
                <td>Office Application Startup</td>
                <td>Add-ins</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1137.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1137.006">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1137.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1137.006">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1140</td>
                <td>Deobfuscate/Decode Files or Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1140">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1140">9</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1140">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1140">2</a></td>
                <td>17</td>
            </tr>
            <tr>
                <td>T1149</td>
                <td>LC_MAIN Hijacking</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1149">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1149">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1149">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1149">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1153</td>
                <td>Source</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1153">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1153">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1153">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1153">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1175</td>
                <td>Component Object Model and Distributed COM</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1175">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1175">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1175">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1175">0</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1176</td>
                <td>Browser Extensions</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1176">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1176">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1176">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1176">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1185</td>
                <td>Man in the Browser</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1185">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1185">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1185">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1185">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1187</td>
                <td>Forced Authentication</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1187">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1187">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1187">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1187">1</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1189</td>
                <td>Drive-by Compromise</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1189">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1189">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1189">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1189">1</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1190</td>
                <td>Exploit Public-Facing Application</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1190">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1190">108</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1190">15</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1190">6</a></td>
                <td>129</td>
            </tr>
            <tr>
                <td>T1195</td>
                <td>Supply Chain Compromise</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1195">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1195">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1195">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1195">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1195.001</td>
                <td>Supply Chain Compromise</td>
                <td>Compromise Software Dependencies and Development Tools</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1195.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1195.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1195.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1195.001">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1195.002</td>
                <td>Supply Chain Compromise</td>
                <td>Compromise Software Supply Chain</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1195.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1195.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1195.002">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1195.002">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1195.003</td>
                <td>Supply Chain Compromise</td>
                <td>Compromise Hardware Supply Chain</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1195.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1195.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1195.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1195.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1197</td>
                <td>BITS Jobs</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1197">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1197">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1197">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1197">3</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1199</td>
                <td>Trusted Relationship</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1199">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1199">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1199">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1199">3</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1200</td>
                <td>Hardware Additions</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1200">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1200">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1200">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1200">5</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1201</td>
                <td>Password Policy Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1201">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1201">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1201">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1201">8</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1202</td>
                <td>Indirect Command Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1202">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1202">14</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1202">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1202">1</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1203</td>
                <td>Exploitation for Client Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1203">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1203">18</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1203">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1203">4</a></td>
                <td>23</td>
            </tr>
            <tr>
                <td>T1204</td>
                <td>User Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1204">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1204">21</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1204">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1204">3</a></td>
                <td>30</td>
            </tr>
            <tr>
                <td>T1204.001</td>
                <td>User Execution</td>
                <td>Malicious Link</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1204.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1204.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1204.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1204.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1204.002</td>
                <td>User Execution</td>
                <td>Malicious File</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1204.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1204.002">28</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1204.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1204.002">3</a></td>
                <td>32</td>
            </tr>
            <tr>
                <td>T1205</td>
                <td>Traffic Signaling</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1205">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1205">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1205">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1205">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1205.001</td>
                <td>Traffic Signaling</td>
                <td>Port Knocking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1205.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1205.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1205.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1205.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1207</td>
                <td>Rogue Domain Controller</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1207">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1207">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1207">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1207">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1210</td>
                <td>Exploitation of Remote Services</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1210">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1210">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1210">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1210">1</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1211</td>
                <td>Exploitation for Defense Evasion</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1211">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1211">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1211">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1211">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1212</td>
                <td>Exploitation for Credential Access</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1212">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1212">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1212">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1212">2</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1213</td>
                <td>Data from Information Repositories</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1213">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1213">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1213">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1213">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1213.001</td>
                <td>Data from Information Repositories</td>
                <td>Confluence</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1213.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1213.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1213.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1213.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1213.002</td>
                <td>Data from Information Repositories</td>
                <td>Sharepoint</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1213.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1213.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1213.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1213.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1216</td>
                <td>Signed Script Proxy Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1216">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1216">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1216">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1216">0</a></td>
                <td>12</td>
            </tr>
            <tr>
                <td>T1216.001</td>
                <td>Signed Script Proxy Execution</td>
                <td>PubPrn</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1216.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1216.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1216.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1216.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1217</td>
                <td>Browser Bookmark Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1217">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1217">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1217">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1217">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1218</td>
                <td>Signed Binary Proxy Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218">53</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218">16</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218">0</a></td>
                <td>69</td>
            </tr>
            <tr>
                <td>T1218.001</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Compiled HTML File</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.001">4</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1218.002</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Control Panel</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.002">1</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1218.003</td>
                <td>Signed Binary Proxy Execution</td>
                <td>CMSTP</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.003">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.003">3</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1218.004</td>
                <td>Signed Binary Proxy Execution</td>
                <td>InstallUtil</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.004">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.004">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1218.005</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Mshta</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.005">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.005">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.005">8</a></td>
                <td>20</td>
            </tr>
            <tr>
                <td>T1218.007</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Msiexec</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.007">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.007">1</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1218.008</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Odbcconf</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.008">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.008">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1218.009</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Regsvcs/Regasm</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.009">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.009">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.009">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.009">6</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1218.010</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Regsvr32</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.010">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.010">17</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.010">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.010">3</a></td>
                <td>24</td>
            </tr>
            <tr>
                <td>T1218.011</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Rundll32</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.011">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.011">25</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.011">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.011">16</a></td>
                <td>45</td>
            </tr>
            <tr>
                <td>T1218.012</td>
                <td>Signed Binary Proxy Execution</td>
                <td>Verclsid</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1218.012">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1218.012">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1218.012">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1218.012">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1219</td>
                <td>Remote Access Software</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1219">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1219">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1219">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1219">0</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1220</td>
                <td>XSL Script Processing</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1220">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1220">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1220">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1220">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1221</td>
                <td>Template Injection</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1221">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1221">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1221">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1221">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1222</td>
                <td>File and Directory Permissions Modification</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1222">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1222">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1222">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1222">8</a></td>
                <td>13</td>
            </tr>
            <tr>
                <td>T1222.001</td>
                <td>File and Directory Permissions Modification</td>
                <td>Windows File and Directory Permissions Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1222.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1222.001">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1222.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1222.001">1</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1222.002</td>
                <td>File and Directory Permissions Modification</td>
                <td>Linux and Mac File and Directory Permissions Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1222.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1222.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1222.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1222.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1480</td>
                <td>Execution Guardrails</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1480">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1480">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1480">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1480">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1480.001</td>
                <td>Execution Guardrails</td>
                <td>Environmental Keying</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1480.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1480.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1480.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1480.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1482</td>
                <td>Domain Trust Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1482">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1482">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1482">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1482">12</a></td>
                <td>20</td>
            </tr>
            <tr>
                <td>T1484</td>
                <td>Domain Policy Modification</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1484">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1484">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1484">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1484">4</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1484.001</td>
                <td>Domain Policy Modification</td>
                <td>Group Policy Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1484.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1484.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1484.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1484.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1484.002</td>
                <td>Domain Policy Modification</td>
                <td>Domain Trust Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1484.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1484.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1484.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1484.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1485</td>
                <td>Data Destruction</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1485">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1485">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1485">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1485">3</a></td>
                <td>12</td>
            </tr>
            <tr>
                <td>T1486</td>
                <td>Data Encrypted for Impact</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1486">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1486">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1486">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1486">6</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1489</td>
                <td>Service Stop</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1489">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1489">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1489">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1489">8</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1490</td>
                <td>Inhibit System Recovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1490">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1490">10</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1490">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1490">9</a></td>
                <td>26</td>
            </tr>
            <tr>
                <td>T1491</td>
                <td>Defacement</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1491">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1491">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1491">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1491">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1491.001</td>
                <td>Defacement</td>
                <td>Internal Defacement</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1491.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1491.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1491.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1491.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1491.002</td>
                <td>Defacement</td>
                <td>External Defacement</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1491.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1491.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1491.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1491.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1495</td>
                <td>Firmware Corruption</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1495">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1495">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1495">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1495">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1496</td>
                <td>Resource Hijacking</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1496">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1496">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1496">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1496">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1497</td>
                <td>Virtualization/Sandbox Evasion</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1497">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1497">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1497">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1497">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1497.001</td>
                <td>Virtualization/Sandbox Evasion</td>
                <td>System Checks</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1497.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1497.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1497.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1497.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1497.002</td>
                <td>Virtualization/Sandbox Evasion</td>
                <td>User Activity Based Checks</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1497.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1497.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1497.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1497.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1497.003</td>
                <td>Virtualization/Sandbox Evasion</td>
                <td>Time Based Evasion</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1497.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1497.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1497.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1497.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1498</td>
                <td>Network Denial of Service</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1498">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1498">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1498">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1498">5</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1498.001</td>
                <td>Network Denial of Service</td>
                <td>Direct Network Flood</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1498.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1498.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1498.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1498.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1498.002</td>
                <td>Network Denial of Service</td>
                <td>Reflection Amplification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1498.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1498.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1498.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1498.002">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1499</td>
                <td>Endpoint Denial of Service</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1499">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1499">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1499">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1499">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1499.001</td>
                <td>Endpoint Denial of Service</td>
                <td>OS Exhaustion Flood</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1499.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1499.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1499.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1499.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1499.002</td>
                <td>Endpoint Denial of Service</td>
                <td>Service Exhaustion Flood</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1499.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1499.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1499.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1499.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1499.003</td>
                <td>Endpoint Denial of Service</td>
                <td>Application Exhaustion Flood</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1499.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1499.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1499.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1499.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1499.004</td>
                <td>Endpoint Denial of Service</td>
                <td>Application or System Exploitation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1499.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1499.004">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1499.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1499.004">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1505</td>
                <td>Server Software Component</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1505">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1505">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1505">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1505">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1505.001</td>
                <td>Server Software Component</td>
                <td>SQL Stored Procedures</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1505.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1505.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1505.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1505.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1505.002</td>
                <td>Server Software Component</td>
                <td>Transport Agent</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1505.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1505.002">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1505.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1505.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1505.003</td>
                <td>Server Software Component</td>
                <td>Web Shell</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1505.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1505.003">19</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1505.003">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1505.003">3</a></td>
                <td>25</td>
            </tr>
            <tr>
                <td>T1518</td>
                <td>Software Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1518">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1518">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1518">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1518">1</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1518.001</td>
                <td>Software Discovery</td>
                <td>Security Software Discovery</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1518.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1518.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1518.001">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1518.001">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1525</td>
                <td>Implant Container Image</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1525">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1525">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1525">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1525">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1526</td>
                <td>Cloud Service Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1526">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1526">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1526">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1526">5</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1528</td>
                <td>Steal Application Access Token</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1528">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1528">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1528">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1528">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1529</td>
                <td>System Shutdown/Reboot</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1529">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1529">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1529">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1529">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1530</td>
                <td>Data from Cloud Storage Object</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1530">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1530">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1530">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1530">6</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1531</td>
                <td>Account Access Removal</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1531">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1531">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1531">7</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1531">3</a></td>
                <td>12</td>
            </tr>
            <tr>
                <td>T1534</td>
                <td>Internal Spearphishing</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1534">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1534">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1534">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1534">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1535</td>
                <td>Unused/Unsupported Cloud Regions</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1535">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1535">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1535">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1535">4</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1537</td>
                <td>Transfer Data to Cloud Account</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1537">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1537">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1537">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1537">1</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1538</td>
                <td>Cloud Service Dashboard</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1538">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1538">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1538">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1538">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1539</td>
                <td>Steal Web Session Cookie</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1539">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1539">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1539">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1539">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1542</td>
                <td>Pre-OS Boot</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1542.001</td>
                <td>Pre-OS Boot</td>
                <td>System Firmware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1542.002</td>
                <td>Pre-OS Boot</td>
                <td>Component Firmware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1542.003</td>
                <td>Pre-OS Boot</td>
                <td>Bootkit</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1542.004</td>
                <td>Pre-OS Boot</td>
                <td>ROMMONkit</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1542.005</td>
                <td>Pre-OS Boot</td>
                <td>TFTP Boot</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1542.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1542.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1542.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1542.005">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1543</td>
                <td>Create or Modify System Process</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1543">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1543">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1543">15</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1543">6</a></td>
                <td>21</td>
            </tr>
            <tr>
                <td>T1543.001</td>
                <td>Create or Modify System Process</td>
                <td>Launch Agent</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1543.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1543.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1543.001">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1543.001">2</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1543.002</td>
                <td>Create or Modify System Process</td>
                <td>Systemd Service</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1543.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1543.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1543.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1543.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1543.003</td>
                <td>Create or Modify System Process</td>
                <td>Windows Service</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1543.003">6</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1543.003">21</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1543.003">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1543.003">4</a></td>
                <td>37</td>
            </tr>
            <tr>
                <td>T1543.004</td>
                <td>Create or Modify System Process</td>
                <td>Launch Daemon</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1543.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1543.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1543.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1543.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1546</td>
                <td>Event Triggered Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546">12</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546">0</a></td>
                <td>18</td>
            </tr>
            <tr>
                <td>T1546.001</td>
                <td>Event Triggered Execution</td>
                <td>Change Default File Association</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.001">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1546.002</td>
                <td>Event Triggered Execution</td>
                <td>Screensaver</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1546.003</td>
                <td>Event Triggered Execution</td>
                <td>Windows Management Instrumentation Event Subscription</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.003">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.003">12</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.003">2</a></td>
                <td>15</td>
            </tr>
            <tr>
                <td>T1546.004</td>
                <td>Event Triggered Execution</td>
                <td>.bash_profile and .bashrc</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.004">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.004">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1546.005</td>
                <td>Event Triggered Execution</td>
                <td>Trap</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1546.006</td>
                <td>Event Triggered Execution</td>
                <td>LC_LOAD_DYLIB Addition</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1546.007</td>
                <td>Event Triggered Execution</td>
                <td>Netsh Helper DLL</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.007">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.007">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1546.008</td>
                <td>Event Triggered Execution</td>
                <td>Accessibility Features</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.008">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.008">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.008">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.008">1</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1546.009</td>
                <td>Event Triggered Execution</td>
                <td>AppCert DLLs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.009">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.009">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.009">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.009">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1546.010</td>
                <td>Event Triggered Execution</td>
                <td>AppInit DLLs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.010">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.010">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.010">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.010">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1546.011</td>
                <td>Event Triggered Execution</td>
                <td>Application Shimming</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.011">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.011">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.011">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.011">3</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1546.012</td>
                <td>Event Triggered Execution</td>
                <td>Image File Execution Options Injection</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.012">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.012">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.012">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.012">1</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1546.013</td>
                <td>Event Triggered Execution</td>
                <td>PowerShell Profile</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.013">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.013">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.013">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.013">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1546.014</td>
                <td>Event Triggered Execution</td>
                <td>Emond</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.014">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.014">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.014">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.014">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1546.015</td>
                <td>Event Triggered Execution</td>
                <td>Component Object Model Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1546.015">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1546.015">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1546.015">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1546.015">1</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1547</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547">22</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547">3</a></td>
                <td>27</td>
            </tr>
            <tr>
                <td>T1547.001</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Registry Run Keys / Startup Folder</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.001">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.001">13</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.001">9</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.001">2</a></td>
                <td>27</td>
            </tr>
            <tr>
                <td>T1547.002</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Authentication Package</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.002">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1547.003</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Time Providers</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1547.004</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Winlogon Helper DLL</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.004">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.004">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.004">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1547.005</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Security Support Provider</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.005">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.005">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.005">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1547.006</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Kernel Modules and Extensions</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.006">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.006">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1547.007</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Re-opened Applications</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.007">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.007">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1547.008</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>LSASS Driver</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.008">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.008">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1547.009</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Shortcut Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.009">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.009">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.009">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.009">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1547.010</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Port Monitors</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.010">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.010">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.010">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.010">1</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1547.011</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Plist Modification</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.011">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.011">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.011">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.011">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1547.012</td>
                <td>Boot or Logon Autostart Execution</td>
                <td>Print Processors</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1547.012">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1547.012">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1547.012">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1547.012">6</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1548</td>
                <td>Abuse Elevation Control Mechanism</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1548">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1548">8</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1548">18</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1548">6</a></td>
                <td>33</td>
            </tr>
            <tr>
                <td>T1548.001</td>
                <td>Abuse Elevation Control Mechanism</td>
                <td>Setuid and Setgid</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1548.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1548.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1548.001">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1548.001">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1548.002</td>
                <td>Abuse Elevation Control Mechanism</td>
                <td>Bypass User Account Control</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1548.002">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1548.002">41</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1548.002">10</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1548.002">10</a></td>
                <td>64</td>
            </tr>
            <tr>
                <td>T1548.003</td>
                <td>Abuse Elevation Control Mechanism</td>
                <td>Sudo and Sudo Caching</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1548.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1548.003">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1548.003">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1548.003">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1548.004</td>
                <td>Abuse Elevation Control Mechanism</td>
                <td>Elevated Execution with Prompt</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1548.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1548.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1548.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1548.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1550</td>
                <td>Use Alternate Authentication Material</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1550">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1550">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1550">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1550">1</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1550.001</td>
                <td>Use Alternate Authentication Material</td>
                <td>Application Access Token</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1550.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1550.001">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1550.001">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1550.001">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1550.002</td>
                <td>Use Alternate Authentication Material</td>
                <td>Pass the Hash</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1550.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1550.002">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1550.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1550.002">2</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1550.003</td>
                <td>Use Alternate Authentication Material</td>
                <td>Pass the Ticket</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1550.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1550.003">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1550.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1550.003">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1550.004</td>
                <td>Use Alternate Authentication Material</td>
                <td>Web Session Cookie</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1550.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1550.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1550.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1550.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1552</td>
                <td>Unsecured Credentials</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552">1</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1552.001</td>
                <td>Unsecured Credentials</td>
                <td>Credentials In Files</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.001">9</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.001">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.001">0</a></td>
                <td>12</td>
            </tr>
            <tr>
                <td>T1552.002</td>
                <td>Unsecured Credentials</td>
                <td>Credentials in Registry</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.002">2</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1552.003</td>
                <td>Unsecured Credentials</td>
                <td>Bash History</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.003">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.003">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1552.004</td>
                <td>Unsecured Credentials</td>
                <td>Private Keys</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.004">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.004">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.004">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1552.005</td>
                <td>Unsecured Credentials</td>
                <td>Cloud Instance Metadata API</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1552.006</td>
                <td>Unsecured Credentials</td>
                <td>Group Policy Preferences</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1552.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1552.006">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1552.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1552.006">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1553</td>
                <td>Subvert Trust Controls</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1553">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1553">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1553">5</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1553">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1553.001</td>
                <td>Subvert Trust Controls</td>
                <td>Gatekeeper Bypass</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1553.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1553.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1553.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1553.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1553.002</td>
                <td>Subvert Trust Controls</td>
                <td>Code Signing</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1553.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1553.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1553.002">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1553.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1553.003</td>
                <td>Subvert Trust Controls</td>
                <td>SIP and Trust Provider Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1553.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1553.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1553.003">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1553.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1553.004</td>
                <td>Subvert Trust Controls</td>
                <td>Install Root Certificate</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1553.004">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1553.004">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1553.004">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1553.004">1</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1554</td>
                <td>Compromise Client Software Binary</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1554">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1554">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1554">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1554">4</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1555</td>
                <td>Credentials from Password Stores</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1555">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1555">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1555">7</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1555">3</a></td>
                <td>11</td>
            </tr>
            <tr>
                <td>T1555.001</td>
                <td>Credentials from Password Stores</td>
                <td>Keychain</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1555.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1555.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1555.001">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1555.001">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1555.002</td>
                <td>Credentials from Password Stores</td>
                <td>Securityd Memory</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1555.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1555.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1555.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1555.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1555.003</td>
                <td>Credentials from Password Stores</td>
                <td>Credentials from Web Browsers</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1555.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1555.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1555.003">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1555.003">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1556</td>
                <td>Modify Authentication Process</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1556">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1556">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1556">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1556">3</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1556.001</td>
                <td>Modify Authentication Process</td>
                <td>Domain Controller Authentication</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1556.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1556.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1556.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1556.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1556.002</td>
                <td>Modify Authentication Process</td>
                <td>Password Filter DLL</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1556.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1556.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1556.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1556.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1556.003</td>
                <td>Modify Authentication Process</td>
                <td>Pluggable Authentication Modules</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1556.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1556.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1556.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1556.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1556.004</td>
                <td>Modify Authentication Process</td>
                <td>Network Device Authentication</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1556.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1556.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1556.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1556.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1557</td>
                <td>Man-in-the-Middle</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1557">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1557">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1557">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1557">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1557.001</td>
                <td>Man-in-the-Middle</td>
                <td>LLMNR/NBT-NS Poisoning and SMB Relay</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1557.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1557.001">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1557.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1557.001">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1557.002</td>
                <td>Man-in-the-Middle</td>
                <td>ARP Cache Poisoning</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1557.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1557.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1557.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1557.002">3</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1558</td>
                <td>Steal or Forge Kerberos Tickets</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1558">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1558">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1558">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1558">2</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1558.001</td>
                <td>Steal or Forge Kerberos Tickets</td>
                <td>Golden Ticket</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1558.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1558.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1558.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1558.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1558.002</td>
                <td>Steal or Forge Kerberos Tickets</td>
                <td>Silver Ticket</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1558.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1558.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1558.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1558.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1558.003</td>
                <td>Steal or Forge Kerberos Tickets</td>
                <td>Kerberoasting</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1558.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1558.003">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1558.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1558.003">2</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1558.004</td>
                <td>Steal or Forge Kerberos Tickets</td>
                <td>AS-REP Roasting</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1558.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1558.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1558.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1558.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1559</td>
                <td>Inter-Process Communication</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1559">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1559">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1559">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1559">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1559.001</td>
                <td>Inter-Process Communication</td>
                <td>Component Object Model</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1559.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1559.001">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1559.001">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1559.001">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1559.002</td>
                <td>Inter-Process Communication</td>
                <td>Dynamic Data Exchange</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1559.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1559.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1559.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1559.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1560</td>
                <td>Archive Collected Data</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1560">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1560">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1560">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1560">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1560.001</td>
                <td>Archive Collected Data</td>
                <td>Archive via Utility</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1560.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1560.001">9</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1560.001">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1560.001">5</a></td>
                <td>16</td>
            </tr>
            <tr>
                <td>T1560.002</td>
                <td>Archive Collected Data</td>
                <td>Archive via Library</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1560.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1560.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1560.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1560.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1560.003</td>
                <td>Archive Collected Data</td>
                <td>Archive via Custom Method</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1560.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1560.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1560.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1560.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1561</td>
                <td>Disk Wipe</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1561">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1561">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1561">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1561">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1561.001</td>
                <td>Disk Wipe</td>
                <td>Disk Content Wipe</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1561.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1561.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1561.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1561.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1561.002</td>
                <td>Disk Wipe</td>
                <td>Disk Structure Wipe</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1561.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1561.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1561.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1561.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1562</td>
                <td>Impair Defenses</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562">48</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562">1</a></td>
                <td>54</td>
            </tr>
            <tr>
                <td>T1562.001</td>
                <td>Impair Defenses</td>
                <td>Disable or Modify Tools</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.001">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.001">43</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.001">33</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.001">22</a></td>
                <td>101</td>
            </tr>
            <tr>
                <td>T1562.002</td>
                <td>Impair Defenses</td>
                <td>Disable Windows Event Logging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.002">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1562.003</td>
                <td>Impair Defenses</td>
                <td>Impair Command History Logging</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1562.004</td>
                <td>Impair Defenses</td>
                <td>Disable or Modify System Firewall</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.004">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.004">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.004">1</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1562.006</td>
                <td>Impair Defenses</td>
                <td>Indicator Blocking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.006">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.006">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.006">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.006">0</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1562.007</td>
                <td>Impair Defenses</td>
                <td>Disable or Modify Cloud Firewall</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.007">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.007">5</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1562.008</td>
                <td>Impair Defenses</td>
                <td>Disable Cloud Logs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1562.008">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1562.008">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1562.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1562.008">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1563</td>
                <td>Remote Service Session Hijacking</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1563">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1563">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1563">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1563">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1563.001</td>
                <td>Remote Service Session Hijacking</td>
                <td>SSH Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1563.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1563.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1563.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1563.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1563.002</td>
                <td>Remote Service Session Hijacking</td>
                <td>RDP Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1563.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1563.002">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1563.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1563.002">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1564</td>
                <td>Hide Artifacts</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564">0</a></td>
                <td>9</td>
            </tr>
            <tr>
                <td>T1564.001</td>
                <td>Hide Artifacts</td>
                <td>Hidden Files and Directories</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.001">4</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.001">1</a></td>
                <td>7</td>
            </tr>
            <tr>
                <td>T1564.002</td>
                <td>Hide Artifacts</td>
                <td>Hidden Users</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1564.003</td>
                <td>Hide Artifacts</td>
                <td>Hidden Window</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1564.004</td>
                <td>Hide Artifacts</td>
                <td>NTFS File Attributes</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.004">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.004">6</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.004">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.004">0</a></td>
                <td>10</td>
            </tr>
            <tr>
                <td>T1564.005</td>
                <td>Hide Artifacts</td>
                <td>Hidden File System</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1564.006</td>
                <td>Hide Artifacts</td>
                <td>Run Virtual Instance</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.006">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.006">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1564.007</td>
                <td>Hide Artifacts</td>
                <td>VBA Stomping</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1564.007">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1564.007">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1564.007">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1564.007">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1565</td>
                <td>Data Manipulation</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1565">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1565">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1565">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1565">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1565.001</td>
                <td>Data Manipulation</td>
                <td>Stored Data Manipulation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1565.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1565.001">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1565.001">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1565.001">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1565.002</td>
                <td>Data Manipulation</td>
                <td>Transmitted Data Manipulation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1565.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1565.002">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1565.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1565.002">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1565.003</td>
                <td>Data Manipulation</td>
                <td>Runtime Data Manipulation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1565.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1565.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1565.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1565.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1566</td>
                <td>Phishing</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1566">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1566">4</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1566">15</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1566">1</a></td>
                <td>20</td>
            </tr>
            <tr>
                <td>T1566.001</td>
                <td>Phishing</td>
                <td>Spearphishing Attachment</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1566.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1566.001">10</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1566.001">10</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1566.001">22</a></td>
                <td>42</td>
            </tr>
            <tr>
                <td>T1566.002</td>
                <td>Phishing</td>
                <td>Spearphishing Link</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1566.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1566.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1566.002">7</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1566.002">1</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1566.003</td>
                <td>Phishing</td>
                <td>Spearphishing via Service</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1566.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1566.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1566.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1566.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1567</td>
                <td>Exfiltration Over Web Service</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1567">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1567">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1567">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1567">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1567.001</td>
                <td>Exfiltration Over Web Service</td>
                <td>Exfiltration to Code Repository</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1567.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1567.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1567.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1567.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1567.002</td>
                <td>Exfiltration Over Web Service</td>
                <td>Exfiltration to Cloud Storage</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1567.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1567.002">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1567.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1567.002">1</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1568</td>
                <td>Dynamic Resolution</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1568">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1568">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1568">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1568">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1568.001</td>
                <td>Dynamic Resolution</td>
                <td>Fast Flux DNS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1568.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1568.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1568.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1568.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1568.002</td>
                <td>Dynamic Resolution</td>
                <td>Domain Generation Algorithms</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1568.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1568.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1568.002">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1568.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1568.003</td>
                <td>Dynamic Resolution</td>
                <td>DNS Calculation</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1568.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1568.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1568.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1568.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1569</td>
                <td>System Services</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1569">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1569">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1569">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1569">2</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1569.001</td>
                <td>System Services</td>
                <td>Launchctl</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1569.001">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1569.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1569.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1569.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1569.002</td>
                <td>System Services</td>
                <td>Service Execution</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1569.002">4</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1569.002">25</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1569.002">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1569.002">5</a></td>
                <td>37</td>
            </tr>
            <tr>
                <td>T1570</td>
                <td>Lateral Tool Transfer</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1570">3</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1570">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1570">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1570">0</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1571</td>
                <td>Non-Standard Port</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1571">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1571">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1571">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1571">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1572</td>
                <td>Protocol Tunneling</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1572">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1572">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1572">3</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1572">0</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1573</td>
                <td>Encrypted Channel</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1573">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1573">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1573">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1573">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1573.001</td>
                <td>Encrypted Channel</td>
                <td>Symmetric Cryptography</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1573.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1573.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1573.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1573.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1573.002</td>
                <td>Encrypted Channel</td>
                <td>Asymmetric Cryptography</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1573.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1573.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1573.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1573.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1574</td>
                <td>Hijack Execution Flow</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574">6</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574">2</a></td>
                <td>13</td>
            </tr>
            <tr>
                <td>T1574.001</td>
                <td>Hijack Execution Flow</td>
                <td>DLL Search Order Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.001">7</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.001">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.001">0</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1574.002</td>
                <td>Hijack Execution Flow</td>
                <td>DLL Side-Loading</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.002">18</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.002">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.002">1</a></td>
                <td>21</td>
            </tr>
            <tr>
                <td>T1574.004</td>
                <td>Hijack Execution Flow</td>
                <td>Dylib Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1574.005</td>
                <td>Hijack Execution Flow</td>
                <td>Executable Installer File Permissions Weakness</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1574.006</td>
                <td>Hijack Execution Flow</td>
                <td>LD_PRELOAD</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.006">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.006">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.006">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1574.007</td>
                <td>Hijack Execution Flow</td>
                <td>Path Interception by PATH Environment Variable</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.007">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.007">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.007">2</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.007">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1574.008</td>
                <td>Hijack Execution Flow</td>
                <td>Path Interception by Search Order Hijacking</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.008">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.008">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.008">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.008">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1574.009</td>
                <td>Hijack Execution Flow</td>
                <td>Path Interception by Unquoted Path</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.009">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.009">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.009">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.009">1</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1574.010</td>
                <td>Hijack Execution Flow</td>
                <td>Services File Permissions Weakness</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.010">2</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.010">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.010">1</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.010">0</a></td>
                <td>4</td>
            </tr>
            <tr>
                <td>T1574.011</td>
                <td>Hijack Execution Flow</td>
                <td>Services Registry Permissions Weakness</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.011">4</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.011">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.011">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.011">1</a></td>
                <td>8</td>
            </tr>
            <tr>
                <td>T1574.012</td>
                <td>Hijack Execution Flow</td>
                <td>COR_PROFILER</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1574.012">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1574.012">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1574.012">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1574.012">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1578</td>
                <td>Modify Cloud Compute Infrastructure</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1578">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1578">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1578">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1578">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1578.001</td>
                <td>Modify Cloud Compute Infrastructure</td>
                <td>Create Snapshot</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1578.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1578.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1578.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1578.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1578.002</td>
                <td>Modify Cloud Compute Infrastructure</td>
                <td>Create Cloud Instance</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1578.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1578.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1578.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1578.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1578.003</td>
                <td>Modify Cloud Compute Infrastructure</td>
                <td>Delete Cloud Instance</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1578.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1578.003">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1578.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1578.003">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1578.004</td>
                <td>Modify Cloud Compute Infrastructure</td>
                <td>Revert Cloud Instance</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1578.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1578.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1578.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1578.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1580</td>
                <td>Cloud Infrastructure Discovery</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1580">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1580">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1580">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1580">2</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1583</td>
                <td>Acquire Infrastructure</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.001</td>
                <td>Acquire Infrastructure</td>
                <td>Domains</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.002</td>
                <td>Acquire Infrastructure</td>
                <td>DNS Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.003</td>
                <td>Acquire Infrastructure</td>
                <td>Virtual Private Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.004</td>
                <td>Acquire Infrastructure</td>
                <td>Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.005</td>
                <td>Acquire Infrastructure</td>
                <td>Botnet</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1583.006</td>
                <td>Acquire Infrastructure</td>
                <td>Web Services</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1583.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1583.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1583.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1583.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584</td>
                <td>Compromise Infrastructure</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1584.001</td>
                <td>Compromise Infrastructure</td>
                <td>Domains</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584.002</td>
                <td>Compromise Infrastructure</td>
                <td>DNS Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584.003</td>
                <td>Compromise Infrastructure</td>
                <td>Virtual Private Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584.004</td>
                <td>Compromise Infrastructure</td>
                <td>Server</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584.005</td>
                <td>Compromise Infrastructure</td>
                <td>Botnet</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1584.006</td>
                <td>Compromise Infrastructure</td>
                <td>Web Services</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1584.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1584.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1584.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1584.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1585</td>
                <td>Establish Accounts</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1585">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1585">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1585">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1585">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1585.001</td>
                <td>Establish Accounts</td>
                <td>Social Media Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1585.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1585.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1585.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1585.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1585.002</td>
                <td>Establish Accounts</td>
                <td>Email Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1585.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1585.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1585.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1585.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1586</td>
                <td>Compromise Accounts</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1586">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1586">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1586">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1586">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1586.001</td>
                <td>Compromise Accounts</td>
                <td>Social Media Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1586.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1586.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1586.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1586.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1586.002</td>
                <td>Compromise Accounts</td>
                <td>Email Accounts</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1586.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1586.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1586.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1586.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1587</td>
                <td>Develop Capabilities</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1587">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1587">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1587">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1587">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1587.001</td>
                <td>Develop Capabilities</td>
                <td>Malware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1587.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1587.001">5</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1587.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1587.001">0</a></td>
                <td>5</td>
            </tr>
            <tr>
                <td>T1587.002</td>
                <td>Develop Capabilities</td>
                <td>Code Signing Certificates</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1587.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1587.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1587.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1587.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1587.003</td>
                <td>Develop Capabilities</td>
                <td>Digital Certificates</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1587.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1587.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1587.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1587.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1587.004</td>
                <td>Develop Capabilities</td>
                <td>Exploits</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1587.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1587.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1587.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1587.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1588</td>
                <td>Obtain Capabilities</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588">2</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588">0</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1588.001</td>
                <td>Obtain Capabilities</td>
                <td>Malware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1588.002</td>
                <td>Obtain Capabilities</td>
                <td>Tool</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.002">3</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.002">0</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1588.003</td>
                <td>Obtain Capabilities</td>
                <td>Code Signing Certificates</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1588.004</td>
                <td>Obtain Capabilities</td>
                <td>Digital Certificates</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1588.005</td>
                <td>Obtain Capabilities</td>
                <td>Exploits</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1588.006</td>
                <td>Obtain Capabilities</td>
                <td>Vulnerabilities</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1588.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1588.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1588.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1588.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1589</td>
                <td>Gather Victim Identity Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1589">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1589">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1589">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1589">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1589.001</td>
                <td>Gather Victim Identity Information</td>
                <td>Credentials</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1589.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1589.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1589.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1589.001">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1589.002</td>
                <td>Gather Victim Identity Information</td>
                <td>Email Addresses</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1589.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1589.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1589.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1589.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1589.003</td>
                <td>Gather Victim Identity Information</td>
                <td>Employee Names</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1589.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1589.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1589.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1589.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1590</td>
                <td>Gather Victim Network Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590">2</a></td>
                <td>3</td>
            </tr>
            <tr>
                <td>T1590.001</td>
                <td>Gather Victim Network Information</td>
                <td>Domain Properties</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.001">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1590.002</td>
                <td>Gather Victim Network Information</td>
                <td>DNS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1590.003</td>
                <td>Gather Victim Network Information</td>
                <td>Network Trust Dependencies</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.003">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1590.004</td>
                <td>Gather Victim Network Information</td>
                <td>Network Topology</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1590.005</td>
                <td>Gather Victim Network Information</td>
                <td>IP Addresses</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.005">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1590.006</td>
                <td>Gather Victim Network Information</td>
                <td>Network Security Appliances</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1590.006">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1590.006">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1590.006">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1590.006">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1591</td>
                <td>Gather Victim Org Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1591">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1591">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1591">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1591">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1591.001</td>
                <td>Gather Victim Org Information</td>
                <td>Determine Physical Locations</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1591.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1591.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1591.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1591.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1591.002</td>
                <td>Gather Victim Org Information</td>
                <td>Business Relationships</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1591.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1591.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1591.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1591.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1591.003</td>
                <td>Gather Victim Org Information</td>
                <td>Identify Business Tempo</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1591.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1591.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1591.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1591.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1591.004</td>
                <td>Gather Victim Org Information</td>
                <td>Identify Roles</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1591.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1591.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1591.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1591.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1592</td>
                <td>Gather Victim Host Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1592">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1592">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1592">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1592">5</a></td>
                <td>6</td>
            </tr>
            <tr>
                <td>T1592.001</td>
                <td>Gather Victim Host Information</td>
                <td>Hardware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1592.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1592.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1592.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1592.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1592.002</td>
                <td>Gather Victim Host Information</td>
                <td>Software</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1592.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1592.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1592.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1592.002">2</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1592.003</td>
                <td>Gather Victim Host Information</td>
                <td>Firmware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1592.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1592.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1592.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1592.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1592.004</td>
                <td>Gather Victim Host Information</td>
                <td>Client Configurations</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1592.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1592.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1592.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1592.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1593</td>
                <td>Search Open Websites/Domains</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1593">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1593">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1593">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1593">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1593.001</td>
                <td>Search Open Websites/Domains</td>
                <td>Social Media</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1593.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1593.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1593.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1593.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1593.002</td>
                <td>Search Open Websites/Domains</td>
                <td>Search Engines</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1593.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1593.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1593.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1593.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1594</td>
                <td>Search Victim-Owned Websites</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1594">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1594">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1594">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1594">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1595</td>
                <td>Active Scanning</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1595">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1595">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1595">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1595">2</a></td>
                <td>2</td>
            </tr>
            <tr>
                <td>T1595.001</td>
                <td>Active Scanning</td>
                <td>Scanning IP Blocks</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1595.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1595.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1595.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1595.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1595.002</td>
                <td>Active Scanning</td>
                <td>Vulnerability Scanning</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1595.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1595.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1595.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1595.002">1</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1596</td>
                <td>Search Open Technical Databases</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1596.001</td>
                <td>Search Open Technical Databases</td>
                <td>DNS/Passive DNS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1596.002</td>
                <td>Search Open Technical Databases</td>
                <td>WHOIS</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1596.003</td>
                <td>Search Open Technical Databases</td>
                <td>Digital Certificates</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1596.004</td>
                <td>Search Open Technical Databases</td>
                <td>CDNs</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596.004">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596.004">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596.004">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596.004">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1596.005</td>
                <td>Search Open Technical Databases</td>
                <td>Scan Databases</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1596.005">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1596.005">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1596.005">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1596.005">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1597</td>
                <td>Search Closed Sources</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1597">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1597">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1597">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1597">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1597.001</td>
                <td>Search Closed Sources</td>
                <td>Threat Intel Vendors</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1597.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1597.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1597.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1597.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1597.002</td>
                <td>Search Closed Sources</td>
                <td>Purchase Technical Data</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1597.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1597.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1597.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1597.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1598</td>
                <td>Phishing for Information</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1598">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1598">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1598">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1598">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1598.001</td>
                <td>Phishing for Information</td>
                <td>Spearphishing Service</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1598.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1598.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1598.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1598.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1598.002</td>
                <td>Phishing for Information</td>
                <td>Spearphishing Attachment</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1598.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1598.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1598.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1598.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1598.003</td>
                <td>Phishing for Information</td>
                <td>Spearphishing Link</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1598.003">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1598.003">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1598.003">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1598.003">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1599</td>
                <td>Network Boundary Bridging</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1599">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1599">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1599">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1599">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1599.001</td>
                <td>Network Boundary Bridging</td>
                <td>Network Address Translation Traversal</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1599.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1599.001">1</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1599.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1599.001">0</a></td>
                <td>1</td>
            </tr>
            <tr>
                <td>T1600</td>
                <td>Weaken Encryption</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1600">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1600">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1600">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1600">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1600.001</td>
                <td>Weaken Encryption</td>
                <td>Reduce Key Space</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1600.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1600.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1600.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1600.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1600.002</td>
                <td>Weaken Encryption</td>
                <td>Disable Crypto Hardware</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1600.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1600.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1600.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1600.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1601</td>
                <td>Modify System Image</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1601">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1601">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1601">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1601">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1601.001</td>
                <td>Modify System Image</td>
                <td>Patch System Image</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1601.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1601.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1601.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1601.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1601.002</td>
                <td>Modify System Image</td>
                <td>Downgrade System Image</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1601.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1601.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1601.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1601.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1602</td>
                <td>Data from Configuration Repository</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1602">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1602">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1602">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1602">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1602.001</td>
                <td>Data from Configuration Repository</td>
                <td>SNMP (MIB Dump)</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1602.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1602.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1602.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1602.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1602.002</td>
                <td>Data from Configuration Repository</td>
                <td>Network Device Configuration Dump</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1602.002">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1602.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1602.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1602.002">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1606</td>
                <td>Forge Web Credentials</td>
                <td>n/a</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1606">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1606">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1606">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1606">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1606.001</td>
                <td>Forge Web Credentials</td>
                <td>Web Cookies</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1606.001">0</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1606.001">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1606.001">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1606.001">0</a></td>
                <td>0</td>
            </tr>
            <tr>
                <td>T1606.002</td>
                <td>Forge Web Credentials</td>
                <td>SAML Tokens</td>
                <td><a href="https://github.com/mitre-attack/car/search?l=YAML&q=T1606.002">1</a></td>
                <td><a href="https://github.com/SigmaHQ/sigma/search?p=1&q=attack.t1606.002">0</a></td>
                <td><a href="https://github.com/elastic/detection-rules/search?l=TOML&q=T1606.002">0</a></td>
                <td><a href="https://github.com/splunk/security_content/search?l=YAML&p=1&q=T1606.002">0</a></td>
                <td>1</td>
            </tr>
      </tbody>
</table>
