# tdfx.4

`tdfx` — Voodoo Graphics 和 VoodooII 内存访问 GLIDE 设备驱动程序

## 名称

`tdfx`

## 概要

`device tdfx`

## 描述

此驱动在 **`/dev`** 中创建一个条目，允许程序（主要是 *基于 GLIDE 的软件*）访问由 *3Dfx, Inc.* 创建的 Voodoo Graphics 和 VoodooII 3D 加速器的设备内存。这为基于 *GLIDE API* 或仅使用 Linux **`/dev/3dfx`** 设备提供的 API 的应用程序提供接口以使用视频设备。

支持基于以下芯片组的所有卡：

- *3Dfx Voodoo Graphics*
- *3Dfx Voodoo II*

具体而言，以下卡应该可以工作：

- *Diamond Multimedia Monster 3D*
- *Diamond Multimedia Monster 3D II*

注意，此驱动目前不支持 Voodoo Banshee、Voodoo3、Voodoo5 或 Voodoo6 卡。它目前也不支持 Voodoo Rush。它也尚未处理 Voodoo II 板的 SLI 功能。你只能分别使用它们。

通过加载 `tdfx_linux.ko` 和 `linux.ko` 模块，你可以为此驱动启用 Linux ioctl 代码，目前唯一支持的应用程序位于此处。

## 文件

**`/dev/3dfx`** 符号链接到默认 *3dfx* 板
**`/dev/3dfx*`** *字符设备* 编程接口
**`/dev/voodoo`** 上述接口的镜像
**`/dev/voodoo*`**（某些应用程序使用 **`/dev/voodoo`** ）

## 参见

[kld(4)](kld.4.md), [linux(4)](linux.4.md), [kldload(8)](../man8/kldload.8.md)

## 历史

`linux.ko` 驱动出现于 FreeBSD 5.0，最初为 Linux 内核 2.0.x 开发，后来为 2.2.x 和 2.4.x 编写。

## 作者

该驱动由 Coleman Kane <cokane@micro.ti.com> 开发，基于 Darryll Straus、John Taylor、Jens Axboe、Carlo Wood <carlo@alinoe.com> 和 Joseph Kain <joseph@3dfx.com> 编写的 Linux 版本驱动，以直接兼容它并支持许多可用于 Linux 和 UNIX 的基于 GLIDE 的游戏。
