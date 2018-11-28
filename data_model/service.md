# Data Model: service
Services, or a service application, can be started automatically at system boot, by a user through the services control panel applet, or by an application that uses service functions. Services can execute even when no user is logged into the system.

## Actions
### create
The event corresponding to the act of creating a new service.

### delete
The event corresponding to the act of deleting a service.

### pause
The event corresponding to the act of pausing a currently running service.

### start
The event corresponding to the act of starting a new service.

### stop
The event corresponding to the act of stopping a service that is currently running.

## Fields

### command_line
The command line that service is started with.
 - `C:\windows\system32\svchost.exe -k rpcss`

### exe
The executable for the service.
 - `svchost.exe`

### fqdn
The fully qualified domain name of the host. Contains the hostname appended with the domain.
 - `Example: HOST1.EXAMPLE_DOMAIN.COM`

### hostname
The hostname of the host, without the domain.
 - `HOST1`

### image_path
Where in the file system the executable is located.
 - `C:\path\to\example.exe`

### name
The name of the service.
 - `RpcSs`

### ppid
The process ID of the process's parent, represented in decimal notation. In the parent process, this will be the pid field.
 - `1860`

### pid
The process ID for the process, represented in decimal notation.
 - `738`

### user
The user context in which the thread that caused this event was running. May be a local, domain or SYSTEM user. Formatted as "\<DOMAIN\>\\\<USER>". Because threads are allowed to impersonate users, this may be different than the user context of the process. For service events, the user is almost always NT AUTHORITY\SYSTEM.
 - `NT AUTHORITY\SYSTEM`

## Coverage Map

| | **command_line** | **exe** | **fqdn** | **hostname** | **image_path** | **name** | **pid** | **ppid** | **user** |
|---|---|---|---|---|---|---|---|---|---|
| **create** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | | |
| **delete** | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | [Autoruns](https://car.mitre.org/wiki/Autoruns) | | | |
| **pause** | | | | | | | | | |
| **start** | | | | | | | | | |
| **stop** | | | | | | | | | |