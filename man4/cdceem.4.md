# cdceem(4)

`cdceem` — USB 通信设备类以太网仿真模型驱动

## 名称

`cdceem`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device cdceem

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_cdceem_load="YES"
```

## 描述

`cdceem` 驱动为基于 USB 通信设备类以太网仿真模型（CDC EEM）规范的 USB 设备提供支持。

该驱动在主机端和设备端均可工作；参见 [usb_template(4)](usb_template.4.md) 获取详细信息。

USB 设备在两侧都呈现为常规网络接口，传输以太网帧。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

`cdceem` 驱动不支持不同的媒体类型或选项。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.cdceem.debug`** `cdceem` 驱动日志消息的详细级别。设置为 0 禁用日志记录，设置为 1 警告潜在问题。较大的值启用调试输出。默认为 1。

**`hw.usb.cdceem.send_echoes`** 如果设置为 1，驱动将在接口启动时发送 Echo EEM 数据包。虽然响应 Echo 是强制性的，但某些设备无法处理它。仅用于调试。默认为 0。

**`hw.usb.cdceem.send_fake_crc`** 如果设置为 1，驱动将使用 0xdeadbeef 作为传出 Data EEM 数据包的 CRC 值。仅用于调试。默认为 0。

## 参见

arp(4), [cdce(4)](cdce.4.md), [intro(4)](intro.4.md), [ipheth(4)](ipheth.4.md), [netintro(4)](netintro.4.md), [urndis(4)](urndis.4.md), [usb(4)](usb.4.md), [usb_template(4)](usb_template.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Universal Serial Bus Communications Class Subclass Specification for Ethernet Emulation Model Devices"。

## 历史

`cdceem` 设备驱动首次出现于 FreeBSD 12.1。

## 作者

`cdceem` 驱动由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 Hewlett Packard Enterprise 赞助下编写。
