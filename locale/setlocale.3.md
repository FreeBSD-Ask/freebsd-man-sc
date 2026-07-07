# setlocale(3)

`setlocale` — C 的自然语言格式化

## 名称

`setlocale`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft char * Fn setlocale int category const char *locale`

## 描述

`setlocale` 函数为特定的例程集合设置 C 库的自然语言格式化风格。每种此类风格称为“locale”，通过以 C 字符串形式传递的适当名称来调用。

`setlocale` 函数识别若干例程类别。以下是这些类别及其选择的例程集合：

**`LC_ALL`** 一般性地设置整个 locale。

**`LC_COLLATE`** 为字符串排序例程设置 locale。这控制 `strcoll` 和 `strxfrm` 中的字母排序。

**`LC_CTYPE`** 为 [ctype(3)](ctype.3.md) 和 [multibyte(3)](multibyte.3.md) 函数设置 locale。这控制大小写、字母或非字母字符等的识别。

**`LC_MESSAGES`** 为消息目录设置 locale，参见 catopen(3) 函数。

**`LC_MONETARY`** 为格式化货币值设置 locale；这影响 `localeconv` 函数。

**`LC_NUMERIC`** 为格式化数字设置 locale。这控制 `printf` 和 `scanf` 等函数中浮点数输入输出的小数点格式化，以及 `localeconv` 返回的值。

**`LC_TIME`** 为使用 `strftime` 函数格式化日期和时间设置 locale。

**`LANG`** 在缺乏更具体的 locale 变量时，设置母语、本地习惯和编码字符集的一般 locale 类别。

默认只定义了三个 locale：空字符串 `""` 表示本机环境，`"C"` 和 `"POSIX"` locale 表示 C 语言环境。`locale` 参数为 `NULL` 时，`setlocale` 返回当前 locale。

locale(1) 命令的 `-a` 选项可用于显示 `locale` 参数可识别的所有其他可能名称。为 `locale` 指定任何无法识别的值会使 `setlocale` 失败。

默认情况下，C 程序在 `"C"` locale 中启动。

库中唯一设置 locale 的函数是 `setlocale`；locale 绝不会因其他例程的副作用而改变。

## 返回值

成功完成后，`setlocale` 返回与所请求 `locale` 的指定 `category` 关联的字符串。如果给定的 `category` 和 `locale` 组合没有意义，`setlocale` 函数返回 `NULL` 且不更改 locale。

## 文件

**$PATH_LOCALE/** *locale/category*

**/usr/share/locale/** *locale/category* locale 文件，对应 locale *locale* 和类别 *category*。

## 实例

以下代码说明程序如何为一种语言初始化国际化环境，同时选择性地修改程序的 locale，使得正则表达式和字符串操作可应用于以不同语言记录的文本：

```c
    setlocale(LC_ALL, "de");
    setlocale(LC_COLLATE, "fr");
```

进程启动时，其当前 locale 设置为 C 或 POSIX locale。依赖于 C 或 POSIX locale 中未定义的 locale 数据的国际化程序，必须在使用任何 locale 特定信息之前按以下方式调用 setlocale 子例程：

```c
    setlocale(LC_ALL, "");
```

## 错误

未定义错误。

## 参见

locale(1), localedef(1), catopen(3), [ctype(3)](ctype.3.md), [localeconv(3)](localeconv.3.md), [multibyte(3)](multibyte.3.md), strcoll(3), strxfrm(3), euc(5), utf8(5), [environ(7)](../man7/environ.7.md)

## 标准

`setlocale` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 历史

`setlocale` 函数首次出现于 4.4BSD。
