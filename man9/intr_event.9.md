# intr_event(9)

`intr_event_add_handler` — 内核中断处理程序与线程 API

## 名称

`intr_event_add_handler`, `intr_event_create`, `intr_event_destroy`, `intr_event_handle`, `intr_event_remove_handler`, `intr_priority`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/bus.h>
```

```c
#include <sys/interrupt.h>
```

```c
int
intr_event_add_handler(struct intr_event *ie, const char *name,
    driver_filter_t filter, driver_intr_t handler, void *arg,
    u_char pri, enum intr_type flags, void **cookiep)

int
intr_event_create(struct intr_event **event, void *source, int flags,
    int irq, void (*pre_ithread)(void *),
    void (*post_ithread)(void *), void (*post_filter)(void *),
    int (*assign_cpu)(void *, int), const char *fmt, ...)

int
intr_event_destroy(struct intr_event *ie)

int
intr_event_handle(struct intr_event *ie, struct trapframe *frame)

int
intr_event_remove_handler(void *cookie)

u_char
intr_priority(enum intr_type flags)
```

## 描述

中断事件 API 提供了管理中断处理程序的注册和执行及其关联线程上下文的方法。

系统中的每个中断事件对应一个硬件或软件中断源。每个中断事件维护一个按优先级排序的中断处理程序列表，这些处理程序在处理事件时被调用。一个中断事件通常会（但不总是）有一个关联的 [kthread(9)](kthread.9.md)，称为中断线程。最后，每个事件包含可选的回调函数，这些函数在处理程序函数本身之前和之后被调用。

中断处理程序包含两个不同的处理函数：*filter* 和线程 *handler*。*filter* 函数在中断上下文中运行，旨在执行快速处理，如确认或屏蔽硬件中断，并为随后的线程 *handler* 排队工作。两个函数都是可选的；每个中断处理程序可以选择注册 filter、线程 handler 或两者。每个中断处理程序还包含一个名称、一组标志和一个不透明参数，该参数将传递给 *filter* 和 *handler* 函数。

### 处理程序约束

*filter* 函数在 critical(9) 临界区内执行。因此，filter 不得因任何原因让出 CPU，并且只能使用自旋锁访问共享数据。不允许在 filter 中分配内存。

*handler* 函数从关联的中断内核线程上下文中执行。不允许睡眠，但中断线程可能被更高优先级的线程抢占。因此，线程化处理函数可以获得非可睡眠锁，如 [locking(9)](locking.9.md) 中所述。中断线程中的任何内存或 zone 分配必须指定 `M_NOWAIT` 标志，并且必须处理任何分配错误。

这些约束的例外是软件中断线程，它允许睡眠，但应使用 [swi(9)](swi.9.md) 接口进行分配和调度。

### 函数说明

`intr_event_create` 函数创建一个新的中断事件。`event` 参数指向一个 `struct intr_event` 指针，成功时该指针将引用新创建的事件。`source` 参数是一个不透明指针，将传递给 `pre_ithread`、`post_ithread` 和 `post_filter` 回调。`flags` 参数是此线程属性的掩码。目前 `intr_event_create` 唯一有效的标志是 `IE_SOFT`，用于指定此中断线程是软件中断。`enable` 和 `disable` 参数指定用于启用和禁用此中断线程中断源的可选函数。`irq` 参数是与此事件对应的唯一中断向量号。`pre_ithread`、`post_ithread` 和 `post_filter` 参数是在处理中断时在不同点调用的回调函数。这在下面的处理程序回调一节中有更详细的描述。它们可以为 `NULL` 以指定无回调。`assign_cpu` 参数指向一个回调函数，在将中断绑定到特定 CPU 时被调用。如果不支持绑定，它可以为 `NULL`。其余参数构成 [printf(9)](printf.9.md) 参数列表，用于构建新中断线程的基本名称。中断线程的完整名称由中断线程的基本名称与其所有中断处理程序的名称连接而成。

`intr_event_destroy` 函数通过释放资源来销毁先前创建的中断事件。只有在没有剩余处理程序时才能销毁中断事件。

`intr_event_add_handler` 函数向由 `ie` 指定的现有中断事件添加新处理程序。`name` 参数指定此处理程序的名称。`filter` 参数提供要执行的 filter 函数。`handler` 参数提供要从事件的中断线程执行的处理函数。`arg` 参数在调用时传递给 `filter` 和 `handler` 函数。`pri` 参数指定此处理程序的优先级，对应于以下文件中定义的值：

```c
#include <sys/priority.h>
```

它确定此处理程序相对于此事件的其他处理程序的调用顺序，以及后备内核线程的调度优先级。`flags` 参数可用于指定此处理程序的属性，定义于：

```c
#include <sys/bus.h>
```

如果 `cookiep` 不为 `NULL`，则会被分配一个 cookie，以后可用于删除此处理程序。

`intr_event_handle` 函数是中断处理代码的主入口点。它必须从中断上下文调用。该函数将执行与中断事件 `ie` 关联的所有 filter 处理程序，并调度关联的中断线程运行（如果适用）。`frame` 参数用于传递指向 `struct trapframe` 的指针，该结构包含中断发生时的机器状态。此函数的主体在 critical(9) 临界区内运行。

`intr_event_remove_handler` 函数从由 `ie` 指定的中断事件中移除中断处理程序。`cookie` 参数（从 `intr_event_add_handler` 获得）标识要移除的处理程序。

`intr_priority` 函数将 `INTR_TYPE_*` 中断标志转换为中断线程调度优先级。

与特定中断类型无关的中断标志（`INTR_TYPE_*`）可用于指定硬件和软件中断处理程序的附加属性。`INTR_EXCL` 标志指定此处理程序不能与另一个处理程序共享中断线程。`INTR_MPSAFE` 标志指定此处理程序是 MP 安全的，即执行时不需要持有 Giant 互斥锁。`INTR_ENTROPY` 标志指定此处理程序绑定的中断源是良好的熵源，因此在来自该处理程序源的中断触发时应收集熵。目前，`INTR_ENTROPY` 标志对软件中断处理程序无效。`INTR_SLEEPABLE` 标志指定中断 ithread 可以睡眠。目前，`INTR_SLEEPABLE` 标志要求设置 `INTR_EXCL` 标志。

### 处理程序回调

每个 `struct intr_event` 在创建时被分配三个可选的回调函数：`pre_ithread`、`post_ithread` 和 `post_filter`。这些回调旨在由中断控制器驱动定义，以允许执行诸如屏蔽和取消屏蔽硬件中断信号之类的操作。

当中断被触发时，所有 filter 都会运行，以确定是否应调度任何线程化中断处理程序由关联的中断线程执行。如果没有调度线程化处理程序，则调用 `post_filter` 回调，该回调应确认中断并允许其在将来再次触发。如果调度了任何线程化处理程序，则改为调用 `pre_ithread` 回调。此处理程序应确认中断，但也应确保在线程化处理程序执行之前中断不会持续触发。通常，此回调在中断控制器中屏蔽电平触发中断，而保持边沿触发中断不变。一旦所有线程化处理程序执行完毕，从中断线程调用 `post_ithread` 回调以启用未来的中断。通常，此回调在中断控制器中取消屏蔽电平触发中断。

## 返回值

`intr_event_add_handler`、`intr_event_create`、`intr_event_destroy`、`intr_event_handle` 和 `intr_event_remove_handler` 函数成功时返回零，失败时返回非零。`intr_priority` 函数返回与传入的中断标志对应的进程优先级。

## 实例

swi_add(9) 函数演示了 `intr_event_create` 和 `intr_event_add_handler` 的使用。

```c
int
swi_add(struct intr_event **eventp, const char *name, driver_intr_t handler,
    void *arg, int pri, enum intr_type flags, void **cookiep)
{
	struct intr_event *ie;
	int error = 0;
	if (flags & INTR_ENTROPY)
		return (EINVAL);
	ie = (eventp != NULL) ? *eventp : NULL;
	if (ie != NULL) {
		if (!(ie->ie_flags & IE_SOFT))
			return (EINVAL);
	} else {
		error = intr_event_create(&ie, NULL, IE_SOFT, 0,
		    NULL, NULL, NULL, swi_assign_cpu, "swi%d:", pri);
		if (error)
			return (error);
		if (eventp != NULL)
			*eventp = ie;
	}
	if (handler != NULL) {
		error = intr_event_add_handler(ie, name, NULL, handler, arg,
		    PI_SWI(pri), flags, cookiep);
	}
	return (error);
}
```

## 错误

`intr_event_add_handler` 函数在以下情况将失败：

`[EINVAL]` `ie` 或 `name` 参数为 `NULL`。

`[EINVAL]` `handler` 和 `filter` 参数均为 `NULL`。

`[EINVAL]` 指定了 `IH_EXCLUSIVE` 标志且中断线程 `ie` 已有至少一个处理程序，或中断线程 `ie` 已有一个独占处理程序。

`intr_event_create` 函数在以下情况将失败：

`[EINVAL]` `flags` 参数中指定了 `IE_SOFT` 以外的标志。

`intr_event_destroy` 函数在以下情况将失败：

`[EINVAL]` `ie` 参数为 `NULL`。

`[EBUSY]` `ie` 指向的中断事件有至少一个尚未用 `intr_event_remove_handler` 移除的处理程序。

`intr_event_handle` 函数在以下情况将失败：

`[EINVAL]` `ie` 参数为 `NULL`。

`[EINVAL]` 没有分配给 `ie` 的中断处理程序。

`[EINVAL]` 中断未被任何 filter 确认且没有关联的线程处理程序。

`intr_event_remove_handler` 函数在以下情况将失败：

`[EINVAL]` `cookie` 参数为 `NULL`。

## 参见

critical(9), [kthread(9)](kthread.9.md), [locking(9)](locking.9.md), [malloc(9)](malloc.9.md), [swi(9)](swi.9.md), uma(9)

## 历史

中断线程及其对应的 API 首次出现于 FreeBSD 5.0。
