# mld.4

`mld` — 多播侦听发现协议

## 名称

`mld`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/in_systm.h>`

`#include <netinet/ip6.h>`

`#include <netinet/icmp6.h>`

`#include <netinet6/mld6.h>`

`Ft int Fn socket AF_INET6 SOCK_RAW IPPROTO_ICMPV6`

## 描述

MLD 是 IPv6 主机和路由器使用的控制平面协议，用于传播多播组成员资格信息。通常不直接使用此协议，除了内核本身响应用户应用程序的多播成员资格请求外。多播路由协议守护进程可以打开原始套接字以直接与 `mld` 交互并接收成员资格报告。

自 FreeBSD 8.0 起，实现了 MLD 版本 2。这增加了对源特定多播（SSM）的支持，应用程序可通过此功能向上游多播路由器传达它们只对从特定源接收多播流感兴趣。状态变更报告的重传为协议增加了一些鲁棒性。

## SYSCTL 变量

**net.inet6.mld.ifinfo** 此不透明的只读变量向 ifmcstat(8) 公开每链路的 MLDv2 状态。

**net.inet6.mld.gsrdelay** 此变量指定处理组和源特定查询（GSR）的时间阈值（以秒为单位）。由于 GSR 查询处理需要在主机上维护状态，可能导致内存分配，因此是拒绝服务（DoS）的潜在攻击点。如果在此阈值内收到多个 GSR 查询，则会被丢弃，以减轻潜在的 DoS。

**net.inet6.mld.v1enable** 如果此变量非零，则此主机将处理 MLDv1 成员资格查询（和主机报告），并启用向后兼容，直到 v1 “较旧版本查询器存在” 计时器到期。此 sysctl 默认启用。

## 参见

[netstat(1)](../man1/netstat.1.md), sourcefilter(3), [icmp6(4)](icmp6.4.md), [inet(4)](inet.4.md), [multicast(4)](multicast.4.md), ifmcstat(8)

## 历史

`mld` 手册页出现于 FreeBSD 8.0。
