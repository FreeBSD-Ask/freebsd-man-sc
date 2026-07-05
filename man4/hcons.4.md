# hcons.4

`hcons` — HID 消费者页面控制驱动

## 名称

`hcons`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hcons
> device hid
> device hidbus
> device hidmap
> device evdev

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hcons_load="YES"
```

## 描述

`hcons` 驱动提供对 HID 消费者页面控制的支持，最常见的用途是作为许多键盘上的“多媒体按键”。

**`/dev/input/event*`** 设备将消费者页面控制以 `evdev` 类型设备的方式呈现。

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.hcons.X.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

其默认值通过 [loader(8)](../man8/loader.8.md) 可调参数设置：

**`hw.hid.hcons.debug`**

## 文件

**`/dev/input/event*`** 输入事件设备节点。

## 参见

[iichid(4)](iichid.4.md), [usbhid(4)](usbhid.4.md)

## 历史

`hcons` 驱动首次出现于 FreeBSD 13.0。

## 作者

`hcons` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
