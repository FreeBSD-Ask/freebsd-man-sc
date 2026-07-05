# ng_ksocket.4

`ng_ksocket` — 内核套接字 netgraph 节点类型

## 名称

`ng_ksocket`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_ksocket.h>`

## 描述

`ksocket` 节点既是 netgraph 节点，也是 BSD 套接字。`ksocket` 节点类型允许在内核中打开一个套接字并将其作为 Netgraph 节点呈现。`ksocket` 节点类型是套接字节点类型的逆向（参见 [ng_socket(4)](ng_socket.4.md)）：套接字节点类型支持用户级操作（通过套接字）通常属于内核级的实体（关联的 Netgraph 节点），而 `ksocket` 节点类型支持内核级操作（通过 Netgraph 节点）通常属于用户级的实体（关联的套接字）。

`ksocket` 节点最多允许一个钩子连接。连接到该节点等价于打开关联的套接字。赋予钩子的名称决定了节点将打开的套接字类型（见下文）。当钩子断开和/或节点关闭时，关联的套接字会被关闭。

## 钩子

本节点类型一次只支持一个钩子连接。钩子名称的格式必须为 *<family>/<type>/<proto>,* 其中 *family,* *type,* 和 *proto* 是与 socket(2) 相同参数的十进制等价值。或者，也接受常用值的别名。例如 `inet/dgram/udp` 是 `2/2/17` 的更可读但等价的版本。

套接字接收到的数据通过钩子发送出去。钩子上接收到的数据从套接字发出（如果后者已连接，即之前向节点发送了 `NGM_KSOCKET_CONNECT`）。如果套接字未连接，则必须在附加到数据的 mbuf 标记中提供目的 `struct sockaddr`，标记 cookie 为 `NGM_KSOCKET_COOKIE`，类型为 `NG_KSOCKET_TAG_SOCKADDR`。否则 `ksocket` 将向发送方返回 `ENOTCONN` 错误。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_KSOCKET_BIND`** (`bind`) 功能与 bind(2) 系统调用完全相同。应提供 `struct sockaddr` 套接字地址参数作为参数。

**`NGM_KSOCKET_LISTEN`** (`listen`) 功能与 listen(2) 系统调用完全相同。应提供 backlog 参数（单个 32 位 `int`）作为参数。

**`NGM_KSOCKET_CONNECT`** (`connect`) 功能与 connect(2) 系统调用完全相同。应提供 `struct sockaddr` 目的地址参数作为参数。

**`NGM_KSOCKET_ACCEPT`** (`accept`) 等价于在非阻塞套接字上调用 accept(2) 系统调用。如果队列上有待处理连接，会创建一个新套接字和相应的克隆节点。返回的是克隆节点的 ID 和对端名称（以 `struct sockaddr` 形式）。如果没有待处理的连接，此控制消息不返回任何内容，已连接的节点会在连接建立时异步收到上述消息。克隆节点支持一个具有任意名称的钩子。如果未连接，节点在其父节点被销毁时消失。一旦连接，它就成为独立节点。

**`NGM_KSOCKET_GETNAME`** (`getname`) 等价于 getsockname(2) 系统调用。名称以 `struct sockaddr` 形式在回复的参数字段中返回。

**`NGM_KSOCKET_GETPEERNAME`** (`getpeername`) 等价于 getpeername(2) 系统调用。名称以 `struct sockaddr` 形式在回复的参数字段中返回。

**`NGM_KSOCKET_SETOPT`** (`setopt`) 等价于 setsockopt(2) 系统调用，区别在于选项名称、级别和值通过 `struct ng_ksocket_sockopt` 传递。

**`NGM_KSOCKET_GETOPT`** (`getopt`) 等价于 getsockopt(2) 系统调用，区别在于选项通过 `struct ng_ksocket_sockopt` 传递。发送此命令时，`value` 字段应为空；返回时，它将包含检索到的值。

## ASCII 形式控制消息

对于在参数字段中传递 `struct sockaddr` 的控制消息，C 结构的正常 ASCII 等价形式是可接受的形式。对于 `PF_INET`、`PF_INET6` 和 `PF_LOCAL` 地址族，还使用更方便的形式，即协议族名称后跟斜杠，再后跟实际地址。对于 `PF_INET`，地址为 IPv4 地址，后跟可选的冒号和端口号。对于 `PF_INET6`，地址为方括号中的 IPv6 地址，后跟可选的冒号和端口号。对于 `PF_LOCAL`，地址为双引号括起的路径名。

示例：

**`PF_LOCAL`** local/"/tmp/foo.socket"

**`PF_INET`** inet/192.168.1.1:1234

**`PF_INET6`** inet6/[2001::1]:1234

**其他** `{ family=16 len=16 data=[0x70 0x00 0x01 0x23] }`

对于传递 `struct ng_ksocket_sockopt` 的控制消息，使用该结构正常的 ASCII 形式。未来可能支持更常用套接字选项的更方便编码。

设置套接字选项示例：

**设置** 套接字的 FIB 为 2（SOL_SOCKET, SO_SETFIB）：`setopt { level=0xffff name=0x1014 data=[ 2 ] }`

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在钩子断开时关闭。节点关闭会关闭关联的套接字。

## 参见

socket(2), [netgraph(4)](netgraph.4.md), [ng_socket(4)](ng_socket.4.md), ngctl(8), [mbuf_tags(9)](../man9/mbuf_tags.9.md), [socket(9)](../man9/socket.9.md)

## 历史

`ksocket` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>
