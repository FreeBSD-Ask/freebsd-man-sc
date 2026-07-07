# vmgenc(4)

`vmgenc` — ACPI 虚拟机生成 ID 计数器

## 名称

`vmgenc`

## 概要

`device vmgenc`

`在 loader.conf(5) 中： vmgenc_load="YES"`

## 描述

`vmgenc` 驱动为虚拟机生成 ID（Virtual Machine Generation ID）提供支持，这是 hypervisor 通过 ACPI 暴露的 128 位唯一标识符。每当虚拟机被克隆、从快照恢复或以其他方式复制时，hypervisor 都会更改此标识符。

当检测到生成 ID 更改时，`vmgenc` 驱动会将新标识符送入内核熵池（通过 [random(4)](random.4.md)），确保复制的虚拟机不共享加密状态。驱动还会发送 [devctl(4)](devctl.4.md) 事件和内部内核通知，以便其他子系统能对复制做出响应。

虚拟机生成 ID 规范由 QEMU、VMware ESXi、Microsoft Hyper-V 和 Xen 支持。

## SYSCTL 变量

以下变量可用：

**`dev.vmgenc.%d.guid`** 当前缓存的 VM 生成计数器，作为 128 位值。每次 hypervisor 发出生成更改信号时都会更新此值。

## 参见

[acpi(4)](acpi.4.md), [random(4)](random.4.md)

## 历史

`vmgenc` 驱动最早出现于 FreeBSD 13.0。

## 作者

`vmgenc` 驱动由 Conrad Meyer <cem@FreeBSD.org> 编写。

本手册页由 Christos Longros <chris.longros@gmail.com> 编写。
