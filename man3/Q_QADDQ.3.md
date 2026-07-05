# Q_QADDQ.3

`Q_QADDQ` — 操作两个 Q 数的定点数学函数

## 名称

`Q_QADDQ`, `Q_QDIVQ`, `Q_QMULQ`, `Q_QSUBQ`, `Q_NORMPREC`, `Q_QMAXQ`, `Q_QMINQ`, `Q_QCLONEQ`, `Q_CPYVALQ`

## 概要

`#include <sys/qmath.h>`

```c
int Q_QADDQ(QTYPE *a, QTYPE b);
int Q_QDIVQ(QTYPE *a, QTYPE b);
int Q_QMULQ(QTYPE *a, QTYPE b);
int Q_QSUBQ(QTYPE *a, QTYPE b);
int Q_NORMPREC(QTYPE *a, QTYPE *b);
QTYPE Q_QMAXQ(QTYPE a, QTYPE b);
QTYPE Q_QMINQ(QTYPE a, QTYPE b);
int Q_QCLONEQ(QTYPE *l, QTYPE r);
int Q_QCPYVALQ(QTYPE *l, QTYPE r);
```

## 描述

`Q_QADDQ`、`Q_QDIVQ`、`Q_QMULQ` 和 `Q_QSUBQ` 函数分别将 `b` 加到、除以、乘以或从 `a` 中减去，并将结果存入 `a`。两个参数必须以相同的小数基数点初始化。

`Q_NORMPREC` 函数在 `a` 和 `b` 精度不同时尝试归一化它们的精度。如有可能，优先采用两者中较高的精度；若如此会截断另一个操作数的整数部分数据，则选择能同时保留 `a` 和 `b` 整数部分的最高精度。

`Q_QMAXQ` 和 `Q_QMINQ` 函数分别返回 `a` 和 `b` 中较大或较小者。

`Q_QCLONEQ` 和 `Q_QCPYVALQ` 函数尝试将 `r` 的相同副本或表示副本存入 `l`。通过克隆产生的相同 Q 数会复制控制位以及逐字的整数/小数位。表示副本仅复制 `r` 的整数和小数位的值，并按 `l` 的 Q 格式可用位数进行表示。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_QADDQ`、`Q_QDIVQ`、`Q_QMULQ`、`Q_QSUBQ`、`Q_NORMPREC`、`Q_QCLONEQ` 和 `Q_QCPYVALQ` 函数成功时返回 0，失败时返回一个 errno 值。除零时返回 `EINVAL`。溢出和下溢分别返回 `EOVERFLOW` 和 `ERANGE`。当参数精度不匹配时也返回 `ERANGE`。

`Q_QMAXQ` 和 `Q_QMINQ` 函数分别返回两个输入中数值较大或较小者。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
