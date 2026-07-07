# condvar(9)

`condvar` — 内核条件变量

## 名称

`condvar`, `cv_init`, `cv_destroy`, `cv_wait`, `cv_wait_sig`, `cv_wait_unlock`, `cv_timedwait`, `cv_timedwait_sbt`, `cv_timedwait_sig`, `cv_timedwait_sig_sbt`, `cv_signal`, `cv_broadcast`, `cv_broadcastpri`, `cv_wmesg`

## 概要

```c
#include <sys/param.h>
#include <sys/proc.h>
#include <sys/condvar.h>

void
cv_init(struct cv *cvp, const char *desc)

void
cv_destroy(struct cv *cvp)

void
cv_wait(struct cv *cvp, lock)

int
cv_wait_sig(struct cv *cvp, lock)

void
cv_wait_unlock(struct cv *cvp, lock)

int
cv_timedwait(struct cv *cvp, lock, int timo)

int
cv_timedwait_sbt(struct cv *cvp, lock, sbintime_t sbt,
    sbintime_t pr, int flags)

int
cv_timedwait_sig(struct cv *cvp, lock, int timo)

int
cv_timedwait_sig_sbt(struct cv *cvp, lock, sbintime_t sbt,
    sbintime_t pr, int flags)

void
cv_signal(struct cv *cvp)

void
cv_broadcast(struct cv *cvp)

void
cv_broadcastpri(struct cv *cvp, int pri)

const char *
cv_wmesg(struct cv *cvp)
```

## 描述

条件变量与互斥锁配合使用以等待条件发生。条件变量通过 `cv_init` 创建，其中 `cvp` 是指向 `struct cv` 空间的指针，`desc` 是指向描述该条件变量的以空字符结尾字符串的指针。条件变量通过 `cv_destroy` 销毁。线程通过调用 `cv_wait`、`cv_wait_sig`、`cv_wait_unlock`、`cv_timedwait` 或 `cv_timedwait_sig` 等待条件变量。线程通过调用 `cv_signal` 唤醒一个等待者，或调用 `cv_broadcast` 或 `cv_broadcastpri` 唤醒所有等待者。除唤醒等待者外，`cv_broadcastpri` 还通过提高任何不满足条件的线程的优先级，确保所有等待者的优先级至少为 `pri`。`cv_wmesg` 返回 `cvp` 的描述字符串，该字符串由初始调用 `cv_init` 时设置。

`lock` 参数是指向 [mutex(9)](mutex.9.md)、[rwlock(9)](rwlock.9.md) 或 [sx(9)](sx.9.md) 锁的指针。[mutex(9)](mutex.9.md) 参数必须使用 `MTX_DEF` 而非 `MTX_SPIN` 初始化。线程在调用 `cv_wait`、`cv_wait_sig`、`cv_wait_unlock`、`cv_timedwait` 或 `cv_timedwait_sig` 之前必须持有 `lock`。当线程等待条件时，`lock` 在线程阻塞之前被原子地释放，然后在函数调用返回之前重新获取。此外，线程在挂起时将完全释放 `Giant` 互斥锁（即使递归持有），并在函数返回之前重新获取 `Giant` 互斥锁。`cv_wait_unlock` 函数在返回之前不会重新获取锁。注意，`Giant` 互斥锁可作为 `lock` 指定。但是，`Giant` 不能用作 `cv_wait_unlock` 函数的 `lock`。所有等待者必须传递与 `cvp` 相同的 `lock`。

当 `cv_wait`、`cv_wait_sig`、`cv_wait_unlock`、`cv_timedwait` 和 `cv_timedwait_sig` 解除阻塞时，其调用线程被设为可运行。`cv_timedwait` 和 `cv_timedwait_sig` 最多等待 `timo` / `HZ` 秒后解除阻塞并返回 `EWOULDBLOCK`；否则返回 0。如果捕获到信号，`cv_wait_sig` 和 `cv_timedwait_sig` 将以 `EINTR` 或 `ERESTART` 提前返回；如果通过 `cv_signal` 或 `cv_broadcast` 发信号，则返回 0。

`cv_timedwait_sbt` 和 `cv_timedwait_sig_sbt` 函数采用 `sbt` 参数代替 `timo`。它允许以 `sbintime_t` 形式指定相对或绝对解除阻塞时间，分辨率更高。参数 `pr` 允许指定所需的绝对事件精度。参数 `flags` 允许传递附加的 `callout_reset_sbt` 标志。

## 返回值

如果成功，`cv_wait_sig`、`cv_timedwait` 和 `cv_timedwait_sig` 返回 0。否则返回非零错误代码。

`cv_wmesg` 返回传递给 `cv_init` 的描述字符串。

## 错误

`cv_wait_sig` 和 `cv_timedwait_sig` 在以下情况失败：

**[`EINTR`]** 捕获到信号，系统调用应被中断。

**[`ERESTART`]** 捕获到信号，系统调用应被重启。

`cv_timedwait` 和 `cv_timedwait_sig` 在以下情况失败：

**[`EWOULDBLOCK`]** 超时已到。

## 参见

[callout(9)](callout.9.md), [locking(9)](locking.9.md), [mtx_pool(9)](mtx_pool.9.md), [mutex(9)](mutex.9.md), [rwlock(9)](rwlock.9.md), [sema(9)](sema.9.md), [sleep(9)](sleep.9.md), [sx(9)](sx.9.md)
