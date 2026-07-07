# putwc.3

`fputwc` — 向流输出宽字符

## 名称

`fputwc`, `putwc`, `putwchar`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft wint_t Fn fputwc wchar_t wc FILE *stream Ft wint_t Fn putwc wchar_t wc FILE *stream Ft wint_t Fn putwchar wchar_t wc`

## 描述

`fputwc` 函数将宽字符 `wc` 写入 `stream` 所指向的输出流。

`putwc` 函数的作用与 `fputwc` 基本相同。

`putwchar` 函数等价于以 `stdout` 为输出流的 `putwc`。

## 返回值

`fputwc`、`putwc` 和 `putwchar` 函数返回写入的宽字符。如果发生错误，返回 `WEOF`。

## 参见

[ferror(3)](ferror.3.md), [fopen(3)](fopen.3.md), [getwc(3)](getwc.3.md), [putc(3)](putc.3.md), [stdio(3)](stdio.3.md)

## 标准

`fputwc`、`putwc` 和 `putwchar` 函数遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。
