---
title: "Thread"
---
A thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically part of the operating system. A thread is typically a component of a process. Multiple threads can exist within the same process and share resources such as memory, while different processes do not share these resources. The threads of a process share executable code instructions and context, such as the values of variables at any given moment.

## Actions
|Action|Description|
|---|---|
|create|The event corresponding to the act of creating a new thread.|
|remote_create|A subset of thread create events that correspond to thread injection, that is, when a process creates a thread in another process. For a remote_create event the src_pid and tgt_pid are different.|
|suspend|The event corresponding to the act of suspending a thread which is currently running.|
|terminate|The event corresponding to the act of terminating a running thread.|

## Fields
|Field|Description|Example|
|---|---|---|
hostname|The hostname of the active host, without the domain.|<code>HOST1</code>
src_pid|The process ID of the process that created the thread.|<code>6016</code>
src_tid|The thread ID of the thread that created the event.|<code>9012</code>
stack_base|The base address of the thread's stack.|<code>18446735827508301824</code>
stack_limit|The limit of the thread's stack.|<code>18446735827508277248</code>
start_address|The memory address at which the thread's execution starts.|<code>18446735827446645728</code>
start_function|The function at `start_address`.|<code>LoadLibrary</code>
start_module|The module in which `start_address` resides.|<code>C:\windows\system32\ntdll.dll</code>
start_module_name|The short name of the `start_module`.|<code>ntdll.dll</code>
tgt_pid|The process ID of the process in which the new thread runs.|<code>232</code>
tgt_tid|The thread ID of the new thread that was created.|<code>6964</code>
uid|The ID of SID of the user who directly or indirectly acted on the thread|<code>S-1-5-18</code>
user|The user context in which the source thread was running. May be a local, domain or SYSTEM user. Formatted as <DOMAIN>\<USER>. Because threads are allowed to impersonate users, this may be different than the user context of the process.|<code>HOST1\LOCALUSER</code>
user_stack_base|The base address of the thread's stack.|<code>0</code>
user_stack_limit|The limit of the thread's stack.|<code>0</code>

## Coverage Map
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