# memchr(3)

`memchr` — 在内存对象中定位字节

## 名称

`memchr`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
void *
memchr(const void *b, int c, size_t len);

void *
memrchr(const void *b, int c, size_t len);
```

## 描述

`memchr` 函数在对象 `b` 中查找 `c`（转换为 `unsigned char`）的首次出现，最多查找 `len` 个字符。

`memrchr` 函数行为与 `memchr` 相同，区别在于它查找对象 `b` 中 `c` 的最后一次出现，限于前 `len` 个字符。

## 返回值

`memchr` 和 `memrchr` 函数返回指向所定位字节的指针；若 `len` 字节内无此字节，返回 `NULL`。

## 参见

[memmem(3)](memmem.3.md), [strchr(3)](strchr.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md), [wmemchr(3)](wmemchr.3.md)

## 标准

`memchr` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

`memrchr` 函数是 GNU 扩展，不遵循任何标准。

## 历史

`memrchr` 函数首次出现于 GNU libc 2.1.91，本实现首次出现于 FreeBSD 6.4，源自 OpenBSD 4.3。
