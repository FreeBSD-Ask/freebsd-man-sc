# ispfw.4

`ispfw` — Qlogic FibreChannel SCSI 主机适配器固件

## 名称

`ispfw`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ispfw

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ispfw_load="YES"
```

## 描述

此简单驱动为 Qlogic FibreChannel SCSI 主机适配器提供固件集访问。它可以静态链接到内核中，或作为模块加载。无论哪种情况，[isp(4)](isp.4.md) 驱动都会注意到有固件可下载到 Qlogic 卡上（用以替换卡上通常过时的固件）。这将促使固件脱离卡住状态。

## 参见

[isp(4)](isp.4.md)

## 作者

此驱动由 Matthew Jacob 编写。后续改进由 Alexander Motin <mav@FreeBSD.org> 完成。
