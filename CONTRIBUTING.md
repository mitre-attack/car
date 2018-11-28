# Contribute
You can help contribute to CAR.

CAR is in a constant state of development. We are always on the lookout for new information to help refine and extend CAR. If you have additional analytics you would like to contribute, then we would like to hear from you.

The easiest way to contribute is to simply fork this repository and add the content directly. Then, issue a pull request and we'll consider it per the submission guidelines below. Issues and comments on issues are, of course, also welcome.

## Submission Guidelines

### Timeliness
We endeavor to vet submissions in a timely manner, but we are busy people. You can expect a response that your submission has been received within 24 hours and an additional substantive response indicating acceptance or denial within one month. Please understand that an influx of submissions may cause our response times to slow down. 

### Content
We understand that there are many analytics and many approaches to cybersecurity. 

Our analytics are focused on processing data collected in a real-time format to detect threat behaviors described in [ATT&CK](https://attack.mitre.org). We see the value of mitigations, vulnerabilities, forensic data, and repositories of indicators of compromise (IOCs) but that is not the focus of CAR. Should you have submissions of those types of information, please consider resources such as CVE, IOC Bucket, [Sigma](https://github.com/Neo23x0/sigma), or other open-source venues dedicated to that category of information.

The following criteria are a consideration for us when vetting analytic submissions:
- An analytic must address a technique in [ATT&CK](https://attack.mitre.org).
- Although we are unable to verify the truth of the submission, an analytic should only be shared if it has been used in an operational setting.
- An analytic must detect behaviors, not a specific artifact or nuance of a RAT or piece of malware. This is very important! A detection for a piece of malware that executes a technique is great, but not a fit for CAR. Consider [Sigma](https://github.com/Neo23x0/sigma).
- We reserve the right to add new criteria over time as the vetting process evolves.

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