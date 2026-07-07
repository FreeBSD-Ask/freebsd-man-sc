# getc(3)

`fgetc` — 从输入流中获取下一个字符或字

## 名称

`fgetc`, `getc`, `getc_unlocked`, `getchar`, `getchar_unlocked`, `getw`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fgetc FILE *stream Ft int Fn getc FILE *stream Ft int Fn getc_unlocked FILE *stream Ft int Fn getchar void Ft int Fn getchar_unlocked void Ft int Fn getw FILE *stream`

## 描述

`fgetc` 函数从 `stream` 所指向的流中获取下一个输入字符（如果有），或获取通过 [ungetc(3)](ungetc.3.md) 推回流中的下一个字符。

`getc` 函数的作用与 `fgetc` 基本相同，但它是内联展开的宏。

`getchar` 函数等价于以 `stdin` 为参数的 `getc`。

`getw` 函数从 `stream` 所指向的流中获取下一个 `int`（如果有）。

`getc_unlocked` 和 `getchar_unlocked` 函数分别等价于 `getc` 和 `getchar`，区别在于调用者在调用它们之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。这些函数可用于避免为每个字符锁定流的开销，并避免输入分散在从同一流读取的多个线程中。

## 返回值

成功时，这些例程从 `stream` 返回下一个请求的对象。字符值以 `unsigned char` 转换为 `int` 的形式返回。如果流处于文件末尾或发生读取错误，例程返回 `EOF`。必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来区分文件末尾和错误。发生错误时，全局变量 `errno` 被设置以指示错误。文件末尾条件会被记住，即使在终端上也是如此，所有后续的读取尝试都将返回 `EOF`，直到用 clearerr(3) 清除该条件。

## 参见

[ferror(3)](ferror.3.md), [flockfile(3)](flockfile.3.md), [fopen(3)](fopen.3.md), [fread(3)](fread.3.md), [getwc(3)](getwc.3.md), [putc(3)](putc.3.md), [ungetc(3)](ungetc.3.md)

## 标准

`fgetc`、`getc` 和 `getchar` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。`getc_unlocked` 和 `getchar_unlocked` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`getc` 和 `getw` 函数以类似形式出现于 Version 1 AT&T UNIX，并在 Version 7 AT&T UNIX 中集成到 stdio；`getchar` 出现于 Version 4 AT&T UNIX；`fgetc` 出现于 Version 7 AT&T UNIX。

## 缺陷

由于 `EOF` 是一个有效的整数值，在调用 `getw` 后必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来检查是否失败。`int` 的大小和字节序因机器而异，不建议在可移植应用程序中使用 `getw`。
