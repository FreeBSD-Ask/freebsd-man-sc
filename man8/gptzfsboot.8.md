# gptzfsboot(8)

`gptzfsboot` — 用于基于 BIOS 的计算机上从 ZFS 启动的 GPT 引导代码

## 名称

`gptzfsboot`

## 描述

`gptzfsboot` 用于在基于 BIOS 的计算机上从 ZFS 存储池中的文件系统引导系统。`gptzfsboot` 通过 [gpart(8)](gpart.8.md) 安装到 GPT 分区磁盘的 `freebsd-boot` 分区中。

## 实现说明

GPT 标准允许可变数量的分区，但 `gptzfsboot` 只能从包含 128 个或更少分区的分区表引导。

## 引导

`gptzfsboot` 会尝试查找所有由 BIOS 可见的硬盘或其上的分区所组成的 ZFS 存储池。`gptzfsboot` 会在所有可见磁盘以及已发现的受支持分区中（针对所有受支持的分区方案类型）查找 ZFS 设备标签。搜索从加载 `gptzfsboot` 自身的磁盘开始。其他磁盘按 BIOS 定义的顺序进行探测。在对磁盘进行探测后，如果 `gptzfsboot` 确定整盘不是 ZFS 存储池的成员，则会按分区表中的顺序逐一探测各分区。目前支持 GPT 和 MBR 分区方案。对于 GPT 方案，仅探测 `freebsd-zfs` 类型的分区。在探测过程中看到的第一个存储池将作为默认引导存储池。

由存储池的 `bootfs` 属性指定的文件系统作为默认引导文件系统。如果未设置 `bootfs` 属性，则使用该存储池的根文件系统作为默认值。从引导文件系统加载 [loader(8)](loader.8.md)。如果引导文件系统中存在 `/boot.config` 或 `/boot/config`，则从中读取引导选项，方式与 [boot(8)](boot.8.md) 相同。

第一个成功探测到的设备以及第一个检测到的存储池的 ZFS GUID 会通过 `vfs.zfs.boot.primary_vdev` 和 `vfs.zfs.boot.primary_pool` 变量提供给 [loader(8)](loader.8.md)。

## 用法

通常 `gptzfsboot` 会以完全自动的模式引导。但与 [boot(8)](boot.8.md) 一样，可以中断自动引导过程，并通过提示符与 `gptzfsboot` 交互。`gptzfsboot` 接受 [boot(8)](boot.8.md) 支持的所有选项。

文件系统规范和 [loader(8)](loader.8.md) 的路径与 [boot(8)](boot.8.md) 不同。其格式为

`[[zfs:pool/filesystem:][/path/to/loader]]`

文件系统和路径都可以指定。如果仅指定路径，则使用默认文件系统。如果仅指定存储池和文件系统，则使用 `/boot/loader` 作为路径。

此外，可以使用 `status` 命令查询有关已发现存储池的信息。输出格式与 `zpool status`（参见 zpool(8)）类似。

已配置或自动确定的 ZFS 引导文件系统会存储在 [loader(8)](loader.8.md) 的 `loaddev` 变量中，并同时设置为 `currdev` 变量的初始值。

## 文件

**`/boot/gptzfsboot`** 引导代码二进制文件

**`/boot.config`** 引导块参数（可选）

**`/boot/config`** 引导块的替代参数（可选）

## 实例

`gptzfsboot` 通常与“保护性 MBR”（参见 [gpart(8)](gpart.8.md)）配合安装。要在 `ada0` 驱动器上安装 `gptzfsboot`：

```sh
gpart bootcode -b /boot/pmbr -p /boot/gptzfsboot -i 1 ada0
```

也可以不带 PMBR 安装 `gptzfsboot`：

```sh
gpart bootcode -p /boot/gptzfsboot -i 1 ada0
```

## 参见

[boot.config(5)](../man5/boot.config.5.md), [boot(8)](boot.8.md), [gpart(8)](gpart.8.md), [loader(8)](loader.8.md), zpool(8)

## 历史

`gptzfsboot` 出现于 FreeBSD 7.3。

## 作者

本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。

## 缺陷

`gptzfsboot` 仅在 MBR 分区（在 FreeBSD 中称为 slice）中查找 ZFS 元数据。它不会查看传统上称为 partition 的 BSD disklabel(8) 分区。如果某个 disklabel 分区恰好被放置在使得 ZFS 元数据可在相对于 slice 的固定偏移处找到的位置，那么 `gptzfsboot` 会将该分区识别为 ZFS 存储池的一部分，但这并不保证一定会发生。
