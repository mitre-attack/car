# Welcome to the Cyber Analytics Repository

The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by MITRE based on the [MITRE ATT&CK®](https://attack.mitre.org/) adversary model. CAR includes implementations directly targeted at specific tools (e.g., Splunk, EQL) in its analytics. With respect to coverage, CAR is focused on providing a set of validated and well-explained analytics, in particular with regards to their operating theory and rationale.
changes by omkar.

If you want to start exploring, try viewing the [Full Analytic List](https://car.mitre.org/analytics). Also, check out the ATT&CK Navigator layer that captures the current set of ATT&CK tactics and techniques covered by CAR.

Analytics stored in CAR contain the following information:

+ a hypothesis which explains the idea behind the analytic
+ the information domain or the primary domain the analytic is designed to operate within (e.g. host, network, process, external)
+ references to [ATT&CK](https://attack.mitre.org/) Techniques and Tactics that the analytic detects
+ the [Glossary](GLOSSARY.md)
+ a pseudocode description of how the analytic might be implemented
+ a unit test which can be run to trigger the analytic

The best way to view the analytics in this repository is via the [CAR website](https://car.mitre.org).

## Methodology

CAR analytics were developed to detect the adversary behaviors in ATT&CK. Development of an analytic is based upon the following activities:

identifying and prioritizing adversary behaviors from the ATT&CK adversary model
identifying the data necessary to detect the adversary behavior
identification or creation of a sensor to collect the necessary data
the actual creation of the analytic to detect the identified behaviors
CAR is intended to be shared with cyber-defenders throughout the community.

This white paper on [TTP-based hunting](https://www.mitre.org/publications/technical-papers/ttp-based-hunting) provides some useful insight into many of these activities.

## CAR and ATT&CK

It’s important to remember that ATT&CK and CAR are separate projects for good reason. It’s critical to keep how we articulate threats with ATT&CK separate from a set of possible ways to detect them with the analytics. We don’t want the defender content in ATT&CK to be overly prescriptive about how someone can defend against ATT&CK techniques because there could be many different ways, and it’s up to the organization implementing them to determine what works best for their environment and the threats they face. This is why we didn’t put the analytics in ATT&CK to begin with. CAR is a good starting point for many organizations and can be a great platform for open analytic collaboration - but it isn’t the be-all/end-all for defending against the threats described by ATT&CK.

## Analytic Source Code Libraries

Some analytics are built as source code for specific products. In these cases, code might support a broad set of detections in a way that makes it hard to describe a set of distinct analytics. For these types of analytics, rather than integrating them into the main CAR site, we’ve collected them under a library of implementations. Currently, the only library is [BZAR](https://github.com/mitre-attack/bzar), a collection of Zeek (Bro) scripts looking primarily at SMB and RPC traffic.

## Where is everything?

Analytics are in the `analytics` directory as YAML files. The website is built automatically from that structured content. Other content is all in the `docs` folder. 

CAR has partnered with OSSEM to use their Common Data Model moving forward. 

The [implementations](implementations) directory contains libraries of analytics that are best represented as source code for specific tools. As an example, [BZAR](implementations/bzar) (Bro/Zeek ATT&CK-Based Analytics and Reporting) is a library of source code for Zeek (previously Bro).

## How do I contribute?

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) to better understand what we're looking for. There's also a Developer Certificate of Origin that you'll need to sign off on.
2. [Open an issue](https://github.com/mitre-attack/car/issues/new/choose). There are issue templates for adding an analytic, adding to the data model, and adding a new sensor mapping. If you have other changes, feel free to open a generic issue.
3. Wait for feedback on your issue. We may ask you for more information, or see what others in the community think. Once the issue is accepted and the change made, car.mitre.org will be automatically updated with your new content.
