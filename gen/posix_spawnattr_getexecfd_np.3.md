# posix_spawnattr_getexecfd_np(3)

`posix_spawnattr_getexecfd_np` — 获取和设置 spawn 属性对象的 spawn-execfd 属性

## 名称

`posix_spawnattr_getexecfd_np`, `posix_spawnattr_setexecfd_np`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getexecfd_np(const posix_spawnattr_t *restrict attr,
    int *restrict fdp);

int
posix_spawnattr_setexecfd_np(posix_spawnattr_t *attr, int fd);
```

## 描述

`posix_spawnattr_getexecfd_np` 函数从 `attr` 所引用的属性对象中获取 spawn-execfd 属性的值。

`posix_spawnattr_setexecfd_np` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-execfd 属性。

spawn-execfd 属性提供文件描述符，[posix_spawn(3)](posix_spawn.3.md) 系列函数使用该描述符在派生进程中执行新镜像。如果该属性设置为 -1 以外的值，则它必须是未设置 `O_CLOFORK` 标志的有效文件描述符。随后，`posix_spawn` 使用 fexecve(2) 系统调用在新创建的进程中执行该文件描述符所引用的可执行镜像。在此情况下，`posix_spawn` 的 `path` 参数被忽略。

spawn-execfd 属性的默认值为 -1，表示执行镜像由 `posix_spawn` 的 `path` 参数指定。

## 返回值

`posix_spawnattr_getexecfd_np` 和 `posix_spawnattr_setexecfd_np` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnp(3)

## 标准

`posix_spawnattr_getexecfd_np` 和 `posix_spawnattr_setexecfd_np` 是 FreeBSD 扩展，首次出现于 FreeBSD 16.0。
