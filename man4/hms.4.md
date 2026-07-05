# hms.4

`hms` — HID 鼠标驱动

## 名称

`hms`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hms
> device hidbus
> device hid
> device evdev

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hms_load="YES"
```

## 描述

`hms` 驱动为附加到 HID 传输后端的 HID 鼠标提供支持。参见 [iichid(4)](iichid.4.md) 或 [usbhid(4)](usbhid.4.md)。支持任意数量按钮的鼠标、带滚轮的鼠标以及绝对鼠标。

**`/dev/input/eventX`** 设备将鼠标以 `evdev` 类型设备的方式呈现。

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.hms.X.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

其默认值派生自 [loader(8)](../man8/loader.8.md) 可调参数：

**`hw.hid.hms.debug`**

## 文件

**`/dev/input/eventX`** 输入事件设备节点。

## 参见

[iichid(4)](iichid.4.md), [usbhid(4)](usbhid.4.md), xorg.conf(5) (`ports/x11/xorg`)

## 缺陷

`hms` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作

## 作者

`hms` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

本手册页最初由 Nick Hibma <n_hibma@FreeBSD.org> 为 umt(4) 驱动编写，并由 Vladimir Kondratyev <wulf@FreeBSD.org> 适配到 `hms`。
