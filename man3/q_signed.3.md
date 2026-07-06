# Q_SIGNED.3

`Q_SIGNED` — 定点数学比较与逻辑函数

## 名称

`Q_SIGNED`, `Q_LTZ`, `Q_PRECEQ`, `Q_QLTQ`, `Q_QLEQ`, `Q_QGTQ`, `Q_QGEQ`, `Q_QEQ`, `Q_QNEQ`, `Q_OFLOW`, `Q_RELPREC`

## 概要

`#include <sys/qmath.h>`

```c
bool Q_SIGNED(NTYPE n);
bool Q_LTZ(NTYPE n);
bool Q_PRECEQ(QTYPE a, QTYPE b);
bool Q_QLTQ(QTYPE a, QTYPE b);
bool Q_QLEQ(QTYPE a, QTYPE b);
bool Q_QGTQ(QTYPE a, QTYPE b);
bool Q_QGEQ(QTYPE a, QTYPE b);
bool Q_QEQ(QTYPE a, QTYPE b);
bool Q_QNEQ(QTYPE a, QTYPE b);
bool Q_OFLOW(QTYPE q, ITYPE iv);
int Q_RELPREC(QTYPE a, QTYPE b);
```

## 描述

`Q_SIGNED` 在以 `n` 形式传入的数值数据类型为有符号时返回 `true`，否则返回 `false`。

`Q_LTZ` 在以 `n` 形式传入的数值为负（要求类型使用 MSB 作为符号位）时返回 `true`，否则返回 `false`。

`Q_PRECEQ` 在 `a` 与 `b` 的小数位数相同时返回 `true`，否则返回 `false`。

`Q_QLTQ`、`Q_QLEQ`、`Q_QGTQ`、`Q_QGEQ`、`Q_QEQ` 和 `Q_QNEQ` 函数比较两个 Q 数，当 `a` 分别小于、小于或等于、大于、大于或等于、等于或不等于 `b` 时返回 `true`，否则返回 `false`。比较使用整数和小数值进行，不显式考虑底层的整数位与小数位数量。

`Q_OFLOW` 在整数值 `iv` 无法在不截断的情况下存入 `q` 时返回 `true`，否则返回 `false`。

`Q_RELPREC` 返回 `a` 相对于 `b` 的相对精度。以 *Qm.n* 表示法而言，该函数返回 `a` 与 `b` 的 *n* 值之差。例如，返回值为 +4 表示 `a` 比 `b` 多 4 位小数精度。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。`NTYPE` 用于指代任何数值类型，因此是 `QTYPE` 和 `ITYPE` 的超集。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_SIGNED`、`Q_LTZ`、`Q_PRECEQ`、`Q_QLTQ`、`Q_QLEQ`、`Q_QGTQ`、`Q_QGEQ`、`Q_QEQ`、`Q_QNEQ` 和 `Q_OFLOW` 函数返回求值为布尔值 `true` 或 `false` 的表达式。

`Q_RELPREC` 以有符号整数形式返回相对精度差值。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
