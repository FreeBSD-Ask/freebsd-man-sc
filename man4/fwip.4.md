# fwip.4

`fwip` — IP over FireWire 驱动程序

## 名称

`fwip`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device firewire
> device fwip

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
firewire_load="YES"
if_fwip_load="YES"
```

## 描述

`fwip` 驱动程序基于 RFC 2734 和 RFC 3146 中描述的协议，提供标准的 IP over FireWire（IEEE 1394）。

[firewire(4)](firewire.4.md) 和 [fwohci(4)](fwohci.4.md) 驱动程序也必须在内核中配置。

如果使用 `DEVICE_POLLING` 选项编译，本驱动程序还支持 [polling(4)](polling.4.md)。

## 参见

arp(4), [firewire(4)](firewire.4.md), [fwe(4)](fwe.4.md), [fwohci(4)](fwohci.4.md), [netintro(4)](netintro.4.md), [polling(4)](polling.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [kldload(8)](../man8/kldload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`fwip` 设备驱动程序首次出现于 FreeBSD 5.3。

## 作者

`fwip` 驱动程序和本手册页由 Doug Rabson 编写，基于 Hidetoshi Shimokawa 的早期工作。

## 缺陷

本驱动程序目前不支持用于 FireWire 上多播 IP 的 MCAP 协议。多播数据包被视为广播数据包，这对于大多数简单的多播用途已足够。
