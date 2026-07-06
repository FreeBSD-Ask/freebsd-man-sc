# unix.4

`unix` — UNIX 域协议族

## 名称

`unix`

## 概要

`#include <sys/types.h>`

`#include <sys/un.h>`

## 描述

UNIX 域协议族是一组协议的集合，通过正常的 socket(2) 机制提供本地（同机）进程间通信。UNIX 域协议族支持 `SOCK_STREAM`、`SOCK_SEQPACKET` 和 `SOCK_DGRAM` 套接字类型，并使用文件系统路径名进行寻址。

## 寻址

UNIX 域地址是变长文件系统路径名，最多 104 个字符。头文件

`#include <sys/un.h>`

定义了该地址：

```sh
struct sockaddr_un {
	u_char	sun_len;
	u_char	sun_family;
	char	sun_path[104];
};
```

使用 bind(2) 将名称绑定到 UNIX 域套接字会导致在文件系统中创建一个套接字文件。当套接字关闭时该文件*不会*被删除——必须使用 unlink(2) 来删除该文件。

在绑定套接字之前，可以使用 fchmod(2) 设置套接字文件的权限。这样可以避免在文件创建与随后调用 chmod(2) 之间可能出现的竞争条件。一旦套接字绑定到文件名，就无法再通过这种方式更改文件的权限。

bind(2) 和 connect(2) 所需的 UNIX 域地址长度可通过以下文件中定义的 Fn SUN_LEN 宏计算：

`#include <sys/un.h>`

`sun_path` 字段必须以 `NUL` 字符结尾才能与 Fn SUN_LEN 一起使用，但结尾的 `NUL` *不是*地址的一部分。

UNIX 域协议族不支持广播寻址，也不支持对传入消息进行任何形式的“通配符”匹配。所有地址都是其他 UNIX 域套接字的绝对路径名或相对路径名。引用路径名时也会应用正常的文件系统访问控制机制；例如，connect(2) 或 sendto(2) 的目标必须是可写的。

## 控制消息

UNIX 域套接字支持通过 sendmsg(2) 和 recvmsg(2) 的 `msg` 参数中的 `msg_control` 字段来传递 UNIX 文件描述符和进程凭证。要传递的项目使用 `struct cmsghdr` 描述，该结构定义于头文件

`#include <sys/socket.h>`

要发送文件描述符，消息类型为 `SCM_RIGHTS`，消息的数据部分是一个整数数组，表示要传递的文件描述符。传递的描述符数量由消息的 length 字段定义；length 字段的值等于头部长度加上文件描述符数组的长度。

接收到的描述符是发送方描述符的*副本*，如同通过 `dup(fd)` 或 `fcntl(fd, F_DUPFD_CLOEXEC, 0)` 创建，具体取决于 recvmsg(2) 调用中是否传入了 `MSG_CMSG_CLOEXEC`。

正在等待传递或故意未被接收的描述符，在目标套接字关闭时会由系统自动关闭。接收套接字可以在 sendmsg(2) 调用时通过套接字选项 `SO_PASSRIGHTS` 拒绝 `SCM_RIGHTS`，该选项可通过 setsockopt(2) 设置并通过 getsockopt(2) 检测。

发送方进程的凭证可以通过类型为 `SCM_CREDS` 的控制消息显式传输，其数据部分为 `struct cmsgcred` 类型，定义于

`#include <sys/socket.h>`

如下：

```sh
struct cmsgcred {
  pid_t	cmcred_pid;		/* 发送进程的 PID */
  uid_t	cmcred_uid;		/* 发送进程的实际 UID */
  uid_t	cmcred_euid;		/* 发送进程的有效 UID */
  gid_t	cmcred_gid;		/* 发送进程的实际 GID */
  short	cmcred_ngroups;		/* 组数 */
  gid_t	cmcred_groups[CMGROUP_MAX];	/* 组 */
};
```

发送方应传递一个清零的缓冲区，由系统负责填充。

组列表最多被截断至 `CMGROUP_MAX` 个 GID。

不应通过查询进程 ID `cmcred_pid`（例如通过 `KERN_PROC_PID` sysctl）来做出安全决策。发送进程可能已经退出，其进程 ID 可能已被重新分配给新进程。

## 套接字选项

UNIX 域套接字支持选项级别 `SOL_LOCAL` 下的多种套接字选项，可通过 setsockopt(2) 设置并通过 getsockopt(2) 检测：

`#include <sys/socket.h>`

```sh
struct sockcred {
  uid_t	sc_uid;		/* 实际用户 ID */
  uid_t	sc_euid;	/* 有效用户 ID */
  gid_t	sc_gid;		/* 实际组 ID */
  gid_t	sc_egid;	/* 有效组 ID */
  int	sc_ngroups;	/* 附加组数量 */
  gid_t	sc_groups[1];	/* 变长 */
};
```

```sh
cmsg_len = CMSG_LEN(SOCKCREDSIZE(ngroups))
cmsg_level = SOL_SOCKET
cmsg_type = SCM_CREDS
```

`#include <sys/socket.h>`

```sh
struct sockcred2 {
  int	sc_version;	/* 此结构的版本 */
  pid_t	sc_pid;		/* 发送进程的 PID */
  uid_t	sc_uid;		/* 实际用户 ID */
  uid_t	sc_euid;	/* 有效用户 ID */
  gid_t	sc_gid;		/* 实际组 ID */
  gid_t	sc_egid;	/* 有效组 ID */
  int	sc_ngroups;	/* 附加组数量 */
  gid_t	sc_groups[1];	/* 变长 */
};
```

```sh
cmsg_len = CMSG_LEN(SOCKCRED2SIZE(ngroups))
cmsg_level = SOL_SOCKET
cmsg_type = SCM_CREDS2
```

`#include <sys/ucred.h>`

```sh
struct xucred {
  u_int	cr_version;		/* 结构布局版本 */
  uid_t	cr_uid;			/* 有效用户 ID */
  short	cr_ngroups;		/* 组数 */
  gid_t	cr_groups[XU_NGROUPS];	/* 组 */
  pid_t	cr_pid;			/* 发送进程的进程 ID */
};
```

**`LOCAL_CREDS`** 该选项可在 `SOCK_DGRAM`、`SOCK_SEQPACKET` 或 `SOCK_STREAM` 套接字上启用。该选项为接收方提供了一种机制，使其能够以 recvmsg(2) 控制消息的形式接收调用 write(2)、send(2)、sendto(2) 或 sendmsg(2) 的进程的凭证。`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含一个 `cmsghdr` 结构，后跟一个变长的 `sockcred` 结构，定义如下：当前实现会将组列表最多截断至 `CMGROUP_MAX` 个组。Fn SOCKCREDSIZE 宏用于计算指定组数对应的 `sockcred` 结构大小。`cmsghdr` 字段具有以下值：在 `SOCK_STREAM` 和 `SOCK_SEQPACKET` 套接字上，凭证仅在第一次从套接字读取时传递，随后系统会清除该套接字上的此选项。该选项与上述显式 `struct cmsgcred` 都使用相同的值 `SCM_CREDS`，但二者是互不兼容的控制消息。如果启用了该选项，而发送方附带了带 `struct cmsgcred` 的 `SCM_CREDS` 控制消息，则该消息会被丢弃，并改为包含 `struct sockcred`。许多 setuid 程序会 write(2) 至少部分由调用者控制的数据，例如错误消息。因此，不应将带有特定 `sc_euid` 值的消息信任为来自该用户。

**`LOCAL_CREDS_PERSISTENT`** 该选项类似于 `LOCAL_CREDS`，区别在于套接字凭证会在每次从 `SOCK_STREAM` 或 `SOCK_SEQPACKET` 套接字读取时传递，而不仅仅是第一次读取。此外，`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含一个 `cmsghdr` 结构，后跟一个变长的 `sockcred2` 结构，定义如下：当前版本为零。`cmsghdr` 字段具有以下值：`LOCAL_CREDS` 和 `LOCAL_CREDS_PERSISTENT` 选项互斥。

**`LOCAL_PEERCRED`** 在 `SOCK_STREAM` 或 `SOCK_SEQPACKET` 套接字上通过 getsockopt(2) 请求时，返回对端的凭证。这些凭证将以填充好的 `xucred` 结构形式返回，定义如下：应将 `cr_version` 字段与 `XUCRED_VERSION` 定义进行校验。提交给服务器（调用 listen(2) 的一方）的凭证是客户端调用 connect(2) 时的凭证；提交给客户端（调用 connect(2) 的一方）的凭证是服务器调用 listen(2) 时的凭证。该机制是可靠的；任何一方都无法影响向其对端呈现的凭证，除非在不同的有效凭证下调用相应的系统调用（例如 connect(2) 或 listen(2)）。要在 `SOCK_DGRAM` 套接字上可靠地获取对端凭证，请参见 `LOCAL_CREDS` 套接字选项。

## 缓冲

由于 UNIX 域套接字的本地特性，它们不实现发送缓冲区。send(2) 和 write(2) 系列系统调用会尝试将数据写入目标套接字的接收缓冲区。

`SOCK_STREAM` 和 `SOCK_SEQPACKET` UNIX 域套接字的默认缓冲区大小可分别通过 sysctl(3) MIB 的 `net.local.stream` 和 `net.local.seqpacket` 分支进行配置。注意，设置发送缓冲区大小（sendspace）仅影响最大写入大小。

`SOCK_DGRAM` 类型的 UNIX 域套接字是不可靠的，且写操作始终为非阻塞。默认接收缓冲区可通过 `net.local.dgram.recvspace` 配置。允许的最大数据报大小受 `net.local.dgram.maxdgram` 限制。通过 bind(2) 绑定的 `SOCK_DGRAM` 套接字可以同时连接多个对端。现代 FreeBSD 实现会为每个已连接的套接字在已绑定套接字的接收缓冲区中分配大小为 `net.local.dgram.recvspace` 的私有缓冲区，从而防止单个写入者耗尽全部缓冲区空间的情况。来自未连接发送（使用 sendto(2)）的消息会落入接收套接字的共享缓冲区，该缓冲区具有相同的大小限制。该实现的一个副作用是，它不保证来自不同发送者的写入会按发送的先后顺序到达接收者。对于通过特定连接进行的写入，顺序会得到保持。

## 参见

connect(2), dup(2), fchmod(2), fcntl(2), getsockopt(2), listen(2), recvmsg(2), sendto(2), setsockopt(2), socket(2), [CMSG_DATA(3)](../man3/cmsg_data.3.md), [intro(4)](intro.4.md), [sysctl(8)](../man8/sysctl.8.md)

> "An Introductory 4.3 BSD Interprocess Communication Tutorial", *PS1*, 7.

> "An Advanced 4.3 BSD Interprocess Communication Tutorial", *PS1*, 8.
