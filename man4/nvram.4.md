# nvram.4

`nvram` — 非易失性 RAM

## 名称

`nvram`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device nvram

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nvram_load="YES"
```

## 描述

`nvram` 驱动提供对 i386 和 amd64 系统上 BIOS 配置 NVRAM 的访问。

PC 主板使用小型非易失性存储器存储 BIOS 设置，通常是其时钟芯片的一部分，有时被称为“CMOS SRAM”。此驱动在设备文件 `/dev/nvram` 的偏移零处暴露 NVRAM 的第 14 到 128 字节，共 114 字节。

此驱动适用于克隆共享相同硬件配置且需要相同 BIOS 设置调整的机器。

## 实现说明

BIOS NVRAM 的第 16 到 31 字节在第 32 字节处校验和。此驱动*不*处理这些校验和。

## 实例

将现有 BIOS NVRAM 备份到 `nvram.bin`：

```sh
dd if=/dev/nvram of=nvram.bin
```

从 `nvram.bin` 恢复 BIOS NVRAM：

```sh
dd if=nvram.bin of=/dev/nvram
```

## 参见

[dd(1)](../man1/dd.1.md)

## 历史

`nvram` 设备驱动首次出现于 FreeBSD 6.4。

## 作者

`nvram` 设备驱动由 Peter Wemm 编写。本手册页由 Xin LI 编写。
