# cyapa(4)

`cyapa` — Cypress APA 触控板 I2C 接口驱动

## 名称

`cyapa`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device cyapa
> device ig4
> device iicbus

`或者，若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
cyapa_load="YES"
ig4_load="YES"
```

`在许多 Chromebook 型号上，可借助 chromebook_platform(4) 驱动自动配置此驱动。或者，可在 /boot/device.hints 中手动配置 cyapa 驱动：hint.cyapa.0.at="iicbus0" hint.cyapa.0.addr="0xCE" hint.cyapa.1.at="iicbus1" hint.cyapa.1.addr="0xCE"`

## 描述

`cyapa` 驱动为 Cypress APA 触控板提供支持。它模拟 IntelliMouse PS/2 协议。它支持基本的鼠标 ioctl，以便正确支持 [moused(8)](../man8/moused.8.md)。

### 触控板布局

```sh
                   2/3               1/3
          +--------------------+------------+
          |                    |   Middle   |
          |                    |   Button   |
          |       Left         |            |
          |      Button        +------------+
          |                    |   Right    |
          |                    |   Button   |
          +--------------------+............|
          |     Thumb/Button Area           | 15%
          +---------------------------------+
```

### 触控板特性

**`双指滚动`** 使用双指进行 Z 轴滚动。

**`按下按钮/第二指`** 当一根手指按下并保持触控板时，可使用第二根手指移动鼠标光标。这对于绘图或选择文本很有用。

**`拇指/按钮区域`** 触控板底部 15% 不会影响鼠标光标位置。这样可以使用食指控制光标，用拇指按压/保持触控板，从而实现高精度点击。

**`触控板按钮`** 按下物理按钮。触控板左侧三分之二发出左键事件。右上角发出中键事件。右下角发出右键事件。可选地，可启用轻触点击（见下文）。

在使用 [device.hints(5)](../man5/device.hints.5.md) 的系统上，可为 `cyapa` 配置以下值：

**`hint.cyapa.%d.at`** 目标 [iicbus(4)](iicbus.4.md)。

**`hint.cyapa.%d.addr`** `cyapa` 在 [iicbus(4)](iicbus.4.md) 上的 i2c 地址。

## SYSCTL 变量

这些 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**0** 禁用轻触点击。这是默认值。

**1** 轻触点击始终生成左键事件。

**2** 如果点击触控板左侧 2/3 区域则轻触点击生成左键事件，否则生成右键事件。

**3** 轻触点击生成鼠标按钮事件，如同按下物理按钮一样（见上文 Sx DESCRIPTION）。

**`debug.cyapa_idle_freq`** 空闲模式下的扫描频率，默认为 1。

**`debug.cyapa_slow_freq`** 慢速模式下的扫描频率，默认为 20。

**`debug.cyapa_norm_freq`** 正常模式下的扫描频率，默认为 100。

**`debug.cyapa_minpressure`** 检测手指的最小压力，默认为 12。

**`debug.cyapa_enable_tapclick`** 控制轻触点击。可能值为：

**`debug.cyapa_tapclick_min_ticks`** 产生点击的最小轻触持续时间（ticks），默认为 1。

**`debug.cyapa_tapclick_max_ticks`** 产生点击的最大轻触持续时间（ticks），默认为 8。

**`debug.cyapa_move_min_ticks`** 光标移动前的最小 ticks，默认为 4。

**`debug.cyapa_scroll_wait_ticks`** 开始滚动前等待的 ticks，默认为 0。

**`debug.cyapa_scroll_stick_ticks`** 单指滚动后阻止光标移动的 ticks，默认为 15。

**`debug.cyapa_thumbarea_percent`** 底部拇指区域大小的百分比，默认为 15。

**`debug.cyapa_debug`** 设置为非零值可启用到控制台和 syslog 的调试输出，默认为 0。

**`debug.cyapa_reset`** 设置为非零值会重新初始化设备。该 sysctl 会立即重置为零。

## 文件

`cyapa` 创建 `/dev/cyapa0`，将鼠标作为 `IntelliMouse PS/2` 设备呈现。它支持 [moused(8)](../man8/moused.8.md) 的 0 到 2 级，默认使用 1 级。

## 实例

要将 `cyapa` 与 [moused(8)](../man8/moused.8.md) 一起使用，请在 [rc.conf(5)](../man5/rc.conf.5.md) 文件中加入以下行：

```sh
moused_enable="YES"
```

```sh
moused_port="/dev/cyapa0"
```

如果不需要垂直滚动，将

```sh
moused_flags="-l0"
```

加入 [rc.conf(5)](../man5/rc.conf.5.md)。

通过在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 文件中加入以下行，启用左键和右键的轻触点击并禁用拇指区域：

```sh
debug.cyapa_thumbarea_percent=0
```

```sh
debug.cyapa_enable_tapclick=2
```

## 参见

[chromebook_platform(4)](chromebook_platform.4.md), [ig4(4)](ig4.4.md), [iicbus(4)](iicbus.4.md), [sysmouse(4)](sysmouse.4.md), [moused(8)](../man8/moused.8.md)

## 作者

最初的 `cyapa` 驱动由 Matthew Dillon 为 Dx 编写。

它由 Michael Gmelin <freebsd@grem.de> 移植、修改并增强到 FreeBSD。

本手册页由 Michael Gmelin <freebsd@grem.de> 编写。

## 缺陷

`cyapa` 驱动通过 I2C 地址检测设备。如果将初始化序列发送到该地址上的未知设备，可能会产生不可预见的后果。
