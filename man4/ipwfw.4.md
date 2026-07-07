# ipwfw(4)

`ipwfw` — Intel PRO/Wireless 2100 驱动的固件模块

## 名称

`ipwfw`

## 概要

`要将此模块编译进内核，请在你的内核配置文件中加入以下行：`

> device ipwfw

`这将在内核中包含三个固件映像。如果只想根据网络适配器要操作的模式选择相应的固件映像，请选择以下之一：`

> device ipwbssfw
> device ipwibssfw
> device ipwmonitorfw

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ipw_bss_load="YES"
ipw_ibss_load="YES"
ipw_monitor_load="YES"
```

## 描述

此模块为 Intel PRO/Wireless 2100 系列 IEEE 802.11 适配器提供固件集访问。它可以静态链接到内核中，或作为模块加载。

要使加载的固件可供使用，必须在 loader.conf(5) 中加入以下行，表示同意 **/usr/share/doc/legal/intel_ipw.LICENSE** 中的许可：

```sh
legal.intel_ipw.license_ack=1
```

## 文件

**/usr/share/doc/legal/intel_ipw.LICENSE** `ipwfw` 固件许可

## 参见

[ipw(4)](ipw.4.md), [firmware(9)](../man9/firmware.9.md)
