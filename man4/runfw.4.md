# runfw(4)

`runfw` — Ralink 驱动程序的固件模块

## 名称

`runfw`

## 概要

若要将此模块编译进内核，请在你的内核配置文件中加入以下行：

> device runfw

`这将在内核中包含两份固件映像：RT2870 和 RT3071。run(4) 会将相应的映像加载到芯片中。`

`或者，若要在引导时以模块方式加载固件映像，在 loader.conf(5) 中加入以下行：`

```sh
runfw_load="YES"
```

## 描述

此模块为基于 Ralink RT2700U、RT2800U、RT3000U 和 RT3900E 芯片的 USB WiFi 适配器提供固件集。请阅读 Ralink 的许可证 src/sys/contrib/dev/run/LICENSE。

## 参见

[run(4)](run.4.md), [firmware(9)](../man9/firmware.9.md)
