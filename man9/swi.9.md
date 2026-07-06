# swi.9

`swi_add` — 注册和调度软件中断处理程序

## 名称

`swi_add`, `swi_remove`, `swi_sched`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <sys/interrupt.h>

extern struct intr_event *clk_intr_event;

int
swi_add(struct intr_event **eventp, const char *name,
    driver_intr_t handler, void *arg, int pri, enum intr_type flags,
    void **cookiep)

int
swi_remove(void *cookie)

void
swi_sched(void *cookie, int flags)
```

## 描述

这些函数用于注册和调度软件中断处理程序。软件中断处理程序附加到软件中断线程，就像硬件中断处理程序附加到硬件中断线程一样。多个处理程序可以附加到同一线程。软件中断处理程序可用于在硬件中断处理程序内排队较不关键的处理，以便稍后完成工作。软件中断线程与其他内核线程不同之处在于它们被视为中断线程。这意味着执行这些线程所花费的时间被计为中断时间，并且它们可以通过轻量级上下文切换运行。

`swi_add` 函数用于向指定的中断事件添加新的软件中断处理程序。`eventp` 参数是指向 `struct intr_event` 指针的可选指针。如果此参数指向持有中断处理程序列表的现有事件，则此处理程序将附加到该事件。否则将创建新事件，如果 `eventp` 非 `NULL`，则该地址处的指针将被修改为指向新创建的事件。`name` 参数用于将名称与特定处理程序关联。此名称附加到此处理程序附加到的软件中断线程的名称。`handler` 参数是处理程序被调度运行时将执行的函数。`arg` 参数将在函数执行时作为 `handler` 的唯一参数传递。`pri` 值指定此中断处理程序相对于其他软件中断处理程序的优先级。如果创建了中断事件，则此值用作向量，`flags` 参数用于指定处理程序的属性，如 `INTR_MPSAFE`。`cookiep` 参数指向 `void *` cookie。此 cookie 将设置为唯一标识此处理程序的值，并用于稍后调度处理程序执行。

`swi_remove` 函数用于拆除由 `cookie` 参数指向的中断处理程序。它将中断处理程序从关联的中断事件分离并释放其内存。

`swi_sched` 函数用于调度中断处理程序及其关联线程运行。`cookie` 参数指定应调度哪个软件中断处理程序运行。`flags` 参数指定处理程序应如何以及何时运行，是以下一个或多个标志的掩码：

**`SWI_DELAY`** 指定内核应将指定处理程序标记为需要运行，但内核不应调度软件中断线程运行。相反，`handler` 将在软件中断线程下次由另一事件调度运行后执行。

**`SWI_FROMNMI`** 指定 `swi_sched` 从 NMI 上下文调用，应谨慎使用 KPI。在允许从 NMI 上下文发送 IPI 的平台上，它通过 IPI 立即唤醒 `clk_intr_event`，否则它的工作方式与 `SWI_DELAY` 相同。

`clk_intr_event` 是指向用于将延迟处理程序挂起到时钟中断的 `struct intr_event` 的指针，由 [hardclock(9)](hardclock.9.md) 直接调用。

## 返回值

`swi_add` 和 `swi_remove` 函数成功时返回零，失败时返回非零。

## 错误

`swi_add` 函数将在以下情况下失败：

`EAGAIN` 将超过系统对执行中进程总数的限制。该限制由 sysctl(3) MIB 变量 `KERN_MAXPROC` 给出。

`EINVAL` `flags` 参数指定了 `INTR_ENTROPY`。

`EINVAL` `eventp` 参数指向硬件中断线程。

`EINVAL` `name` 或 `handler` 参数中任一为 `NULL`。

`EINVAL` 指定了 `INTR_EXCL` 标志且 `eventp` 指向的中断事件已有至少一个处理程序，或中断事件已有独占处理程序。

`swi_remove` 函数将在以下情况下失败：

`EINVAL` `cookie` 指向的软件中断处理程序为 `NULL`。

## 参见

[hardclock(9)](hardclock.9.md), [intr_event(9)](intr_event.9.md), [taskqueue(9)](taskqueue.9.md)

## 历史

`swi_add` 和 `swi_sched` 函数首次出现在 FreeBSD 5.0 中。它们替代了首次出现在 FreeBSD 3.0 中的 `register_swi` 函数以及至少可追溯到 4.4BSD 的 `setsoft*` 和 `schedsoft*` 函数。`swi_remove` 函数首次出现在 FreeBSD 6.1 中。
