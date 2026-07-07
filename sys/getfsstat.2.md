# getfsstat(2)

`getfsstat` — 获取所有已挂载文件系统的列表

## 名称

`getfsstat`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/ucred.h>`

`#include <sys/mount.h>`

```c
int
getfsstat(struct statfs *buf, long bufsize, int mode);
```

## 描述

`getfsstat()` 系统调用返回所有已挂载文件系统的信息。`buf` 参数是指向 `statfs` 结构的指针，如 [statfs(2)](statfs.2.md) 中所述。

对于特定文件系统未定义的字段被设置为 -1。缓冲区被填充为 `statfs` 结构数组，每个已挂载文件系统对应一个结构，最多填充到 `bufsize` 指定的字节数。注意，`bufsize` 参数是 `buf` 能容纳的字节数，而不是它能容纳的 `statfs` 结构数量。

如果 `buf` 指定为 NULL，`getfsstat()` 仅返回已挂载文件系统的数量。

通常 `mode` 应指定为 `MNT_WAIT`。如果 `mode` 设置为 `MNT_NOWAIT`，`getfsstat()` 将返回其可用的信息，而不向每个文件系统请求更新。因此，某些信息将会过时，但 `getfsstat()` 不会因等待无法响应的文件系统返回信息而阻塞。它还会跳过任何正在卸载过程中的文件系统，即使卸载最终会失败。

## 返回值

成功完成时，返回 `statfs` 结构的数量。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getfsstat()` 系统调用在以下情况下会失败：

**[`EFAULT`]** `buf` 参数指向无效地址。

**[`EINVAL`]** `mode` 设置为 `MNT_WAIT` 或 `MNT_NOWAIT` 以外的值。

**[`EIO`]** 从文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

## 参见

[statfs(2)](statfs.2.md), [fstab(5)](../man5/fstab.5.md), [mount(8)](../man8/mount.8.md)

## 历史

`getfsstat()` 系统调用首次出现于 4.4BSD。
