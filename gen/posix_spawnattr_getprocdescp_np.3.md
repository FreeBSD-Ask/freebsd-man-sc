# posix_spawnattr_getprocdescp_np(3)

`posix_spawnattr_getprocdescp_np` — 获取和设置 spawn 属性对象的 spawn-procdescp 属性

## 名称

`posix_spawnattr_getprocdesp_np`, `posix_spawnattr_setprocdescp_np`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getprocdescp_np(const posix_spawnattr_t *restrict attr,
    int **restrict fdpp, int *restrict pdrflagsp);

int
posix_spawnattr_setprocdescp_np(posix_spawnattr_t *attr,
    int *restrict fdp, int pdrflags);
```

## 描述

`posix_spawnattr_getprocdescp_np` 函数从 `attr` 所引用的属性对象中获取 spawn-procdescp 属性的值。

`posix_spawnattr_procdescp_np` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-procdescp 属性。

spawn-procdescp 属性提供在成功 spawn 后存储子进程文件描述符的位置。将该属性设置为非 NULL 值会隐式请求创建引用子进程的文件描述符。该描述符将由 pdrfork(2) 系统调用创建，当该属性设置为 `NULL` 时，将使用它替代 fork/vfork/rfork(2)。

如果该属性设置为 `NULL` 以外的值，则它必须是指向 `int` 类型变量的有效指针，所得描述符将存储于该变量中。`pdrflags` 参数指定 [pdfork(2)](../sys/pdfork.2.md) 系统调用所接受的附加标志。有效标志列表参见其说明。注意，`PD_CLOEXEC` 标志始终被设置，以防止进程描述符泄漏到新创建的子进程中。

spawn-procdescp 属性的默认值为 `NULL`，表示不会创建进程描述符。

## 返回值

`posix_spawnattr_getprocdescp_np` 和 `posix_spawnattr_setprocdescp_np` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnp(3)

## 标准

`posix_spawnattr_getprocdescp_np` 和 `posix_spawnattr_setprocdescp_np` 是 FreeBSD 扩展，首次出现于 FreeBSD 16.0。
