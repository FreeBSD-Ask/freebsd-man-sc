# ucontext(3)

`ucontext` — 用户线程上下文

## 名称

`ucontext`

## 库

Lb libc

## 概要

`#include <ucontext.h>`

## 描述

`ucontext_t` 类型是一个结构类型，适合保存用户执行线程的上下文。线程的上下文包括其栈、保存的寄存器和被阻塞的信号列表。

`ucontext_t` 结构至少包含以下字段：

**`ucontext_t *uc_link`** 此上下文返回时接管的上下文

**`sigset_t uc_sigmask`** 被阻塞的信号

**`stack_t uc_stack`** 栈区域

**`mcontext_t uc_mcontext`** 保存的寄存器

`uc_link` 字段指向此上下文的入口点函数返回时要恢复的上下文。如果 `uc_link` 等于 `NULL`，则此上下文返回时进程退出。

`uc_mcontext` 字段是机器相关的，可移植应用程序应将其视为不透明。

以下函数用于操作 `ucontext_t` 结构：

- `Ft int Fn getcontext ucontext_t *` ;
- `Ft ucontext_t * Fn getcontextx void` ;
- `Ft int Fn setcontext const ucontext_t *` ;
- `Ft void Fn makecontext ucontext_t * void *void int ...` ;
- `Ft int Fn swapcontext ucontext_t * const ucontext_t *` ;

## 参见

[sigaltstack(2)](../man2/sigaltstack.2.md), [getcontext(3)](getcontext.3.md), getcontextx(3), [makecontext(3)](makecontext.3.md)

## 标准

`ucontext_t` 类型遵循 -xsh5 和 IEEE Std 1003.1-2001 ("POSIX.1") 标准。IEEE Std 1003.1-2008 ("POSIX.1") 修订版从规范中移除了 `ucontext_t`。
