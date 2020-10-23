## Identifying Internal hosts and services for lateral movement
After compromising an initial machine, adversaries commonly attempt to laterally move across the network. The first step to attempt the lateral movement often involves conducting host identification, port and service scans on the internal network via the compromised machine using tools such as Nmap, Cobalt Strike, etc.
### ATT&CK Coverage
|Technique |Level of Coverage |
|---|---|
|[Network Service Scanning](https://attack.mitre.org/techniques/T1046/)|Moderate|
### Analytic Code
It should be noted that when a host/ port/ service scan is performed from a compromised machine, a single machine makes multiple calls to other hosts in the network to identify live hosts and services. This can be detected using the following query:
Splunk Query
|---|
sourcetype='firewall_logs' dest_ip = 'internal_subnet' \| stats dc(dest_port) as pcount by source_ip \| where pcount >5
### Test Cases
To trigger this as an alert, we can run a test port scan from inside the network. To avoid generating unnecessary files on a host system, it is advised to run the following commands from a virtual machine or a docker instance connected via a bridged adaptor.
sudo apt-get install nmap
nmap -sn 0.0.0.0/24
Note: [Replace the 0.0.0.0 with relevant subnet address].
### Data Model Mappings
|Object|Action|Field|
|---|---|---|
|flow | start | dest_ip |
| flow | stop | dest_ip |
