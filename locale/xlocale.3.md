# xlocale(3)

`xlocale` — 线程安全的扩展 locale 支持

## 名称

`xlocale`

## 库

Lb libc

## 概要

`#include <xlocale.h>`

## 描述

扩展 locale 支持包含一组用于设置线程局部 locale 的函数，以及用于以指定 locale 执行 locale 相关调用的便利函数。

xlocale API 的核心是 `locale_t` 类型。这是一个封装 locale 的不透明类型。其实例既可以设置为特定线程的 locale，也可以直接传递给各种标准 C 函数的 `_l` 后缀变体。有两个特殊的 `locale_t` 值可用：

- NULL 引用该线程的当前 locale，若该线程未设置 locale 则引用全局 locale。
- LC_GLOBAL_LOCALE 引用全局 locale。

全局 locale 是通过 [setlocale(3)](setlocale.3.md) 函数设置的 locale。

## 参见

[duplocale(3)](duplocale.3.md), [freelocale(3)](freelocale.3.md), [localeconv(3)](localeconv.3.md), [newlocale(3)](newlocale.3.md), [querylocale(3)](querylocale.3.md), [uselocale(3)](uselocale.3.md)

## 便利函数

xlocale API 包含若干 `_l` 后缀的便利函数。这些函数是标准 C 函数的变体，经过修改以接受显式的 `locale_t` 参数作为最后一个参数；对于可变参数函数，则作为紧接在格式字符串之前的附加参数。这些函数均接受 NULL 或 LC_GLOBAL_LOCALE。在这些函数中，NULL 引用 C locale，而非线程的当前 locale。若希望使用线程的当前 locale，请使用不带后缀的函数版本。

通过在包含标准变体的相关头文件*之后*包含

`#include <xlocale.h>`

来暴露这些函数。例如，strtol_l(3) 函数通过在包含

`#include <stdlib.h>`

（其定义了 strtol(3)）之后再包含

`#include <xlocale.h>`

来暴露。

供参考，此处列出以此形式提供的所有 locale 相关函数及其暴露它们的头文件：

**wctype.h** [iswalnum_l(3)](iswalnum_l.3.md), iswalpha_l(3), iswcntrl_l(3), iswctype_l(3), iswdigit_l(3), iswgraph_l(3), iswlower_l(3), iswprint_l(3), iswpunct_l(3), iswspace_l(3), iswupper_l(3), iswxdigit_l(3), towlower_l(3), towupper_l(3), wctype_l(3),

**ctype.h** digittoint_l(3), isalnum_l(3), isalpha_l(3), isblank_l(3), iscntrl_l(3), isdigit_l(3), isgraph_l(3), ishexnumber_l(3), isideogram_l(3), islower_l(3), isnumber_l(3), isphonogram_l(3), isprint_l(3), ispunct_l(3), isrune_l(3), isspace_l(3), isspecial_l(3), isupper_l(3), isxdigit_l(3), tolower_l(3), toupper_l(3)

**inttypes.h** strtoimax_l(3), strtoumax_l(3), wcstoimax_l(3), wcstoumax_l(3)

**langinfo.h** nl_langinfo_l(3)

**monetary.h** strfmon_l(3)

**stdio.h** asprintf_l(3), fprintf_l(3), fscanf_l(3), printf_l(3), scanf_l(3), snprintf_l(3), sprintf_l(3), sscanf_l(3), vasprintf_l(3), vfprintf_l(3), vfscanf_l(3), vprintf_l(3), vscanf_l(3), vsnprintf_l(3), vsprintf_l(3), vsscanf_l(3)

**stdlib.h** mblen_l(3), mbstowcs_l(3), mbtowc_l(3), strtod_l(3), strtof_l(3), strtol_l(3), strtold_l(3), strtoll_l(3), strtoul_l(3), strtoull_l(3), wcstombs_l(3), wctomb_l(3)

**string.h** strcoll_l(3), strxfrm_l(3), strcasecmp_l(3), strcasestr_l(3), strncasecmp_l(3)

**time.h** strftime_l(3) strptime_l(3)

**wchar.h** btowc_l(3), fgetwc_l(3), fgetws_l(3), fputwc_l(3), fputws_l(3), fwprintf_l(3), fwscanf_l(3), getwc_l(3), getwchar_l(3), mbrlen_l(3), mbrtowc_l(3), mbsinit_l(3), mbsnrtowcs_l(3), mbsrtowcs_l(3), putwc_l(3), putwchar_l(3), swprintf_l(3), swscanf_l(3), ungetwc_l(3), vfwprintf_l(3), vfwscanf_l(3), vswprintf_l(3), vswscanf_l(3), vwprintf_l(3), vwscanf_l(3), wcrtomb_l(3), wcscoll_l(3), wcsftime_l(3), wcsnrtombs_l(3), wcsrtombs_l(3), wcstod_l(3), wcstof_l(3), wcstol_l(3), wcstold_l(3), wcstoll_l(3), wcstoul_l(3), wcstoull_l(3), wcswidth_l(3), wcsxfrm_l(3), wctob_l(3), wcwidth_l(3), wprintf_l(3), wscanf_l(3)

**wctype.h** iswblank_l(3), iswhexnumber_l(3), iswideogram_l(3), iswnumber_l(3), iswphonogram_l(3), iswrune_l(3), iswspecial_l(3), nextwctype_l(3), towctrans_l(3), wctrans_l(3)

**xlocale.h** localeconv_l(3)

## 标准

这些函数遵循 IEEE Std 1003.1-2008 (“POSIX.1”)。

## 历史

xlocale API 首次出现于 Darwin 8.0。本实现由 David Chisnall 编写，由 FreeBSD Foundation 赞助，首次出现于 FreeBSD 9.1。

## 注意事项

[setlocale(3)](setlocale.3.md) 函数及其同族函数引用全局 locale。然而，其他依赖 locale 的函数在设置了线程局部 locale 时会使用该线程局部 locale。这意味着，若当前线程通过 [uselocale(3)](uselocale.3.md) 设置了 locale，则使用 [setlocale(3)](setlocale.3.md) 设置 locale、调用依赖 locale 的函数、再恢复 locale 的惯用法将不会产生预期行为。应避免这种惯用法，优先使用 `_l` 后缀版本。
