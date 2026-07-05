# capsicum.4

`Capsicum` — 轻量级 OS 能力与沙箱框架

## 名称

`Capsicum`

## 概要

`options CAPABILITY_MODE options CAPABILITIES`

## 描述

`Capsicum` 是一个轻量级 OS 能力和沙箱框架，实现了混合能力系统模型。`Capsicum` 旨在将能力与 UNIX 融合。此方法在保留现有 UNIX API 和性能的同时，实现了许多最小权限操作的好处，并为应用程序作者提供了面向能力设计的采用路径。

能力是不可伪造的权限令牌，可以委托，必须呈现才能执行操作。`Capsicum` 将文件描述符变为能力。

`Capsicum` 可用于应用程序和库的 compartmentalisation，即将较大的软件体分解为隔离（沙箱化）的组件，以实现安全策略并限制软件漏洞的影响。

`Capsicum` 提供两个核心内核原语：

**capability** mode 一种进程模式，通过调用 cap_enter(2) 进入，在此模式下对全局 OS 命名空间（如文件系统和 PID 命名空间）的访问受到限制；只有显式委托的、由内存映射或文件描述符引用的权限才能使用。一旦设置，该标志由未来的子进程继承，且无法清除。能力模式下对系统调用的访问受限：某些需要全局命名空间访问的系统调用不可用，而其他一些则受到约束。例如，sysctl(2) 可用于查询进程本地信息（如地址空间布局），也可用于监视系统的网络连接。sysctl(2) 通过显式标记（~~在超过 15000 个参数中约 60 个）为能力模式下允许的参数来约束；所有其他参数都被拒绝。需要约束的系统调用有 sysctl(2)、shm_open(2)（允许创建匿名内存对象但不允许命名对象）以及 openat(2) 系列系统调用。openat(2) 调用已接受一个文件描述符参数作为执行 open(2)、rename(2) 等操作的目录；在能力模式下，openat(2) 系列系统调用受到约束，使其只能操作“under”所提供文件描述符的对象。

**capabilities** 限制可在文件描述符上调用的操作。例如，由 open(2) 返回的文件描述符可使用 cap_rights_limit(2) 进行细化，使得只能调用 read(2) 和 write(2)，而不能调用 fchmod(2)。完整的能力权限列表可在 [rights(4)](rights.4.md) 手册页中找到。

在某些情况下，`Capsicum` 需要使用传统 POSIX API 的替代方案，以便使用能力而非全局命名空间来命名对象：

**process** descriptors 表示进程的文件描述符，允许父进程管理子进程而无需访问 PID 命名空间；在 [procdesc(4)](procdesc.4.md) 中有更详细的描述。

**anonymous** shared memory POSIX 共享内存 API 的扩展，支持与文件描述符关联的匿名交换对象；在 shm_open(2) 中有更详细的描述。

在某些情况下，`Capsicum` 限制传统 API 的某些参数的有效值，以限制对全局命名空间的访问：

**process** IDs 进程只能使用 cpuset_setaffinity(2) 等系统调用对自己的进程 ID 进行操作。

FreeBSD 提供了一些额外功能以支持应用程序沙箱，这些功能不是 `Capsicum` 本身的一部分：

**capsicum_helpers(3)** 一组内联函数，简化了修改程序以使用 `Capsicum` 的过程。

**libcasper(3)** 一个为沙箱化应用程序提供服务的库，例如操作命令行上指定的文件或建立网络连接。

## 参见

cap_enter(2), cap_fcntls_limit(2), cap_getmode(2), cap_ioctls_limit(2), cap_rights_limit(2), fchmod(2), open(2), pdfork(2), pdgetpid(2), pdkill(2), pdwait4(2), read(2), shm_open(2), write(2), cap_rights_get(3), capsicum_helpers(3), libcasper(3), [procdesc(4)](procdesc.4.md)

## 历史

`Capsicum` 首次出现于 FreeBSD 9.0，由剑桥大学开发。

## 作者

`Capsicum` 由剑桥大学的 Robert Watson <rwatson@FreeBSD.org> 和 Jonathan Anderson <jonathan@FreeBSD.org>、Google, Inc. 的 Ben Laurie <benl@FreeBSD.org> 和 Kris Kennaway <kris@FreeBSD.org> 以及 Pawel Jakub Dawidek <pawel@dawidek.net> 开发。本手册页的部分内容取材于

> Robert N. M. Watson, Jonathan Anderson, Ben Laurie, Kris Kennaway, "Capsicum: practical capabilities for UNIX", *USENIX Security Symposium*, August 2010, DOI: 10.5555/1929820.1929824。
