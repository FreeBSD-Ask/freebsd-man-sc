# fopen(3)

`fopen` — 流打开函数

## 名称

`fopen`, `fdopen`, `freopen`, `fmemopen`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft FILE * Fn fopen const char * restrict path const char * restrict mode Ft FILE * Fn fdopen int fildes const char *mode Ft FILE * Fn freopen const char *path const char *mode FILE *stream Ft FILE * Fn fmemopen void * restrict buf size_t size const char * restrict mode`

## 描述

`fopen` 函数打开名为 `path` 所指向字符串的文件，并将流与之关联。

`mode` 参数指向以以下字母之一开头的字符串：

**"`r`"** 以读取方式打开。流定位在文件起始。若文件不存在则失败。

**"`w`"** 以写入方式打开。流定位在文件起始。若文件存在则截断为零长度，若不存在则创建。

**"`a`"** 以写入方式打开。流定位在文件末尾。后续对文件的写入始终到达当时当前的文件末尾，无论其间是否有 [fseek(3)](fseek.3.md) 或类似操作。若文件不存在则创建。

在 "`r`"、"`w`" 或 "`a`" 后跟可选的 "`+`" 以读写方式打开文件。在 "`w`" 或 "`w+`" 后跟可选的 "`x`" 使 `fopen` 在文件已存在时调用失败。在上述之后跟可选的 "`e`" 使 `fopen` 调用在底层文件描述符上设置 `FD_CLOEXEC` 标志。

`mode` 字符串还可在 "`+`" 或首字母之后包含字母 "`b`"。这严格是为了与 ISO/IEC 9899:1990 ("ISO C89") 兼容，仅对 `fmemopen` 有效；否则 "`b`" 被忽略。

任何创建的文件将具有模式 "`S_IRUSR` | `S_IWUSR` | `S_IRGRP` | `S_IWGRP` | `S_IROTH` | `S_IWOTH`"（`0666`），并由进程的 umask 值修改（参见 [umask(2)](../sys/umask.2.md)）。

读写流上读取和写入可以任意顺序交织，不需要像早期版本 *stdio* 那样中间定位。但这不可移植到其他系统；ISO/IEC 9899:1990 ("ISO C89") 和 IEEE Std 1003.1 ("POSIX.1") 都要求在输出和输入之间介入文件定位函数，除非输入操作遇到文件末尾。

`fdopen` 函数将流与已有文件描述符 `fildes` 关联。流的模式必须与文件描述符的模式兼容。"`x`" 模式选项被忽略。若存在 "`e`" 模式选项，设置 `FD_CLOEXEC` 标志，否则保持不变。当通过 [fclose(3)](fclose.3.md) 关闭流时，`fildes` 也被关闭。

`freopen` 函数打开名为 `path` 所指向字符串的文件，并将 `stream` 所指向的流与之关联。原流（若存在）被关闭。`mode` 参数的使用与 `fopen` 函数相同。

若 `path` 参数为 `NULL`，`freopen` 尝试以新模式重新打开与 `stream` 关联的文件。新模式必须与流最初打开时的模式兼容：以读取方式打开的流只能重新以读取方式打开，以写入方式打开的流只能重新以写入方式打开，以读写方式打开的流可以任意模式重新打开。"`x`" 模式选项在此情况下无意义。

`freopen` 函数的主要用途是更改与标准文本流（`stderr`、`stdin` 或 `stdout`）关联的文件。

`fmemopen` 函数将 `buf` 和 `size` 参数给定的缓冲区与流关联。`buf` 参数为空指针或指向至少 `size` 字节长的缓冲区。若指定空指针作为 `buf` 参数，`fmemopen` 分配 `size` 字节的内存。此缓冲区在关闭流时自动释放。缓冲区可以以文本模式（默认）或二进制模式（若 `mode` 参数的第二或第三位置存在 "`b`"）打开。以文本模式打开的缓冲区确保写入以 `NULL` 字节终止，前提是最后一次写入未填满整个缓冲区。以二进制模式打开的缓冲区从不追加 `NULL` 字节。

## 返回值

成功完成时，`fopen`、`fdopen`、`freopen` 和 `fmemopen` 返回 `FILE` 指针。否则返回 `NULL`，并设置全局变量 `errno` 以指示错误。

## 错误

**`EINVAL`** `fopen`、`fdopen`、`freopen` 或 `fmemopen` 的 `mode` 参数无效。

`fopen`、`fdopen`、`freopen` 和 `fmemopen` 函数也可能失败，并为 malloc(3) 例程所指定的任何错误设置 `errno`。

`fopen` 函数也可能失败，并为 [open(2)](../sys/open.2.md) 例程所指定的任何错误设置 `errno`。

`fdopen` 函数也可能失败，并为 [fcntl(2)](../sys/fcntl.2.md) 例程所指定的任何错误设置 `errno`。

`freopen` 函数也可能失败，并为 [open(2)](../sys/open.2.md)、[fclose(3)](fclose.3.md) 和 [fflush(3)](fflush.3.md) 例程所指定的任何错误设置 `errno`。

若 `size` 参数为 0，`fmemopen` 函数也可能失败并设置 `errno`。

## 参见

[open(2)](../sys/open.2.md), [fclose(3)](fclose.3.md), fileno(3), [fseek(3)](fseek.3.md), [funopen(3)](funopen.3.md)

## 标准

`fopen` 和 `freopen` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")，但 "`x`" 模式选项遵循 ISO/IEC 9899:2011 ("ISO C11")。`fdopen` 函数遵循 IEEE Std 1003.1-1988 ("POSIX.1")。"`e`" 模式选项不遵循任何标准，但 glibc 也支持。`fmemopen` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。"`b`" 模式不遵循任何标准，但 glibc 也支持。

## 历史

`fopen` 函数出现于 Version 1 AT&T UNIX。
