# newlocale(3)

`newlocale` — 创建新的 locale

## 名称

`newlocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft locale_t Fn newlocale int mask const char * locale locale_t base`

## 描述

创建新的 locale，从现有的 locale 继承某些属性。`mask` 指定了新 locale 的哪些组件将被设置为 `locale` 参数所指定名称的 locale。未在 `mask` 中指定的组件将从 `base` 所引用的 locale 继承（若 `base` 不为 `NULL`）。若调用成功，`base` 所引用的 locale 的状态是未指定的，不得再对其进行访问。特殊的 locale `LC_GLOBAL_LOCALE` 不能指定为 `base`。`mask` 为 `LC_ALL_MASK`（表示所有可能的 locale 组件），或以下各项的某种组合的逻辑或：

**LC_COLLATE_MASK** 用于字符串排序例程的 locale。这控制 strcoll(3) 和 strxfrm(3) 中的字母排序。

**LC_CTYPE_MASK** 用于 [ctype(3)](ctype.3.md) 和 [multibyte(3)](multibyte.3.md) 函数的 locale。这控制大小写、字母或非字母字符等的识别。

**LC_MESSAGES_MASK** 为消息目录设置 locale，参见 catopen(3) 函数。

**LC_MONETARY_MASK** 为货币值格式化设置 locale；这影响 [localeconv(3)](localeconv.3.md) 函数。

**LC_NUMERIC_MASK** 为数字格式化设置 locale。这控制 printf(3) 和 scanf(3) 等函数中浮点数输入输出的小数点格式，以及 [localeconv(3)](localeconv.3.md) 返回的值。

**LC_TIME_MASK** 为使用 strftime(3) 函数格式化日期和时间设置 locale。

此函数使用与 [setlocale(3)](setlocale.3.md) 相同的规则加载 locale 组件。

## 返回值

返回一个新的、有效的 `locale_t`，若发生错误则返回 `NULL`。必须用 [freelocale(3)](freelocale.3.md) 释放返回的 locale。

## 参见

[duplocale(3)](duplocale.3.md), [freelocale(3)](freelocale.3.md), [localeconv(3)](localeconv.3.md), [querylocale(3)](querylocale.3.md), [uselocale(3)](uselocale.3.md), [xlocale(3)](xlocale.3.md)

## 标准

此函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。
