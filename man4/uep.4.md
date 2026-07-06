# uep.4

`uep` — eGalax 触摸屏驱动

## 名称

`uep`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device uep
> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uep_load="YES"
```

若要编译此驱动并启用 evdev 支持，请将以下行加入内核配置文件：

> options EVDEV_SUPPORT
> device evdev

## 描述

`uep` 驱动为 eGalax 屏幕触摸面板提供支持。

该驱动是一个桩驱动。它仅探测并附加到 USB 设备，创建设备条目，并将从硬件重新组装的数据包馈送至该设备。依据编译时的内核选项，它支持原生或 evdev 操作模式。

要在原生模式下使鼠标在 X(7)（`ports/x11/xorg-docs`）中工作，请安装 `ports/x11-drivers/xf86-input-egalax`。

要在 evdev 模式下使鼠标在 X(7)（`ports/x11/xorg-docs`）中工作，请安装 `ports/x11-drivers/xf86-input-evdev`。

## 文件

`uep` 会创建一个阻塞型伪设备文件，原生模式下为 **`/dev/uep0`**，evdev 模式下为 **`/dev/input/eventN`**。

## 参见

[usb(4)](usb.4.md), loader.conf(5), xorg.conf(5)（`ports/x11/xorg`），egalax(4)（`ports/x11-drivers/xf86-input-egalax`），evdev(4)（`ports/x11-drivers/xf86-input-evdev`）。

## 作者

`uep` 驱动由 Gleb Smirnoff <glebius@FreeBSD.org> 编写。

## 缺陷

`uep` 无法像 [sysmouse(4)](sysmouse.4.md) 那样工作，因为 [sysmouse(4)](sysmouse.4.md) 不支持绝对运动事件。
