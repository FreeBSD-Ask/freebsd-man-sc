# get_cyclecount.9

`get_cyclecount` — 获取 CPU 的快速计数器寄存器内容

## 名称

`get_cyclecount`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/systm.h>
```

```c
#include <machine/cpu.h>
```

```c
uint64_t
get_cyclecount(void)
```

## 描述

`get_cyclecount` 函数使用大多数现代 CPU 中可用的寄存器返回一个在每个 CPU 内单调递增的值。

在 SMP 系统上，会有若干独立的单调序列，每个运行的 CPU 一个。SMP 情况下的值从这些序列之一中选择，取决于哪个 CPU 被调度来服务请求。

每个计数器的速度和最大值取决于 CPU。某些 CPU（如 Intel 80486）没有这样的寄存器，因此在这些平台上 `get_cyclecount` 返回由 `binuptime(9)` 返回的结构所表示的数字的（单调）组合。

AMD64 和 Intel 64 处理器使用 `TSC` 寄存器。

## 参见

`binuptime(9)`

## 历史

`get_cyclecount` 函数首次出现于 FreeBSD 5.0。

## 作者

本手册页由 Mark Murray <markm@FreeBSD.org> 编写。
