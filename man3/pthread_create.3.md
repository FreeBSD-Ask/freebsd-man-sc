# pthread_create.3

`pthread_create` — 创建新线程

## 名称

`pthread_create`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_create(pthread_t *restrict thread,
    const pthread_attr_t *restrict attr,
    void *(*start_routine)(void *), void *restrict arg);
```

## 描述

`pthread_create` 函数用于在一个进程中创建一个新线程，其属性由 `attr` 指定。如果 `attr` 为 `NULL`，则使用默认属性。如果 `attr` 指定的属性随后被修改，已创建线程的属性不受影响。成功完成后，`pthread_create` 会将所创建线程的 ID 存入 `thread` 所指定的位置。

新线程创建后即开始执行 `start_routine`，并以 `arg` 作为其唯一参数。如果 `start_routine` 返回，其效果等同于以 `start_routine` 的返回值作为退出状态隐式调用 `pthread_exit`。注意，最初调用 `main` 的线程与此不同：当它从 `main` 返回时，其效果等同于以 `main` 的返回值作为退出状态隐式调用 `exit`。

新线程的信号状态初始化如下：

- 信号掩码从创建线程继承。
- 新线程的待处理信号集为空。

## 返回值

如果成功，`pthread_create` 函数将返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_create` 函数可能返回以下任何错误：

**`[ENOMEM]`** 系统缺乏必要的资源来创建另一个线程。

**`[EAGAIN]`** 将超出系统对单个进程中线程总数的限制 `[PTHREAD_THREADS_MAX]`。

**`[EAGAIN]`** 将超出 `RACCT_NTHR` 限制；参见 racct(2)。

**`[EPERM]`** 调用者没有权限设置调度参数或调度策略。

**`[EINVAL]`** 由 `attr` 指定的值无效。

**`[EDEADLK]`** 由 `attr` 指定的 CPU 集合将导致该线程无法在任何 CPU 上运行。

**`[EFAULT]`** 由 `attr` 指定的栈基址无效，或内核无法将所需的初始数据放入栈中。

## 参见

cpuset_setaffinity(2), fork(2), racct(2), thr_new(2), [pthread_attr(3)](pthread_attr.3.md), [pthread_cancel(3)](pthread_cancel.3.md), [pthread_cleanup_pop(3)](pthread_cleanup_pop.3.md), [pthread_cleanup_push(3)](pthread_cleanup_push.3.md), [pthread_exit(3)](pthread_exit.3.md), [pthread_join(3)](pthread_join.3.md)

## 标准

`pthread_create` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
