# pthread_join(3)

`pthread_join` — 检查线程终止状态

## 名称

`pthread_join`, `pthread_peekjoin_np`, `pthread_timedjoin_np`, `pthread_tryjoin_np`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_join(pthread_t thread, void **value_ptr);
```

```c
#include <pthread_np.h>

int
pthread_peekjoin_np(pthread_t thread, void **value_ptr);

int
pthread_timedjoin_np(pthread_t thread, void **value_ptr,
    const struct timespec *abstime);

int
pthread_tryjoin_np(pthread_t thread, void **value_ptr);
```

## 描述

`pthread_join` 函数挂起调用线程的执行，直到目标 `thread` 终止，除非目标 `thread` 已经终止。

当以非 NULL 的 `value_ptr` 参数成功调用 `pthread_join` 返回时，终止线程传递给 `pthread_exit` 的值将被存入 `value_ptr` 所引用的位置。当 `pthread_join` 成功返回时，目标线程已经终止。多个线程同时调用 `pthread_join` 指定同一目标线程的结果未定义。如果调用 `pthread_join` 的线程被取消，则目标线程不会被分离。

`pthread_timedjoin_np` 函数等同于 `pthread_join` 函数，区别在于如果目标线程在指定的绝对时间过去之后仍未退出，它将返回 `[ETIMEDOUT]`。

`pthread_peekjoin_np` 仅查看指定线程的退出状态。如果该线程尚未退出，返回 `[EBUSY]` 错误。否则返回零，并可选择将线程退出值存入 `*value_ptr` 所指向的位置。目标线程保持未汇合状态，可再次作为 `pthread_join` 系列函数的参数使用。

`pthread_tryjoin_np` 函数在线程已经终止时将其汇合，与 `pthread_join` 相同。如果线程尚未终止，该函数返回 `[EBUSY]`。

已经退出但尚未被汇合的线程计入 `_POSIX_THREAD_THREADS_MAX` 限制。

## 返回值

如果成功，上述函数返回零；否则返回一个错误号以指示错误或特殊状况。

## 错误

`pthread_join`、`pthread_peekjoin_np` 和 `pthread_timedjoin_np` 函数将在以下情况失败：

**`[EINVAL]`** 实现检测到 `thread` 指定的值不引用一个可汇合的线程。

**`[ESRCH]`** 找不到与给定的线程 ID `thread` 相对应的线程。

**`[EDEADLK]`** 检测到死锁，或 `thread` 的值指定了调用线程自身。

**`[EOPNOTSUPP]`** 实现检测到另一个调用者已在等待 `thread`。

此外，`pthread_timedjoin_np` 函数将在以下情况失败：

**`[ETIMEDOUT]`** 在 `pthread_timedjoin_np` 等待线程退出期间，指定的绝对时间已过。

`pthread_peekjoin_np` 和 `pthread_tryjoin_np` 函数还将在以下情况失败：

**`[EBUSY]`** 指定的线程尚未退出。

## 参见

wait(2), [pthread(3)](pthread.3.md), [pthread_create(3)](pthread_create.3.md), [pthread_np(3)](pthread_np.3.md)

## 标准

`pthread_join` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。`pthread_timedjoin_np` 函数是首次出现于 FreeBSD 6.1 的 FreeBSD 扩展。`pthread_peekjoin_np` 函数是首次出现于 FreeBSD 13.0 的 FreeBSD 扩展。`pthread_tryjoin_np` 函数是首次出现于 FreeBSD 16.0 的 FreeBSD 扩展。
