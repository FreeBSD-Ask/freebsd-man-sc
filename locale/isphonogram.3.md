# isphonogram(3)

`isphonogram` — 表音字符测试

## 名称

`isphonogram`, `isphonogram_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn isphonogram int c Ft int Fn isphonogram_l int c locale_t loc`

## 描述

`isphonogram` 和 `isphonogram_l` 函数测试是否为表音字符。

`isphonogram_l` 函数接受一个显式的 locale 参数，而 `isphonogram` 函数使用当前的全局或每线程 locale。

## 返回值

`isphonogram` 和 `isphonogram_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), [isideogram(3)](isideogram.3.md), isideogram_l(3), iswphonogram(3), iswphonogram_l(3), [xlocale(3)](xlocale.3.md)

## 历史

`isphonogram` 函数出现于 4.4BSD。
