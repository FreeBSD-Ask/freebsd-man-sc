# hgame(4)

`hgame` — 通用 HID 游戏手柄、摇杆和控制器 evdev 驱动

## 名称

`hgame`

## 概要

`device hgame device hid device hidbus device hidmap device evdev`

`在 sysctl.conf(5) 中：dev.hgame.X.debug`

`在 loader.conf(5) 中：hw.hid.hgame.debug hgame_load`

## 描述

`hgame` 驱动支持附加到 HID 传输后端的通用游戏控制器，并通过 **evdev** 接口将其呈现给应用程序。

如果检测到相应硬件，[devmatch(8)](../man8/devmatch.8.md) 会自动加载该驱动。要在引导时手动加载驱动，请在 [loader(8)](../man8/loader.8.md) 提示符处将 `hgame_load` 变量设置为 `YES`，或将其添加到 loader.conf(5)。

要让用户应用程序访问游戏控制器，可通过将用户加入 *games* 组来允许用户访问 **`/dev/input/event*`** 节点。

## 硬件

`hgame` 驱动支持 HID 游戏手柄、摇杆和控制器，例如：

- 8bitdo USB Wireless Adapter 2

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.hgame.X.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

其默认值通过 [loader(8)](../man8/loader.8.md) 可调参数设置：

**`hw.hid.hgame.debug`**

## 文件

**`/dev/input/event*`** 输入事件设备 (**evdev**) 节点

## 参见

[iichid(4)](iichid.4.md), [ps4dshock(4)](ps4dshock.4.md), [usbhid(4)](usbhid.4.md), [xb360gp(4)](xb360gp.4.md), [devfs.rules(5)](../man5/devfs.rules.5.md)

## 历史

`hgame` 驱动首次出现于 FreeBSD 13.0。

## 作者

`hgame` 驱动由 Val Packett <val@packett.cool> 编写。

本手册页由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
