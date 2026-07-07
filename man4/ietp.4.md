# ietp(4)

`ietp` — Elantech I2C 触摸板设备驱动

## 名称

`ietp`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device ietp
> device hidbus
> device hid
> device iichid
> device iicbus
> device evdev

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ietp_load="YES"
```

## 描述

`ietp` 驱动为许多笔记本电脑中存在的 Elantech I2C 触摸板多点触控设备提供支持。

要在 X(7)（`ports/x11/xorg-docs`）中使多点触控设备正常工作，请安装 `ports/x11-drivers/xf86-input-libinput`。

## 文件

`ietp` 创建一个伪设备文件 `/dev/input/eventX`，将多点触控设备呈现为输入事件设备。

## 参见

hid(4), loader.conf(5), xorg.conf(5) (`ports/x11/xorg`), libinput(4) (`ports/x11-drivers/xf86-input-libinput`).

## 作者

`ietp` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

## 缺陷

`ietp` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作。
