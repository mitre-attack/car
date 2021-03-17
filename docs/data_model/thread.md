---
title: "Thread"
---

A thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically part of the operating system. A thread is typically a component of a process. Multiple threads can exist within the same process and share resources such as memory, while different processes do not share these resources. The threads of a process share executable code instructions and context, such as the values of variables at any given moment.

## Actions

|Action|Description|
|---|---|
|create|The event corresponding to the act of creating a new thread.|
|suspend|The event corresponding to the act of suspending a thread which is currently running.|
|terminate|The event corresponding to the act of terminating a running thread.|
|remote_create|A subset of thread create events that correspond to thread injection, that is, when a process creates a thread in another process. For a remote_create event the src_pid and tgt_pid are different.|

## Fields

|Field|Description|Example|
|---|---|---|
|hostname|The hostname of the active host, without the domain.|`HOST1`|
|src_pid|The process ID of the process that created the thread.|`6016`|
|src_tid|The thread ID of the thread that created the event.|`9012`|
|stack_base|The base address of the thread’s stack.|`0xfffff880081a9000`|
|stack_limit|The limit of the thread’s stack.|`0xfffff880081a3000`|
|start_address|The memory address at which the thread's execution starts.|`0xfffff880046dc3e0`|
|start_function|The function at `start_address`|`LoadLibrary`|
|start_module|The module in which `start_address` resides.|`C:\windows\system32\ntdll.dll`|
|start_module_name|The short name of the `start_module.`|`ntdll.dll`|
|subprocess_tag|Identifies the service if the thread is owned by a service; otherwise, it is listed as zero.|`0`|
|tgt_pid|The process ID of the process in which the new thread runs.|`4`|
|tgt_tid|The thread ID of the new thread that was created.|`6964`|
|uid|The ID or SID of the user who directly or indirectly acted on the thread.|`S-1-5-18`|
|user|The user context in which the source thread was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process.|`HOST1\LOCALUSER`|
|user_stack_base|The base address of the thread’s stack.|`0x0`|
|user_stack_limit|The limit of the thread’s stack.|`0x0`|

## Coverage Map

| | **hostname** | **src_pid** | **src_tid** | **stack_base** | **stack_limit** | **start_address** | **start_function** | **start_module** | **start_module_name** | **subprocess_tag** | **tgt_pid** | **tgt_tid** | **uid** | **user** | **user_stack_base** | **user_stack_limit** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **create** | | | | | | | | | | | | | | | | |
| **remote_create** | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | |[Sysmon]( ../sensors/sysmon_13) |[Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | [Sysmon]( ../sensors/sysmon_13) | | |
| **suspend** | | | | | | | | | | | | | | | | | |
| **terminate** | | | | | | | | | | | | | | | | |
