# open_memstream(3)

`open_memstream` — 动态内存缓冲区流打开函数

## 名称

`open_memstream`, `open_wmemstream`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft FILE * Fn open_memstream char **bufp size_t *sizep`

`#include <wchar.h>`

`Ft FILE * Fn open_wmemstream wchar_t **bufp size_t *sizep`

## 描述

`open_memstream` 和 `open_wmemstream` 函数创建一个由动态分配的内存缓冲区支持的只写、可定位流。`open_memstream` 函数创建面向字节的流，而 `open_wmemstream` 函数创建面向宽字符的流。

每个流维护当前位置和大小。初始时，位置和大小均设置为零。每次写入从当前位置开始，并将位置前进成功写入的字节数（对于 `open_memstream`）或宽字符数（对于 `open_wmemstream`）。如果写入使当前位置超出了缓冲区长度，缓冲区长度将被扩展，并在缓冲区末尾追加一个空字符。

流的缓冲区末尾始终包含一个空字符，该空字符不计入当前长度。

如果通过定位操作将流的当前位置移动到超出当前长度，并执行写入，则在写入之前，当前长度与当前位置之间的字符将用空字符填充。

成功调用 [fclose(3)](fclose.3.md) 或 [fflush(3)](fflush.3.md) 后，`bufp` 所引用的指针将包含内存缓冲区的起始地址，`sizep` 所引用的变量将包含当前位置和当前缓冲区长度中的较小值。

成功调用 [fflush(3)](fflush.3.md) 后，`bufp` 所引用的指针和 `sizep` 所引用的变量仅在下次写入操作或调用 [fclose(3)](fclose.3.md) 之前有效。

流关闭后，`bufp` 所引用的已分配缓冲区在不再需要时应通过调用 free(3) 释放。

## 实现说明

在内部，所有 I/O 流实际上都是面向字节的，因此使用面向宽字符的操作向通过 `open_wmemstream` 打开的流写入时，宽字符会在 stdio 的内部缓冲区中被扩展为多字节字符流。这些多字节字符在写入流时又被转换回宽字符。因此，面向宽字符的流维护着一个内部多字节字符转换状态，任何改变当前位置的定位操作都会清除该状态。只要在面向宽字符的流上使用面向宽字符的输出操作，这不会产生影响。

## 返回值

成功完成时，`open_memstream` 和 `open_wmemstream` 返回一个 `FILE` 指针。否则返回 `NULL`，并设置全局变量 `errno` 以指示错误。

## 错误

**`EINVAL`** `bufp` 或 `sizep` 参数为 `NULL`。

**`ENOMEM`** 无法为流或缓冲区分配内存。

## 参见

[fclose(3)](fclose.3.md), [fflush(3)](fflush.3.md), [fopen(3)](fopen.3.md), free(3), [fseek(3)](fseek.3.md), [stdio(3)](stdio.3.md), [sbuf(9)](../man9/sbuf.9.md)

## 标准

`open_memstream` 和 `open_wmemstream` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准。
