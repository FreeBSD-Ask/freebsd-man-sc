# fgets(3)

`fgets` — 从流中获取一行

## 名称

`fgets`, `gets_s`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft char * Fn fgets char * restrict str int size FILE * restrict stream Fd #define __STDC_WANT_LIB_EXT1__ 1 Ft char * Fn gets_s char *str rsize_t size`

## 描述

`fgets` 函数从给定的 `stream` 中读取最多比 `size` 指定数量少一个的字符，并将其存储在字符串 `str` 中。读取在找到换行符、文件末尾或出错时停止。换行符（如果有）会被保留。如果读取了任何字符且没有错误，会追加一个 `'\0'` 字符以结束字符串。

`gets_s` 函数等价于 `stream` 为 `stdin` 的 `fgets`，区别在于换行符（如果有）不会存储在字符串中。

`gets` 函数不安全，已不再可用。

## 返回值

成功完成时，`fgets` 和 `gets_s` 返回指向字符串的指针。如果在读取任何字符之前到达文件末尾，返回 `NULL`，缓冲区内容保持不变。如果发生错误，返回 `NULL`，缓冲区内容不确定。`fgets` 和 `gets_s` 函数不区分文件末尾和错误，调用者必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来确定发生的是哪种情况。

## 错误

**`EBADF`** 给定的 `stream` 不是可读流。

`fgets` 函数也可能失败并为 [fflush(3)](fflush.3.md)、fstat(2)、[read(2)](../sys/read.2.md) 或 malloc(3) 所指定的任何错误设置 `errno`。

`gets_s` 函数也可能失败并为 getchar(3) 所指定的任何错误设置 `errno`。

## 参见

feof(3), [ferror(3)](ferror.3.md), [fgetln(3)](fgetln.3.md), [fgetws(3)](fgetws.3.md), [getline(3)](getline.3.md)

## 标准

`fgets` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。`gets_s` 遵循 ISO/IEC 9899:2011 ("ISO C11") K.3.7.4.1。`gets` 已从 ISO/IEC 9899:2011 ("ISO C11") 中移除。

## 历史

`fgets` 和 `gets` 函数首次出现于 Version 7 AT&T UNIX。
