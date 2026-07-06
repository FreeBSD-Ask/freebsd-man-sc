# callout.9

`callout_active` — 在指定时间后执行函数

## 名称

`callout_active`, `callout_deactivate`, `callout_drain`, `callout_init`, `callout_init_mtx`, `callout_init_rm`, `callout_init_rw`, `callout_pending`, `callout_reset`, `callout_reset_curcpu`, `callout_reset_on`, `callout_reset_sbt`, `callout_reset_sbt_curcpu`, `callout_reset_sbt_on`, `callout_schedule`, `callout_schedule_curcpu`, `callout_schedule_on`, `callout_schedule_sbt`, `callout_schedule_sbt_curcpu`, `callout_schedule_sbt_on`, `callout_stop`, `callout_when`

## 概要

```c
#include <sys/types.h>
#include <sys/callout.h>

typedef void callout_func_t (void *);

int
callout_active(struct callout *c)

void
callout_deactivate(struct callout *c)

int
callout_drain(struct callout *c)

void
callout_init(struct callout *c, int mpsafe)

void
callout_init_mtx(struct callout *c, struct mtx *mtx, int flags)

void
callout_init_rm(struct callout *c, struct rmlock *rm, int flags)

void
callout_init_rw(struct callout *c, struct rwlock *rw, int flags)

int
callout_pending(struct callout *c)

int
callout_reset(struct callout *c, int ticks, callout_func_t *func,
    void *arg)

int
callout_reset_curcpu(struct callout *c, int ticks, callout_func_t *func,
    void *arg)

int
callout_reset_on(struct callout *c, int ticks, callout_func_t *func,
    void *arg, int cpu)

int
callout_reset_sbt(struct callout *c, sbintime_t sbt, sbintime_t pr,
    callout_func_t *func, void *arg, int flags)

int
callout_reset_sbt_curcpu(struct callout *c, sbintime_t sbt,
    sbintime_t pr, callout_func_t *func, void *arg, int flags)

int
callout_reset_sbt_on(struct callout *c, sbintime_t sbt, sbintime_t pr,
    callout_func_t *func, void *arg, int cpu, int flags)

int
callout_schedule(struct callout *c, int ticks)

int
callout_schedule_curcpu(struct callout *c, int ticks)

int
callout_schedule_on(struct callout *c, int ticks, int cpu)

int
callout_schedule_sbt(struct callout *c, sbintime_t sbt, sbintime_t pr,
    int flags)

int
callout_schedule_sbt_curcpu(struct callout *c, sbintime_t sbt,
    sbintime_t pr, int flags)

int
callout_schedule_sbt_on(struct callout *c, sbintime_t sbt,
    sbintime_t pr, int cpu, int flags)

int
callout_stop(struct callout *c)

sbintime_t
callout_when(sbintime_t sbt, sbintime_t precision, int flags,
    sbintime_t *sbt_res, sbintime_t *precision_res)
```

## 描述

`callout` API 用于调度在未来的特定时间调用任意函数。此 API 的使用者必须为每个挂起的函数调用分配一个 callout 结构（struct callout）。此结构存储有关挂起函数调用的状态，包括要调用的函数和应调用该函数的时间。挂起的函数调用可以被取消或重新调度到其他时间。此外，在已调度的调用完成后，callout 结构可被重用以调度新的函数调用。

callout 仅提供单次模式。如果使用者需要周期性定时器，必须显式地重新调度每次函数调用。通常通过在被调用函数内重新调度后续调用来实现。

callout 函数不得睡眠。它们不能获取可睡眠的锁、等待条件变量、执行阻塞分配请求，或调用任何可能睡眠的其他操作。

每个 callout 结构在传递给任何其他 callout 函数之前，必须通过 `callout_init`、`callout_init_mtx`、`callout_init_rm` 或 `callout_init_rw` 初始化。`callout_init` 函数在 `c` 中初始化一个不与特定锁关联的 callout 结构。如果 `mpsafe` 参数为零，则该 callout 结构不被视为“多处理器安全”；调用 callout 函数之前将获取 Giant 锁，并在 callout 函数返回时释放。

`callout_init_mtx`、`callout_init_rm` 和 `callout_init_rw` 函数在 `c` 中初始化一个与特定锁关联的 callout 结构。该锁由 `mtx`、`rm` 或 `rw` 参数指定。在停止或重新调度 callout 时必须持有该关联锁。callout 子系统在调用 callout 函数之前获取关联锁，并在函数返回后释放。如果 callout 在 callout 子系统等待关联锁时被取消，则不会调用 callout 函数，并释放关联锁。这确保了停止或重新调度 callout 将中止任何先前调度的调用。

可睡眠的读多锁（用 `RM_SLEEPABLE` 标志初始化的锁）不能与 `callout_init_rm` 一起使用。类似地，其他可睡眠锁类型（如 [sx(9)](sx.9.md) 和 lockmgr(9)）不能与 callout 一起使用，因为 callout 子系统中不允许睡眠。

可为 `callout_init_mtx`、`callout_init_rm` 或 `callout_init_rw` 指定以下 `flags`：

**`CALLOUT_RETURNUNLOCKED`** callout 函数将自行释放关联锁，因此 callout 子系统不应在 callout 函数返回后尝试解锁。

**`CALLOUT_SHAREDLOCK`** 运行 callout 处理程序时，仅在读模式下获取锁。此标志被 `callout_init_mtx` 忽略。

`callout_stop` 函数在 callout `c` 当前挂起时取消该 callout。如果 callout 处于挂起状态且成功停止，则 `callout_stop` 返回 1。如果 callout 未设置或已服务完毕，则返回 -1。如果 callout 当前正在服务且无法停止，则返回 0。如果 callout 当前正在服务且无法停止，同时同一 callout 的下一次调用也已调度，则 `callout_stop` 取消下一次运行并返回 0。如果 callout 有关联锁，则在调用此函数时必须持有该锁。

`callout_drain` 函数与 `callout_stop` 相同，但如果 callout `c` 已在进行中，它将等待其完成。此函数**不得**在持有 callout 可能阻塞的任何锁时调用，否则会导致死锁。注意，如果 callout 子系统已开始处理此 callout，则 callout 函数可能在 `callout_drain` 返回之前被调用。但是，callout 子系统保证在 `callout_drain` 返回之前 callout 将完全停止。

`callout_reset` 和 `callout_schedule` 函数族为 callout `c` 调度未来的函数调用。如果 `c` 已有挂起的 callout，则在调度新调用之前取消它。如果取消了挂起的 callout，这些函数返回 1；如果没有挂起的 callout，返回 0。如果 callout 有关联锁，则在调用这些函数时必须持有该锁。

调用 callout 函数的时间由 `ticks` 参数或 `sbt`、`pr` 和 `flags` 参数决定。使用 `ticks` 时，callout 调度在 `ticks`/hz 秒后执行。`ticks` 的非正值被静默转换为值“1”。

`sbt`、`pr` 和 `flags` 参数提供对调度时间的更多控制，包括支持更高分辨率的时间、指定调度时间的精度，以及设置绝对截止时间而非相对超时。callout 调度在 `sbt` 指定的时间开始、并持续 `pr` 指定的时间窗口内执行。如果 `sbt` 指定了一个过去的时间，窗口将调整为从当前时间开始。`pr` 的非零值允许 callout 子系统将调度时间相近的 callout 合并为更少的定时器中断，从而降低处理开销和功耗。可指定以下 `flags` 来调整 `sbt` 和 `pr` 的解释：

**`C_ABSOLUTE`** 将 `sbt` 参数视为自启动以来的绝对时间。默认情况下，`sbt` 被视为相对时间量，类似于 `ticks`。

**`C_DIRECT_EXEC`** 直接从硬件中断上下文运行处理程序，而不是从 softclock 线程运行。这降低了延迟和开销，但对 callout 函数施加了更多约束。在此上下文中运行的 callout 函数只能使用自旋互斥锁进行锁定，并且应尽可能简短，因为它们以绝对优先级运行。

**`C_PREL`** 以时间间隔除以可接受时间偏差的二元对数形式指定相对事件时间精度：1 —— 1/2，2 —— 1/4，等等。注意，使用 `pr` 或此值中的较大者作为时间窗口的长度。较小的值（导致较大的时间间隔）允许 callout 子系统在一次定时器中断中聚合更多事件。

**`C_PRECALC`** `sbt` 参数指定 callout 应运行的绝对时间，`pr` 参数指定请求的精度，该精度在调度过程中不会被调整。`sbt` 和 `pr` 值应通过先前调用 `callout_when` 计算，该函数使用用户提供的 `sbt`、`pr` 和 `flags` 值。

**`C_HARDCLOCK`** 如果可能，将超时与 `hardclock` 调用对齐。

`callout_reset` 函数接受 `func` 参数，用于标识时间到期时要调用的函数。它必须是指向接受单个 `void *` 参数的函数的指针。调用时，`func` 将以 `arg` 作为其唯一参数。`callout_schedule` 函数重用前一次 callout 的 `func` 和 `arg` 参数。注意，在使用 `callout_schedule` 函数之前，必须始终调用 `callout_reset` 函数之一来初始化 `func` 和 `arg`。

callout 子系统为系统中的每个 CPU 提供一个 softclock 线程。callout 被分配到单个 CPU，并由该 CPU 的 softclock 线程执行。最初，callout 被分配到 CPU 0。`callout_reset_on`、`callout_reset_sbt_on`、`callout_schedule_on` 和 `callout_schedule_sbt_on` 函数将 callout 分配到 CPU `cpu`。`callout_reset_curcpu`、`callout_reset_sbt_curcpu`、`callout_schedule_curcpu` 和 `callout_schedule_sbt_curcpu` 函数将 callout 分配到当前 CPU。`callout_reset`、`callout_reset_sbt`、`callout_schedule` 和 `callout_schedule_sbt` 函数调度 callout 在其当前分配到的 CPU 的 softclock 线程中执行。

默认情况下，softclock 线程不会固定到各自的 CPU。通过将 `kern.pin_default_swi` 加载器可调参数设置为非零值，可将 CPU 0 的 softclock 线程固定到 CPU 0。通过将 `kern.pin_pcpu_swi` 加载器可调参数设置为非零值，可将非零 CPU 的 softclock 线程固定到各自的 CPU。

`callout_pending`、`callout_active` 和 `callout_deactivate` 宏提供对 callout 当前状态的访问。`callout_pending` 宏检查 callout 是否*挂起*；当已设置超时但时间尚未到达时，callout 被视为*挂起*。注意，一旦超时时间到达且 callout 子系统开始处理此 callout，即使 callout 函数可能尚未完成（甚至尚未开始）执行，`callout_pending` 也将返回 `FALSE`。`callout_active` 宏检查 callout 是否被标记为*活动*，`callout_deactivate` 宏清除 callout 的*活动*标志。callout 子系统在设置超时时将 callout 标记为*活动*，并在 `callout_stop` 和 `callout_drain` 中清除*活动*标志，但当 callout 通过执行 callout 函数正常到期时，它*不会*清除该标志。

`callout_when` 函数可用于根据所需时间 `sbt`、精度 `precision` 和 `flags` 参数请求的其他调整，预先计算超时应运行的绝对时间和调度运行时间的精度。`callout_when` 函数接受的标志与 `callout_reset` 函数的标志相同。结果时间赋值给 `sbt_res` 参数指向的变量，结果精度赋值给 `*precision_res`。将结果传递给 `callout_reset` 时，将 `C_PRECALC` 标志添加到 `flags`，以避免不正确的重新调整。此函数适用于需要预先知道 callout 运行的精确时间的情况，因为在 `callout_reset` 调用后尝试从 callout 结构本身读取此时间存在竞态。

### 避免竞态条件

callout 子系统从其自身的线程上下文调用 callout 函数。如果没有某种同步，callout 函数可能与另一线程尝试停止或重置 callout 的操作并发调用。特别是，由于 callout 函数通常将获取锁作为其第一个操作，因此 callout 函数可能已被调用，但在另一线程尝试重置或停止 callout 时正阻塞等待该锁。

有三种主要技术可解决这些同步问题。第一种方法是首选的，因为它最简单：

- callout 在通过 `callout_init_mtx`、`callout_init_rm` 或 `callout_init_rw` 初始化时可以与特定锁关联。当 callout 与锁关联时，callout 子系统在调用 callout 函数之前获取该锁。这允许 callout 子系统透明地处理 callout 取消、调度和执行之间的竞态。注意，在调用 `callout_stop` 或 `callout_reset`/`callout_schedule` 函数之一之前，必须获取关联锁以提供此安全性。通过 `callout_init` 初始化且 `mpsafe` 设置为零的 callout 隐式与 `Giant` 互斥锁关联。如果在取消或重新调度 callout 时持有 `Giant`，则其使用将防止与 callout 函数的竞态。

```c
if (sc->sc_flags & SCFLG_CALLOUT_RUNNING) {
	if (callout_stop(&sc->sc_callout)) {
		sc->sc_flags &= ~SCFLG_CALLOUT_RUNNING;
		/* 成功停止 */
	} else {
		/*
		 * callout 已到期，callout
		 * 函数即将执行
		 */
	}
}
```

- `callout_stop`（或 `callout_reset` 和 `callout_schedule` 函数族）的返回值指示 callout 是否已被移除。如果已知 callout 已设置且 callout 函数尚未执行，则返回值 `FALSE` 表示 callout 函数即将被调用。例如：

- `callout_pending`、`callout_active` 和 `callout_deactivate` 宏可组合使用以解决竞态条件。当 callout 的超时被设置时，callout 子系统将 callout 同时标记为*活动*和*挂起*。当超时时间到达时，callout 子系统首先清除*挂起*标志，开始处理 callout。然后调用 callout 函数，不改变*活动*标志，即使在 callout 函数返回后也不清除*活动*标志。此处描述的机制要求 callout 函数本身使用 `callout_deactivate` 宏清除*活动*标志。`callout_stop` 和 `callout_drain` 函数在返回之前始终清除*活动*和*挂起*标志。callout 函数应首先检查*挂起*标志，如果 `callout_pending` 返回 `TRUE`，则不执行任何操作并返回。这表示 callout 在调用 callout 函数之前刚通过 `callout_reset` 重新调度。如果 `callout_active` 返回 `FALSE`，callout 函数也应不执行任何操作并返回。这表示 callout 已被停止。最后，callout 函数应调用 `callout_deactivate` 清除*活动*标志。例如：

```c
mtx_lock(&sc->sc_mtx);
if (callout_pending(&sc->sc_callout)) {
	/* callout 已被重置 */
	mtx_unlock(&sc->sc_mtx);
	return;
}
if (!callout_active(&sc->sc_callout)) {
	/* callout 已被停止 */
	mtx_unlock(&sc->sc_mtx);
	return;
}
callout_deactivate(&sc->sc_callout);
/* callout 函数的其余部分 */
```

结合适当的同步（如上面使用的互斥锁），此方法允许 `callout_stop` 和 `callout_reset` 函数在任何时候使用而不会产生竞态。例如：

```c
mtx_lock(&sc->sc_mtx);
callout_stop(&sc->sc_callout);
/* callout 现在已有效停止。 */
```

如果 callout 仍处于挂起状态，这些函数正常运行；但如果 callout 的处理已经开始，则 callout 函数中的测试会导致它不执行进一步操作而返回。callout 函数与其他代码之间的同步确保在 callout 函数已通过 `callout_deactivate` 调用之后，永远不会尝试停止或重置 callout。上述技术还确保*活动*标志始终反映 callout 是否有效启用或禁用。如果 `callout_active` 返回 false，则 callout 已被有效禁用，因为即使 callout 子系统实际上即将调用 callout 函数，callout 函数也将不执行任何操作而返回。

当 callout 最后一次被停止时，必须考虑最后一个竞态条件。在这种情况下，让 callout 函数本身检测到 callout 已被停止可能不安全，因为它可能需要访问已被销毁或回收的数据对象。为确保 callout 完全完成，应使用 `callout_drain`。特别是，在销毁其关联锁或释放 callout 结构的存储之前，应始终对 callout 进行排空。

## 返回值

`callout_active` 宏返回 callout 的*活动*标志的状态。

`callout_pending` 宏返回 callout 的*挂起*标志的状态。

`callout_reset` 和 `callout_schedule` 函数族在新函数调用调度之前，如果 callout 处于挂起状态，则返回 1。

`callout_stop` 和 `callout_drain` 函数在调用时如果 callout 仍处于挂起状态，则返回 1；如果 callout 无法停止，则返回 0；如果 callout 未运行或已完成，则返回 -1。

## 参见

[dtrace_callout_execute(4)](../man4/dtrace_callout_execute.4.md)

## 历史

FreeBSD 最初使用长期存在的 BSD 链表 callout 机制，该机制提供 O(n) 的插入和删除运行时间，但不为 untimeout 操作生成或要求句柄。

FreeBSD 3.0 引入了一组来自 NetBSD 的新的 timeout 和 untimeout 例程，这些例程基于 Adam M. Costello 和 George Varghese 的工作，发表在题为《Redesigning the BSD Callout and Timer Facilities》的技术报告中，并由 Justin T. Gibbs 修改以包含到 FreeBSD 中。该实现中使用的数据结构的原始工作由 G. Varghese 和 A. Lauck 在论文《Hashed and Hierarchical Timing Wheels: Data Structures for the Efficient Implementation of a Timer Facility》中发表，刊登于《Proceedings of the 11th ACM Annual Symposium on Operating Systems Principles》。

FreeBSD 3.3 引入了 `callout_init`、`callout_reset` 和 `callout_stop` 的第一个实现，允许调用者为 callout 分配专用存储。这确保了 callout 始终会触发，而 `timeout` 在无法分配 callout 时会静默失败。

FreeBSD 5.0 允许通过 `callout_init` 将 callout 处理程序标记为 MPSAFE。

FreeBSD 5.3 引入了 `callout_drain`。

FreeBSD 6.0 引入了 `callout_init_mtx`。

FreeBSD 8.0 引入了每 CPU callout 轮、`callout_init_rw` 和 `callout_schedule`。

FreeBSD 9.0 更改了用于驱动 callout 的底层定时器中断，优先使用一次性事件定时器而非周期性定时器中断。

FreeBSD 10.0 将 callout 轮切换为支持无滴答操作。这些更改引入了 `sbintime_t` 和 `callout_reset_sbt*` 函数族。FreeBSD 10.0 还添加了 `C_DIRECT_EXEC` 和 `callout_init_rm`。

FreeBSD 10.2 引入了 `callout_schedule_sbt*` 函数族。

FreeBSD 11.0 引入了 `callout_async_drain`。FreeBSD 11.1 引入了 `callout_when`。FreeBSD 13.0 移除了 `timeout_t`、`timeout` 和 `untimeout`。
