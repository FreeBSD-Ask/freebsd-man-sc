# freelocale.3

`freelocale` — 释放由 duplocale(3) 或 newlocale(3) 创建的 locale

## 名称

`freelocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft void Fn freelocale locale_t locale`

## 描述

释放一个 `locale_t`。这会放弃该 locale 独占持有的任何资源。注意，locale 共享引用计数的组件，因此调用此函数不保证释放所有组件。

## 参见

[duplocale(3)](duplocale.3.md), [localeconv(3)](localeconv.3.md), [newlocale(3)](newlocale.3.md), [querylocale(3)](querylocale.3.md), [uselocale(3)](uselocale.3.md), [xlocale(3)](xlocale.3.md)

## 标准

此函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
