# getrlimit(2)

`getrlimit` — 控制系统资源最大消耗量

## 名称

`getrlimit`, `setrlimit`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/time.h>`

`#include <sys/resource.h>`

```c
int
getrlimit(int resource, struct rlimit *rlp);

int
setrlimit(int resource, const struct rlimit *rlp);
```

## 描述

当前进程及其创建的每个进程对系统资源的消耗限制可通过 `getrlimit()` 系统调用获取，并通过 `setrlimit()` 系统调用设置。

`resource` 参数为以下之一：

**`RLIMIT_AS`** 进程允许映射的虚拟内存最大量（以字节为单位）。

**`RLIMIT_CORE`** 可创建的 [core(5)](../man5/core.5.md) 文件的最大尺寸（以字节为单位）。

**`RLIMIT_CPU`** 每个进程可使用的最大 CPU 时间（以秒为单位）。

**`RLIMIT_DATA`** 进程数据段的最大尺寸（以字节为单位）；这定义了程序可通过 sbrk(2) 函数将 break 扩展多远。

**`RLIMIT_FSIZE`** 可创建文件的最大尺寸（以字节为单位）。

**`RLIMIT_KQUEUES`** 此用户 ID 允许创建的 kqueue 最大数量。

**`RLIMIT_MEMLOCK`** 进程可通过 [mlock(2)](mlock.2.md) 系统调用锁定到内存中的最大尺寸（以字节为单位）。

**`RLIMIT_NOFILE`** 此进程打开文件的最大数量。

**`RLIMIT_NPROC`** 此用户 ID 同时存在的进程最大数量。

**`RLIMIT_NPTS`** 此用户 ID 允许创建的伪终端最大数量。

**`RLIMIT_PIPEBUF`** 此用户 ID 允许占用的双向管道/FIFO 内核缓冲区最大总量。在首次打开由 ([mkfifo(2)](mkfifo.2.md)) 创建的文件系统对象时所创建的内核 FIFO 缓冲区，也会计入打开该对象的进程的用户 ID，而非 FIFO 的文件系统所有者。尽管这有些出人意料，但实际上是公平的，因为 fifo 的使用者并不必然是其创建者。

**`RLIMIT_RSS`** 当存在内存压力且有交换空间可用时，优先回收进程常驻页面中超出此数量（以字节为单位）的部分。当内存不存在压力时，此 rlimit 实际上被忽略。超过所设置 `RLIMIT_RSS` 的进程不会被发送信号或停止。该限制仅仅是向 VM 守护进程提供一个提示，使其优先停用超过所设置 `RLIMIT_RSS` 的进程的页面。

**`RLIMIT_SBSIZE`** 此用户套接字缓冲区使用的最大尺寸（以字节为单位）。这限制了此用户在任意时刻可持有的网络内存量，进而限制 mbuf 的数量。

**`RLIMIT_STACK`** 进程栈段的最大尺寸（以字节为单位）；这定义了程序的栈段可扩展多远。栈扩展由系统自动执行。

**`RLIMIT_SWAP`** 此用户 ID 的所有进程可预留或使用的交换空间最大尺寸（以字节为单位）。仅当 `vm.overcommit` sysctl 的第 1 位被设置时，此限制才被强制执行。有关此 sysctl 的完整描述，请参见 [tuning(7)](../man7/tuning.7.md)。

**`RLIMIT_UMTXP`** 用户 ID 分配的进程共享 POSIX 线程库对象数量限制。

**`RLIMIT_VMEM`** `RLIMIT_AS` 的别名。

资源限制以软限制和硬限制形式指定。当软限制被超出时，进程可能收到也可能不会收到信号。例如，当超出 CPU 时间或文件大小时会生成信号，但超出地址空间或 RSS 限制时则不会。超过软限制的程序可继续执行，直到达到硬限制，或修改自身的资源限制。即使达到硬限制也未必会停止进程。例如，若超出 RSS 硬限制，不会发生任何事。

`rlimit` 结构用于指定资源的硬限制和软限制。

```c
struct rlimit {
	rlim_t	rlim_cur;	/* 当前（软）限制 */
	rlim_t	rlim_max;	/* rlim_cur 的最大值 */
};
```

只有超级用户可提高最大限制。其他用户只能在 0 到 `rlim_max` 范围内修改 `rlim_cur`，或（不可逆地）降低 `rlim_max`。

限制的“无限”值定义为 `RLIM_INFINITY`。

由于此信息存储在每进程信息中，若要影响 shell 创建的所有未来进程，此系统调用必须由 shell 直接执行；因此 `limit` 是 [csh(1)](../man1/csh.1.md) 的内建命令。

当限制在正常方式下会被超出时，系统拒绝扩展数据或栈空间：若达到数据空间限制，[brk(2)](brk.2.md) 函数会失败。当达到栈限制时，进程收到段错误（`SIGSEGV`）；若使用信号栈的处理程序未捕获此信号，此信号将杀死进程。

文件 I/O 操作若会创建大于进程软限制的文件，将导致写操作失败并生成 `SIGXFSZ` 信号；这通常会终止进程，但可被捕获。当超出软 CPU 时间限制时，向违规进程发送 `SIGXCPU` 信号。

当大多数操作会分配超过 `RLIMIT_AS` 软限制所允许的虚拟内存时，操作以 `ENOMEM` 失败，且不引发信号。一个值得注意的例外是上述栈扩展。如果栈扩展会分配超过 `RLIMIT_AS` 软限制所允许的虚拟内存，将发送 `SIGSEGV` 信号。调用者可自由地将软地址空间限制提高到硬限制并重试分配。

## 返回值

成功完成后返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`getrlimit()` 和 `setrlimit()` 系统调用将在以下情况下失败：

**[`EFAULT`]** 为 `rlp` 指定的地址无效。

**[`EPERM`]** 为 `setrlimit()` 指定的限制会提高最大限制值，且调用者不是超级用户。

## 参见

[csh(1)](../man1/csh.1.md), quota(1), [quotactl(2)](quotactl.2.md), [sigaction(2)](sigaction.2.md), [sigaltstack(2)](sigaltstack.2.md), [sysctl(3)](../man3/sysctl.3.md), [ulimit(3)](../man3/ulimit.3.md)

## 历史

`getrlimit()` 系统调用出现于 4.2BSD。
