# MODULE\_DEPEND.9

`MODULE_DEPEND` — 设置内核模块依赖

## 名称

`MODULE_DEPEND`

## 概要

```c
#include <sys/param.h>
#include <sys/module.h>

MODULE_DEPEND(name, moddepend, int minversion, int prefversion, int maxversion)
```

## 描述

`MODULE_DEPEND` 宏设置对另一个名为 `moddepend` 的内核模块的依赖，该模块已通过 `MODULE_VERSION` 注册了其版本。

`MODULE_DEPEND` 宏向内核 [loader(8)](../man8/loader.8.md) 和内核链接器提供提示，以确保指定的依赖项在当前模块之前加载。它不会改变或决定模块在运行时初始化的顺序。

必须为 `moddepend` 指定三个版本：

**`minversion`** 当前模块可以依赖的最低版本。

**`maxversion`** 当前模块可以依赖的最高版本。

**`prefversion`** 当前模块首选依赖的版本。

## 实例

```c
MODULE_DEPEND(foo, bar, 1, 3, 4);
```

## 参见

[DECLARE_MODULE(9)](DECLARE_MODULE.9.md), [module(9)](module.9.md), [MODULE_VERSION(9)](MODULE_VERSION.9.md)

## 作者

本手册页由 Alexander Langer <alex@FreeBSD.org> 编写。
