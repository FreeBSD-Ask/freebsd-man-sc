# mwlfw.4

`mwlfw` — Marvell 88W8363 无线驱动的固件模块

## 名称

`mwlfw`

## 概要

要将此模块编译进内核，请在内核配置文件中加入以下行：

> device mwlfw

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
mwlfw_load="YES"
```

## 描述

此模块提供对 Marvell 88W8363 IEEE 802.11n 无线适配器固件集的访问。它可以静态链接到内核中，或作为模块加载。

## 参见

[mwl(4)](mwl.4.md), [firmware(9)](../man9/firmware.9.md)
