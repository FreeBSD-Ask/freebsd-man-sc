# posix_spawnattr_getpgroup(3)

`posix_spawnattr_getpgroup` — 获取和设置 spawn 属性对象的 spawn-pgroup 属性

## 名称

`posix_spawnattr_getpgroup`, `posix_spawnattr_setpgroup`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getpgroup(const posix_spawnattr_t *restrict attr,
    pid_t *restrict pgroup);

int
posix_spawnattr_setpgroup(posix_spawnattr_t *attr, pid_t pgroup);
```

## 描述

`posix_spawnattr_getpgroup` 函数从 `attr` 所引用的属性对象中获取 spawn-pgroup 属性的值。

`posix_spawnattr_setpgroup` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-pgroup 属性。

spawn-pgroup 属性表示在 spawn 操作中（若 spawn-flags 属性中设置了 `POSIX_SPAWN_SETPGROUP`）新进程镜像要加入的进程组。该属性的默认值为零。

## 返回值

`posix_spawnattr_getpgroup` 和 `posix_spawnattr_setpgroup` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnp(3)

## 标准

`posix_spawnattr_getpgroup` 和 `posix_spawnattr_setpgroup` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_spawnattr_getpgroup` 和 `posix_spawnattr_setpgroup` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
