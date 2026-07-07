# atp(4)

`atp` — Apple 触控板驱动

## 名称

`atp`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device atp
> device hid
> device usb

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
atp_load="YES"
```

## 描述

`atp` 驱动为许多 Apple 笔记本中内置的 Apple Internal Trackpad 设备提供支持。较旧的（Fountain/Geyser）和较新的（Wellspring）触控板系列都通过统一的驱动提供支持。

该驱动通过多指敲击检测来模拟三键鼠标。单指敲击产生左键点击；双指敲击映射为中键；三指敲击则被视为右键点击。

支持双指水平滚动，对应于页面向后/向前事件；垂直多指滚动则模拟鼠标滚轮。

双击后紧接拖动的操作被视为选择手势；在拖动持续期间假定按住虚拟左键。

`atp` 支持使用 [sysctl(8)](../man8/sysctl.8.md) 进行动态重配置，通过 `hw.usb.atp` 下的节点进行。指针灵敏度可通过 sysctl 可调参数 `hw.usb.atp.scale_factor` 控制。`scale_factor` 的值越小，移动越快。简单的通高通滤波器用于减弱小幅移动的影响；此滤波器的阈值可由 `hw.usb.atp.small_movement` 控制。触摸手势的最大可容忍持续时间由 `hw.usb.atp.touch_timeout`（单位为微秒）控制；超过此时间的触摸被视为滑动。（当手指划动累积移动量至少达到 `hw.usb.atp.slide_min_movement`（单位为 mickey）时，也会发生此转换。）允许的双击与拖动手势之间关联的最大时间（单位为微秒）可由 `hw.usb.atp.double_tap_threshold` 控制。若想禁用敲击检测而仅依赖物理按键按下，可将以下 sysctl 设置为 2：`hw.usb.atp.tap_minimum`。

## 硬件

`atp` 驱动支持以下产品 ID：

- PowerBooks、iBooks（ID：0x020e、0x020f、0x0210、0x0214、0x0215、0x0216）
- Core Duo MacBook 与 MacBook Pro（ID：0x0217、0x0218、0x0219）
- Core2 Duo MacBook 与 MacBook Pro（ID：0x021a、0x021b、0x021c）
- Core2 Duo MacBook3,1（ID：0x0229、0x022a、0x022b）
- 12 英寸 PowerBook 与 iBook（ID：0x030a、0x030b）
- 15 英寸 PowerBook（ID：0x020e、0x020f、0x0215）
- 17 英寸 PowerBook（ID：0x020d）
- 几乎所有近期的 MacBook Pro 与 Air（ID：0x0223、0x0223、0x0224、0x0224、0x0225、0x0225、0x0230、0x0230、0x0231、0x0231、0x0232、0x0232、0x0236、0x0236、0x0237、0x0237、0x0238、0x0238、0x023f、0x023f、0x0240、0x0241、0x0242、0x0243、0x0244、0x0245、0x0246、0x0247、0x0249、0x024a、0x024b、0x024c、0x024d、0x024e、0x0252、0x0252、0x0253、0x0253、0x0254、0x0254、0x0259、0x025a、0x025b、0x0262、0x0262、0x0263、0x0264、0x0290、0x0291、0x0292）

要查看触控板的产品 ID，可在 lshal(1) 的输出中搜索 "Trackpad"，并查看属性 `usb_device.product_id`。

## 文件

`atp` 创建一个阻塞式伪设备文件 **`/dev/atp0`**，将鼠标呈现为 `sysmouse` 或 `mousesystems` 类型设备——关于这些鼠标类型的说明，参见 [moused(8)](../man8/moused.8.md)。

## 参见

[sysmouse(4)](sysmouse.4.md), [usb(4)](usb.4.md), loader.conf(5), xorg.conf(5)（`ports/x11/xorg`），[moused(8)](../man8/moused.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

`atp` 驱动由 Rohit Grover <rgrover1@gmail.com> 编写。
