# mi_switch.9

`mi_switch` — 切换到另一线程上下文

## 名称

`mi_switch`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/proc.h>
```

```c
void
mi_switch(int flags)
```

## 描述

`mi_switch` 函数实现线程上下文切换的机器无关前奏。它是每次上下文切换的唯一入口点，仅从内核中少数几个特定位置调用。上下文切换必然始终由被切换的线程执行，即使切换是从其他地方发起的；例如通过处理器间中断（IPI）请求的抢占。

`mi_switch` 的主要用途可枚举如下：

- 在诸如 sleepq_wait(9) 或 `turnstile_wait` 等函数内部，当前线程自愿让出 CPU 以等待某些资源或锁变为可用时。
- 由于到达更高优先级线程而导致的非自愿抢占。
- 在 critical_exit(9) 的末尾，如果由于临界区而推迟了抢占。
- 在 TDA_SCHED AST 处理程序内部，当请求在返回用户模式之前重新调度时。这有多种原因，其中值得注意的是来自 `sched_clock` 的请求，当运行线程超过其时间片时。
- 在信号处理代码中（参见 issignal(9)），如果传递的信号导致进程停止。
- 在 `thread_suspend_check` 中，当线程由于整个进程的挂起状态而需要停止执行时。
- 在 [kern_yield(9)](kern_yield.9.md) 中，当线程希望自愿让出处理器时。

`mi_switch` 的 `flags` 参数指示上下文切换类型。必须传递以下之一：

**`SWT_OWEPREEMPT`** 由于退出临界区后延迟抢占而切换。

**`SWT_TURNSTILE`** 在将调度优先级传播给资源所有者后切换。

**`SWT_SLEEPQ`** 开始在 [sleepqueue(9)](sleepqueue.9.md) 上等待。

**`SWT_RELINQUISH`** yield 调用。

**`SWT_NEEDRESCHED`** 请求了重新调度。

**`SWT_IDLE`** 从空闲线程切换。

**`SWT_IWAIT`** 处理中断的内核线程已完成工作，必须等待中断调度额外工作。

**`SWT_SUSPEND`** 线程被挂起。

**`SWT_REMOTEPREEMPT`** 由远程处理器发起的、被更高优先级线程抢占。

**`SWT_REMOTEWAKEIDLE`** 由远程处理器发起的、空闲线程被抢占。

**`SWT_BIND`** 运行线程已被绑定到另一处理器，必须被切换出。

除切换类型外，调用者必须通过按位或运算与 `SW_VOL` 或 `SW_INVOL` 标志之一（但不能同时）指定切换的性质。这两个标志分别表示上下文切换对当前线程而言是自愿的还是非自愿的。对于运行线程被抢占的非自愿上下文切换，调用者还应传递 `SW_PREEMPT` 标志。

进入 `mi_switch` 时，当前线程必须持有其分配的线程锁。该锁可作为上下文切换的一部分被解锁。线程在被重新调度并恢复执行后，将以未加锁状态退出 `mi_switch`。

`mi_switch` 通过 `sched_switch` 记录当前线程在将控制权交给调度器之前运行的时间量。在选择新线程运行后，调度器将调用 `cpu_switch` 执行低级上下文切换。

`cpu_switch` 是执行从运行线程 `oldtd` 到所选线程 `newtd` 实际切换的机器相关函数。

## 参见

cpu_switch(9), cpu_throw(9), critical_exit(9), issignal(9), [kern_yield(9)](kern_yield.9.md), [mutex(9)](mutex.9.md), [pmap(9)](pmap.9.md), [sleepqueue(9)](sleepqueue.9.md), [thread_exit(9)](thread_exit.9.md)
