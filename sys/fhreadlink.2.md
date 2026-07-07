# fhreadlink(2)

`fhreadlink` — 读取符号链接的值

## 名称

`fhreadlink`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

```c
int
fhreadlink(fhandle_t *fhp, char *buf, size_t bufsize);
```

## 描述

`fhreadlink()` 系统调用将符号链接 `fhp` 的内容放入缓冲区 `buf` 中，该缓冲区大小为 `bufsiz`。`fhreadlink()` 系统调用不会在 `buf` 末尾追加 `NUL` 字符。

## 返回值

调用成功时返回放入缓冲区的字符数，出错时返回 -1，并将错误代码存入全局变量 `errno`。

## 错误

`fhreadlink()` 系统调用在以下情况下会失败：

**[`ENOENT`]** 指定的文件不存在。

**[`ELOOP`]** 在转换文件句柄 `fhp` 时遇到过多的符号链接。

**[`EINVAL`]** 指定的文件不是符号链接。

**[`EIO`]** 从文件系统读取时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFAULT`]** `buf` 参数超出了进程分配的地址空间。

**[`ESTALE`]** 文件句柄 `fhp` 已不再有效。

## 参见

[fhlink(2)](fhlink.2.md), fhstat(2), [readlink(2)](readlink.2.md)

## 历史

`fhreadlink()` 系统调用首次出现于 FreeBSD 12.1。
