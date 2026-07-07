# ferror(3)

`clearerr` — 检查并重置流状态

## 名称

`clearerr`, `clearerr_unlocked`, `feof`, `feof_unlocked`, `ferror`, `ferror_unlocked`, `fileno`, `fileno_unlocked`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft void Fn clearerr FILE *stream Ft void Fn clearerr_unlocked FILE *stream Ft int Fn feof FILE *stream Ft int Fn feof_unlocked FILE *stream Ft int Fn ferror FILE *stream Ft int Fn ferror_unlocked FILE *stream Ft int Fn fileno FILE *stream Ft int Fn fileno_unlocked FILE *stream`

## 描述

`clearerr` 函数清除 `stream` 所指向的流的文件末尾和错误指示器。

`feof` 函数测试 `stream` 所指向的流的文件末尾指示器，如果已设置则返回非零值。文件末尾指示器可通过显式调用 `clearerr` 清除，或作为其他操作（如 `fseek`）的副作用而被清除。

`ferror` 函数测试 `stream` 所指向的流的错误指示器，如果已设置则返回非零值。

`fileno` 函数检查参数 `stream` 并返回其整数描述符。

`clearerr_unlocked`、`feof_unlocked`、`ferror_unlocked` 和 `fileno_unlocked` 函数分别等价于 `clearerr`、`feof`、`ferror` 和 `fileno`，区别在于调用者在调用它们之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。这些函数可用于避免锁定流的开销，并防止多个线程操作同一流时出现竞争。

## 错误

这些函数（`fileno` 除外）不应失败，也不会设置外部变量 `errno`。

出错时，`fileno` 返回 -1，并将 `errno` 设置为以下值之一：

**`EBADF`** 流未与文件关联。

**`EBADF`** 流底层的文件描述符不是有效的文件描述符。注意，对此条件的检测并不可靠，可能不会报告该错误。

## 参见

[open(2)](../man2/open.2.md), fdopen(3), [flockfile(3)](flockfile.3.md), [stdio(3)](stdio.3.md)

## 标准

`clearerr`、`feof` 和 `ferror` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 历史

`clearerr`、`feof`、`ferror` 和 `fileno` 函数首次出现于 Version 7 AT&T UNIX。
