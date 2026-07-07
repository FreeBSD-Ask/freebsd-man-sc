# cpuset(9)

`cpuset(9)` — cpuset 操作宏

## 名称

`cpuset(9)`, `CPUSET_T_INITIALIZER`, `CPUSET_FSET`, `CPU_CLR`, `CPU_COPY`, `CPU_ISSET`, `CPU_SET`, `CPU_ZERO`, `CPU_FILL`, `CPU_SETOF`, `CPU_EMPTY`, `CPU_ISFULLSET`, `CPU_FFS`, `CPU_COUNT`, `CPU_SUBSET`, `CPU_OVERLAP`, `CPU_CMP`, `CPU_OR`, `CPU_ORNOT`, `CPU_AND`, `CPU_ANDNOT`, `CPU_XOR`, `CPU_CLR_ATOMIC`, `CPU_TEST_CLR_ATOMIC`, `CPU_SET_ATOMIC`, `CPU_SET_ATOMIC_ACQ`, `CPU_TEST_SET_ATOMIC`, `CPU_AND_ATOMIC`, `CPU_OR_ATOMIC`, `CPU_COPY_STORE_REL`

## 概要

```c
#include <sys/_cpuset.h>
#include <sys/cpuset.h>

CPUSET_T_INITIALIZER(ARRAY_CONTENTS);
CPUSET_FSET;

CPU_CLR(size_t cpu_idx, cpuset_t *cpuset);
CPU_COPY(cpuset_t *from, cpuset_t *to);
bool
CPU_ISSET(size_t cpu_idx, cpuset_t *cpuset);
CPU_SET(size_t cpu_idx, cpuset_t *cpuset);
CPU_ZERO(cpuset_t *cpuset);
CPU_FILL(cpuset_t *cpuset);
CPU_SETOF(size_t cpu_idx, cpuset_t *cpuset);
bool
CPU_EMPTY(cpuset_t *cpuset);
bool
CPU_ISFULLSET(cpuset_t *cpuset);
int
CPU_FFS(cpuset_t *cpuset);
int
CPU_COUNT(cpuset_t *cpuset);

bool
CPU_SUBSET(cpuset_t *haystack, cpuset_t *needle);
bool
CPU_OVERLAP(cpuset_t *cpuset1, cpuset_t *cpuset2);
bool
CPU_CMP(cpuset_t *cpuset1, cpuset_t *cpuset2);
CPU_OR(cpuset_t *dst, cpuset_t *src1, cpuset_t *src2);
CPU_ORNOT(cpuset_t *dst, cpuset_t *src1, cpuset_t *src2);
CPU_AND(cpuset_t *dst, cpuset_t *src1, cpuset_t *src2);
CPU_ANDNOT(cpuset_t *dst, cpuset_t *src1, cpuset_t *src2);
CPU_XOR(cpuset_t *dst, cpuset_t *src1, cpuset_t *src2);

CPU_CLR_ATOMIC(size_t cpu_idx, cpuset_t *cpuset);
CPU_TEST_CLR_ATOMIC(size_t cpu_idx, cpuset_t *cpuset);
CPU_SET_ATOMIC(size_t cpu_idx, cpuset_t *cpuset);
CPU_SET_ATOMIC_ACQ(size_t cpu_idx, cpuset_t *cpuset);
CPU_TEST_SET_ATOMIC(size_t cpu_idx, cpuset_t *cpuset);

CPU_AND_ATOMIC(cpuset_t *dst, cpuset_t *src);
CPU_OR_ATOMIC(cpuset_t *dst, cpuset_t *src);
CPU_COPY_STORE_REL(cpuset_t *from, cpuset_t *to);
```

## 描述

`cpuset(9)` 系列宏提供了灵活且高效的 CPU 集合实现，基于 [bitset(9)](bitset.9.md) 宏构建。每个 CPU 由单个位表示。`cpuset_t` 可表示的 CPU 最大数量为 `CPU_SETSIZE`。cpuset 中的各个 CPU 通过 0 到 `CPU_SETSIZE - 1` 的索引引用。

`CPUSET_T_INITIALIZER` 宏允许使用编译期字面值初始化 `cpuset_t`。

`CPUSET_FSET` 宏定义一个编译期字面值，可供 `CPUSET_T_INITIALIZER` 使用，表示一个完整的 cpuset（包含所有 CPU）。关于 `CPUSET_T_INITIALIZER` 和 `CPUSET_FSET` 的用法示例，参见 [CPUSET_T_INITIALIZER 示例](#cpuset_t_initializer-示例) 章节。

`CPU_CLR` 宏从 `cpuset` 所指向的 cpuset 中移除 CPU `cpu_idx`。`CPU_CLR_ATOMIC` 宏功能相同，但使用原子机器指令清除表示该 CPU 的位。`CPU_TEST_CLR_ATOMIC` 宏原子地清除表示该 CPU 的位，并返回该位此前是否被设置。

`CPU_COPY` 宏将 cpuset `from` 的内容复制到 cpuset `to`。`CPU_COPY_STORE_REL` 类似，但从 `from` 读取组成机器字，并使用带释放语义的原子存储写入 `to`。（也就是说，如果 `to` 由多个机器字组成，`CPU_COPY_STORE_REL` 会执行多次独立的原子操作。）

`CPU_SET` 宏将 CPU `cpu_idx` 添加到 `cpuset` 所指向的 cpuset 中（若该 CPU 尚未存在）。`CPU_SET_ATOMIC` 宏功能相同，但使用原子机器指令设置表示该 CPU 的位。`CPU_SET_ATOMIC_ACQ` 宏使用原子获取语义设置表示该 CPU 的位。`CPU_TEST_SET_ATOMIC` 宏原子地设置表示该 CPU 的位，并返回该位此前是否被设置。

`CPU_ISSET` 宏在 CPU `cpu_idx` 属于 `cpuset` 所指向的 cpuset 时返回 `true`。

`CPU_ZERO` 宏从 `cpuset` 中移除所有 CPU。

`CPU_FILL` 宏将所有 CPU 添加到 `cpuset` 中。

`CPU_SETOF` 宏先移除 `cpuset` 中的所有 CPU，然后仅添加 CPU `cpu_idx`。

`CPU_EMPTY` 宏在 `cpuset` 为空时返回 `true`。

`CPU_ISFULLSET` 宏在 `cpuset` 为满集（包含所有 CPU）时返回 `true`。

`CPU_FFS` 宏返回 `cpuset` 中第一个（最低位）CPU 的从 1 开始的索引，若 `cpuset` 为空则返回 0。与 [ffs(3)](../string/ffs.3.md) 类似，若要把 `CPU_FFS` 的非零结果用作其他 `cpuset(9)` 宏的 `cpu_idx` 索引参数，必须从结果中减去一。

`CPU_COUNT` 宏返回 `cpuset` 中 CPU 的总数。

`CPU_SUBSET` 宏在 `needle` 是 `haystack` 的子集时返回 `true`。

`CPU_OVERLAP` 宏在 `cpuset1` 和 `cpuset2` 有公共 CPU 时返回 `true`。（也就是说，`cpuset1` AND `cpuset2` 不为空集。）

`CPU_CMP` 宏在 `cpuset1` 不等于 `cpuset2` 时返回 `true`。

`CPU_OR` 宏将 `src` 中存在的 CPU 添加到 `dst`。（它等价于标量运算：`dst` |= `src`。）`CPU_OR_ATOMIC` 类似，但使用原子机器指令设置 `dst` 中组成机器字里表示 CPU 的位。（也就是说，如果 `dst` 由多个机器字组成，`CPU_OR_ATOMIC` 会执行多次独立的原子操作。）

`CPU_ORNOT` 宏将 `src` 中不存在的 CPU 添加到 `dst`。（它等价于标量运算：`dst` |= ~ `src`。）

`CPU_AND` 宏从 `dst` 中移除 `src` 中不存在的 CPU。（它等价于标量运算：`dst` &= `src`。）`CPU_AND_ATOMIC` 类似，与 `CPU_OR_ATOMIC` 具有相同的原子语义。

`CPU_ANDNOT` 宏从 `dst` 中移除 `src` 中存在的 CPU。（它等价于标量运算：`dst` &= ~ `src`。）

## CPUSET_T_INITIALIZER 示例

```c
cpuset_t myset;

/* 将 myset 初始化为满集（所有 CPU） */
myset = CPUSET_T_INITIALIZER(CPUSET_FSET);

/* 将 myset 初始化为仅包含最低位 CPU */
myset = CPUSET_T_INITIALIZER(0x1);
```

## 参见

[cpuset(1)](../man1/cpuset.1.md), [cpuset(2)](../sys/cpuset.2.md), [bitset(9)](bitset.9.md)

## 历史

**`#include <sys/cpuset.h>`** 最早出现于 FreeBSD 7.1（2009 年 1 月发布）和 FreeBSD 8.0（2009 年 11 月发布）。

本手册页最早出现于 FreeBSD 11.0。

## 作者

`cpuset(9)` 宏由 Jeff Roberson <jeff@FreeBSD.org> 编写。本手册页由 Conrad Meyer <cem@FreeBSD.org> 编写。

## 注意事项

与所有其他对集合成员的引用（使用从 0 开始的索引）不同，`CPU_FFS` 返回从 1 开始的索引结果（若 cpuset 为空则返回 0）。
