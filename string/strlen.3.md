# strlen(3)

`strlen` — 查找字符串的长度

## 名称

`strlen`, `strnlen`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
size_t
strlen(const char *s);

size_t
strnlen(const char *s, size_t maxlen);
```

## 描述

`strlen` 函数计算字符串 `s` 的长度。`strnlen` 函数尝试计算 `s` 的长度，但不会扫描超过 `s` 的前 `maxlen` 个字节。

## 返回值

`strlen` 函数返回终止符 `NUL` 之前的字符数。`strnlen` 函数返回与 `strlen` 相同的结果或 `maxlen`，取较小者。

## 参见

[string(3)](string.3.md), wcslen(3), [wcswidth(3)](wcswidth.3.md)

## 标准

`strlen` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strnlen` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`strlen` 函数首次出现于 Programmer's Workbench (PWB/UNIX)，并移植到 Version 7 AT&T UNIX。`strnlen` 函数首次出现于 FreeBSD 8.0、OpenBSD 4.8 和 NetBSD 6.0。
