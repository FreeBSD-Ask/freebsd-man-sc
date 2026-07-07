# listen(2)

`listen` — 在套接字上监听连接

## 名称

`listen`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
int
listen(int s, int backlog);
```

## 描述

要接受连接，首先通过 [socket(2)](socket.2.md) 创建套接字，然后用 `listen()` 指明愿意接受传入连接并为传入连接设置队列长度限制，最后通过 [accept(2)](accept.2.md) 接受连接。`listen()` 系统调用仅适用于 `SOCK_STREAM` 或 `SOCK_SEQPACKET` 类型的套接字。

`backlog` 参数定义了待处理连接队列可能增长到的最大长度。实际的最大队列长度将是 `backlog` 参数指定值的 1.5 倍。在监听套接字上后续的 `listen()` 系统调用允许调用者使用新的 `backlog` 参数更改最大队列长度。如果连接请求到达时队列已满，客户端可能会收到带有 `ECONNREFUSED` 错误指示的错误，或者在 TCP 的情况下，连接将被静默丢弃。

可以使用 [netstat(1)](../man1/netstat.1.md) 命令查询监听套接字的当前队列长度。

注意，在 FreeBSD 4.5 之前以及引入 syncache 之前，`backlog` 参数还决定了不完整连接队列的长度，该队列用于存放正在完成 TCP 三次握手中的 TCP 套接字。这些不完整的连接现在完全保存在 syncache 中，不受队列长度影响。为帮助应对拒绝服务攻击而增大 `backlog` 值已不再必要。

[sysctl(3)](../man3/sysctl.3.md) MIB 变量 `kern.ipc.soacceptqueue` 指定了 `backlog` 的硬性限制；如果指定的值大于 `kern.ipc.soacceptqueue` 或小于零，`backlog` 将被静默地强制设为 `kern.ipc.soacceptqueue`。

如果监听队列溢出，内核将使用默认优先级 LOG_DEBUG (7) 发出 syslog 消息。[sysctl(3)](../man3/sysctl.3.md) MIB 变量 `kern.ipc.sooverprio` 可用于将此优先级更改为 0..7 (LOG_EMERG..LOG_DEBUG) 范围内的任何值。详细信息请参见 [syslog(3)](../man3/syslog.3.md)。可将其设置为 -1 以禁用这些消息。

变量 `kern.ipc.sooverinterval` 指定了内核发出这些消息的每套接字频率限制。

## 与接受过滤器的交互

在套接字上使用接受过滤时，将使用第二个队列来存放已连接但尚未满足其接受过滤条件的套接字。一旦满足条件，这些套接字将被移至已完成连接队列，等待 [accept(2)](accept.2.md) 接受。如果此辅助队列已满且有新连接到来，则尚未满足其接受过滤条件的最旧套接字将被终止。

此辅助队列与主监听队列一样，根据 `backlog` 参数确定大小。

## 返回值

成功完成时，`listen()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`listen()` 系统调用在以下情况下会失败：

**[`EBADF`]** 参数 `s` 不是有效的描述符。

**[`EDESTADDRREQ`]** 套接字未绑定到本地地址，且协议不支持在未绑定的套接字上监听。

**[`EINVAL`]** 套接字已经连接，或正在连接过程中。

**[`ENOTSOCK`]** 参数 `s` 不是套接字。

**[`EOPNOTSUPP`]** 套接字的类型不支持 `listen()` 操作。

## 参见

[netstat(1)](../man1/netstat.1.md), [accept(2)](accept.2.md), [connect(2)](connect.2.md), [socket(2)](socket.2.md), [sysctl(3)](../man3/sysctl.3.md), [syslog(3)](../man3/syslog.3.md), [sysctl(8)](../man8/sysctl.8.md), [accept_filter(9)](../man9/accept_filter.9.md)

## 历史

`listen()` 系统调用出现于 4.2BSD。在运行时配置最大 `backlog` 的能力，以及使用负的 `backlog` 来请求最大允许值的功能，在 FreeBSD 2.2 中引入。在 FreeBSD 10.0 中，`kern.ipc.somaxconn` [sysctl(3)](../man3/sysctl.3.md) 已被 `kern.ipc.soacceptqueue` 替换，以避免对其实际功能的混淆。原有的 [sysctl(3)](../man3/sysctl.3.md) `kern.ipc.somaxconn` 仍然可用，但已从 [sysctl(3)](../man3/sysctl.3.md) -a 的输出中隐藏，以使现有应用程序和脚本继续工作。
