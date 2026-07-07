# duplocale(3)

`duplocale` — 复制 locale

## 名称

`duplocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft locale_t Fn duplocale locale_t locale`

## 描述

复制现有的 `locale_t`，返回一个新的 `locale_t`，它引用相同的 locale 值但具有独立的内部状态。许多函数（如 [mblen(3)](mblen.3.md)）需要持久状态。这些函数以前使用静态变量，从多个线程调用它们会产生未定义行为。它们现在使用由 [uselocale(3)](uselocale.3.md) 关联到当前线程的 `locale_t` 中的字段。因此，这些调用仅在具有唯一每线程 locale 的线程上是线程安全的。此调用返回的 locale 必须用 [freelocale(3)](freelocale.3.md) 释放。

## 参见

[freelocale(3)](freelocale.3.md), [localeconv(3)](localeconv.3.md), [newlocale(3)](newlocale.3.md), [querylocale(3)](querylocale.3.md), [uselocale(3)](uselocale.3.md), [xlocale(3)](xlocale.3.md)

## 标准

此函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 缺陷

理想情况下，[uselocale(3)](uselocale.3.md) 应隐式复制 `locale_t` 以确保线程安全，并且全局 locale 的副本应延迟安装到每个线程上。为了与 Darwin 兼容，FreeBSD 实现未这样做。
