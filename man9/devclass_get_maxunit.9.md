# devclass_get_maxunit(9)

`devclass_get_maxunit` — 查找类中的最大单元号

## 名称

`devclass_get_maxunit`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
devclass_get_maxunit(devclass_t dc)
```

## 描述

返回要分配给 `devclass` 中设备实例的下一个单元号。这比当前已分配的最高单元号大一。

## 返回值

`devclass_get_maxunit` 函数在 `dc` 为 `NULL` 时返回 -1，否则返回 `dc` 的 devclass 中的下一个单元号。

## 错误

无。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。

## 缺陷

此名称容易引起混淆，因为它比最大单元号大一。
