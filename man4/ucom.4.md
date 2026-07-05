# ucom.4

`ucom` — USB tty 支持

## 名称

`ucom`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ucom

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ucom_load="YES"
```

## 描述

`ucom` 驱动附着到 USB 调制解调器、串口和其他需要看起来像 tty 的设备。`ucom` 驱动表现出类似 [tty(4)](tty.4.md) 的行为。这意味着可以使用 tip(1) 或 ppp(8) 等正常程序访问设备。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.ucom.debug`** 调试输出级别，0 为禁用调试，更大的值增加调试消息的详尽程度。默认为 0。

**`hw.usb.ucom.device_mode_console`** 设为 1 时，`ucom` 驱动在设备模式下运行时将终端标记为控制台设备。默认为 1。

**`hw.usb.ucom.pps_mode`** 启用并配置如下所述的 PPS 捕获模式。

## 每秒脉冲（PPS）定时接口

`ucom` 驱动能捕获 RFC 2783 中定义的 PPS 定时信息。该 API 通过 ioctl(2) 访问，在 tty 设备上可用。要将 PPS 捕获功能与 ntpd(8) 一起使用，请将 tty 设备符号链接到 **`/dev/pps0`**。

`hw.usb.ucom.pps_mode` sysctl 配置 PPS 捕获模式。可在 loader.conf(5) 或 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置。可用的捕获模式如下：

**0** 禁用捕获（默认）。
**1** 在 CTS 线路上捕获脉冲。
**2** 在 DCD 线路上捕获脉冲。

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 相应的呼入初始状态和锁定状态设备

## 参见

cu(1), [tty(4)](tty.4.md), [uark(4)](uark.4.md), [ubsa(4)](ubsa.4.md), [ubser(4)](ubser.4.md), [uchcom(4)](uchcom.4.md), [ucycom(4)](ucycom.4.md), [ufoma(4)](ufoma.4.md), [uftdi(4)](uftdi.4.md), [uhso(4)](uhso.4.md), [uipaq(4)](uipaq.4.md), [umcs(4)](umcs.4.md), [umct(4)](umct.4.md), [umodem(4)](umodem.4.md), [umoscom(4)](umoscom.4.md), [uplcom(4)](uplcom.4.md), [usb(4)](usb.4.md), [uslcom(4)](uslcom.4.md), [uvisor(4)](uvisor.4.md), [uvscom(4)](uvscom.4.md), ttys(5)

## 历史

`ucom` 驱动于 2002 年 3 月从 NetBSD 引入。本 man 页面由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入。

## 缺陷

在 FreeBSD 6.0 之前，`ucom` 创建的是 **`/dev/ucom?`** 而非今天创建的统一设备名。旧脚本必须相应调整。
