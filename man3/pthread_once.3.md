# pthread_once.3

`pthread_once` — 动态包初始化

## 名称

`pthread_once`

## 库

libpthread

## 概要

```c
#include <pthread.h>

pthread_once_t once_control = PTHREAD_ONCE_INIT;

int
pthread_once(pthread_once_t *once_control,
    void (*init_routine)(void));
```

## 描述

进程中的任意线程首次以给定的 `once_control` 调用 `pthread_once` 时，将调用不带参数的 `init_routine`。后续以相同 `once_control` 对 `pthread_once` 的调用不会再调用 `init_routine`。从 `pthread_once` 返回时，可以保证 `init_routine` 已执行完毕。`once_control` 参数用于判断相关的初始化例程是否已被调用。

`pthread_once` 函数不是取消点。但如果 `init_routine` 是一个取消点且被取消，对 `once_control` 的影响等同于 `pthread_once` 从未被调用。

常量 `PTHREAD_ONCE_INIT` 由头文件

```c
#include <pthread.h>
```

定义。

如果 `once_control` 具有自动存储期或未由 `PTHREAD_ONCE_INIT` 初始化，`pthread_once` 的行为未定义。

## 返回值

如果成功，`pthread_once` 函数将返回零。否则返回一个错误编号以指示错误。

## 错误

无。

## 标准

`pthread_once` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
