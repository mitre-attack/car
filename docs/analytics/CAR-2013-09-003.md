---
title: "CAR-2013-09-003: SMB Session Setups"
layout: analytic
submission_date: 2013/09/12
information_domain: Network
subtypes: PCAP
analytic_type: Situational Awareness
contributors: MITRE
---

Account usage within SMB can be used to identify compromised credentials, and the hosts accessed with them.

This analytic monitors SMB activity that deals with user activity rather than file activity.

## ATT&CK Detection

|Technique |Tactic |Level of Coverage |
|---|---|---|
|[Forced Authentication](https://attack.mitre.org/techniques/T1187/)|[Credential Access](https://attack.mitre.org/tactics/TA0006/)|Low|

## Data Model References

|Object|Action|Field|
|---|---|---|
|[flow](../data_model/flow) | [message](../data_model/flow#message) | [dest_port](../data_model/flow#dest_port) |
|[flow](../data_model/flow) | [message](../data_model/flow#message) | [proto_info](../data_model/flow#proto_info) |
|[flow](../data_model/flow) | [message](../data_model/flow#message) | [protocol](../data_model/flow#protocol) |


## Implementations

### Pseudocode

```
flow = search Flow:Message
smb_setup = filter flow where (dest_port == 445 and protocol == smb.setup)
smb_setup.user = smb_write.proto_info.user_name
smb_setup.target_host = smb_write.proto_info.hostname
output smb_write
```

