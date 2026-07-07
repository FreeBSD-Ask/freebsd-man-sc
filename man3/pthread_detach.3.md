# pthread_detach(3)

`pthread_detach` — 分离线程

## 名称

`pthread_detach`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_detach(pthread_t thread);
```

## 描述

`pthread_detach` 函数用于向实现指示：当线程 `thread` 终止时，可以回收该线程的存储资源。如果 `thread` 尚未终止，`pthread_detach` 不会导致其终止。对同一目标线程多次调用 `pthread_detach` 的效果未定义。

## 返回值

如果成功，`pthread_detach` 函数将返回零；否则将返回一个错误号以指示错误。注意，该函数不会像某些标准草案中那样改变 `errno` 的值。这些早期草案还将指向 pthread_t 的指针作为参数传递。务必注意！

## 错误

`pthread_detach` 函数将在以下情况失败：

**`[EINVAL]`** 实现检测到 `thread` 指定的值不引用一个可汇合的线程。

**`[ESRCH]`** 找不到与给定的线程 ID `thread` 相对应的线程。

## 参见

[pthread_join(3)](pthread_join.3.md)

## 标准

`pthread_detach` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
