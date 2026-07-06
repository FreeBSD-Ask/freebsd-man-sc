# fpu_kern.9

`fpu_kern` — 在内核中使用 FPU 的设施

## 名称

`fpu_kern`

## 概要

```c
#include <machine/fpu.h>

struct fpu_kern_ctx *
fpu_kern_alloc_ctx(u_int flags)

void
fpu_kern_free_ctx(struct fpu_kern_ctx *ctx)

void
fpu_kern_enter(struct thread *td, struct fpu_kern_ctx *ctx, u_int flags)

int
fpu_kern_leave(struct thread *td, struct fpu_kern_ctx *ctx)

int
fpu_kern_thread(u_int flags)

int
is_fpu_kern_thread(u_int flags)
```

## 描述

`fpu_kern` 系列函数允许在内核代码中使用 FPU 硬件。现代 FPU 不仅限于为浮点运算提供硬件实现，还为密码学和其它计算密集型算法提供高级加速器。这些设施与 FPU 硬件共享寄存器。

典型的内核代码不需要访问 FPU。每次进入内核时都保存大型寄存器文件会浪费时间。当内核代码使用 FPU 时，必须保存当前 FPU 状态以避免破坏用户态状态，反之亦然。

保存和恢复的管理是自动的。当非当前上下文尝试访问 FPU 寄存器时，处理器会捕获该访问。需要显式调用来分配保存区域，并通知使用 FPU 的代码的开始和结束。

`fpu_kern_alloc_ctx` 函数分配 `fpu_kern` 用于跟踪 FPU 硬件状态使用及相关软件状态的内存。`fpu_kern_alloc_ctx` 函数需要 `flags` 参数，目前接受以下标志：

**`FPU_KERN_NOWAIT`** 如果无法在不休眠的情况下满足请求，则不等待可用内存。

**`0`** 不需要特殊处理。

该函数返回分配的上下文区域，如果分配失败则返回 `NULL`。

`fpu_kern_free_ctx` 函数释放先前由 `fpu_kern_alloc_ctx` 分配的上下文。

`fpu_kern_enter` 函数指定允许使用 FPU 的内核代码区域的开始。其参数为：

**`FPU_KERN_NORMAL`** 指示调用者打算访问完整的 FPU 状态。目前必须指定。

**`FPU_KERN_KTHR`** 指示如果线程调用了 fpu_kern_thread(9) 函数，则不应保存当前 FPU 状态。这旨在减少可从内核线程和系统调用上下文中使用的调用者的代码重复。`fpu_kern_leave` 函数能正确处理此类上下文。

**`FPU_KERN_NOCTX`** 避免嵌套保存区域。如果指定此标志，`ctx` 必须传递为 `NULL`。该标志仅应用于可在临界区内执行的非常短的代码块。它以增加系统延迟为代价，避免了分配 FPU 上下文的需要。

**`td`** 目前必须为 `curthread`。

**`ctx`** 先前由 `fpu_kern_alloc_ctx` 分配且当前未被另一次 `fpu_kern_enter` 调用使用的上下文保存区域。

**`flags`** 此参数目前接受以下标志：

该函数不休眠或阻塞。它可能在执行期间以及函数返回后的首次 FPU 访问时，以及每次上下文切换后引发 FPU 陷阱。在 i386 和 amd64 上，这将是 `Device` 异常（参见 Intel 软件开发者手册）。

`fpu_kern_leave` 函数结束由 `fpu_kern_enter` 启动的区域。在 `fpu_kern_enter` 之前或 `fpu_kern_leave` 之后在内核中使用 FPU 是错误的。该函数接受 `td` 线程参数（目前必须为 `curthread`）以及先前传递给 `fpu_kern_enter` 的 `ctx` 上下文指针。函数返回后，该上下文可被释放或由另一次 `fpu_kern_enter` 调用重用。该函数始终返回 0。

`fpu_kern_thread` 函数为从不离开到用户态的线程启用优化。当前线程将重用用户态保存区域来保存内核 FPU 状态，而不需要显式分配的上下文。该函数未定义任何标志，也不返回任何错误状态。一旦调用此函数，即无需调用 `fpu_kern_enter` 或 `fpu_kern_leave`，FPU 可在调用线程中使用。

`is_fpu_kern_thread` 函数返回一个布尔值，指示当前线程是否已进入由 `fpu_kern_thread` 启用的模式。该函数目前未定义任何标志，如果当前线程具有永久 FPU 保存区域则返回值为真，否则为假。

## 注释

`Device` 目前仅在 i386、amd64、arm64 和 powerpc 架构上实现。

无法处理从内核态引发的浮点异常。

`Device` 函数的未使用 `flags` 参数将被扩展，以允许指定代码区域使用的 FPU 硬件状态集。这将允许优化保存和恢复状态。

## 作者

`Device` 设施及本手册页由 Konstantin Belousov <kib@FreeBSD.org> 编写。arm64 支持由 Andrew Turner <andrew@FreeBSD.org> 添加。powerpc 支持由 Shawn Anastasio <sanastasio@raptorengineering.com> 添加。

## 缺陷

`fpu_kern_leave` 可能应为 `void` 类型（类似于 `fpu_kern_enter`）。
