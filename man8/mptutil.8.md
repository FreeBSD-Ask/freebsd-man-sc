# mptutil(8)

`mptutil` — 管理 LSI Fusion-MPT 控制器的实用工具

## 名称

`mptutil`

## 概要

`mptutil version`  
`mptutil [-u unit] show adapter`  
`mptutil [-u unit] show config`  
`mptutil [-u unit] show drives`  
`mptutil [-u unit] show events`  
`mptutil [-u unit] show volumes`  
`mptutil [-u unit] fail drive`  
`mptutil [-u unit] online drive`  
`mptutil [-u unit] offline drive`  
`mptutil [-u unit] name volume name`  
`mptutil [-u unit] volume status volume`  
`mptutil [-u unit] volume cache volume enable|enabled|disable|disabled`  
`mptutil [-u unit] clear`  
`mptutil [-u unit] create type [-q] [-v] [-s stripe_size] drive[,drive[,...]]`  
`mptutil [-u unit] delete volume`  
`mptutil [-u unit] add drive [volume]`  
`mptutil [-u unit] remove drive`

## 描述

`mptutil` 工具可用于显示或修改 LSI Fusion-MPT 控制器上的各种参数。每次调用 `mptutil` 由零个或多个全局选项后跟一个命令组成。命令可以在命令之后支持额外的可选或必需参数。

当前支持一个全局选项：

**`-u`** `unit` `unit` 指定要使用的控制器单元。如果未指定单元，则使用单元 0。

卷可以用两种形式指定。第一种，卷可以通过其位置标识为 [`xx`:]`yy`，其中 `xx` 是总线 ID，`yy` 是目标 ID。如果省略总线 ID，则假定卷位于总线 0 上。第二种，卷可以通过相应的 *daX* 设备指定，如 *da0*。

[mpt(4)](../man4/mpt.4.md) 控制器将驱动器分为两类。已配置的驱动器作为成员驱动器或热备盘属于 RAID 卷。每个已配置的驱动器被分配一个唯一的设备 ID，如 0 或 1，显示在 `show config` 中，以及 `show drives` 的第一列中。任何未作为成员或热备盘与 RAID 卷关联的驱动器都是独立驱动器。独立驱动器作为 SCSI 磁盘设备对操作系统可见。因此，驱动器可以用三种形式指定。第一种，已配置的驱动器可以通过其设备 ID 标识。第二种，任何驱动器可以通过其位置标识为 `xx`:`yy`，其中 `xx` 是总线 ID，`yy` 是每个驱动器的目标 ID，如 `show drives` 中所示。注意，与卷不同，驱动器位置始终需要总线 ID，以避免与设备 ID 混淆。第三种，不属于卷的独立驱动器可以通过其对应的 *daX* 设备标识，如 `show drives` 中所示。

`mptutil` 工具支持几组不同的命令。第一组命令提供有关控制器、它管理的卷以及它控制的驱动器的信息。第二组命令用于管理连接到控制器的物理驱动器。第三组命令用于管理控制器管理的逻辑卷。第四组命令用于管理控制器的驱动器配置。

信息命令包括：

**`version`** 显示 `mptutil` 的版本。

**`show adapter`** 显示有关 RAID 控制器的信息，如型号。

**`show config`** 显示控制器的卷和驱动器配置。每个卷连同该卷跨越的物理驱动器一起列出。如果配置了任何热备盘驱动器，则也会列出它们。

**`show drives`** 列出连接到控制器的所有物理驱动器。

**`show events`** 显示控制器事件日志中的所有条目。由于缺乏文档，此命令目前不太有用，仅以十六进制转储每个日志条目。

**`show volumes`** 列出控制器管理的所有逻辑卷。

物理驱动器管理命令包括：

**`fail`** `drive` 将 `drive` 标记为“failed requested”。注意，此状态与固件使驱动器失败时使用的“failed”状态不同。`Drive` 必须是已配置的驱动器。

**`online`** `drive` 将 `drive` 标记为在线驱动器。`Drive` 必须是处于“offline”或“failed requested”状态的已配置驱动器。

**`offline`** `drive` 将 `drive` 标记为离线。`Drive` 必须是已配置的在线驱动器。

逻辑卷管理命令包括：

**`name`** `volume` `name` 将 `volume` 的名称设置为 `name`。

**`volume cache`** `volume` `enable|enabled|disable|disabled` 为 `volume` 的成员驱动器启用或禁用驱动器写缓存。

**`volume status`** `volume` 显示有关单个卷的更详细状态，包括如果正在执行重建操作的当前进度。

配置命令包括：

**`raid0`** 创建一个跨越单个驱动器列表中列出的驱动器的 RAID0 卷。

**`raid1`** 创建一个跨越单个驱动器列表中列出的驱动器的 RAID1 卷。

**`raid1e`** 创建一个跨越单个驱动器列表中列出的驱动器的 RAID1E 卷。

**`clear`** 删除整个配置，包括所有卷和热备盘。所有驱动器将成为独立驱动器。

**`create`** `type` [`-q`] [`-v`] [`-s` `stripe_size`] `drive`[,`drive`[,...]] 创建新卷。`type` 指定要创建的卷类型。当前支持的类型包括：**注意：** 并非所有控制器都支持所有卷类型。如果在 `type` 之后指定了 `-q` 标志，则将对卷执行“快速”初始化。当驱动器不包含需要保留的任何现有数据时，这很有用。如果在 `type` 之后指定了 `-v` 标志，则将启用更详细的输出。目前这只是在构建配置时随着驱动器添加到卷中而提供通知。`-s` `stripe_size` 参数允许设置阵列的条带大小。默认使用 64K 的条带大小。给定 `type` 的有效值列表列在 `show adapter` 的输出中。

**`delete`** `volume` 删除卷 `volume`。成员驱动器将成为独立驱动器。

**`add`** `drive` [`volume`] 将 `drive` 标记为热备盘。`Drive` 不能是卷的成员。如果指定了 `volume`，则热备盘将专用于该卷。否则，`drive` 将用作支持此控制器所有卷的全局热备盘。注意，`drive` 必须与其将要支持的所有卷中最小的驱动器一样大。

**`remove`** `drive` 将热备盘 `drive` 从服务中移除。它将成为独立驱动器。

## 实例

将总线 0 目标 4 处的驱动器标记为离线：

```sh
`mptutil` `offline 0:4`
```

从两个独立驱动器 `da1` 和 `da2` 创建 RAID1 阵列：

```sh
`mptutil` `create raid1 da1,da2`
```

将独立驱动器 `da3` 标记为全局热备盘：

```sh
`mptutil` `add da3`
```

## 参见

[mpt(4)](../man4/mpt.4.md)

## 历史

`mptutil` 工具首次出现在 FreeBSD 8.0 中。

## 缺陷

热备盘的处理似乎不可靠。[mpt(4)](../man4/mpt.4.md) 固件通过热备盘“池”管理热备盘。有八个编号为 0 到 7 的池。每个热备盘只能分配给一个池。每个卷可以由零个或多个热备盘池的任意组合支持。`mptutil` 工具尝试使用以下算法管理热备盘。全局热备盘始终分配给池 0，所有卷始终由池 0 支持。对于专用热备盘，`mptutil` 将剩余 7 个池中的一个分配给每个卷，并将专用驱动器分配给该池。但实际上，将驱动器分配为热备盘似乎直到机器重启后才生效。此外，固件在重启后重新编号热备盘池分配，这撤销了上述算法的效果。简单情况如分配全局热备盘似乎可以正常工作（尽管需要重启才能生效），但更“异类”的配置可能无法可靠工作。

驱动器配置命令会导致控制台上消息过度泛滥。

`mptutil` 和 [mpt(4)](../man4/mpt.4.md) 使用的 mpt 版本 1 API 不支持超过 2 TB 的卷。这是 API 的限制。如果在大于 2 TB 的卷上使用此适配器，请以 JBOD 模式使用适配器。利用 geom(8)、[zfs(8)](zfs.8.md) 或其他软件卷管理器来解决此限制。
