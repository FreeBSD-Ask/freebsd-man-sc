# wmt(4)

`wmt` — 兼容 MS Windows 7/8/10 的 USB HID 多点触控设备驱动

## 名称

`wmt`

## 概要

`要将此驱动编译进内核，请将以下行加入你的内核配置文件：`

> device wmt
> device usb
> device hid
> device evdev

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
wmt_load="YES"
```

## 描述

`wmt` 驱动为许多笔记本电脑中存在的兼容 MS Windows 7/8/10 的 USB HID 多点触控设备提供支持。

要在 X(7)（`ports/x11/xorg-docs`）中使多点触控设备工作，请安装 `ports/x11-drivers/xf86-input-evdev`。

## 文件

`wmt` 创建一个伪设备文件 **/dev/input/eventX**，将多点触控设备呈现为输入事件设备。

## 参见

[usb(4)](usb.4.md), loader.conf(5), xorg.conf(5)（`ports/x11/xorg`）, evdev(4)（`ports/x11-drivers/xf86-input-evdev`）。

## 作者

`wmt` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

## 缺陷

`wmt` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作，因为 [sysmouse(4)](sysmouse.4.md) 不支持绝对运动事件。
