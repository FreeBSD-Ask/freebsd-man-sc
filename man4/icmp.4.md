# icmp.4

`icmp` — Internet 控制报文协议

## 名称

`icmp`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`Ft int Fn socket AF_INET SOCK_RAW proto`

## 描述

ICMP 是 IP 及互联网协议族使用的差错和控制报文协议。可通过“raw socket”访问它，用于网络监控和诊断功能。创建 ICMP 套接字时，socket 调用的 `proto` 参数可从 getprotobyname(3) 获取。ICMP 套接字是无连接的，通常与 sendto(2) 和 recvfrom(2) 调用一起使用，不过也可以使用 connect(2) 调用固定后续数据包的目的地（此时可使用 read(2) 或 recv(2) 以及 write(2) 或 send(2) 系统调用）。

发出的数据包会自动在前面加上 IP 头（基于目的地址）。接收到的数据包保留 IP 头和选项不变。

### 类型

ICMP 报文根据 ICMP 头中的 type 和 code 字段进行分类。类型和代码的缩写可用于 [pf.conf(5)](../man5/pf.conf.5.md) 中的规则。已定义以下类型：

| **Num** | **Abbrev.** | **Description** |
| ------- | ----------- | --------------- |
| 0 | echorep | Echo reply |
| 3 | unreach | Destination unreachable |
| 4 | squench | Packet loss, slow down |
| 5 | redir | Shorter route exists |
| 6 | althost | Alternate host address |
| 8 | echoreq | Echo request |
| 9 | routeradv | Router advertisement |
| 10 | routersol | Router solicitation |
| 11 | timex | Time exceeded |
| 12 | paramprob | Invalid IP header |
| 13 | timereq | Timestamp request |
| 14 | timerep | Timestamp reply |
| 15 | inforeq | Information request |
| 16 | inforep | Information reply |
| 17 | maskreq | Address mask request |
| 18 | maskrep | Address mask reply |
| 30 | trace | Traceroute |
| 31 | dataconv | Data conversion problem |
| 32 | mobredir | Mobile host redirection |
| 33 | ipv6-where | IPv6 where-are-you |
| 34 | ipv6-here | IPv6 i-am-here |
| 35 | mobregreq | Mobile registration request |
| 36 | mobregrep | Mobile registration reply |
| 39 | skip | SKIP |
| 40 | photuris | Photuris |

已定义以下代码：

| **Num** | **Abbrev.** | **Type** | **Description** |
| ------- | ----------- | -------- | --------------- |
| 0 | net-unr | unreach | Network unreachable |
| 1 | host-unr | unreach | Host unreachable |
| 2 | proto-unr | unreach | Protocol unreachable |
| 3 | port-unr | unreach | Port unreachable |
| 4 | needfrag | unreach | Fragmentation needed but DF bit set |
| 5 | srcfail | unreach | Source routing failed |
| 6 | net-unk | unreach | Network unknown |
| 7 | host-unk | unreach | Host unknown |
| 8 | isolate | unreach | Host isolated |
| 9 | net-prohib | unreach | Network administratively prohibited |
| 10 | host-prohib | unreach | Host administratively prohibited |
| 11 | net-tos | unreach | Invalid TOS for network |
| 12 | host-tos | unreach | Invalid TOS for host |
| 13 | filter-prohib | unreach | Prohibited access |
| 14 | host-preced | unreach | Precedence violation |
| 15 | cutoff-preced | unreach | Precedence cutoff |
| 0 | redir-net | redir | Shorter route for network |
| 1 | redir-host | redir | Shorter route for host |
| 2 | redir-tos-net | redir | Shorter route for TOS and network |
| 3 | redir-tos-host | redir | Shorter route for TOS and host |
| 0 | normal-adv | routeradv | Normal advertisement |
| 16 | common-adv | routeradv | Selective advertisement |
| 0 | transit | timex | Time exceeded in transit |
| 1 | reassemb | timex | Time exceeded in reassembly |
| 0 | badhead | paramprob | Invalid option pointer |
| 1 | optmiss | paramprob | Missing option |
| 2 | badlen | paramprob | Invalid length |
| 1 | unknown-ind | photuris | Unknown security index |
| 2 | auth-fail | photuris | Authentication failed |
| 3 | decrypt-fail | photuris | Decryption failed |

### MIB (sysctl) 变量

ICMP 协议在 sysctl(3) MIB 的 `net.inet.icmp` 分支中实现了若干变量，也可通过 [sysctl(8)](../man8/sysctl.8.md) 读取或修改。

**`bmcastecho`** (`boolean`) 启用/禁用对通过广播或多播接收到的 ICMP 报文的回复。默认为 false。

**`drop_redirect`** (`boolean`) 启用/禁用丢弃 ICMP Redirect 数据包。默认为 false。

**`icmplim`** (`unsigned integer`) 报文的平均速率限制，单位为包/秒。实际限制为 `icmplim` 加上由 `icmplim_jitter` 限定的随机抖动。设为零则不进行限制。默认为 200。

**`icmplim_jitter`** (`unsigned integer`) 在 `icmplim_jitter` 的负值与正值之间取一个随机抖动，应用于 `icmplim`，用于限制报文发送速率。`icmplim` 不为零时，`icmplim_jitter` 必须小于 `icmplim`。设为零则不应用抖动。默认为 16。

**`icmplim_output`** (`boolean`) 启用/禁用 ICMP 报文带宽限制的日志记录。默认为 true。

**`log_redirect`** (`boolean`) 启用/禁用 ICMP Redirect 数据包的日志记录。默认为 false。

**`maskfake`** (`unsigned integer`) 当 `maskrepl` 已设置且此值非零时，系统回复 ICMP Address Mask Request 数据包时将使用此值替代真实地址掩码。默认为 0。

**`maskrepl`** (`boolean`) 启用/禁用对 ICMP Address Mask Request 数据包的回复。默认为 false。

**`quotelen`** (`integer`) 在 ICMP 回复中引用原始数据包的字节数。此数字在内部强制为至少 8 字节（依据 RFC792），至多为 ICMP 回复 mbuf 中剩余的最大空间。

**`redirtimeout`** (`integer`) 由 ICMP redirect 创建的路由过期前的延迟（秒）。

**`reply_from_interface`** (`boolean`) 对并非直接发往本机的数据包，使用数据包进入接口的 IP 地址作为响应源。若启用，此规则先于其他所有规则处理。默认情况下继续进行正常的源地址选择。在路由器上启用此选项特别有用，因为这样可使外部 traceroute 显示数据包经过的实际路径，而非可能不同的返回路径。

**`reply_src`** (`str`) 用于响应并非直接发往本机的数据包的 ICMP 回复源的接口名。默认情况下继续进行正常的源地址选择。

**`tstamprepl`** (`boolean`) 启用/禁用对 ICMP Timestamp 数据包的回复。默认为 true。

## 错误

套接字操作可能失败并返回以下错误之一：

**[EISCONN]** 当尝试在已建立连接的套接字上再次建立连接，或尝试在套接字已连接时指定目的地址发送数据报时；

**[ENOTCONN]** 当尝试发送数据报，但未指定目的地址且套接字未连接时；

**[ENOBUFS]** 当系统为内部数据结构耗尽内存时；

**[EADDRNOTAVAIL]** 当尝试创建一个网络地址对应的网络接口不存在的套接字时。

## 参见

recv(2), send(2), sysctl(3), [dtrace_mib(4)](dtrace_mib.4.md), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [pf.conf(5)](../man5/pf.conf.5.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`icmp` 协议实现出现于 4.2BSD。
