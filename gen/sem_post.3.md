# sem_post(3)

`sem_post` — 增加（解锁）信号量

## 名称

`sem_post`

## 库

Lb libc

## 概要

```c
#include <semaphore.h>

int
sem_post(sem_t *sem);
```

## 描述

`sem_post()` 函数增加（解锁） `sem` 所指向的信号量。如果在调用 `sem_post()` 时有线程阻塞在该信号量上，那么在信号量上阻塞时间最长的最高优先级线程将被允许从 `sem_wait()` 返回。

`sem_post()` 函数是信号可重入的，可以在信号处理函数中调用。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_post()` 函数在以下情况下会失败：

**`[EINVAL]`** `sem` 参数指向一个无效的信号量。

**`[EOVERFLOW]`** 信号量的值将超过 `SEM_VALUE_MAX`。

## 参见

[sem_getvalue(3)](sem_getvalue.3.md), sem_trywait(3), [sem_wait(3)](sem_wait.3.md)

## 标准

`sem_post()` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
