# rtwnfw(4)

`rtwnfw` — Realtek 无线驱动程序的固件模块

## 名称

`rtwnfw`

## 概要

若要将此模块编译进内核，请在你的内核配置文件中加入以下行：

> device rtwnfw

`这将在内核中包含所有固件映像。如果你只想选择网络适配器对应的固件映像，请从以下项中选择一项：`

> device rtwn-rtl8188eefw
> device rtwn-rtl8188eufw
> device rtwn-rtl8192cfwE_B
> device rtwn-rtl8192cfwE
> device rtwn-rtl8192cfwT
> device rtwn-rtl8192cfwU
> device rtwn-rtl8192eufw
> device rtwn-rtl8812aufw
> device rtwn-rtl8821aufw

`或者，若要在引导时以模块方式加载所有固件映像，在 loader.conf(5) 中加入以下行：`

```sh
rtwn-rtl8188eefw_load="YES"
rtwn-rtl8188eufw_load="YES"
rtwn-rtl8192cfwE_B_load="YES"
rtwn-rtl8192cfwE_load="YES"
rtwn-rtl8192cfwT_load="YES"
rtwn-rtl8192cfwU_load="YES"
rtwn-rtl8192eufw_load="YES"
rtwn-rtl8812aufw_load="YES"
rtwn-rtl8821aufw_load="YES"
```

## 描述

rtwn-rtl8192cfwE 和 rtl8192cfwE_B 模块提供对基于 Realtek RTL8188CE 芯片的 PCIe 适配器的固件集访问。rtwn-rtl8188ee 模块提供对基于 Realtek RTL8188EE 芯片的 PCIe 适配器的固件集访问。其他模块提供对基于 Realtek RTL8188CUS、RTL8188CE-VAU、RTL8188EUS、RTL8188RU、RTL8192CU、RTL8192EU、RTL8812AU 和 RTL8821AU 芯片的 USB WiFi 适配器的固件集访问。它们可以静态链接到内核中，或作为模块加载。

要使加载的固件启用，必须在 loader.conf(5) 中加入以下行以同意 **`/usr/share/doc/legal/realtek.LICENSE`** 中的许可证：

```sh
legal.realtek.license_ack=1
```

## 文件

**`/usr/share/doc/legal/realtek.LICENSE`** `rtwnfw` 固件许可证

## 参见

[rtwn(4)](rtwn.4.md), [firmware(9)](../man9/firmware.9.md)
