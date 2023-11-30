  BHYVECTL(8)  

BHYVECTL(8)

FreeBSD System Manager's Manual

BHYVECTL(8)

[名称](#__u540D___u79F0_)
=======================

`bhyvectl` —

bhyve 实例的控制实用程序

[概要](#__u6982___u8981_)
=======================

`bhyvectl` `--vm=`<vmname> \[`--create`\] \[`--destroy`\] \[`--get-stats`\] \[`--inject-nmi`\] \[`--force-reset`\] \[`--force-poweroff`\] \[`--checkpoint=`<filename>\] \[`--suspend=`<filename>\]

[描述](#__u63CF___u8FF0_)
=======================

`bhyvectl` 命令是活动 bhyve(8) 虚拟机实例的控制实用程序。

_注意_: 大多数 `bhyvectl` 标志用于查询和设置活动实例的状态。 这些命令用于开发目的，此处未记录。 通过执行不带任何参数的 `bhyvectl` 可以获得完整的列表。

面向用户的选项如下：

[`--vm=`](#-vm=)<vmname>

在虚拟机 <vmname> 上操作。

[`--create`](#-create)

创建指定的虚拟机。

[`--destroy`](#-destroy)

销毁指定的虚拟机。

[`--get-stats`](#-get-stats)

检索指定 VM 的统计信息。

[`--inject-nmi`](#-inject-nmi)

将不可屏蔽中断 (NMI) 注入 VM。

[`--force-reset`](#-force-reset)

强制 VM 重置。

[`--force-poweroff`](#-force-poweroff)

强制关闭虚拟机。

[`--checkpoint=`](#-checkpoint=)<filename>

保存虚拟机的快照。 来宾内存内容保存在 <filename> 中给出的文件中。 来宾设备和 vCPU 状态保存在文件 <filename>.kern 中。

[`--suspend=`](#-suspend=)<filename>

保存类似于 `--checkpoint` 的虚拟机快照。 保存快照后，虚拟机将终止。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `bhyvectl` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

销毁名为 fbsd10 的 VM：

`bhyvectl --vm=fbsd10 --destroy`

[兼容性](#__u517C___u5BB9___u6027_)
================================

快照文件格式尚不稳定，可能会发生变化。 将来进行更改时，不能保证对当前快照文件格式的向后兼容性支持。

[参见](#__u53C2___u89C1_)
=======================

bhyve(8), bhyveload(8)

[历史](#__u5386___u53F2_)
=======================

`bhyvectl` 命令首次出现在 FreeBSD 10.1 中。

[作者](#__u4F5C___u8005_)
=======================

`bhyvectl` 实用程序由 Peter Grehan 和 Neel Natu 编写。

May 4, 2020

FreeBSD 13.1-RELEASE