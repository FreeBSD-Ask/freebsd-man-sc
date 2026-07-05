# dtrace_sched.4

`dtrace_sched` — 用于跟踪 CPU 调度事件的 DTrace 提供者

## 名称

`dtrace_sched`

## 概要

`Fn sched:::change-pri struct thread * struct proc * uint8_t Fn sched:::dequeue struct thread * struct proc * void * Fn sched:::enqueue struct thread * struct proc * void * int Fn sched:::lend-pri struct thread * struct proc * uint8_t struct thread * Fn sched:::load-change int int Fn sched:::off-cpu struct thread * struct proc * Fn sched:::on-cpu Fn sched:::preempt Fn sched:::remain-cpu Fn sched:::surrender struct thread * struct proc * Fn sched:::sleep Fn sched:::tick struct thread * struct proc * Fn sched:::wakeup struct thread * struct proc *`

## 描述

DTrace `sched` 提供者允许跟踪 4BSD 和 ULE 调度器中与 CPU 调度相关的事件。

Fn sched:::change-pri 探测在线程的活动调度优先级即将更新时触发。前两个参数是即将更改优先级的线程和相应的进程。第三个参数是线程的新绝对优先级，而当前值由 `args[0]->td_priority` 给出。Fn sched:::lend-pri 探测在当前运行的线程通过优先级借用来提升另一线程的优先级时触发。前两个参数是即将更改优先级的线程和相应的进程。第三个参数是线程的新绝对优先级。第四个参数是当前运行的线程。

Fn sched:::dequeue 探测在可运行线程从调度器运行队列中移除之前立即触发。这可能在线程即将在 CPU 上开始执行时，或在线程正在迁移到不同运行队列时发生。后者可能在几种情况下发生：调度器可能正在尝试在多个 CPU 之间重新平衡负载、线程的调度优先级可能已更改，或线程的 CPU 亲和性设置可能已更改。Fn sched:::dequeue 的前两个参数是线程和相应的进程。第三个参数当前始终为 `NULL`。Fn sched:::enqueue 探测在可运行线程即将添加到调度器运行队列时触发。其前两个参数是线程和相应的进程。第三个参数当前始终为 `NULL`。第四个参数是布尔值，如果线程在其运行队列槽的开头入队则为非零，如果线程在末尾入队则为零。

Fn sched:::load-change 探测在线程队列的负载调整后触发。第一个参数是与线程队列关联的 CPU 的 cpuid，第二个参数是线程队列的调整后负载，即队列中的元素数。

Fn sched:::off-cpu 探测由调度器暂停当前运行线程的执行触发，Fn sched:::on-cpu 探测在当前线程已被选择在 CPU 上运行并即将开始或恢复执行时触发。Fn sched:::off-cpu 的参数是选择在当前运行线程之后运行的线程和相应的进程。如果这两个线程是同一线程，则改为触发 Fn sched:::remain-cpu 探测。

Fn sched:::surrender 探测在调度器被另一 CPU 上运行的线程通过处理器间中断调用以做出调度决策时触发。此探测的参数是被中断的线程及其相应的进程。此探测当前始终在被中断线程的上下文中触发。

Fn sched:::preempt 探测在当前运行线程被抢占之前立即触发。当此情况发生时，调度器将选择新线程运行，随后将触发 Fn sched:::off-cpu 或 Fn sched:::remain-cpu 探测之一，具体取决于调度器是否选择被抢占的线程。

Fn sched:::sleep 探测在当前运行线程即将暂停执行并开始等待条件满足之前立即触发。Fn sched:::wakeup 探测在线程在进入睡眠后设置为恢复执行时触发。其参数是被唤醒的线程和相应的进程。

Fn sched:::tick 在每个调度器时钟节拍之前触发。其参数是当前运行的线程及其相应的进程。

## 参数

`sched` 提供者探测使用内核类型 `struct proc` 和 `struct thread` 分别表示进程和线程。这些结构有许多字段，定义在 `sys/proc.h` 中。在探测体中，当前运行的线程始终可通过 `curthread` 全局变量获取，其类型为 `struct thread *`。例如，当运行中的线程即将睡眠时，Fn sched:::sleep 探测在该线程的上下文中触发，可使用 `curthread` 访问。`curcpu` 全局变量包含当前运行线程正在执行的 CPU 的 cpuid。

## 实例

以下脚本按进程名称分解 CPU 利用率：

```sh
sched:::on-cpu
{
        self->ts = timestamp;
}
sched:::off-cpu
/self->ts != 0/
{
        @[execname] = sum((timestamp - self->ts) / 1000);
        self->ts = 0;
}
```

此处，DTrace 在每次线程被调度运行时存储时间戳，并在其被取消调度时计算经过的微秒数。结果按进程名称求和。

## 兼容性

此提供者与 Solaris 中的 `sched` 提供者不兼容。特别是，探测参数类型为原生 FreeBSD 类型，且 Fn sched:::cpucaps-sleep、Fn sched:::cpucaps-wakeup、Fn sched:::schedctl-nopreempt、Fn sched:::schedctl-preempt 和 Fn sched:::schedctl-yield 探测在 FreeBSD 中不可用。

Fn sched:::lend-pri 和 Fn sched:::load-change 探测是 FreeBSD 特有的。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [sched_4bsd(4)](sched_4bsd.4.md), [sched_ule(4)](sched_ule.4.md), [SDT(9)](../man9/SDT.9.md), [sleepqueue(9)](../man9/sleepqueue.9.md)

## 历史

`sched` 提供者首次出现于 FreeBSD 8.4 和 9.1。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
