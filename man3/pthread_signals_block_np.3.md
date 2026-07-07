# pthread_signals_block_np(3)

`pthread_signals_block_np` — 快速阻塞和解阻塞异步信号

## 名称

`pthread_signals_block_np`, `pthread_signals_unblock_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

void
pthread_signals_block_np(void)

void
pthread_signals_unblock_np(void)
```

## 描述

`pthread_signals_block_np` 和 `pthread_signals_unblock_np` 函数为用户程序提供了访问快速异步信号阻塞设施 sigfastblock(2) 的接口。

使用 `pthread_signals_block_np` 阻塞信号会禁用任何异步信号的递送，直到解除阻塞。信号阻塞建立了一个临界区，线程的执行流不能被转向信号处理函数。阻塞信号速度很快，通过向与内核建立的位置执行一次内存写入完成。

同步信号递送通常无法被阻塞，包括使用这些函数。

`pthread_signals_block_np` 建立的阻塞状态并不完全符合 POSIX。具体而言，在阻塞区段内执行的系统调用可能会在异步信号排队到线程时中止睡眠并返回 `EINTR`，但信号处理函数在最后一次解除阻塞之前不会被调用。

对 `pthread_signals_block_np` 的调用可以嵌套，必须配以同等数量的 `pthread_signals_unblock_np` 调用才能使调用线程返回到标准的信号接收模式。

这些函数的一个使用示例是构建无法原子化完成的 CPU 状态，其中包含线程状态不符合 ABI 的阶段。如果在此类状态尚未完成时递送信号，信号处理函数将行为异常。使用标准函数（`sigprocmask`）建立临界区可能要慢得多，因为 `sigprocmask` 是系统调用，而 `pthread_signals_block_np` 仅由一次原子内存写入组成。

## 返回值

这些函数不返回值。

## 错误

这些函数不报告任何错误。

## 参见

sigfastblock(2), sigprocmask(2), [pthread_sigmask(3)](pthread_sigmask.3.md), [pthread_np(3)](pthread_np.3.md)
