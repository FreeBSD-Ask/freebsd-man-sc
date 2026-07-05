# gre.4

`gre` — 封装网络设备

## 名称

`gre`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device gre

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_gre_load="YES"
```

## 描述

`gre` 网络接口伪设备将数据报封装到 IP 中。这些封装的数据报被路由到目的主机，在那里被解封装并进一步路由到最终目的地。“隧道”对内部数据报而言如同只有一跳。

`gre` 接口通过 [ifconfig(8)](../man8/ifconfig.8.md) `create` 和 `destroy` 子命令动态创建和销毁。

此驱动对应 RFC 2784。封装的数据报前面会加上外部数据报和 GRE 头部。GRE 头部指定了封装数据报的类型，因此允许对 IP 以外的其他协议进行隧道封装。GRE 模式也是 Cisco 路由器上的默认隧道模式。`gre` 还支持 Cisco WCCP 协议，包括版本 1 和版本 2。

`gre` 接口支持许多传给 [ifconfig(8)](../man8/ifconfig.8.md) 的附加参数：

**`grekey`** 设置用于发出数据包的 GRE 密钥。值为 0 时禁用密钥选项。

**`enable_csum`** 启用发出数据包的校验和计算。

**`enable_seq`** 启用在 GRE 头部中为发出数据包使用序列号字段。

**`udpencap`** 启用 UDP-in-GRE 封装（详见下文 Sx GRE-IN-UDP ENCAPSULATION 一节）。

**`udpport`** 设置发出数据包的源 UDP 端口。值为 0 时禁用发出数据包的源 UDP 端口持久化。详见下文 Sx GRE-IN-UDP ENCAPSULATION 一节。

## GRE-IN-UDP 封装

`gre` 支持 RFC 8086 中定义的 GRE in UDP 封装。GRE in UDP 隧道为在传输网络中对 GRE 流量进行负载均衡提供了更好性能的可能性。将 GRE 封装在 UDP 中可以使用 UDP 源端口为 ECMP 哈希提供熵。

GRE in UDP 隧道使用单值 4754 作为 UDP 目的端口。UDP 源端口包含一个 14 位熵值，由封装方生成以标识封装数据包所属的流。`udpport` 选项可用于禁用此行为并使用单一源 UDP 端口值。`udpport` 的值应在临时端口范围内，即默认为 49152 到 65535。

注意，GRE in UDP 隧道是单向的；隧道流量不会返回到用于生成熵的 UDP 源端口值。这可能影响 NAPT（网络地址端口转换器）中间盒。如果预期在带中间盒的路径上使用此类隧道，可以将隧道配置为禁用 UDP 源端口作为熵，或启用中间盒以放行具有 UDP 源端口熵的数据包。

## 实例

```sh
192.168.1.* --- Router A  -------tunnel-------- Router B --- 192.168.2.*
                                                 /
                                                /
                     +------ the Internet ------+
```

假设路由器 A 的（外部）IP 地址为 A，内部地址为 192.168.1.1，而路由器 B 的外部地址为 B，内部地址为 192.168.2.1，以下命令将配置隧道：

在路由器 A 上：

```sh
ifconfig greN create
ifconfig greN inet 192.168.1.1 192.168.2.1
ifconfig greN inet tunnel A B
route add -net 192.168.2 -netmask 255.255.255.0 192.168.2.1
```

在路由器 B 上：

```sh
ifconfig greN create
ifconfig greN inet 192.168.2.1 192.168.1.1
ifconfig greN inet tunnel B A
route add -net 192.168.1 -netmask 255.255.255.0 192.168.1.1
```

当内部和外部 IP 地址相同时，应使用不同的路由表（FIB）。默认 FIB 将在 GRE 封装之前应用于 IP 数据包。封装后，GRE 接口应为发出数据包设置不同的 FIB 号。然后不同的 FIB 将应用于此类封装数据包。根据此 FIB，数据包应被路由到隧道端点。

```sh
Host X -- Host A (198.51.100.1) ---tunnel--- Cisco D (203.0.113.1) -- Host E
                                                      /
                                                     /
	             +----- Host B ----- Host C -----+
                       (198.51.100.254)
```

在 Host A（FreeBSD）上：

首先应通过 loader.conf 配置多个 FIB：

```sh
net.fibs=2
net.add_addr_allfibs=0
```

然后应将经过网关到此网关远程隧道端点的路由添加到第二个 FIB：

```sh
route add -net 198.51.100.0 -netmask 255.255.255.0 -fib 1 -iface em0
route add -host 203.0.113.1 -fib 1 198.51.100.254
```

并且应将 GRE 隧道配置为对封装数据包更改 FIB：

```sh
ifconfig greN create
ifconfig greN inet 198.51.100.1 203.0.113.1
ifconfig greN inet tunnel 198.51.100.1 203.0.113.1 tunnelfib 1
```

## 注释

`gre` 接口的 MTU 默认设置为 1476，以与 Cisco 路由器使用的值匹配。根据两个隧道端点之间的链路情况，这可能不是最优值。可通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行调整。

为正确操作，`gre` 设备需要一条不经过隧道的到解封装主机的路由，否则会形成环路。

必须通过将 `net.inet.ip.forwarding` [sysctl(8)](../man8/sysctl.8.md) 变量设置为非零值，使内核能够转发数据报。

默认情况下，`gre` 隧道不能嵌套。可在运行时通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.gre.max_nesting` 设置为所需的嵌套级别来修改此行为。

## 参见

[gif(4)](gif.4.md), [inet(4)](inet.4.md), [ip(4)](ip.4.md), [me(4)](me.4.md), [netintro(4)](netintro.4.md), [protocols(5)](../man5/protocols.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 标准

> S. Hanks, T. Li, D. Farinacci, P. Traina, "Generic Routing Encapsulation (GRE)", October 1994.

> S. Hanks, T. Li, D. Farinacci, P. Traina, "Generic Routing Encapsulation over IPv4 networks", October 1994.

> D. Farinacci, T. Li, S. Hanks, D. Meyer, P. Traina, "Generic Routing Encapsulation (GRE)", March 2000.

> G. Dommety, "Key and Sequence Number Extensions to GRE", September 2000.

## 作者

Andrey V. Elsukov <ae@FreeBSD.org> Heiko W.Rupp <hwr@pilhuhn.de>

## 缺陷

当前实现仅将密钥用于发出数据包。带有不同密钥或无密钥的传入数据包将被视为属于此接口。

序列号字段也仅用于发出数据包。
