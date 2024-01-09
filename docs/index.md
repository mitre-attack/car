---
title: Welcome to the Cyber Analytics Repository
---
The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by [MITRE](https://www.mitre.org) based on the [MITRE ATT&CK](https://attack.mitre.org/) adversary model. CAR defines a data model that is leveraged in its pseudocode representations, but also includes implementations directly targeted at specific tools (e.g., Splunk, EQL) in its analytics. With respect to coverage, CAR is focused on providing a set of validated and well-explained analytics, in particular with regards to their operating theory and rationale.

If you want to start exploring, try viewing the [Full Analytic List](analytics). Also, check out the [ATT&CK Navigator layer](https://mitre-attack.github.io/attack-navigator/beta/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fcar%2Fmaster%2Fdocs%2Fcar_attack%2Fcar_attack.json) that captures the current set of ATT&CK tactics and techniques covered by CAR.

Analytics stored in CAR contain the following information:
* a *hypothesis* which explains the idea behind the analytic
* the *information domain* or the primary domain the analytic is designed to operate within (e.g. host, network, process, external)
* references to [ATT&CK](https://attack.mitre.org/) Techniques and Tactics that the analytic detects
* the [Glossary](resources/glossary)
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

[This](https://www.mitre.org/publications/technical-papers/ttp-based-hunting) white paper on TTP-based hunting provides some useful insight into many of these activities.

## CAR and ATT&CK

It's important to remember that ATT&CK and CAR are separate projects for good reason. It's critical to keep how we articulate threats with ATT&CK separate from a set of possible ways to detect them with the analytics. We don't want the defender content in ATT&CK to be overly prescriptive about how someone can defend against ATT&CK techniques because there could be many different ways, and it's up to the organization implementing them to determine what works best for their environment and the threats they face. This is why we didn't put the analytics in ATT&CK to begin with. CAR is a good starting point for many organizations and can be a great platform for open analytic collaboration - but it isn't the be-all/end-all for defending against the threats described by ATT&CK.

## Analytic Source Code Libraries

Some analytics are built as source code for specific products. In these cases, code might support a broad set of detections in a way that makes it hard to describe a set of distinct analytics. For these types of analytics, rather than integrating them into the main CAR site, we've collected them under a library of implementations. Currently, the only library is [BZAR](https://github.com/mitre-attack/bzar), a collection of Zeek (Bro) scripts looking primarily at SMB and RPC traffic.

## Contributing

We would love your contributions! Please see the [Contribution Guidance]({{ site.contributing }}) for more information.
