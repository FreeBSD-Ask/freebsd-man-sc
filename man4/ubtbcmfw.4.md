# ubtbcmfw(4)

`ubtbcmfw` — 基于 Broadcom BCM2033 芯片的蓝牙 USB 设备固件驱动

## 名称

`ubtbcmfw`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ubtbcmfw

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ubtbcmfw_load="YES"
```

## 描述

`ubtbcmfw` 是基于 Broadcom BCM2033 芯片的蓝牙 USB 设备的固件驱动。它提供对设备下载固件所需部分的最低访问。

`ubtbcmfw` 驱动创建三个固定端点设备节点。

控制传输只能在控制端点上进行，该端点始终为端点 0。控制请求通过 ioctl(2) 调用发出。

中断端点仅支持传入传输。要在中断端点上执行 I/O，应使用 read(2)。中断端点上的所有 I/O 操作都是无缓冲的。中断端点始终为端点 1。

批量端点仅支持传出批量传输。要在批量端点上执行 I/O，应使用 write(2)。批量端点上的所有 I/O 操作都是无缓冲的。传出批量端点始终为端点 2。

控制端点（端点 0）处理以下 ioctl(2) 调用：

**`USB_GET_DEVICE_DESC`** (`usb_device_descriptor_t`) 返回设备描述符。

## 文件

**`/dev/ubtbcmfw`** `N``.``EE` 设备 `N` 的端点 `EE`。

## 参见

[ng_ubt(4)](ng_ubt.4.md), [ugen(4)](ugen.4.md), [usb(4)](usb.4.md), bcmfw(8)

## 历史

`ubtbcmfw` 驱动实现于 FreeBSD 5.0。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 缺陷

很可能有。如发现请报告。
