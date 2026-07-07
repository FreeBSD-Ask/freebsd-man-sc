# MODULE_VERSION(9)

`MODULE_VERSION` — 设置内核模块版本

## 名称

`MODULE_VERSION`

## 概要

```c
#include <sys/param.h>
#include <sys/module.h>

MODULE_VERSION(name, int version)
```

## 描述

`MODULE_VERSION` 宏设置名为 `name` 的模块的版本。其他内核模块随后可以依赖此模块（参见 [MODULE_DEPEND(9)](module_depend.9.md)）。

## 实例

```c
MODULE_VERSION(foo, 1);
```

## 参见

[DECLARE_MODULE(9)](declare_module.9.md), [module(9)](module.9.md), [MODULE_DEPEND(9)](module_depend.9.md)

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
