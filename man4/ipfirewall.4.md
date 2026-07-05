# ipfirewall.4

`ipfw` — IP 数据包过滤和流量统计

## 名称

`ipfw`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下选项：

> options IPFIREWALL

其他可能也有用的相关内核选项：

> options IPFIREWALL_DEFAULT_TO_ACCEPT
> options IPDIVERT
> options IPFIREWALL_NAT
> options IPFIREWALL_NAT64
> options IPFIREWALL_NPTV6
> options IPFIREWALL_PMOD
> options IPFIREWALL_VERBOSE
> options IPFIREWALL_VERBOSE_LIMIT=100
> options LIBALIAS

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 文件中加入以下行：

```sh
ipfw_load="YES"
```

## 描述

`ipfw` 系统设施允许对通过网络接口的 IP 数据包进行过滤、重定向和其他操作。

`ipfw` 的默认行为是阻止所有进入和外出流量。可通过启用 `IPFIREWALL_DEFAULT_TO_ACCEPT` 内核选项来修改此行为，使 `ipfw` 防火墙默认允许所有流量通过。在首次配置 `ipfw` 时，此选项可能有用。如果 `ipfw` 的默认行为是允许一切，则更容易应对可能意外阻止所有流量的防火墙调优错误。

当 [natd(8)](../man8/natd.8.md) 与 `ipfw` 结合作为 NAT 设施使用时，内核选项 `IPDIVERT` 启用将数据包分流到 [natd(8)](../man8/natd.8.md) 进行转换。

当使用 `ipfw` 的内核内 NAT 设施时，内核选项 `IPFIREWALL_NAT` 在内核中启用基本的 libalias(3) 功能。

当使用 `ipfw` 的任何 IPv4 到 IPv6 过渡机制时，内核选项 `IPFIREWALL_NAT64` 在内核中启用所有这些 NAT64 方法。

当使用 `ipfw` 的 IPv6 网络前缀转换设施时，内核选项 `IPFIREWALL_NPTV6` 在内核中启用此功能。

当使用 `ipfw` 的数据包修改设施时，内核选项 `IPFIREWALL_PMOD` 在内核中启用此功能。

要启用记录通过 `ipfw` 的数据包的日志，启用 `IPFIREWALL_VERBOSE` 内核选项。`IPFIREWALL_VERBOSE_LIMIT` 选项可防止 syslogd(8) 充斥系统日志或导致本地拒绝服务。此选项可设置为每个条目在被速率限制之前将记录的数据包数量。

当使用 `ipfw` 的内核内 NAT 设施时，内核选项 `LIBALIAS` 在内核中启用完整的 libalias(3) 功能。完整功能是指包括对 ftp、bbt、skinny、irc、pptp 和 smedia 数据包的支持，这些在通过 `IPFIREWALL_NAT` 内核选项实现的基本 libalias(3) 功能中缺失。

`ipfw` 的用户界面由 [ipfw(8)](../man8/ipfw.8.md) 实用程序实现，因此请参阅 [ipfw(8)](../man8/ipfw.8.md) 手册页以获取有关 `ipfw` 功能及其使用方法的完整说明。

## 参见

setsockopt(2), libalias(3), [divert(4)](divert.4.md), [ip(4)](ip.4.md), [ip6(4)](ip6.4.md), [ipfw(8)](../man8/ipfw.8.md), [natd(8)](../man8/natd.8.md), [sysctl(8)](../man8/sysctl.8.md), syslogd(8), [pfil(9)](../man9/pfil.9.md)
