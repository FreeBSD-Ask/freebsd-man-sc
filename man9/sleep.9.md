# sleep(9)

`msleep` — 等待事件

## 名称

`msleep`, `msleep_sbt`, `msleep_spin`, `msleep_spin_sbt`, `pause`, `pause_sig`, `pause_sbt`, `tsleep`, `tsleep_sbt`, `wakeup`, `wakeup_one`, `wakeup_any`

## 概要

`#include <sys/param.h>`

`#include <sys/systm.h>`

`#include <sys/proc.h>`

`Ft int Fn msleep const void *chan struct mtx *mtx int priority const char *wmesg int timo Ft int Fn msleep_sbt const void *chan struct mtx *mtx int priority \ "const char *wmesg" "sbintime_t sbt" "sbintime_t pr" "int flags" Ft int Fn msleep_spin const void *chan struct mtx *mtx const char *wmesg int timo Ft int Fn msleep_spin_sbt const void *chan struct mtx *mtx const char *wmesg \ "sbintime_t sbt" "sbintime_t pr" "int flags" Ft int Fn pause const char *wmesg int timo Ft int Fn pause_sig const char *wmesg int timo Ft int Fn pause_sbt const char *wmesg sbintime_t sbt sbintime_t pr \ "int flags" Ft int Fn tsleep const void *chan int priority const char *wmesg int timo Ft int Fn tsleep_sbt const void *chan int priority const char *wmesg \ "sbintime_t sbt" "sbintime_t pr" "int flags" Ft void Fn wakeup const void *chan Ft void Fn wakeup_one const void *chan Ft void Fn wakeup_any const void *chan`

## 描述

函数 `tsleep`、`msleep`、`msleep_spin`、`pause`、`pause_sig`、`pause_sbt`、`wakeup`、`wakeup_one` 和 `wakeup_any` 处理基于事件的线程阻塞。如果线程必须等待外部事件，它会通过 `tsleep`、`msleep`、`msleep_spin`、`pause`、`pause_sig` 或 `pause_sbt` 进入睡眠。线程也可以使用锁定原语睡眠例程 mtx_sleep(9)、rw_sleep(9) 或 sx_sleep(9) 来等待。

参数 `chan` 是一个任意地址，用于唯一标识使线程进入睡眠的事件。所有在单个 `chan` 上睡眠的线程稍后会被 `wakeup`（通常从某个中断例程中调用）唤醒，以表示线程正在阻塞等待的资源现在可用。

参数 `priority` 指定线程的新优先级以及一些可选标志。如果新优先级不为 0，则线程在恢复时将以指定的 `priority` 变为可运行。永远不应使用 `PZERO`，因为它仅用于兼容性。新优先级为 0 表示在线程再次变为可运行时使用线程的当前优先级。

如果 `priority` 包含 `PCATCH` 标志，则允许挂起信号中断睡眠，否则在睡眠期间忽略挂起的信号。如果设置了 `PCATCH` 且信号变为挂起，则如果可能应重新启动当前系统调用则返回 `ERESTART`，如果系统调用应被信号中断（返回 `EINTR`）则返回 `EINTR`。

参数 `wmesg` 是描述睡眠条件的字符串，供 [ps(1)](../man1/ps.1.md) 等工具使用。由于这些程序显示任意字符串的空间有限，此消息不应超过 6 个字符。

参数 `timo` 指定睡眠的超时。如果 `timo` 不为 0，则线程最多睡眠 `timo` / `hz` 秒。如果超时到期，则睡眠函数将返回 `EWOULDBLOCK`。

`msleep_sbt`、`msleep_spin_sbt`、`pause_sbt` 和 `tsleep_sbt` 函数采用 `sbt` 参数而不是 `timo`。它允许调用者以 `sbintime_t` 形式指定具有更高分辨率的相对或绝对唤醒时间。参数 `pr` 允许调用者指定所需的绝对事件精度。参数 `flags` 允许调用者传递额外的 `callout_reset_sbt` 标志。

包括 `msleep`、`msleep_spin` 在内的多个睡眠函数以及锁定原语睡眠例程都指定了一个额外的锁参数。该锁会在睡眠之前被释放，并在睡眠例程返回之前重新获取。如果 `priority` 包含 `PDROP` 标志，则该锁在返回之前不会被重新获取。该锁用于确保可以原子性地检查条件，并且当前线程可以在不遗漏条件变化或相关唤醒的情况下被挂起。此外，所有睡眠例程在线程挂起期间都会完全释放 `Giant` 互斥锁（即使被递归持有），并在函数返回之前重新获取 `Giant` 互斥锁。注意，`Giant` 互斥锁可以被指定为要释放的锁。但是，在这种情况下，不允许使用 `PDROP` 标志。

为避免丢失唤醒，应使用锁来防止竞态，或指定超时以限制由于丢失唤醒而导致的延迟上限。因此，仅当持有 `Giant` 互斥锁时才应以超时 0 调用 `tsleep` 函数。

`msleep` 函数要求 `mtx` 引用默认（即非自旋）互斥锁。其使用已弃用，推荐使用 mtx_sleep(9)，后者提供相同的行为。

`msleep_spin` 函数要求 `mtx` 引用自旋互斥锁。`msleep_spin` 函数不接受 `priority` 参数，因此不支持更改当前线程的优先级、`PDROP` 标志或通过 `PCATCH` 标志捕获信号。

`pause` 函数是 `tsleep` 的包装器，它将当前线程的执行挂起指定的超时时间。线程不能通过信号或调用 `wakeup`、`wakeup_one` 或 `wakeup_any` 提前唤醒。`pause_sig` 函数是 `pause` 的变体，可以通过信号提前唤醒。

`wakeup_one` 函数使队列中在参数 `chan` 上睡眠的第一个最高优先级线程变为可运行。当大量线程在同一地址上睡眠，但只有一个线程在变为可运行时实际上能做任何有用的工作时，这减少了负载。

由于其工作方式，`wakeup_one` 函数要求只有相关线程在特定的 `chan` 地址上睡眠。程序员有责任选择唯一的 `chan` 值。旧的 `wakeup` 函数不要求这一点，尽管线程共享 `chan` 值从来都不是好做法。从 `wakeup` 转换到 `wakeup_one` 时，要特别注意确保没有其他线程在同一 `chan` 上等待。

`wakeup_any` 函数类似于 `wakeup_one`，不同之处在于它使队列中的最后一个线程（睡眠较少）变为可运行，忽略公平性。当已知在 `chan` 上睡眠的线程相同且没有理由公平时，可以使用它。

如果 `timo` 或 `sbt` 给定的超时基于绝对实时时钟值，则线程在读取 RTC 之前应将全局 `rtc_generation` 复制到其 `td_rtcgen` 成员中。如果调整了实时时钟，这些函数会将 `td_rtcgen` 设置为零并返回零。调用者应使用新的 RTC 值重新考虑其方向。

## 返回值

当通过调用 `wakeup` 或 `wakeup_one` 唤醒时，如果有挂起的信号且指定了 `PCATCH`，则返回非零错误代码。如果线程通过调用 `wakeup` 或 `wakeup_one` 唤醒，则 `msleep`、`msleep_spin`、`tsleep` 和锁定原语睡眠函数返回 0。当调整实时时钟时也可以返回零；有关 `td_rtcgen` 的信息见上文。否则，返回非零错误代码。

## 错误

如果出现以下情况，`msleep`、`msleep_spin`、`tsleep` 和锁定原语睡眠函数将失败：

**[EINTR]** 指定了 `PCATCH` 标志，捕获了信号，且系统调用应被中断。

**[ERESTART]** 指定了 `PCATCH` 标志，捕获了信号，且系统调用应重新启动。

**[EWOULDBLOCK]** 指定了非零超时且超时已到期。

## 参见

[ps(1)](../man1/ps.1.md), [callout(9)](callout.9.md), [locking(9)](locking.9.md), [malloc(9)](malloc.9.md), [mi_switch(9)](mi_switch.9.md), mtx_sleep(9), rw_sleep(9), sx_sleep(9)

## 历史

函数 `sleep` 和 `wakeup` 出现在 Version 1 AT&T UNIX 中。它们可能也出现在之前的 PDP-7 版本的 UNIX 中。它们是基本的进程同步模型。

`tsleep` 函数出现在 4.4BSD 中，并添加了参数 `wmesg` 和 `timo`。`sleep` 函数在 FreeBSD 2.2 中被移除。`wakeup_one` 函数出现在 FreeBSD 2.2 中。`msleep` 函数出现在 FreeBSD 5.0 中，`msleep_spin` 函数出现在 FreeBSD 6.2 中。`pause` 函数出现在 FreeBSD 7.0 中。`pause_sig` 函数出现在 FreeBSD 12.0 中。

## 作者

本手册页由 Jörg Wunsch <joerg@FreeBSD.org> 编写。
