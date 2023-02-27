---
title: "Data Model with Sensors"
---

The **Data Model**, strongly inspired by [CybOX](https://cyboxproject.github.io/), is an organization of the objects that may be monitored from a host-based or network-based perspective. Each object can be identified by two dimensions: its actions and fields. When paired together, the three-tuple of `(object, action, field)` act like a coordinate, and describe what properties and state changes of the object can be captured by a sensor.

Compare the data model's use in analytics that map to [ATT&CK](https://attack.mitre.org/).


## [authentication](authentication)

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

## [driver](driver)

<table>
  <tr>
    <th />
    <th>base_address</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>md5_hash</th>
    <th>module_name</th>
    <th>pid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
  </tr>
  <tr>
    <th>load</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
  <tr>
    <th>unload</th>
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

## [email](email)

<table>
  <tr>
    <th />
    <th>action_reason</th>
    <th>attachment_mime_type</th>
    <th>attachment_name</th>
    <th>attachment_size</th>
    <th>date</th>
    <th>dest_address</th>
    <th>dest_ip</th>
    <th>dest_port</th>
    <th>from</th>
    <th>message_body</th>
    <th>message_links</th>
    <th>message_type</th>
    <th>return_address</th>
    <th>server_relay</th>
    <th>smtp_uid</th>
    <th>src_address</th>
    <th>src_domain</th>
    <th>src_ip</th>
    <th>src_port</th>
    <th>subject</th>
    <th>to</th>
  </tr>
  <tr>
    <th>block</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>delete</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>deliver</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>quarantine</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>redirect</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>

## [file](file)

<table>
  <tr>
    <th />
    <th>company</th>
    <th>content</th>
    <th>creation_time</th>
    <th>extension</th>
    <th>file_name</th>
    <th>file_path</th>
    <th>fqdn</th>
    <th>gid</th>
    <th>group</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>link_target</th>
    <th>md5_hash</th>
    <th>mime_type</th>
    <th>mode</th>
    <th>owner</th>
    <th>owner_uid</th>
    <th>pid</th>
    <th>ppid</th>
    <th>previous_creation_time</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>acl_modify</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>create</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>delete</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>modify</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>read</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>timestomp</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>write</th>
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
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>

## [flow](flow)

<table>
  <tr>
    <th />
    <th>application_protocol</th>
    <th>content</th>
    <th>dest_fqdn</th>
    <th>dest_hostname</th>
    <th>dest_ip</th>
    <th>dest_port</th>
    <th>end_time</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>in_bytes</th>
    <th>network_direction</th>
    <th>out_bytes</th>
    <th>packet_count</th>
    <th>pid</th>
    <th>ppid</th>
    <th>proto_info</th>
    <th>src_fqdn</th>
    <th>src_hostname</th>
    <th>src_ip</th>
    <th>src_port</th>
    <th>start_time</th>
    <th>tcp_flags</th>
    <th>transport_protocol</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>end</th>
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
    <th>message</th>
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
    <th>start</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
</table>

## [http](http)

<table>
  <tr>
    <th />
    <th>hostname</th>
    <th>http_version</th>
    <th>request_body_bytes</th>
    <th>request_body_content</th>
    <th>request_referrer</th>
    <th>requester_ip_address</th>
    <th>response_body_bytes</th>
    <th>response_body_content</th>
    <th>response_status_code</th>
    <th>url_domain</th>
    <th>url_full</th>
    <th>url_remainder</th>
    <th>url_scheme</th>
    <th>user_agent_device</th>
    <th>user_agent_full</th>
    <th>user_agent_name</th>
    <th>user_agent_version</th>
  </tr>
  <tr>
    <th>get</th>
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
    <th>post</th>
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
    <th>put</th>
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
    <th>tunnel</th>
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

## [module](module)

<table>
  <tr>
    <th />
    <th>base_address</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>md5_hash</th>
    <th>module_name</th>
    <th>module_path</th>
    <th>pid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>tid</th>
  </tr>
  <tr>
    <th>load</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
  <tr>
    <th>unload</th>
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

## [process](process)

<table>
  <tr>
    <th />
    <th>access_level</th>
    <th>call_trace</th>
    <th>command_line</th>
    <th>current_working_directory</th>
    <th>env_vars</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>guid</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>integrity_level</th>
    <th>md5_hash</th>
    <th>parent_command_line</th>
    <th>parent_exe</th>
    <th>parent_guid</th>
    <th>parent_image_path</th>
    <th>pid</th>
    <th>ppid</th>
    <th>sha1_hash</th>
    <th>sha256_hash</th>
    <th>sid</th>
    <th>signature_valid</th>
    <th>signer</th>
    <th>target_address</th>
    <th>target_guid</th>
    <th>target_name</th>
    <th>target_pid</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>access</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>create</th>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
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
    <th>terminate</th>
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

## [registry](registry)

<table>
  <tr>
    <th />
    <th>data</th>
    <th>fqdn</th>
    <th>hive</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>key</th>
    <th>new_content</th>
    <th>pid</th>
    <th>type</th>
    <th>user</th>
    <th>value</th>
  </tr>
  <tr>
    <th>add</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
  </tr>
  <tr>
    <th>key_edit</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a>&#10<a href='../sensors/sysmon_13'>Sysmon</a></td>
  </tr>
  <tr>
    <th>remove</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>value_edit</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
  </tr>
</table>

## [service](service)

<table>
  <tr>
    <th />
    <th>command_line</th>
    <th>exe</th>
    <th>fqdn</th>
    <th>hostname</th>
    <th>image_path</th>
    <th>name</th>
    <th>pid</th>
    <th>ppid</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>create</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>delete</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/autoruns_13.98'>Autoruns</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>pause</th>
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
    <th>start</th>
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
    <th>stop</th>
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

## [socket](socket)

<table>
  <tr>
    <th />
    <th>family</th>
    <th>image_path</th>
    <th>local_address</th>
    <th>local_path</th>
    <th>local_port</th>
    <th>pid</th>
    <th>protocol</th>
    <th>remote_address</th>
    <th>remote_port</th>
    <th>success</th>
  </tr>
  <tr>
    <th>bind</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>close</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>listen</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/osquery_4.6.0'>osquery</a></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>

## [thread](thread)

<table>
  <tr>
    <th />
    <th>hostname</th>
    <th>src_pid</th>
    <th>src_tid</th>
    <th>stack_base</th>
    <th>stack_limit</th>
    <th>start_address</th>
    <th>start_function</th>
    <th>start_module</th>
    <th>start_module_name</th>
    <th>tgt_pid</th>
    <th>tgt_tid</th>
    <th>uid</th>
    <th>user</th>
    <th>user_stack_base</th>
    <th>user_stack_limit</th>
  </tr>
  <tr>
    <th>create</th>
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
    <th>remote_create</th>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"><a href='../sensors/sysmon_13'>Sysmon</a></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <th>suspend</th>
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
    <th>terminate</th>
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

## [user_session](user_session)

<table>
  <tr>
    <th />
    <th>dest_ip</th>
    <th>dest_port</th>
    <th>hostname</th>
    <th>login_id</th>
    <th>login_successful</th>
    <th>login_type</th>
    <th>src_ip</th>
    <th>src_port</th>
    <th>uid</th>
    <th>user</th>
  </tr>
  <tr>
    <th>lock</th>
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
    <th>login</th>
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
    <th>logout</th>
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
    <th>reconnect</th>
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
    <th>unlock</th>
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
