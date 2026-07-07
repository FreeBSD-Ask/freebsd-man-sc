# thread_exit(9)

`thread_exit` — 放弃当前线程上下文

## 名称

`thread_exit`

## 概要

`#include <sys/param.h>`

`#include <sys/proc.h>`

`void thread_exit(void)`

## 描述

`thread_exit()` 函数实现线程关闭的机器无关前奏。它不会返回，并将导致调用 [mi_switch(9)](mi_switch.9.md) 来调度其他线程。

`thread_exit()` 安排释放线程的所有资源，特别是内核栈。

为保护 [runqueue(9)](runqueue.9.md)，调用 `thread_exit()` 时必须持有 `sched_lock` 互斥锁。

## 参见

[mi_switch(9)](mi_switch.9.md), [mutex(9)](mutex.9.md), [runqueue(9)](runqueue.9.md), [sleep(9)](sleep.9.md)
