# getwc(3)

`fgetwc` — 从输入流中获取下一个宽字符

## 名称

`fgetwc`, `getwc`, `getwchar`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft wint_t Fn fgetwc FILE *stream Ft wint_t Fn getwc FILE *stream Ft wint_t Fn getwchar void`

## 描述

`fgetwc` 函数从 `stream` 所指向的流中获取下一个输入宽字符（如果有），或获取通过 [ungetwc(3)](ungetwc.3.md) 推回流中的下一个字符。

`getwc` 函数的作用与 `fgetwc` 基本相同。

`getwchar` 函数等价于以 `stdin` 为参数的 `getwc`。

## 返回值

成功时，这些例程从 `stream` 返回下一个宽字符。如果流处于文件末尾或发生读取错误，例程返回 `WEOF`。必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来区分文件末尾和错误。发生错误时，全局变量 `errno` 被设置以指示错误。文件末尾条件会被记住，即使在终端上也是如此，所有后续的读取尝试都将返回 `WEOF`，直到用 clearerr(3) 清除该条件。

## 参见

[ferror(3)](ferror.3.md), [fopen(3)](fopen.3.md), [fread(3)](fread.3.md), [getc(3)](getc.3.md), [putwc(3)](putwc.3.md), [stdio(3)](stdio.3.md), [ungetwc(3)](ungetwc.3.md)

## 标准

`fgetwc`、`getwc` 和 `getwchar` 函数遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。

## 历史

`getc` 和 `getw` 函数的一个版本出现于 Version 1 AT&T UNIX。
