# iswalnum_l.3

`iswalnum_l` — 宽字符分类工具

## 名称

`iswalnum_l`, `iswalpha_l`, `iswcntrl_l`, `iswctype_l`, `iswdigit_l`, `iswgraph_l`, `iswlower_l`, `iswprint_l`, `iswpunct_l`, `iswspace_l`, `iswupper_l`, `iswxdigit_l`, `towlower_l`, `towupper_l`, `wctype_l`, `iswblank_l`, `iswhexnumber_l`, `iswideogram_l`, `iswnumber_l`, `iswphonogram_l`, `iswrune_l`, `iswspecial_l`, `nextwctype_l`, `towctrans_l`, `wctrans_l`

## 库

Lb libc

## 概要

`#include <wctype.h>`

`Ft int Fn iswalnum_l wint_t wc locale_t loc Ft int Fn iswalpha_l wint_t wc locale_t loc Ft int Fn iswcntrl_l wint_t wc locale_t loc Ft int Fn iswctype_l wint_t wc locale_t loc Ft int Fn iswdigit_l wint_t wc locale_t loc Ft int Fn iswgraph_l wint_t wc locale_t loc Ft int Fn iswlower_l wint_t wc locale_t loc Ft int Fn iswprint_l wint_t wc locale_t loc Ft int Fn iswpunct_l wint_t wc locale_t loc Ft int Fn iswspace_l wint_t wc locale_t loc Ft int Fn iswupper_l wint_t wc locale_t loc Ft int Fn iswxdigit_l wint_t wc locale_t loc Ft wint_t Fn towlower_l wint_t wc locale_t loc Ft wint_t Fn towupper_l wint_t wc locale_t loc Ft wctype_t Fn wctype_l wint_t wc locale_t loc Ft int Fn iswblank_l wint_t wc locale_t loc Ft int Fn iswhexnumber_l wint_t wc locale_t loc Ft int Fn iswideogram_l wint_t wc locale_t loc Ft int Fn iswnumber_l wint_t wc locale_t loc Ft int Fn iswphonogram_l wint_t wc locale_t loc Ft int Fn iswrune_l wint_t wc locale_t loc Ft int Fn iswspecial_l wint_t wc locale_t loc Ft wint_t Fn nextwctype_l wint_t wc locale_t loc Ft wint_t Fn towctrans_l wint_t wc wctrans_t locale_t loc Ft wctrans_t Fn wctrans_l const char * locale_t loc`

## 描述

上述函数是字符分类工具函数，用于在 locale `loc` 下处理宽字符（`wchar_t` 或 `wint_t`）。它们的行为与不带 _l 后缀的版本相同，但使用指定的 locale 而非全局或每线程 locale。这些函数可能以内联函数形式实现在

`#include <wctype.h>`

中，也可能作为函数实现在 C 库中。更多信息参见具体的手册页。

## 返回值

这些函数的返回值与其非 locale 版本相同。若 locale 无效，其行为未定义。

## 参见

iswalnum(3), iswalpha(3), iswblank(3), iswcntrl(3), iswctype(3), iswdigit(3), iswgraph(3), iswhexnumber(3), iswideogram(3), iswlower(3), iswnumber(3), iswphonogram(3), iswprint(3), iswpunct(3), iswrune(3), iswspace(3), iswspecial(3), iswupper(3), iswxdigit(3), nextwctype(3), towctrans(3), towlower(3), towupper(3), [wctrans(3)](wctrans.3.md), wctype(3)

## 标准

这些函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")，但 `iswascii_l`、`iswhexnumber_l`、`iswideogram_l`、`iswphonogram_l`、`iswrune_l`、`iswspecial_l` 和 `nextwctype_l` 除外，它们是 FreeBSD 扩展。
