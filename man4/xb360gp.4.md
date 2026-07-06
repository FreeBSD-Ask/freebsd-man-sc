# xb360gp.4

`xb360gp` — XBox 360 手柄驱动

## 名称

`xb360gp`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device xb360gp
> device hgame
> device hid
> device hidbus
> device hidmap
> device evdev

`或者，要在引导时以模块形式加载驱动，请将以下行放入 loader.conf(5)：`

```sh
xb360gp_load="YES"
```

## 描述

`xb360gp` 驱动为 XBox 360 手柄驱动提供支持。

**`/dev/input/event*`** 设备将游戏控制器呈现为 `evdev` 类型设备。*games* 组的成员可以访问它。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.xb360gp.X.debug`** 调试输出级别，其中 0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

其默认值通过 [loader(8)](../man8/loader.8.md) 可调参数设置：

**`hw.hid.xb360gp.debug`**

## 文件

**`/dev/input/event*`** 输入事件设备节点。

## 历史

`xb360gp` 驱动首次出现于 FreeBSD 13.0。

## 作者

`xb360gp` 驱动由 Val Packett <val@packett.cool> 编写。

本手册页由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
