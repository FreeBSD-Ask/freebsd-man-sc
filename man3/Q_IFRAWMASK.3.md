# Q_IFRAWMASK.3

`Q_IFRAWMASK` — 操作整数/小数组合数据位的定点数学函数

## 名称

`Q_IFRAWMASK`, `Q_IFVALIMASK`, `Q_IFVALFMASK`, `Q_GIFRAW`, `Q_GIFABSVAL`, `Q_GIFVAL`, `Q_SIFVAL`, `Q_SIFVALS`

## 概要

`#include <sys/qmath.h>`

```c
ITYPE Q_IFRAWMASK(QTYPE q);
ITYPE Q_IFVALIMASK(QTYPE q);
ITYPE Q_IFVALFMASK(QTYPE q);
ITYPE Q_GIFRAW(QTYPE q);
ITYPE Q_GIFABSVAL(QTYPE q);
ITYPE Q_GIFVAL(QTYPE q);
QTYPE Q_SIFVAL(QTYPE q, ITYPE ifv);
QTYPE Q_SIFVALS(QTYPE q, ITYPE iv, ITYPE fv);
```

## 描述

`Q_IFRAWMASK` 返回 `q` 的整数与小数组合数据位所对应的特定位掩码。

`Q_IFVALIMASK` 与 `Q_IFVALFMASK` 分别返回 `q` 的整数/小数组合数据位值中整数部分和小数部分所对应的特定位掩码，即适用于 `Q_GIFABSVAL` 和 `Q_GIFVAL` 所返回的值。

`Q_GIFRAW` 返回 `q` 的原始掩码整数/小数数据位。

`Q_GIFABSVAL` 与 `Q_GIFVAL` 分别返回 `q` 的整数/小数数据位的绝对值和实际值。

`Q_SIFVAL` 将 `q` 的整数/小数组合数据位设置为值 `ifv`，而 `Q_SIFVALS` 则独立地将 `q` 的整数和小数数据位分别设置为 `iv` 和 `fv`。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_IFRAWMASK`、`Q_IFVALIMASK`、`Q_IFVALFMASK`、`Q_GIFRAW`、`Q_GIFABSVAL` 和 `Q_GIFVAL` 以与 `q` 相同底层 ITYPE 的整数形式返回各自对应的值。

`Q_SIFVAL` 和 `Q_SIFVALS` 返回修改后的 `q` 值。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
