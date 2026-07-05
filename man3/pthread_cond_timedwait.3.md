# pthread_cond_timedwait.3

`pthread_cond_timedwait` — 在指定时间内等待条件变量

## 名称

`pthread_cond_timedwait`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_cond_timedwait(pthread_cond_t *cond,
    pthread_mutex_t *mutex, const struct timespec *abstime);
```

## 描述

`pthread_cond_timedwait` 函数以原子方式阻塞当前线程，使其等待由 `cond` 指定的条件变量，并释放由 `mutex` 指定的互斥锁。等待线程只有在另一个线程针对同一条件变量调用 [pthread_cond_signal(3)](pthread_cond_signal.3.md) 或 [pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md)，或者系统时间到达 `abstime` 所指定的时刻，并且当前线程重新获取 `mutex` 上的锁之后，才会被唤醒。

可在创建条件变量时使用 pthread_condattr_setclock(3) 指定用于度量 `abstime` 的时钟。

## 返回值

如果成功，`pthread_cond_timedwait` 函数将返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_cond_timedwait` 函数将在以下情况失败：

**`[EINVAL]`** 由 `cond`、`mutex` 或 `abstime` 指定的值无效。

**`[ETIMEDOUT]`** 系统时间已到达或超过 `abstime` 所指定的时刻。

**`[EPERM]`** 指定的 `mutex` 未被调用线程锁定。

## 参见

[pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md), pthread_condattr_setclock(3)

## 标准

`pthread_cond_timedwait` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
