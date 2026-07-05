# bhyve.4

`bhyve` — 虚拟机监视器

## 名称

`bhyve`

## 概要

**/usr/sbin/bhyve**
**/usr/sbin/bhyveload**
**/usr/sbin/bhyvectl**
**/boot/kernel/vmm.ko**

## 描述

`bhyve` 是由 FreeBSD 承载的虚拟机监视器，用于在 FreeBSD 之上托管未修改的客户机操作系统。

`bhyve` 严重依赖 CPU 和芯片组提供的硬件辅助来虚拟化处理器和内存资源。

## 参见

[vmm(4)](vmm.4.md), [bhyve(8)](../man8/bhyve.8.md), [bhyvectl(8)](../man8/bhyvectl.8.md), [bhyveload(8)](../man8/bhyveload.8.md)

## 历史

`bhyve` 首次出现于 FreeBSD 10.0，由 NetApp Inc. 开发。

## 作者

`bhyve` 由 Peter Grehan <grehan@FreeBSD.org> 和 Neel Natu <neel@FreeBSD.org> 在 NetApp Inc. 开发。

## 缺陷

`bhyve` 在 FreeBSD 中被视为实验性功能。
