# Q_QADDI.3

`Q_QADDI` — 将整数应用于 Q 数的定点数学函数

## 名称

`Q_QADDI`, `Q_QDIVI`, `Q_QMULI`, `Q_QSUBI`, `Q_QFRACI`, `Q_QCPYVALI`

## 概要

`#include <sys/qmath.h>`

```c
int Q_QADDI(QTYPE *a, ITYPE b);
int Q_QDIVI(QTYPE *a, ITYPE b);
int Q_QMULI(QTYPE *a, ITYPE b);
int Q_QSUBI(QTYPE *a, ITYPE b);
int Q_QFRACI(QTYPE *q, ITYPE n, ITYPE d);
int Q_QCPYVALI(QTYPE *q, ITYPE i);
```

## 描述

`Q_QADDI`、`Q_QDIVI`、`Q_QMULI` 和 `Q_QSUBI` 函数分别将 `b` 加到、除以、乘以或从 `a` 中减去，并将结果存入 `a`。

`Q_QFRACI` 函数计算 `n` 除以 `d` 的分数值，并将定点结果存入 `q`。

`Q_QCPYVALI` 函数用整数值 `i` 的 Q 表示覆盖 `q` 的整数和小数位。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_QADDI`、`Q_QDIVI`、`Q_QMULI`、`Q_QSUBI`、`Q_QFRACI` 和 `Q_QCPYVALI` 函数成功时返回 0，失败时返回一个 errno 值。除零时返回 `EINVAL`。溢出和下溢分别返回 `EOVERFLOW` 和 `ERANGE`。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
