# udplite(4)

`udplite` — 轻量用户数据报协议

## 名称

`udplite`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/udplite.h>`

`Ft int Fn socket AF_INET SOCK_DGRAM IPPROTO_UDPLITE`

## 描述

UDP-Lite 协议提供部分校验和，允许损坏的数据包传送到接收应用程序。这对于某些类型的多媒体传输有优势，可能能够利用略微损坏的数据报，而不是让低层协议丢弃它们。

UDP-Lite 支持许多套接字选项，可使用 setsockopt(2) 设置、使用 getsockopt(2) 测试：

**`UDPLITE_SEND_CSCOV`** 此选项设置发送方校验和覆盖范围。值为零表示所有发送的数据包将具有完整校验和覆盖。值为 8 到 65535 将所有发送数据包的校验和覆盖范围限制为给定值。

**`UDPLITE_RECV_CSCOV`** 此选项是接收方的对应物。值为零指示内核丢弃所有未具有完整校验和覆盖的接收数据包。值为 8 到 65535 指示内核丢弃所有部分校验和覆盖小于指定值的接收数据包。

## 错误

套接字操作可能失败并返回以下错误之一：

**[Er** EISCONN] 当试图在已有连接的套接字上建立连接时，或当试图发送数据报时指定了目标地址而套接字已连接时；

**[Er** ENOTCONN] 当试图发送数据报但未指定目标地址，且套接字未连接时；

**[Er** ENOBUFS] 当系统内存不足以容纳内部数据结构时；

**[Er** EADDRINUSE] 当尝试使用已分配的端口创建套接字时；

**[Er** EADDRNOTAVAIL] 当尝试为没有网络接口的网络地址创建套接字时。

## 参见

getsockopt(2), recv(2), send(2), socket(2)
