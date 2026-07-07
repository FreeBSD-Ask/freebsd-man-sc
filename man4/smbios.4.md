# smbios(4)

`smbios` — 系统管理 BIOS

## 名称

`smbios`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device smbios

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
smbios_load="YES"
```

## 描述

系统管理 BIOS（SMBIOS）描述硬件组件。

## 参见

efi(8)

> "System Management BIOS (SMBIOS) Reference Specification", DMTF DSP0134.

## 历史

`smbios` 设备驱动最早出现于 FreeBSD 4.8。

## 作者

`smbios` 设备驱动由 Matthew N. Dodd <winter@jurai.net> 编写。本手册页由 Gordon Bergling <gbe@FreeBSD.org> 编写。
