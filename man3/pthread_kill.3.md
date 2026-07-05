# pthread_kill.3

`pthread_kill` — 向指定线程发送信号

## 名称

`pthread_kill`

## 库

libpthread

## 概要

```c
#include <pthread.h>
#include <signal.h>

int
pthread_kill(pthread_t thread, int sig);
```

## 描述

`pthread_kill` 函数向由 `thread` 指定的线程发送由 `sig` 指定的信号。如果 `sig` 为 0，仅执行错误检查，但不会实际发送信号。

## 返回值

如果成功，`pthread_kill` 返回 0；否则返回一个错误号。

## 错误

`pthread_kill` 函数将在以下情况失败：

**`[ESRCH]`** `thread` 是无效的线程 ID。

**`[EINVAL]`** `sig` 是无效或不支持的信号编号。

## 参见

kill(2), [pthread_self(3)](pthread_self.3.md), raise(3)

## 标准

`pthread_kill` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
