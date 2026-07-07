# powermac_nvram(4)

`powermac_nvram` — 非易失性 RAM

## 名称

`powermac_nvram`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device powermac_nvram

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
powermac_nvram_load="YES"
```

## 描述

`powermac_nvram` 驱动提供对 Apple 基于 PowerPC 的机器上可用的 Open Firmware 配置 NVRAM 的访问。

此驱动目前支持包含 Sharp、Micron 或 AMD NVRAM 的“Core99”机器。

## 参见

nvram(8)

## 历史

`powermac_nvram` 驱动首次出现于 FreeBSD 7.0。

## 作者

`powermac_nvram` 驱动由 Maxim Sobolev <sobomax@FreeBSD.org> 编写。
