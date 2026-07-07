# posix_spawn_file_actions_init(3)

`posix_spawn_file_actions_init` — 初始化和销毁 spawn 文件操作对象

## 名称

`posix_spawn_file_actions_init`, `posix_spawn_file_actions_destroy`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawn_file_actions_init(posix_spawn_file_actions_t * file_actions);

int
posix_spawn_file_actions_destroy(posix_spawn_file_actions_t * file_actions);
```

## 描述

`posix_spawn_file_actions_init()` 函数初始化 `file_actions` 所引用的对象，使其不包含任何用于 `posix_spawn()` 或 `posix_spawnp()` 的文件操作。对一个已经初始化过的 spawn 文件操作对象再次进行初始化可能导致内存泄漏。

`posix_spawn_file_actions_destroy()` 函数销毁 `file_actions` 所引用的对象；该对象实际上变为未初始化状态。已销毁的 spawn 文件操作对象可以使用 `posix_spawn_file_actions_init()` 重新初始化。该对象在被销毁后不应再被使用。

## 返回值

若成功完成，这些函数返回零；否则，返回一个错误号以指示错误。

## 错误

`posix_spawn_file_actions_init()` 函数在以下情况下会失败：

**`[ENOMEM]`** 内存不足，无法初始化 spawn 文件操作对象。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawn_file_actions_addclose(3), posix_spawn_file_actions_addclosefrom_np(3), posix_spawn_file_actions_adddup2(3), [posix_spawn_file_actions_addopen(3)](posix_spawn_file_actions_addopen.3.md), posix_spawnp(3)

## 标准

`posix_spawn_file_actions_init()` 和 `posix_spawn_file_actions_destroy()` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`posix_spawn_file_actions_init()` 和 `posix_spawn_file_actions_destroy()` 函数首次出现在 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
