# funopen.3

`funopen` — 打开流

## 名称

`funopen`, `fropen`, `fwopen`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft FILE * Fn funopen const void *cookie int (*readfn)(void *, char *, int) int (*writefn)(void *, const char *, int) fpos_t (*seekfn)(void *, fpos_t, int) int (*closefn)(void *) Ft FILE * Fn fropen void *cookie int (*readfn)(void *, char *, int) Ft FILE * Fn fwopen void *cookie int (*writefn)(void *, const char *, int)`

## 描述

`funopen` 函数将流与最多四个“I/O 函数”关联。必须指定 `readfn` 或 `writefn` 之一；其他函数可以传递适当类型的 `NULL` 指针。这些 I/O 函数将用于读取、写入、定位和关闭新流。

通常，省略某个函数意味着对生成的流执行相应操作的任何尝试都将失败。若省略关闭函数，关闭流时将刷新所有缓冲输出然后成功返回。

`readfn`、`writefn`、`seekfn` 和 `closefn` 的调用约定必须分别与 [read(2)](../man2/read.2.md)、[write(2)](../man2/write.2.md)、[lseek(2)](../man2/lseek.2.md) 和 [close(2)](../man2/close.2.md) 匹配，唯一区别是传递给它们的 `cookie` 参数（在 `funopen` 中指定）替代了传统的文件描述符参数。

读写 I/O 函数允许通过调用 setvbuf(3) 更改全缓冲或行缓冲流的底层缓冲区。它们也不必完全填满或清空缓冲区。但不允许将流从无缓冲改为缓冲，也不允许更改行缓冲标志的状态。它们还必须准备应对在最近指定缓冲区之外的其他缓冲区上发生读取或写入调用的情况。

所有用户 I/O 函数都可以通过返回 -1 报告错误。此外，所有函数在发生错误时应适当设置外部变量 `errno`。

`closefn` 发生错误时不会使流保持打开状态。

为方便使用，头文件

`#include <stdio.h>`

将 `fropen` 和 `fwopen` 宏定义为仅指定读或写函数的 `funopen` 调用。

## 返回值

成功完成时，`funopen` 返回 `FILE` 指针。否则返回 `NULL`，并设置全局变量 `errno` 以指示错误。

## 错误

**`EINVAL`** 调用 `funopen` 函数时未指定读或写函数。

`funopen` 函数也可能失败并为 malloc(3) 例程指定的任何错误设置 `errno`。

## 参见

[fcntl(2)](../man2/fcntl.2.md), [open(2)](../man2/open.2.md), [fclose(3)](fclose.3.md), [fopen(3)](fopen.3.md), [fopencookie(3)](fopencookie.3.md), [fseek(3)](fseek.3.md), [setbuf(3)](setbuf.3.md)

## 历史

`funopen` 函数首次出现于 4.4BSD。

## 缺陷

`funopen` 函数可能无法移植到 BSD 以外的系统。

`funopen` 接口错误地假设 `fpos_t` 是整型；参见 [fseek(3)](fseek.3.md) 中对该问题的讨论。
