# umct(4)

`umct` — Magic Control Technology USB-RS232 转换器驱动

## 名称

`umct`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device umct

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
umct_load="YES"
```

## 描述

`umct` 驱动为基于 Magic Control Technology USB-232 设计的 USB 转 RS-232 转换器提供支持。这些设备支持大多数标准 RS-232 特性，包括 300 到 115200 比特每秒的波特率。但似乎既不支持硬件流控制，也不支持软件流控制。

此驱动下对设备的访问通过 [ucom(4)](ucom.4.md) 框架和设备节点进行。

## 硬件

`umct` 驱动支持以下适配器：

- Belkin F5U109
- Belkin F5U409
- D-Link DU-H3SP USB BAY 集线器
- Magic Control Technology USB-232
- Sitecom USB-232

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`umct` 驱动出现于 FreeBSD 5.2。它大致基于 Alexander Kabaev <kan@FreeBSD.org> 编写的 [ubsa(4)](ubsa.4.md) 驱动，文档由 Wolfgang Grandeggar <wolfgang@cec.ch> 提供。

## 作者

`umct` 驱动由 Scott Long <scottl@FreeBSD.org> 编写。
