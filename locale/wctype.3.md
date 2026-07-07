# wctype(3)

`iswctype` — 宽字符类函数

## 名称

`iswctype`, `wctype`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft int Fn iswctype wint_t wc wctype_t charclass Ft wctype_t Fn wctype const char *property`

## 描述

`wctype` 函数返回一个 `wctype_t` 类型的值，该值表示所请求的宽字符类，可用作调用 `iswctype` 时的第二个参数。

识别以下字符类名：

- `alnum`、`cntrl`、`ideogram`、`print`、`space`、`xdigit`
- `alpha`、`digit`、`lower`、`punct`、`special`
- `blank`、`graph`、`phonogram`、`rune`、`upper`

`iswctype` 函数检查宽字符 `wc` 是否属于字符类 `charclass`。

## 返回值

`iswctype` 函数当且仅当 `wc` 具有 `charclass` 所描述的属性，或 `charclass` 为零时返回非零。

`wctype` 函数在 `property` 无效时返回 0，否则返回一个 `wctype_t` 类型的值，可用于后续对 `iswctype` 的调用。

## 实例

用 `iswctype` 和 `wctype` 重新实现 iswalpha(3)：

```c
int
myiswalpha(wint_t wc)
{
	return (iswctype(wc, wctype("alpha")));
}
```

## 参见

[ctype(3)](ctype.3.md), [nextwctype(3)](nextwctype.3.md)

## 标准

`iswctype` 和 `wctype` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。`ideogram`、`phonogram`、`special` 和 `rune` 字符类是扩展。

## 历史

`iswctype` 和 `wctype` 函数首次出现于 FreeBSD 5.0。
