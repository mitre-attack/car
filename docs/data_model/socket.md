---
title: "Socket"
---

Socket events are low-level events that may or may not result in a flow. Socket listening events in particular can be helpful in detecting malicious activity.

## Actions

|Action|Description|
|---|---|
|bind|The event corresponding to a socket binding to a specific address.
|listen|The event corresponding to a socket being opened into a listening status, usually on a specific local port.|
|close|The event corresponding to a socket being closed.|

## Fields

|Field|Description|Example|
|---|---|---|
|family|The type of socket in question.|`AF_UNIX, AF_INET, AF_INET6`|
|image_path|Path to the executable that initiated the socket event.|`C:/user/adam/malware.exe`|
|local_address|IP address on which the socket will accept connections; does not include the port number.|`10.0.211.200`|
|local_path|In the case that a socket is used for local interprocess communication, the socket binds to a local filepath, and will usually be visible in the filesystem. This is the case with AF_UNIX type sockets.|`/tmp/foo`|
|local_port|Port number on which the socket is bound at the local end. This pertains to TCP and UDP sockets but not IP sockets.|`48777`|
|pid|ID of the process that acted on the socket.|`3930`|
|protocol|The type of connection that was attempted on the socket.|`TCP`|
|remote_address|IP address with which the socket is communicating on the remote end.|`199.121.21.20`|
|remote_port|Port number on which the socket is bound at the remote end.|`559`|
|success|Boolean indicator of whether the socket event was successful (e.g. the socket was created as requested).|`True`|

## Coverage Map

| | **family** | **image_path** | **local_address** | **local_path** | **local_port** | **pid** | **protocol** | **remote_address** | **remote_port** | **success** |
|---|---|---|---|---|---|---|---|---|---|---|
| **bind** | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | |
| **listen** | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | |
| **close** | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | o[osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | [osquery](../sensors/osquery_4.6.0) | |

