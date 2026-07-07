# ipsec(4)

`ipsec` — Internet 协议安全协议

## 名称

`ipsec`

## 概要

`options IPSEC options IPSEC_SUPPORT device crypto`

`#include <sys/types.h>`

`#include <netinet/in.h>`

`#include <netipsec/ipsec.h>`

`#include <netipsec/ipsec6.h>`

## 描述

`ipsec` 是在网络协议栈的 Internet 协议层中实现的安全协议。`ipsec` 同时为 IPv4 和 IPv6（[inet(4)](inet.4.md) 和 [inet6(4)](inet6.4.md)）定义。`ipsec` 是一组协议，包括 ESP（Encapsulating Security Payload，封装安全载荷）、AH（Authentication Header，认证头）和 IPComp（IP Payload Compression Protocol，IP 载荷压缩协议），为 IP 数据报提供安全服务。AH 通过附加使用单向哈希函数计算的加密校验和，既认证又保证 IP 数据包的完整性。ESP 此外还通过对 IP 数据包的载荷进行加密，防止未授权方读取载荷。IPComp 试图通过压缩 IP 载荷来提高通信性能，从而减少发送的数据量。这将有助于处于慢速链路但具有足够计算能力的节点。`ipsec` 以两种模式之一运行：传输模式或隧道模式。传输模式用于保护端节点之间的对等通信。隧道模式将 IP 数据包封装在其他 IP 数据包内，专为 VPN 端点等安全网关设计。

系统配置需要 [crypto(4)](crypto.4.md) 子系统。

数据包可传递到虚拟 [enc(4)](enc.4.md) 接口，以在出站加密之前和解封装入站之后执行数据包过滤。

要正确过滤 `ipsec` 隧道的内部数据包，可更改以下 sysctl 的值

| **名称 | 默认 | 启用** |
| --- |
| net.inet.ipsec.filtertunnel | 0 | 1 |
| net.inet6.ipsec6.filtertunnel | 0 | 1 |

### 内核接口

`ipsec` 由驻留在操作系统内核中的密钥管理和策略引擎控制。密钥管理是将密钥与安全关联（也称为 SA）关联的过程。策略管理决定何时创建或销毁新的安全关联。

可使用 `PF_KEY` 套接字从用户空间访问密钥管理引擎。`PF_KEY` 套接字 API 定义于 RFC2367。

策略引擎通过 `PF_KEY` API 的扩展、setsockopt(2) 操作和 sysctl(3) 接口控制。内核实现了 `PF_KEY` 接口的扩展版本，允许程序员定义类似于每包过滤器的 IPsec 策略。setsockopt(2) 接口用于定义每套接字行为，sysctl(3) 接口用于定义主机范围的默认行为。

内核代码未实现动态加密密钥交换协议（如 IKE，Internet Key Exchange）。密钥交换协议超出了内核的必要范围，应实现为调用这些 API 的守护进程。

### 策略管理

IPsec 策略可通过两种方式之一管理：使用 setsockopt(2) 系统调用配置每套接字策略，或使用 `PF_KEY` 接口配置内核级基于包过滤器的策略，通过 setkey(8) 可使用类似于包过滤规则的规则定义针对数据包的 IPsec 策略。有关使用方法，请参阅 setkey(8)。

根据套接字的地址族，可使用 IPPROTO_IP 或 IPPROTO_IPV6 传输级别和 IP_IPSEC_POLICY 或 IPV6_IPSEC_POLICY 套接字选项配置每套接字安全策略。可使用 ipsec_set_policy(3) 函数创建格式正确的 IPsec 策略规范结构，并将其用作 setsockopt(2) 调用的套接字选项值。

使用 setkey(8) 命令设置策略时，“`default`”选项指示系统使用其默认策略（如下所述）处理数据包。以下 sysctl 变量可用于配置系统的 IPsec 行为。这些变量可具有两个值之一。`1` 表示“`use`”，即如果存在安全关联则使用它，但如果没有，则数据包不由 IPsec 处理。值 `2` 同义于“`require`”，即要求必须存在安全关联数据包才能移动，否则被丢弃。这些术语在 ipsec_set_policy(3) 中定义。

| **名称 | 类型 | 可更改** |
| --- |
| net.inet.ipsec.esp_trans_deflev | integer | yes |
| net.inet.ipsec.esp_net_deflev | integer | yes |
| net.inet.ipsec.ah_trans_deflev | integer | yes |
| net.inet.ipsec.ah_net_deflev | integer | yes |
| net.inet6.ipsec6.esp_trans_deflev | integer | yes |
| net.inet6.ipsec6.esp_net_deflev | integer | yes |
| net.inet6.ipsec6.ah_trans_deflev | integer | yes |
| net.inet6.ipsec6.ah_net_deflev | integer | yes |

如果内核未找到匹配的系统级策略，则应用默认值。系统级默认策略由以下 [sysctl(8)](../man8/sysctl.8.md) 变量指定。`0` 表示“`discard`”，即要求内核丢弃数据包。`1` 表示“`none`”。

| **名称 | 类型 | 可更改** |
| --- |
| net.inet.ipsec.def_policy | integer | yes |
| net.inet6.ipsec6.def_policy | integer | yes |

### 其他 sysctl 变量

当配置使用 IPsec 协议时，所有协议都包含在系统中。要选择性启用/禁用协议，使用 [sysctl(8)](../man8/sysctl.8.md)。

| **名称 | 默认** |
| --- |
| net.inet.esp.esp_enable | On |
| net.inet.ah.ah_enable | On |
| net.inet.ipcomp.ipcomp_enable | On |

此外，以下变量可通过 [sysctl(8)](../man8/sysctl.8.md) 访问，用于调整内核的 IPsec 行为：

| **名称 | 类型 | 可更改** |
| --- |
| net.inet.ipsec.ah_cleartos | integer | yes |
| net.inet.ipsec.ah_offsetmask | integer | yes |
| net.inet.ipsec.dfbit | integer | yes |
| net.inet.ipsec.ecn | integer | yes |
| net.inet.ipsec.debug | integer | yes |
| net.inet.ipsec.natt_cksum_policy | integer | yes |
| net.inet.ipsec.check_policy_history | integer | yes |
| net.inet.ipsec.random_id | integer | yes |
| net.inet6.ipsec6.ecn | integer | yes |
| net.inet6.ipsec6.debug | integer | yes |

这些变量的解释如下：

**`ipsec.ah_cleartos`** 如果设为非零，内核在 AH 认证数据计算期间清除 IPv4 头中的服务类型字段。此变量用于使当前系统与实现 RFC1826 AH 的设备互操作。为符合 RFC2402，应将其设为非零（清除服务类型字段）。

**`ipsec.ah_offsetmask`** 在 AH 认证数据计算期间，内核将在 IPv4 头中包含 16 位分片偏移字段（包括标志位），在与该变量进行逻辑与计算之后。此变量用于与实现 RFC1826 AH 的设备互操作。为符合 RFC2402，应将其设为零（计算期间清除分片偏移字段）。

**`ipsec.dfbit`** 此变量配置内核在 IPv4 IPsec 隧道封装上的行为。设为 0 时，外部 IPv4 头中的 DF 位将被清除；1 表示无论内部 DF 位如何都设置外部 DF 位；2 表示 DF 位从内部头复制到外部头。提供此变量以符合 RFC2401 第 6.1 章。

**`ipsec.ecn`** 如果设为非零，IPv4 IPsec 隧道封装/解封装行为将对 ECN（显式拥塞通知）友好，如 `draft-ietf-ipsec-ecn-02.txt` 中所述。[gif(4)](gif.4.md) 对此行为有更多讨论。

**`ipsec.debug`** 如果设为非零，将通过 syslog(3) 生成调试消息。

**`ipsec.natt_cksum_policy`** 控制 IPsec 传输模式使用 UDP 中的 ESP 封装时内核如何处理 TCP 和 UDP 校验和。设为非零值时，内核在入站 TCP 段和 UDP 数据报解封装和解密后完全重新计算校验和。如果设为 0 且 IKE 守护进程为相应 SA 配置了原始地址，内核则增量重新计算入站 TCP 段和 UDP 数据报的校验和。如果未配置地址，则忽略校验和。

**`ipsec.check_policy_history`** 为入站数据包启用严格策略检查。默认情况下，入站安全策略检查由 IPsec 处理的数据包是否已解密和认证。如果此变量设为非零值，则每个由 IPsec 处理的数据包都将对照 IPsec 安全关联历史进行检查。IPsec 安全协议、模式和 SA 地址必须匹配。

**`ipsec.random_id`** 启用封装 IPv4 数据包 ID 的随机化。默认情况下不启用 ID 随机化。

`net.inet6.ipsec6` 树下的变量具有与上述类似的含义。

## 协议

`ipsec` 协议作为 [inet(4)](inet.4.md) 和 [inet6(4)](inet6.4.md) 协议的插件，因此支持大多数在这些 IP 层协议之上定义的协议。[icmp(4)](icmp.4.md) 和 [icmp6(4)](icmp6.4.md) 协议在 `ipsec` 下的行为可能不同，因为 `ipsec` 可阻止 [icmp(4)](icmp.4.md) 或 [icmp6(4)](icmp6.4.md) 例程查看 IP 载荷。

## 参见

ioctl(2), socket(2), ipsec_set_policy(3), [crypto(4)](crypto.4.md), [dtrace_mib(4)](dtrace_mib.4.md), [enc(4)](enc.4.md), [icmp6(4)](icmp6.4.md), [if_ipsec(4)](if_ipsec.4.md), [intro(4)](intro.4.md), [ip6(4)](ip6.4.md), setkey(8), [sysctl(8)](../man8/sysctl.8.md)

> S. Kent, R. Atkinson, "IP Authentication Header", RFC 2404.

> S. Kent, R. Atkinson, "IP Encapsulating Security Payload (ESP)", RFC 2406.

## 标准

> Daniel L. McDonald, Craig Metz, Bao G. Phan, "PF_KEY Key Management API, Version 2", 2367.

> D. L. McDonald, "A Simple IP Security API Extension to BSD Sockets", draft-mcdonald-simple-ipsec-api-03.txt, work in progress material.

## 历史

原始 `ipsec` 实现出现于 WIDE/KAME IPv6/IPsec 协议栈。

在 FreeBSD 5.0 中引入了称为 fast_ipsec 的完全锁定 IPsec 实现。这些协议大量借鉴了 OpenBSD 的 IPsec 协议实现。策略管理代码源自 KAME 在其 IPsec 协议中的实现。fast_ipsec 实现缺乏 [ip6(4)](ip6.4.md) 支持，但使用了 [crypto(4)](crypto.4.md) 子系统。

在 FreeBSD 7.0 中，为 fast_ipsec 添加了 [ip6(4)](ip6.4.md) 支持。此后旧的 KAME IPsec 实现被弃用，fast_ipsec 成为 FreeBSD 中唯一的 `ipsec` 实现。

## 缺陷

策略引擎 API 没有统一标准，因此本文描述的策略引擎 API 仅适用于此实现。

AH 和隧道模式封装可能不如预期工作。如果配置入站“require”策略为 AH 隧道或任何带 AH 的 IPsec 封装策略（如“`esp/tunnel/A-B/use ah/transport/A-B/require`”），隧道化数据包将被拒绝。这是因为策略检查在接收时对内部数据包执行，而 AH 认证的是封装（外部）数据包，而非被封装（内部）数据包（因此对于接收内核来说没有真实性迹象）。当我们改造策略引擎以保留所有数据包解封装历史时，将解决此问题。

当内核中存在大量安全关联或策略数据库时，`PF_KEY` 套接字上的 `SADB_DUMP` 和 `SADB_SPDDUMP` 操作可能因空间不足而失败。增大套接字缓冲区大小可缓解此问题。

由于 zlib(3) 问题，IPcomp 协议偶尔可能出错。

本文档需要更多审查。
