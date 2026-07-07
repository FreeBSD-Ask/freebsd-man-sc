# ugold(4)

`ugold` — TEMPer gold HID 温度计

## 名称

`ugold`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device hid
> device ugold

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ugold_load="YES"
```

## 描述

`ugold` 驱动为 pcsensors TEMPer gold 设备提供支持。

该驱动拥有一组传感器值，通过 [sysctl(8)](../man8/sysctl.8.md) 接口提供。

## 硬件

`ugold` 驱动支持以下设备：

- RDing TEMPer1V1.2

## 参见

[usb(4)](usb.4.md), [sysctl(8)](../man8/sysctl.8.md)
