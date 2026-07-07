# fgetws(3)

`fgetws` — 从流中获取一行宽字符

## 名称

`fgetws`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft wchar_t * Fn fgetws wchar_t * restrict ws int n FILE * restrict fp`

## 描述

`fgetws` 函数从给定的 `fp` 中读取最多比 `n` 指定数量少一个的字符，并将其存储在宽字符串 `ws` 中。读取在找到换行符、文件末尾或出错时停止。换行符（如果有）会被保留。如果读取了任何字符且没有错误，会追加一个 `'\0'` 字符以结束字符串。

## 返回值

成功完成时，`fgetws` 返回 `ws`。如果在读取任何字符之前到达文件末尾，`fgetws` 返回 `NULL`，缓冲区内容保持不变。如果发生错误，`fgetws` 返回 `NULL`，缓冲区内容不确定。`fgetws` 函数不区分文件末尾和错误，调用者必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来确定发生的是哪种情况。

## 错误

`fgetws` 函数在以下情况失败：

**`EBADF`** 给定的 `fp` 参数不是可读流。

**`EILSEQ`** 从输入流获取的数据不构成有效的多字节字符。

`fgetws` 函数也可能失败并为 [fflush(3)](fflush.3.md)、fstat(2)、[read(2)](../man2/read.2.md) 或 malloc(3) 所指定的任何错误设置 `errno`。

## 参见

feof(3), [ferror(3)](ferror.3.md), [fgets(3)](fgets.3.md)

## 标准

`fgetws` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。
