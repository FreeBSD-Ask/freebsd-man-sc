# fclose(3)

`fclose` — 关闭流

## 名称

`fclose`, `fdclose`, `fcloseall`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fclose FILE *stream Ft int Fn fdclose FILE *stream int *fdp Ft void Fn fcloseall void`

## 描述

`fclose` 函数将指定的 `stream` 与其底层文件或函数集合解除关联。如果流用于输出，会先使用 [fflush(3)](fflush.3.md) 写入所有缓冲数据。

`fdclose` 函数等价于 `fclose`，区别在于它不关闭底层文件描述符。如果 `fdp` 不为 `NULL`，文件描述符将被写入其中。如果流没有关联的文件描述符，`fdp` 将被设置为 -1。此类流由 fmemopen(3)、[funopen(3)](funopen.3.md) 或 [open_memstream(3)](open_memstream.3.md) 等函数创建。

`fcloseall` 函数对所有打开的流调用 `fclose`。

## 返回值

`fcloseall` 不返回值。

`fclose` 和 `fdclose` 函数成功完成时返回 0。否则返回 `EOF`，并设置全局变量 `errno` 以指示错误。

## 错误

`fdclose` 在以下情况失败：

**`EOPNOTSUPP`** 流没有关联的文件描述符。

`fclose` 和 `fdclose` 函数也可能失败，并为 [fflush(3)](fflush.3.md) 所指定的任何错误设置 `errno`。

`fclose` 函数也可能失败，并为 [close(2)](../sys/close.2.md) 所指定的任何错误设置 `errno`。

## 注释

`fclose` 和 `fdclose` 函数不处理 `stream` 变量为 `NULL` 的参数；这将导致段错误。这是有意为之，便于确保在 FreeBSD 上编写的程序无缺陷。此行为属于实现细节，程序不应依赖于它。

## 参见

[close(2)](../sys/close.2.md), [fflush(3)](fflush.3.md), [fopen(3)](fopen.3.md), [setbuf(3)](setbuf.3.md)

## 标准

`fclose` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 历史

`fcloseall` 函数首次出现于 FreeBSD 7.0。

`fdclose` 函数首次出现于 FreeBSD 11.0。
