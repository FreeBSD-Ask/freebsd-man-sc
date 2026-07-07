# sem_getvalue(3)

`sem_getvalue` — 获取信号量的值

## 名称

`sem_getvalue`

## 库

Lb libc

## 概要

`#include <semaphore.h>`

```c
int
sem_getvalue(sem_t *restrict sem, int *restrict sval);
```

## 描述

`sem_getvalue` 函数将 `sval` 所指向的变量设置为 `sem` 所指向信号量的当前值，该值为调用 `sem_getvalue` 时实际运行的值。

## 返回值

若成功完成，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sem_getvalue` 函数在以下情况下会失败：

**[`EINVAL`]** `sem` 参数指向一个无效的信号量。

## 参见

[sem_post(3)](sem_post.3.md), sem_trywait(3), [sem_wait(3)](sem_wait.3.md)

## 标准

`sem_getvalue` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。

信号量的值永远不会为负数，即使有线程阻塞在该信号量上。POSIX 对于存在阻塞等待线程时信号量的值应该是什么的表述有些模糊，但鉴于规范的措辞，此行为是符合标准的。
