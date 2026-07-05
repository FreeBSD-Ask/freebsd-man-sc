# devclass_get_name.9

`devclass_get_name` — 访问 devclass 的名称

## 名称

`devclass_get_name`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

const char *
devclass_get_name(devclass_t dc)
```

## 描述

返回 devclass 的名称。

## 参见

[devclass(9)](devclass.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
