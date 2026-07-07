# sched_getcpu(3)

`sched_getcpu` — 获取当前 CPU

## 名称

`sched_getcpu`

## 库

libc

## 概要

```c
#include <sched.h>

int
sched_getcpu(void);
```

## 描述

`sched_getcpu` 函数返回调用线程当前正在其上运行的 CPU。

## 返回值

`sched_getcpu` 返回调用时当前 CPU 的从 0 开始的索引。除非线程被绑定到特定 CPU，否则该值在返回后可能立即失效。CPU 编号与 cpuset(2) 及 CPU 亲和性调用所使用的编号相同。

`sched_getcpu` 不会失败，因此没有错误值。

## 参见

cpuset(2), cpuset_getaffinity(2), cpuset_setaffinity(2), pthread_getaffinity_np(3), pthread_setaffinity_np(3)

## 标准

`sched_getcpu` 函数源于 Linux。本实现旨在与 Linux 实现保持源码兼容。

## 历史

`sched_getcpu` 函数引入于 FreeBSD 13.1。
