# rights(4)

`Capability` — 文件描述符的 Capsicum 能力权能

## 名称

`Capability`

## 描述

当文件描述符由 fhopen(2)、kqueue(2)、mq_open(2)、open(2)、pdfork(2)、pipe(2)、shm_open(2)、socket(2) 或 socketpair(2) 等函数创建时，它被赋予所有能力权能；对于 accept(2)、accept4(2) 或 openat(2)，则从"父"文件描述符继承能力权能。这些权能可通过 cap_rights_limit(2)、cap_fcntls_limit(2) 和 cap_ioctls_limit(2) 系统调用进行缩减（但绝不能扩展）。一旦能力权能被缩减，对该文件描述符的操作将被限制为权能所允许的范围。

完整的能力权能列表见下文。`cap_rights_t` 类型用于存储能力权能列表。应使用 cap_rights_init(3) 系列函数来管理此结构。

## 权能

注意，权能不是简单的位掩码（不能按位进行 OR 运算组合）。详见 cap_rights_init(3)。

可用的权能如下：

**`CAP_ACCEPT`** 允许 accept(2) 和 accept4(2)。

**`CAP_ACL_CHECK`** 允许 acl_valid_fd_np(3)。

**`CAP_ACL_DELETE`** 允许 acl_delete_fd_np(3)。

**`CAP_ACL_GET`** 允许 acl_get_fd(3) 和 acl_get_fd_np(3)。

**`CAP_ACL_SET`** 允许 acl_set_fd(3) 和 acl_set_fd_np(3)。

**`CAP_BIND`** 不在能力模式时，允许在 `fd` 参数中使用特殊值 `AT_FDCWD` 的 bind(2) 和 bindat(2)。注意，套接字也可能因 connect(2) 或 send(2) 而隐式绑定，并且使用 setsockopt(2) 设置的套接字选项也可能影响绑定行为。

**`CAP_BINDAT`** 允许 bindat(2)。此权能必须存在于目录描述符上。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_CHFLAGSAT`** `CAP_FCHFLAGS` 和 `CAP_LOOKUP` 的别名。

**`CAP_CONNECT`** 不在能力模式时，允许在 `fd` 参数中使用特殊值 `AT_FDCWD` 的 connect(2) 和 connectat(2)。对于带非空目的地址的 sendto(2)，此权能也是必需的。

**`CAP_CONNECTAT`** 允许 connectat(2)。此权能必须存在于目录描述符上。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_CREATE`** 允许带 `O_CREAT` 标志的 openat(2)。

**`CAP_EVENT`** 允许使用 select(2)、poll(2) 和 kevent(2) 监视文件描述符上的事件。

**`CAP_EXTATTR_DELETE`** 允许 extattr_delete_fd(2)。

**`CAP_EXTATTR_GET`** 允许 extattr_get_fd(2)。

**`CAP_EXTATTR_LIST`** 允许 extattr_list_fd(2)。

**`CAP_EXTATTR_SET`** 允许 extattr_set_fd(2)。

**`CAP_FCHDIR`** 允许 fchdir(2)。

**`CAP_FCHFLAGS`** 允许 fchflags(2)；若同时存在 `CAP_LOOKUP` 权能，则允许 chflagsat(2)。

**`CAP_FCHMOD`** 允许 fchmod(2)；若同时存在 `CAP_LOOKUP` 权能，则允许 fchmodat(2)。

**`CAP_FCHMODAT`** `CAP_FCHMOD` 和 `CAP_LOOKUP` 的别名。

**`CAP_FCHOWN`** 允许 fchown(2)；若同时存在 `CAP_LOOKUP` 权能，则允许 fchownat(2)。

**`CAP_FCHOWNAT`** `CAP_FCHOWN` 和 `CAP_LOOKUP` 的别名。

**`CAP_FCHROOT`** 允许 fchroot(2)。

**`CAP_FCNTL`** 允许 fcntl(2)。注意，仅 `F_GETFL`、`F_SETFL`、`F_GETOWN` 和 `F_SETOWN` 命令需要此能力权能。另请注意，可通过 cap_fcntls_limit(2) 系统调用进一步限制允许的命令列表。

**`CAP_FEXECVE`** 允许 fexecve(2) 和带 `O_EXEC` 标志的 openat(2)；还需要 `CAP_READ`。

**`CAP_FLOCK`** 允许 flock(2)、fcntl(2)（带 `F_GETLK`、`F_SETLK`、`F_SETLKW` 或 `F_SETLK_REMOTE` 标志）以及 openat(2)（带 `O_EXLOCK` 或 `O_SHLOCK` 标志）。

**`CAP_FPATHCONF`** 允许 fpathconf(2)。

**`CAP_FSCK`** 允许在该描述符上执行 UFS 后台 fsck 操作。

**`CAP_FSTAT`** 允许 fstat(2)；若同时存在 `CAP_LOOKUP` 权能，则允许 fstatat(2)。

**`CAP_FSTATAT`** `CAP_FSTAT` 和 `CAP_LOOKUP` 的别名。

**`CAP_FSTATFS`** 允许 fstatfs(2)。

**`CAP_FSYNC`** 允许 aio_fsync(2)、fdatasync(2)、fsync(2) 和带 `O_DSYNC`、`O_FSYNC` 或 `O_SYNC` 标志的 openat(2)。

**`CAP_FTRUNCATE`** 允许 ftruncate(2) 和带 `O_TRUNC` 标志的 openat(2)。

**`CAP_FUTIMES`** 允许 futimens(2) 和 futimes(2)；若同时存在 `CAP_LOOKUP` 权能，则允许 futimesat(2) 和 utimensat(2)。

**`CAP_FUTIMESAT`** `CAP_FUTIMES` 和 `CAP_LOOKUP` 的别名。

**`CAP_GETPEERNAME`** 允许 getpeername(2)。

**`CAP_GETSOCKNAME`** 允许 getsockname(2)。

**`CAP_GETSOCKOPT`** 允许 getsockopt(2)。

**`CAP_INOTIFY_ADD`** 允许 inotify_add_watch(2) 和 inotify_add_watch_at(2)。

**`CAP_INOTIFY_RM`** 允许 inotify_rm_watch(2)。

**`CAP_IOCTL`** 允许 ioctl(2)。注意此系统调用作用范围极大，对某些对象甚至可能具有全局作用范围。可通过 cap_ioctls_limit(2) 系统调用进一步限制允许的 ioctl 命令列表。

**`CAP_KQUEUE`** `CAP_KQUEUE_CHANGE` 和 `CAP_KQUEUE_EVENT` 的别名。

**`CAP_KQUEUE_CHANGE`** 允许在 kqueue(2) 描述符上执行修改被监视事件列表（`changelist` 参数非空）的 kevent(2)。

**`CAP_KQUEUE_EVENT`** 允许在 kqueue(2) 描述符上执行监视事件（`eventlist` 参数非空）的 kevent(2)。对于将使用 kevent(2) 监视的文件描述符，还需要 `CAP_EVENT`。

**`CAP_LINKAT_SOURCE`** 允许在源目录描述符上执行 linkat(2)。此权能包含 `CAP_LOOKUP` 权能。警告：`CAP_LINKAT_SOURCE` 使得可以将文件链接到存在具备额外权能的文件描述符的目录中。例如，存储在不允许 `CAP_READ` 的目录中的文件，可能被链接到另一个允许 `CAP_READ` 的目录中，从而授予对原本不可读文件的读访问权。

**`CAP_LINKAT_TARGET`** 允许在目标目录描述符上执行 linkat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_LISTEN`** 允许 listen(2)；通常情况下（一般）若没有 `CAP_BIND` 用处不大。

**`CAP_LOOKUP`** 允许文件描述符作为 linkat(2)、openat(2) 和 unlinkat(2) 等调用的起始目录。

**`CAP_MAC_GET`** 允许 mac_get_fd(3)。

**`CAP_MAC_SET`** 允许 mac_set_fd(3)。

**`CAP_MKDIRAT`** 允许 mkdirat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_MKFIFOAT`** 允许 mkfifoat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_MKNODAT`** 允许 mknodat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_MMAP`** 允许带 `PROT_NONE` 保护的 mmap(2)。

**`CAP_MMAP_R`** 允许带 `PROT_READ` 保护的 mmap(2)。此权能包含 `CAP_READ` 和 `CAP_SEEK` 权能。

**`CAP_MMAP_RW`** `CAP_MMAP_R` 和 `CAP_MMAP_W` 的别名。

**`CAP_MMAP_RWX`** `CAP_MMAP_R`、`CAP_MMAP_W` 和 `CAP_MMAP_X` 的别名。

**`CAP_MMAP_RX`** `CAP_MMAP_R` 和 `CAP_MMAP_X` 的别名。

**`CAP_MMAP_W`** 允许带 `PROT_WRITE` 保护的 mmap(2)。此权能包含 `CAP_WRITE` 和 `CAP_SEEK` 权能。

**`CAP_MMAP_WX`** `CAP_MMAP_W` 和 `CAP_MMAP_X` 的别名。

**`CAP_MMAP_X`** 允许带 `PROT_EXEC` 保护的 mmap(2)。此权能包含 `CAP_SEEK` 权能。

**`CAP_PDGETPID`** 允许 pdgetpid(2)。

**`CAP_PDKILL`** 允许 pdkill(2)。

**`CAP_PDWAIT`** 允许 pdwait(2)。

**`CAP_PEELOFF`** 允许 sctp_peeloff(2)。

**`CAP_PREAD`** `CAP_READ` 和 `CAP_SEEK` 的别名。

**`CAP_PWRITE`** `CAP_SEEK` 和 `CAP_WRITE` 的别名。

**`CAP_READ`** 允许 aio_read(2)（还需要 `CAP_SEEK`）、带 `O_RDONLY` 标志的 openat(2)、read(2)、readv(2)、recv(2)、recvfrom(2)、recvmsg(2)、pread(2)（还需要 `CAP_SEEK`）、preadv(2)（还需要 `CAP_SEEK`）、getdents(2)、getdirentries(2) 及相关系统调用。

**`CAP_RECV`** `CAP_READ` 的别名。

**`CAP_RENAMEAT_SOURCE`** 允许在源目录描述符上执行 renameat(2)。此权能包含 `CAP_LOOKUP` 权能。警告：`CAP_RENAMEAT_SOURCE` 使得可以将文件移动到存在具备额外权能的文件描述符的目录中。例如，存储在不允许 `CAP_READ` 的目录中的文件，可能被移动到另一个允许 `CAP_READ` 的目录中，从而授予对原本不可读文件的读访问权。

**`CAP_RENAMEAT_TARGET`** 允许在目标目录描述符上执行 renameat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_SEEK`** 允许在文件描述符上执行如 lseek(2) 之类的寻址操作，但对于可在文件任意位置读写的 I/O 系统调用（如 pread(2) 和 pwrite(2)）也是必需的。

**`CAP_SEM_GETVALUE`** 允许 sem_getvalue(3)。

**`CAP_SEM_POST`** 允许 sem_post(3)。

**`CAP_SEM_WAIT`** 允许 sem_wait(3) 和 sem_trywait(3)。

**`CAP_SEND`** `CAP_WRITE` 的别名。

**`CAP_SETSOCKOPT`** 允许 setsockopt(2)；此权能控制套接字行为的诸多方面，可能影响绑定、连接及其他具有全局作用范围的行为。

**`CAP_SHUTDOWN`** 允许显式的 shutdown(2)；关闭套接字通常也会关闭其上的所有连接。

**`CAP_SYMLINKAT`** 允许 symlinkat(2)。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_TTYHOOK`** 允许在文件描述符上配置 TTY 钩子，如 [snp(4)](snp.4.md)。

**`CAP_UNLINKAT`** 允许 unlinkat(2) 和 renameat(2)。仅当目标对象已存在且将被重命名操作删除时，对目标目录描述符执行 renameat(2) 才需要此权能。此权能包含 `CAP_LOOKUP` 权能。

**`CAP_WRITE`** 允许 aio_write(2)、带 `O_WRONLY` 和 `O_APPEND` 标志的 openat(2)、send(2)、sendmsg(2)、sendto(2)、write(2)、writev(2)、pwrite(2)、pwritev(2) 及相关系统调用。对于带非空连接地址的 sendto(2)，还需要 `CAP_CONNECT`。对于带 `O_WRONLY` 标志但不含 `O_APPEND` 或 `O_TRUNC` 标志的 openat(2)，还需要 `CAP_SEEK`。对于 aio_write(2)、pwrite(2) 和 pwritev(2)，还需要 `CAP_SEEK`。

## 参见

accept(2), accept4(2), aio_fsync(2), aio_read(2), aio_write(2), bind(2), bindat(2), cap_enter(2), cap_fcntls_limit(2), cap_ioctls_limit(2), cap_rights_limit(2), chflagsat(2), connect(2), connectat(2), extattr_delete_fd(2), extattr_get_fd(2), extattr_list_fd(2), extattr_set_fd(2), fchflags(2), fchmod(2), fchmodat(2), fchown(2), fchownat(2), fcntl(2), fexecve(2), fhopen(2), flock(2), fpathconf(2), fstat(2), fstatat(2), fstatfs(2), fsync(2), ftruncate(2), futimes(2), getdents(2), getdirentries(2), getpeername(2), getsockname(2), getsockopt(2), ioctl(2), kevent(2), kqueue(2), linkat(2), listen(2), mmap(2), mq_open(2), open(2), openat(2), pdfork(2), pdgetpid(2), pdkill(2), pdwait4(2), pipe(2), poll(2), pread(2), preadv(2), pwrite(2), pwritev(2), read(2), readv(2), recv(2), recvfrom(2), recvmsg(2), renameat(2), sctp_peeloff(2), select(2), send(2), sendmsg(2), sendto(2), setsockopt(2), shm_open(2), shutdown(2), socket(2), socketpair(2), symlinkat(2), unlinkat(2), write(2), writev(2), acl_delete_fd_np(3), acl_get_fd(3), acl_get_fd_np(3), acl_set_fd(3), acl_set_fd_np(3), acl_valid_fd_np(3), mac_get_fd(3), mac_set_fd(3), sem_getvalue(3), sem_post(3), sem_trywait(3), sem_wait(3), [capsicum(4)](capsicum.4.md), [snp(4)](snp.4.md)

## 历史

对能力和能力模式的支持作为 TrustedBSD 项目的一部分开发。

## 作者

本手册页由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下，基于 Robert Watson <rwatson@FreeBSD.org> 的 cap_new(2) 手册页创建。
