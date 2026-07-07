# sigaltstack(2)

`sigaltstack` — 设置和/或获取信号栈上下文

## 名称

`sigaltstack`

## 库

Lb libc

## 概要

```c
#include <signal.h>

typedef struct {
        char    *ss_sp;
        size_t  ss_size;
        int     ss_flags;
} stack_t;

int
sigaltstack(const stack_t * restrict ss, stack_t * restrict oss);
```

## 描述

`sigaltstack()` 系统调用允许为当前线程定义一个备用栈，在该栈上处理信号。如果 `ss` 非零，它指定了一个指向*信号栈*（signal stack）的指针及其大小，用于传递信号。当一个信号的动作表明其处理程序应在信号栈上执行（通过 [sigaction(2)](sigaction.2.md) 系统调用指定）时，系统会检查该线程当前是否正在该栈上执行。如果线程当前未在信号栈上执行，系统会安排在信号处理程序执行期间切换到信号栈。

活动的栈无法被修改。

如果在 `ss_flags` 中设置了 `SS_DISABLE`，`ss_sp` 和 `ss_size` 将被忽略，信号栈将被禁用。被禁用的栈将导致所有信号都在常规用户栈上处理。如果随后重新启用该栈，所有指定在备用栈上处理的信号将恢复在备用栈上处理。

如果 `oss` 非零，将返回当前信号栈的状态。`ss_flags` 字段将包含 `SS_ONSTACK`（如果线程当前在信号栈上）或 `SS_DISABLE`（如果信号栈当前被禁用）。

## 注释

`SIGSTKSZ` 的值定义为分配备用栈区域时用于覆盖通常情况所需的字节数/字符数。以下代码片段通常用于分配备用栈。

```c
if ((sigstk.ss_sp = malloc(SIGSTKSZ)) == NULL)
	/* 错误返回 */
sigstk.ss_size = SIGSTKSZ;
sigstk.ss_flags = 0;
if (sigaltstack(&sigstk, NULL) < 0)
	perror("sigaltstack");
```

对于信号处理程序需要特定数量栈空间（而非默认大小）的程序，提供了另一种方法。`MINSIGSTKSZ` 的值定义为操作系统实现备用栈功能所需的字节数/字符数。在计算备用栈大小时，程序应将其栈需求加上 `MINSIGSTKSZ`，以补偿操作系统的开销。

信号栈会根据栈增长方向和对齐要求自动调整。信号栈可能受硬件保护，也可能不受保护，并且不会像常规栈那样自动“增长”。如果栈溢出且此空间未受保护，可能会产生不可预测的结果。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果发生以下情况之一，`sigaltstack()` 系统调用将失败，且信号栈上下文保持不变。

**[`EFAULT`]** `ss` 或 `oss` 指向的内存不是进程地址空间的有效部分。

**[`EPERM`]** 试图修改活动的栈。

**[`EINVAL`]** `ss_flags` 字段无效。

**[`ENOMEM`]** 备用栈区域的大小小于或等于 `MINSIGSTKSZ`。

## 参见

[sigaction(2)](sigaction.2.md), [setjmp(3)](../gen/setjmp.3.md)

## 历史

`sigaltstack()` 的前身，即 `sigstack()` 系统调用，出现于 4.2BSD。
