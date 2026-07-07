# rsufw(4)

`rsufw` — Realtek 驱动的固件模块

## 名称

`rsufw`

## 概要

`要将此模块编译进内核，请在你的内核配置文件中加入以下行：`

> device rsufw

`这会将固件镜像 RTL8712 包含进内核。rsu(4) 会将该镜像加载到芯片中。`

`或者，要在引导时以模块形式加载固件镜像，请在 loader.conf(5) 中加入以下行：`

```sh
rsu-rtl8712fw_load="YES"
```

## 描述

此模块为基于 Realtek RTL8188SU 和 RTL8192SU 芯片的 USB WiFi 适配器提供固件。请阅读 Realtek 的许可证 **`/usr/share/doc/legal/realtek.LICENSE`**。

## 参见

[rsu(4)](rsu.4.md), [firmware(9)](../man9/firmware.9.md)
