# strverscmp(3)

`strverscmp` — 按自然顺序比较字符串

## 名称

`strverscmp`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft int Fn strverscmp const char *s1 const char *s2`

## 描述

`strverscmp` 函数按自然顺序比较以 NUL 结尾的字符串 `s1` 和 `s2`，返回一个大于、等于或小于 0 的整数，分别对应 `s1` 大于、等于或小于 `s2`。

更具体地说，通过遍历两个字符串直至发现差异来确定此自然顺序。若差异出现在非十进制字符之间，`strverscmp` 的行为类似 [strcmp(3)](strcmp.3.md)（因此排序结果为 "a"、"b"、"train"）。若发现十进制数字，则读取并比较整个数字（因此排序结果为 "9"、"10"、"420"，这与 [strcmp(3)](strcmp.3.md) 所做的字典序不同）。带前导零的数字被解释为小数部分（即使没有小数点），且前导零较多的数字排在前导零较少的数字之前（因此排序结果为 "000"、"00"、"01"、"010"、"09"、"0"、"1"、"9"、"10"）。

## 参见

[strcmp(3)](strcmp.3.md), versionsort(3)

## 标准

`strverscmp` 函数是 GNU 扩展，不遵循任何标准。

## 历史

`strverscmp` 函数在 FreeBSD 13.2 中引入。
