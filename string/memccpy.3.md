# memccpy(3)

`memccpy` — 复制字节直至找到指定字符

## 名称

`memccpy`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft void * Fo memccpy void * restrict dst const void * restrict src int c size_t len Fc`

## 描述

`memccpy` 函数从对象 `src` 复制字节到对象 `dst`。若字符 `c`（转换为 `unsigned char` 后）出现在对象 `src` 中，复制停止，并返回指向对象 `dst` 中 `c` 的副本之后字节的指针。否则，复制 `len` 个字节，并返回 `NULL` 指针。若 `src` 和 `dst` 重叠，行为未定义。

## 参见

[bcopy(3)](bcopy.3.md), [memcpy(3)](memcpy.3.md), [memmove(3)](memmove.3.md), [strcpy(3)](strcpy.3.md)

## 标准

`memccpy` 函数遵循 IEEE Std 1003.1-2004 ("POSIX.1") 和 ISO/IEC 9899:2023 ("ISO C23")。

## 历史

`memccpy` 函数首次出现于 4.4BSD，并首次在 System V Interface Definition, Issue 1 中被规范。`restrict` 关键字在 FreeBSD 5.0.0 中被添加到原型，以符合 IEEE Std 1003.1-2004 ("POSIX.1") 的更新规范。
