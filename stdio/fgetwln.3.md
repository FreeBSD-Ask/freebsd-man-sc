# fgetwln(3)

`fgetwln` — 从流中获取一行宽字符

## 名称

`fgetwln`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`#include <wchar.h>`

`Ft wchar_t * Fn fgetwln FILE * restrict stream size_t * restrict len`

## 描述

`fgetwln` 函数返回指向 `stream` 所引用流的下一行的指针。该行 **并非** 标准宽字符串，因为它不以终止空宽字符结尾。行的长度（包括最后的换行符）存储在 `len` 所指向的内存位置。（但注意，如果该行是文件中不以换行符结尾的最后一行，返回的文本将不包含换行符。）

## 返回值

成功完成时返回一个指针；该指针在 `stream` 上的下一次 I/O 操作（无论是否成功）后或流关闭后即变为无效。否则返回 `NULL`。`fgetwln` 函数不区分文件末尾和错误；必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来确定发生的是哪种情况。发生错误时，全局变量 `errno` 被设置以指示错误。文件末尾条件会被记住，即使在终端上也是如此，所有后续的读取尝试都将返回 `NULL`，直到用 clearerr(3) 清除该条件。

返回指针所指向的文本可以被修改，前提是不超过返回的大小进行更改。一旦指针变为无效，这些更改即丢失。

## 错误

**`EBADF`** 参数 `stream` 不是为读取而打开的流。

`fgetwln` 函数也可能失败并为 mbrtowc(3)、realloc(3) 或 [read(2)](../man2/read.2.md) 所指定的任何错误设置 `errno`。

## 参见

[ferror(3)](ferror.3.md), [fgetln(3)](fgetln.3.md), [fgetws(3)](fgetws.3.md), [fopen(3)](fopen.3.md)
