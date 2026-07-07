# i386_get_ioperm(2)

`i386_get_ioperm` — 管理每进程对 i386 I/O 端口空间的访问

## 名称

`i386_get_ioperm`, `i386_set_ioperm`

## 库

Lb libc

## 概要

`#include <machine/sysarch.h>`

```c
int
i386_get_ioperm(unsigned int start, unsigned int *length, int *enable);

int
i386_set_ioperm(unsigned int start, unsigned int length, int enable);
```

## 描述

`i386_get_ioperm()` 系统调用将在 `*enable` 参数中返回进程 I/O 端口空间的权限。端口范围从 `start` 开始，连续条目的数量将在 `*length` 中返回。

`i386_set_ioperm()` 系统调用将把由 `start` 和 `length` 参数描述的 I/O 端口范围的访问权限设置为 `enable` 参数指定的状态。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`i386_get_ioperm()` 和 `i386_set_ioperm()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `start` 或 `length` 参数指定了无效的范围。

**[`EPERM`]** i386_set_ioperm 的调用者不是超级用户。

## 参见

[io(4)](../man4/io.4.md)

## 作者

本手册页由 Jonathan Lemon 编写。