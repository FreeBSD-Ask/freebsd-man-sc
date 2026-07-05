# memcchr.9

`memcchr` — 在字节串中定位不相等字节

## 名称

`memcchr`

## 概要

```c
#include <sys/libkern.h>
```

```c
void *
memcchr(const void *b, int c, size_t len)
```

## 描述

`memcchr` 函数在字符串 `b` 中定位第一个不等于 `c`（转换为 `unsigned char`）的字节。

## 返回值

`memcchr` 函数返回指向所定位字节的指针，如果在 `len` 字节内不存在这样的字节，则返回 NULL。

## 参见

memchr(3)

## 历史

`memcchr` 函数首次出现于 FreeBSD 10.0。
