# cpu_machdep(9)

`cpu_machdep` — 处理 CPU 和线程状态的机器相关接口

## 名称

`cpu_machdep`, `cpu_copy_thread`, `cpu_exec_vmspace_reuse`, `cpu_exit`, `cpu_fetch_syscall_args`, `cpu_fork`, `cpu_fork_kthread_handler`, `cpu_idle`, `cpu_idle_wakeup`, `cpu_procctl`, `cpu_set_syscall_retval`, `cpu_set_upcall`, `cpu_set_user_tls`, `cpu_switch`, `cpu_sync_core`, `cpu_thread_alloc`, `cpu_thread_clean`, `cpu_thread_exit`, `cpu_thread_free`, `cpu_thread_new_kstack`, `cpu_throw`, `cpu_update_pcb`

## 概要

```c
#include <sys/proc.h>
#include <sys/ptrace.h>

void
cpu_copy_thread(struct thread *td, struct thread *td0)

bool
cpu_exec_vmspace_reuse(struct proc *p, struct vm_map *map)

void
cpu_exit(struct thread *td)

int
cpu_fetch_syscall_args(struct thread *td)

void
cpu_fork(struct thread *td1, struct proc *p2, struct thread *td2,
    int flags)

void
cpu_fork_kthread_handler(struct thread *td, void (*func)(void *),
    void *arg)

void
cpu_idle(int busy)

int
cpu_idle_wakeup(int cpu)

int
cpu_procctl(struct thread *td, int idtype, id_t id, int com,
    void *data)

int
cpu_ptrace(struct thread *_td, int req, void *addr, int data)

void
cpu_set_syscall_retval(struct thread *td, int error)

int
cpu_set_upcall(struct thread *td, void (*entry)(void *), void *arg,
    stack_t *stack)

int
cpu_set_user_tls(struct thread *td, void *tls_base, int thr_flags)

void
cpu_switch(struct thread *old, struct thread *new, struct mtx *mtx)

void
cpu_sync_core(void)

void
cpu_thread_alloc(struct thread *td)

void
cpu_thread_clean(struct thread *td)

void
cpu_thread_exit(struct thread *td)

void
cpu_thread_free(struct thread *td)

void
cpu_thread_new_kstack(struct thread *td)

void
cpu_throw(struct thread *old, struct thread *new)

void
cpu_update_pcb(struct thread *td)
```

## 描述

这些函数提供机器无关抽象的架构相关实现。

`cpu_exec_vmspace_reuse` 在 [execve(2)](../sys/execve.2.md) 期间，如果 `exec_new_vmspace` 可以为进程 `p` 重用现有的 `struct vmspace`（`map`），则返回 true。仅当 `map` 未与任何其他消费者共享时才调用此函数。如果返回 false，`exec_new_vmspace` 将创建新的 `struct vmspace`。

`cpu_exit` 在进程退出期间释放包含 `td` 的进程的地址空间以外的机器相关资源。

`cpu_fork` 从现有进程中的分叉线程 `td1` 复制并更新机器相关状态（例如 pcb 和用户寄存器）到新进程 `p2` 中的新线程 `td2`。此函数必须设置新线程的内核栈和 pcb，以便 `td2` 在开始执行时调用 `fork_exit`，传递指向 `fork_return` 的指针作为 `callout` 参数，`td2` 作为 `arg` 参数。

`cpu_fork_kthread_handler` 调整新线程的初始 pcb 和/或内核栈，以将 `func` 和 `arg` 作为 `callout` 和 `arg` 参数传递给 `fork_exit`。这必须在新线程被调度运行之前调用，用于设置内核线程的“main”函数。

`cpu_copy_thread` 在同一进程中创建新线程时，从 `td` 复制机器相关状态（例如 pcb 和用户寄存器）到 `td0`。此函数必须设置新线程的内核栈和 pcb，以便 `td0` 在开始执行时调用 `fork_exit`，传递指向 `fork_return` 的指针作为 `callout` 参数，`td0` 作为 `arg` 参数。

`cpu_set_upcall` 更新新线程的初始用户寄存器状态，以使用 `stack` 中描述的用户栈调用 `entry`，`arg` 作为唯一参数。

`cpu_set_user_tls` 设置新线程的初始用户线程指针寄存器以引用用户 TLS 基指针 `tls_base`。`thr_flags` 参数提供标志位，来自 [thr_new(2)](../sys/thr_new.2.md) 系统调用的 `struct thr_param` 参数的 `flags` 成员的同一命名空间。

`cpu_update_pcb` 用当前用户寄存器值更新当前线程的 pcb。这在核心转储中写出寄存器注释之前调用。此函数通常只需更新当前线程在上下文切换期间保存在 pcb 中（而非内核进入时的陷阱帧中）的用户寄存器。

注意，当使用 `cpu_update_pcb` 时，进程中除当前线程外的线程被停止，通常通过 `thread_single`。这些已停止线程的 pcb 应已由 `cpu_switch` 更新。

`cpu_fetch_syscall_args` 从当前线程的用户寄存器状态和/或用户栈获取本机 FreeBSD ABI 的当前系统调用参数。参数保存在 `td` 的 `td_sa` 成员中。

`cpu_set_syscall_retval` 更新 `td` 的用户寄存器状态以存储系统调用错误和返回值。如果 `error` 为 0，指示成功并返回 `td_retval` 中的两个值。如果 `error` 为 `ERESTART`，调整用户 PC 以在返回用户模式后重新调用当前系统调用。如果 `error` 为 `EJUSTRETURN`，保持当前用户寄存器状态不变。对于 `error` 的任何其他值，指示错误并返回 `error` 作为错误代码。

`cpu_idle` 等待当前 CPU 上发生下一个中断。如果架构支持低功耗空闲，此函数应在等待时将 CPU 置于低功耗状态。`busy` 是来自调度器的提示。如果 `busy` 非零，调度器预期短睡眠，因此 CPU 应优先考虑低延迟而非最大节能。如果 `busy` 为零，CPU 应最大化节能，包括通过 `cpu_idleclock` 推迟不必要的时钟中断。

`cpu_idle_wakeup` 将 ID 为 `cpu` 的空闲 CPU 从低功耗状态唤醒。

`cpu_procctl` 处理任何机器相关的 [procctl(2)](../sys/procctl.2.md) 请求。

`cpu_ptrace` 处理任何机器相关的 [ptrace(2)](../sys/ptrace.2.md) 请求。

`cpu_switch` 通过交换寄存器状态在当前 CPU 上的线程之间切换。此函数将当前 CPU 寄存器状态保存在 `old` 的 pcb 中，并在返回前从 `new` 的 pcb 加载寄存器值。虽然 pcb 通常包含调用者保存的内核寄存器状态，但它也可包含未保存在陷阱帧中的用户寄存器。

保存 `old` 的当前 CPU 寄存器状态后，`cpu_switch` 将 `mtx` 存储在 `old` 的 `td_lock` 成员中，转移旧线程的所有权。在该存储之后不能访问属于 `old` 的任何数据。特别是，在此点之后不得访问旧线程的内核栈。

当使用 `SCHED_ULE` 时，此函数必须（通过自旋）等待 `new` 的 `td_lock` 成员变为不等于 `&blocked_lock` 的值，然后才能从 `new` 加载寄存器值或访问其内核栈。

从调用者的角度，`cpu_switch` 在未来 `old` 被重新调度时返回，可能在不同 CPU 上。但是，`cpu_switch` 的实现在同一 CPU 上立即返回到 `new` 先前保存的上下文。

`cpu_throw` 类似于 `cpu_switch`，但不为 `old` 保存任何状态或写入旧线程的 `td_lock` 成员。

`cpu_sync_core` 确保当前 CPU 上所有可能的推测和乱序执行被串行化。注意，这是从 IPI 处理程序调用的，因此只需处理 IPI 处理所提供的之外的附加串行化。

### 线程对象生命周期

这些函数支持与线程对象生命周期相关的机器相关线程状态管理。

一般模型是每次通过 [fork(2)](../sys/fork.2.md) 或 [thr_new(2)](../sys/thr_new.2.md) 等系统调用创建新内核线程，或通过 [kproc_create(9)](kproc.9.md)、kproc_kthread_add(9) 或 [kthread_add(9)](kthread.9.md) 创建仅内核线程时，都会分配一个线程对象。当内核线程退出时，线程对象被释放。但是，有一个特殊情况支持每个空闲进程对象缓存一个线程对象的优化。当进程退出时，最后一个线程对象不被释放，而是保持附加到进程。当进程对象稍后在 [fork(2)](../sys/fork.2.md) 中为新进程重用时，内核回收该最后线程对象并将其用作新进程中的初始线程。当线程被回收时，如果现有内核栈不适合新进程，可能会分配新的内核栈。

`cpu_thread_alloc` 在分配新线程对象时初始化 `td` 中的机器相关字段。

`cpu_thread_new_kstack` 在分配新内核栈后初始化 `td` 中与内核栈相关的机器相关字段。此函数通常设置 `td_pcb`（在将 pcb 存储在内核栈中的架构上）和初始 `td_frame` 指针。`cpu_thread_new_kstack` 在分配新线程对象和回收线程分配新内核栈时都被调用。注意，如果回收线程重用其现有内核栈，则*不*调用此函数。

`cpu_thread_clean` 在 [wait(2)](../sys/wait.2.md) 期间释放进程中最后一个线程的机器相关资源。由于该线程是回收候选，机器相关字段应重置为作为新线程运行，以防它被未来的 [fork(2)](../sys/fork.2.md) 回收。特别是，如果线程重用其现有内核栈，则在线程被重用为新进程的主线程之前不会调用其他 `cpu_thread_*` 函数。

`cpu_thread_exit` 在 `td` 退出时清理任何机器相关状态。这由退出的线程调用，因此不能释放内核内执行期间所需的状态。

`cpu_thread_free` 在 `td` 被释放时释放任何机器相关状态。这对进程中除最后一个线程外的任何线程在完成执行后被调用。

## 参见

[fork(2)](../sys/fork.2.md), [procctl(2)](../sys/procctl.2.md), [ptrace(2)](../sys/ptrace.2.md), [thr_new(2)](../sys/thr_new.2.md), [wait(2)](../sys/wait.2.md), [kproc_create(9)](kproc.9.md), kproc_kthread_add(9), [kthread_add(9)](kthread.9.md), [mi_switch(9)](mi_switch.9.md)

## 作者

本手册页由 SRI International、剑桥大学计算机实验室（计算机科学与技术系）和 Capabilities Limited 在合同（FA8750-24-C-B047）（“DEC”）下开发。
