# uled(4)

`uled` — USB LED 驱动

## 名称

`uled`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device uled
> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uled_load="YES"
```

## 描述

`uled` 驱动为 Dream Cheeky WebMail Notifier 和 ThingM blink(1) 通知 LED 提供支持。

随后，用户空间应用程序可使用 **`/dev/uled0`** 设备。

## IOCTLS

可在 **`/dev/uled0`** 上执行以下 ioctl(2) 命令，这些命令定义于

`#include <dev/usb/uled_ioctl.h>`

```sh
struct uled_color {
	uint8_t	red;
	uint8_t	green;
	uint8_t	blue;
};
```

**`ULED_GET_COLOR`** 此命令返回 LED 的 RGB 颜色值。此 ioctl(2) 使用以下结构：

**`ULED_SET_COLOR`** 此命令设置 LED 的 RGB 颜色值。它使用与上述相同的结构。

## 文件

**`/dev/uled0`** 阻塞型设备节点

## 参见

[ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md)

## 作者

`uled` 驱动由 Kevin Lo <kevlo@FreeBSD.org> 编写。
