# fputws(3)

`fputws` — 向流输出一行宽字符

## 名称

`fputws`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft int Fn fputws const wchar_t * restrict ws FILE * restrict fp`

## 描述

`fputws` 函数将 `ws` 所指向的宽字符串写入 `fp` 所指向的流。

## 返回值

`fputws` 函数成功时返回 0，出错时返回 -1。

## 错误

`fputws` 函数在以下情况失败：

**`EBADF`** 提供的 `fp` 参数不是可写流。

`fputws` 函数也可能失败并为 [write(2)](../man2/write.2.md) 例程指定的任何错误设置 `errno`。

## 参见

[ferror(3)](ferror.3.md), [fputs(3)](fputs.3.md), [putwc(3)](putwc.3.md), [stdio(3)](stdio.3.md)

## 标准

`fputws` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。
