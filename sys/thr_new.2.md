# thr_new(2)

`thr_new` — 创建新的执行线程

## 名称

`thr_new`

## 库

Lb libc

## 概要

`#include <sys/thr.h>`

```c
int
thr_new(struct thr_param *param, int param_size);
```

## 描述

此函数旨在实现线程。普通应用程序应改用 [pthread_create(3)](../man3/pthread_create.3.md)。

`thr_new()` 系统调用在当前进程的上下文中创建一个新的内核调度执行线程。新创建的线程与进程中现有的内核调度线程共享进程的所有属性，但具有私有的处理器执行状态。新线程的机器上下文（包括协处理器状态）从创建线程的上下文复制。FPU 状态和特定机器寄存器被排除在复制之外。这些根据 ABI 要求和系统调用参数设置。新线程的 FPU 状态被重新初始化为干净状态。

`param` 结构提供影响线程创建的参数。该结构定义于

`#include <sys/thr.h>`

头文件，如下所示

```c
struct thr_param {
    void          (*start_func)(void *);
    void          *arg;
    char          *stack_base;
    size_t        stack_size;
    char          *tls_base;
    size_t        tls_size;
    long          *child_tid;
    long          *parent_tid;
    int           flags;
    struct rtprio *rtp;
};
```

包含以下字段：

**`THR_SUSPENDED`** 以挂起状态创建新线程。此标志目前未实现。

**`THR_SYSTEM_SCOPE`** 创建系统作用域线程。此标志目前未实现。

**`THR_C_RUNTIME`** 指示新线程由 C 语言运行时创建。它具有架构特定的含义。在 amd64 上，该标志请求在调用信号处理程序之前将指定的 `tls_base` 加载到 `%fsbase` 寄存器中。

**`start_func`** 指向线程入口函数的指针。内核安排新线程在首次返回用户空间时开始执行该函数。

**`arg`** 提供给入口函数的不透明参数。

**`stack_base`** 栈基地址。栈必须由调用者分配。在某些架构上，ABI 可能要求系统在栈上放置信息以确保 `start_func` 的执行环境。

**`stack_size`** 栈大小。

**`tls_base`** TLS 基地址。TLS 基的值被加载到新线程上下文中由 ABI 定义的机器寄存器中。

**`tls_size`** TLS 大小。

**`child_tid`** 用于存储新线程标识符的地址，供子线程使用。

**`parent_tid`** 用于存储新线程标识符的地址，供父线程使用。同时提供 `child_tid` 和 `parent_tid`，意图是 `child_tid` 由新线程用于获取其线程标识符而无需发出 [thr_self(2)](thr_self.2.md) 系统调用，而 `parent_tid` 由线程创建者使用。后者与 `child_tid` 分开，因为新线程可能在父进程有机会执行足够远以访问它之前就退出并释放其线程数据。

**`flags`** 线程创建标志。`flags` 成员可指定以下标志：

**`rtp`** 新线程的实时调度优先级。可为 `NULL` 以从创建线程继承优先级。

`param_size` 参数应设置为 `param` 结构的大小。

首次成功创建额外线程后，进程被内核标记为多线程。特别是，进程的 `p_flag` 中会设置 `P_HADTHREADS` 标志（在 [ps(1)](../man1/ps.1.md) 输出中可见），并且若干操作以多线程模式执行。例如，[execve(2)](execve.2.md) 系统调用在成功执行时终止除调用线程外的所有线程。

## 返回值

如果成功，`thr_new()` 返回零；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`thr_new()` 操作返回以下错误：

**[`EFAULT`]** `param` 参数所指向的内存无效。

**[`EFAULT`]** `param` 结构的 `child_tid`、`parent_tid` 或 `rtp` 参数所指向的内存无效。

**[`EFAULT`]** 指定的栈基地址无效，或内核无法在栈上放置所需的初始数据。

**[`EINVAL`]** `param_size` 参数指定了负值，或该值大于内核可解释的最大 `struct param` 大小。

**[`EINVAL`]** `rtp` 成员不为 `NULL` 且指定了无效的调度参数。

**[`EINVAL`]** 指定的 TLS 基地址无效。

**[`EPERM`]** 调用者没有权限设置调度参数或调度策略。

**[`EPROCLIM`]** 创建新线程将超过 `RACCT_NTHR` 限制，参见 rctl_get_racct(2)。

**[`EPROCLIM`]** 创建新线程将超过 `kern.threads.max_threads_per_proc` [sysctl(3)](../man3/sysctl.3.md) 限制。

**[`ENOMEM`]** 没有足够的内核内存来分配新线程结构。

## 参见

[ps(1)](../man1/ps.1.md), [_umtx_op(2)](_umtx_op.2.md), [execve(2)](execve.2.md), rctl_get_racct(2), [thr_exit(2)](thr_exit.2.md), [thr_kill(2)](thr_kill.2.md), thr_kill2(2), [thr_self(2)](thr_self.2.md), [thr_set_name(2)](thr_set_name.2.md), [pthread_create(3)](../man3/pthread_create.3.md)

## 标准

`thr_new()` 系统调用是非标准的，由 Lb libthr 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") [pthread(3)](../man3/pthread.3.md) 功能。

## 历史

`thr_new()` 系统调用首次出现于 FreeBSD 5.2。
