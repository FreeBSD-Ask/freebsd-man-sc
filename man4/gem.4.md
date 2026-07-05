# gem.4

`gem` — GEM/GMAC 以太网设备驱动程序

## 名称

`gem`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device gem

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_gem_load="YES"
```

## 描述

`gem` 驱动程序为 GMAC 以太网硬件提供支持，这些硬件主要见于最后一批 Apple PowerBook G3 和大多数基于 G4 的 Apple 硬件。

`gem` 驱动程序支持的所有控制器在接收和发送方面均具有 TCP 校验和卸载能力，支持 [vlan(4)](vlan.4.md) 的扩展帧接收和发送，以及 512 位多播哈希过滤器。

## 硬件

`gem` 驱动程序支持的芯片包括：

- Apple GMAC
- Sun GEM Gigabit Ethernet

目前已知可与 `gem` 驱动程序配合工作的附加卡如下：

- Sun Gigabit Ethernet PCI 2.0/3.0 (GBE/P)（部件号 501-4373）

## 参见

[altq(4)](altq.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`gem` 设备驱动程序出现于 NetBSD 1.6。第一个包含它的 FreeBSD 版本是 FreeBSD 5.0。

## 作者

`gem` 驱动程序由 Eduardo Horvath <eeh@NetBSD.org> 为 NetBSD 编写。由 Thomas Moestl <tmm@FreeBSD.org> 移植到 FreeBSD，后由 Marius Strobl <marius@FreeBSD.org> 改进。手册页由 Thomas Klausner <wiz@NetBSD.org> 编写。
