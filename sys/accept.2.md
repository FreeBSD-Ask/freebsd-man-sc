# accept(2)

`accept` — 在套接字上接受连接

## 名称

`accept`, `accept4`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
accept(int s, struct sockaddr * restrict addr,
    socklen_t * restrict addrlen);

int
accept4(int s, struct sockaddr * restrict addr,
    socklen_t * restrict addrlen, int flags);
```

## 描述

参数 `s` 是一个已通过 [socket(2)](socket.2.md) 创建、经 [bind(2)](bind.2.md) 绑定到地址、并在 [listen(2)](listen.2.md) 之后开始监听连接的套接字。`accept()` 系统调用从待处理连接队列中取出第一个连接请求，创建一个新的套接字，并为该套接字分配一个新的文件描述符。新套接字继承原套接字 `s` 的 `O_NONBLOCK` 和 `O_ASYNC` 属性以及 `SIGIO` 和 `SIGURG` 信号的目标。

`accept4()` 系统调用与此类似，但新套接字的 `O_NONBLOCK` 属性由 `flags` 参数中的 `SOCK_NONBLOCK` 标志决定，`O_ASYNC` 属性会被清除，信号目标也会被清除，并且可以通过 `flags` 参数中的 `SOCK_CLOEXEC` 标志设置新文件描述符的 close-on-exec 标志。类似地，可以通过 `flags` 参数中的 `SOCK_CLOFORK` 标志设置 `O_CLOFORK` 属性。

如果队列中没有待处理的连接，且原套接字未标记为非阻塞，`accept()` 会阻塞调用者直到有连接到来。如果原套接字已标记为非阻塞且队列中没有待处理的连接，`accept()` 会返回如下所述的错误。被接受的套接字不能用于接受更多连接。原套接字 `s` 保持打开状态。

参数 `addr` 是一个结果参数，会被填入通信层所知的连接方地址。`addr` 参数的确切格式由通信所处的域决定。如果不需要地址信息，可以为 `addr` 指定空指针；此时 `addrlen` 不会被使用，也应为空。否则，`addrlen` 参数是一个值-结果参数；它最初应包含 `addr` 所指向空间的大小；返回时将包含返回地址的实际长度（以字节为单位）。该调用用于面向连接的套接字类型，目前为 `SOCK_STREAM`。

可以通过 [select(2)](select.2.md) 对套接字进行读选择来实现 `accept()` 的就绪检测。

对于某些需要显式确认的协议（如 ISO 或 DATAKIT），`accept()` 可视为仅从队列中取出下一个连接请求，并不表示确认。确认可以通过对新文件描述符进行普通的读或写来暗示，拒绝可以通过关闭新套接字来暗示。

对于某些应用，使用 [accept_filter(9)](../man9/accept_filter.9.md) 预处理传入连接可能提升性能。

使用 `accept()` 时，可移植程序不应依赖 `O_NONBLOCK` 和 `O_ASYNC` 属性以及信号目标被继承，而应使用 [fcntl(2)](fcntl.2.md) 显式设置；`accept4()` 会一致地设置这些属性，但在不同 UNIX 平台上可能不完全可移植。

## 返回值

这些调用出错时返回 -1。成功时返回一个非负整数，作为已接受套接字的描述符。

## 错误

`accept()` 和 `accept4()` 系统调用在以下情况下会失败：

**[EBADF]** 描述符无效。

**[EINTR]** `accept()` 操作被中断。

**[EMFILE]** 进程的描述符表已满。

**[ENFILE]** 系统文件表已满。

**[ENOTSOCK]** 描述符引用的是文件，而非套接字。

**[EINVAL]** 套接字描述符未调用过 [listen(2)](listen.2.md)。

**[EFAULT]** `addr` 参数不在用户地址空间的可写部分。

**[EWOULDBLOCK]** **[EAGAIN]** 套接字已标记为非阻塞，且没有可接受的连接。

**[ECONNABORTED]** 有连接到来，但在监听队列上等待时被关闭。

`accept4()` 系统调用在以下情况下也会失败：

**[EINVAL]** `flags` 参数无效。

## 参见

[bind(2)](bind.2.md), [connect(2)](connect.2.md), [getpeername(2)](getpeername.2.md), [getsockname(2)](getsockname.2.md), [listen(2)](listen.2.md), [select(2)](select.2.md), [socket(2)](socket.2.md), [accept_filter(9)](../man9/accept_filter.9.md)

## 历史

`accept()` 系统调用首次出现于 4.2BSD。

`accept4()` 系统调用首次出现于 FreeBSD 10.0。

`SOCK_CLOFORK` 标志首次出现于 FreeBSD 15.0。
