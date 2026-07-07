# pthread_cond_init(3)

`pthread_cond_init` — 创建条件变量

## 名称

`pthread_cond_init`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_cond_init(pthread_cond_t *restrict cond,
    const pthread_condattr_t *restrict attr);
```

## 描述

`pthread_cond_init` 函数创建一个新的条件变量，其属性由 `attr` 指定。如果 `attr` 为 NULL，则使用默认属性。

## 返回值

如果成功，`pthread_cond_init` 函数将返回零，并将新的条件变量 ID 存入 `cond`；否则将返回一个错误号以指示错误。

## 错误

`pthread_cond_init` 函数将在以下情况失败：

**`[EINVAL]`** 由 `attr` 指定的值无效。

**`[ENOMEM]`** 进程无法分配足够的内存来创建另一个条件变量。

**`[EAGAIN]`** 系统暂时缺乏资源来创建另一个条件变量。

## 参见

[pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md), [pthread_condattr(3)](pthread_condattr.3.md)

## 标准

`pthread_cond_init` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
