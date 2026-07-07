# open(2)

`open`, `openat` — 为读、写或执行而打开或创建文件

## 名称

`open`, `openat`

## 库

Lb libc

## 概要

```c
#include <fcntl.h>

int
open(const char *path, int flags, ...);

int
openat(int fd, const char *path, int flags, ...);
```

## 描述

`path` 所指定的文件名将根据 `flags` 参数指定的方式被打开，用于执行或读和/或写，并将文件描述符返回给调用进程。`flags` 参数可指示在文件不存在时创建该文件（通过指定 `O_CREAT` 标志）。在这种情况下，`open()` 和 `openat()` 需要一个额外参数 `mode_t mode`，文件将以 `mode` 所描述的模式创建，详见 [chmod(2)](chmod.2.md)，并经过进程的 umask 值修改（参见 [umask(2)](umask.2.md)）。

`openat()` 函数等价于 `open()` 函数，除非 `path` 指定了相对路径或指定了 `O_EMPTY_PATH` 标志。对于 `openat()` 和相对 `path`，当 `fd` 引用一个目录且未指定 `O_EMPTY_PATH` 标志时，要打开的文件相对于与文件描述符 `fd` 关联的目录来确定，而非相对于当前工作目录。`flag` 参数和可选的第四个参数与 `open()` 的参数完全对应。如果 `openat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，行为与调用 `open()` 完全相同。

当 `openat()` 以绝对 `path` 调用时，它忽略 `fd` 参数。

当 `openat()` 以不引用目录的 `fd` 参数调用时，调用将失败，除非指定了 `O_EMPTY_PATH` 标志，参见下文。

在 [capsicum(4)](../man4/capsicum.4.md) capability 模式下，不允许调用 `open()`。`openat()` 的 `path` 参数必须严格相对于文件描述符 `fd`；即 `path` 不能是绝对路径，也不能包含导致路径解析逃逸出以 `fd` 为起点的目录层级的 ".." 组件。此外，`path` 中的符号链接不能以绝对路径为目标，也不能包含逃逸的 ".." 组件。`fd` 不能为 `AT_FDCWD`。

如果 `vfs.lookup_cap_dotdot` [sysctl(3)](../man3/sysctl.3.md) MIB 设置为零，则 capability 模式下使用的路径中的 ".." 组件将被完全禁用。如果 `vfs.lookup_cap_dotdot_nonlocal` MIB 设置为零，则在非本地文件系统上不允许 ".."。

`flags` 由以下值按位或构成：

**`O_RDONLY`** 以只读方式打开

**`O_WRONLY`** 以只写方式打开

**`O_RDWR`** 以读写方式打开

**`O_EXEC`** 以仅执行方式打开

**`O_SEARCH`** 以仅搜索方式打开（`O_EXEC` 的别名，通常与 `O_DIRECTORY` 一起使用）

**`O_NONBLOCK`** 打开时不阻塞

**`O_APPEND`** 每次写入前将文件指针设置到文件末尾

**`O_CREAT`** 如果文件不存在则创建

**`O_TRUNC`** 将大小截断为 0

**`O_EXCL`** 如果设置了 `O_CREAT` 且文件已存在则失败

**`O_SHLOCK`** 原子性地获取共享锁

**`O_EXLOCK`** 原子性地获取排他锁

**`O_DIRECT`** 直接从后备存储读写

**`O_FSYNC`** 同步数据和元数据写入（`O_SYNC` 的历史同义词）

**`O_SYNC`** 同步数据和元数据写入

**`O_DSYNC`** 同步数据写入

**`O_NOFOLLOW`** 不跟随符号链接

**`O_NOCTTY`** 被忽略

**`O_TTY_INIT`** 被忽略

**`O_DIRECTORY`** 如果文件不是目录则出错

**`O_CLOEXEC`** 在 [execve(2)](execve.2.md) 时自动关闭文件

**`O_CLOFORK`** 在通过 [fork(2)](fork.2.md) 创建的任何子进程上自动关闭文件

**`O_VERIFY`** 用 mac_veriexec(4) 验证文件内容

**`O_RESOLVE_BENEATH`** （openat(2)）路径解析不得跨越 `fd` 目录

**`O_PATH`** 在打开的描述符中仅记录目标路径

**`O_EMPTY_PATH`** （openat(2)）如果路径为空则打开 `fd` 所引用的文件

**`O_NAMEDATTR`** 打开命名属性或命名属性目录

必须提供 `O_RDONLY`、`O_WRONLY`、`O_RDWR` 或 `O_EXEC` 中的一个。

以设置了 `O_APPEND` 的方式打开文件会导致在生成的文件描述符上的每次写入都追加到文件末尾。

如果指定了 `O_TRUNC` 且文件存在，文件将被截断为零长度。

如果设置了 `O_CREAT` 但文件已存在，此标志无效，除非同时设置了 `O_EXCL`，此时 `open()` 以 EEXIST 失败。这可用于实现简单的独占访问锁定机制。在所有其他情况下，文件将被创建，文件模式的访问权限位（参见 chmod(2)）被设置为作为 `mode_t mode` 的第三个参数的值，并经过 [umask(2)](umask.2.md) 处理。此参数不影响文件是以读、写还是两者都打开的方式打开。对使用 `O_CREAT` 创建的文件请求加锁时，只要底层文件系统支持锁定，就不会失败；另见下文的 `O_SHLOCK` 和 `O_EXLOCK`。

如果设置了 `O_EXCL` 且路径名的最后一个组件是符号链接，即使该符号链接指向一个不存在的名称，`open()` 也会失败。

如果指定了 `O_NONBLOCK` 且 `open()` 系统调用因某种原因会阻塞（例如，等待拨号线路上的载波），`open()` 将立即返回。该描述符在后续操作中保持非阻塞模式。

如果在掩码中使用了 `O_SYNC`，所有写入将立即同步写入磁盘。`O_FSYNC` 是 `O_SYNC` 的历史同义词。

如果在掩码中使用了 `O_DSYNC`，读取数据所需的所有数据和元数据将同步写入磁盘，但文件访问和修改时间戳等元数据的更改可能会稍后写入。

如果在掩码中使用了 `O_NOFOLLOW` 且传递给 `open()` 的目标文件是符号链接，则 `open()` 将失败。

打开文件时，可以通过设置 `O_SHLOCK` 获取共享锁或设置 `O_EXLOCK` 获取排他锁，来获得具有 [flock(2)](flock.2.md) 语义的锁。

`O_DIRECT` 可用于最小化或消除读写的缓存效应。系统将尝试避免缓存你读取或写入的数据。如果无法避免缓存数据，将最小化数据对缓存的影响。如果不谨慎使用，此标志会大幅降低性能。此标志的语义取决于文件系统，某些文件系统可能完全忽略它。

`O_NOCTTY` 可用于确保操作系统在打开 tty 设备时不会将该文件分配为控制终端。这在 FreeBSD 上是默认行为，但为了 POSIX 兼容性而保留。`open()` 系统调用在 FreeBSD 上不会分配控制终端。

`O_TTY_INIT` 可用于确保操作系统在首次打开 TTY 时恢复终端属性。这在 FreeBSD 上是默认行为，但为了 POSIX 兼容性而保留。在 FreeBSD 上，首次对 TTY 调用 `open()` 将始终恢复默认终端属性。

`O_DIRECTORY` 可用于确保生成的文件描述符引用的是目录。此标志可用于防止具有提升权限的应用程序打开即使以 `O_RDONLY` 打开也不安全的文件，例如设备节点。

`O_CLOEXEC` 可用于为新返回的文件描述符设置 `FD_CLOEXEC` 标志。

`O_CLOFORK` 可用于为新返回的文件描述符设置 `FD_CLOFORK` 标志。该文件将在通过 [fork(2)](fork.2.md)、[vfork(2)](vfork.2.md) 或带 `RFFDG` 标志的 [rfork(2)](rfork.2.md) 创建的任何子进程上关闭，在父进程中保持打开。`O_CLOEXEC` 和 `O_CLOFORK` 标志都可通过 `F_SETFD` [fcntl(2)](fcntl.2.md) 命令修改。

`O_VERIFY` 可用于向内核指示在允许打开继续之前应验证文件内容。"验证"的具体含义取决于实现。运行时链接器（rtld）使用此标志确保共享对象在操作之前已通过验证。

`O_RESOLVE_BENEATH` 在指定相对路径的任何中间组件不驻留在起始目录下方的目录层级中时返回 ENOTCAPABLE。不允许绝对路径，甚至不允许暂时逃逸出起始目录下方。

当以 `O_SEARCH` 打开目录时，将在打开时检查执行权限。返回的文件描述符不能用于任何读操作，如 [getdirentries(2)](getdirentries.2.md)。此描述符的主要用途是作为 `*at` 系列函数的查找描述符。如果在打开时未请求 `O_SEARCH`，则 `*at` 函数在调用 `*at` 时使用描述符所引用目录的当前目录权限。

`O_PATH` 返回一个文件描述符，可用作 `openat()` 和其他以文件描述符为参数的文件系统相关系统调用（统称为 `*at`）的第一个参数，如 fstatat(2) 等。返回的文件描述符的其他功能仅限于以下描述符级操作：

**[connectat(2)](connectat.2.md)** 用于 unix 域套接字（参见 [unix(4)](../man4/unix.4.md)）
**[fcntl(2)](fcntl.2.md)** 但不允许建议性锁定
**[dup(2)](dup.2.md)**
**[close(2)](close.2.md)**
**fstat(2)**
**fstatfs(2)**
**fchdir(2)**
**fchroot(2)**
**fexecve(2)**
**funlinkat(2)** 可作为第三个参数传递
**`SCM_RIGHTS`** 可通过 `SCM_RIGHTS` 消息在 [unix(4)](../man4/unix.4.md) 套接字上传递
**[kqueue(2)](kqueue.2.md)** 仅限 `EVFILT_VNODE`
**__acl_get_fd(2)**
**__acl_aclcheck_fd(2)**
**extattr(2)**
**[capsicum(4)](../man4/capsicum.4.md)** 可传递给 `cap_*_limit` 和 `cap_*_get` 系统调用（如 [cap_rights_limit(2)](cap_rights_limit.2.md)）。

其他操作如 [read(2)](read.2.md)、ftruncate(2) 以及任何其他作用于文件而非文件描述符的操作（fstat(2) 除外）都不允许。

使用 `O_PATH` 标志创建的文件描述符可以通过将其作为 `fd` 参数传递给 `openat()`（`path` 为空且带 `O_EMPTY_PATH` 标志）来打开为正常（可操作的）文件描述符。这种打开方式的行为如同传递了 `fd` 所引用文件的当前路径，但不检查路径遍历权限。另见 fstatat(2) 及相关系统调用中对 `AT_EMPTY_PATH` 标志的描述。

反之，引用文件系统文件的文件描述符 `fd` 可通过以下调用转换为 `O_PATH` 类型的描述符：

```sh
opath_fd = openat(fd, "", O_EMPTY_PATH | O_PATH);
```

如果成功，`open()` 返回一个称为文件描述符的非负整数。失败时返回 -1。返回的文件描述符值是当前进程未使用的最低编号描述符。用于标记文件内当前位置的文件指针设置为文件开头。

如果从 [devfs(4)](../man4/devfs.4.md) 设备节点的休眠打开被信号中断，调用总是以 EINTR 失败，即使为该信号设置了 `SA_RESTART` 标志。fifo 的休眠打开（参见 [mkfifo(2)](mkfifo.2.md)）会正常重启。

创建新文件时，它被分配包含它的目录的组。

除非指定了 `O_CLOEXEC` 标志，否则新描述符被设置为在 [execve(2)](execve.2.md) 系统调用之间保持打开；参见 [close(2)](close.2.md)、[fcntl(2)](fcntl.2.md) 和 `O_CLOEXEC` 标志的描述。

当为 `fd` 参数是文件对象的 `openat()` 指定 `O_NAMEDATTR` 标志时，将打开该文件对象的命名属性而非文件对象本身。如果同时指定了 `O_CREAT` 标志，则在命名属性不存在时创建它。当为 `open()` 指定 `O_NAMEDATTR` 标志时，将打开当前工作目录的命名属性而非当前工作目录本身。此 `openat()` 或 `open()` 的 `path` 参数必须是单个组件名称，不包含嵌入的 `/`。如果 `path` 参数为 `.` 则打开文件对象的命名属性目录。（更多信息参见 [named_attribute(7)](../man7/named_attribute.7.md)。）

系统对一个进程可同时打开的文件描述符数量施加限制。[getdtablesize(2)](getdtablesize.2.md) 系统调用返回当前系统限制。

## 返回值

如果成功，`open()` 和 `openat()` 返回一个称为文件描述符的非负整数。失败时返回 -1，并设置 `errno` 以指示错误。

## 错误

除非以下情况，否则指定的文件将被打开：

**[ENOTDIR]** 路径前缀的某个组件不是目录。

**[ENAMETOOLONG]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[ENOENT]** 未设置 `O_CREAT` 且指定文件不存在。

**[ENOENT]** 路径名中必须存在的某个组件不存在。

**[EACCES]** 路径前缀的某个组件拒绝搜索权限。

**[EACCES]** 给定标志所需的权限（读和/或写）被拒绝。

**[EACCES]** 指定了 `O_TRUNC` 且写权限被拒绝。

**[EACCES]** 指定了 `O_CREAT`，文件不存在，且要创建文件的目录不允许写入。

**[EPERM]** 指定了 `O_CREAT`，文件不存在，且要创建文件的目录设置了不可变标志，更多信息参见 [chflags(2)](chflags.2.md) 手册页。

**[EPERM]** 指定文件设置了不可变标志且要修改该文件。

**[EPERM]** 指定文件设置了仅追加标志，要修改该文件，且指定了 `O_TRUNC` 或未指定 `O_APPEND`。

**[ELOOP]** 在转换路径名时遇到过多的符号链接。

**[EISDIR]** 指定文件是目录，且参数指定要修改它。

**[EISDIR]** 指定文件是目录，且标志指定了 `O_CREAT` 但未指定 `O_DIRECTORY`。

**[EROFS]** 指定文件位于只读文件系统上，且要修改该文件。

**[EROFS]** 指定了 `O_CREAT` 且指定文件将位于只读文件系统上。

**[EMFILE]** 进程已达到其打开文件描述符的限制。

**[ENFILE]** 系统文件表已满。

**[EMLINK]** 指定了 `O_NOFOLLOW` 且目标是符号链接。POSIX 对此情况指定了不同的错误；参见下文 Sx 标准 的说明。

**[ENXIO]** 指定文件是字符特殊文件或块特殊文件，且与此特殊文件关联的设备不存在。

**[ENXIO]** 设置了 `O_NONBLOCK`，指定文件是 fifo，设置了 `O_WRONLY`，且没有进程以读方式打开该文件。

**[EINTR]** `open()` 操作被信号中断。

**[EOPNOTSUPP]** 指定了 `O_SHLOCK` 或 `O_EXLOCK` 但底层文件系统不支持锁定。

**[EOPNOTSUPP]** 指定文件是通过不支持访问的文件系统挂载的特殊文件（例如 NFS）。

**[EWOULDBLOCK]** 指定了 `O_NONBLOCK` 和 `O_SHLOCK` 或 `O_EXLOCK` 之一且文件已锁定。

**[ENOSPC]** 指定了 `O_CREAT`，文件不存在，且正在放置新文件条目的目录因包含该目录的文件系统上没有剩余空间而无法扩展。

**[ENOSPC]** 指定了 `O_CREAT`，文件不存在，且正在创建文件的文件系统上没有空闲 inode。

**[EDQUOT]** 指定了 `O_CREAT`，文件不存在，且正在放置新文件条目的目录因用户在包含该目录的文件系统上的磁盘块配额已耗尽而无法扩展。

**[EDQUOT]** 指定了 `O_CREAT`，文件不存在，且用户在正在创建文件的文件系统上的 inode 配额已耗尽。

**[EIO]** 在为 `O_CREAT` 创建目录项或分配 inode 时发生 I/O 错误。

**[EINTEGRITY]** 从文件系统读取数据时检测到损坏的数据。

**[ETXTBSY]** 文件是正在执行的纯过程（共享文本）文件，且 `open()` 系统调用请求写访问。

**[EFAULT]** `path` 参数指向进程分配地址空间之外。

**[EEXIST]** 指定了 `O_CREAT` 和 `O_EXCL` 且文件已存在。

**[EOPNOTSUPP]** 尝试打开套接字（当前未实现）。

**[EINVAL]** 尝试以 `O_RDONLY`、`O_WRONLY` 或 `O_RDWR` 与 `O_EXEC` 或 `O_SEARCH` 的非法组合打开描述符。

**[EINVAL]** 指定了 `O_CREAT`，且 `path` 参数的最后一个组件在正在创建文件的文件系统上无效。

**[EBADF]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的可搜索文件描述符。

**[ENOTDIR]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[ENOTDIR]** 指定了 `O_DIRECTORY` 且文件不是目录。

**[ECAPMODE]** 指定了 `AT_FDCWD` 且进程处于 capability 模式。

**[ECAPMODE]** 调用了 `open()` 且进程处于 capability 模式。

**[ENOTCAPABLE]** `path` 是绝对路径且进程处于 capability 模式。

**[ENOTCAPABLE]** `path` 是绝对路径且指定了 `O_RESOLVE_BENEATH`。

**[ENOTCAPABLE]** `path` 包含导致目录超出 `fd` 指定目录层级的 ".." 组件，且进程处于 capability 模式。

**[ENOTCAPABLE]** `path` 包含导致目录超出 `fd` 指定目录层级的 ".." 组件，且指定了 `O_RESOLVE_BENEATH`。

**[ENOTCAPABLE]** `path` 包含 ".." 组件，设置了 `vfs.lookup_cap_dotdot` [sysctl(3)](../man3/sysctl.3.md)，且进程处于 capability 模式。

**[ENOATTR]** 指定了 `O_NAMEDATTR` 且文件对象不是命名属性目录或命名属性。

## 参见

[chmod(2)](chmod.2.md), [chflags(2)](chflags.2.md), [close(2)](close.2.md), [dup(2)](dup.2.md), [execve(2)](execve.2.md), [fexecve(2)](fexecve.2.md), [fhopen(2)](fhopen.2.md), [fork(2)](fork.2.md), [getdtablesize(2)](getdtablesize.2.md), [getfh(2)](getfh.2.md), [lgetfh(2)](lgetfh.2.md), [lseek(2)](lseek.2.md), [read(2)](read.2.md), [umask(2)](umask.2.md), [write(2)](write.2.md), [fopen(3)](../man3/fopen.3.md), [capsicum(4)](../man4/capsicum.4.md), [devfs(4)](../man4/devfs.4.md), [unix(4)](../man4/unix.4.md), [named_attribute(7)](../man7/named_attribute.7.md)

## 标准

这些函数由 IEEE Std 1003.1-2008 ("POSIX.1") 规定。

当设置了 `O_NOFOLLOW` 且路径名的最终组件是指向符号链接时，FreeBSD 将 `errno` 设置为 EMLINK 而非 POSIX 规定的 ELOOP，以区分其非最终组件中符号链接遍历过多的情况。

引入 `*at` API 的 Open Group Extended API Set 2 规范要求，关于 `fd` 是否可搜索的测试应基于 `fd` 是否以搜索方式打开，而非底层目录当前是否允许搜索。当前 `openat` 系统调用的实现被认为与 IEEE Std 1003.1-2008, 2017 Edition ("POSIX.1") 兼容，该规范为 `O_SEARCH` 规定了该行为，在缺少该标志时，实现检查目录的当前权限。

## 历史

`open()` 函数首次出现于 Version 1 AT&T UNIX。`openat()` 函数引入于 FreeBSD 8.0。`O_DSYNC` 出现于 13.0。`O_NAMEDATTR` 出现于 15.0。`O_CLOFORK` 出现于 FreeBSD 15.0。

## 缺陷

`mode` 参数是可变参数，可能导致与预期不同的调用约定。