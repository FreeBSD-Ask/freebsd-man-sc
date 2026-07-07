# umcs(4)

`umcs` — 基于 MCS7820 和 MCS7840 芯片的串口适配器的 USB 支持

## 名称

`umcs`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device umcs

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
umcs_load="YES"
```

## 描述

`umcs` 驱动为基于 MosCom MCS7820 和 MCS7840 芯片的各种多端口串口适配器提供支持。它们是 2 端口或 4 端口适配器，具有功能齐全的 16550 兼容 UART 和非常灵活的波特率发生器。此外，这些芯片还支持 RS422/RS485 和 IrDA 操作。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

设备上的不同端口以子单元形式呈现，例如 **`/dev/ttyU0.1`** 和 **`/dev/ttyU0.2`**。

## 硬件

`umcs` 驱动已在以下适配器上测试：

- ST Lab U-360 双端口串口 USB 适配器
- ST Lab U-400 四端口串口 USB 适配器

## 文件

**`/dev/ttyU*.*`** 用于呼入端口
**`/dev/ttyU*.*.init`**
**`/dev/ttyU*.*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*.*`** 用于呼出端口
**`/dev/cuaU*.*.init`**
**`/dev/cuaU*.*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`umcs` 驱动自 2010 年 12 月起出现于 ports 中。

## 作者

`umcs` 驱动由 Lev Serebryakov <lev@FreeBSD.org> 编写。

## 缺陷

此驱动不支持访问芯片的任何精细调整，例如 RS522/RS485 模式、非标准波特率等。
