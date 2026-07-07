# quotacheck(8)

`quotacheck` — 文件系统配额一致性检查器

## 名称

`quotacheck`

## 概要

`quotacheck [-guv] [-c 32 | 64] [-l maxrun] -a`  
`quotacheck [-guv] [-c 32 | 64] filesystem ...`

## 描述

`quotacheck` 工具检查每个文件系统，构建当前磁盘使用情况表，并将此表与文件系统磁盘配额文件中记录的表进行比较。如果检测到任何不一致，配额文件和错误配额的当前系统副本都会被更新（后者仅在检查活动文件系统时发生）。默认情况下，用户和组配额都会被检查。

以下选项可用：

**`-a`** 如果代替任何文件系统名称提供，`quotacheck` 将检查 **/etc/fstab** 中指示为读写且启用磁盘配额的所有文件系统。默认情况下，仅检查 **/etc/fstab** 中列出的配额类型。

**`-c`** `32 | 64` 在执行检查之前，`quotacheck` 会将配额文件转换为指定的字长。转换大小为 64 用于请求转换为新的 64 位配额文件格式。转换大小为 32 用于请求转换回旧的 32 位配额文件格式。原始配额文件保持不变，并以加下划线及其格式大小加上 `.orig` 扩展名的方式移到一边。因此，原始 32 位 `quota.user` 配额文件转换为 64 位格式配额文件后将重命名为 `quota.user_32.orig`。

**`-g`** 仅检查 **/etc/fstab** 中列出的组配额。

**`-l`** `maxrun` 指定要并行检查的并发文件系统的最大数量。如果省略此选项，或 `maxrun` 为零，则按 [fsck(8)](fsck.8.md) 运行并行遍历。此选项已弃用，并行遍历始终按 [fsck(8)](fsck.8.md) 运行。

**`-u`** 仅检查 **/etc/fstab** 中列出的用户配额。

**`-v`** 报告计算和记录的磁盘配额之间的差异以及其他附加诊断消息。

同时指定 `-g` 和 `-u` 等同于默认值。在所需的文件系统上运行并行遍历，使用 **/etc/fstab** 中的遍历号，方式与 [fsck(8)](fsck.8.md) 相同。

通常，`quotacheck` 静默运行。

`quotacheck` 工具期望每个要检查的文件系统具有名为 `quota.user` 和 `quota.group` 的配额文件，这些文件位于关联文件系统的根目录。这些默认值可以在 **/etc/fstab** 中覆盖。如果文件不存在，`quotacheck` 将创建它。这些文件应使用 [edquota(8)](edquota.8.md) 工具编辑。

`quotacheck` 工具通常在引导时从 **/etc/rc** 文件运行。rc 启动过程由 **/etc/rc.conf** 变量 `check_quotas` 控制。注意，要在 **/etc/rc** 中启用此功能，你还需要在 **/etc/rc.conf** 中使用变量 `enable_quotas` 启用启动配额过程。内核还必须使用 `options QUOTA` 构建。

`quotacheck` 工具在计算每个用户的实际磁盘使用情况时访问原始设备。因此，在 `quotacheck` 运行时，检查的文件系统应处于静止状态。

## 文件

**`quota.user`** 位于文件系统根目录，包含用户配额  
**`quota.group`** 位于文件系统根目录，包含组配额  
**`/etc/fstab`** 默认文件系统

## 参见

[quota(1)](../man1/quota.1.md), [quotactl(2)](../sys/quotactl.2.md), [fstab(5)](../man5/fstab.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [edquota(8)](edquota.8.md), [fsck(8)](fsck.8.md), [quotaon(8)](quotaon.8.md), [repquota(8)](repquota.8.md)

## 历史

`quotacheck` 工具出现在 4.2BSD 中。

## 缺陷

配额系统将忽略当作为有符号值评估时为负的 UID 或 GID。通常，这些类型的 ID 可能来自 NFS 挂载或其他操作系统的归档文件出现在文件系统中。极大的 UID 或 GID 会导致 `quotacheck` 运行不合理的时间，并产生极大的配额数据文件。
