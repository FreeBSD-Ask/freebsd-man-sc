# iwnfw(4)

`iwnfw` — Intel Wireless 驱动的固件模块

## 名称

`iwnfw`

## 概要

`要将此模块编译进内核，请在你的内核配置文件中加入以下行：`

> device iwnfw

`这将在内核中包含所有 iwn(4) 设备的固件映像。如果只想为你的网络适配器选择相应的固件映像，请选择以下之一：`

> device iwn1000fw
> device iwn100fw
> device iwn105fw
> device iwn135fw
> device iwn2000fw
> device iwn2030fw
> device iwn4965fw
> device iwn5000fw
> device iwn5150fw
> device iwn6000fw
> device iwn6000g2afw
> device iwn6000g2bfw
> device iwn6050fw

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
iwn1000fw_load="YES"
iwn100fw_load="YES"
iwn105fw_load="YES"
iwn135fw_load="YES"
iwn2000fw_load="YES"
iwn2030fw_load="YES"
iwn4965fw_load="YES"
iwn5000fw_load="YES"
iwn5150fw_load="YES"
iwn6000fw_load="YES"
iwn6000g2afw_load="YES"
iwn6000g2bfw_load="YES"
iwn6050fw_load="YES"
```

## 描述

此模块为 Intel Wireless WiFi Link 100、105、135、1000、2000、2030、4965、5000 和 6000 系列 IEEE 802.11n 适配器提供固件集访问。它可以静态链接到内核中，或作为模块加载。

## 参见

[iwn(4)](iwn.4.md), [firmware(9)](../man9/firmware.9.md)
