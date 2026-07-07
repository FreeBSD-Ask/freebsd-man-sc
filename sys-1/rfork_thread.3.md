# rfork_thread(3)

`rfork_thread` — 创建基于 rfork 的进程线程

## 名称

`rfork_thread`

## 库

libc

## 概要

```c
#include <unistd.h>

pid_t
rfork_thread(int flags, void *stack, int (*func)(void *arg),
    void *arg);
```

## 描述

`rfork_thread` 函数已弃用，推荐使用 [pthread_create(3)](../man3/pthread_create.3.md) 替代。

`rfork_thread` 函数是 rfork(2) 的辅助函数。它安排创建一个新进程，子进程将在所提供的栈上运行，并以指定参数调用指定函数。

使用该函数可避免实现复杂的栈切换代码。

## 返回值

成功完成时，`rfork_thread` 向父进程返回子进程的进程 ID。否则，向父进程返回 -1，不创建子进程，并设置全局变量 `errno` 以指示错误。

子进程上下文不会感知到从 `rfork_thread` 函数返回，因为它直接从所提供的函数开始执行。

## 错误

错误返回码参见 rfork(2)。

## 参见

fork(2), intro(2), minherit(2), rfork(2), vfork(2), [pthread_create(3)](../man3/pthread_create.3.md)

## 历史

`rfork_thread` 函数首次出现于 FreeBSD 4.3。
