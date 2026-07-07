# sem_init(3)

`sem_init` — 初始化一个未命名信号量

## 名称

`sem_init`

## 库

Lb libc

## 概要

```c
#include <semaphore.h>

int
sem_init(sem_t *sem, int pshared, unsigned int value);
```

## 描述

`sem_init()` 函数将 `sem` 所指向的未命名信号量初始化为值 `value`。

`pshared` 的非零值指定一个可由多个进程共享的信号量，该信号量应位于共享内存区域中（参见 [mmap(2)](../sys/mmap.2.md)、[shm_open(2)](../sys/shm_open.2.md) 和 [shmget(2)](../sys/shmget.2.md)），任何对地址 `sem` 具有读写访问权限的进程都可以对 `sem` 执行信号量操作。

在成功调用 `sem_init()` 之后， `sem` 可作为参数用于后续对 [sem_wait(3)](sem_wait.3.md)、sem_trywait(3)、[sem_post(3)](sem_post.3.md) 和 [sem_destroy(3)](sem_destroy.3.md) 的调用。在成功调用 [sem_destroy(3)](sem_destroy.3.md) 之后， `sem` 参数不再有效。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_init()` 函数在以下情况下会失败：

**`[EINVAL]`** `value` 参数超过 `SEM_VALUE_MAX`。

**`[ENOSPC]`** 内存分配错误。

## 参见

[sem_destroy(3)](sem_destroy.3.md), [sem_getvalue(3)](sem_getvalue.3.md), [sem_post(3)](sem_post.3.md), sem_trywait(3), [sem_wait(3)](sem_wait.3.md)

## 标准

`sem_init()` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
