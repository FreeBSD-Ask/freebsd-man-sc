# umb(4)

`umb` — USB 移动宽带接口模型（MBIM）蜂窝调制解调器驱动

## 名称

`umb`

## 概要

`device usb device umb`

在 loader.conf(5) 中：`umb_load="YES"`

## 描述

`umb` 驱动为 USB MBIM 设备提供支持。若检测到相应硬件，该驱动会由 [devmatch(8)](../man8/devmatch.8.md) 自动加载。若要手动加载该驱动，请在 loader.conf(5) 中 `load`，或在 [loader(8)](../man8/loader.8.md) 提示符下加载。

MBIM 设备通过 GPRS、UMTS 和 LTE 等蜂窝网络建立连接。它们以常规点对点网络接口的形式呈现，传输原始 IP 帧。

PIN 和 APN 等必需的配置参数必须通过 umbctl(8) 设置。一旦 SIM 卡用正确的 PIN 解锁，它将保持此状态，直到 MBIM 设备断电重启。如果设备连接到“常通”USB 端口，即使系统重启，也可能无需再次输入 PIN 即可连接到提供商。

## 硬件

`umb` 驱动应支持任何实现 MBIM 的 USB 设备，包括以下蜂窝调制解调器：

- Ericsson H5321gw 和 N5321gw
- Fibocom L831-EAU
- Medion Mobile S4222（MediaTek OEM）
- Sierra Wireless EM7345
- Sierra Wireless EM7455
- Sierra Wireless EM8805
- Sierra Wireless MC8305

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md), umbctl(8)

> "Universal Serial Bus Communications Class Subclass Specification for Mobile Broadband Interface Model"。

## 历史

`umb` 设备驱动首次出现于 OpenBSD 6.0、NetBSD 9.0 和 FreeBSD 15.0。

## 作者

`umb` 驱动由 Gerhard Roth <gerhard@openbsd.org> 编写，并由 Pierre Pronchery <khorben@defora.org> 从 OpenBSD 移植。

## 注意事项

`umb` 驱动不支持 IPv6。

未能提供合规 MBIM 实现的设备可能会附加为其他驱动，例如 [u3g(4)](u3g.4.md)。
