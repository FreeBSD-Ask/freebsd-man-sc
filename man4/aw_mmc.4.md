# aw_mmc(4)

`aw_mmc` — Allwinner SoC 中 SD/MMC 控制器驱动

## 名称

`aw_mmc`

## 概要

`device mmc`

## 描述

`aw_mmc` 设备驱动为 Allwinner SD/MMC 主控制器提供支持。

## 硬件

当前版本的 `aw_mmc` 驱动支持具有以下兼容字符串之一的 SD/MMC 控制器：

- allwinner,sun4i-a10-mmc
- allwinner,sun5i-a13-mmc
- allwinner,sun7i-a20-mmc
- allwinner,sun50i-a64-mmc
- allwinner,sun20i-d1-mmc

## SYSCTL 变量

以下只读变量可通过 [sysctl(8)](../man8/sysctl.8.md) 访问：

**`dev.aw_mmc.req_timeout`** 请求超时时间（单位为秒，默认：10）。

## 参见

[fdt(4)](fdt.4.md), [mmc(4)](mmc.4.md)

## 历史

`aw_mmc` 设备驱动最初由 Alexander Fedorov <alexander.fedorov@rtlservice.com> 编写。后续工作及本手册页由 Emmanuel Vadot <manu@freebsd.org> 完成。
