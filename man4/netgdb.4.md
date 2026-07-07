# netgdb(4)

`netgdb` — 通过网络用 GDB 调试内核的协议

## 名称

`netgdb`

## 概要

要将 NetGDB 支持编译进内核，请在内核配置文件中加入以下行：

> options DDB
> options GDB
> options INET
> options DEBUGNET
> options NETGDB

## 描述

`netgdb` 是一种基于 UDP 的协议，用于通过中间代理与远程 GDB 客户端通信。

`netgdb` 会话通过在 [ddb(4)](ddb.4.md) 中使用 `netgdb` `-s` `server` [`-g` `gateway` `-c` `client` `-i` `iface` ]] 命令连接到代理服务器来启动。建立连接后，代理服务器会记录一条消息，表明 `netgdb` 客户端已连接。随后它建立一个 TCP 侦听套接字，并记录一条消息，指明它正在侦听的端口。然后等待 GDB 客户端连接。连接的 GDB 命令为：

> `target remote` <`proxyip:proxyport`>

此时，服务器在 `netgdb` 和普通 GDB 客户端之间来回代理流量，使用普通的 GDB 远程协议。从 GDB 调试器的角度来看，`netgdb` 会话与任何其他内核 GDB 会话相同。

## 实现说明

UDP 协议基于与 [netdump(4)](netdump.4.md) 相同的数据包结构和部分完全相同的消息类型。它使用 `HERALD`、`DATA（旧称 VMCORE）` 和 `FINISHED` 消息类型。与 [netdump(4)](netdump.4.md) 一样，客户端的初始 `HERALD` 消息从随机源端口确认，客户端将后续通信发送到该端口。

与 [netdump(4)](netdump.4.md) 不同，初始 `HERALD` 端口为 20025。此外，代理服务器将响应发送到客户端初始 `HERALD` 的源端口，而非单独的保留端口。`netgdb` 消息和确认是双向的。序列号和确认协议在其他方面与 netdump 使用的单向版本相同；它只是在两个方向上运行。确认与常规消息发送到和来自相同的地址和端口。

`netgdb` 协议的第一版在初始 `HERALD` 消息的 32 位 `aux2` 参数中使用协议号‘0x2515f095’。

支持的网络驱动程序和协议族列表与 [netdump(4)](netdump.4.md) 相同。

## 诊断

以下变量既可通过 [sysctl(8)](../man8/sysctl.8.md)，也可通过 [loader(8)](../man8/loader.8.md)（作为可调参数）使用：

**`debug.gdb.netgdb.debug`** 控制调试消息的详细程度。调试消息默认禁用。可以通过将变量设置为非零值来启用。

## 参见

[ddb(4)](ddb.4.md), [gdb(4)](gdb.4.md), [netdump(4)](netdump.4.md)

## 历史

`netgdb` 首次出现于 FreeBSD 13.0。

## 缺陷

由于 [ddb(4)](ddb.4.md) 中对锁原语处理的限制，`netgdb` 只能在内核发生 panic 后使用。

## 安全注意事项

`netgdb` 协议的第 1 版没有任何安全属性。所有消息都以明文形式发送和确认，并且不使用消息认证码来防止攻击者伪造消息。绝对不适合在公共互联网上使用。
