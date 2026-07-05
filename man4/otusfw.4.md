# otusfw.4

`otusfw` — AR9170 驱动的固件模块

## 名称

`otusfw`

## 概要

`要将此模块编译进内核，请在你的内核配置文件中加入以下行：`

> device otusfw

`这将在内核中包含固件映像 AR9170。otus(4) 会将该映像加载到芯片中。`

`或者，要在引导时以模块形式加载固件映像，请在 loader.conf(5) 中加入以下行：`

```sh
otusfw_init_load="YES"
otusfw_main_load="YES"
```

## 描述

此模块为基于 Atheros AR9170 的 USB Wi-Fi 适配器提供固件。

## 参见

[otus(4)](otus.4.md), [firmware(9)](../man9/firmware.9.md)
