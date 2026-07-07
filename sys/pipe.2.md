# pipe(2)

`pipe` — 创建用于进程间通信的描述符对

## 名称

`pipe`, `pipe2`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
pipe(int fildes[2]);

int
pipe2(int fildes[2], int flags);
```

## 描述

`pipe()` 函数创建一个 *管道*，这是一种允许双向数据流的对象，并分配一对文件描述符。

`pipe2()` 系统调用允许通过 `flags` 参数控制文件描述符的属性。`flags` 的值由以下列表中定义的标志按位或构造，定义于

`#include <fcntl.h>`

**`O_CLOEXEC`** 为新文件描述符设置 close-on-exec 标志。

**`O_CLOFORK`** 为新文件描述符设置 close-on-fork 标志。

**`O_NONBLOCK`** 为管道的两端设置非阻塞标志。

如果 `flags` 参数为 0，行为与调用 `pipe()` 相同。

按照惯例，第一个描述符通常用作管道的 *读端*，第二个通常用作 *写端*，因此写入 `fildes[1]` 的数据会出现在 `fildes[0]`（即可以从 `fildes[0]` 读取）。这允许将一个程序的输出发送给另一个程序：源的输出设置为管道的写端，接收方的标准输入设置为管道的读端。管道本身持续存在，直到所有与之关联的描述符都被关闭。

关闭了一端的管道被视为 *widowed*。在此类管道上写入会导致写入进程收到 `SIGPIPE` 信号。使管道 widowed 是向读取者传递文件结束的唯一方式：在读取者消费所有缓冲数据后，读取 widowed 管道返回零计数。

此管道实现的双向特性不可移植到较旧的系统，因此建议在单向使用管道时按传统方式使用端点。

## 实现说明

`pipe()` 函数调用 `pipe2()` 系统调用。因此，由 [dtrace(1)](../man1/dtrace.1.md) 或 [ktrace(1)](../man1/ktrace.1.md) 捕获的系统调用跟踪将显示对 `pipe2()` 的调用。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`pipe()` 和 `pipe2()` 系统调用将在以下情况下失败：

**[`EFAULT`]** `fildes` 参数指向无效的内存位置。

**[`EMFILE`]** 活动描述符过多。

**[`ENFILE`]** 系统文件表已满。

**[`ENOMEM`]** 没有足够的内核内存来建立管道。

`pipe2()` 系统调用还将在以下情况下失败：

**[`EINVAL`]** `flags` 参数无效。

## 参见

[sh(1)](../man1/sh.1.md), [fork(2)](fork.2.md), [read(2)](read.2.md), [socketpair(2)](socketpair.2.md), [write(2)](write.2.md)

## 历史

`pipe()` 函数出现于 Version 3 AT&T UNIX。

双向管道首次用于 AT&T System V Release 4 UNIX。

`pipe2()` 函数出现于 FreeBSD 10.0。

`pipe()` 函数在 FreeBSD 11.0 中成为 `pipe2()` 的包装。

`O_CLOFORK` 标志出现于 FreeBSD 15.0。
