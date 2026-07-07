# ums(4)

`ums` — USB 鼠标驱动

## 名称

`ums`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ums
> device hid
> device uhci
> device ohci
> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ums_load="YES"
```

## 描述

`ums` 驱动为连接到 USB 端口的鼠标提供支持。支持任意数量按键的鼠标以及带滚轮的鼠标。

**/dev/ums0** 设备将鼠标呈现为 `sysmouse` 或 `mousesystems` 类型设备。有关这些鼠标类型的说明，请参见 [moused(8)](../man8/moused.8.md)。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`hw.usb.ums.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 文件

**/dev/ums0** 阻塞型设备节点

## 实例

将系统上的第一个 USB 鼠标作为控制台鼠标使用：

```sh
moused -p /dev/ums0 -t auto
```

要在 X 下使用 USB 鼠标，请将 `xorg.conf` 中的 "Pointer" 段修改为如下内容：

```sh
Device /dev/ums0
```

```sh
Protocol Auto
```

如果你希望同时在虚拟控制台和 X 中使用鼠标，请将其改为：

```sh
Device /dev/sysmouse
```

```sh
Protocol Auto
```

## 参见

[ohci(4)](ohci.4.md), [sysmouse(4)](sysmouse.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), xorg.conf(5) (**ports/x11/xorg**), [moused(8)](../man8/moused.8.md)

## 作者

`xorg.conf` 驱动由 Lennart Augustsson <augustss@cs.chalmers.se> 为 NetBSD 编写，并由 MAEKAWA Masahide <bishop@rr.iij4u.or.jp> 移植到 FreeBSD。

本手册页由 Nick Hibma <n_hibma@FreeBSD.org> 编写，Kazutaka YOKOTA <yokota@zodiac.mech.utsunomiya-u.ac.jp> 提供了输入。
