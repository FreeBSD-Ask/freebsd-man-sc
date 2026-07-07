# led(4)

`led` — 操作 LED、灯和其他指示器的 API

## 名称

`led`

## 概要

`#include <dev/led/led.h>`

`Fd typedef void led_t(void *priv, int onoff); Ft struct cdev * Fn led_create_state led_t *func void *priv char const *name int state Ft struct cdev * Fn led_create led_t *func void *priv char const *name Ft void Fn led_destroy struct cdev *`

## 描述

`led` 驱动提供处理 LED、灯和其他指示器的通用支持。

硬件驱动必须提供一个用于打开和关闭指示器的函数，以及相对于 `/dev/led/` 的指示器设备 `name`。`priv` 参数传回给此开/关函数，可由硬件驱动自行决定如何使用。

可通过打开并向 `/dev/led/bla` 设备写入 ASCII 字符串来控制灯。

在以下内容中，我们将使用此特殊表示法来表示指示器的输出：

**`*`** 指示器亮 1/10 秒。

**`_`** 指示器灭 1/10 秒。

可直接设置状态，由于更改立即发生，因此可以以非常短的周期闪烁指示器并将其与程序事件同步。应注意存在非平凡的开销，因此这可能不适用于基准测试或测量短间隔。

**`0`** 立即关闭指示器。

**`1`** 立即打开指示器。

可设置给定周期的闪烁。模式无限循环。

**`f`** _*

**`f1`** _*

**`f2`** __**

**`f3`** ___***

**`...`**

**`f9`** _________*********

提供三个高级命令：

**`.`** 变为 `_*`

**`-`** 变为‘`_***`’

**`\`** 变为‘`__`’

**`en`** 变为‘`____`’

**`d%d`** 数字。每个数字以 1/10 秒闪烁，零为十次脉冲。数字之间暂停一秒，最后一个数字后暂停两秒，然后重复序列。

**`s%s`** 字符串。这给予对指示器的完全控制。字母 `A` ... `J` 将指示器亮 1/10 秒到整整一秒。字母 `a` ... `j` 将指示器灭 1/10 秒到整整一秒。字母 `u` 和 `U` 分别在下一个 UTC 秒开始时关闭和打开指示器。除非以 `.` 终止，否则序列立即重复。

**`m%s`** 摩斯码。

序列在一秒暂停后重复。

## 文件

**`/dev/led/*`**

## 实例

‘`d12`’闪烁灯

```sh
*__________*_*______________________________
```

‘`sAaAbBa`’闪烁

```sh
*_*__**_
```

```sh
/usr/bin/morse -l "Soekris rocks" > /dev/led/error
```

## 参见

morse(6)

## 历史

`led` 驱动最早出现于 FreeBSD 5.2。

## 作者

此软件由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。

本手册页由 Sergey A. Osokin <osa@FreeBSD.org> 和 Poul-Henning Kamp <phk@FreeBSD.org> 编写。
