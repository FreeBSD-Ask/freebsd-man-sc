# sigfastblock(2)

`sigfastblock` — 通过简单的内存写入控制信号阻塞

## 名称

`sigfastblock`

## 库

Lb libc

## 概要

`#include <sys/signalvar.h>`

```c
int
sigfastblock(int cmd, void *ptr);
```

## 描述

此函数不打算由应用程序直接使用。该功能用于在 ld-elf.so.1(8) 和 Lb libthr 中实现某些优化。

该函数配置内核机制，允许线程通过对用户空间内存的单次写入来阻塞异步信号传递，避免 [sigprocmask(2)](sigprocmask.2.md) 等系统调用为建立临界区而产生的开销。C 运行时使用它来优化 async-signal-safe 功能的实现。

线程可将一个 `int` 类型的 `sigblock` 变量注册为一个位置，内核在计算异步信号传递的阻塞信号掩码时会查询该位置。如果该变量指示请求阻塞，则内核实际上像向 [sigprocmask(2)](sigprocmask.2.md) 提供了包含所有可阻塞信号的掩码一样运作。

该变量只能由所属线程修改，当传递信号时无法保证从其他线程到内核的更新可见性。

sigblock 变量的低位保留作为标志，内核可能在任意时刻设置或清除这些标志。用户空间代码应使用 [atomic(9)](../man9/atomic.9.md) 操作，以 `SIGFASTBLOCK_INC` 量递增和递减来递归阻塞或解除阻塞信号传递。

如果在未掩蔽时本应传递信号，内核可能在 sigblock 变量中设置 `SIGFASTBLOCK_PEND` “pending signal”（待决信号）标志。用户空间在清除该变量时，如果注意到待决信号位被设置，应执行 `SIGFASTBLOCK_UNBLOCK` 操作，这将立即传递待决信号。否则，信号传递可能被推迟。

`cmd` 参数指定以下操作之一：

**`SIGFASTBLOCK_SETPTR`** 将 `ptr` 参数所指向位置的 `int` 类型变量注册为调用线程的 sigblock 变量。

**`SIGFASTBLOCK_UNSETPTR`** 注销当前注册的 sigblock 位置。内核停止从其阻塞计数的非零值推断阻塞掩码。可在前一个注销后注册新位置。

**`SIGFASTBLOCK_UNBLOCK`** 如果有应传递给调用线程的待决信号，这些信号在从调用返回之前被传递。sigblock 变量应具有零阻塞计数，并指示存在待决信号。这实际上意味着该变量的值应为 `SIGFASTBLOCK_PEND`。

## 返回值

成功完成后返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

操作可能因以下错误失败：

**[`EBUSY`]** 在 sigblock 地址已注册时尝试 `SIGFASTBLOCK_SETPTR`。在 sigblock 变量值不等于 `SIGFASTBLOCK_PEND` 时调用 `SIGFASTBLOCK_UNBLOCK`。

**[`EINVAL`]** 传递给 `SIGFASTBLOCK_SETPTR` 的变量地址未自然对齐。在没有先前成功调用 `SIGFASTBLOCK_SETPTR` 的情况下尝试 `SIGFASTBLOCK_UNSETPTR` 操作。

**[`EFAULT`]** 尝试读取或写入 sigblock 变量失败。注意，如果在系统调用入口的隐式访问期间尝试从 sigblock 变量读取时发生故障，内核会生成 `SIGSEGV` 信号。

## 参见

[kill(2)](kill.2.md), signal(2), [sigprocmask(2)](sigprocmask.2.md), libthr(3), ld-elf.so.1(8)

## 标准

`sigfastblock` 函数是非标准的，尽管类似的功能是其他多个系统提供的常见优化。

## 历史

`sigfastblock` 函数引入于 FreeBSD 13.0。

## 缺陷

`sigfastblock` 符号目前有意不从 libc 导出。使用者应使用私有 libc 命名空间的 `__sys_fast_sigblock` 符号，或使用 [syscall(2)](syscall.2.md)。
