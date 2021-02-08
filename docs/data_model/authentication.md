---
title: "Authentication"
---

An authentication event occurs whenever a user or process attempts to access a privileged system resource. Examples include logging into a system, or elevating privilege.

## Actions

|Action|Description|
|---|---|
|failure|The event corresponding to an authentication service responding negatively to an authentication request.
|error|The event corresponding to the case when an authentication requests results in an any kind of unexpected error.
|success|The event corresponding to an authentication service responding positively to an authentication request.

## Fields

|Field|Description|Example|
|---|---|---|
ad_domain|Active Directory domain from which the authentication request was generated; may differ from the target_ad_domain.|`ad2.mitre.org`|
app_name|Name of the application that made the authentication request.|`ssh, win:local`|
auth_service|The name of the service that was utilized to accomplish authentication.|`Okta, ActiveDirectory`|
auth_target|machine for which authentication was requested; may be different than the host that the request is made from.|`HOST2`|
decision_reason|The justification for approving or denying an authentication request.|`password is invalid`|
fqdn|The fully qualified domain name for the host from which authentication was requested.|`HOST1.mitre.org`|
hostname|Hostname of the host from which authentication was requested.|`HOST1`|
method|The authentication method that was used.|`SMAL, Kerberos`|
response_time|Duration of time it took for an authentication response to be received.|`12ms`|
target_ad_domain|The Active Directory domain within which authentication was requested.|`ad.mitre.org`|
target_uid|User ID or SID for the user being authenticated.|`S-1-5-19`|
target_user|Name of the user being authenticated; this only pertains to privilage escalation events where the current user is not necessarily the same as the target user.|`HOST1\LOCALUSER2`|
target_user_role|IPAM access control role for the user being authenticated; this only pertains to privilege escalation events where the current user is not necessarily the same as the target user.|`System Administrator Role`|
target_user_type|User ID or SID for the user being authenticated.|`Administrator, Standard, Guest`|
uid|User ID for the process that initiated the authentication request.|`S-1-5-18`|
user|Name of the user that initiated the request.|`HOST1\LOCALUSER1`|
user_agent|The user agent through which the request was made.|`aws-cli/2.0.0 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0dev4`|
user_role|IPAM access control role for the user that initiated the authentication request.|`DNS Record Administrator Role`|
user_type|type of user that initiated the request.|`Administrator, Standard, Guest`|

## Coverage Map

| | **ad_domain** | **app_name** | **auth_service** | **auth_target** | **decision_reason** | **fqdn** | **hostname** | **method** | **response_time** | **target_ad_domain** | **target_uid** | **target_user** | **target_user_role** | **target_user_type** | **uid** | **user** | **user_agent** | **user_role** | **user_type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **failure** | | | | | | | | | | | | | | | | | | | |
| **error** | | | | | | | | | | | | | | | | | | | |
| **success** | | | | | | | | | | | | | | | | | | | |
