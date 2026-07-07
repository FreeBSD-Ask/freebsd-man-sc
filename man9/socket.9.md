# socket(9)

`socket` — 内核套接字接口

## 名称

`socket`

## 概要

```c
#include <sys/socket.h>
#include <sys/socketvar.h>

void
soabort(struct socket *so)

int
soaccept(struct socket *so, struct sockaddr *nam)

int
socheckuid(struct socket *so, uid_t uid)

int
sobind(struct socket *so, struct sockaddr *nam, struct thread *td)

void
soclose(struct socket *so)

int
soconnect(struct socket *so, struct sockaddr *nam, struct thread *td)

int
socreate(int dom, struct socket **aso, int type, int proto,
    struct ucred *cred, struct thread *td)

int
sodisconnect(struct socket *so)

void
sodtor_set(struct socket *so, void (*func)(struct socket *))

struct sockaddr *
sodupsockaddr(const struct sockaddr *sa, int mflags)

void
sofree(struct socket *so)

void
sohasoutofband(struct socket *so)

int
solisten(struct socket *so, int backlog, struct thread *td)

void
solisten_proto(struct socket *so, int backlog)

int
solisten_proto_check(struct socket *so)

struct socket *
sonewconn(struct socket *head, int connstatus)

int
sopoll(struct socket *so, int events, struct ucred *active_cred,
    struct thread *td)

int
sopoll_generic(struct socket *so, int events, struct ucred *active_cred,
    struct thread *td)

int
soreceive(struct socket *so, struct sockaddr **psa, struct uio *uio,
    struct mbuf **mp0, struct mbuf **controlp, int *flagsp)

int
soreceive_stream(struct socket *so, struct sockaddr **paddr,
    struct uio *uio, struct mbuf **mp0, struct mbuf **controlp,
    int *flagsp)

int
soreceive_dgram(struct socket *so, struct sockaddr **paddr,
    struct uio *uio, struct mbuf **mp0, struct mbuf **controlp,
    int *flagsp)

int
soreceive_generic(struct socket *so, struct sockaddr **paddr,
    struct uio *uio, struct mbuf **mp0, struct mbuf **controlp,
    int *flagsp)

int
soreserve(struct socket *so, u_long sndcc, u_long rcvcc)

void
sorflush(struct socket *so)

int
sosend(struct socket *so, struct sockaddr *addr, struct uio *uio,
    struct mbuf *top, struct mbuf *control, int flags, struct thread *td)

int
sosend_dgram(struct socket *so, struct sockaddr *addr, struct uio *uio,
    struct mbuf *top, struct mbuf *control, int flags, struct thread *td)

int
sosend_generic(struct socket *so, struct sockaddr *addr, struct uio *uio,
    struct mbuf *top, struct mbuf *control, int flags, struct thread *td)

int
soshutdown(struct socket *so, int how)

void
sotoxsocket(struct socket *so, struct xsocket *xso)

void
soupcall_clear(struct socket *so, int which)

void
soupcall_set(struct socket *so, int which,
    int (*func)(struct socket *, void *, int), void *arg)

void
sowakeup(struct socket *so, struct sockbuf *sb)
```

```c
#include <sys/sockopt.h>

int
sosetopt(struct socket *so, struct sockopt *sopt)

int
sogetopt(struct socket *so, struct sockopt *sopt)

int
sooptcopyin(struct sockopt *sopt, void *buf, size_t len, size_t minlen)

int
sooptcopyinptr(struct sockopt *sopt, void *buf, size_t len, size_t minlen)

int
sooptcopyout(struct sockopt *sopt, const void *buf, size_t len)
```

## 描述

内核 `socket` 编程接口允许内核内消费者以类似于 socket(2) 用户 API 所允许的方式与本地和网络套接字对象交互。这些接口适用于分布式文件系统和其他网络感知内核服务。虽然用户 API 操作文件描述符，但内核接口直接操作 `struct socket` 指针。内核 API 的某些部分仅用于实现用户 API，不期望被内核代码使用。套接字消费者和网络协议实现所使用的套接字 API 部分会有所不同；某些例程仅对协议实现者有用。

除非另有说明，`socket` 函数可能睡眠，不适用于在中断线程上下文中或持有不可睡眠的内核锁时使用。

### 创建和销毁套接字

可以使用 `socreate` 创建新套接字。与 socket(2) 一样，参数通过 `dom`、`type` 和 `proto` 指定请求的域、类型和协议。成功时套接字通过 `aso` 返回。此外，用于授权与套接字关联操作的凭证通过 `cred` 传递（并将在套接字生命周期内缓存），执行操作的线程通过 `td` 传递。*警告：* 对于某些协议（如原始套接字），套接字创建操作的授权将使用线程凭证执行。

可以使用 `soclose` 关闭和释放套接字，其语义类似于 close(2)。

在某些情况下，适合在不等待套接字断开连接的情况下销毁它，为此使用 `soabort`。这仅适用于处于部分连接状态的传入连接。它必须由从监听队列中移除套接字的线程在未引用的套接字上调用，以防止竞争。它将调用协议代码，因此在调用期间不能持有任何套接字锁。`soabort` 的调用者负责设置 VNET 上下文。释放套接字的正常路径是 `sofree`，它处理套接字上的引用计数。每当释放引用时，以及每当在套接字或协议代码中清除引用标志时，都应调用它。不应从套接字层外部调用 `sofree`；外部调用者应改用 `soclose`。

### 连接和地址

`sobind` 函数等效于 bind(2) 系统调用，将套接字 `so` 绑定到地址 `nam`。该操作将使用线程 `td` 上的凭证进行授权。

`soconnect` 函数等效于 connect(2) 系统调用，在套接字 `so` 上向地址 `nam` 发起连接。该操作将使用线程 `td` 上的凭证进行授权。与用户系统调用不同，`soconnect` 立即返回；调用者可以在持有套接字互斥体并等待 `SS_ISCONNECTING` 标志清除或 `so->so_error` 变为非零时，在 `so->so_timeo` 上 msleep(9)。如果 `soconnect` 失败，调用者必须手动清除 `SS_ISCONNECTING` 标志。

调用 `sodisconnect` 可断开套接字而不关闭它。

`soshutdown` 函数等效于 shutdown(2) 系统调用，导致套接字上连接的部分或全部被关闭。

套接字通过 `solisten` 从非监听状态转换为监听状态。

### 套接字选项

`sogetopt` 函数等效于 getsockopt(2) 系统调用，在套接字 `so` 上检索套接字选项。`sosetopt` 函数等效于 setsockopt(2) 系统调用，在套接字 `so` 上设置套接字选项。

`sogetopt` 和 `sosetopt` 中的第二个参数是指向描述套接字选项操作的 `struct sopt` 的 `sopt` 指针。调用者分配的结构必须清零，然后初始化其字段以指定套接字选项操作参数：

**`sopt_dir`** 根据是获取还是设置操作，设置为 `SOPT_SET` 或 `SOPT_GET`。

**`sopt_level`** 指定操作所针对的网络栈中的层级；例如 `SOL_SOCKET`。

**`sopt_name`** 指定要设置的套接字选项的名称。

**`sopt_val`** 指向套接字选项参数值的内核空间指针。

**`sopt_valsize`** 参数值的字节大小。

### 套接字上行调用

为使套接字的所有者在套接字准备好发送或接收数据时收到通知，可以在套接字上注册上行调用。上行调用是一个函数，当与给定套接字关联的套接字缓冲区准备好读取或写入时，套接字框架将调用它。`soupcall_set` 用于注册套接字上行调用。函数 `func` 被注册，指针 `arg` 将在框架调用它时作为其第二个参数传递。`which` 的可能值是 `SO_RCV` 和 `SO_SND`，分别注册接收和发送事件的上行调用。上行调用函数 `func` 必须返回 `SU_OK` 或 `SU_ISCONNECTED`，取决于上行调用返回后套接字框架是否应调用 soisconnected。由于与套接字缓冲区锁的锁顺序问题，上行调用 `func` 不能自己调用 soisconnected。只有 `SO_RCV` 上行调用应返回 `SU_ISCONNECTED`。当 `SO_RCV` 上行调用返回 `SU_ISCONNECTED` 时，上行调用将从套接字中移除。

上行调用通过 `soupcall_clear` 从套接字中移除。`which` 参数再次指定要清除的是发送还是接收上行调用，使用 `SO_RCV` 或 `SO_SND`。

### 套接字析构函数回调

内核系统可以使用 `sodtor_set` 函数为套接字设置析构函数。析构函数在套接字即将被释放时调用。析构函数在协议分离例程之前调用。析构函数可以作为回调来启动额外的清理操作。

### 套接字 I/O

`soreceive` 函数等效于 recvmsg(2) 系统调用，尝试从套接字 `so` 接收数据字节，如果没有数据准备好读取，则可选地阻塞等待数据。数据可以通过 `uio` 参数直接检索到内核或用户内存，或作为通过 `mp0` 返回给调用者的 mbuf 链，避免数据复制。`uio` 必须始终非 `NULL`。如果 `mp0` 非 `NULL`，则仅使用 `uio` 的 `uio_resid`。调用者可以通过提供非 `NULL` 的 `psa` 参数存储，可选地在具有 `PR_ADDR` 能力的协议上检索套接字地址。调用者可以通过非 `NULL` 的 `controlp` 参数可选地检索控制数据 mbuf。可选标志可以通过非 `NULL` 的 `flagsp` 参数传递给 `soreceive`，并使用与 recvmsg(2) 系统调用相同的标志命名空间。

`sosend` 函数等效于 sendmsg(2) 系统调用，尝试通过套接字 `so` 发送数据字节，如果数据无法立即发送则可选地阻塞。数据可以通过 `uio` 参数直接从内核或用户内存发送，或通过 `top` 作为 mbuf 链发送，避免数据复制。`uio` 或 `top` 指针中只能有一个非 `NULL`。可以通过非 `NULL` 的 `addr` 参数指定可选目标地址，如果协议支持，这可能导致隐式连接。调用者可以通过非 `NULL` 的 `control` 参数可选地发送控制数据 mbuf。可以使用 `flags` 参数将标志传递给 `sosend`，并使用与 sendmsg(2) 系统调用相同的标志命名空间。

在中断线程上下文中运行或持有互斥体的内核调用者将希望使用非阻塞套接字并传递 `MSG_DONTWAIT` 标志，以防止这些函数睡眠。

可以使用 `sopoll` 查询套接字的可读性、可写性、带外数据或文件结束。`events` 的可能值与 poll(2) 相同，符号值 `POLLIN`、`POLLPRI`、`POLLOUT`、`POLLRDNORM`、`POLLWRNORM`、`POLLRDBAND` 和 `POLLINGEOF` 取自

```c
#include <sys/poll.h>
```

对 `soaccept` 的调用传递给协议的 accept 例程以接受传入连接。

### 套接字实用函数

可以使用 `socheckuid` 将套接字凭证的 uid 与 `uid` 进行比较。

可以使用 `sodupsockaddr` 复制现有的 `struct sockaddr`。

协议实现使用 `sohasoutofband` 通知套接字层带外数据的到达，以便套接字层可以通知套接字消费者可用数据。

可以使用 `sotoxsocket` 创建 `struct socket` 的"外部格式"版本，适合将用户代码与内核结构中的更改隔离。

### 协议实现

协议必须提供 `solisten` 的实现；此类协议实现可以使用 `solisten_proto_check` 和 `solisten_proto` 回调到套接字层以检查和设置套接字层监听状态。提供这些回调以便协议实现可以根据需要对套接字层和协议锁排序。协议必须提供 `soreceive` 的实现；函数 `soreceive_stream`、`soreceive_dgram` 和 `soreceive_generic` 供此类实现使用。

协议实现可以使用 `sonewconn` 创建套接字并将协议状态附加到该套接字。这可用于创建在监听套接字上可供 `soaccept` 使用的新套接字。返回的套接字引用计数为零。

协议必须提供 `sopoll` 的实现；`sopoll_generic` 供协议实现使用。

函数 `sosend_dgram` 和 `sosend_generic` 用于辅助 `sosend` 的协议实现。

当协议创建新套接字结构时，需要通过调用 `soreserve` 为该套接字预留套接字缓冲区空间。此预留的大致逆操作由 `sorflush` 执行，它由套接字框架自动调用。

当协议需要唤醒等待套接字准备好读取或写入的线程时，使用 `sowakeup` 的变体。`sowakeup` 函数不应由协议代码直接调用，而是分别对读者和写者使用包装器 `sorwakeup`、`sorwakeup_locked`、`sowwakeup` 和 `sowwakeup_locked`，对应的套接字缓冲区锁分别为尚未锁定或已持有。

函数 `sooptcopyin` 和 `sooptcopyout` 用于在用户和内核代码之间传输 `struct sockopt` 数据。它们不保留所复制对象中指针的来源（参见 [memory_model(7)](../man7/memory_model.7.md)）。如果要复制的对象包含指针，必须使用 `sooptcopyinptr` 函数保留这些指针的来源。没有对应的 `sooptcopyoutptr`，因为内核通常不返回指向用户空间对象的指针，而是更新先前通过 sooptcopyinptr 传递的对象。

## 参见

bind(2), close(2), connect(2), getsockopt(2), recv(2), send(2), setsockopt(2), shutdown(2), socket(2), [ng_ksocket(4)](../man4/ng_ksocket.4.md), [intr_event(9)](intr_event.9.md), msleep(9), [ucred(9)](ucred.9.md)

## 历史

socket(2) 系统调用出现在 4.2BSD 中。本手册页在 FreeBSD 7.0 中引入。

## 作者

本手册页由 Robert Watson 和 Benjamin Kaduk 编写。

## 缺陷

显式传递的凭证、从显式传递的线程挂起的凭证、`curthread` 上的凭证以及套接字创建时缓存的凭证的使用不一致，可能导致意外行为。一些 `td` 参数可能是 `cred` 参数，或者根本不应存在。

如果 `soconnect` 返回错误，调用者可能需要手动清除 `SS_ISCONNECTING`。

`MSG_DONTWAIT` 标志未对 `sosend` 实现，并且在启用零拷贝套接字时可能并不总是与 `soreceive` 一起工作。

本手册页未描述如何在不使用阻塞 I/O 的情况下注册套接字上行调用或监视套接字的可读性/可写性。

`soref` 和 `sorele` 函数未描述，在大多数情况下不应使用，因为在 `soclose` 之后最后调用 `sorele` 时会有令人困惑且可能不正确的交互。
