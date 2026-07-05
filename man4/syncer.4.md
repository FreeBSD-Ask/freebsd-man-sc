# syncer.4

`syncer` — 文件系统同步器内核进程

## 名称

`syncer`

## 概要

`syncer`

## 描述

`syncer` 内核进程通过将易失的缓存文件系统数据刷新到磁盘，帮助保护磁盘卷的完整性。

内核将所有 [vnode(9)](../man9/vnode.9.md) 放入多个队列中。`syncer` 进程以轮转方式处理这些队列，通常每秒处理一个队列。对于该队列中的每个 [vnode(9)](../man9/vnode.9.md)，`syncer` 进程强制将其脏缓冲区写入磁盘。

缓冲区变脏与缓冲区被同步之间的常规延迟由以下 [sysctl(8)](../man8/sysctl.8.md) 可调变量控制：

| *变量* | *默认值* | *说明* |
| --- | --- | --- |
| `kern.filedelay` | 30 | 延迟同步文件的时间 |
| `kern.dirdelay` | 29 | 延迟同步目录的时间 |
| `kern.metadelay` | 28 | 延迟同步元数据的时间 |

## 参见

sync(2), fsck(8), sync(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`syncer` 进程是“update”命令的后代，后者出现于 Version 6 AT&T UNIX，通常在系统进入多用户模式时由 **`/etc/rc`** 启动。内核发起的“update”进程首次出现于 FreeBSD 2.0。

## 缺陷

在某些系统上，sync(2) 与崩溃同时发生可能导致文件系统损坏。参见 fsck(8)。
