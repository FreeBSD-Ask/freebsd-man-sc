# Q_INI.3

`Q_INI` — 定点数学杂项函数/变量

## 名称

`Q_INI`, `Q_NCBITS`, `Q_BT`, `Q_TC`, `Q_NTBITS`, `Q_NFCBITS`, `Q_MAXNFBITS`, `Q_NFBITS`, `Q_NIBITS`, `Q_RPSHFT`, `Q_ABS`, `Q_MAXSTRLEN`, `Q_TOSTR`, `Q_SHL`, `Q_SHR`, `Q_DEBUG`

## 概要

`#include <sys/qmath.h>`

```c
QTYPE Q_INI(QTYPE *q, ITYPE iv, ITYPE dfv, int rpshft);
Q_NCBITS;
__typeof(q) Q_BT(QTYPE q);
ITYPE Q_TC(QTYPE q, ITYPE v);
uint32_t Q_NTBITS(QTYPE q);
uint32_t Q_NFCBITS(QTYPE q);
uint32_t Q_MAXNFBITS(QTYPE q);
uint32_t Q_NFBITS(QTYPE q);
uint32_t Q_NIBITS(QTYPE q);
uint32_t Q_RPSHFT(QTYPE q);
NTYPE Q_ABS(NTYPE n);
uint32_t Q_MAXSTRLEN(QTYPE q, int base);
char *Q_TOSTR(QTYPE q, int prec, int base, char *s, int slen);
ITYPE Q_SHL(QTYPE q, ITYPE iv);
ITYPE Q_SHR(QTYPE q, ITYPE iv);
char *, ... Q_DEBUG(QTYPE q, char *prefmt, char *postfmt, incfmt);
ITYPE Q_DFV2BFV(ITYPE dfv, int nfbits);
```

## 描述

`Q_INI` 使用提供的整数值 `iv` 与十进制小数值 `dfv` 初始化一个 Q 数，并根据所请求的基数移位点 `rpshft` 设置相应的控制位。`dfv` 必须以预处理字面量形式传递，以保留前导零。

`Q_NCBITS` 定义常量指定保留的控制位数，目前为 3。

`Q_NTBITS`、`Q_NFCBITS`、`Q_MAXNFBITS`、`Q_NFBITS` 和 `Q_NIBITS` 分别返回适用于 `q` 的总位数、控制编码的小数位数、最大小数位数、有效小数位数和整数位数。

`Q_BT` 返回 `q` 的 C 数据类型，而 `Q_TC` 返回将 `v` 类型转换为 `q` 的 C 数据类型后的值。

`Q_RPSHFT` 返回 `q` 的二进制小数点相对于第 0 位的位位置。

`Q_ABS` 返回以 `n` 形式传入的任何标准数值类型（使用 MSB 作为符号位，但不包括 Q 数）的绝对值。该函数对有符号/无符号类型安全。

`Q_SHL` 和 `Q_SHR` 返回将整数值 `v` 按 `q` 所对应的适当量进行左移或右移后的结果。

`Q_MAXSTRLEN` 计算以数值基 `base` 渲染 `q` 的 C 字符串表示所需的最大字符数。

`Q_TOSTR` 将 `q` 以数值基 `base` 和小数精度 `prec` 渲染为 C 字符串表示，写入到可用容量为 `slen` 个字符的 `s` 中。`base` 必须在 [2,16] 范围内。将 `prec` 指定为 -1 时以最大精度渲染数字的小数部分。如果 `slen` 大于零但不足以容纳完整的 C 字符串，则会向 `*s` 写入 '\0' C 字符串终止符，从而返回长度为零的 C 字符串。

`Q_DEBUG` 返回适合 printf 类函数渲染 `q` 调试信息的格式字符串及关联数据。如果指定了 `prefmt` 和/或 `postfmt`，它们会分别被前置和追加到结果格式字符串。`incfmt` 布尔值指定是否在调试输出中包含（`true`）或排除（`false`）原始格式字符串本身。

`Q_DFV2BFV` 将十进制小数值 `dfv` 转换为具有 `nfbits` 位二进制精度的二进制编码表示。`dfv` 必须以预处理字面量形式传递，以保留前导零。返回值可用于设置 Q 数的小数位，例如使用 `Q_SFVAL`。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。`NTYPE` 用于指代任何数值类型，因此是 `QTYPE` 和 `ITYPE` 的超集。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_INI` 返回初始化后的 Q 数，可用于链式初始化更多 Q 数。

`Q_TOSTR` 返回指向追加到 `s` 中已渲染数值数据之后的 '\0' C 字符串终止符的指针，缓冲区溢出时返回 NULL。

`Q_DFV2BFV` 返回十进制小数值 `dfv` 在 `nfbits` 位二进制精度下的二进制编码表示。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
