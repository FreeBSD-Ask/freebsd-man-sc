# ufoma(4)

`ufoma` — USB 移动电话支持

## 名称

`ufoma`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device ufoma

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ufoma_load="YES"
```

## 描述

`ufoma` 驱动为移动电话终端提供支持，这些终端遵循移动计算促进协会 USB 实现指南的子集，该指南由 FOMA（NTT DoCoMo 的 3G 系统）终端采用。这些设备部分类似基于 CDC ACM 模型的调制解调器（由 [umodem(4)](umodem.4.md) 支持），但 `ufoma` 驱动会识别描述其角色和接口结构的特定 USB 描述符，并在设备打开时协商其角色。它们支持常规 AT 命令集，命令可与数据流复用，也可通过独立管道处理。在后一种情况下，AT 命令必须在独立于数据设备的设备上发出。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## SYSCTL

这些设备通常具有若干接口集，这些接口各有其角色，有时会复用。以下 sysctl MIB 用于标识这些角色：

**`dev.ucom.%d.supportmode`** 该接口支持的模式。

**`dev.ucom.%d.currentmode`** 该接口的当前模式。

**`dev.ucom.%d.openmode`** 下次打开设备时要切换到的模式。

各模式如下：

**`modem`** 接受 AT 命令并传递分组通信数据。

**`handsfree`** 接受 AT 命令但不传递数据。

**`obex`** 接受 OBEX 帧，用于交换电话簿等。

**`vendor1 , vendor2`** 可传递厂商特定数据。

**`deactivated`** 当系统识别到某接口但未使用时，该接口会设置为此模式。

**`unlinked`** 当某接口尚未协商时，该接口处于此模式。

## 硬件

`ufoma` 驱动支持的设备包括：

- SHARP FOMA SH902i
- KYOCERA PHS AH-K3001V（又名 Kyopon）
- SANYO Vodafone3G V801SA

## 参见

规范可在以下地址找到：

- `http://www.nttdocomo.co.jp/corporate/technology/document/foma/index.html`
- `http://www.mcpc-jp.org/doclist.htm`

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [umodem(4)](umodem.4.md), [usb(4)](usb.4.md)

## 历史

`ufoma` 驱动首次出现于 FreeBSD 7.0，部分代码派生自 [umodem(4)](umodem.4.md)。

## 缺陷

支持命令与数据复用的接口以及仅含命令的接口。
