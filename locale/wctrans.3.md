# wctrans.3

`towctrans` — 宽字符映射函数

## 名称

`towctrans`, `wctrans`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft wint_t Fn towctrans wint_t wc wctrans_t desc Ft wctrans_t Fn wctrans const char *charclass`

## 描述

`wctrans` 函数返回一个 `wctrans_t` 类型的值，该值表示所请求的宽字符映射操作，可用作调用 `towctrans` 时的第二个参数。

以下字符映射名称被识别：

| `tolower	toupper` |
| --- |

`towctrans` 函数根据 `desc` 所描述的映射转换宽字符 `wc`。

## 返回值

`towctrans` 函数若成功则返回转换后的字符，否则返回未改变的字符并设置 `errno`。

`wctrans` 函数若成功则返回非零值，否则返回零并设置 `errno`。

## 实例

使用 `towctrans` 和 `wctrans` 重新实现 `towupper`：

```sh
wint_t
mytowupper(wint_t wc)
{
	return (towctrans(wc, wctrans("toupper")));
}
```

## 错误

`towctrans` 函数在以下情况下会失败：

**[Er** EINVAL] 提供的 `desc` 参数无效。

`wctrans` 函数在以下情况下会失败：

**[Er** EINVAL] 请求的映射名称无效。

## 参见

tolower(3), toupper(3), wctype(3)

## 标准

`towctrans` 和 `wctrans` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`towctrans` 和 `wctrans` 函数首次出现于 FreeBSD 5.0。
