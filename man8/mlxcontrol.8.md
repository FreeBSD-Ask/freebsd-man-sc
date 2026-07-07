# mlxcontrol(8)

`mlxcontrol` — Mylex DAC 系列 RAID 管理工具

## 名称

`mlxcontrol`

## 概要

`mlxcontrol <command> [args]`

`mlxcontrol status [-qv] [drive]`

`mlxcontrol rescan controller [controller ...]`

`mlxcontrol detach drive [drive ...]`

`mlxcontrol detach -a`

`mlxcontrol check drive`

`mlxcontrol config controller`

`mlxcontrol help command`

## 描述

`mlxcontrol` 工具为连接到 [mlx(4)](../man4/mlx.4.md) 驱动程序的设备提供状态监控和管理功能。

控制器名称形式为“mlxN”，其中 N 是控制器的单元号。驱动器名称形式为“mlxdN”，其中 N 是驱动器的单元号。请勿指定设备节点的路径。

**status** 打印控制器和系统驱动器的状态。如果指定了一个或多个驱动器，则仅打印这些驱动器的信息，否则打印系统中所有控制器和驱动器的信息。使用 `-v` 标志可显示更详细的信息。使用 `-q` 标志则不打印任何输出。如果所有受测驱动器均在线，此命令返回 0；如果一个或多个驱动器处于临界状态，返回 1；如果一个或多个驱动器离线，返回 2。

**rescan** 重新扫描一个或多个控制器以查找未附加的系统驱动器（例如已分离或在驱动程序初始化之后创建的驱动器）。如果提供了 `-a` 标志，则重新扫描系统中的所有控制器。

**detach** 分离一个或多个系统驱动器。驱动器必须已卸载且未被任何其他工具打开，此命令才能成功。如果提供了 `-a` 标志，则从指定控制器分离所有系统驱动器。

**check** 对冗余系统驱动器（例如 RAID1 或 RAID5）启动一致性检查和修复过程。控制器将扫描系统驱动器并修复任何不一致之处。此命令立即返回；使用 `status` 命令监控检查进度。

**rebuild** 需要两个参数，`controller` 和 `physdrive`，如 `status` 命令输出中所指定。使用物理驱动器 `physdrive` 上空间的所有系统驱动器都将被重建，重构该驱动器上的所有数据。请注意，每个控制器一次只能执行一个重建操作。此命令立即返回；使用 `status` 命令监控重建进度。

**config** 从指定控制器打印当前配置。此命令将在未来版本中更新，以允许从配置中添加/删除系统驱动器。

**help** 打印 `command` 的用法信息。

## 作者

`mlxcontrol` 工具由 Michael Smith <msmith@FreeBSD.org> 编写。

## 缺陷

`config` 命令尚不支持修改系统驱动器配置。

尚不支持错误日志提取。
