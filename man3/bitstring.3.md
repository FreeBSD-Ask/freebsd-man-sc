# bitstring.3

`bit_alloc` — 位串操作函数与宏

## 名称

`bit_alloc`, `bit_clear`, `bit_count`, `bit_decl`, `bit_ffc`, `bit_ffs`, `bit_ff_at`, `bit_ffc_at`, `bit_ffs_at`, `bit_ffc_area`, `bit_ffs_area`, `bit_ff_area_at`, `bit_ffc_area_at`, `bit_ffs_area_at`, `bit_nclear`, `bit_nset`, `bit_ntest`, `bit_set`, `bit_test`, `bitstr_size`

## 概要

`#include <bitstring.h>`

```c
bitstr_t *bit_alloc(size_t nbits);
void bit_decl(bitstr_t *name, size_t nbits);
void bit_clear(bitstr_t *name, size_t bit);
void bit_count(bitstr_t *name, size_t count, size_t nbits, ssize_t *value);
void bit_ffc(bitstr_t *name, size_t nbits, ssize_t *value);
void bit_ffs(bitstr_t *name, size_t nbits, ssize_t *value);
void bit_ffc_at(bitstr_t *name, size_t start, size_t nbits, ssize_t *value);
void bit_ffs_at(bitstr_t *name, size_t start, size_t nbits, ssize_t *value);
void bit_ff_at(bitstr_t *name, size_t start, size_t nbits, int match, ssize_t *value);
void bit_ffc_area(bitstr_t *name, size_t nbits, size_t size, ssize_t *value);
void bit_ffs_area(bitstr_t *name, size_t nbits, size_t size, ssize_t *value);
void bit_ffc_area_at(bitstr_t *name, size_t start, size_t nbits, size_t size, ssize_t *value);
void bit_ffs_area_at(bitstr_t *name, size_t start, size_t nbits, size_t size, ssize_t *value);
void bit_ff_area_at(bitstr_t *name, size_t start, size_t nbits, size_t size, int match, ssize_t *value);
bit_foreach(bitstr_t *name, size_t nbits, size_t var);
bit_foreach_at(bitstr_t *name, size_t start, size_t nbits, size_t var);
bit_foreach_unset(bitstr_t *name, size_t nbits, size_t var);
bit_foreach_unset_at(bitstr_t *name, size_t start, size_t nbits, size_t var);
void bit_nclear(bitstr_t *name, size_t start, size_t stop);
void bit_nset(bitstr_t *name, size_t start, size_t stop);
int bit_ntest(bitstr_t *name, size_t start, size_t stop, int match);
void bit_set(bitstr_t *name, size_t bit);
int bitstr_size(size_t nbits);
int bit_test(bitstr_t *name, size_t bit);
```

## 描述

这些宏用于操作位串。

`bit_alloc` 函数返回一个类型为 "`bitstr_t *`" 的指针，指向足以存储 `nbits` 位的内存空间；若无可用空间则返回 `NULL`。若成功，返回的位串在初始化时所有位都被清零。

`bit_decl` 宏声明一个足以存储 `nbits` 位的位串。`bit_decl` 可用于在结构体定义中包含静态大小的位串，或在栈上创建位串。使用此宏的用户需负责位串的初始化，通常通过包含结构体的全局初始化或使用 `bit_nset` 或 `bin_nclear` 函数完成。

`bitstr_size` 宏返回存储 `nbits` 位所需的字节数。这对复制位串很有用。

`bit_clear` 和 `bit_set` 函数分别清零或置位位串 `name` 中以零为基的编号位 `bit`。

`bit_nset` 和 `bit_nclear` 函数分别置位或清零位串 `name` 中从 `start` 到 `stop` 的以零为基的编号位。

如果位串 `name` 中以零为基的编号位 `bit` 已置位，`bit_test` 函数求值为非零值，否则为零。

如果位串 `name` 中从 `start` 到 `stop` 的以零为基的编号位全部具有值 `match`，`bit_ntest` 函数求值为非零值。

`bit_ffc` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中第一个未置位位的以零为基的编号。如果所有位都已置位，`value` 所引用的位置被设置为 -1。

`bit_ffs` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中第一个已置位位的以零为基的编号。如果没有已置位的位，`value` 所引用的位置被设置为 -1。

`bit_ffc_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，第一个未置位位的以零为基的编号。如果 `start` 起或之后所有位都已置位，`value` 所引用的位置被设置为 -1。

`bit_ffs_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，第一个已置位位的以零为基的编号。如果 `start` 之后没有已置位的位，`value` 所引用的位置被设置为 -1。

`bit_ff_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，第一个具有值 `match` 的位的以零为基的编号。如果 `start` 之后没有匹配该值的位，`value` 所引用的位置被设置为 -1。

`bit_ffc_area` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，开始一段至少 `size` 个未置位位的连续未置位序列的第一个位的以零为基的编号。如果找不到指定 `size` 的连续未置位序列，`value` 所引用的位置被设置为 -1。

`bit_ffs_area` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，开始一段至少 `size` 个已置位位的连续已置位序列的第一个位的以零为基的编号。如果找不到指定 `size` 的连续已置位序列，`value` 所引用的位置被设置为 -1。

`bit_ffc_area_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，开始一段至少 `size` 个未置位位的连续未置位序列的第一个位的以零为基的编号。如果 `start` 起或之后找不到指定 `size` 的连续未置位序列，`value` 所引用的位置被设置为 -1。

`bit_ffs_area_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，开始一段至少 `size` 个已置位位的连续已置位序列的第一个位的以零为基的编号。如果 `start` 起或之后找不到指定 `size` 的连续已置位序列，`value` 所引用的位置被设置为 -1。

`bit_ff_area_at` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后，开始一段至少 `size` 个位且所有位均具有值 `match` 的连续位序列的第一个位的以零为基的编号。如果 `start` 起或之后找不到指定 `size` 的此类连续位序列，`value` 所引用的位置被设置为 -1。

`bit_count` 函数在 `value` 所引用的位置中存储 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后已置位位的数量。

`bit_foreach` 宏按正向遍历 `name` 所引用的 `nbits` 位数组中所有已置位位，依次将每个位置赋值给 `var`。

`bit_foreach_at` 宏按正向遍历 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后所有已置位位，依次将每个位置赋值给 `var`。

`bit_foreach_unset` 宏按正向遍历 `name` 所引用的 `nbits` 位数组中所有未置位位，依次将每个位置赋值给 `var`。

`bit_foreach_unset_at` 宏按正向遍历 `name` 所引用的 `nbits` 位数组中，从以零为基的位索引 `start` 起或之后所有未置位位，依次将每个位置赋值给 `var`。

位串宏中的参数仅求值一次，可以安全地带有副作用。

## 实例

```c
#include <limits.h>
#include <bitstring.h>
...
#define	LPR_BUSY_BIT		0
#define	LPR_FORMAT_BIT		1
#define	LPR_DOWNLOAD_BIT	2
...
#define	LPR_AVAILABLE_BIT	9
#define	LPR_MAX_BITS		10
make_lpr_available()
{
	bitstr_t bit_decl(bitlist, LPR_MAX_BITS);
	...
	bit_nclear(bitlist, 0, LPR_MAX_BITS - 1);
	...
	if (!bit_test(bitlist, LPR_BUSY_BIT)) {
		bit_clear(bitlist, LPR_FORMAT_BIT);
		bit_clear(bitlist, LPR_DOWNLOAD_BIT);
		bit_set(bitlist, LPR_AVAILABLE_BIT);
	}
}
```

## 参见

malloc(3), [stdbit(3)](stdbit.3.md), [bitset(9)](../man9/bitset.9.md)

## 历史

`bitstring` 函数首次出现于 4.4BSD。
