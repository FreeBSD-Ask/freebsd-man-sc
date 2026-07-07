# rpmatch(3)

`rpmatch` — 判断对问题的回答是肯定还是否定

## 名称

`rpmatch`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

`Ft int Fn rpmatch const char *response`

## 描述

`rpmatch` 函数根据当前 locale 判断 `response` 参数是对问题的肯定还是否定回答。

## 返回值

`rpmatch` 函数返回：

**1** 回答为肯定。

**0** 回答为否定。

**-1** 无法识别回答。

## 参见

[nl_langinfo(3)](nl_langinfo.3.md), [setlocale(3)](setlocale.3.md)

## 历史

`rpmatch` 函数出现于 FreeBSD 6.0。
