# ungetc(3)

`ungetc` — 从输入流中回退字符

## 名称

`ungetc`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn ungetc int c FILE *stream`

## 描述

`ungetc` 函数将字符 `c`（转换为 `unsigned char`）回退到 `stream` 所指向的输入流中。回退的字符将由后续对该流的读取按相反顺序返回。使用同一流，对文件定位函数（fseek、fsetpos(3) 或 rewind(3)）的成功介入调用将丢弃回退的字符。

保证支持一个字符的回退，但只要有足够内存，实际上允许无限量的回退。

如果字符成功回退，流的文件末尾指示器将被清除。每次成功调用 `ungetc` 都会使文件位置指示器递减；若调用前其值为 0，则调用后其值未指定。

## 返回值

`ungetc` 函数返回转换后回退的字符，若操作失败则返回 `EOF`。若参数 `c` 的值等于 `EOF`，操作将失败，流保持不变。

## 参见

[fseek(3)](fseek.3.md), [getc(3)](getc.3.md), setvbuf(3), [ungetwc(3)](ungetwc.3.md)

## 标准

`ungetc` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。
