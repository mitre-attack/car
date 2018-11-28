---
title: "User Session"
---

User sessions are the user activities undertaken on the computer in the course of conducting standard user actions.

## Actions

|Action|Description|
|---|---|
|interactive|The event corresponding to the act of a user conducting a local login. The logon session used requires a GUI.
|local|The event corresponding to the act of a user logging on locally to the machine.
|lock|The event corresponding to the act of a user locking a machine such that they are still logged into the machine but unable to access it without re-entering credentials, effectively entering the machine into a locked state.
|login|The event corresponding to the act of a user logging into a machine.
|logout|The event corresponding to the act of a user logging out of a machine.
|rdp|The event corresponding to the act of a user accessing a machine remotely.
|reconnect|The event corresponding to the act of a user reconnecting when an RDP session disconnects but the user is not logged off.
|remote|The event corresponding to the act of a user conducting a network logon.
|unlock|The event corresponding to the act of a user unlocking a machine currently in a locked state.

## Fields

|Field|Description|Example|
|---|---|---|
|dest_ip|The destination IP address of the user session. Only applicable to remote or RDP sessions.|`192.168.1.5`
|dest_port|The destination port of the user session. Only applicable to remote or RDP sessions.|`1900`
|hostname|The hostname of the host, without the domain.|`HOST1`
|logon_id|A hex value corresponding to the session. The logon id will persist until logout occurs.|`0xf61f3`
|src_ip|The source IP address of the user session. Only applicable to remote or RDP sessions.|`10.0.0.54`
|src_port|The source port of the user session. Only applicable to remote or RDP sessions.|`50438`
|user|The user affiliated with the session. May be a local, domain or SYSTEM user.|`HOST1\LOCALUSER`

## Coverage Map

| | **dest_ip** | **dest_port** | **hostname** | **logon_id** | **src_ip** | **src_port** | **user** |
|---|---|---|---|---|---|---|---|
| **interactive** | | | | | | | |
| **local** | | | | | | | |
| **lock** | | | | | | | |
| **login** | | | | | | | |
| **logout** | | | | | | | |
| **rdp** | | | | | | | |
| **reconnect** | | | | | | | |
| **remote** | | | | | | | |
| **unlock** | | | | | | | |