# Contribute
You can help contribute to CAR. We're always on the lookout for new information to help refine and extend it.

In particular, we're hoping that people can contribute new analytics, updates to the data model, and new sensor mappings.

The best way to do all of that is to [open an issue](https://github.com/mitre-attack/car/issues/new/choose). There are issue templates for analytics, data model additions, and sensor mappings. But first, please read the submission guidelines below!

## Submission Guidelines

### Contributing Analytics
We understand that there are many analytics and many approaches to cybersecurity. 

The analytics in CAR are focused on processing data collected in a real-time format to detect threat behaviors described in [ATT&CK](https://attack.mitre.org). We see the value of mitigations, vulnerabilities, forensic data, and repositories of indicators of compromise (IOCs) but that is not the focus of CAR. Should you have submissions of those types of information, please consider resources such as CVE, IOC Bucket, [Sigma](https://github.com/Neo23x0/sigma), or other open-source venues dedicated to that category of information.

The following criteria are a consideration for us when vetting analytic submissions:
- An analytic must address a technique in [ATT&CK](https://attack.mitre.org).
- An analytic should only be shared if it has been used in an operational setting.
- An analytic must detect behaviors, not a specific artifact or nuance of a RAT or piece of malware. This is important! A detection for a piece of malware that executes a technique is great, but not a fit for CAR. Consider [Sigma](https://github.com/Neo23x0/sigma).
- We reserve the right to add new criteria over time as the vetting process evolves.

### Contributing to the Data Model
We're also looking for help extending the CAR data model.

The main rules for data model extensions are:
- The properties, objects, or actions to be added must be used in an analytic that meets the criteria above. That analytic doesn't necessarily need to be contributed to CAR, but we of course would prefer that you do so.
- The properties, objects, or actions to be added must be detectable using commonly available sensors.

The goal behind these rules is to ensure that the data model is grounded in real needs for data that can really be collected. We don't want an all-inclusive model that tends to confuse people.

### Contributing Sensors
New sensor mappings are also appreciated. In order to stay sensitive to any concerns about mapping commercial products, CAR only accepts sensor mappings for built-in operating system utilities or open source tools. Mappings of commercial products, either from the vendor or anyone else, will not be accepted.

### Contributing Updates

If you have updates or changes to any of the analytics, data model objects, or sensors please submit an issue and, optionally, a pull request. Changes are considered on an ad-hoc basis depending on the nature of the change and discussion on the issue. When in doubt, file an issue.

## License and IPR

To ensure that they can be used freely by all, CAR analytics in this repository are licensed using [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/). Those contributing content need to agree to the Developer's Certificate of Origin below.

### Developer's Certificate of Origin v1.1

```
By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
 have the right to submit it under the open source license
 indicated in the file; or

(b) The contribution is based upon previous work that, to the best
 of my knowledge, is covered under an appropriate open source
 license and I have the right under that license to submit that
 work with modifications, whether created in whole or in part
 by me, under the same open source license (unless I am
 permitted to submit under a different license), as indicated
 in the file; or

(c) The contribution was provided directly to me by some other
 person who certified (a), (b) or (c) and I have not modified
 it.

(d) I understand and agree that this project and the contribution
 are public and that a record of the contribution (including all
 personal information I submit with it, including my sign-off) is
 maintained indefinitely and may be redistributed consistent with
 this project or the open source license(s) involved.
```
THIS IS VERY KNOWLEDGABLE.
