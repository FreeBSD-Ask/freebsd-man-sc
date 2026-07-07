# linuxkpi(4)

`linuxkpi` — Linux 内核编程接口支持

## 名称

`linuxkpi`

## 描述

`linuxkpi` 内核模块提供一个有限的 KPI（内核编程接口），允许 Linux 内核驱动和其他 Linux 内核代码在 FreeBSD 上编译，并几乎无需修改即可与 FreeBSD 内核一起使用。

从历史上看，*OpenFabrics Enterprise Distribution（Infiniband）* 以及某些厂商驱动曾使用 `linuxkpi`。如今，用于图形驱动支持的 *drm-kmod* 和用于无线驱动的 [linuxkpi_wlan(4)](linuxkpi_wlan.4.md) 是其主要的使用者。

不要将 `linuxkpi` 与 [linux(4)](linux.4.md) 混淆，后者提供有限的 Linux ABI（应用二进制接口）兼容性，用于在 FreeBSD 上原样运行 Linux 应用二进制文件。

## 参见

[linuxkpi_wlan(4)](linuxkpi_wlan.4.md)
