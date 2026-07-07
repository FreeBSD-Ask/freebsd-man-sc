# sync(8)

`sync` — 强制完成待处理的磁盘写入（刷新缓存）

## 名称

`sync`

## 概要

`sync`

## 描述

调用 `sync` 工具可以确保在处理器以 [reboot(8)](reboot.8.md) 或 [halt(8)](reboot.8.md) 不适合的方式停止之前，所有磁盘写入都已完成。通常，使用 [reboot(8)](reboot.8.md) 或 [halt(8)](reboot.8.md) 关闭系统更可取，因为它们在执行最终 `sync` 之前可能会执行额外的操作，例如重新同步硬件时钟和刷新内部缓存。

`sync` 工具使用 [sync(2)](../sys/sync.2.md) 函数调用。

## 参见

[fsync(2)](../sys/fsync.2.md), [sync(2)](../sys/sync.2.md), [syncer(4)](../man4/syncer.4.md), [halt(8)](reboot.8.md), [reboot(8)](reboot.8.md)

## 历史

`sync` 工具出现于 Version 4 AT&T UNIX。

在早于 4.0BSD 的系统上，没有 [reboot(8)](reboot.8.md) 和 [halt(8)](reboot.8.md) 之类的命令。关机过程包括运行 `sync`，等待指示灯停止闪烁，然后关闭机器电源。

发出三个单独的 `sync` 命令（每行一个）是一种安慰剂做法，在原本已处于静默状态的 Version 7 AT&T UNIX 机器上通常足够了。它以每行一个 `sync` 的方式替代了等待。

4.0BSD 引入了 [reboot(2)](../sys/reboot.2.md) 和 [sync(2)](../sys/sync.2.md)，使这个技巧过时了。
