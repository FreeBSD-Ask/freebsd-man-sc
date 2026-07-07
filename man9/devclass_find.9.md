# devclass_find(9)

`devclass_find` — 搜索 devclass

## 名称

`devclass_find`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

devclass_t
devclass_find(const char *classname)
```

## 描述

搜索具有指定名称的 `devclass`。

## 返回值

如果 `devclass` 存在，则返回它，否则返回 `NULL`。

## 参见

[devclass(9)](devclass.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
