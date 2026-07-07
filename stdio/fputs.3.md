# fputs.3

`fputs` — 向流输出一行

## 名称

`fputs`, `fputs_unlocked`, `puts`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fputs const char *str FILE *stream Ft int Fn fputs_unlocked const char *str FILE *stream Ft int Fn puts const char *str`

## 描述

`fputs` 函数将 `str` 所指向的字符串写入 `stream` 所指向的流。

`fputs_unlocked` 函数等价于 `fputs`，区别在于调用者在调用它之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。该函数可用于避免锁定流的开销，并防止多个线程操作同一流时出现竞争。

`puts` 函数将字符串 `str` 及一个结束换行符写入流 `stdout`。

## 返回值

`fputs` 和 `puts` 函数成功时返回非负整数，出错时返回 `EOF`。

## 错误

**`EBADF`** `stream` 参数不是可写流。

`fputs` 和 `puts` 函数也可能失败并为 [write(2)](../man2/write.2.md) 例程指定的任何错误设置 `errno`。

## 参见

[ferror(3)](ferror.3.md), [fputws(3)](fputws.3.md), [putc(3)](putc.3.md), [stdio(3)](stdio.3.md)

## 标准

`fputs` 和 `puts` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。
