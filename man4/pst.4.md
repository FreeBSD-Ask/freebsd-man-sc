# pst(4)

`pst` — Promise Supertrak SX6000 设备驱动程序

## 名称

`pst`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device pst

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
pst_load="YES"
```

## 描述

此驱动程序用于 Promise Supertrak SX6000 ATA 硬件 RAID 控制器。它在硬件层面支持 RAID 级别 0、1、0+1、3、5 和 JBOD，最多支持 6 块 ATA 磁盘驱动器，包括自动重建和热插拔，并支持在 Promise Superswap 磁盘 enclosure 的 LED 上指示磁盘状态。Supertrak 系列控制器不支持非磁盘设备。

## 硬件

`pst` 驱动程序支持 Promise Supertrak SX6000 ATA 硬件 RAID 控制器。

## 注释

`pst` 驱动程序不支持从操作系统操作 RAID，RAID 需从板载 BIOS 中设置。但是，热插拔、热备和自动重建无需重启即可支持。

## 历史

`pst` 驱动程序首次出现于 FreeBSD 4.7。

## 作者

`pst` 驱动程序和手册页由 Søren Schmidt <sos@FreeBSD.org> 编写。
