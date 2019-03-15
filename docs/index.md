---
title: Welcome to the Cyber Analytics Repository
---

The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by [MITRE](https://www.mitre.org) based on the [MITRE ATT&CK](https://attack.mitre.org/) adversary model.

If you want to start exploring, try viewing the [Full Analytic List](analytics) or use the [CAR Exploration Tool (CARET)](https://mitre-attack.github.io/caret/#/).

Analytics stored in CAR contain the following information:
* a *hypothesis* which explains the idea behind the analytic
* the *information domain* or the primary domain the analytic is designed to operate within (e.g. host, network, process, external)
* references to [ATT&CK](https://attack.mitre.org/) Techniques and Tactics that the analytic detects
* the [Glossary](Glossary)
* a pseudocode description of how the analytic might be implemented
* a unit test which can be run to trigger the analytic

In addition to the analytics, CAR also contains a [data model](data_model) for observable data used to run the analytics and [sensors](sensors) that are used to collect that data.

## Methodology
CAR analytics were developed to detect the adversary behaviors in [ATT&CK](https://attack.mitre.org/). Development of an analytic is based upon the following activities: 
* identifying and prioritizing adversary behaviors from the ATT&CK adversary model 
* identifying the data necessary to detect the adversary behavior
* identification or creation of a sensor to collect the necessary data
* the actual creation of the analytic to detect the identified behaviors

CAR is intended to be shared with cyber-defenders throughout the community.

## CAR and ATT&CK

It's important to remember that ATT&CK and CAR are separate projects for good reason. It's critical to keep how we articulate threats with ATT&CK separate from a set of possible ways to detect them with the analytics. We don't want the defender content in ATT&CK to be overly prescriptive about how someone can defend against ATT&CK techniques because there could be many different ways, and it's up to the organization implementing them to determine what works best for their environment and the threats they face. This is why we didn't put the analytics in ATT&CK to begin with. CAR is a good starting point for many organizations and can be a great platform for open analytic collaboration - but it isn't the be-all/end-all for defending against the threats described by ATT&CK.

## Contributing

We would love your contributions! Please see the [Contribution Guidance]({{ site.contributing }}) for more information.