# sem_wait.3

`sem_wait` — 减少（锁定）信号量

## 名称

`sem_wait`, `sem_trywait`

## 库

libc

## 概要

`#include <semaphore.h>`

```c
int
sem_wait(sem_t *sem);

int
sem_trywait(sem_t *sem);
```

## 描述

`sem_wait` 函数减少（锁定） `sem` 所指向的信号量，但如果 `sem` 的值为零，则会阻塞，直到其值变为非零且可以被减少。

`sem_trywait` 函数仅在 `sem` 的值为非零时，减少（锁定） `sem` 所指向的信号量。否则，信号量不会被减少，并返回错误。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_wait` 和 `sem_trywait` 函数在以下情况下会失败：

**`[EINVAL]`** `sem` 参数指向一个无效的信号量。

此外，`sem_wait` 在以下情况下也会失败：

**`[EINTR]`** 一个信号中断了此函数。

此外，`sem_trywait` 在以下情况下也会失败：

**`[EAGAIN]`** 信号量的值为零，因此无法被减少。

## 参见

[sem_getvalue(3)](sem_getvalue.3.md), [sem_post(3)](sem_post.3.md), [sem_timedwait(3)](sem_timedwait.3.md)

## 标准

`sem_wait` 和 `sem_trywait` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
