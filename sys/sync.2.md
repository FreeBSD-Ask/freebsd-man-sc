# sync(2)

`sync` — 调度文件系统更新

## 名称

`sync`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
void
sync(void);
```

## 描述

`sync()` 系统调用强制将块缓冲区缓存中的脏（已修改）缓冲区写入磁盘。内核将这些信息保留在内存中，以减少系统所需的磁盘 I/O 传输次数。由于缓存中的信息在系统崩溃后会丢失，内核进程 [syncer(4)](../man4/syncer.4.md) 会频繁地发出 `sync()` 系统调用（大约每 30 秒一次）。

[fsync(2)](fsync.2.md) 系统调用可用于同步单个文件描述符的属性。

## 参见

[fsync(2)](fsync.2.md), [syncer(4)](../man4/syncer.4.md), [sync(8)](../man8/sync.8.md)

## 历史

`sync()` 函数首次出现于 Version 3 AT&T UNIX。

## 缺陷

`sync()` 系统调用可能在缓冲区完全刷新之前就返回。
