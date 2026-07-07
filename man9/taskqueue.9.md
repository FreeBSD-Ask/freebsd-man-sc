# taskqueue(9)

`taskqueue` — 异步任务执行

## 名称

`taskqueue`

## 概要

`#include <sys/param.h>`

`#include <sys/kernel.h>`

`#include <sys/malloc.h>`

`#include <sys/queue.h>`

`#include <sys/taskqueue.h>`

```c
typedef void (*task_fn_t)(void *context, int pending);
typedef void (*taskqueue_enqueue_fn)(void *context);
struct task {
	STAILQ_ENTRY(task)	ta_link;	/* 队列链接 */
	u_short			ta_pending;	/* 入队次数计数 */
	u_short			ta_priority;	/* 队列中任务的优先级 */
	task_fn_t		ta_func;	/* 任务处理函数 */
	void			*ta_context;	/* 处理函数的参数 */
};
enum taskqueue_callback_type {
	TASKQUEUE_CALLBACK_TYPE_INIT,
	TASKQUEUE_CALLBACK_TYPE_SHUTDOWN,
};
typedef void (*taskqueue_callback_fn)(void *context);
struct timeout_task;
```

`struct taskqueue * taskqueue_create(const char *name, int mflags, taskqueue_enqueue_fn enqueue, void *context)`

`struct taskqueue * taskqueue_create_fast(const char *name, int mflags, taskqueue_enqueue_fn enqueue, void *context)`

`int taskqueue_start_threads(struct taskqueue **tqp, int count, int pri, const char *name, ...)`

`int taskqueue_start_threads_cpuset(struct taskqueue **tqp, int count, int pri, cpuset_t *mask, const char *name, ...)`

`int taskqueue_start_threads_in_proc(struct taskqueue **tqp, int count, int pri, struct proc *proc, const char *name, ...)`

`void taskqueue_set_callback(struct taskqueue *queue, enum taskqueue_callback_type cb_type, taskqueue_callback_fn callback, void *context)`

`void taskqueue_free(struct taskqueue *queue)`

`int taskqueue_enqueue(struct taskqueue *queue, struct task *task)`

`int taskqueue_enqueue_flags(struct taskqueue *queue, struct task *task, int flags)`

`int taskqueue_enqueue_timeout(struct taskqueue *queue, struct timeout_task *timeout_task, int ticks)`

`int taskqueue_enqueue_timeout_sbt(struct taskqueue *queue, struct timeout_task *timeout_task, sbintime_t sbt, sbintime_t pr, int flags)`

`int taskqueue_cancel(struct taskqueue *queue, struct task *task, u_int *pendp)`

`int taskqueue_cancel_timeout(struct taskqueue *queue, struct timeout_task *timeout_task, u_int *pendp)`

`void taskqueue_drain(struct taskqueue *queue, struct task *task)`

`void taskqueue_drain_timeout(struct taskqueue *queue, struct timeout_task *timeout_task)`

`void taskqueue_drain_all(struct taskqueue *queue)`

`void taskqueue_quiesce(struct taskqueue *queue)`

`void taskqueue_block(struct taskqueue *queue)`

`void taskqueue_unblock(struct taskqueue *queue)`

`int taskqueue_member(struct taskqueue *queue, struct thread *td)`

`void taskqueue_run(struct taskqueue *queue)`

`TASK_INIT(struct task *task, int priority, task_fn_t func, void *context)`

`TASK_INITIALIZER(int priority, task_fn_t func, void *context)`

`TASKQUEUE_DECLARE(name)`

`TASKQUEUE_DEFINE(name, taskqueue_enqueue_fn enqueue, void *context, init)`

`TASKQUEUE_FAST_DEFINE(name, taskqueue_enqueue_fn enqueue, void *context, init)`

`TASKQUEUE_DEFINE_THREAD(name)`

`TASKQUEUE_FAST_DEFINE_THREAD(name)`

`TIMEOUT_TASK_INIT(struct taskqueue *queue, struct timeout_task *timeout_task, int priority, task_fn_t func, void *context)`

## 描述

这些函数为代码的异步执行提供了简单接口。

`taskqueue_create()` 用于创建新队列。其参数包括一个应当唯一的名称、一组指定调用 `malloc()` 是否允许睡眠的 [malloc(9)](malloc.9.md) 标志、一个在任务添加到队列时由 `taskqueue_enqueue()` 调用的函数，以及一个指向记录服务该队列的线程标识的内存位置的指针。从 `taskqueue_enqueue()` 调用的函数必须安排对队列进行处理（例如通过调度软件中断或唤醒内核线程）。记录线程标识的内存位置用于通知服务线程终止——当此值设为零并向线程发送信号时，线程将终止。如果该队列打算用于快速中断处理程序，应使用 `taskqueue_create_fast()` 而非 `taskqueue_create()`。

`taskqueue_free()` 用于释放队列所占用的内存。队列上的所有任务将在此时执行，随后服务该队列的线程将收到退出通知。

创建任务队列后，应使用 `taskqueue_start_threads()`、`taskqueue_start_threads_cpuset()` 或 `taskqueue_start_threads_in_proc()` 启动其线程。`taskqueue_start_threads_cpuset()` 接受 `cpuset` 参数，使为该任务队列启动的线程限制在指定的 CPU 上运行。`taskqueue_start_threads_in_proc()` 接受 `proc` 参数，使为该任务队列启动的线程分配到指定的内核进程中。可选地，可使用 `taskqueue_set_callback()` 注册回调。目前可为以下目的注册回调：

**`TASKQUEUE_CALLBACK_TYPE_INIT`** 此回调由任务队列中的每个线程在执行任何任务之前调用。此回调必须在任务队列的线程启动之前设置。

**`TASKQUEUE_CALLBACK_TYPE_SHUTDOWN`** 此回调由任务队列中的每个线程在执行完最后一个任务之后调用。此回调始终在任务队列结构被回收之前调用。

要将任务添加到任务队列上排队的任务列表中，需调用 `taskqueue_enqueue()`，并传入指向队列和任务的指针。如果任务的 `ta_pending` 字段非零，则简单地将其递增以反映任务入队的次数，上限为 USHRT_MAX。否则，将该任务添加到列表中第一个具有较低 `ta_priority` 值的任务之前，如果没有更低优先级的任务则添加到列表末尾。入队任务不执行任何内存分配，因此适合从中断处理程序中调用。如果队列正在被释放，此函数将返回 `EPIPE`。

当任务执行时，首先将其从队列中移除，记录 `ta_pending` 的值，然后将该字段清零。任务结构中的 `ta_func` 函数以 `ta_context` 字段的值作为第一个参数、`ta_pending` 字段的值作为第二个参数被调用。在 `ta_func` 函数返回后，对传给 `taskqueue_enqueue()` 的任务指针调用 wakeup(9)。

`taskqueue_enqueue_flags()` 接受一个额外的 `flags` 参数，该参数指定一组可选标志以改变 `taskqueue_enqueue()` 的行为。它包含以下一个或多个标志：

**`TASKQUEUE_FAIL_IF_PENDING`** 如果任务已计划执行，则 `taskqueue_enqueue_flags()` 失败。返回 `EEXIST`，`ta_pending` 计数值保持不变。

**`TASKQUEUE_FAIL_IF_CANCELING`** 如果任务处于取消状态，则 `taskqueue_enqueue_flags()` 失败并返回 `ECANCELED`。

`taskqueue_enqueue_timeout()` 用于在指定的 `ticks` 数之后调度入队。`taskqueue_enqueue_timeout_sbt()` 基于 `sbt`、`pr` 和 `flags` 提供更精细的调度控制，详见 [callout(9)](callout.9.md)。如果 `ticks` 参数为负数，则已计划的入队不会被重新调度。否则，任务将在未来、即经过 `ticks` 绝对值个时钟滴答之后入队。如果任务正在被排空，此函数返回 -1。否则返回待处理调用的次数。

`taskqueue_cancel()` 用于取消任务。`ta_pending` 计数被清零，旧值通过引用参数 `pendp` 返回（如果 `pendp` 非 `NULL`）。如果任务当前正在运行，返回 `EBUSY`，否则返回 0。要实现一个阻塞式 `taskqueue_cancel()` 以等待运行中的任务完成，可以这样编写：

```sh
while (taskqueue_cancel(tq, task, NULL) != 0)
	taskqueue_drain(tq, task);
```

注意，与 `taskqueue_drain()` 一样，调用者有责任确保任务在取消后不会被重新入队。

类似地，`taskqueue_cancel_timeout()` 用于取消已计划的任务执行。

`taskqueue_drain()` 用于等待任务完成，`taskqueue_drain_timeout()` 用于等待已计划的任务完成。无法保证在调用 `taskqueue_drain()` 之后任务不会被入队。如果调用者希望将任务置于已知状态，则在调用 `taskqueue_drain()` 之前，调用者应使用带外手段确保任务不会被入队。例如，如果任务由中断过滤器入队，则可以禁用该中断。

`taskqueue_drain_all()` 用于等待任务队列上所有待处理和运行中的任务完成。在 `taskqueue_drain_all()` 开始处理后投递到任务队列的任务，包括由之前调用 `taskqueue_enqueue_timeout()` 计划的待处理入队，不会延长 `taskqueue_drain_all()` 的等待时间，并可能在 `taskqueue_drain_all()` 返回后才完成。`taskqueue_quiesce()` 用于等待队列变空且所有运行中的任务完成。为避免无限期阻塞，调用者必须通过某种机制确保任务最终停止投递到队列。

`taskqueue_block()` 阻塞任务队列。它阻止任何已入队但尚未运行的任务被执行。未来对 `taskqueue_enqueue()` 的调用会将任务入队，但这些任务在调用 `taskqueue_unblock()` 之前不会运行。请注意，`taskqueue_block()` 不会等待任何当前正在运行的任务完成。因此，`taskqueue_block()` 不保证 `taskqueue_run()` 在 `taskqueue_block()` 返回后没有正在运行，但确实保证在调用 `taskqueue_unblock()` 之前不会再调用 `taskqueue_run()`。如果调用者要求保证 `taskqueue_run()` 没有运行，则必须由调用者自行安排。注意，如果对由 `taskqueue_block()` 阻塞的任务队列上入队的任务调用 `taskqueue_drain()`，则 `taskqueue_drain()` 在任务队列解除阻塞之前无法返回。如果阻塞在 `taskqueue_drain()` 中的线程应当调用 `taskqueue_unblock()` 的线程，则可能导致死锁。因此，不鼓励在 `taskqueue_block()` 之后使用 `taskqueue_drain()`，因为无法预先知道任务的状态。同样的警告也适用于 `taskqueue_drain_all()`。

`taskqueue_unblock()` 解除先前被阻塞的任务队列。此调用后所有已入队的任务均可运行。

`taskqueue_member()` 如果给定线程 `td` 是给定任务队列 `queue` 的一部分则返回 1，否则返回 0。

`taskqueue_run()` 运行指定 `queue` 中的所有待处理任务。通常此函数仅供内部使用。

提供了一个便捷宏 `TASK_INIT(task, priority, func, context)` 用于初始化 `task` 结构。`TASK_INITIALIZER` 宏生成任务结构体的初始化器。宏 `TIMEOUT_TASK_INIT(queue, timeout_task, priority, func, context)` 初始化 `timeout_task` 结构。`priority`、`func` 和 `context` 的值被简单地复制到任务结构字段中，`ta_pending` 字段被清零。

五个宏 `TASKQUEUE_DECLARE(name)`、`TASKQUEUE_DEFINE(name, enqueue, context, init)`、`TASKQUEUE_FAST_DEFINE(name, enqueue, context, init)`、`TASKQUEUE_DEFINE_THREAD(name)` 和 `TASKQUEUE_FAST_DEFINE_THREAD(name)` 用于声明对全局队列的引用、定义队列的实现，以及声明使用自身线程的队列。`TASKQUEUE_DEFINE` 宏安排在系统初始化期间使用其 `name`、`enqueue` 和 `context` 参数的值调用 `taskqueue_create()`。在调用 `taskqueue_create()` 之后，该宏的 `init` 参数作为 C 语句执行，允许执行任何进一步的初始化（例如注册中断处理程序等）。

`TASKQUEUE_DEFINE_THREAD` 宏定义了一个新的任务队列，并拥有自己的内核线程来服务任务。变量 `struct taskqueue *taskqueue_name` 用于将任务入队到该队列。

`TASKQUEUE_FAST_DEFINE` 和 `TASKQUEUE_FAST_DEFINE_THREAD` 的行为分别与 `TASKQUEUE_DEFINE` 和 `TASKQUEUE_DEFINE_THREAD` 相同，但任务队列使用 `taskqueue_create_fast()` 创建。

### 预定义任务队列

系统提供四个全局任务队列：`taskqueue_fast`、`taskqueue_swi`、`taskqueue_swi_giant` 和 `taskqueue_thread`。`taskqueue_fast` 队列用于从快速中断处理程序分发的 swi 处理程序，其中不能使用睡眠互斥锁。swi 任务队列通过软件中断机制运行。`taskqueue_swi` 队列在没有 `Giant` 内核锁保护的情况下运行，`taskqueue_swi_giant` 队列在 `Giant` 内核锁保护下运行。线程任务队列 `taskqueue_thread` 在内核线程上下文中运行，从此线程运行的任务不在 `Giant` 内核锁下运行。如果调用者希望在 `Giant` 下运行，应在其任务队列处理例程中显式获取和释放 `Giant`。

要使用这些队列，调用 `taskqueue_enqueue()` 并传入希望使用的队列对应的全局任务队列变量的值。

例如，软件中断队列可用于实现必须在中断处理程序中执行大量处理的中断处理程序。硬件中断处理程序对中断进行最少量的处理，然后入队一个任务来完成剩余工作。这最大限度减少了禁用中断所花费的时间。

例如，线程队列可由需要调用内核函数的中断级例程使用，这些函数所做的事情只能在线程上下文中完成（例如，使用 M_WAITOK 标志调用 malloc）。

注意，在共享任务队列（如 `taskqueue_swi`）上排队的任务在执行前可能会被延迟不确定的时间。如果无法容忍排队延迟，则应创建具有专用处理线程的私有任务队列。

## 参见

[callout(9)](callout.9.md), [intr_event(9)](intr_event.9.md), [kthread(9)](kthread.9.md), [swi(9)](swi.9.md)

## 历史

此接口首次出现在 FreeBSD 5.0 中。在 Plan 9 中有一个类似的设施。

## 作者

`taskqueue` 最初由 Doug Rabson <dfr@FreeBSD.org> 编写。

## 缺陷

无法保证任务不会延迟执行。
