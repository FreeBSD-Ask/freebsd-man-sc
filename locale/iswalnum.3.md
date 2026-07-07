# iswalnum(3)

`iswalnum` — 宽字符分类工具

## 名称

`iswalnum`, `iswalpha`, `iswascii`, `iswblank`, `iswcntrl`, `iswdigit`, `iswgraph`, `iswhexnumber`, `iswideogram`, `iswlower`, `iswnumber`, `iswphonogram`, `iswprint`, `iswpunct`, `iswrune`, `iswspace`, `iswspecial`, `iswupper`, `iswxdigit`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft int Fn iswalnum wint_t wc Ft int Fn iswalpha wint_t wc Ft int Fn iswascii wint_t wc Ft int Fn iswblank wint_t wc Ft int Fn iswcntrl wint_t wc Ft int Fn iswdigit wint_t wc Ft int Fn iswgraph wint_t wc Ft int Fn iswhexnumber wint_t wc Ft int Fn iswideogram wint_t wc Ft int Fn iswlower wint_t wc Ft int Fn iswnumber wint_t wc Ft int Fn iswphonogram wint_t wc Ft int Fn iswprint wint_t wc Ft int Fn iswpunct wint_t wc Ft int Fn iswrune wint_t wc Ft int Fn iswspace wint_t wc Ft int Fn iswspecial wint_t wc Ft int Fn iswupper wint_t wc Ft int Fn iswxdigit wint_t wc`

## 描述

上述函数是字符分类工具函数，用于宽字符（`wchar_t` 或 `wint_t`）。参见类似命名的单字节分类函数（如 [isalnum(3)](isalnum.3.md)）的描述以了解详情。

## 返回值

这些函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 参见

[isalnum(3)](isalnum.3.md), [isalpha(3)](isalpha.3.md), [isascii(3)](isascii.3.md), [isblank(3)](isblank.3.md), [iscntrl(3)](iscntrl.3.md), [isdigit(3)](isdigit.3.md), [isgraph(3)](isgraph.3.md), ishexnumber(3), [isideogram(3)](isideogram.3.md), [islower(3)](islower.3.md), isnumber(3), [isphonogram(3)](isphonogram.3.md), [isprint(3)](isprint.3.md), [ispunct(3)](ispunct.3.md), [isrune(3)](isrune.3.md), [isspace(3)](isspace.3.md), [isspecial(3)](isspecial.3.md), [isupper(3)](isupper.3.md), [isxdigit(3)](isxdigit.3.md), [wctype(3)](wctype.3.md)

## 标准

这些函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")，但 `iswascii`、`iswhexnumber`、`iswideogram`、`iswnumber`、`iswphonogram`、`iswrune` 和 `iswspecial` 除外，它们是 FreeBSD 扩展。

## 注意事项

除非参数是 `WEOF` 或当前 locale 中有效的 `wchar_t` 值，否则这些函数的结果未定义。
