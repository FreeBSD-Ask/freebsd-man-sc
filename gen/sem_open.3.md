# sem_open(3)

`sem_open` — 命名信号量操作

## 名称

`sem_open`, `sem_close`, `sem_unlink`

## 库

Lb libc

## 概要

```c
#include <semaphore.h>

sem_t *
sem_open(const char *name, int oflag, ...);

int
sem_close(sem_t *sem);

int
sem_unlink(const char *name);
```

## 描述

`sem_open()` 函数创建或打开由 `name` 指定的命名信号量。返回的信号量可用于后续对 [sem_getvalue(3)](sem_getvalue.3.md)、[sem_wait(3)](sem_wait.3.md)、sem_trywait(3)、[sem_post(3)](sem_post.3.md) 和 `sem_close()` 的调用。

本实现对 `name` 的值有严格的要求：必须以斜杠（`/`）开头，且不包含其他斜杠字符。

`oflag` 参数中可设置以下位：

**`O_CREAT`** 如果信号量不存在则创建。对 `sem_open()` 调用的第三个参数必须是 `mode_t` 类型，指定信号量的模式。仅检查 `S_IWUSR`、`S_IWGRP` 和 `S_IWOTH` 位；无法仅授予信号量的“读”权限。该模式会根据进程的文件创建掩码进行修改；参见 [umask(2)](../man2/umask.2.md)。第四个参数必须是 `unsigned int` 类型，指定信号量的初始值，且不得大于 `SEM_VALUE_MAX`。

**`O_EXCL`** 如果信号量不存在则创建。如果信号量已存在，`sem_open()` 将失败。除非同时指定了 `O_CREAT`，否则此标志被忽略。

`sem_close()` 函数关闭由 `sem_open()` 调用所打开的命名信号量。

`sem_unlink()` 函数移除名为 `name` 的信号量。只有当所有打开该信号量的进程都将其关闭后，分配给该信号量的资源才会被释放。

## 返回值

若成功，`sem_open()` 函数返回所打开信号量的地址。如果同一进程对 `sem_open()` 的多次调用使用相同的 `name` 参数，且中间没有调用 `sem_close()`，则每次返回相同的地址。如果信号量无法打开，`sem_open()` 返回 `SEM_FAILED`，并设置全局变量 `errno` 以指示错误。

若成功完成，`sem_close()` 和 `sem_unlink()` 返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_open()` 函数在以下情况下会失败：

**`[EACCES]`** 信号量已存在，且创建时由 `oflag` 指定的权限拒绝本进程访问。

**`[EACCES]`** 信号量不存在，但拒绝创建权限。

**`[EEXIST]`** 设置了 `O_CREAT` 和 `O_EXCL`，但信号量已存在。

**`[EINTR]`** 调用被信号中断。

**`[EINVAL]`** 对给定的 `name` 不支持 `sem_open()` 操作。

**`[EINVAL]`** `value` 参数大于 `SEM_VALUE_MAX`。

**`[ENAMETOOLONG]`** `name` 参数过长。

**`[ENFILE]`** 已达到系统的信号量数量限制。

**`[ENOENT]`** 未设置 `O_CREAT`，但指定的命名信号量不存在。

**`[ENOSPC]`** 没有足够的空间创建信号量。

`sem_close()` 函数在以下情况下会失败：

**`[EINVAL]`** `sem` 参数不是有效的信号量。

`sem_unlink()` 函数在以下情况下会失败：

**`[EACCES]`** 拒绝移除信号量的权限。

**`[ENAMETOOLONG]`** 指定的 `name` 过长。

**`[ENOENT]`** 指定的命名信号量不存在。

## 参见

[close(2)](../man2/close.2.md), [open(2)](../man2/open.2.md), [umask(2)](../man2/umask.2.md), [unlink(2)](../man2/unlink.2.md), [sem_getvalue(3)](sem_getvalue.3.md), [sem_post(3)](sem_post.3.md), sem_trywait(3), [sem_wait(3)](sem_wait.3.md)

## 标准

`sem_open()`、`sem_close()` 和 `sem_unlink()` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。

## 历史

命名信号量的支持首次出现在 FreeBSD 5.0 中。
