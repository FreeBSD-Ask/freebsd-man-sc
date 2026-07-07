# offsetof(3)

`offsetof` — 结构成员的偏移量

## 名称

`offsetof`

## 概要

`#include <stddef.h>`

`Ft size_t Fn offsetof type member`

## 描述

`Fn offsetof` 宏展开为类型为 `Ft size_t` 的整型常量表达式，其值为字段 `member` 相对于结构 `type` 起始处的偏移量（以字节为单位）。

如果 `member` 未按字节边界对齐（即它是位域），将导致编译器报错。

## 标准

`Fn offsetof` 宏遵循 ANSI X3.159-1989 ("ANSI C89") 标准。
