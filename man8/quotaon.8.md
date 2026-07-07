# quotaon(8)

`quotaon` — 开启和关闭文件系统配额

## 名称

`quotaon`, `quotaoff`

## 概要

`quotaon [-g] [-u] [-v] filesystem ...` `quotaon [-g] [-u] [-v] -a` `quotaoff [-g] [-u] [-v] filesystem ...` `quotaoff [-g] [-u] [-v] -a`

## 描述

`quotaon` 工具向系统声明应在一个或多个文件系统上启用磁盘配额。`quotaoff` 工具向系统声明指定的文件系统应关闭磁盘配额。指定的文件系统必须在 **`/etc/fstab`** 中有条目并已挂载。`quotaon` 工具期望每个文件系统在相应文件系统的根目录下有名为 `quota.user` 和 `quota.group` 的配额文件。这些默认值可在 **`/etc/fstab`** 中被覆盖。默认情况下，用户配额和组配额都会被启用。

可用选项如下：

**`-a`** 如果提供该选项以替代任何文件系统名称，`quotaon`/`quotaoff` 将启用/禁用 **`/etc/fstab`** 中指示的所有带有磁盘配额的读写文件系统。默认情况下，仅启用 **`/etc/fstab`** 中列出的配额类型。

**`-g`** 仅启用/禁用 **`/etc/fstab`** 中列出的组配额。

**`-u`** 仅启用/禁用 **`/etc/fstab`** 中列出的用户配额。

**`-v`** 使 `quotaon` 和 `quotaoff` 在打开或关闭配额的每个文件系统上打印一条消息。

同时指定 `-g` 和 `-u` 等同于默认行为。

## 文件

**`quota.user`** 位于具有用户配额的文件系统根目录
**`quota.group`** 位于具有组配额的文件系统根目录
**`/etc/fstab`** 文件系统表

## 参见

[quota(1)](../man1/quota.1.md), [quotactl(2)](../sys/quotactl.2.md), [fstab(5)](../man5/fstab.5.md), [edquota(8)](edquota.8.md), [quotacheck(8)](quotacheck.8.md), [repquota(8)](repquota.8.md)

## 历史

`quotaon` 工具出现于 4.2BSD。
