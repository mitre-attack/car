---
title: "User Session"
---

User sessions are the user activities undertaken on the computer in the course of conducting standard user actions.

## Actions

|Action|Description|
|---|---|
|lock|The event corresponding to the act of a user locking a machine such that they are still logged into the machine but unable to access it without re-entering credentials, effectively entering the machine into a locked state.
|login|The event corresponding to the act of a user logging into a machine.
|logout|The event corresponding to the act of a user logging out of a machine.
|reconnect|The event corresponding to the act of a user reconnecting when an RDP session disconnects but the user is not logged off.
|unlock|The event corresponding to the act of a user unlocking a machine currently in a locked state.

## Fields

|Field|Description|Example|
|---|---|---|
|dest_ip|The destination IP address of the user session. Only applicable to remote or RDP sessions.|`192.168.1.5`
|dest_port|The destination port of the user session. Only applicable to remote or RDP sessions.|`1900`
|hostname|The hostname of the host, without the domain.|`HOST1`
|login_successful|Boolean indicator of whether a login attempt was successful.|`False`
|login_type|The type of login that was accomplished or attempted.|`interactive`,`local`,`rdp`,`remote`
|login_id|A hex value corresponding to the session. The login id will persist until logout occurs.|`0xf61f3`
|src_ip|The source IP address of the user session. Only applicable to remote or RDP sessions.|`10.0.0.54`
|src_port|The source port of the user session. Only applicable to remote or RDP sessions.|`50438`
|uid|ID or SID of the user for which a session event occured.|`S-1-5-18`
|user|The user affiliated with the session. May be a local, domain or SYSTEM user.|`HOST1\LOCALUSER`

## Coverage Map

| | **dest_ip** | **dest_port** | **hostname** | **login_successful** | **login_type** | **logon_id** | **src_ip** | **src_port** | **uid** | **user** |
|---|---|---|---|---|---|---|---|---|---|---|
| **lock** | | | | | | | | | | |
| **login** | | | | | | | | | | |
| **logout** | | | | | | | | | | |
| **reconnect** | | | | | | | | | | |
| **unlock** | | | | | | | | | | |
