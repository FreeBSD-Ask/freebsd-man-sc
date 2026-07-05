# fsync.1

`fsync` — 将文件在内存中的状态与磁盘上的状态同步

## 名称

`fsync`

## 概要

`fsync file`

## 描述

`fsync` 实用程序会将命令行上所列出的全部文件已修改的数据和元数据写入永久存储设备。

`fsync` 实用程序使用 fsync(2) 函数调用。

## 退出状态

如果发生错误，`fsync` 实用程序会继续处理下一个文件，并以大于 0 的值退出。否则以 0 退出。

## 参见

fsync(2), sync(2), [syncer(4)](../man4/syncer.4.md), [halt(8)](../man8/halt.8.md), [reboot(8)](../man8/reboot.8.md)

## 历史

`fsync` 命令首次出现于 FreeBSD 4.3。
