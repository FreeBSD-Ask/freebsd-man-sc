# select(2)

`select` — 同步 I/O 多路复用

## 名称

`select`

## 库

Lb libc

## 概要

`#include <sys/select.h>`

```c
int
select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds,
    struct timeval *timeout);
```

```c
FD_SET(fd, &fdset);
FD_CLR(fd, &fdset);
FD_ISSET(fd, &fdset);
FD_ZERO(&fdset);
```

## 描述

`select` 系统调用检查其地址通过 `readfds`、`writefds` 和 `exceptfds` 传入的 I/O 描述符集，以查看其中部分描述符是否已准备好读取、已准备好写入或有待处理的异常情况。唯一可检测的异常情况是 socket 上接收到的带外数据。每个集合中检查前 `nfds` 个描述符；即检查描述符集中从 0 到 `nfds`-1 的描述符。返回时，`select` 用由那些已准备好进行所请求操作的描述符组成的子集替换给定的描述符集。`select` 系统调用返回所有集合中就绪描述符的总数。

描述符集以整数数组中的位字段形式存储。提供了以下宏来操作此类描述符集：`FD_ZERO(&fdset)` 将描述符集 `fdset` 初始化为空集。`FD_SET(fd, &fdset)` 将特定描述符 `fd` 包含到 `fdset` 中。`FD_CLR(fd, &fdset)` 从 `fdset` 中移除 `fd`。如果 `fd` 是 `fdset` 的成员，则 `FD_ISSET(fd, &fdset)` 为非零，否则为零。如果描述符值小于零或大于等于 `FD_SETSIZE`（通常至少等于系统支持的最大描述符数量），则这些宏的行为是未定义的。

如果 `timeout` 不是空指针，它指定等待选择完成的最大间隔。系统活动可能使该间隔增加不确定的量。

如果 `timeout` 是空指针，select 无限期阻塞。

为执行轮询，`timeout` 参数不应为空指针，而应指向一个零值的 timeval 结构。

如果没有感兴趣的描述符，`readfds`、`writefds` 和 `exceptfds` 中的任何一个都可以作为空指针给出。

## 返回值

`select` 系统调用返回描述符集中包含的就绪描述符数量，如果发生错误则返回 -1。如果时间限制到期，`select` 返回 0。如果 `select` 返回时出错（包括因中断的系统调用而导致的错误），描述符集将不被修改。

## 错误

`select` 返回错误表示：

**[`EBADF`]** 某个描述符集指定了无效的描述符。

**[`EFAULT`]** 参数 `readfds`、`writefds`、`exceptfds` 或 `timeout` 之一指向无效地址。

**[`EINTR`]** 在时间限制到期之前且在任何选定事件发生之前，交付了信号。

**[`EINVAL`]** 指定的时间限制无效。其某个分量为负或过大。

**[`EINVAL`]** `nfds` 参数无效。

## 参见

[accept(2)](accept.2.md), [connect(2)](connect.2.md), [getdtablesize(2)](getdtablesize.2.md), [gettimeofday(2)](gettimeofday.2.md), [kqueue(2)](kqueue.2.md), [poll(2)](poll.2.md), [pselect(2)](pselect.2.md), [read(2)](read.2.md), [recv(2)](recv.2.md), [send(2)](send.2.md), [write(2)](write.2.md), [clocks(7)](../man7/clocks.7.md)

## 注释

`FD_SETSIZE` 的默认大小当前为 1024。为了适应可能使用大量打开文件的程序与 `select` 配合使用，可通过让程序在包含

`#include <sys/types.h>`

的任何头文件之前定义 `FD_SETSIZE` 来增加此大小。

如果 `nfds` 大于打开文件的数量，不保证 `select` 会检查未使用的文件描述符。由于历史原因，`select` 将始终检查前 256 个描述符。

## 标准

`select` 系统调用和 `FD_CLR`、`FD_ISSET`、`FD_SET`、`FD_ZERO` 宏遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`select` 系统调用出现于 4.2BSD。

## 缺陷

-susv2 允许系统就地修改原始超时值。因此，假设超时值不会被 `select` 系统调用修改是不明智的。FreeBSD 不会修改返回值，这可能对从其他系统移植的应用程序造成问题。
