# pthread_equal(3)

`pthread_equal` — 比较线程 ID

## 名称

`pthread_equal`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_equal(pthread_t t1, pthread_t t2);
```

## 描述

`pthread_equal` 函数比较线程 ID `t1` 和 `t2`。

## 返回值

如果线程 ID `t1` 和 `t2` 对应同一个线程，`pthread_equal` 函数将返回非零值；否则返回零。

## 错误

无。

## 参见

[pthread_create(3)](pthread_create.3.md), [pthread_exit(3)](pthread_exit.3.md)

## 标准

`pthread_equal` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
