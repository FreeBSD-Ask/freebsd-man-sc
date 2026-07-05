# hsctrl.4

`hsctrl` — HID 系统控制驱动

## 名称

`hsctrl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hsctrl
> device hid
> device hidbus
> device hidmap
> device evdev

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hsctrl_load="YES"
```

## 描述

`hsctrl` 驱动为 HID 系统控制提供支持，最常用于许多键盘上的"电源关闭/睡眠键"。

`/dev/input/event*` 设备将消费页控制呈现为 `evdev` 类型设备。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.hsctrl.X.debug`** 调试输出级别，0 表示禁用调试，值越大调试消息越详细。默认为 0。

其默认值通过 [loader(8)](../man8/loader.8.md) 可调参数设置：

**`hw.hid.hsctrl.debug`**

## 文件

**`/dev/input/event*`** 输入事件设备节点。

## 参见

[iichid(4)](iichid.4.md), [usbhid(4)](usbhid.4.md)

## 历史

`hsctrl` 驱动最早出现在 FreeBSD 13.0 中。

## 作者

`hsctrl` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
