# ufintek.4

`ufintek` — Fintek F81232 USB 串口 UART 驱动

## 名称

`ufintek`

## 概要

`device usb device ucom device ufintek`

在 rc.conf(5) 中：`kld_list="ufintek"`

在 sysctl.conf(5) 中：`hw.usb.ufintek.debug=1`

## 描述

`ufintek` 驱动为 FINTEK 的 F81232 串口适配器提供支持。若检测到相应硬件，该驱动会由 [devmatch(8)](../man8/devmatch.8.md) 自动加载。若要手动加载该驱动，请将其加入 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `kld_list`，或在运行时使用 [kldload(8)](../man8/kldload.8.md)。该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

通过此接口可使用 cu(1) 或 tip(1) 等应用程序进行呼出。

## 硬件

`ufintek` 驱动支持以下 USB 串口 UART 控制器：

- FT82332

## SYSCTL 变量

以下设置可在 [loader(8)](../man8/loader.8.md) 提示符下输入，在 loader.conf(5)、[sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，或在运行时通过 [sysctl(8)](../man8/sysctl.8.md) 更改：

**`hw.usb.uftdi.debug`** 启用调试消息，默认 `0` `1`

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

cu(1), [tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`ufintek` 驱动首次出现于 FreeBSD 16.0。

## 缺陷

此驱动仅支持 9600 波特率。
