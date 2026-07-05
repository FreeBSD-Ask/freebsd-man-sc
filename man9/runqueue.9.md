# runqueue.9

`choosethread` — 管理可运行进程队列

## 名称

`choosethread`, `procrunnable`, `remrunqueue`, `setrunqueue`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
extern struct rq itqueues[];
extern struct rq rtqueues[];
extern struct rq queues[];
extern struct rq idqueues[];

struct thread *
choosethread(void)

int
procrunnable(void)

void
remrunqueue(struct thread *td)

void
setrunqueue(struct thread *td)
```

## 描述

运行队列由四个优先级队列组成：用于中断线程的 `itqueues`、用于实时优先级进程的 `rtqueues`、用于分时进程的 `queues`，以及用于空闲优先级进程的 `idqueues`。每个优先级队列由 `NQS` 个队列头结构的数组组成。每个队列头标识一个具有相同优先级的可运行进程列表。每个队列还有一个单字，包含标识非空队列的位掩码，以协助快速选择进程。它们分别命名为 `itqueuebits`、`rtqueuebits`、`queuebits` 和 `idqueuebits`。运行队列受 `sched_lock` 互斥锁保护。

`procrunnable` 在除空闲进程外没有其他可运行进程时返回零。如果除空闲进程外至少有一个可运行进程，则返回非零值。注意，调用此函数时*不需要*持有 `sched_lock` 互斥锁。存在一个小的竞争窗口，当一个 CPU 在当前没有其他可运行进程时将进程放入运行队列，而另一个 CPU 正在调用此函数时。在这种情况下，第二个 CPU 将在注意到有可运行进程之前，在空闲循环中多走一次。这之所以可行，是因为 SMP 系统中空闲 CPU 不会被停机。如果 SMP 系统中空闲 CPU 被停机，则此竞争条件在失败情况下可能会有更严重的后果，`procrunnable` 可能必须要求获取 `sched_lock` 互斥锁。

`choosethread` 返回最高优先级的可运行线程。如果没有可运行线程，则返回空闲线程。此函数由 `cpu_switch` 和 `cpu_throw` 调用以确定切换到哪个线程。必须在持有 `sched_lock` 互斥锁时调用 `choosethread`。

`setrunqueue` 将线程 `td` 添加到适当优先级队列中相应队列的尾部。该线程必须是可运行的，即 `p_stat` 必须设置为 `SRUN`。必须在持有 `sched_lock` 互斥锁时调用此函数。

`remrunqueue` 从其运行队列中移除线程 `td`。如果 `td` 不在运行队列上，内核将 [panic(9)](panic.9.md)。必须在持有 `sched_lock` 互斥锁时调用此函数。

## 参见

[cpu_switch(9)](mi_switch.9.md), [scheduler(9)](scheduler.9.md), [sleepqueue(9)](sleepqueue.9.md)
