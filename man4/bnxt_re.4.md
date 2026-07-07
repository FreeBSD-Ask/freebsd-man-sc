# bnxt_re(4)

`bnxt_re` — Broadcom NetXtreme-E RoCE 驱动

## 名称

`bnxt_re`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> options COMPAT_LINUXKPI
> device bnxt
> device bnxt_re

要在运行时以模块形式加载该驱动，请以 root 身份执行以下命令：

```sh
kldload bnxt_re
```

要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
bnxt_re_load="YES"
```

## 描述

`bnxt_re` 驱动为 Broadcom NetXtreme-E PCI Express 网络适配器提供基于融合以太网的远程直接内存访问（RoCE）支持。

## 硬件

`bnxt_re` 驱动为 NetXtreme-E BCM575xx 10/20/25/40/50/100/200Gb 网络适配器提供支持，包括：

- Broadcom BCM57502 NetXtreme-E 10Gb/25Gb/50Gb/100Gb/200Gb 以太网
- Broadcom BCM57504 NetXtreme-E 10Gb/25Gb/50Gb/100Gb/200Gb 以太网
- Broadcom BCM57508 NetXtreme-E 10Gb/25Gb/50Gb/100Gb/200Gb 以太网

## 支持

有关一般信息和支持，请访问 Broadcom 支持网站：<http://www.broadcom.com/>

将所支持适配器的驱动问题报告至 <freebsd.pdl@broadcom.com>。

## 参见

[bnxt_re(4)](bnxt_re.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bnxt_re` 设备驱动首次出现于 FreeBSD 15.0。

## 作者

`bnxt_re` 驱动由 Broadcom <freebsd.pdl@broadcom.com> 编写。
