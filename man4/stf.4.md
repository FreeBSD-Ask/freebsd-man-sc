# stf(4)

`stf` —

## 名称

`stf` 6to4 隧道接口

## 概要

`device stf`

## 描述

`stf` 接口支持“6to4”和“6rd”IPv6 in IPv4 封装。它可以在 IPv4 上隧道传输 IPv6 流量，如 `RFC3056` 或 `RFC5969` 所规定。

对于 6to4 或 6RD 站点中的普通节点，无需 `stf` 接口。`stf` 接口是站点边界路由器（在规范中称为“6to4 路由器”或“6rd Customer Edge (CE)”）所必需的。

每个 `stf` 接口都在运行时通过接口克隆创建。这最易于通过 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量完成。

## 6to4

由于 6to4 协议的规范方式，`stf` 接口需要某些配置才能正常工作。需要为接口配置单个（不超过 1 个）有效的 6to4 地址。“有效的 6to4 地址”是具有以下属性的地址。如果不满足以下任何属性，`stf` 将在数据包传输时引发运行时错误。更多细节请阅读规范。

- 匹配 `2002:xxyy:zzuu::/48`，其中 `xxyy:zzuu` 是节点 IPv4 地址的十六进制表示。IPv4 地址可取自节点拥有的任何接口。由于规范禁止使用 IPv4 私有地址，因此该地址需要是全局 IPv4 地址。
- 子网标识符部分（第 48 至 63 位）和接口标识符部分（低 64 位）被正确填充以避免地址冲突。

如果希望节点充当中继路由器，IPv6 接口地址的前缀长度需要为 16，以便节点将任何 6to4 目标视为“在链上”。如果希望将 6to4 对端限制在某个 IPv4 前缀内，可将 IPv6 前缀长度配置为“16 + IPv4 前缀长度”。如果 IPv6 前缀长度大于 16，`stf` 接口将检查数据包的 IPv4 源地址。

`stf` 可配置为对 ECN 友好。这可通过 `IFF_LINK1` 配置。详见 [gif(4)](gif.4.md)。

请注意，6to4 规范被写为“接受来自所有人的隧道数据包”的隧道设备。启用 `stf` 设备会使恶意方更容易向你的节点注入伪造的 IPv6 数据包。此外，恶意方可以注入具有伪造源地址的 IPv6 数据包，使你的节点生成不当的隧道数据包。管理员在启用接口时必须谨慎。为防止可能的攻击，`stf` 接口会过滤以下数据包。注意，这些检查绝非完整：

- 外部 IPv4 源/目的为 IPv4 未指定地址的数据包（`0.0.0.0/8`）
- 外部 IPv4 源/目的为环回地址的数据包（`127.0.0.0/8`）
- 外部 IPv4 源/目的为 IPv4 多播地址的数据包（`224.0.0.0/4`）
- 外部 IPv4 源/目的为受限广播地址的数据包（`255.0.0.0/8`）
- 外部 IPv4 源/目的为私有地址的数据包（`10.0.0.0/8 , 172.16.0.0/12 , 192.168.0.0/16`）
- 外部 IPv4 源/目的为子网广播地址的数据包。检查针对所有直接连接子网的子网广播地址进行。
- 未通过入口过滤的数据包。外部 IPv4 源地址必须符合路由表中的 IPv4 拓扑。入口过滤器可通过 `IFF_LINK2` 位关闭。
- 如果 IPv6 地址匹配 6to4 前缀，则相同的规则集也应用于嵌入在内部 IPv6 地址中的 IPv4 地址。

建议根据需要对传入的 IP 协议号为 41 的 IPv4 数据包进行过滤/审计。也建议对封装的 IPv6 数据包进行过滤/审计。你可能还希望对内部 IPv6 地址运行正常的入口过滤器以避免欺骗。

通过在 `stf` 接口上设置 `IFF_LINK0` 标志，可以禁用输入路径，使来自外部的直接攻击成为不可能。但请注意，还存在其他安全风险。如果希望使用此配置，则不得向他人通告你的 6to4 地址。

## 6rd

与“6to4”一样，“6rd”在使用前也需要配置。所需的配置参数为：

- IPv6 地址和前缀长度。
- 边界路由器 IPv4 地址。
- IPv4 WAN 地址。
- IPv4 WAN 地址的前缀长度。

这些参数都通过 [ifconfig(8)](../man8/ifconfig.8.md) 配置。

IPv6 地址和前缀长度可像任何其他 IPv6 地址一样配置。注意，前缀长度是不包括嵌入 IPv4 地址位的 IPv6 前缀长度。委派网络的前缀长度是 IPv6 前缀长度与 IPv4 前缀长度之和。

边界路由器 IPv4 地址通过 [ifconfig(8)](../man8/ifconfig.8.md) `stfv4br` 命令配置。

IPv4 WAN 地址和 IPv4 前缀长度通过 [ifconfig(8)](../man8/ifconfig.8.md) `stfv4net` 命令配置。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用于控制 `stf` 的行为。默认值显示在每个变量旁边。

**`net.link.stf.permit_rfc1918`** : 0 RFC3056 要求使用全局唯一的 32 位 IPv4 地址。此 sysctl 变量控制此要求的行为。当设置为非 0 时，`stf` 允许使用 RFC1918 中描述的私有 IPv4 地址。这对于 Intranet 环境或使用某些网络地址转换（NAT）机制的情况可能有用。

## 实例

注意，`8504:0506` 等于 `133.4.5.6`，以十六进制表示。

```sh
# ifconfig ne0 inet 133.4.5.6 netmask 0xffffff00
# ifconfig stf0 inet6 2002:8504:0506:0000:a00:5aff:fe38:6f86 \
	prefixlen 16 alias
```

以下配置仅接受来自 IPv4 源 `9.1.0.0/16` 的数据包。它仅对 IPv6 目标 2002:0901::/32 发出 6to4 数据包（IPv4 目标将匹配 `9.1.0.0/16`）。

```sh
# ifconfig ne0 inet 9.1.2.3 netmask 0xffff0000
# ifconfig stf0 inet6 2002:0901:0203:0000:a00:5aff:fe38:6f86 \
	prefixlen 32 alias
```

以下配置将 `stf` 接口用作仅输出设备。你需要有备用 IPv6 连接（非 6to4）才能使用此配置。对于出站流量，可通过 `stf` 高效地到达其他 6to4 网络。对于入站流量，你将不会收到任何 6to4 隧道数据包（安全缺陷较少）。注意不要向他人通告你的 6to4 前缀（`2002:8504:0506::/48`），也不要使用你的 6to4 前缀作为源。

```sh
# ifconfig ne0 inet 133.4.5.6 netmask 0xffffff00
# ifconfig stf0 inet6 2002:8504:0506:0000:a00:5aff:fe38:6f86 \
	prefixlen 16 alias deprecated link0
# route add -inet6 2002:: -prefixlen 16 ::1
# route change -inet6 2002:: -prefixlen 16 ::1 -ifp stf0
```

以下示例在“6rd CE”上配置“6rd”隧道，其中 ISP 的“6rd”IPv6 前缀为 2001:db8::/32。边界路由器为 192.0.2.1。“6rd CE”的 WAN 地址为 192.0.2.2，完整的 IPv4 地址嵌入在“6rd IPv6 地址”中：

```sh
# ifconfig stf0 inet6 2001:db8:c000:0202:: prefixlen 32 up
# ifconfig stf0 stfv4br 192.0.2.1
# ifconfig stf0 stfv4net 192.0.2.2/32
```

## 参见

[gif(4)](gif.4.md), [inet(4)](inet.4.md), [inet6(4)](inet6.4.md)

> Brian Carpenter, Keith Moore, "Connection of IPv6 Domains via IPv4 Clouds", 3056, February 2001.

> Jun-ichiro itojun Hagino, "Possible abuse against IPv6 transition technologies", draft-itojun-ipv6-transition-abuse-01.txt, July 2000, work in progress.

## 历史

`stf` 设备首次出现于 WIDE/KAME IPv6 协议栈。

## 缺陷

一个节点最多只允许一个 `stf` 接口，一个 `stf` 接口最多只允许一个 IPv6 接口地址。这是为了避免 IPv6 层与 IPv4 层之间的源地址选择冲突，并应对对端的入口过滤规则。这是使 `stf` 在所有场合下正确工作的特性。
