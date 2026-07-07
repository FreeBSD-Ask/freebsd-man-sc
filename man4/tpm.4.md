# tpm(4)

`tpm` — 可信平台模块

## 名称

`tpm`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device tpm

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
tpm_load="YES"
```

`在 /boot/device.hints 中： hint.tpm.0.at="isa" hint.tpm.0.maddr="0xfed40000" hint.tpm.0.msize="0x5000" hint.tpm.1.at="isa" hint.tpm.1.maddr="0xfed40000" hint.tpm.1.msize="0x1000"`

## 描述

`tpm` 驱动为各种可信平台模块（TPM）提供支持，这些模块可以存储加密密钥。

支持的模块：

- Atmel 97SC3203
- Broadcom BCM0102
- Infineon IFX SLD 9630 TT 1.1 和 IFX SLB 9635 TT 1.2
- Intel INTC0102
- Sinosun SNS SSX35
- STM ST19WP18
- Winbond WEC WPCT200

可以通过在 **`/boot/device.hints`** 中提供空闲 ISA 中断向量来配置驱动使用 IRQ。

## 参见

[intro(4)](intro.4.md), [device.hints(5)](../man5/device.hints.5.md), [config(8)](../man8/config.8.md)

BSSSD 项目的首页，该项目开发了原始 `tpm` 驱动：Lk <http://bsssd.sourceforge.net/> 。

TPM 主规范可在以下位置找到：Lk <https://trustedcomputinggroup.org/resource/tpm-main-specification/> 。

## 标准

TPM 主规范级别 2 版本 1.2：

> ISO/IEC, "11889-1:2009, Information technology -- Trusted Platform Module -- Part 1: Overview".

> ISO/IEC, "11889-2:2009, Information technology -- Trusted Platform Module -- Part 2: Design principles".

> ISO/IEC, "11889-3:2009, Information technology -- Trusted Platform Module -- Part 3: Structures".

-
-
-

## 历史

`tpm` 驱动首次出现于 FreeBSD 8.2，后来添加到 OpenBSD 6.1。

## 作者

`tpm` 驱动由 Michael Shalayeff 和 Hans-Joerg Hoexer 编写。
