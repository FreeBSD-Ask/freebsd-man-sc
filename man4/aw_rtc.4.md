# aw_rtc.4

`aw_rtc` — Allwinner SoC 中实时时钟（RTC）控制器驱动

## 名称

`aw_rtc`

## 描述

`aw_rtc` 设备驱动为 Allwinner RTC 控制器提供支持。

## 硬件

当前版本的 `aw_rtc` 驱动支持具有以下任意兼容字符串之一的 RTC 控制器：

- allwinner,sun4i-a10-rtc
- allwinner,sun7i-a20-rtc
- allwinner,sun6i-a31-rtc
- allwinner,sun8i-h3-rtc
- allwinner,sun20i-d1-rtc
- allwinner,sun50i-h5-rtc
- allwinner,sun50i-h6-rtc

## 历史

`aw_rtc` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`aw_rtc` 设备驱动由 Vladimir Belian <fate10@gmail.com> 编写。本手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
