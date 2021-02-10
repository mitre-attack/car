---
title: "Email"
---

Email events are at the mail server level.

## Actions

|Action|Description|
|---|---|
|block|The event corresponding to an email being blcoked by the email server.
|delete|The event corresponding to an email being deleted.
|deliver|The event corresponding to an email being sent to an end recipient.
|redirect|The event corresponding to an email being redirected.
|quarantine|The event corresponding to an email being qurantined for security reasons.
## Fields

|Field|Description|Example|
|---|---|---|
action_reason|The rationale given for blocking, redirecting, or quarantining an email.|`Malformed Message`|
attachment_mime_type|The MIME type of the attachment.|`.docx`|
attachment_name|Filename of any email attachment that may exist.|`cuddly-cats.pdf`|
attachment_size|Filesize of the attachment.|`567 Kb`|
date|SMTP date header, which is actually a date time group.|`Thu Jul 18 09:30:00 PDT 2019`|
dest_address|Recipient email address, taken from the SMTP "Recipient" field.|`adam@example.com`|
dest_ip|The destination IP address for the email.|`221.174.222.111`|
dest_port|The destination port for the email.|`993`|
from|Displayed sender name from the Message Information header; can be easily forged.|`eve@trusted-advisors.com`|
message_body|Content of the email, not including subject.|`Hello World`|
message_links|URLs extracted from the email body.|`https://www.cnn.com`|
message_type|Content protocol of the message body|`html`|
return_address|Email address to which replies should be sent, also known as Return-Path or Reply-To; may differ from the src_address.|`eve_secondary@example.com`|
server_relay|The Received portion of the SMTP header, which provides the chain of hosts that the email passed through during delivery; each link usually contains an IP address, domain, and datetime group.||
smtp_uid|Distinct ID used to distingquish emails.|`MN2PR09MB4876CCE7F183A83E6BA1C4C1CBF50@PP34399.prod.outlook.com`|
src_address|Email address of the sender, taken from the "Sender" SMTP field.|`eve@example.com`|
src_domain|The domain portion of the src_address.|`example.com`|
src_ip|Originating IP address.|`172.183.195.200`|
src_port|Originating port.|`1248`|
subject|Subject line of the email.|`Lo0k Younger Whl1e L0slng We19ht!!`|
to|The content of the To field in the email header; does not necessarily match up with real recipients.|`adam@example.com`|

## Coverage Map

| | **action_reason** | **attachment_mime_type** | **attachment_name** | **attachment_size** | **date** | **dest_address** | **dest_ip** | **dest_port** | **from** | **message_body** | **message_links** | **message_type** | **return_address** | **server_relay** | **smtp_uid** | **src_address** | **src_domain** | **src_ip** | **src_port** | **subject** | **to** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--|--|
| **block** | | | | | | | | | | | | | | | | | | | | | |
| **delete** | | | | | | | | | | | | | | | | | | | | | |
| **deliver** | | | | | | | | | | | | | | | | | | | | | |
| **redirect** | | | | | | | | | | | | | | | | | | | | | |
| **quarantine** | | | | | | | | | | | | | | | | | | | | | |
