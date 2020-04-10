# Welcome to the Cyber Analytics Repository

The best way to view the analytics in this repository is via the [CAR website](https://car.mitre.org).

This repository is the way to contribute new analytics, data model changes, or sensor changes. Analytics contributed in this repo are automatically published in CAR.

## Where is everything?

Analytics are in the `analytics` directory as YAML files; the same is true for the YAML representations of `sensors` and the `data_model`. The website is built automatically from that structured content. Other content is all in the `docs` folder. 

The [implementations](implementations) directory contains libraries of analytics that are best represented as source code for specific tools. As an example, [BZAR](implementations/bzar) (Bro/Zeek ATT&CK-Based Analytics and Reporting) is a library of source code for Zeek (previously Bro).

## How do I contribute?

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) to better understand what we're looking for. There's also a Developer Certificate of Origin that you'll need to sign off on.
2. [Open an issue](https://github.com/mitre-attack/car/issues/new/choose). There are issue templates for adding an analytic, adding to the data model, and adding a new sensor mapping. If you have other changes, feel free to open a generic issue.
3. Wait for feedback on your issue. We may ask you for more information, or see what others in the community think. Once the issue is accepted and the change made, car.mitre.org will be automatically updated with your new content.
