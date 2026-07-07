# poll(2)

`poll` — 同步 I/O 多路复用

## 名称

`poll`

## 库

Lb libc

## 概要

`#include <poll.h>`

```c
int
poll(struct pollfd fds[], nfds_t nfds, int timeout);
```

```c
int
ppoll(struct pollfd fds[], nfds_t nfds,
    const struct timespec * restrict timeout,
    const sigset_t * restrict newsigmask);
```

## 描述

`poll` 系统调用检查一组文件描述符，以查看其中部分是否已准备好进行 I/O。`fds` 参数是指向 pollfd 结构数组的指针，该结构定义于

`#include <poll.h>`

（如下所示）。`nfds` 参数确定 `fds` 数组的大小。

```c
struct pollfd {
    int    fd;       /* 文件描述符 */
    short  events;   /* 要查找的事件 */
    short  revents;  /* 返回的事件 */
};
```

`struct pollfd` 的字段如下：

**fd** 要轮询的文件描述符。如果 fd 等于 -1，则 `revents` 被清零，且该 pollfd 不被检查。

**events** 要轮询的事件。（见下文。）

**revents** 可能发生的事件。（见下文。）

`events` 和 `revents` 中的事件位掩码包含以下位：

**POLLIN** 可无阻塞地读取非高优先级数据。

**POLLRDNORM** 可无阻塞地读取普通数据。

**POLLRDBAND** 可无阻塞地读取非零优先级的数据。

**POLLPRI** 可无阻塞地读取高优先级数据。

**POLLOUT**

**POLLWRNORM** 可无阻塞地写入普通数据。

**POLLWRBAND** 可无阻塞地写入非零优先级的数据。

**POLLERR** 设备或 socket 上发生了异常情况。即使 `events` 位掩码中不存在此标志，也会始终被检查。

**POLLHUP** 设备或 socket 已断开连接。即使 `events` 位掩码中不存在此标志，也会始终被检查。注意，POLLHUP 和 POLLOUT 不应同时出现在 `revents` 位掩码中。

**POLLRDHUP** 远端对等方关闭了连接，或关闭了写入。与 POLLHUP 不同，POLLRDHUP 必须存在于 `events` 位掩码中才会被报告。仅适用于流式 socket。

**POLLNVAL** 文件描述符未打开，或在能力模式下文件描述符权限不足。即使 `events` 位掩码中不存在此标志，也会始终被检查。

如果 `timeout` 既非零也非 INFTIM (-1)，它指定等待任一文件描述符变为就绪的最大间隔，以毫秒为单位。如果 `timeout` 为 INFTIM (-1)，则 poll 无限期阻塞。如果 `timeout` 为零，则 `poll` 将不阻塞而返回。

`ppoll` 系统调用与 `poll` 不同，用于安全地等待直到一组文件描述符变为就绪或捕获到信号。`fds` 和 `nfds` 参数与 `poll` 的相应参数相同。`ppoll` 中的 `timeout` 参数指向一个 `const struct timespec`，该结构定义于

`#include <sys/timespec.h>`

（如下所示），而不是 `poll` 所使用的 `int timeout`。可传递空指针以指示 `ppoll` 应无限期等待。最后，`newsigmask` 指定一个在等待输入时设置的信号掩码。当 `ppoll` 返回时，原始信号掩码会被恢复。

```c
struct timespec {
	time_t  tv_sec;         /* 秒 */
	long    tv_nsec;        /* 以及纳秒 */
};
```

## 返回值

`poll` 系统调用返回已准备好进行 I/O 的描述符数量，如果发生错误则返回 -1。如果时间限制到期，`poll` 返回 0。如果 `poll` 返回时出错（包括因中断的系统调用而导致的错误），`fds` 数组将不被修改。

## 兼容性

此实现与历史实现的不同之处在于，给定的文件描述符可能不会导致 `poll` 返回错误。在历史实现中会发生此情况的情况下（例如尝试轮询一个被 [revoke(2)](revoke.2.md) 的描述符），此实现改为将 `events` 位掩码复制到 `revents` 位掩码。然后，尝试对该描述符执行 I/O 将返回错误。此行为被认为更有用。

## 错误

`poll` 返回错误表示：

**[`EFAULT`]** `fds` 参数指向进程已分配地址空间之外。

**[`EINTR`]** 在时间限制到期之前且在任何选定事件发生之前，交付了信号。

**[`EINVAL`]** 指定的时间限制无效。其某个分量为负或过大。

**[`EINVAL`]** 由 `nfds` 指定的 pollfd 结构数量超过了系统可调参数 `kern.maxfilesperproc` 和 `FD_SETSIZE`。

## 参见

[accept(2)](accept.2.md), [connect(2)](connect.2.md), [kqueue(2)](kqueue.2.md), [pselect(2)](pselect.2.md), [read(2)](read.2.md), [recv(2)](recv.2.md), [select(2)](select.2.md), [send(2)](send.2.md), [write(2)](write.2.md)

## 标准

`poll` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。`ppoll` 函数遵循 -p1003.1-2024。POLLRDHUP 标志未被 POSIX 指定，但与 Linux 和 illumos 兼容。

## 历史

`poll` 函数出现于 AT&T System V UNIX。本手册页和实现的核心部分取自 NetBSD。`ppoll` 函数首次出现于 FreeBSD 10.2。

## 缺陷

在没有 STREAMS 的情况下，`events` 和 `revents` 位掩码中某些字段之间的区分实际上并无用处。这些字段是为与现有软件兼容而定义的。
