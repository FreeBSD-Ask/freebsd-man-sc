# mac_ipacl.4

`mac_ipacl` — IP 地址访问控制策略

## 名称

`mac_ipacl`

## 概要

要将 IP 地址访问控制策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_IPACL

要在引导时加载 mac_ipacl 策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_ipacl_load= YES
```

## 描述

`mac_ipacl` 策略允许主机 root 使用 [sysctl(8)](../man8/sysctl.8.md) 接口限制 [VNET(9)](../man9/VNET.9.md) jail 设置 IPv4 和 IPv6 地址的能力。因此，主机可通过 [sysctl(8)](../man8/sysctl.8.md) MIB 为 jail 及其接口定义有关 IP 地址的规则。

其默认行为是：如果强制执行 `mac_ipacl` 策略，则禁止 jail 的所有 IP 地址，并根据通过 [sysctl(8)](../man8/sysctl.8.md) 指定的 `security.mac.ipacl.rules` 字符串允许/拒绝 IP（或子网）。

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 用于控制此 MAC 策略的执行和行为。

> jid , allow , interface , addr_family , IP_addr / prefix [@ jid , ...]

**jid** 描述编写规则所针对的 jail 的 jail ID。

**allow** 1 表示允许，0 表示拒绝。决定该规则执行的操作。

**interface** 规则所针对的接口名称。如果接口留空，则为通配符，对所有接口执行规则。

**addr_family** IP_addr 的地址族。输入只能为 AF_INET 或 AF_INET6 字符串。

**IP_addr** 要允许/拒绝的 IP 地址（或子网）。操作取决于前缀长度。

**prefix** 策略要执行的子网前缀长度。-1 表示策略对单个 IP 地址执行。对于非负值，计算为子网 = IP_addr & mask 的 IP 地址范围（位于子网内）。

**`security.mac.ipacl.ipv4`** 对 IPv4 地址强制执行 `mac_ipacl`。（默认：1）。

**`security.mac.ipacl.ipv6`** 对 IPv6 地址强制执行 `mac_ipacl`。（默认：1）。

**`security.mac.ipacl.rules`** IP 地址访问控制列表按以下格式指定：

## 实例

`mac_ipacl` 策略模块针对 sysctl 变量不同输入的行为：

**1.** 设 ipv4=1、ipv6=0 和 rules="1,1,,AF_INET,169.254.123.123/-1" 它仅允许 jail 1 的所有接口（通配符）使用 169.254.123.123 IPv4 地址。由于不对 IPv6 强制执行策略，因此允许所有 IPv6 地址。

**2.** 设 ipv4=1、ipv6=1 和 rules="1,1,epair0b,AF_INET6,fe80::/32@1,0,epair0b,AF_INET6,fe80::abcd/-1" 由于强制执行策略但未指定相关规则，它拒绝所有 IPv4 地址。它允许子网 fe80::/32 中的所有 IPv6 地址，但仅对接口 epair0b 拒绝 fe80::abcd。

**3.** 设 ipv4=1、ipv6=1、rules="2,1,,AF_INET6,fc00::/7@2,0,,AF_INET6,fc00::1111:2200/120@2,1,,AF_INET6,fc00::1111:2299/-1@1,1,,AF_INET,198.51.100.0/24" 它允许 jail 2 的所有接口在子网 198.51.100.0/24 中的 IPv4。它允许子网 fc00::/7 中的 IPv6 地址，但拒绝子网 fc00::1111:2200/120，并允许 jail 2 的所有接口上来自被拒绝子网的个别 IP fc00::1111:2299。

有关使用 ipacl 模块的各种示例，请参见 mac/ipacl 测试框架。

## 限制/注意事项

当多条规则适用于一个 IP 地址或一组 IP 地址时，列表中后定义的规则决定结果，忽略该 IP 地址的任何先前规则。

## 未来工作

规则通过 sysctl 接口给出，在命令行中全部给出会变得非常复杂。需要用更好的方式输入这些规则来简化。

## 参见

[mac(4)](mac.4.md), [mac(9)](../man9/mac.9.md)

## 作者

`mac_ipacl` 策略模块由 Shivank Garg <shivank@FreeBSD.org> 在 Bjoern A. Zeeb <bz@FreeBSD.org> 指导下，作为 2019 年 Google 编程之夏项目开发。
