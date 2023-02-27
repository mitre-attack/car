---
title: "Email"
---
Email events are at the mail server level.

## Actions
|Action|Description|
|---|---|
|block|The event corresponding to an email being blocked by the email server.|
|delete|The event corresponding to an email being deleted.|
|deliver|The event corresponding to an email being sent to an end recipient.|
|quarantine|The event corresponding to an email being quarantined for security reasons.|
|redirect|The event corresponding to an email being redirected.|

## Fields
|Field|Description|Example|
|---|---|---|
action_reason|The rationale given for blocking, redirecting, or quarantining an email.|<code>Malformed Message</code>
attachment_mime_type|The MIME type of the attachment.|<code>.docx</code>
attachment_name|Filename of any email attachment that may exist.|<code>cuddly-cats.pdf</code>
attachment_size|Filesize of the attachment.|<code>567 Kb</code>
date|SMTP date header, which is actually a date time group.|<code>Thu Jul 18 09:30:00 PDT 2019</code>
dest_address|Recipient email address, taken from the SMTP "Recipient" field.|<code>adam@example.com</code>
dest_ip|The destination IP address for the email.|<code>221.174.222.111</code>
dest_port|The destination port for the email.|<code>993</code>
from|Displayed sender name from the Message Information header; can be easily forged.|<code>eve@trusted-advisors.com</code>
message_body|Content of the email, not including subject.|<code>Hello World</code>
message_links|URLs extracted from the email body.|<code>https://www.cnn.com</code>
message_type|Content protocol of the message body|<code>html</code>
return_address|Email address to which replies should be sent, also known as Return-Path or Reply-To; may differ from the src_address.|<code>eve_secondary@example.com</code>
server_relay|The Received portion of the SMTP header, which provides the chain of hosts that the email passed through during delivery; each link usually contains an IP address, domain, and datetime group.|
smtp_uid|Distint ID used to distinguish emails.|<code>MN2PR09MB4876CCE7F183A83E6BA1C4C1CBF50@PP34399.prod.outlook.com</code>
src_address|Email address of the sender, taken from the "Sender" SMTP field.|<code>eve@example.com</code>
src_domain|The domain portion of the src_address.|<code>example.com</code>
src_ip|Originating IP address.|<code>172.183.195.200</code>
src_port|Originating port.|<code>1248</code>
subject|Subject line of the email.|<code>Lo0k Younger Whl1e L0slng We19ht!!</code>
to|the content of the To field in the email header; does not necessarily match up with real recipients.|<code>adam@example.com</code>

## Coverage Map
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