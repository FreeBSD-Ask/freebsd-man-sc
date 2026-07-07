# pthread_mutexattr(3)

`pthread_mutexattr_init` — mutex 属性操作

## 名称

`pthread_mutexattr_init`, `pthread_mutexattr_destroy`, `pthread_mutexattr_setprioceiling`, `pthread_mutexattr_getprioceiling`, `pthread_mutexattr_setprotocol`, `pthread_mutexattr_getprotocol`, `pthread_mutexattr_setpshared`, `pthread_mutexattr_getpshared`, `pthread_mutexattr_setrobust`, `pthread_mutexattr_getrobust`, `pthread_mutexattr_settype`, `pthread_mutexattr_gettype`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutexattr_init(pthread_mutexattr_t *attr);

int
pthread_mutexattr_destroy(pthread_mutexattr_t *attr);

int
pthread_mutexattr_setprioceiling(pthread_mutexattr_t *attr,
    int prioceiling);

int
pthread_mutexattr_getprioceiling(const pthread_mutexattr_t *attr,
    int *prioceiling);

int
pthread_mutexattr_setprotocol(pthread_mutexattr_t *attr,
    int protocol);

int
pthread_mutexattr_getprotocol(const pthread_mutexattr_t *restrict attr,
    int *restrict protocol);

int
pthread_mutexattr_setpshared(pthread_mutexattr_t *attr,
    int shared);

int
pthread_mutexattr_getpshared(const pthread_mutexattr_t *attr,
    int *shared);

int
pthread_mutexattr_setrobust(pthread_mutexattr_t *attr,
    int robust);

int
pthread_mutexattr_getrobust(pthread_mutexattr_t *attr,
    int *robust);

int
pthread_mutexattr_settype(pthread_mutexattr_t *attr,
    int type);

int
pthread_mutexattr_gettype(const pthread_mutexattr_t *restrict attr,
    int *restrict type);
```

## 描述

mutex 属性用于为 `pthread_mutex_init` 指定参数。一个属性对象可在多次调用 `pthread_mutex_init` 时使用，每次调用之间可对其进行修改或不修改。

`pthread_mutexattr_init` 函数以所有默认的 mutex 属性初始化 `attr`。

`pthread_mutexattr_destroy` 函数销毁 `attr`。

`pthread_mutexattr_setprioceiling` 函数设置 mutex 的优先级上限，供在 `PTHREAD_PRIO_PROTECT` 协议下执行的线程使用。

`pthread_mutexattr_setprotocol` 函数指定使用 mutex 时应遵循的协议。`protocol` 参数可取以下值之一：

**`PTHREAD_PRIO_NONE`** 持有该 mutex 的线程的优先级和调度不受其持有 mutex 的影响。

**`PTHREAD_PRIO_INHERIT`** 请求优先级继承协议，持有该 mutex 的线程将在所有等待该线程持有的任意 mutex 的线程的最高优先级下执行。

**`PTHREAD_PRIO_PROTECT`** 请求优先级继承协议，持有该 mutex 的线程将在所有等待该线程持有的任意 mutex 的线程的优先级或优先级上限中的最高者优先级下执行。

`pthread_mutexattr_setpshared` 函数将 `attr` 的进程共享属性设置为 `pshared` 指定的值。`pshared` 参数可取以下值之一：

**`PTHREAD_PROCESS_PRIVATE`** 该 mutex 只能由创建该对象的进程中的线程使用。

**`PTHREAD_PROCESS_SHARED`** 该 mutex 可由创建该对象的进程以外的其他进程中的线程使用，前提是其他进程共享对该 mutex 所在内存的访问。

有关共享 mutex 的实现细节及其限制，请参见 libthr(3)。

`pthread_mutexattr_setrobust` 函数指定 mutex 的健壮性属性。`robust` 参数的可能取值为：

**`PTHREAD_MUTEX_STALLED`** 如果持有 mutex 的线程在未解锁的情况下终止，不采取任何特殊操作。如果没有其他线程能解锁该 mutex，可能导致死锁。此为默认值。

**`PTHREAD_MUTEX_ROBUST`** 如果持有 robust mutex 的进程或线程在持有 mutex 锁时终止，下一个获取该 mutex 的线程会通过加锁函数的返回值 `EOWNERDEAD` 收到终止通知。随后，可以使用 [pthread_mutex_consistent(3)](pthread_mutex_consistent.3.md) 修复 mutex 锁的状态，或者使用 [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md) 解锁 mutex 锁，但同时会使其进入不可用状态，此后所有获取该锁的尝试都将返回 `ENOTRECOVERABLE` 错误。

`pthread_mutexattr_settype` 函数设置 mutex 的类型。类型会影响加锁和解锁 mutex 的调用行为。`type` 参数的可能取值为：

**`PTHREAD_MUTEX_NORMAL`** 递归加锁以及当前线程未持有锁时解锁，都会使相应函数返回错误。这与 `PTHREAD_MUTEX_ERRORCHECK` 行为一致，但在某种程度上与 POSIX 规定的行为相矛盾。

**`PTHREAD_MUTEX_ERRORCHECK`** 递归加锁以及当前线程未持有锁时解锁，都会使相应函数返回错误。

**`PTHREAD_MUTEX_RECURSIVE`** 允许递归加锁。当前线程不是锁的所有者时尝试解锁将返回错误。

**`PTHREAD_MUTEX_DEFAULT`** FreeBSD 实现将该类型映射为 `PTHREAD_MUTEX_ERRORCHECK` 类型。

`pthread_mutexattr_get*` 函数将各函数名对应属性的值复制到第二个函数参数所指向的位置。

## 返回值

如果成功，这些函数返回 0。否则返回一个错误编号以指示错误。

## 错误

`pthread_mutexattr_init` 函数在以下情况下将失败：

**`[ENOMEM]`** 内存不足。

`pthread_mutexattr_destroy` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_mutexattr_setprioceiling` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效，或 `prioceiling` 的值无效。

`pthread_mutexattr_getprioceiling` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_mutexattr_setprotocol` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效，或 `protocol` 的值无效。

`pthread_mutexattr_getprotocol` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_mutexattr_setpshared` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效，或 `shared` 的值无效。

`pthread_mutexattr_getpshared` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_mutexattr_settype` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效，或 `type` 的值无效。

`pthread_mutexattr_gettype` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_mutexattr_setrobust` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效，或 `robust` 的值无效。

`pthread_mutexattr_getrobust` 函数在以下情况下将失败：

**`[EINVAL]`** `attr` 的值无效。

## 参见

libthr(3), [pthread_mutex_init(3)](pthread_mutex_init.3.md)

## 标准

`pthread_mutexattr_init` 和 `pthread_mutexattr_destroy` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。

`pthread_mutexattr_setprioceiling`、`pthread_mutexattr_getprioceiling`、`pthread_mutexattr_setprotocol`、`pthread_mutexattr_getprotocol`、`pthread_mutexattr_setpshared`、`pthread_mutexattr_getpshared`、`pthread_mutexattr_settype` 和 `pthread_mutexattr_gettype` 函数遵循 Version 2 of the Single UNIX Specification (“SUSv2”) 标准。`pthread_mutexattr_setrobust` 和 `pthread_mutexattr_getrobust` 函数遵循 IEEE Std 1003.1-2008 (“POSIX.1”) 标准。
