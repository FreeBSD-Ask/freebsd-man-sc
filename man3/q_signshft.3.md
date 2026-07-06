# Q_SIGNSHFT.3

`Q_SIGNSHFT` — 操作控制/符号数据位的定点数学函数

## 名称

`Q_SIGNSHFT`, `Q_SSIGN`, `Q_CRAWMASK`, `Q_SRAWMASK`, `Q_GCRAW`, `Q_GCVAL`, `Q_SCVAL`

## 概要

`#include <sys/qmath.h>`

```c
uint32_t Q_SIGNSHFT(QTYPE q);
QTYPE Q_SSIGN(QTYPE q, bool isneg);
ITYPE Q_CRAWMASK(QTYPE q);
ITYPE Q_SRAWMASK(QTYPE q);
ITYPE Q_GCRAW(QTYPE q);
ITYPE Q_GCVAL(QTYPE q);
QTYPE Q_SCVAL(QTYPE q, ITYPE cv);
```

## 描述

`Q_SIGNSHFT` 获取 `q` 的符号位相对于第 0 位的位位置。

`Q_SSIGN` 根据布尔值 `isneg` 设置 `q` 的符号位。

`Q_CRAWMASK` 与 `Q_SRAWMASK` 分别返回 `q` 的控制位和符号位所对应的特定位掩码。

`Q_GCRAW` 与 `Q_GCVAL` 分别获取 `q` 控制位的原始掩码值和实际值。

`Q_SCVAL` 将 `q` 的控制位设置为值 `cv`。

所有这些函数均操作以下数据类型：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，统称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。

更多细节参见 [qmath(3)](qmath.3.md)。

## 返回值

`Q_SIGNSHFT` 以整数形式返回符号位的位置。

`Q_SSIGN` 返回修改后的 `q` 值。

`Q_CRAWMASK`、`Q_SRAWMASK`、`Q_GCRAW` 和 `Q_GCVAL` 以与 `q` 相同底层 ITYPE 的整数形式返回各自对应的值。

`Q_SCVAL` 返回修改后的 `q` 值。

## 参见

errno(2), [qmath(3)](qmath.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

[qmath(3)](qmath.3.md) 函数首次出现于 FreeBSD 13.0。

## 作者

[qmath(3)](qmath.3.md) 函数及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
