# fcntl(2)

`fcntl` — 文件控制

## 名称

`fcntl`

## 库

Lb libc

## 概要

`#include <fcntl.h>`

```c
int
fcntl(int fd, int cmd, ...);
```

## 描述

`fcntl()` 系统调用提供对描述符的控制。参数 `fd` 是由 `cmd` 操作的描述符，如下所述。根据 `cmd` 的值，`fcntl()` 可以接受额外的第三个参数 `arg`。除非下面针对特定操作另有说明，`arg` 的类型为 `int`。

- 大于或等于 `arg` 的最小可用描述符编号。
- 与原始描述符相同的对象引用。
- 如果对象是文件，新描述符共享相同的文件偏移量。
- 相同的访问模式（读、写或读/写）。
- 相同的文件状态标志（即两个文件描述符共享相同的文件状态标志）。
- 与新文件描述符关联的 close-on-exec 标志 `FD_CLOEXEC` 被清除，因此文件描述符在 [execve(2)](execve.2.md) 系统调用期间保持打开。
- 与新文件描述符关联的 close-on-fork 标志 `FD_CLOFORK` 被清除，因此文件描述符在 [fork(2)](fork.2.md) 系统调用期间保持打开。
- 下文描述的 `FD_RESOLVE_BENEATH` 标志，如果在原始描述符上已设置，则会被设置。

```c
dup2(fd, arg)
```

**`FD_CLOEXEC`** 在执行 exec() 时文件将被关闭（`arg` 被忽略）。否则，文件描述符保持打开。

**`FD_CLOFORK`** 在执行 fork() 系列系统调用时文件将被关闭。

**`FD_RESOLVE_BENEATH`** 相对于该文件描述符的所有路径名查找行为如同查找具有 `O_RESOLVE_BENEATH` 或 `AT_RESOLVE_BENEATH` 语义。不允许对此类文件描述符调用 fchdir(2) 或 fchroot(2)。`FD_RESOLVE_BENEATH` 标志是粘性的，意味着它会被 [dup(2)](dup.2.md) 及类似操作保留，并且使用 openat(2) 打开目录时如果目录描述符设置了此标志，新目录描述符也会设置此标志。

**`F_DUPFD`** 按如下方式返回新描述符：

**`F_DUPFD_CLOEXEC`** 类似于 `F_DUPFD`，但与新文件描述符关联的 `FD_CLOEXEC` 标志被设置，因此文件描述符在 [execve(2)](execve.2.md) 系统调用执行时关闭。

**`F_DUPFD_CLOFORK`** 类似于 `F_DUPFD`，但与新文件描述符关联的 `FD_CLOFORK` 标志被设置，因此文件描述符在 [fork(2)](fork.2.md) 系统调用执行时关闭。

**`F_DUP2FD`** 功能上等同于

**`F_DUP2FD_CLOEXEC`** 类似于 `F_DUP2FD`，但与新文件描述符关联的 `FD_CLOEXEC` 标志被设置。`F_DUP2FD` 和 `F_DUP2FD_CLOEXEC` 常量不可移植，因此如果需要可移植性则不应使用。使用 `dup2()` 代替 `F_DUP2FD`。

**`F_DUP3FD`** 用于实现 `dup3()` 调用。不要使用它。

**`F_GETFD`** 获取与文件描述符 `fd` 关联的标志。定义了以下标志：

**`F_SETFD`** 将与 `fd` 关联的标志设置为 `arg`。可用标志为 `FD_CLOEXEC`、`FD_CLOFORK` 和 `FD_RESOLVE_BENEATH`。`FD_RESOLVE_BENEATH` 标志一旦设置就无法清除。

**`F_GETFL`** 获取描述符状态标志，如下所述（`arg` 被忽略）。

**`F_SETFL`** 将描述符状态标志设置为 `arg`。

**`F_GETOWN`** 获取当前接收 `SIGIO` 和 `SIGURG` 信号的进程 ID 或进程组；进程组以负值返回（`arg` 被忽略）。

**`F_SETOWN`** 设置接收 `SIGIO` 和 `SIGURG` 信号的进程或进程组；进程组通过将 `arg` 指定为负值来指定，否则 `arg` 被解释为进程 ID。

**`F_READAHEAD`** 将顺序访问的预读量设置或清除为第三个参数 `arg`，该值向上取整到最近的块大小。`arg` 为零值关闭预读，为负值恢复系统默认值。

**`F_RDAHEAD`** 等同于 Darwin 对应功能，当第三个参数 `arg` 非零时设置 128KB 的预读量。`arg` 为零值关闭预读。

**`F_ADD_SEALS`** 如果底层文件系统支持密封，则向文件添加密封，如下所述。

**`F_GET_SEALS`** 如果底层文件系统支持密封，则获取与文件关联的密封。

**`F_ISUNIONSTACK`** 检查 vnode 是否是联合栈的一部分（来自 [mount(2)](mount.2.md) 的 “union” 标志或 unionfs）。这是一个 hack，不打算在 libc 之外使用。

**`F_KINFO`** 为指定文件描述符引用的文件填充 `struct kinfo_file`。`arg` 参数应指向 `struct kinfo_file` 的存储空间。传递的结构的 `kf_structsize` 成员必须用 `struct kinfo_file` 的 sizeof 初始化，以允许接口版本控制和演进。

`F_GETFL` 和 `F_SETFL` 命令的标志如下：

**`O_NONBLOCK`** 非阻塞 I/O；如果 [read(2)](read.2.md) 系统调用没有可用数据，或 [write(2)](write.2.md) 操作会阻塞，则读或写调用返回 -1 并带有 `EAGAIN` 错误。

**`O_APPEND`** 强制每次写入追加到文件末尾；对应于 [open(2)](open.2.md) 的 `O_APPEND` 标志。

**`O_DIRECT`** 最小化或消除读写的缓存效应。系统将尝试避免缓存你读或写的数据。如果无法避免缓存数据，将最小化数据对缓存的影响。如果不谨慎使用，此标志会大幅降低性能。

**`O_ASYNC`** 启用 `SIGIO` 信号，在 I/O 可用时（例如有可读数据时）发送到进程组。

**`O_SYNC`** 启用同步写入。对应于 [open(2)](open.2.md) 的 `O_SYNC` 标志。`O_FSYNC` 是 `O_SYNC` 的历史同义词。

**`O_DSYNC`** 启用同步数据写入。对应于 [open(2)](open.2.md) 的 `O_DSYNC` 标志。

可通过 `F_ADD_SEALS` 应用的密封如下：

**`F_SEAL_SEAL`** 阻止对文件应用任何进一步的密封。

**`F_SEAL_SHRINK`** 阻止通过 ftruncate(2) 缩小文件。

**`F_SEAL_GROW`** 阻止通过 ftruncate(2) 扩大文件。

**`F_SEAL_WRITE`** 阻止对文件的任何进一步 [write(2)](write.2.md) 调用。任何正在进行的写入将在 `fcntl()` 返回之前完成。如果存在任何可写映射，`F_ADD_SEALS` 将失败并返回 `EBUSY`。

密封基于每个 inode，需要底层文件系统的支持。如果底层文件系统不支持密封，`F_ADD_SEALS` 和 `F_GET_SEALS` 将失败并返回 `EINVAL`。

有几种操作可用于进行咨询文件锁定；它们都操作以下结构：

```c
struct flock {
	off_t	l_start;	/* 起始偏移量 */
	off_t	l_len;		/* len = 0 表示到文件末尾 */
	pid_t	l_pid;		/* 锁所有者 */
	short	l_type;		/* 锁类型：读/写等 */
	short	l_whence;	/* l_start 的类型 */
	int	l_sysid;	/* 远程系统 ID，本地为零 */
};
```

这些咨询文件锁定操作接受指向 `struct flock` 的指针作为第三个参数 `arg`。可用于咨询记录锁定的命令如下：

**`F_GETLK`** 获取第一个阻塞由第三个参数 `arg` 所指向的锁描述的锁，`arg` 作为指向 `struct flock` 的指针（见上文）。检索到的信息覆盖传递给 `fcntl()` 的 `flock` 结构中的信息。如果未找到会阻止创建此锁的锁，则该结构在此系统调用中保持不变，但锁类型被设置为 `F_UNLCK`。

**`F_SETLK`** 根据第三个参数 `arg` 所指向的锁描述设置或清除文件段锁，`arg` 作为指向 `struct flock` 的指针（见上文）。`F_SETLK` 用于建立共享（或读）锁（`F_RDLCK`）或独占（或写）锁（`F_WRLCK`），以及移除任一类型的锁（`F_UNLCK`）。如果无法设置共享或独占锁，`fcntl()` 立即返回 `EAGAIN`。

**`F_SETLKW`** 此命令与 `F_SETLK` 相同，区别在于如果共享或独占锁被其他锁阻塞，进程会等待直到请求可以被满足。如果在 `fcntl()` 等待区域时收到要捕获的信号，且信号处理程序未指定 `SA_RESTART`，则 `fcntl()` 将被中断（参见 [sigaction(2)](sigaction.2.md)）。

当在文件段上设置共享锁时，其他进程可以在该段或其部分上设置共享锁。共享锁阻止任何其他进程在受保护区域的任何部分设置独占锁。如果文件描述符未以读访问方式打开，则共享锁请求失败。

独占锁阻止任何其他进程在受保护区域的任何部分设置共享锁或独占锁。如果文件未以写访问方式打开，则独占锁请求失败。

`l_whence` 的值为 `SEEK_SET`、`SEEK_CUR` 或 `SEEK_END`，分别表示相对偏移量 `l_start` 字节将从文件开头、当前位置或文件末尾开始计算。`l_len` 的值是要锁定的连续字节数。如果 `l_len` 为负，`l_start` 表示区域的结束边。`l_pid` 和 `l_sysid` 字段仅与 `F_GETLK` 一起使用，用于返回持有阻塞锁的进程的进程 ID 和拥有该进程的系统的系统 ID。本地系统创建的锁的系统 ID 为零。在成功的 `F_GETLK` 请求后，`l_whence` 的值为 `SEEK_SET`。

锁可以始于并延伸超过文件当前末尾，但不能始于或延伸到文件开头之前。如果 `l_len` 设置为零，锁被设置为延伸到该文件偏移量的最大可能值。如果 `l_whence` 和 `l_start` 指向文件开头且 `l_len` 为零，则锁定整个文件。如果应用程序只想锁定整个文件，[flock(2)](flock.2.md) 系统调用效率更高。

文件中的每个字节最多设置一种类型的锁。在调用进程先前在请求指定区域的字节上存在锁的情况下，从 `F_SETLK` 或 `F_SETLKW` 请求成功返回之前，指定区域中每个字节的先前锁类型将被新锁类型替换。如上文共享锁和独占锁描述中所指定，当另一个进程在指定区域的字节上存在锁且这些锁的类型与请求中指定的类型冲突时，`F_SETLK` 或 `F_SETLKW` 请求分别失败或阻塞。

本地文件上 `F_SETLKW` 请求的排队是公平的；即当线程阻塞时，与其请求冲突的后续请求不会被授予，即使这些请求与现有锁不冲突。

此接口遵循 System V 和 -p1003.1-88 的完全愚蠢的语义，即当进程关闭该文件的 *任何* 文件描述符时，与该文件相关联的给定进程的所有锁都会被移除。此语义意味着应用程序必须了解子例程库可能访问的任何文件。例如，如果用于更新密码文件的应用程序在更新时锁定密码文件数据库，然后调用 getpwnam(3) 检索记录，锁将丢失，因为 getpwnam(3) 会打开、读取并关闭密码数据库。数据库关闭将释放进程与该数据库关联的所有锁，即使库例程从未请求数据库上的锁。此接口的另一个小语义问题是，使用 [fork(2)](fork.2.md) 系统调用创建的子进程不会继承锁。[flock(2)](flock.2.md) 接口具有更合理的最后关闭语义，并允许锁被子进程继承。对于希望在使用库例程时确保锁完整性或希望将锁传递给子进程的应用程序，推荐使用 [flock(2)](flock.2.md) 系统调用。

`fcntl()`、[flock(2)](flock.2.md) 和 [lockf(3)](../sys-1/lockf.3.md) 锁是兼容的。使用不同锁定接口的进程可以在同一文件上安全协作。但是，同一进程内只应使用这些接口中的一个。如果进程通过 [flock(2)](flock.2.md) 锁定文件，从使用 `fcntl()` 或 [lockf(3)](../sys-1/lockf.3.md) 的另一个进程的角度看，文件内的任何记录都将被视为已锁定，反之亦然。注意，如果持有阻塞锁的进程先前通过 [flock(2)](flock.2.md) 锁定了文件描述符，`fcntl()` `F_GETLK` 在 `l_pid` 中返回 -1。

进程终止时，与该进程关联的文件的所有锁都会被移除。

在调用 [execve(2)](execve.2.md) 之前获得的所有锁在新程序释放它们之前保持有效。如果新程序不知道这些锁，它们将不会被释放，直到程序退出。

如果控制锁定区域的进程因尝试锁定另一个进程的锁定区域而进入睡眠，则可能发生死锁。此实现检测到等待锁定区域解锁会导致死锁，并以 `EDEADLK` 错误失败。

## 返回值

成功完成时，返回值取决于 `cmd`，如下所示：

**`F_DUPFD`** 一个新的文件描述符。

**`F_DUP2FD`** 等于 `arg` 的文件描述符。

**`F_GETFD`** 标志的值。

**`F_GETFL`** 标志的值。

**`F_GETOWN`** 文件描述符所有者的值。

**其他** 非 -1 的值。

否则，返回值 -1，并设置 `errno` 以指示错误。

## 错误

`fcntl()` 系统调用在以下情况下会失败：

**[`EAGAIN`]** 参数 `cmd` 为 `F_SETLK`，锁类型（`l_type`）为共享锁（`F_RDLCK`）或独占锁（`F_WRLCK`），且要锁定的文件段已被另一个进程独占锁定；或类型为独占锁，且要锁定的文件段的某些部分已被另一个进程共享锁定或独占锁定。

**[`EBADF`]** `fd` 参数不是有效的打开文件描述符。参数 `cmd` 为 `F_DUP2FD`，且 `arg` 不是有效的文件描述符。参数 `cmd` 为 `F_SETLK` 或 `F_SETLKW`，锁类型（`l_type`）为共享锁（`F_RDLCK`），且 `fd` 不是为读打开的有效文件描述符。参数 `cmd` 为 `F_SETLK` 或 `F_SETLKW`，锁类型（`l_type`）为独占锁（`F_WRLCK`），且 `fd` 不是为写打开的有效文件描述符。

**[`EBUSY`]** 参数 `cmd` 为 `F_ADD_SEALS`，尝试设置 `F_SEAL_WRITE`，且文件存在可写映射。

**[`EDEADLK`]** 参数 `cmd` 为 `F_SETLKW`，且检测到死锁条件。

**[`EINTR`]** 参数 `cmd` 为 `F_SETLKW`，且系统调用被信号中断。

**[`EINVAL`]** `cmd` 参数为 `F_DUPFD` 且 `arg` 为负或大于最大允许数量（参见 [getdtablesize(2)](getdtablesize.2.md)）。参数 `cmd` 为 `F_GETLK`、`F_SETLK` 或 `F_SETLKW` 且 `arg` 指向的数据无效。参数 `cmd` 为 `F_ADD_SEALS` 或 `F_GET_SEALS`，且底层文件系统不支持密封。参数 `cmd` 无效。

**[`EMFILE`]** 参数 `cmd` 为 `F_DUPFD` 且进程允许的最大文件描述符数已在使用中，或没有大于或等于 `arg` 的文件描述符可用。

**[`ENOTTY`]** `fd` 参数对于请求的操作不是有效的文件描述符。如果 `fd` 是设备节点或 [kqueue(2)](kqueue.2.md) 返回的描述符，可能就是这种情况。

**[`ENOLCK`]** 参数 `cmd` 为 `F_SETLK` 或 `F_SETLKW`，且满足锁定或解锁请求将导致系统中锁定区域数超过系统施加的限制。

**[`EOPNOTSUPP`]** 参数 `cmd` 为 `F_GETLK`、`F_SETLK` 或 `F_SETLKW`，且 `fd` 引用的文件不支持锁定。

**[`EOVERFLOW`]** 参数 `cmd` 为 `F_GETLK`、`F_SETLK` 或 `F_SETLKW`，且 `off_t` 计算溢出。

**[`EPERM`]** `cmd` 参数为 `F_SETOWN` 且作为参数给出的进程 ID 或进程组与调用者不在同一会话。`cmd` 参数为 `F_ADD_SEALS` 且 `F_SEAL_SEAL` 密封已设置。

**[`ESRCH`]** `cmd` 参数为 `F_SETOWN` 且作为参数给出的进程 ID 未在使用中。

此外，如果 `fd` 引用的是终端设备上打开的描述符（而非套接字上打开的描述符），`F_SETOWN` 的 `cmd` 可能因与 [tcsetpgrp(3)](../gen/tcsetpgrp.3.md) 中相同的原因而失败，`F_GETOWN` 的 `cmd` 可能因 [tcgetpgrp(3)](../gen/tcgetpgrp.3.md) 中所述的原因而失败。

## 参见

[close(2)](close.2.md), dup2(2), [execve(2)](execve.2.md), [flock(2)](flock.2.md), [getdtablesize(2)](getdtablesize.2.md), [open(2)](open.2.md), [sigaction(2)](sigaction.2.md), [lockf(3)](../sys-1/lockf.3.md), [tcgetpgrp(3)](../gen/tcgetpgrp.3.md), [tcsetpgrp(3)](../gen/tcsetpgrp.3.md)

## 标准

`F_DUP2FD` 和 `F_DUP3FD` 常量不可移植。它们是为与 AIX 和 Solaris 兼容而提供的。

根据 -susv4，使用 `F_SETLKW` 的调用应在任何捕获的信号之后以 `EINTR` 失败，并应在线程挂起（如停止信号）期间继续等待。然而，在此实现中，使用 `F_SETLKW` 的调用在捕获到具有 `SA_RESTART` 处理程序的信号或线程挂起（如停止信号）后会重新启动。

## 历史

`fcntl()` 系统调用出现于 4.2BSD。

`F_DUP2FD` 常量首次出现于 FreeBSD 7.1。

`F_DUPFD_CLOFORK` 和 `F_DUP3FD` 标志出现于 FreeBSD 15.0。
