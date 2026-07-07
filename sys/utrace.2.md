# utrace(2)

`utrace` — 在 ktrace 日志中插入用户记录

## 名称

`utrace`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/time.h>`

`#include <sys/uio.h>`

`#include <sys/ktrace.h>`

```c
int
utrace(const void *addr, size_t len);
```

## 描述

向进程跟踪添加一条由用户提供信息的记录。该记录包含 `addr` 所指向内存中的 `len` 字节。此调用仅在调用进程正在被跟踪时才有效。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EINVAL`]** 指定的数据长度 `len` 大于 `KTR_USER_MAXLEN`。

**[`ENOMEM`]** 内存不足，无法满足请求。

**[`ENOSYS`]** 当前运行的内核编译时未包含 [ktrace(2)](ktrace.2.md) 支持（`options KTRACE`）。

## 参见

[kdump(1)](../man1/kdump.1.md), [ktrace(1)](../man1/ktrace.1.md), [truss(1)](../man1/truss.1.md), [ktrace(2)](ktrace.2.md), [sysdecode_utrace(3)](../man3/sysdecode_utrace.3.md)

## 历史

`utrace()` 系统调用首次出现于 FreeBSD 2.2。