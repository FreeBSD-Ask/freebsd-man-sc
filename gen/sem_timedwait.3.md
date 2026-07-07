# sem_timedwait(3)

`sem_timedwait` — 锁定信号量

## 名称

`sem_timedwait`, `sem_clockwait_np`

## 库

Lb libc

## 概要

```c
#include <semaphore.h>
#include <time.h>

int
sem_timedwait(sem_t * restrict sem,
    const struct timespec * restrict abs_timeout);

int
sem_clockwait_np(sem_t * restrict sem, clockid_t clock_id, int flags,
    const struct timespec * rqtp, struct timespec * rmtp);
```

## 描述

`sem_timedwait()` 函数锁定 `sem` 所引用的信号量，与 [sem_wait(3)](sem_wait.3.md) 函数相同。然而，如果信号量无法被锁定，且必须等待另一个进程或线程通过执行 [sem_post(3)](sem_post.3.md) 函数来解锁该信号量，则当指定的超时时间到期时，该等待将被终止。

当 `abs_timeout` 所指定的绝对时间过去时，超时到期，该时间由作为超时基准的时钟测量（即当该时钟的值等于或超过 `abs_timeout` 时），或者在调用时 `abs_timeout` 所指定的绝对时间已经过去。

注意，超时基于 `CLOCK_REALTIME` 时钟。

如果信号量可以立即锁定，则不检查 `abs_timeout` 的有效性。

`sem_clockwait_np()` 函数是 `sem_timedwait()` 的更灵活变体。`clock_id` 参数指定参考时钟。如果 `flags` 参数包含 `TIMER_ABSTIME`，则所请求的超时（`rqtp`）为绝对超时；否则，超时为相对超时。如果此函数因 `EINTR` 失败且超时为相对超时，非 `NULL` 的 `rmtp` 将被更新以包含间隔中剩余的时间量（即所请求的时间减去实际睡眠的时间）。绝对超时对 `rmtp` 无影响。`rqtp` 和 `rmtp` 可使用同一结构。

## 返回值

如果调用进程成功对 `sem` 所指定的信号量执行了锁定操作，这些函数返回零。如果调用不成功，信号量的状态不变，函数返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

这些函数在以下情况下会失败：

**`[EINVAL]`** `sem` 参数不引用有效的信号量，或者进程或线程将被阻塞，且 `abs_timeout` 参数指定的纳秒字段值小于零或大于等于 10 亿。

**`[ETIMEDOUT]`** 在指定的超时时间到期之前无法锁定信号量。

**`[EINTR]`** 一个信号中断了此函数。

## 参见

[sem_post(3)](sem_post.3.md), sem_trywait(3), [sem_wait(3)](sem_wait.3.md)

## 标准

`sem_timedwait()` 函数遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。`sem_clockwait_np()` 函数未由任何标准指定；在撰写本文时，它仅存在于 FreeBSD 中。

## 历史

`sem_timedwait()` 函数首次出现在 FreeBSD 5.0 中。`sem_clockwait_np()` 函数首次出现在 FreeBSD 11.1 中。
