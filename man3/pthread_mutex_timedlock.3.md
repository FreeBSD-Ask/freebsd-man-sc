# pthread_mutex_timedlock.3

`pthread_mutex_timedlock` — 锁定 mutex 且不无限期阻塞

## 名称

`pthread_mutex_timedlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

#include <time.h>

int
pthread_mutex_timedlock(pthread_mutex_t *restrict mutex,
    const struct timespec *restrict abs_timeout);
```

## 描述

`pthread_mutex_timedlock` 函数将锁定 `mutex`。如果 mutex 已被锁定，调用线程将阻塞，直至 mutex 可用或由 `abs_timeout` 指定的超时时间到达。超时时间为绝对时间，而非相对于当前时间。

## 返回值

如果成功，`pthread_mutex_timedlock` 将返回零，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_timedlock` 函数在以下情况下将失败：

**`[ENOTRECOVERABLE]`** `mutex` 创建时其协议属性值为 `PTHREAD_PRIO_PROTECT`，且调用线程的优先级高于 mutex 当前的优先级上限。

**`[EINVAL]`** 进程或线程本应阻塞，且 `abs_timeout` 指定的纳秒值小于零或大于等于 10 亿。

**`[EINVAL]`** `mutex` 参数无效。

**`[ETIMEDOUT]`** 在超时时间到达之前未能锁定 `mutex`。

**`[EAGAIN]`** 无法获取 `mutex`，因为已超出 `mutex` 的最大递归加锁次数。

**`[EDEADLK]`** 当前线程已持有 `mutex`。

**`[EOWNERDEAD]`** `mutex` 参数指向一个 robust mutex，且持有该 mutex 锁的前一线程所在进程在持有锁时终止。锁已授予调用者，由新所有者负责将状态恢复一致。

**`[ENOTRECOVERABLE]`** 由 `mutex` 保护的状态不可恢复。

## 参见

[pthread_mutex_consistent(3)](pthread_mutex_consistent.3.md), [pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_trylock(3)](pthread_mutex_trylock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md)

## 标准

`pthread_mutex_timedlock` 函数预期遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
