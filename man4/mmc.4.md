# mmc.4

`mmc` — MultiMediaCard 和 SD 卡总线驱动

## 名称

`mmc`

## 概要

`device mmc`

## 描述

`mmc` 驱动实现了 MMC 和 SD 卡总线。`mmc` 驱动支持系统中的所有 MMC 和 SD 桥。系统中的所有 SD 或 MMC 卡都附加到 `mmc` 的一个实例上。`mmc` 总线通常只有一个插槽，且只有存储卡。MultiMediaCard 仅以存储形式存在。SD 卡则可作为存储卡、I/O 卡或组合卡存在。

## 参见

[mmcsd(4)](mmcsd.4.md), [sdhci(4)](sdhci.4.md)

> "SD Specifications, Part 1, Physical Layer, Simplified Specification"。

> "The MultiMediaCard System Specification"。

## 缺陷

SDIO 卡目前无法工作。
