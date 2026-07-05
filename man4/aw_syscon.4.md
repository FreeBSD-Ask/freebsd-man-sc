# aw_syscon.4

`aw_syscon` — Allwinner SoC 中系统控制器驱动

## 名称

`aw_syscon`

## 描述

`aw_syscon` 设备驱动为 Allwinner 系统控制器提供支持。此控制器提供寄存器，将相关功能汇集到公共空间中。在受支持的设备上，`aw_syscon` 是以太网功能所必需的。

## 硬件

`aw_syscon` 驱动支持具有以下兼容字符串之一的系统控制器：

- allwinner,sun50i-a64-system-controller
- allwinner,sun50i-a64-system-control
- allwinner,sun8i-a83t-system-controller
- allwinner,sun8i-h3-system-controller
- allwinner,sun8i-h3-system-control
- allwinner,sun50i-h5-system-control
- allwinner,sun20i-d1-system-control

## 作者

`aw_syscon` 设备驱动由 Kyle Evans <kevans@FreeBSD.org> 编写。
