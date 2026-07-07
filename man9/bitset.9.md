# bitset(9)

`bitset` — 位集操作宏

## 名称

`bitset`, `BITSET_DEFINE`, `BITSET_T_INITIALIZER`, `BITSET_FSET`, `BIT_CLR`, `BIT_COPY`, `BIT_ISSET`, `BIT_SET`, `BIT_ZERO`, `BIT_FILL`, `BIT_SETOF`, `BIT_EMPTY`, `BIT_ISFULLSET`, `BIT_FFS`, `BIT_FFS_AT`, `BIT_FLS`, `BIT_FOREACH_ISSET`, `BIT_FOREACH_ISCLR`, `BIT_COUNT`, `BIT_SUBSET`, `BIT_OVERLAP`, `BIT_CMP`, `BIT_OR`, `BIT_OR2`, `BIT_ORNOT`, `BIT_ORNOT2`, `BIT_AND`, `BIT_AND2`, `BIT_ANDNOT`, `BIT_ANDNOT2`, `BIT_XOR`, `BIT_XOR2`, `BIT_CLR_ATOMIC`, `BIT_SET_ATOMIC`, `BIT_SET_ATOMIC_ACQ`, `BIT_TEST_SET_ATOMIC`, `BIT_TEST_CLR_ATOMIC`, `BIT_AND_ATOMIC`, `BIT_OR_ATOMIC`, `BIT_COPY_STORE_REL`

## 概要

```c
#include <sys/_bitset.h>
#include <sys/bitset.h>

BITSET_DEFINE(STRUCTNAME, const SETSIZE)
BITSET_T_INITIALIZER(ARRAY_CONTENTS)
BITSET_FSET(N_WORDS)

BIT_CLR(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)
BIT_COPY(const SETSIZE, struct STRUCTNAME *from, struct STRUCTNAME *to)

bool
BIT_ISSET(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)

BIT_SET(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)
BIT_ZERO(const SETSIZE, struct STRUCTNAME *bitset)
BIT_FILL(const SETSIZE, struct STRUCTNAME *bitset)
BIT_SETOF(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)

bool
BIT_EMPTY(const SETSIZE, struct STRUCTNAME *bitset)

bool
BIT_ISFULLSET(const SETSIZE, struct STRUCTNAME *bitset)

long
BIT_FFS(const SETSIZE, struct STRUCTNAME *bitset)

long
BIT_FFS_AT(const SETSIZE, struct STRUCTNAME *bitset, long start)

long
BIT_FLS(const SETSIZE, struct STRUCTNAME *bitset)

BIT_FOREACH_ISSET(const SETSIZE, size_t bit, const struct STRUCTNAME *bitset)
BIT_FOREACH_ISCLR(const SETSIZE, size_t bit, const struct STRUCTNAME *bitset)

long
BIT_COUNT(const SETSIZE, struct STRUCTNAME *bitset)

bool
BIT_SUBSET(const SETSIZE, struct STRUCTNAME *haystack,
    struct STRUCTNAME *needle)

bool
BIT_OVERLAP(const SETSIZE, struct STRUCTNAME *bitset1,
    struct STRUCTNAME *bitset2)

bool
BIT_CMP(const SETSIZE, struct STRUCTNAME *bitset1,
    struct STRUCTNAME *bitset2)

BIT_OR(const SETSIZE, struct STRUCTNAME *dst, struct STRUCTNAME *src)
BIT_OR2(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src1, struct STRUCTNAME *src2)
BIT_ORNOT(const SETSIZE, struct STRUCTNAME *dst, struct STRUCTNAME *src)
BIT_ORNOT2(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src1, struct STRUCTNAME *src2)
BIT_AND(const SETSIZE, struct STRUCTNAME *dst, struct STRUCTNAME *src)
BIT_AND2(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src1, struct STRUCTNAME *src2)
BIT_ANDNOT(const SETSIZE, struct STRUCTNAME *dst, struct STRUCTNAME *src)
BIT_ANDNOT2(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src1, struct STRUCTNAME *src2)
BIT_XOR(const SETSIZE, struct STRUCTNAME *dst, struct STRUCTNAME *src)
BIT_XOR2(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src1, struct STRUCTNAME *src2)

BIT_CLR_ATOMIC(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)
BIT_SET_ATOMIC(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)
BIT_SET_ATOMIC_ACQ(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)

bool
BIT_TEST_SET_ATOMIC(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)

bool
BIT_TEST_CLR_ATOMIC(const SETSIZE, size_t bit, struct STRUCTNAME *bitset)

BIT_AND_ATOMIC(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src)
BIT_OR_ATOMIC(const SETSIZE, struct STRUCTNAME *dst,
    struct STRUCTNAME *src)
BIT_COPY_STORE_REL(const SETSIZE, struct STRUCTNAME *from,
    struct STRUCTNAME *to)
```

```c
#define _WANT_FREEBSD_BITSET
```

## 描述

bitset 宏族提供了灵活高效的位集实现，前提是编译时已知集合的最大大小。在本手册页中，名称 `SETSIZE` 指位集的大小（以位为单位）。位集中的各个位通过索引 0 到 `SETSIZE - 1` 引用。一个使用

```c
#include <sys/bitset.h>
```

的示例是

```c
#include <sys/cpuset.h>
```

这些宏用于内核中，如果在包含

```c
#include <sys/_bitset.h>
```

或

```c
#include <sys/bitset.h>
```

时定义了 `_KERNEL`，则这些宏可见。用户态程序必须在包含这些文件之前定义 `_WANT_FREEBSD_BITSET` 才能使宏可见。

`BITSET_DEFINE` 宏定义了一个位集结构体 `STRUCTNAME`，可容纳 `SETSIZE` 位。

`BITSET_T_INITIALIZER` 宏允许使用编译时常量值初始化位集结构体。

`BITSET_FSET` 宏生成一个编译时常量，可被 `BITSET_T_INITIALIZER` 使用，表示填满的位集（所有位均置位）。有关 `BITSET_T_INITIALIZER` 和 `BITSET_FSET` 的使用示例，参见 [BITSET_T_INITIALIZER 示例](#bitset_t_initializer-示例) 章节。`BITSET_FSET` 的 `N_WORDS` 参数应为：

```c
__bitset_words(SETSIZE)
```

`BIT_CLR` 宏清除 `bitset` 所指向位集中的 `bit` 位。`BIT_CLR_ATOMIC` 宏功能相同，但以原子方式清除位。`BIT_TEST_CLR_ATOMIC` 宏以原子方式清除位并返回该位是否曾被置位。

`BIT_COPY` 宏将位集 `from` 的内容复制到位集 `to`。`BIT_COPY_STORE_REL` 类似，但从 `from` 复制组成机器字并以原子存储（带释放语义）写入 `to`。（即，如果 `to` 由多个机器字组成，`BIT_COPY_STORE_REL` 执行多个独立的原子操作。）

`BIT_ISSET` 宏在 `bitset` 所指向位集中的 `bit` 位被置位时返回 `true`。

`BIT_SET` 宏设置 `bitset` 所指向位集中的 `bit` 位。`BIT_SET_ATOMIC` 宏功能相同，但以原子方式设置位。`BIT_SET_ATOMIC_ACQ` 宏以获取语义设置位。`BIT_TEST_SET_ATOMIC` 宏以原子方式设置位并返回该位是否曾被置位。

`BIT_ZERO` 宏清除 `bitset` 中的所有位。

`BIT_FILL` 宏设置 `bitset` 中的所有位。

`BIT_SETOF` 宏清除 `bitset` 中的所有位，然后仅设置 `bit` 位。

`BIT_EMPTY` 宏在 `bitset` 为空时返回 `true`。

`BIT_ISFULLSET` 宏在 `bitset` 已满（所有位均置位）时返回 `true`。

`BIT_FFS` 宏返回 `bitset` 中第一个（最低）置位位的 1 基索引，如果 `bitset` 为空则返回零。与 ffs(3) 一样，要将 `BIT_FFS` 的非零结果作为其他 bitset 宏的 `bit` 索引参数，必须从结果中减去一。

`BIT_FFS_AT` 宏返回 `bitset` 中第一个（最低）置位位的 1 基索引，该位大于给定的 1 基索引 `start`，如果 `bitset` 中没有大于 `start` 的置位位则返回零。

`BIT_FLS` 宏返回 `bitset` 中最后一个（最高）置位位的 1 基索引，如果 `bitset` 为空则返回零。与 fls(3) 一样，要将 `BIT_FLS` 的非零结果作为其他 bitset 宏的 `bit` 索引参数，必须从结果中减去一。

`BIT_FOREACH_ISSET` 宏可用于遍历 `bitset` 中所有置位位。索引变量 `bit` 必须声明为 `int` 类型，每次迭代时 `bit` 被设置为连续置位位的索引。循环结束后 `bit` 的值未定义。类似地，`BIT_FOREACH_ISCLR` 遍历 `bitset` 中所有清除位。在循环体中，可以设置或清除当前索引位。但是，设置或清除当前索引位以外的位不保证它们会在同一循环的后续迭代中返回或不返回。

`BIT_COUNT` 宏返回 `bitset` 中置位位的总数。

`BIT_SUBSET` 宏在 `needle` 是 `haystack` 的子集时返回 `true`。

`BIT_OVERLAP` 宏在 `bitset1` 和 `bitset2` 有任何公共位时返回 `true`。（即，如果 `bitset1` AND `bitset2` 不是空集。）

`BIT_CMP` 宏在 `bitset1` 不等于 `bitset2` 时返回 `true`。

`BIT_OR` 宏在 `dst` 中设置 `src` 中存在的位。（相当于标量操作：`dst` |= `src`。）`BIT_OR_ATOMIC` 类似，但以原子方式设置 `dst` 中组成机器字的位。（即，如果 `dst` 由多个机器字组成，`BIT_OR_ATOMIC` 执行多个独立的原子操作。）

`BIT_OR2` 宏计算 `src1` 按位或 `src2`，并将结果赋值给 `dst`。（相当于标量操作：`dst` = `src1` | `src2`。）

`BIT_ORNOT` 宏在 `dst` 中设置 `src` 中不存在的位。（相当于标量操作：`dst` |= ~ `src`。）

`BIT_ORNOT2` 宏计算 `src1` 按位或非 `src2`，并将结果赋值给 `dst`。（相当于标量操作：`dst` = `src1` | ~ `src2`。）

`BIT_AND` 宏从 `dst` 中清除 `src` 中不存在的位。（相当于标量操作：`dst` &= `src`。）`BIT_AND_ATOMIC` 类似，具有与 `BIT_OR_ATOMIC` 相同的原子语义。

`BIT_AND2` 宏计算 `src1` 按位与 `src2`，并将结果赋值给 `dst`。（相当于标量操作：`dst` = `src1` & `src2`。）

`BIT_ANDNOT` 宏从 `dst` 中清除 `src` 中设置的位。（相当于标量操作：`dst` &= ~ `src`。）

`BIT_ANDNOT2` 宏计算 `src1` 按位与非 `src2`，并将结果赋值给 `dst`。（相当于标量操作：`dst` = `src1` & ~ `src2`。）

`BIT_XOR` 宏在 `dst` 中切换 `src` 中设置的位。（相当于标量操作：`dst` ^= `src`。）

`BIT_XOR2` 宏计算 `src1` 按位异或 `src2`，并将结果赋值给 `dst`。（相当于标量操作：`dst` = `src1` ^ `src2`。）

## BITSET_T_INITIALIZER 示例

```c
BITSET_DEFINE(_myset, MYSETSIZE);
struct _myset myset;
/* 将 myset 初始化为填满状态（所有位均置位） */
myset = BITSET_T_INITIALIZER(BITSET_FSET(__bitset_words(MYSETSIZE)));
/* 将 myset 初始化为仅最低位置位 */
myset = BITSET_T_INITIALIZER(0x1);
```

## 参见

[bitstring(3)](../man3/bitstring.3.md), [cpuset(9)](cpuset.9.md)

## 历史

bitset 宏族首次出现于 FreeBSD 10.0（2014 年 1 月）。它们被 MFC 合并到 FreeBSD 9.3（2014 年 7 月发布）。

本手册页首次出现于 FreeBSD 11.0。

## 作者

bitset 宏族由 Attilio Rao <attilio@FreeBSD.org> 从

```c
#include <sys/cpuset.h>
```

中泛化并提取为

```c
#include <sys/_bitset.h>
```

和

```c
#include <sys/bitset.h>
```

本手册页由 Conrad Meyer <cem@FreeBSD.org> 编写。

## 注意事项

所有这些宏的 `SETSIZE` 参数必须与提供给 `BITSET_DEFINE` 的值匹配。

与所有其他对集合成员的零基索引引用不同，`BIT_FFS`、`BIT_FFS_AT` 和 `BIT_FLS` 返回 1 基索引结果（如果集合为空则返回零）。

为了在用户态程序中使用

```c
#include <sys/bitset.h>
```

和

```c
#include <sys/_bitset.h>
```

中定义的宏，必须在包含头文件之前定义 `_WANT_FREEBSD_BITSET`。此要求的存在是为了防止在包含

```c
#include <sys/cpuset.h>
```

或

```c
#include <sched.h>
```

的程序中由于 bitset 宏定义导致的命名空间污染。
