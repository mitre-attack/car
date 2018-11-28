---
title: Welcome to the Cyber Analytics Repository
---

The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by [MITRE](https://www.mitre.org) based on the [MITRE ATT&CK](https://attack.mitre.org/) adversary model.

If you want to start exploring, try viewing the [Full Analytic List](analytics) or use the [CAR Exploration Tool (CARET)](https://mitre-attack.github.io/caret/#/).

Analytics stored in CAR contain the following information:
* a *hypothesis* which explains the idea behind the analytic
* the *information domain* or the primary domain the analytic is designed to operate within (e.g. host, network, process, external)
* references to [ATT&CK](https://attack.mitre.org/) Techniques and Tactics that the analytic detexts
* the [Glossary](Glossary)
* a pseudocode description of how the analytic might be implemented
* a unit test which can be run to trigger the analytic


## Methodology
CAR analytics were developed to detect the adversary behaviors in [ATT&CK](https://attack.mitre.org/). Development of an analytic is based upon the following activities: 
* identifying and prioritizing adversary behaviors from the ATT&CK adversary model 
* identifying the data necessary to detect the adversary behavior
* identification or creation of a sensor to collect the necessary data
* the actual creation of the analytic to detect the identified behaviors

CAR is intended to be shared with cyber-defenders throughout the community.

## Contributing

We would love your contributions, ideally via a pull request. Please see the [Contribution Guidance]({{ site.contributing }}) for more information.