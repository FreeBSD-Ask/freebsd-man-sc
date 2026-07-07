# wsp(4)

`wsp` — Wellspring 触控板驱动

## 名称

`wsp`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device wsp
> device hid
> device usb

`或者，要在引导时以模块形式加载驱动，请将以下行放入 loader.conf(5)：`

```sh
wsp_load="YES"
```

## 描述

`wsp` 驱动为许多 Apple 笔记本电脑中常见的 Apple 内置触控板设备提供支持。

此驱动使用多指按下/点按检测来模拟三键鼠标。单指按下生成左键单击。双指按下映射到右键；而三指按下被视为中键单击。

触控板通过按下和点按工作。按下是完全用力的按压，会导致触控板物理下陷。点按是对触控板的触摸，不会使物理触控板下陷。

如果启用，`wsp` 驱动支持接收 evdev 输入设备数据。此数据用于触控板的扩展使用，如多指支持、压力检测、点按支持和手势。[sysctl(8)](../man8/sysctl.8.md) 可调参数 `kern.evdev.rcpt_mask` 至少必须设置第二位。可以使用 `kern.evdev.rcpt_mask=3` 启用。

垂直滚动（z 轴）默认启用，使用双指点按和手指上下移动。水平滚动（t 轴）不被 sysmouse 协议原生支持，因此必须使用 evdev 数据启用。可以使用 [sysctl(8)](../man8/sysctl.8.md) 可调参数 `kern.evdev.sysmouse_t_axis=3` 启用。水平滚动可使用双指点按和手指左右移动。[sysctl(8)](../man8/sysctl.8.md) 可调参数 `hw.usb.wsp.t_factor` 也必须大于 0 才能启用水平滚动。

三指点按的水平滑动根据方向注册为鼠标按钮 8 和 9。这些按钮默认为后退和前进键盘事件。

## SYSCTL 变量

以下变量作为 [sysctl(8)](../man8/sysctl.8.md) 可调参数可用：

**`hw.usb.wsp.scale_factor`** 控制指针灵敏度。默认为 12。

**`hw.usb.wsp.enable_single_tap_clicks`** 启用单指点按注册为左键单击。默认为 1（启用）。

**`hw.usb.wsp.enable_single_tap_movement`** 启用触控板上的移动跟随部分释放的左键单击。默认为 1（启用）。

**`hw.usb.wsp.max_finger_diameter`** 指定触控板上被注册为手指的最大手指直径（较低值用于手掌检测）。默认为 1900。

**`max_scroll_finger_distance`** 指定注册 z 轴和 t 轴移动时两根手指之间的最大距离。Z 轴和 T 轴移动分别是多点按（非点击）手指的垂直和水平移动。默认为 8192。

**`hw.usb.wsp.max_double_tap_distance`** 指定双指点击注册为右键单击时两根手指之间的最大距离。默认为 2500。

**`hw.usb.wsp.scr_threshold`** 指定注册为滚动手势所需的最小水平或垂直距离。默认为 20。

**`hw.usb.wsp.z_factor`** Z 轴灵敏度。默认为 5。

**`hw.usb.wsp.z_invert`** Z 轴反转。默认为 0（禁用）。

**`hw.usb.wsp.t_factor`** T 轴灵敏度。默认为 0（禁用）。

**`hw.usb.wsp.t_invert`** T 轴反转。默认为 0（禁用）。

**`hw.usb.wsp.scroll_finger_count`** 指定注册为滚动移动的点按手指数。默认为 2。

**`hw.usb.wsp.horizontal_swipe_finger_count`** 指定注册为滑动手势的点按手指数。默认为 3。

**`hw.usb.wsp.pressure_touch_threshold`** 指定手指注册为单击的阈值。默认为 50。

**`hw.usb.wsp.pressure_untouch_threshold`** 指定手指注册为释放单击的阈值。默认为 10。

**`hw.usb.wsp.pressure_tap_threshold`** 指定手指注册为点按的阈值。默认为 120。

**`hw.usb.wsp.debug`** 指定 `wsp` 驱动调试级别（0-3）。默认为 1。

## 文件

`wsp` 创建一个阻塞伪设备文件 **`/dev/wsp0`**，将鼠标呈现为 *sysmouse* 或 *mousesystems* 类型设备——有关这些鼠标类型的说明，请参见 [moused(8)](../man8/moused.8.md)。

## 参见

[sysmouse(4)](sysmouse.4.md), [usb(4)](usb.4.md), loader.conf(5), xorg.conf(5) (`ports/x11/xorg`), [moused(8)](../man8/moused.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

`wsp` 驱动由 Huang Wen Hui <huanghwh@gmail.com> 编写。
