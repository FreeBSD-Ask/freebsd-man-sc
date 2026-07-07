# linsysfs(4)

`linsysfs` — Linux 内核对象文件系统

## 名称

`linsysfs`

## 概要

```sh
linsysfs		/compat/linux/sys	linsysfs	rw 0 0
```

## 描述

Linux 系统文件系统，或 `linsysfs`，模拟 Linux sys 文件系统的一个子集，某些 Linux 二进制文件的完整运行需要它。

`linsysfs` 提供设备的二级视图。在最高级别，PCI 设备本身根据其在系统层次结构中的总线、插槽和功能命名。PCI 存储设备列在 `scsi_host` 类中，并带有指向设备 PCI 目录的设备符号链接。

每个设备节点是一个包含一些文件和目录的目录：

**`host`** 存储主机信息的占位符。

**`pci_id`** `pci_id` 的目录，包含设备信息或 PCI 桥的另一个目录结构。

scsi_host 的每个 host 节点是一个包含一些文件和目录的目录：

**`proc_name`** 这些设备的 Linux 注册驱动名称。

**`device`** 指向 PCI 设备目录的符号链接。

## 文件

**`/compat/linux/sys`** `linsysfs` 的正常挂载点。

**`/compat/linux/sys/class/scsi_host`** 存储主机节点。

**`/compat/linux/sys/devices/pci0000:00`** PCI 设备层次结构节点。

## 实例

最常见的用法如下：

```sh
mount -t linsysfs linsysfs /compat/linux/sys
```

其中 **/compat/linux/sys** 是挂载点。

## 参见

nmount(2), unmount(2), [linprocfs(4)](linprocfs.4.md), [linux(4)](linux.4.md), pseudofs(9)

## 历史

`linsysfs` 驱动最早出现于 FreeBSD 6.2。

## 作者

`linsysfs` 驱动由 Doug Ambrisko 从 `linprocfs` 派生。本手册页由 Doug Ambrisko 编辑，基于 Garrett Wollman 的 [linprocfs(4)](linprocfs.4.md) 手册页。
