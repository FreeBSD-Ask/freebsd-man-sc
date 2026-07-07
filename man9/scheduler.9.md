# scheduler(9)

`curpriority_cmp` — 对可运行进程执行轮转调度

## 名称

`curpriority_cmp`, `maybe_resched`, `resetpriority`, `roundrobin`, `roundrobin_interval`, `sched_setup`, `schedclock`, `schedcpu`, `setrunnable`, `updatepri`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
int
curpriority_cmp(struct proc *p)

void
maybe_resched(struct thread *td)

void
propagate_priority(struct proc *p)

void
resetpriority(struct ksegrp *kg)

void
roundrobin(void *arg)

int
roundrobin_interval(void)

void
sched_setup(void *dummy)

void
schedclock(struct thread *td)

void
schedcpu(void *arg)

void
setrunnable(struct thread *td)

void
updatepri(struct thread *td)
```

## 描述

每个进程在 `struct proc` 中存储三个不同的优先级：`p_usrpri`、`p_nativepri` 和 `p_priority`。

`p_usrpri` 成员是根据进程估计的 CPU 时间和 nice 级别计算的进程用户优先级。

`p_nativepri` 成员是 `propagate_priority` 使用的保存优先级。当进程获取互斥锁时，其优先级保存在 `p_nativepri` 中。当它持有互斥锁时，进程的优先级可能被另一个在该互斥锁上阻塞的进程提升。当进程释放互斥锁时，其优先级恢复为保存在 `p_nativepri` 中的优先级。

`p_priority` 成员是进程的实际优先级，用于确定它在哪个 [runqueue(9)](runqueue.9.md) 上运行等。

`curpriority_cmp` 函数将当前运行进程的缓存优先级与进程 `p` 进行比较。如果当前运行进程的优先级更高，则返回小于零的值。如果当前进程的优先级更低，则返回大于零的值。如果当前进程与 `p` 具有相同优先级，则 `curpriority_cmp` 返回零。当前运行进程的缓存优先级在进程从 tsleep(9) 恢复或在 `userret` 中返回用户态时更新，并存储在私有变量 `curpriority` 中。

`maybe_resched` 函数比较当前线程和 `td` 的优先级。如果 `td` 的优先级高于当前线程，则需要上下文切换，并设置 `KEF_NEEDRESCHED`。

`propagate_priority` 查看拥有 `p` 所阻塞的互斥锁的进程。如果需要，该进程的优先级将提升到 `p` 的优先级。如果该进程当前正在运行，则函数返回。如果该进程在 [runqueue(9)](runqueue.9.md) 上，则该进程被移至其新优先级的相应 [runqueue(9)](runqueue.9.md)。如果该进程在互斥锁上阻塞，则其在所讨论互斥锁上阻塞的进程列表中的位置将更新以反映其新优先级。然后，函数使用刚刚遇到的互斥锁的拥有者进程重复该过程。注意，进程的优先级仅提升到原始进程 `p` 的优先级，而不是先前遇到的进程的优先级。

`resetpriority` 函数重新计算 ksegrp `kg` 的用户优先级（存储在 `kg_user_pri` 中），并在需要时调用 `maybe_resched` 强制重新调度该组中的每个线程。

`roundrobin` 函数用作 timeout(9) 函数，以每 `sched_quantum` 个 tick 强制重新调度。

`roundrobin_interval` 函数仅返回由 `roundrobin` 触发的重新调度之间的时钟 tick 数。因此，它所做的就是返回 `sched_quantum` 的当前值。

`sched_setup` 函数是一个 [SYSINIT(9)](sysinit.9.md)，被调用来启动 callout 驱动的调度器函数。它只是首次调用 `roundrobin` 和 `schedcpu` 函数。初始调用后，这两个函数将在各自函数完成时再次注册其 callout 事件来传播自身。

`schedclock` 函数由 `statclock` 调用以调整当前运行线程的 ksegrp 的优先级。它更新该组的估计 CPU 时间，然后通过 `resetpriority` 调整优先级。

`schedcpu` 函数更新所有进程优先级。首先，它更新跟踪进程在各种进程状态中停留时间的统计信息。其次，它更新当前进程的估计 CPU 时间，使得在 5 \* 负载平均值秒内遗忘约 90% 的 CPU 使用。例如，如果负载平均值为 2.00，则进程估计 CPU 时间的至少 90% 应基于该进程在过去 10 秒内的 CPU 时间。然后它重新计算进程的优先级，并在必要时将其移至相应的 [runqueue(9)](runqueue.9.md)。第三，它更新 [ps(1)](../man1/ps.1.md) 和 [top(1)](../man1/top.1.md) 等实用程序使用的 %CPU 估计，使得在 60 秒内遗忘 95% 的 CPU 使用。一旦所有进程优先级都更新完毕，`schedcpu` 调用 `vmmeter` 更新包括负载平均值在内的各种其他统计信息。最后，它安排自己在 `hz` 个时钟 tick 后再次运行。

`setrunnable` 函数用于将进程的状态更改为可运行。如果需要，将进程放置在 [runqueue(9)](runqueue.9.md) 上，并唤醒 swapper 进程告知其如果进程被换出则换入该进程。如果进程已休眠至少一次 `schedcpu` 运行，则使用 `updatepri` 调整进程的优先级。

`updatepri` 函数用于调整已休眠进程的优先级。它为进程休眠期间的每个 `schedcpu` 事件追溯衰减进程的估计 CPU 时间。最后，它调用 `resetpriority` 调整进程的优先级。

## 参见

[mi_switch(9)](mi_switch.9.md), [runqueue(9)](runqueue.9.md), [sleepqueue(9)](sleepqueue.9.md), [tsleep(9)](sleep.9.md)

## 缺陷

`curpriority` 变量确实应该是每 CPU 的。此外，`maybe_resched` 应将 `chk` 的优先级与每个 CPU 的优先级进行比较，然后向优先级最低的处理器发送 IPI 以在需要时触发重新调度。

优先级传播已损坏，因此默认禁用。`p_nativepri` 变量仅在进程第一次尝试未获取休眠互斥锁时更新。此外，如果进程以这种方式获取多个休眠互斥锁，并且在此之间优先级被提升，则 `p_nativepri` 将被覆盖。
