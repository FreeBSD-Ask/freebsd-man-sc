# qmath.3

`qmath` — 基于 "Q" 数值格式的定点数学库

## 名称

`qmath` "Q" 数值格式

## 概要

`#include <sys/qmath.h>`

## 描述

`qmath` 数据类型和 API 支持基于"Q"数值格式的定点数学运算。这些 API 围绕以下数据类型构建：`s8q_t`、`u8q_t`、`s16q_t`、`u16q_t`、`s32q_t`、`u32q_t`、`s64q_t` 和 `u64q_t`，在先前的 API 定义中泛称为 `QTYPE`。`ITYPE` 指 [stdint(7)](../man7/stdint.7.md) 中的整数类型。`NTYPE` 用于指代任何数值类型，因此是 `QTYPE` 和 `ITYPE` 的超集。

该方案可以表示在小数点后具有 [2, 4, 6, 8, 16, 32, 48] 位精度的 Q 数，具体精度取决于 `Q_INI()` 的 `rpshft` 参数。可用于整数部分的位数没有显式指定，而是隐式占用所选 Q 数据类型的剩余可用位。

对 Q 数的操作保持其参数的精度。小数部分被截断以适应目标，不进行舍入。这些操作均不受浮点环境的影响。

有关更多细节，请参见下文的实现细节部分。

## 函数列表

### 创建/初始化 Q 数的函数

[Q_INI(3)](Q_INI.3.md)

### 对两个 Q 数进行运算的数值函数

[Q_QADDQ(3)](Q_QADDQ.3.md), Q_QDIVQ(3), Q_QMULQ(3), Q_QSUBQ(3), Q_NORMPREC(3), Q_QMAXQ(3), Q_QMINQ(3), Q_QCLONEQ(3), Q_QCPYVALQ(3)

### 将整数应用于 Q 数的数值函数

[Q_QADDI(3)](Q_QADDI.3.md), Q_QDIVI(3), Q_QMULI(3), Q_QSUBI(3), Q_QFRACI(3), Q_QCPYVALI(3)

### 对单个 Q 数进行运算的数值函数

[Q_QABS(3)](Q_QABS.3.md), Q_Q2D(3), Q_Q2F(3)

### 比较与逻辑函数

[Q_SIGNED(3)](Q_SIGNED.3.md), Q_LTZ(3), Q_PRECEQ(3), Q_QLTQ(3), Q_QLEQ(3), Q_QGTQ(3), Q_QGEQ(3), Q_QEQ(3), Q_QNEQ(3), Q_OFLOW(3), Q_RELPREC(3)

### 操作控制/符号数据位的函数

[Q_SIGNSHFT(3)](Q_SIGNSHFT.3.md), Q_SSIGN(3), Q_CRAWMASK(3), Q_SRAWMASK(3), Q_GCRAW(3), Q_GCVAL(3), Q_SCVAL(3)

### 操作组合整数/小数数据位的函数

[Q_IFRAWMASK(3)](Q_IFRAWMASK.3.md), Q_IFVALIMASK(3), Q_IFVALFMASK(3), Q_GIFRAW(3), Q_GIFABSVAL(3), Q_GIFVAL(3), Q_SIFVAL(3), Q_SIFVALS(3)

### 操作整数数据位的函数

[Q_IRAWMASK(3)](Q_IRAWMASK.3.md), Q_GIRAW(3), Q_GIABSVAL(3), Q_GIVAL(3), Q_SIVAL(3)

### 操作小数数据位的函数

[Q_FRAWMASK(3)](Q_FRAWMASK.3.md), Q_GFRAW(3), Q_GFABSVAL(3), Q_GFVAL(3), Q_SFVAL(3)

### 杂项函数/变量

Q_NCBITS(3), Q_BT(3), Q_TC(3), Q_NTBITS(3), Q_NFCBITS(3), Q_MAXNFBITS(3), Q_NFBITS(3), Q_NIBITS(3), Q_RPSHFT(3), Q_ABS(3), Q_MAXSTRLEN(3), Q_TOSTR(3), Q_SHL(3), Q_SHR(3), Q_DEBUG(3), Q_DFV2BFV(3)

## 实现细节

`qmath` 数据类型和 API 支持基于"Q"数值格式的定点数学运算。本实现使用 Q 表示法 *Qm.n*，其中 *m* 指定整数数据的位数（对于有符号类型不包括符号位），*n* 指定小数数据的位数。

这些 API 围绕以下从 q_t 派生的数据类型构建：

```c
typedef int8_t		s8q_t;
typedef uint8_t		u8q_t;
typedef int16_t		s16q_t;
typedef uint16_t	u16q_t;
typedef int32_t		s32q_t;
typedef uint32_t	u32q_t;
typedef int64_t		s64q_t;
typedef uint64_t	u64q_t;
```

在先前的 API 定义中，这些类型被泛称为 `QTYPE`，而 `ITYPE` 指 Q 数据类型所派生自的 [stdint(7)](../man7/stdint.7.md) 整数类型。`NTYPE` 用于指代任何数值类型，因此是 `QTYPE` 和 `ITYPE` 的超集。

所有 q_t 数据类型的最低 3 位（LSB）保留用于嵌入式控制数据：

- 位 1-2 指定小数点移位索引操作数，00、01、10、11 分别对应 1、2、3、4。
- 位 3 指定小数点移位索引操作数的乘数为 2（0）或 16（1）。

因此，该方案可以表示在小数点后具有 [2, 4, 6, 8, 16, 32, 48, 64] 位精度的 Q 数。可用于整数部分的位数没有显式指定，而是隐式占用所选 Q 数据类型的剩余可用位。

此外，有符号 Q 类型的最高位（MSB）存储符号位，位值为 0 表示正数，位值为 1 表示负数。负数以设置了符号位的绝对值形式存储，而不是更常见的二进制补码表示。这避免了对负数进行位移操作，因为某些编译器可能导致未定义行为。

因此，用于 Q 数的二进制表示由一组不同的数据位类型和相关位计数组成。数据位类型/标签按从 LSB 到 MSB 的顺序列出为：控制位 'C'、小数位 'F'、整数位 'I' 和符号位 'S'。以下示例说明了使用 s32q_t 变量表示的 Q20.8 数的二进制表示：

```c
M                                                             L
S                                                             S
B                                                             B
3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
S I I I I I I I I I I I I I I I I I I I I F F F F F F F F C C C
```

重要的位计数包括：总位数、控制位、控制编码小数位、最大小数位、有效小数位和整数位。

总位数由 q_t 数据类型的大小决定。例如，s32q_t 有 32 个总位数。

控制编码小数位数通过按控制位编码方案计算小数位数得出。例如，控制位的二进制值 101 编码的小数位数为 2 × 16 = 32 位。

最大小数位数由总位数与控制/符号位数之差得出。例如，s32q_t 最多有 32 - 3 - 1 = 28 个小数位。

有效小数位数由控制编码小数位数和最大小数位数中的较小值决定。例如，具有 32 个控制编码小数位的 s32q_t 实际上被限制为 28 个小数位。

整数位数由总位数与所有其他非整数数据位（控制位、小数位和符号位之和）的差值得出。例如，具有 8 个有效小数位的 s32q_t 有 32 - 3 - 8 - 1 = 20 个整数位。如果所有可用的数值数据位都保留给小数数据，则整数位数可以为零，例如当控制编码小数位数大于或等于底层 Q 数据类型的最大小数位数时。

## 实例

### 计算 r=4.2、rpshft=16 时圆的面积

```c
u64q_t a, pi, r;
char buf[32];
Q_INI(&a, 0, 0, 16);
Q_INI(&pi, 3, 14159, 16);
Q_INI(&r, 4, 2, 16);
Q_QCLONEQ(&a, r);
Q_QMULQ(&a, r);
Q_QMULQ(&a, pi);
Q_TOSTR(a, -1, 10, buf, sizeof(buf));
printf("%s\n", buf);
```

### 调试

声明一个 Q20.8 的 s32q_t 数 `s32`，用 5/3 的定点值初始化它，并将该变量的调试表示（包括其完整精度的十进制 C 字符串表示）渲染到控制台：

```c
s32q_t s32;
Q_INI(&s32, 0, 0, 8);
Q_QFRACI(&s32, 5, 3);
char buf[Q_MAXSTRLEN(s32, 10)];
Q_TOSTR(s32, -1, 10, buf, sizeof(buf));
printf(Q_DEBUG(s32, "", "\n\ntostr=%s\n\n", 0), buf);
```

上述代码向控制台输出以下内容：

```c
"s32"@0x7fffffffe7d4
	type=s32q_t, Qm.n=Q20.8, rpshft=11, imin=0xfff00001, \
imax=0xfffff
	qraw=0x00000d53
	imask=0x7ffff800, fmask=0x000007f8, cmask=0x00000007, \
ifmask=0x7ffffff8
	iraw=0x00000800, iabsval=0x1, ival=0x1
	fraw=0x00000550, fabsval=0xaa, fval=0xaa
	tostr=1.664
```

注意：上面渲染输出中的 "\n" 表示为使手册页保持在 80 列以内而手动插入的换行符，并非实际输出的一部分。

## 参见

errno(2), math(3), [Q_FRAWMASK(3)](Q_FRAWMASK.3.md), [Q_IFRAWMASK(3)](Q_IFRAWMASK.3.md), [Q_INI(3)](Q_INI.3.md), [Q_IRAWMASK(3)](Q_IRAWMASK.3.md), [Q_QABS(3)](Q_QABS.3.md), [Q_QADDI(3)](Q_QADDI.3.md), [Q_QADDQ(3)](Q_QADDQ.3.md), [Q_SIGNED(3)](Q_SIGNED.3.md), [Q_SIGNSHFT(3)](Q_SIGNSHFT.3.md), [stdint(7)](../man7/stdint.7.md)

## 历史

`qmath` 函数首次出现于 FreeBSD 13.0。

## 作者

`qmath` 函数和本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。
