# posix_spawnattr_init(3)

`posix_spawnattr_init` — 初始化和销毁 spawn 属性对象

## 名称

`posix_spawnattr_init`, `posix_spawnattr_destroy`

## 库

Lb libc

## 概要

```c
#include <spawn.h>

int
posix_spawnattr_init(posix_spawnattr_t * attr);

int
posix_spawnattr_destroy(posix_spawnattr_t * attr);
```

## 描述

`posix_spawnattr_init()` 函数以实现所使用的各个属性的默认值初始化 spawn 属性对象 `attr`。对一个已经初始化过的 spawn 属性对象再次进行初始化可能导致内存泄漏。

`posix_spawnattr_destroy()` 函数销毁一个 spawn 属性对象。已销毁的 `attr` 属性对象可以使用 `posix_spawnattr_init()` 重新初始化。该对象在被销毁后不应再被使用。

spawn 属性对象的类型为 `posix_spawnattr_t`（定义于 `<spawn.h>`），用于指定跨 spawn 操作的进程属性继承关系。

生成的 spawn 属性对象（可能已通过设置各个属性值进行了修改），用于修改 `posix_spawn()` 或 `posix_spawnp()` 的行为。在一个 spawn 属性对象被用于通过调用 `posix_spawn()` 或 `posix_spawnp()` 派生进程之后，任何影响该属性对象的函数（包括销毁操作）都不会影响以这种方式派生的任何进程。

## 返回值

若成功完成， `posix_spawnattr_init()` 和 `posix_spawnattr_destroy()` 返回零；否则，返回一个错误号以指示错误。

## 错误

`posix_spawnattr_init()` 函数在以下情况下会失败：

**`[ENOMEM]`** 内存不足，无法初始化 spawn 属性对象。

## 参见

[posix_spawn(3)](posix_spawn.3.md), posix_spawnp(3)

## 标准

`posix_spawnattr_init()` 和 `posix_spawnattr_destroy()` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`posix_spawnattr_init()` 和 `posix_spawnattr_destroy()` 函数首次出现在 FreeBSD 8.0。

## 作者

Ed Schouten <ed@FreeBSD.org>
