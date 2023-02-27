---
title: "Authentication"
---
An authentication event occurs whenever a user or process attempts to access a privileged system resource. Examples include logging into a system, or elevating privilege.

## Actions
|Action|Description|
|---|---|
|error|The event corresponding to the case when an authentication request results in any kind of unexpected error.|
|failure|The event corresponding to an authentication service responding negatively to an authentication request.|
|success|The event corresponding to an authentication service responding positively to an authentication request.|

## Fields
|Field|Description|Example|
|---|---|---|
ad_domain|Active Directory domain from which the authentication request was generated; may differ from the target_ad_domain.|<code>ad2.mitre.org</code>
app_name|Name of the application that made the authentication request|<code>ssh, win:local</code>
auth_service|The name of the service that was utilized to accomplish authentication|<code>Okta, ActiveDirectory</code>
auth_target|machine for which authentication was requested; may be different than the host that the request is made from.|<code>HOST2</code>
decision_reason|The justification for approving or denying an authentication request.|<code>password is invalid</code>
fqdn|The fully qualified domain name for the host from which authentication was requested.|<code>HOST1.mitre.org</code>
hostname|Hostname of the host from which authentication was requested.|<code>HOST1</code>
method|The authentication method that was used.|<code>SMAL, Kerberos</code>
response_time|Duration of time it took for an authentication response to be received.|<code>12ms</code>
target_ad_domain|The Active Directory domain within which authentication was requested.|<code>ad.mitre.org</code>
target_uid|User ID for the user being authenticated.|<code>S-1-5-19</code>
target_user|Name of the user being authenticated; this only pertains to privilage escalation events where the current user is not necessarily the same as the target user.|<code>HOST1\LOCALUSER2</code>
target_user_role|IPAM access control role for the user being authenticated; this only pertains to privilege escalation events where the current user is not necessarily the same as the target user.|<code>System Administrator Role</code>
target_user_type|type of user that was authenticated; this only pertains to privilege escalation events where the current user is not necessarily the same as the target user.|<code>Administrator, Standard, Guest</code>
uid|User ID for the process that initiated the authentication request.|<code>S-1-5-18</code>
user|Name of the user that initiated the request.|<code>HOST1\LOCALUSER1</code>
user_agent|The user agent through which the request was made.|<code>aws-cli/2.0.0 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0dev4</code>
user_role|IPAM access control role for the user that initiated the authentication request.|<code>DNS Record Administrator Role</code>
user_type|type of user that initiated the request.|<code>Administrator, Standard, Guest</code>

## Coverage Map
<table>
  <tr>
    <th />
    <th>ad_domain</th>
    <th>app_name</th>
    <th>auth_service</th>
    <th>auth_target</th>
    <th>decision_reason</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>method</th>
    <th>response_time</th>
    <th>target_ad_domain</th>
    <th>target_uid</th>
    <th>target_user</th>
    <th>target_user_role</th>
    <th>target_user_type</th>
    <th>uid</th>
    <th>user</th>
    <th>user_agent</th>
    <th>user_role</th>
    <th>user_type</th>
  </tr>
  <tr>
    <th>error</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>failure</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>success</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>