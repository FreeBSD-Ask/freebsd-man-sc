# hmt(4)

`hmt` — 兼容 MS Windows 7/8/10 的 HID 多点触控设备驱动

## 名称

`hmt`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hmt
> device hidbus
> device hid
> device hconf
> device evdev

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hmt_load="YES"
```

## 描述

`hmt` 驱动为许多笔记本电脑中常见的兼容 MS Windows 7/8/10 的 HID 多点触控设备提供支持。

要让多点触控设备在 X(7) (`ports/x11/xorg-docs`) 中工作，请安装 `ports/x11-drivers/xf86-input-evdev`。

## 文件

`hmt` 创建一个伪设备文件 **`/dev/input/eventX`**，将多点触控设备呈现为输入事件设备。

## 参见

hid(4), loader.conf(5), xorg.conf(5) (`ports/x11/xorg`), evdev(4) (`ports/x11-drivers/xf86-input-evdev`).

## 作者

`hmt` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

## 缺陷

`hmt` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作
