---
title: Glossary
---

The *Glossary* is description of commonly used words and features of CAR.

### ATT&CK
[MITRE ATT&CK™](https://attack.mitre.org) is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community. 

### Analytic
An *analytic* describes the observable behavior generated for a TTP. It is the method by which a TTP can be identified. Its *hypothesis* describes the behavior expected, and the instantiation details its platform-specific implementation.

### Hypothesis
The *hypothesis* should generally describe why this analytic is worth making, that is, what information do you hope to gather through this analytic, and what could this information indicate? It should describe the identifiable objects or artifacts that are associated with or modified when an ATT&CK technique takes place.

### Information Domain
The *information domain* is the top-level categorization of the analytic. It should describe the type of analytic: *Is it based on anomaly detection? A specific behavior? Statistical analysis?* There are five possible information domains: **Host**, **Network**, and **Analytic**, **External**, and **Other**.

### Pseudocode
The *pseudocode* is a representative example of how the analytic query would be made.

### ATT&CK Detection 
A summary of the ATT&CK tactic and techniques the analytic detects as well as the level of coverage.

### Unit Tests
A set of commands that can be run which should trigger the analytic.

### Analytic Type
The kind of mechanism this analytic uses. 
The following table summarizes the different types of analytics.

Analytic Type|Description
---|---
**TTP**| A TTP analytic is designed to detect a certain adversary tactic, technique or procedure.
**Attribution**| An attribution analytic is an analytic that is designed to detect actions that are unique to a single to a certain threat actor.
**Posture/Hygiene**|A posture or hygiene analytic is designed to help in the maintenance of the analytic or security infrastructure.
**Situational Awareness**|A situational awareness analytic provide general information on the state of the environment. Often these analytics can be useful during an investigation, (e.g. information such as login times doesn't indicate malicious activity, but when coupled with other indicators can provide much needed additional information). These types of analytics can also be helpful for monitoring the "health" of the environment (e.g. on which hosts are sensors not working).
**Forensic**|A forensic analytic has a low SNR and is less likely to be indicative of adversary behavior but is nevertheless useful during an investigation. Several ''forensic analytics'' are anomaly-based, which can create excessive noise in a highly dynamic environment. Other analytics may also have noise as a result of admins/[[wikipedia:Power user|power users]], software installations, or internal scripts. However, when related results are triggered by multiple forensic analytics, the collective probability rises. Thus, the forensics analytics reinforce each other during the investigative process.}}
**Anomaly**|An anomaly analytic triggers on behavior that is not normally observed. Anomalous may not be explicitly malicious but may be suspect. For example, detection of executables that have never been run before or a process using the network which does not normally use the network. Like ''Situational Awareness analytics'', ''anomaly analytics'' don't necessarily indicate an attack.
**Statistical**|A 'statistical analytic uses various statistical mechanisms to identify adversarial behavior.
**Investigative**|An investigative analytic is an analytic that is primarily used during an investigation rather than as an alert.
**Malware**|A malware analytic is an analytic used to detect a specific kind of malware, such as Mimikatz.
**Event Characterization**|An event characterization analytic is used to characterize the output of another analytic into certain event types.
