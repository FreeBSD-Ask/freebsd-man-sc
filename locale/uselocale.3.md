# uselocale(3)

`uselocale` — 设置线程局部 locale

## 名称

`uselocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft locale_t Fn uselocale locale_t locale`

## 描述

指定此线程使用的 locale。指定 `LC_GLOBAL_LOCALE` 将禁用每线程 locale，而传入 `NULL` 则返回当前 locale 而不设置新 locale。

## 返回值

返回之前的 locale，若此线程未关联任何 locale，则返回 `LC_GLOBAL_LOCALE`。

## 参见

[duplocale(3)](duplocale.3.md), [freelocale(3)](freelocale.3.md), [localeconv(3)](localeconv.3.md), [newlocale(3)](newlocale.3.md), [querylocale(3)](querylocale.3.md), [xlocale(3)](xlocale.3.md)

## 标准

此函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
