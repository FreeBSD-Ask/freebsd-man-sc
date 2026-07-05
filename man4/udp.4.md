# udp.4

`udp` — Internet 用户数据报协议

## 名称

`udp`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`Ft int Fn socket AF_INET SOCK_DGRAM 0`

## 描述

UDP 是一种简单的、不可靠的数据报协议，用于支持 Internet 协议族的 `SOCK_DGRAM` 抽象。UDP 套接字是无连接的，通常与 sendto(2) 和 recvfrom(2) 调用一起使用，但也可使用 connect(2) 调用固定后续数据包的目标（在这种情况下可使用 recv(2) 或 read(2) 以及 send(2) 或 write(2) 系统调用）。

UDP 地址格式与 TCP 使用的相同。特别是，UDP 在正常 Internet 地址格式之外提供端口标识符。注意，UDP 端口空间与 TCP 端口空间是分开的（即 UDP 端口不能“连接”到 TCP 端口）。此外，可使用保留的“广播地址”发送广播数据包（假设底层网络支持此功能）；此地址取决于网络接口。

IP 传输层级的选项可与 UDP 一起使用；参见 [ip(4)](ip.4.md)。可在 IPPROTO_UDP 层级使用 UDP_ENCAP 套接字选项将 ESP 数据包封装在 UDP 中。此选项仅支持一个值：RFC 3948 中定义的 UDP_ENCAP_ESPINUDP，定义于

`#include <netinet/udp.h>`

## FIB 支持

UDP 套接字具有 FIB 感知。它们继承创建套接字的进程的 FIB。默认情况下，绑定到地址的 UDP 套接字可接收源自任何 FIB 的数据报。如果 `net.inet.udp.bind_all_fibs` 可调参数设为 0，所有 UDP 套接字将仅接收源自与套接字相同 FIB 的数据报。在此模式下，多个套接字可绑定到同一地址，只要每个套接字属于不同的 FIB，类似于 `SO_REUSEPORT` 选项的行为。

## MIB（sysctl）变量

`udp` 协议在 sysctl(3) MIB 的 `net.inet.udp` 分支下实现许多变量，也可使用 [sysctl(8)](../man8/sysctl.8.md) 读取或修改：

**`blackhole`** 当数据报到达没有套接字监听的端口时，不返回 ICMP 端口不可达消息。（默认禁用。参见 [blackhole(4)](blackhole.4.md)）

**`checksum`** 启用 UDP 校验和（默认启用）。

**`log_in_vain`** 对于所有到达没有套接字监听端口的 UDP 数据报，记录连接尝试（默认禁用）。

**`maxdgram`** 最大传出 UDP 数据报大小

**`recvspace`** 传入 UDP 数据报的最大空间

## 错误

套接字操作可能失败并返回以下错误之一：

**[Er** EISCONN] 当试图在已有连接的套接字上建立连接时，或当试图发送数据报时指定了目标地址而套接字已连接时；

**[Er** ENOTCONN] 当试图发送数据报但未指定目标地址，且套接字未连接时；

**[Er** ENOBUFS] 当系统内存不足以容纳内部数据结构时；

**[Er** EADDRINUSE] 当尝试使用已分配的端口创建套接字时；

**[Er** EADDRNOTAVAIL] 当尝试为没有网络接口的网络地址创建套接字时。

## 参见

getsockopt(2), recv(2), send(2), socket(2), [blackhole(4)](blackhole.4.md), [dtrace_mib(4)](dtrace_mib.4.md), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [udplite(4)](udplite.4.md)

## 历史

`udp` 协议出现于 4.2BSD。
