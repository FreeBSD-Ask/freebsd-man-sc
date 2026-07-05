# firewire.4

`firewire` — IEEE1394 高性能串行总线

## 名称

`firewire`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device firewire

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
firewire_load="YES"
```

## 弃用通知

`firewire` 驱动程序计划在 FreeBSD 16.0 之前移除。

## 描述

FreeBSD 为 `firewire` 接口提供机器无关的总线支持和原始驱动程序。

`firewire` 驱动程序由两层组成：控制器层和总线层。控制器附着到物理总线（如 [pci(4)](pci.4.md)）。`firewire` 总线附着到控制器。其他驱动程序可附着到总线。

最多 63 台设备（包括主机本身）可连接到 `firewire` 总线。根节点通过 PHY 设备功能动态分配。其他 `firewire` 总线特定参数（如节点 ID、cycle master、isochronous resource manager 和 bus manager）在发起总线复位后动态分配。在 `firewire` 总线上，每台设备由 EUI 64 地址标识。

可通过 [dcons(4)](dcons.4.md) 驱动程序在 firewire 接口上进行调试。有关如何设置 firewire 调试的详情，请参见 <https://docs.freebsd.org/en/books/developers-handbook/kerneldebug/#kerneldebug-dcons>。

## 文件

**`/dev/fw0.0`**

**`/dev/fwmem0.0`**

## 参见

[dcons(4)](dcons.4.md), [fwe(4)](fwe.4.md), [fwip(4)](fwip.4.md), [fwohci(4)](fwohci.4.md), [pci(4)](pci.4.md), [sbp(4)](sbp.4.md), [eui64(5)](../man5/eui64.5.md), fwcontrol(8), [kldload(8)](../man8/kldload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`firewire` 驱动程序首次出现于 FreeBSD 5.0。

## 作者

`firewire` 驱动程序由 Katsushi Kobayashi 和 Hidetoshi Shimokawa 为 FreeBSD 项目编写。

## 缺陷

安全说明请参见 [fwohci(4)](fwohci.4.md)。
