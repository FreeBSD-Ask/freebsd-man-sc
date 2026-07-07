# posix_spawnattr_getsigmask(3)

`posix_spawnattr_getsigmask` — 获取和设置 spawn 属性对象的 spawn-sigmask 属性

## 名称

`posix_spawnattr_getsigmask`, `posix_spawnattr_setsigmask`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_getsigmask(const posix_spawnattr_t *restrict attr,
    sigset_t *restrict sigmask);

int
posix_spawnattr_setsigmask(posix_spawnattr_t *attr,
    const sigset_t *restrict sigmask);
```

## 描述

`posix_spawnattr_getsigmask` 函数从 `attr` 所引用的属性对象中获取 spawn-sigmask 属性的值。

`posix_spawnattr_setsigmask` 函数在 `attr` 所引用的已初始化属性对象中设置 spawn-sigmask 属性。

spawn-sigmask 属性表示 spawn 操作中新进程镜像生效的信号掩码（如果在 spawn-flags 属性中设置了 `POSIX_SPAWN_SETSIGMASK`）。该属性的默认值未指定。

## 返回值

`posix_spawnattr_getsigmask` 和 `posix_spawnattr_setsigmask` 函数返回零。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnattr_destroy(3), [posix_spawnattr_getsigmask(3)](posix_spawnattr_getsigmask.3.md), [posix_spawnattr_init(3)](posix_spawnattr_init.3.md), posix_spawnattr_setsigmask(3), posix_spawnp(3)

## 标准

`posix_spawnattr_getsigmask` 和 `posix_spawnattr_setsigmask` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_spawnattr_getsigmask` 和 `posix_spawnattr_setsigmask` 函数首次出现于 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
