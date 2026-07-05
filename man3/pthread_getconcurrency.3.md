# pthread_getconcurrency.3

`pthread_getconcurrency` — 获取或设置并发级别

## 名称

`pthread_getconcurrency`, `pthread_setconcurrency`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_getconcurrency(void);

int
pthread_setconcurrency(int new_level);
```

## 描述

`pthread_setconcurrency` 函数允许应用程序向线程实现告知其期望的并发级别 `new_level`。该函数调用后实现所提供的实际并发级别未定义。如果 `new_level` 为零，实现将自行决定维持并发级别，如同从未调用过 `pthread_setconcurrency`。`pthread_getconcurrency` 函数返回先前调用 `pthread_setconcurrency` 函数所设置的值。如果先前未调用过 `pthread_setconcurrency` 函数，该函数返回零以指示实现正在自行维持并发级别。应用程序调用 `pthread_setconcurrency` 时，是在向实现告知其期望的并发级别。实现仅将其作为提示，而非要求。

## 返回值

如果成功，`pthread_setconcurrency` 函数返回零；否则返回一个错误号以指示错误。`pthread_getconcurrency` 函数总是返回先前调用 `pthread_setconcurrency` 所设置的并发级别。如果从未调用过 `pthread_setconcurrency` 函数，`pthread_getconcurrency` 返回零。

## 错误

`pthread_setconcurrency` 函数将在以下情况失败：

**`[EINVAL]`** `new_level` 指定的值为负数。

**`[EAGAIN]`** `new_level` 指定的值将导致超出系统资源限制。

## 应用程序使用说明

使用这些函数会改变应用程序所依赖的底层并发状态。建议库开发者不要使用 `pthread_getconcurrency` 和 `pthread_setconcurrency` 函数，因为其使用可能与应用程序对这些函数的使用产生冲突。

## 标准

`pthread_getconcurrency` 和 `pthread_setconcurrency` 函数符合 -susv2 规范。
