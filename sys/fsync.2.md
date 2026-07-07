# fsync(2)

`fdatasync` — 同步对文件的更改

## 名称

`fdatasync`, `fsync`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
fdatasync(int fd);
```

```c
int
fsync(int fd);
```

## 描述

`fsync` 系统调用将文件描述符 `fd` 所引用文件的所有已修改数据和属性移动到永久存储设备。这通常会导致关联文件的所有内存中已修改缓冲区副本被写入磁盘。

`fdatasync` 系统调用将 `fd` 的所有已修改数据移动到永久存储设备。与 `fsync` 不同，该系统调用不保证将文件属性或访问文件所需的元数据提交到永久存储。

`fsync` 系统调用应当被要求文件处于已知状态的程序使用，例如在构建简单的事务设施时。如果文件元数据已被提交，使用 `fdatasync` 可能比 `fsync` 更高效。

`fdatasync` 和 `fsync` 调用都是取消点。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`fsync` 和 `fdatasync` 调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`EINVAL`]** `fd` 参数引用的是 socket，而非文件。

**[`EIO`]** 在对文件系统进行读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 在从文件系统读取时检测到损坏的数据。

## 参见

[fsync(1)](../man1/fsync.1.md), [sync(2)](sync.2.md), [syncer(4)](../man4/syncer.4.md), [sync(8)](../man8/sync.8.md)

## 历史

`fsync` 系统调用出现于 4.2BSD。`fdatasync` 系统调用出现于 FreeBSD 11.1。

## 缺陷

`fdatasync` 系统调用目前不保证在系统调用返回之前，已为 `fd` 所引用文件排队的 [aio(4)](../man4/aio.4.md) 请求已完成。
