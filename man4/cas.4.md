# cas.4

`cas` — Sun Cassini/Cassini+ 及 National Semiconductor DP83065 Saturn 千兆以太网驱动

## 名称

`cas`

## 概要

要将此驱动编译进内核，请在你的内核配置文件中加入以下行：

> device miibus
> device cas

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_cas_load="YES"
```

## 描述

`cas` 驱动为 Sun Cassini/Cassini+ 和 National Semiconductor DP83065 Saturn 千兆以太网控制器提供支持。

`cas` 驱动支持的所有控制器均具备收发 TCP/UDP 校验和卸载能力，支持 [vlan(4)](vlan.4.md) 扩展帧的收发，具有中断合并/调节机制以及 512 位多播哈希过滤器。

`cas` 驱动还支持 Jumbo 帧（最大 9022 字节），可通过接口 MTU 设置来配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具将 MTU 设置为大于 1500 字节时，适配器将被配置为收发 Jumbo 帧。

## 硬件

`cas` 驱动支持的芯片有：

- National Semiconductor DP83065 Saturn 千兆以太网
- Sun Cassini 千兆以太网
- Sun Cassini+ 千兆以太网

目前已知可与 `cas` 驱动配合工作的附加卡如下：

- Sun GigaSwift Ethernet 1.0 MMF（Cassini Kuheen）（部件号 501-5524）
- Sun GigaSwift Ethernet 1.0 UTP（Cassini）（部件号 501-5902）
- Sun GigaSwift Ethernet UTP（GCS）（部件号 501-6719）
- Sun Quad GigaSwift Ethernet UTP（QGE）（部件号 501-6522）
- Sun Quad GigaSwift Ethernet PCI-X（QGE-X）（部件号 501-6738）

## 参见

[altq(4)](altq.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`cas` 设备驱动出现于 FreeBSD 8.0 和 FreeBSD 7.3。其名称取自首次出现于 OpenBSD 4.1 的 `cas` 驱动，两者支持同一组控制器，但除此之外并无关联。

## 作者

`cas` 驱动由 Marius Strobl <marius@FreeBSD.org> 基于 [gem(4)](gem.4.md) 驱动编写。
