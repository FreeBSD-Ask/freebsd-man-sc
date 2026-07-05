# en.4

`en` — 基于 Midway 的 ATM 接口设备驱动程序

## 名称

`en`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device en
> device atm
> device utopia

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_en_load="YES"
```

## 描述

`en` 设备驱动程序支持基于 Midway 的 ATM 接口，包括 Efficient Networks, Inc. ENI-155 和 Adaptec ANA-59x0。Midway 是一种 AAL5 SAR（分段与重组）芯片。

有关配置卡以支持 IP，请参见 natmip(4)。

除 utopia(4) 处理的 sysctl 之外，驱动程序还识别以下 sysctl：

**`hw.atm.enX.istats`** 包含一个 `uint32_t` 数组，存储内部驱动程序统计信息。

**`hw.atm.enX.debug`** 调试选项的位图。此变量仅在编译驱动程序时启用调试支持时可用。

驱动程序支持媒体选项 `sdh`、`noscramb` 和 `unassigned`（参见 utopia(4)）。

## 诊断

- `en0 <Efficient Networks ENI-155p> rev 0 int a irq 5 on pci0:16`
- `en0: ATM midway v0, board IDs 6.0, Utopia (pipelined), 512KB on-board RAM`
- `en0: maximum DMA burst length = 64 bytes`
- `en0: 7 32KB receive buffers, 8 32KB transmit buffers allocated`

## 参见

natm(4), natmip(4), utopia(4), ifconfig(8), route(8)

## 作者

Chuck Cranor of Washington University 于 1996 年为 NetBSD 实现了 `en` 驱动程序。

## 注意事项

该驱动程序大量使用 PCI 上的 DMA。第一代 PCI 芯片组无法工作或性能很差。
