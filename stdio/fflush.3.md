# fflush(3)

`fflush` — 刷新流

## 名称

`fflush`, `fflush_unlocked`, `fpurge`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fflush FILE *stream Ft int Fn fflush_unlocked FILE *stream Ft int Fn fpurge FILE *stream`

## 描述

`fflush` 函数强制通过流底层写函数写入给定输出或更新 `stream` 的所有缓冲数据。流的打开状态不受影响。

如果 `stream` 参数为 `NULL`，`fflush` 刷新*所有*打开的输出流。

`fflush_unlocked` 函数等价于 `fflush`，区别在于调用者在调用它之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。此函数可用于避免锁定流的开销，并防止多个线程操作同一流时出现竞争。

`fpurge` 函数擦除给定 `stream` 中缓冲的所有输入或输出。对于输出流，这会丢弃所有未写入的输出。对于输入流，这会丢弃从底层对象读取但尚未通过 [getc(3)](getc.3.md) 获取的所有输入；这包括通过 [ungetc(3)](ungetc.3.md) 推回的任何文本。

## 返回值

成功完成时返回 0。否则返回 `EOF`，并设置全局变量 `errno` 以指示错误。

## 错误

**`EBADF`** `stream` 参数不是打开的流。

`fflush` 函数也可能失败，并为 [write(2)](../sys/write.2.md) 例程所指定的任何错误设置 `errno`，但如果 `stream` 是只读描述符，`fflush` 返回 0。

## 参见

[write(2)](../sys/write.2.md), [fclose(3)](fclose.3.md), [fopen(3)](fopen.3.md), [setbuf(3)](setbuf.3.md)

## 标准

`fflush` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 历史

`fflush` 函数首次出现于 Version 4 AT&T UNIX。`fpurge` 函数首次出现于 4.4BSD。
