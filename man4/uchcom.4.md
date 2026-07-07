# uchcom(4)

`uchcom` — WinChipHead CH9102/CH343/CH341/CH340 USB 转串口 UART 驱动

## 名称

`uchcom`

## 概要

`device usb device ucom device uchcom`

`在 rc.conf(5) 中：kld_list="uchcom"`

`在 sysctl.conf(5) 中：hw.usb.uchcom.debug=1`

## 描述

`uchcom` 驱动提供对 WinChipHead USB 转串口 UART 适配器的支持。如果检测到相应硬件，驱动会由 [devmatch(8)](../man8/devmatch.8.md) 自动加载。要手动加载驱动，请将其添加到 [rc.conf(5)](../man5/rc.conf.5.md) 的 `kld_list` 中，或在运行时使用 [kldload(8)](../man8/kldload.8.md)。该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

通过 cu(1) 或 tip(1) 等应用程序使用此接口呼出。

## 硬件

`uchcom` 驱动支持以下 USB 转串口 UART 控制器：

- WinChipHead CH9102（最高 6Mbps）
- WinChipHead CH343（最高 6Mbps）
- WinChipHead CH341（最高 2Mbps）
- WinChipHead CH340（最高 2Mbps）

## SYSCTL 变量

这些设置可在 [loader(8)](../man8/loader.8.md) 提示符处输入，在 loader.conf(5) 中设置，在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，或在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 更改：

**`hw.usb.uchcom.debug`** 启用调试消息，默认为 `0`

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 相应的呼出初始状态和锁定状态设备

## 参见

cu(1), [tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uchcom` 驱动从 NetBSD 5.0 出现于 FreeBSD 8.0。
