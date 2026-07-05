# iwmfw.4

`iwmfw` — Intel Wireless 驱动的固件模块

## 名称

`iwmfw`

## 概要

`要将此模块编译进内核，请在你的内核配置文件中加入以下行：`

> device iwmfw

`这将在内核中包含所有 iwm(4) 设备的固件映像。如果只想为你的网络适配器选择相应的固件映像，请选择以下之一：`

> device iwm3160fw
> device iwm3168fw
> device iwm7260fw
> device iwm7265fw
> device iwm7265Dfw
> device iwm8000Cfw
> device iwm8265fw
> device iwm9000fw
> device iwm9260fw

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行之一：`

```sh
iwm3160fw_load="YES"
iwm3168fw_load="YES"
iwm7260fw_load="YES"
iwm7265fw_load="YES"
iwm7265Dfw_load="YES"
iwm8000Cfw_load="YES"
iwm8265fw_load="YES"
iwm9000fw_load="YES"
iwm9260fw_load="YES"
```

## 描述

此模块为 Intel Dual Band Wireless WiFi 3160、3165、3168、7260、7265、8000、8260、8265、9000 和 9260 系列 IEEE 802.11n/11ac 适配器提供固件集访问。它可以静态链接到内核中，或作为模块加载。

## 参见

[iwm(4)](iwm.4.md), [firmware(9)](../man9/firmware.9.md)
