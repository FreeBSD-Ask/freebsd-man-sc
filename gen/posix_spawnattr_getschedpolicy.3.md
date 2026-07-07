# posix_spawnattr_getschedpolicy(3)

`posix_spawnattr_getschedpolicy` — 获取和设置 spawn 属性对象的 spawn-schedpolicy 属性

## 名称

`posix_spawnattr_getschedpolicy`, `posix_spawnattr_setschedpolicy`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getschedpolicy(const posix_spawnattr_t *restrict attr,
    int *restrict schedpolicy);

int
posix_spawnattr_setschedpolicy(posix_spawnattr_t *attr, int schedpolicy);
```

## 描述

`posix_spawnattr_getschedpolicy` 函数从 `attr` 所引用的属性对象中获取 spawn-schedpolicy 属性的值。

`posix_spawnattr_setschedpolicy` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-schedpolicy 属性。

spawn-schedpolicy 属性表示在 spawn 操作中（若 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSCHEDULER`）要分配给新进程镜像的调度策略。该属性的默认值未指定。

## 返回值

`posix_spawnattr_getschedpolicy` 和 `posix_spawnattr_setschedpolicy` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_getschedparam(3)](posix_spawnattr_getschedparam.3.md), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnattr_setschedparam(3), posix_spawnp(3)

## 标准

`posix_spawnattr_getschedpolicy` 和 `posix_spawnattr_setschedpolicy` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_spawnattr_getschedpolicy` 和 `posix_spawnattr_setschedpolicy` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
