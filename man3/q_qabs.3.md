# Q_QABS.3

`Q_QABS` — 操作单个 Q 数的定点数学函数

## 名称

`Q_QABS`, `Q_Q2S`, `Q_Q2F`

## 概要

`#include <sys/qmath.h>`

```c
QTYPE Q_QABS(QTYPE q);
double Q_Q2D(QTYPE q);
float Q_Q2F(QTYPE q);
```

## 描述

`Q_QABS` 函数返回 `q` 的绝对值表示。

`Q_Q2D` 和 `Q_Q2F` 函数分别返回 `q` 的 double 和 float 表示。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_QABS` 函数返回与 `q` 类型相同的 QTYPE。

`Q_Q2D` 和 `Q_Q2F` 函数分别返回 `q` 的 double 和 float 表示。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
