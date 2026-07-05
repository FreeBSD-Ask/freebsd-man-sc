# fwe.4

`fwe` — FireWire 的以太网模拟驱动程序

## 名称

`fwe`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device firewire
> device fwe

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_fwe_load="YES"
```

## 描述

`fwe` 驱动程序通过 FireWire（IEEE 1394）提供非标准的以太网模拟。

[firewire(4)](firewire.4.md) 和 [fwohci(4)](fwohci.4.md) 也必须在内核中配置。

本驱动程序利用 IEEE 1394 上的异步流来承载以太网帧。流通道可通过 `hw.firewire.fwe.stream_ch` [sysctl(8)](../man8/sysctl.8.md) 指定。

如果使用 `DEVICE_POLLING` 选项编译，本驱动程序还支持 [polling(4)](polling.4.md)。

## 参见

arp(4), [firewire(4)](firewire.4.md), [fwip(4)](fwip.4.md), [fwohci(4)](fwohci.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [kldload(8)](../man8/kldload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`fwe` 设备驱动程序首次出现于 FreeBSD 5.0。

## 作者

`fwe` 驱动程序和本手册页由 Hidetoshi Shimokawa 编写。

## 缺陷

本驱动程序以一种非常临时的方式模拟以太网，且不使用等时管理器预留流通道。注意，本驱动程序使用的协议与 RFC 2734（IPv4 over IEEE 1394）非常不同。
