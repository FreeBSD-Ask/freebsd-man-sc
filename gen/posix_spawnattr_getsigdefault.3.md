# posix_spawnattr_getsigdefault(3)

`posix_spawnattr_getsigdefault` — 获取和设置 spawn 属性对象的 spawn-sigdefault 属性

## 名称

`posix_spawnattr_getsigdefault`, `posix_spawnattr_setsigdefault`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getsigdefault(const posix_spawnattr_t *restrict attr,
    sigset_t *restrict sigdefault);

int
posix_spawnattr_setsigdefault(posix_spawnattr_t *attr,
    const sigset_t *restrict sigdefault);
```

## 描述

`posix_spawnattr_getsigdefault` 函数从 `attr` 所引用的属性对象中获取 spawn-sigdefault 属性的值。

`posix_spawnattr_setsigdefault` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-sigdefault 属性。

spawn-sigdefault 属性表示在 spawn 操作中，新进程镜像中被强制采用默认信号处理的信号集合（如果在 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSIGDEF`）。该属性的默认值为空信号集。

## 返回值

`posix_spawnattr_getsigdefault` 和 `posix_spawnattr_setsigdefault` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_getsigmask(3)](posix_spawnattr_getsigmask.3.md), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnattr_setsigmask(3), posix_spawnp(3)

## 标准

`posix_spawnattr_getsigdefault` 和 `posix_spawnattr_setsigdefault` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_spawnattr_getsigdefault` 和 `posix_spawnattr_setsigdefault` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
