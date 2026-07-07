# mksnap_ffs(8)

`mksnap_ffs` — 创建文件系统快照

## 名称

`mksnap_ffs`

## 概要

`mksnap_ffs snapshot_name`

## 描述

`mksnap_ffs` 工具创建名为 `snapshot_name` 的快照。此名称是要创建快照的文件系统中的路径。通常位于文件系统根目录下的 `.snap` 目录中，但也可以位于被快照文件系统中的任何位置。可以使用 snapinfo(8) 命令列出快照。

创建快照后，它会显示为一个文件。快照文件的大小等于创建它的文件系统的大小。它可以被移动、重命名或删除（删除即移除快照）。

文件的组所有者设置为“`operator`”；文件所有者保持为“`root`”。快照的权限模式设置为所有者或“`operator`”组成员可读。

## 实例

创建 **/home** 文件系统的快照并将快照挂载到其他位置：

```sh
mksnap_ffs /home/.snap/snap1
mdconfig -a -t vnode -o readonly -f /home/.snap/snap1
mount -o ro /dev/md0 /mnt/
```

删除快照：

```sh
rm /home/.snap/snap1
```

## 参见

[rm(1)](../man1/rm.1.md), [chmod(2)](../man2/chmod.2.md), [chown(8)](chown.8.md), mdconfig(8), [mount(8)](mount.8.md), snapinfo(8)

## 历史

`mksnap_ffs` 工具首次出现在 FreeBSD 5.1 中。

## 注意事项

磁盘满的情况处理不够优雅，当找不到空闲块时可能导致系统崩溃。

每个文件系统最多只能有 20 个活动快照。达到此限制后，尝试创建更多快照会以 Er ENOSPC 错误失败，`mksnap_ffs` 会报告“out of space”。
