# fread(3)

`fread` — 二进制流输入/输出

## 名称

`fread`, `fread_unlocked`, `fwrite`, `fwrite_unlocked`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft size_t Fn fread void * restrict ptr size_t size size_t nmemb FILE * restrict stream Ft size_t Fn fread_unlocked void * restrict ptr size_t size size_t nmemb FILE * restrict stream Ft size_t Fn fwrite const void * restrict ptr size_t size size_t nmemb FILE * restrict stream Ft size_t Fn fwrite_unlocked const void * restrict ptr size_t size size_t nmemb FILE * restrict stream`

## 描述

`fread` 函数从 `stream` 所指向的流中读取 `nmemb` 个对象，每个对象长 `size` 字节，并将其存储到 `ptr` 所给定的位置。

`fwrite` 函数向 `stream` 所指向的流写入 `nmemb` 个对象，每个对象长 `size` 字节，并从 `ptr` 所给定的位置获取数据。

`fread_unlocked` 和 `fwrite_unlocked` 函数分别等价于 `fread` 和 `fwrite`，区别在于调用者在调用它们之前需使用 [flockfile(3)](flockfile.3.md) 锁定流。这些函数可用于避免锁定流的开销，并防止多个线程操作同一流时出现竞争。

## 返回值

`fread` 和 `fwrite` 函数按读取或写入的字节数推进流的文件位置指示器。它们返回读取或写入的对象数。如果发生错误或到达文件末尾，返回值为较短的对象计数（或零）。

`fread` 函数不区分文件末尾和错误，调用者必须使用 feof(3) 和 [ferror(3)](ferror.3.md) 来确定发生了哪种情况。`fwrite` 函数仅在发生写入错误时返回小于 `nmemb` 的值。

## 参见

[read(2)](../man2/read.2.md), [write(2)](../man2/write.2.md)

## 标准

`fread` 和 `fwrite` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 历史

`fread` 和 `fwrite` 函数首次出现于 Version 7 AT&T UNIX。
