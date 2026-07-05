# appleir.4

`appleir` — Apple IR 接收器驱动

## 名称

`appleir` 接收器驱动

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device appleir
> device hidbus
> device hid
> device evdev

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
appleir_load="YES"
```

## 描述

`appleir` 驱动为 Mac 计算机（2006-2011 年代）中发现的 Apple IR 接收器提供支持。它支持 Apple Remote 遥控器以及使用 NEC 红外协议的通用红外遥控器。

支持的设备包括：

- Apple IR Receiver（USB 产品 ID 0x8240、0x8241、0x8242、0x8243、0x1440）

该驱动解码专有的 Apple Remote 按键按下，并为通用红外遥控器使用的常见 NEC 协议代码提供默认键映射。未映射的按键代码可通过 `/dev/hidrawX` 处的原始 HID 设备访问，以便进行自定义用户空间重映射。

`/dev/input/eventX` 设备将遥控器呈现为具有标准 KEY_* 代码的 evdev 输入设备，适用于媒体应用程序。

## 硬件

`appleir` 驱动支持 USB 厂商 ID 为 0x05ac 且具有以下产品 ID 的 Apple IR 接收器：

**0x8240** Apple IR Receiver（第一代）

**0x8241** Apple IR Receiver

**0x8242** Apple IR Receiver（Mac Mini 2011、MacBook Pro 3,1）

**0x8243** Apple IR Receiver

**0x1440** Apple IR Receiver（超薄）

## 文件

**`/dev/input/eventX`** evdev 输入设备

**`/dev/hidrawX`** 用于自定义按键映射的原始 HID 设备

## 参见

evdev , [hidbus(4)](hidbus.4.md), [usbhid(4)](usbhid.4.md)

NEC 红外传输协议：Lk <https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol>

## 历史

`appleir` 驱动首次出现于 FreeBSD 16.0。

## 作者

Abdelkader Boudih <freebsd@seuros.com>

基于 James McKenzie 等人的协议逆向工程。
