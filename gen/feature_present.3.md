# feature_present(3)

`feature_present` — 查询内核特性是否存在

## 名称

`feature_present`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
feature_present(const char *feature);
```

## 描述

`feature_present` 函数为应用程序提供了一种方法，以确定当前运行的内核中是否存在特定的内核特性。`feature` 参数指定要检查的特性名称。如果指定的特性存在，`feature_present` 函数将返回 1，否则返回 0。如果由于内部错误导致 `feature_present` 函数无法确定 `feature` 是否存在，它将返回 0。

## 返回值

如果 `feature` 存在则返回 1；否则返回 0。

## 参见

[sysconf(3)](sysconf.3.md), [sysctl(3)](sysctl.3.md)

## 历史

`feature_present` 函数首次出现于 FreeBSD 8.0。
