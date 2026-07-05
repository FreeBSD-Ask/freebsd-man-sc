# ncthwm.4

`ncthwm` — Nuvoton Super I/O 上的硬件监控控制器

## 名称

`ncthwm`

## 概要

`device ncthwm device superio`

## 描述

`ncthwm` 是可在 Nuvoton Super I/O 芯片中找到的硬件监控控制器的驱动程序。它通过 [sysctl(8)](../man8/sysctl.8.md) 公开风扇转速。

`ncthwm` 驱动支持以下芯片：

- Nuvoton NCT6779
- Nuvoton NCT6796D-E

## SYSCTL 变量

这些变量作为只读 [sysctl(8)](../man8/sysctl.8.md) 变量提供：

**`dev.ncthwm.0.CPUFAN`** CPU 风扇转速（RPM）。

**`dev.ncthwm.0.SYSFAN`** 系统风扇转速（RPM）。

**`dev.ncthwm.0.AUXFAN0`** AUX0 风扇转速（RPM）。

**`dev.ncthwm.0.AUXFAN1`** AUX1 风扇转速（RPM）。

**`dev.ncthwm.0.AUXFAN2`** AUX2 风扇转速（RPM）。

## 历史

该驱动首次出现于 FreeBSD 14.0。

## 作者

该驱动最初由 Stéphane Rochoy <stephane.rochoy@stormshield.eu> 编写。
