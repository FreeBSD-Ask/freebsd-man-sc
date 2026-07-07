# quota(1)

`quota` — 显示磁盘使用量和限制

## 名称

`quota`

## 概要

`quota [-ghlu] [-f path] [-v | -q | -r] quota [-hlu] [-f path] [-v | -q | -r] user ... quota -g [-hl] [-f path] [-v | -q | -r] group ...`

## 描述

`quota` 实用程序显示用户的磁盘使用量和限制。默认仅打印用户配额。磁盘块使用量和限制以 1024 字节块为单位显示。

以下选项可用：

**`-f`** `path` 仅显示包含指定路径的文件系统的配额信息。可以是已挂载文件系统中的任何文件。

**`-g`** 打印用户所属组的组配额。

**`-h`** “人类可读”输出。使用单位后缀：Byte、Kilobyte、Megabyte、Gigabyte、Terabyte 和 Petabyte。

**`-l`** 不报告 NFS 文件系统上的配额。

**`-q`** 打印更简洁的消息，仅包含使用量超过配额的文件系统信息。`-q` 标志优先于 `-v` 标志。

**`-r`** 显示配额结构中出现的原始配额信息。非零时间值也将以 [ctime(3)](../man3/ctime.3.md) 格式显示。此选项隐含 `-v` 并将覆盖 `-q` 标志。

**`-u`** 打印用户配额。除非指定了 `-g`，否则这是默认行为。

**`-v`** 显示未分配存储的文件系统上的配额。

同时指定 `-g` 和 `-u` 会同时显示用户配额和（该用户的）组配额。

只有超级用户可以使用 `-u` 标志和可选的 `user` 参数查看其他用户的限制。非超级用户可以使用 `-g` 标志和可选的 `group` 参数仅查看其所属组的限制。

`quota` 实用程序尝试报告所有已挂载文件系统的配额。如果文件系统通过 NFS 挂载，它将尝试联系 NFS 服务器上的 rpc.rquotad(8) 守护进程。对于 UFS 文件系统，必须在 **/etc/fstab** 中启用配额。如果 `quota` 以非零状态退出，表示一个或多个文件系统超过配额，或 `-f` 选项指定的路径不存在。

如果指定了 `-l` 标志，`quota` 将不检查 NFS 文件系统。

## 文件

**`quota.user`** 位于文件系统根目录，包含用户配额

**`quota.group`** 位于文件系统根目录，包含组配额

**/etc/fstab** 用于查找文件系统名称和位置

## 参见

[quotactl(2)](../man2/quotactl.2.md), [ctime(3)](../man3/ctime.3.md), [fstab(5)](../man5/fstab.5.md), [edquota(8)](../man8/edquota.8.md), [quotacheck(8)](../man8/quotacheck.8.md), [quotaon(8)](../man8/quotaon.8.md), [repquota(8)](../man8/repquota.8.md), rpc.rquotad(8)

## 历史

`quota` 命令出现于 4.2BSD。
