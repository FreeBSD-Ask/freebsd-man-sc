# posix_spawnattr_getflags(3)

`posix_spawnattr_getflags` — 获取和设置 spawn 属性对象的 spawn-flags 属性

## 名称

`posix_spawnattr_getflags`, `posix_spawnattr_setflags`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getflags(const posix_spawnattr_t *restrict attr,
    short *restrict flags);

int
posix_spawnattr_setflags(posix_spawnattr_t *attr, short flags);
```

## 描述

`posix_spawnattr_getflags` 函数从 `attr` 所引用的属性对象中获取 spawn-flags 属性的值。

`posix_spawnattr_setflags` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-flags 属性。

spawn-flags 属性用于指示调用 `posix_spawn` 或 `posix_spawnp` 时在新进程镜像中要更改的进程属性。它是下列零个或多个标志的按位或（参见 `posix_spawn`）：

`POSIX_SPAWN_RESETIDS`

`POSIX_SPAWN_SETPGROUP`

`POSIX_SPAWN_SETSIGDEF`

`POSIX_SPAWN_SETSIGMASK`

`POSIX_SPAWN_SETSCHEDPARAM`

`POSIX_SPAWN_SETSCHEDULER`

`POSIX_SPAWN_DISABLE_ASLR_NP`

这些标志定义于

```c
#include <spawn.h>
```

该属性的默认值等同于未设置任何标志。

## 返回值

`posix_spawnattr_getflags` 函数返回零。`posix_spawnattr_setflags` 函数成功时返回零，因指定了无效标志而失败时返回 `EINVAL`。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnp(3)

## 标准

`posix_spawnattr_getflags` 和 `posix_spawnattr_setflags` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_spawnattr_getflags` 和 `posix_spawnattr_setflags` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
