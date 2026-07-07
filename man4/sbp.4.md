# sbp(4)

`sbp` — Serial Bus Protocol 2 (SBP-2) 大容量存储设备驱动

## 名称

`sbp`

## 概要

`kldload firewire kldload cam kldload sbp`

`或`

`device sbp device firewire device scbus device da device cd device pass`

## 描述

`sbp` 驱动为连接到 FireWire（IEEE 1394）端口的 SBP-2 设备提供支持。它应与 CAM 层支持的 SBP-2 设备一起工作，例如 HDD、CDROM 驱动器和 DVD 驱动器。

熟悉 [umass(4)](umass.4.md) 的某些用户可能会想知道为什么设备拔出时不在 CAM 层分离。仅在多次总线重置期间未再次插入设备时才分离。这是为了在总线重置后由于某种原因无法正确探测设备，或用户更改总线拓扑导致设备临时断开时，防止分离活动文件系统。如果要强制分离设备，请多次运行 `fwcontrol -r` 或通过 [sysctl(8)](../man8/sysctl.8.md) 设置 `hw.firewire.hold_count=0`。

某些（有缺陷的）HDD 在标记队列方面工作不正常。如果遇到此类驱动器问题，请尝试 `camcontrol [device id] tags -N 1` 禁用标记队列。

## 硬件

`sbp` 驱动支持 FireWire Serial Bus Protocol 2（SBP-2）存储设备。

## 参见

cam(4), [firewire(4)](firewire.4.md), [camcontrol(8)](../man8/camcontrol.8.md), fwcontrol(8), [kldload(8)](../man8/kldload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

`sbp` 驱动由 Katsushi Kobayashi 和 Hidetoshi Shimokawa 编写。

本手册页由 Katsushi Kobayashi 编写。
