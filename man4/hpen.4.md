# hpen.4

`hpen` — 兼容 MS Windows 的 HID 数位板驱动

## 名称

`hpen`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hpen
> device hid
> device hidbus
> device hidmap
> device evdev

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hpen_load="YES"
```

## 描述

`hpen` 驱动为连接到 HID 传输后端的通用兼容 MS Windows 的 HID 数位板和数字化仪提供支持。参见 [iichid(4)](iichid.4.md) 或 [usbhid(4)](usbhid.4.md)。

`/dev/input/event*` 设备将数位板呈现为 `evdev` 类型设备。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.hpen.X.debug`** 调试输出级别，0 表示禁用调试，值越大调试消息越详细。默认为 0。

其默认值通过 [loader(8)](../man8/loader.8.md) 可调参数设置：

**`hw.hid.hpen.debug`**

## 文件

**`/dev/input/event*`** 输入事件设备节点。

## 参见

[iichid(4)](iichid.4.md), [usbhid(4)](usbhid.4.md), xorg.conf(5) (`ports/x11/xorg`)

## 缺陷

`hpen` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作。

不支持数位笔电池电量报告。

## 历史

`hpen` 驱动最早出现在 FreeBSD 13.0 中。

## 作者

`hpen` 驱动由 Val Packett <val@packett.cool> 编写。

本手册页由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
