# repquota(8)

`repquota` — 汇总文件系统的配额

## 名称

`repquota`

## 概要

`repquota [-h] [-g] [-n] [-u] [-v] filesystem ...` `repquota [-h] [-g] [-n] [-u] [-v] -a`

## 描述

`repquota` 工具打印指定文件系统的磁盘使用量和配额汇总。

可用选项如下：

**`-a`** 打印 **`/etc/fstab`** 中列出的所有文件系统的配额。

**`-g`** 仅打印组配额（默认情况下，如果组配额和用户配额都存在，则两者都打印）。

**`-h`** 以更易读的格式显示信息，而不是以历史上的千字节格式。

**`-n`** 以数字形式显示用户和组 ID，而不是转换为用户名或组名。

**`-u`** 仅打印用户配额（默认情况下，如果组配额和用户配额都存在，则两者都打印）。

**`-v`** 在打印每个文件系统的配额之前打印一个标题行。

对于每个用户或组，打印当前文件数和空间量，以及使用 [edquota(8)](edquota.8.md) 创建的任何配额。

只有 operator 组的成员或超级用户可以使用此命令。

## 文件

**`quota.user`** 位于具有用户配额的文件系统根目录
**`quota.group`** 位于具有组配额的文件系统根目录
**`/etc/fstab`** 用于文件系统名称和位置

## 诊断

有关无法访问文件的各种消息；不言自明。

## 参见

[quota(1)](../man1/quota.1.md), [quotactl(2)](../sys/quotactl.2.md), [fstab(5)](../man5/fstab.5.md), [edquota(8)](edquota.8.md), [quotacheck(8)](quotacheck.8.md), [quotaon(8)](quotaon.8.md)

## 历史

`repquota` 工具出现于 4.2BSD。
