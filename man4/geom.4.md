# geom.4

`GEOM` — 模块化的磁盘 I/O 请求转换框架

## 名称

`GEOM`

## 概要

`options GEOM_CACHE options GEOM_CONCAT options GEOM_ELI options GEOM_GATE options GEOM_JOURNAL options GEOM_LABEL options GEOM_LINUX_LVM options GEOM_MAP options GEOM_MIRROR options GEOM_MOUNTVER options GEOM_MULTIPATH options GEOM_NOP options GEOM_PART_APM options GEOM_PART_BSD options GEOM_PART_BSD64 options GEOM_PART_EBR options GEOM_PART_EBR_COMPAT options GEOM_PART_GPT options GEOM_PART_LDM options GEOM_PART_MBR options GEOM_RAID options GEOM_RAID3 options GEOM_SHSEC options GEOM_STRIPE options GEOM_UZIP options GEOM_VIRSTOR options GEOM_ZERO`

## 描述

`GEOM` 框架提供了一种基础设施，其中“类”（classes）可以在磁盘 I/O 请求从上层内核到设备驱动程序以及返回的路径上执行转换。

在 `GEOM` 上下文中，转换的范围从典型磁盘分区模块中执行的简单几何位移，到 RAID 算法和设备多路径解析，再到存储数据的全面加密保护。

与传统的“卷管理”相比，`GEOM` 与大多数甚至所有先前实现的不同之处在于：

- `GEOM` 是可扩展的。编写一个新的转换类非常简单，而且不会被区别对待。如果有人出于某种原因想要挂载 IBM MVS 磁盘包，编写一个识别并配置其 VTOC 信息的类是一件轻而易举的事。
- `GEOM` 在拓扑上是无关的。大多数卷管理实现对于类如何组合在一起有非常严格的限制，通常只提供一个固定的层次结构，例如，子盘 - plex - 卷。

可扩展性意味着新的转换与现有转换的处理方式没有区别。

固定的层次结构是不好的，因为它们使得无法有效地表达意图。在上面的固定层次结构中，无法镜像两个物理磁盘然后再将镜像划分为子盘，而是被迫在物理卷上创建子盘并两两镜像，导致配置更加复杂。而 `GEOM` 不关心操作的顺序，唯一的限制是图中不允许出现环。

## 术语和拓扑

`GEOM` 相当面向对象，因此其术语从面向对象词汇表中借鉴了大量上下文和语义：

“类”（class）由数据结构 `g_class` 表示，实现一种特定的转换。典型示例包括 MBR 磁盘分区、BSD disklabel 和 RAID5 类。

类的一个实例称为“geom”，由数据结构 `g_geom` 表示。在典型的 i386 FreeBSD 系统中，每块磁盘都会有一个 MBR 类的 geom。

“提供者”（provider）由数据结构 `g_provider` 表示，是 geom 提供服务的前门。提供者是“出现在 `/dev` 中的类磁盘事物”，换句话说就是一个磁盘。所有提供者都有三个主要属性：“name”（名称）、“sectorsize”（扇区大小）和“size”（大小）。

“消费者”（consumer）是 geom 连接到另一个 geom 提供者并发送 I/O 请求的后门。

这些实体之间的拓扑关系如下：

- 一个类有零个或多个 geom 实例。
- 一个 geom 恰好有一个派生它的类。
- 一个 geom 有零个或多个消费者。
- 一个 geom 有零个或多个提供者。
- 一个消费者可以附加到零个或一个提供者。
- 一个提供者可以有零个或多个附加的消费者。

所有 geom 都有一个分配的秩号，用于检测和防止有向无环图中的环。该秩号的分配规则如下：

- 没有附加消费者的 geom 的秩为 1。
- 有附加消费者的 geom 的秩比其消费者所附加的提供者的 geom 的最高秩高 1。

## 特殊拓扑操作

除了简单的附加（将消费者附加到提供者）和分离（断开连接）之外，还存在一些特殊的拓扑操作以方便配置并提高整体灵活性。

- 检查磁盘上的特定数据结构。
- 检查提供者的“sectorsize”或“mediasize”等属性。
- 检查提供者 geom 的秩号。
- 检查提供者 geom 的方法名。

- 设备驱动程序检测到磁盘已离开，并使其提供者成为孤儿。
- 磁盘上方的 geom 接收到孤儿化事件，并依次使其所有提供者成为孤儿。没有附加消费者的提供者通常会立即自毁。此过程以准递归方式继续，直到树中所有相关部分都收到坏消息。
- 最终当到达栈顶的 geom_dev 时，责任到此为止。
- geom_dev 将调用 destroy_dev(9) 以阻止更多请求进入。它会休眠直到所有未完成的 I/O 请求都已返回。它会显式关闭（即：将访问计数清零），此变更将向下传播到整个网格。然后它将分离并销毁其 geom。
- 提供者现已分离的 geom 将销毁该提供者，分离并销毁其消费者，并销毁其 geom。
- 此过程一直向下渗透到整个网格，直到清理完成。

***TASTING***（品尝）是一个过程，每当创建新类或新提供者时发生，它为类提供了在它识别为自己的提供者上自动配置实例的机会。典型示例是 MBR 磁盘分区类，它会在第一个扇区中查找 MBR 表，如果找到并验证通过，就会实例化一个 geom 根据 MBR 的内容进行多路复用。新类将依次被提供给所有现有提供者，新提供者也将依次被提供给所有类。`GEOM` 并未定义类如何识别是否应接受所提供的提供者，但合理的选项集合是：品尝由 `kern.geom.notaste` sysctl 控制。要禁用品尝，将 sysctl 设置为 1，要重新启用品尝，将 sysctl 设置为 0。

***ORPHANIZATION***（孤儿化）是在提供者可能仍在使用时将其移除的过程。当 geom 使一个提供者成为孤儿时，所有未来的 I/O 请求都将在该提供者上“反弹”，并带有由 geom 设置的错误代码。附加到该提供者的任何消费者将在事件循环处理到它时收到孤儿化通知，并可在此时采取适当行动。因正常品尝操作而产生的 geom 应自毁，除非它有办法在缺少孤儿化提供者的情况下继续运行。因此，磁盘切片器之类的 geom 应自毁，而 RAID5 或镜像 geom 只要不超过法定数量就可以继续运行。当提供者被孤儿化时，不一定会立即导致拓扑的任何变化：任何附加的消费者仍然附加，任何打开的路径仍然打开，任何未完成的 I/O 请求仍然未完成。典型场景是：虽然这种方法看起来复杂，但它确实在处理消失设备时提供了最大的灵活性和健壮性。一个绝对关键的细节是，如果设备驱动程序不返回所有 I/O 请求，树将不会解开。

***SPOILING***（ spoilage）是孤儿化的一个特例，用于防止过期的元数据。通过一个例子来理解 spoiling 可能最容易。想象一块磁盘 `da0`，在其上有一个 MBR geom 提供 `da0s1` 和 `da0s2`，在 `da0s1` 之上有 BSD geom 提供 `da0s1a` 到 `da0s1e`，并且 MBR 和 BSD geom 都是基于磁盘介质上的数据结构自动配置的。现在想象 `da0` 被打开以写入，这些数据结构被修改或覆盖：除非有通知系统能告知它们，否则 geom 现在将在过期的元数据上操作。为避免这种情况，当 `da0` 被打开以写入时，所有附加的消费者都会收到通知，MBR 和 BSD 之类的 geom 将因此自毁。当 `da0` 关闭时，它将再次被提供品尝，如果 MBR 和 BSD 的数据结构仍然存在，新的 geom 将重新实例化。现在看细节：如果通过 MBR 或 BSD 模块的任何路径是打开的，它们将以独占位向下打开，因此在这种情况下不可能打开 `da0` 以写入。反之，请求的独占位将使得当 `da0` 被打开以写入时，无法通过 MBR geom 打开路径。由此还可得出，更改打开 geom 的大小只能在其配合下进行。最后：spoilage 只在写入计数从零变为非零时发生，重新品尝只在写入计数从非零变为零时发生。

***CONFIGURE***（配置）是管理员发出指令让特定类实例化自身的过程。在这种情况下有多种表达意图的方式——可以指定一个特定的提供者并带有一定程度的覆盖强制，例如，强制 BSD disklabel 模块附加到在 TASTE 操作中未被发现可接受的提供者。最后，I/O 是我们做这一切的原因：它涉及通过图发送 I/O 请求。

***I/O 请求***由 `struct bio` 表示，起源于消费者，在其附加的提供者上调度，处理完成后返回给消费者。重要的是要认识到，通过特定 geom 的提供者进入的 `struct bio` 不会“从另一端出来”。即使是 MBR 和 BSD 这样的简单转换也会克隆 `struct bio`，修改克隆，并在自己的消费者上调度克隆。注意，克隆 `struct bio` 不涉及克隆 I/O 请求中指定的实际数据区域。`GEOM` 中共有四种不同的 I/O 请求：读、写、删除和“获取属性”。读和写不言自明。删除表示某个范围内的数据不再使用，可以按底层技术支持的方式擦除或释放。闪存适配层之类的技术可以安排在相关块被重新分配之前擦除它们，加密设备可能希望用随机位填充该范围以减少可用于攻击的数据量。重要的是要认识到，删除指示不是请求，因此不保证数据实际上会被擦除或变得不可用，除非由图中特定的 geom 保证。如果需要“安全删除”语义，应推入一个将删除指示转换为（一系列）写请求的 geom。“获取属性”支持检查和操作特定提供者或路径上的带外属性。属性由 ASCII 字符串命名，将在下面单独的章节中讨论。

（作者休息脑力和手指时敬请期待：更多内容即将到来。）

## 诊断

通过 `kern.geom.debugflags` sysctl 提供了几个标志，用于跟踪 `GEOM` 操作和解锁保护机制。所有这些标志默认关闭，启用时需格外小心。

**0x01** (`G_T_TOPOLOGY`) 提供拓扑变更事件的跟踪。

**0x02** (`G_T_BIO`) 提供缓冲区 I/O 请求的跟踪。

**0x04** (`G_T_ACCESS`) 提供访问检查控制的跟踪。

**0x08** （未使用）

**0x10** （允许自伤）允许写入秩 1 的提供者。例如，这将允许超级用户覆盖根磁盘上的 MBR，或向已挂载磁盘的其他位置写入随机扇区。其影响是显而易见的。

**0x40** (`G_F_DISKIOCTL`) 此选项目前未使用。

**0x80** (`G_F_CTLDUMP`) 转储 gctl 请求的内容。

## 参见

libgeom(3), geom(8), [DECLARE_GEOM_CLASS(9)](../man9/DECLARE_GEOM_CLASS.9.md), [disk(9)](../man9/disk.9.md), [g_access(9)](../man9/g_access.9.md), [g_attach(9)](../man9/g_attach.9.md), [g_bio(9)](../man9/g_bio.9.md), [g_consumer(9)](../man9/g_consumer.9.md), [g_data(9)](../man9/g_data.9.md), [g_event(9)](../man9/g_event.9.md), [g_geom(9)](../man9/g_geom.9.md), [g_provider(9)](../man9/g_provider.9.md), [g_provider_by_name(9)](../man9/g_provider_by_name.9.md)

## 历史

此软件最初由 Poul-Henning Kamp 和 NAI Labs（Network Associates, Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分，为 FreeBSD 项目开发。

以下过时的 `GEOM` 组件在 FreeBSD 13.0 中被移除：

- `GEOM_BSD`、
- `GEOM_FOX`、
- `GEOM_MBR`、
- `GEOM_SUNLABEL`, 和
- `GEOM_VOL`。

请分别使用

- `GEOM_PART_BSD`、
- `GEOM_MULTIPATH`、
- `GEOM_PART_MBR`, 和
- `GEOM_LABEL`

选项替代。

## 作者

Poul-Henning Kamp <phk@FreeBSD.org>
