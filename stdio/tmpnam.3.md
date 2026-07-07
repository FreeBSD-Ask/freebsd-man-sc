# tmpnam(3)

`tempnam` — 临时文件例程

## 名称

`tempnam`, `tmpfile`, `tmpnam`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft FILE * Fn tmpfile void Ft char * Fn tmpnam char *str Ft char * Fn tempnam const char *tmpdir const char *prefix`

## 描述

`tmpfile` 函数返回指向流的指针，该流与 mkstemp(3) 例程返回的文件描述符关联。创建的文件在 `tmpfile` 返回前被解除链接，使得当对它的最后一个引用关闭时文件被自动删除。文件以访问值 `w+` 打开。若设置了环境变量 `TMPDIR`，文件在 `TMPDIR` 确定的目录中创建。若未设置 `TMPDIR`，默认位置为 **/tmp**。

`tmpnam` 函数返回指向 `P_tmpdir` 目录中文件名的指针，该文件名在过去某个不确定时刻不引用已存在的文件。`P_tmpdir` 定义于头文件

`#include <stdio.h>`

若参数 `str` 非 `NULL`，文件名被复制到它所引用的缓冲区。否则，文件名被复制到静态缓冲区。无论哪种情况，`tmpnam` 都返回指向文件名的指针。

`str` 所引用的缓冲区预期至少有 `L_tmpnam` 字节长。`L_tmpnam` 定义于头文件

`#include <stdio.h>`

`tempnam` 函数类似于 `tmpnam`，但提供指定包含临时文件的目录和文件名前缀的能力。

按所列顺序依次尝试环境变量 `TMPDIR`（若设置）、参数 `tmpdir`（若非 `NULL`）、目录 `P_tmpdir` 和目录 **/tmp**，作为存储临时文件的目录。

参数 `prefix`（若非 `NULL`）用于指定文件名前缀，该前缀将成为创建文件名的第一部分。`tempnam` 函数分配内存以存储文件名；返回的指针可作为 free(3) 的后续参数使用。

## 返回值

`tmpfile` 函数成功时返回指向打开文件流的指针，出错时返回 `NULL` 指针。

`tmpnam` 和 `tempnam` 函数成功时返回指向文件名的指针，出错时返回 `NULL` 指针。

## 环境变量

**`TMPDIR`** [仅 `tempnam` 和 `tmpfile`] 若设置，指定临时文件存储的目录。对于 [issetugid(2)](../sys/issetugid.2.md) 为真的进程，`TMPDIR` 被忽略。

## 兼容性

这些接口仅为 System V 和 ANSI 兼容性而提供。

这些函数的大多数历史实现仅提供有限数量的可能临时文件名（通常 26 个），之后文件名开始被回收。这些函数的 System V 实现（以及 [mktemp(3)](mktemp.3.md)）使用 [access(2)](../sys/access.2.md) 系统调用来确定是否可创建临时文件。这对 setuid 或 setgid 程序有明显的影响，复杂了此类程序中这些接口的可移植使用。

若用户可能不希望临时文件被公开读写，则不应在期望在其他系统上使用的软件中使用 `tmpfile` 接口。

## 错误

`tmpfile` 函数可能失败，并为 fdopen(3) 或 mkstemp(3) 库函数所指定的任何错误设置全局变量 `errno`。

`tmpnam` 函数可能失败，并为 [mktemp(3)](mktemp.3.md) 库函数所指定的任何错误设置 `errno`。

`tempnam` 函数可能失败，并为 malloc(3) 或 [mktemp(3)](mktemp.3.md) 库函数所指定的任何错误设置 `errno`。

## 参见

mkstemp(3), [mktemp(3)](mktemp.3.md)

## 标准

`tmpfile` 和 `tmpnam` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 安全注意事项

`tmpnam` 和 `tempnam` 函数易受文件名选择和文件创建之间发生的竞争条件影响，允许恶意用户根据运行程序的权限级别，潜在地覆盖系统中的任意文件。此外，没有指定文件权限的手段。强烈建议使用 mkstemp(3) 替代这些函数。
