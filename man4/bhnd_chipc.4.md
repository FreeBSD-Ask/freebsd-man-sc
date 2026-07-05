# bhnd_chipc.4

`bhnd_chipc` — Broadcom 家庭网络部门 ChipCommon 驱动

## 名称

`bhnd_chipc`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd

要编译支持嵌入式系统中所有附加设备的驱动，请在内核配置文件中加入以下额外行：

> device cfi
> device gpio
> device spibus
> device uart

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bhnd_load="YES"
```

## 描述

`bhnd_chipc` 驱动支持 Broadcom 家庭网络部门网络芯片组和嵌入式系统中使用的 ChipCommon 核心。

ChipCommon 核心提供对通用硬件设施的接口，包括设备识别、UART、CFI 与 SPI flash、一次性可编程（OTP）存储器以及 GPIO。

## 参见

[bhnd(4)](bhnd.4.md), [intro(4)](intro.4.md)

## 历史

`bhnd_chipc` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`bhnd_chipc` 驱动由 Landon Fuller <landonf@FreeBSD.org> 和 Michael Zhilin <mizhka@FreeBSD.org> 编写。
