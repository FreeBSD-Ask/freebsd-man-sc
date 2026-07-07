# ungetwc(3)

`ungetwc` — 从输入流中回退宽字符

## 名称

`ungetwc`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft wint_t Fn ungetwc wint_t wc FILE *stream`

## 描述

`ungetwc` 函数将宽字符 `wc`（转换为 `wchar_t`）回退到 `stream` 所指向的输入流中。回退的宽字符将由后续对该流的读取按相反顺序返回。使用同一流，对文件定位函数 [fseek(3)](fseek.3.md)、fsetpos(3) 或 rewind(3) 的成功介入调用将丢弃回退的宽字符。

保证支持一个宽字符的回退，但只要有足够内存，实际上允许无限量的回退。

如果字符成功回退，流的文件末尾指示器将被清除。

## 返回值

`ungetwc` 函数返回转换后回退的宽字符，若操作失败则返回 `WEOF`。若参数 `c` 的值等于 `WEOF`，操作将失败，流保持不变。

## 参见

[fseek(3)](fseek.3.md), [getwc(3)](getwc.3.md)

## 标准

`ungetwc` 函数遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。
