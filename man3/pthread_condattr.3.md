# pthread_condattr(3)

`pthread_condattr_init` — 条件变量属性操作

## 名称

`pthread_condattr_init`, `pthread_condattr_destroy`, `pthread_condattr_getclock`, `pthread_condattr_setclock`, `pthread_condattr_getpshared`, `pthread_condattr_setpshared`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_condattr_init(pthread_condattr_t *attr);

int
pthread_condattr_destroy(pthread_condattr_t *attr);

int
pthread_condattr_getclock(const pthread_condattr_t * restrict attr,
    clockid_t * restrict clock_id);

int
pthread_condattr_setclock(pthread_condattr_t *attr, clockid_t clock_id);

int
pthread_condattr_getpshared(const pthread_condattr_t * restrict attr,
    int * restrict pshared);

int
pthread_condattr_setpshared(pthread_condattr_t *attr, int pshared);
```

## 描述

条件变量属性对象用于为 [pthread_cond_init(3)](pthread_cond_init.3.md) 指定参数。

`pthread_condattr_init` 函数以默认属性初始化一个条件变量属性对象。

`pthread_condattr_destroy` 函数销毁一个条件变量属性对象。

`pthread_condattr_getclock` 函数将 `attr` 中的时钟属性值存入 `clock_id` 所指向的内存区域。`pthread_condattr_setclock` 函数将 `attr` 的时钟属性设置为 `clock_id` 所指定的值。时钟属性影响 [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md) 中对 `abstime` 的解释，可设置为 `CLOCK_REALTIME`（默认）、`CLOCK_TAI` 或 `CLOCK_MONOTONIC`。

`pthread_condattr_getpshared` 函数将 `attr` 中的进程共享属性值存入 `pshared` 所指向的内存区域。`pthread_condattr_setpshared` 函数将 `attr` 的进程共享属性设置为 `pshared` 所指定的值。参数 `pshared` 可取以下值之一：

**`PTHREAD_PROCESS_PRIVATE`** 与之关联的条件变量只能被与创建该对象的线程处于同一进程中的线程访问。

**`PTHREAD_PROCESS_SHARED`** 与之关联的条件变量可被创建该对象的进程以外的其他进程中的线程访问。

有关共享条件变量的实现细节及其限制，参见 libthr(3)。

## 返回值

如果成功，这些函数返回 0；否则返回一个错误号以指示错误。

## 错误

`pthread_condattr_init` 函数将在以下情况失败：

**`[ENOMEM]`** 内存不足。

`pthread_condattr_destroy` 函数将在以下情况失败：

**`[EINVAL]`** `attr` 的值无效。

`pthread_condattr_setclock` 函数将在以下情况失败：

**`[EINVAL]`** `clock_id` 所指定的值不是允许的值之一。

`pthread_condattr_setpshared` 函数将在以下情况失败：

**`[EINVAL]`** `pshared` 所指定的值不是允许的值之一。

## 参见

libthr(3), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md)

## 标准

`pthread_condattr_init` 和 `pthread_condattr_destroy` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
