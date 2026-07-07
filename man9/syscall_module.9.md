# SYSCALL_MODULE(9)

`SYSCALL_MODULE` — 系统调用内核模块声明宏

## 名称

`SYSCALL_MODULE`

## 概要

```c
#include <sys/param.h>
#include <sys/kernel.h>
#include <sys/proc.h>
#include <sys/module.h>
#include <sys/sysent.h>

SYSCALL_MODULE(name, int *offset, struct sysent *new_sysent,
    modeventhand_t evh, void *arg)
```

## 描述

`SYSCALL_MODULE` 宏声明一个新的系统调用。`SYSCALL_MODULE` 展开为一个名为 `sys/` + `name` 的内核模块声明。

此宏所需的其他参数为：

```c
#include <sys/sysent.h>
```

**`offset`** 指向一个 `int` 的指针，用于保存在 `struct sysent` 中分配该系统调用的偏移量。如果 `offset` 所指向的位置持有非 0 值，则尽可能使用该值。如果持有 0，则分配一个新值。

**`new_sysent`** 是一个指向结构的指针，该结构指定实现系统调用的函数以及该函数所需的参数数量（参见

**`evh`** 指向内核模块事件处理程序函数的指针，带有参数 `arg`。更多信息请参见 [module(9)](module.9.md)。

**`arg`** 调用 `evh` 事件处理程序的回调函数时传递的参数。

分配给模块的系统调用号可以使用 modstat(2) 和 modfind(2) 系统调用获取。宏 `SYSCALL_MODULE_HELPER` 包含了 `SYSCALL_MODULE` 及其大部分样板代码。

## 实例

系统调用模块的最小示例可在 **`/usr/share/examples/kld/syscall/module/syscall.c`** 中找到。

## 参见

[module(9)](module.9.md), **`/usr/share/examples/kld/syscall/module/syscall.c`**

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
