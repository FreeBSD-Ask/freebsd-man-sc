# pthread_cond_wait(3)

`pthread_cond_wait` — 等待条件变量

## 名称

`pthread_cond_wait`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_cond_wait(pthread_cond_t *restrict cond,
    pthread_mutex_t *restrict mutex);
```

## 描述

`pthread_cond_wait` 函数以原子方式阻塞当前线程，使其等待由 `cond` 指定的条件变量，并释放由 `mutex` 指定的互斥锁。等待线程只有在另一个线程针对同一条件变量调用 [pthread_cond_signal(3)](pthread_cond_signal.3.md) 或 [pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md)，并且当前线程重新获取 `mutex` 上的锁之后，才会被唤醒。

## 返回值

如果成功，`pthread_cond_wait` 函数将返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_cond_wait` 函数将在以下情况失败：

**`[EINVAL]`** 由 `cond` 指定的值或由 `mutex` 指定的值无效。

**`[EPERM]`** 指定的 `mutex` 未被调用线程锁定。

**`[EOWNERDEAD]`** 参数 `mutex` 指向一个健壮互斥锁，且包含原持有线程的进程在持有该互斥锁时终止。锁被授予调用者，由新所有者负责使状态恢复一致。

**`[ENOTRECOVERABLE]`** 由 `mutex` 保护的状态不可恢复。

## 参见

[pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_mutex_consistent(3)](pthread_mutex_consistent.3.md)

## 标准

`pthread_cond_wait` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
