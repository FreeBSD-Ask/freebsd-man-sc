# ng_socket(4)

`ng_socket` — netgraph 套接字节点类型

## 名称

`ng_socket`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_socket.h>`

## 描述

`socket` 节点既是 BSD 套接字又是 netgraph 节点。`socket` 节点类型允许用户态进程使用 BSD 套接字接口参与内核 [netgraph(4)](netgraph.4.md) 网络子系统。进程必须具有 root 权限才能创建 netgraph 套接字，但一旦创建，任何拥有它的进程均可使用。

通过使用 socket(2) 系统调用在协议族 `PF_NETGRAPH` 中创建类型为 `NG_CONTROL` 的新套接字来创建新的 `socket` 节点。节点收到的任何 cookie 值不为 `NGM_SOCKET_COOKIE` 的控制消息都可由进程使用 recvfrom(2) 接收；套接字地址参数是包含发送者 netgraph 地址的 `struct sockaddr_ng`。反之，可以通过调用 sendto(2) 将控制消息发送到任何节点，在 `struct sockaddr_ng` 中提供接收者地址。bind(2) 系统调用可用于为节点分配全局 netgraph 名称。

要传输和接收 netgraph 数据包，还必须使用 socket(2) 创建 `NG_DATA` 套接字并将其与 `socket` 节点关联。`NG_DATA` 套接字不会自动关联节点；它们通过 connect(2) 系统调用绑定到特定节点。地址参数是已创建的 `socket` 节点的 netgraph 地址。一旦数据套接字与节点关联，节点收到的任何数据包都可使用 recvfrom(2) 读取，要从节点发出的任何数据包都可使用 sendto(2) 写入。对于数据套接字，`struct sockaddr_ng` 包含接收或应发送数据的*钩子*名称。

作为特例，为了允许 netgraph 数据套接字用作朴素程序的 stdin 或 stdout，当只有一个钩子附加到套接字节点时（因此路径明确），带有 NULL sockaddr 指针的 sendto(2)、send(2) 或 write(2) 将成功。

有一个用户库可简化 netgraph 套接字的使用；见 netgraph(3)。

## 钩子

此节点类型支持任意名称（只要唯一）的钩子，并总是接受钩子连接请求。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**`NGM_SOCK_CMD_NOLINGER`** 当最后一个钩子从该节点移除时，它将如同收到 `NGM_SHUTDOWN` 消息一样关闭。尝试访问关联的套接字将返回 Er ENOTCONN。

**`NGM_SOCK_CMD_LINGER`** 这是默认模式。当最后一个钩子被移除时，节点将继续存在，准备接受新钩子，直到被显式关闭。

所有既无 `NGM_SOCKET_COOKIE` 也无 `NGM_GENERIC_COOKIE` 的其他消息将原样传递上 `NG_CONTROL` 套接字。

## 关闭

当关联的 `NG_CONTROL` 和 `NG_DATA` 套接字均已关闭，或收到 `NGM_SHUTDOWN` 控制消息时，此节点类型关闭并消失。在后一种情况下，尝试写入仍打开的套接字将返回 Er ENOTCONN。如果已收到 `NGM_SOCK_CMD_NOLINGER` 消息，关闭最后一个钩子也将启动节点的关闭。

## 参见

socket(2), netgraph(3), [netgraph(4)](netgraph.4.md), [ng_ksocket(4)](ng_ksocket.4.md), ngctl(8)

## 历史

`socket` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>

## 缺陷

无法拒绝钩子的连接，尽管在该钩子上接收的任何数据当然可以被忽略。

控制进程不会被通知所有内核内节点会被通知的事件，例如新钩子或钩子移除。应为此定义一些由节点发起的消息（沿控制套接字向上发送）。
