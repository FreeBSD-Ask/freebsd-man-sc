# bhyvectl.8

`bhyvectl` — bhyve 实例的控制工具

## 名称

`bhyvectl`

## 概要

`bhyvectl --vm=<vmname> [--create] [--destroy] [--get-stats] [--inject-nmi] [--force-reset] [--force-poweroff] [--checkpoint=<file>] [--suspend=<file>]`

## 描述

`bhyvectl` 命令是一个用于控制活动 [bhyve(8)](bhyve.8.md) 虚拟机实例的工具。

面向用户的选项如下：

**`--vm=`** `<vmname>` 对虚拟机 `<vmname>` 进行操作。

**`--create`** 创建指定的虚拟机。

**`--destroy`** 销毁指定的虚拟机。

**`--get-stats`** 获取指定虚拟机的统计信息。

**`--inject-nmi`** 向虚拟机注入一个不可屏蔽中断（NMI）。

**`--force-reset`** 强制虚拟机复位。

**`--force-poweroff`** 强制虚拟机关机。

**`--checkpoint=`** `<file>` 保存虚拟机的快照。客户机内存内容保存在 `<file>` 指定的文件中。客户机设备及 vCPU 状态保存在 `<file>.kern` 文件中。

**`--suspend=`** `<file>` 类似于 `--checkpoint`，保存虚拟机的快照。虚拟机在快照保存完成后将终止运行。

*注：* 大多数 `bhyvectl` 标志用于查询和设置活动实例的状态。这些命令仅用于开发目的，此处不予说明。完整列表可通过执行不带任何参数的 `bhyvectl` 命令获取。

## 退出状态

`bhyvectl` 工具成功时退出状态为 0，发生错误时大于 0。

## 实例

销毁名为 fbsd10 的虚拟机：

```sh
bhyvectl --vm=fbsd10 --destroy
```

运行中的虚拟机将在 **/dev/vmm/** 目录中可见。

## 兼容性

快照文件格式尚未稳定，未来可能发生变化。不保证在未来修改后仍向后兼容当前的快照文件格式。

## 参见

[bhyve(8)](bhyve.8.md), [bhyveload(8)](bhyveload.8.md)

## 历史

`bhyvectl` 命令首次出现在 FreeBSD 10.1 中。

## 作者

`bhyvectl` 工具由 Peter Grehan 和 Neel Natu 编写。
