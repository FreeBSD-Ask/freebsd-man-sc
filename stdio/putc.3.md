# putc(3)

`fputc` — 向流输出字符或字

## 名称

`fputc`, `fputc_unlocked`, `putc`, `putc_unlocked`, `putchar`, `putchar_unlocked`, `putw`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fputc int c FILE *stream Ft int Fn fputc_unlocked int c FILE *stream Ft int Fn putc int c FILE *stream Ft int Fn putc_unlocked int c FILE *stream Ft int Fn putchar int c Ft int Fn putchar_unlocked int c Ft int Fn putw int w FILE *stream`

## 描述

`fputc` 函数将字符 `c`（转换为 `unsigned char`）写入 `stream` 所指向的输出流。

`putc` 宏的作用与 `fputc` 基本相同，但它是内联展开的宏。它可能多次求值 `stream`，因此传递给 `putc` 的参数不应是具有潜在副作用的表达式。

`putchar` 函数等价于以 `stdout` 为输出流的 `putc`。

`putw` 函数将指定的 `int` 写入指定的输出 `stream`。

`fputc_unlocked`、`putc_unlocked` 和 `putchar_unlocked` 函数分别等价于 `fputc`、`putc` 和 `putchar`，区别在于调用者在调用它们之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。这些函数可用于避免为每个字符锁定流的开销，并避免输出分散在向同一流写入的多个线程中。

## 返回值

`fputc`、`putc`、`putchar`、`putc_unlocked` 和 `putchar_unlocked` 函数返回写入的字符。如果发生错误，返回 `EOF`。`putw` 函数成功时返回 0；发生写入错误或尝试写入只读流时返回 `EOF`。

## 参见

[ferror(3)](ferror.3.md), [flockfile(3)](flockfile.3.md), [fopen(3)](fopen.3.md), [getc(3)](getc.3.md), [putwc(3)](putwc.3.md), [stdio(3)](stdio.3.md)

## 标准

`fputc`、`putc` 和 `putchar` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。`putc_unlocked` 和 `putchar_unlocked` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。`putw` 函数出现于 Version 6 AT&T UNIX。

## 缺陷

`int` 的大小和字节序因机器而异，不建议在可移植应用程序中使用 `putw`。
