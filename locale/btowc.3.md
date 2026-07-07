# btowc(3)

`btowc` — 在宽字符与单字节字符之间进行转换

## 名称

`btowc`, `wctob`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft wint_t Fn btowc int c Ft int Fn wctob wint_t c`

`#include <wchar.h>`

`#include <xlocale.h>`

`Ft wint_t Fn btowc_l int c locale_t loc Ft int Fn wctob_l wint_t c locale_t loc`

## 描述

`btowc` 函数将单字节字符转换为相应的宽字符。若该字符为 `EOF` 或在初始移位状态下无效，`btowc` 返回 `WEOF`。

`wctob` 函数将宽字符转换为相应的单字节字符。若该宽字符为 `WEOF` 或在初始移位状态下无法表示为单个字节，`wctob` 返回 `EOF`。

带 `_l` 后缀的版本接受显式的 locale 参数，而不带后缀的版本使用当前的全局或每线程 locale。

## 参见

[mbrtowc(3)](mbrtowc.3.md), [multibyte(3)](multibyte.3.md), [wcrtomb(3)](wcrtomb.3.md)

## 标准

`btowc` 和 `wctob` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`btowc` 和 `wctob` 函数首次出现于 FreeBSD 5.0。
