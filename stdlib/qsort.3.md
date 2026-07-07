# qsort(3)

`qsort` — 排序函数

## 名称

`qsort`, `qsort_b`, `qsort_r`, `heapsort`, `heapsort_b`, `mergesort`, `mergesort_b`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void
qsort(void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *));

void
qsort_b(void *base, size_t nmemb, size_t size,
    int (^compar)(const void *, const void *));

void
qsort_r(void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *, void *), void *thunk);

int
heapsort(void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *));

int
heapsort_b(void *base, size_t nmemb, size_t size,
    int (^compar)(const void *, const void *));

int
mergesort(void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *));

int
mergesort_b(void *base, size_t nmemb, size_t size,
    int (^compar)(const void *, const void *));
```

`#define __STDC_WANT_LIB_EXT1__ 1`

```c
errno_t
qsort_s(void *base, rsize_t nmemb, rsize_t size,
    int (*compar)(const void *, const void *, void *), void *thunk);
```

## 描述

`qsort` 函数是修改版的分区交换排序，即快速排序。`heapsort` 函数是修改版的选择排序。`mergesort` 函数是修改版的归并排序，带有指数搜索，专为对已有顺序的数据进行排序而设计。

`qsort` 和 `heapsort` 函数对 `nmemb` 个对象的数组进行排序，`base` 指向该数组的初始成员。每个对象的大小由 `size` 指定。`mergesort` 函数行为类似，但*要求* `size` 大于 `sizeof(void *) / 2`。

数组 `base` 的内容按 `compar` 所指向的比较函数以升序排序，该函数需要两个参数，分别指向待比较的对象。

当第一个参数分别小于、等于或大于第二个参数时，比较函数必须返回一个小于、等于或大于零的整数。

`qsort_r` 函数的行为与 `qsort` 相同，区别在于它接受一个额外的参数 `thunk`，该参数原样作为最后一个参数传递给 `compar` 所指向的函数。这使得比较函数无需使用全局变量即可访问额外数据，因此 `qsort_r` 适用于必须是可重入的函数。`qsort_b` 函数的行为与 `qsort` 相同，区别在于它接受一个 block 而非函数指针。

`qsort`、`qsort_r` 和 `heapsort` 所实现的算法*不*稳定，即若两个成员比较结果相等，它们在排序后数组中的顺序是未定义的。`heapsort_b` 函数的行为与 `heapsort` 相同，区别在于它接受一个 block 而非函数指针。`mergesort` 算法是稳定的。`mergesort_b` 函数的行为与 `mergesort` 相同，区别在于它接受一个 block 而非函数指针。

`qsort` 和 `qsort_r` 函数是 C.A.R. Hoare 的 "quicksort" 算法的实现，该算法是分区交换排序的一种变体；具体参见 D.E. Knuth 的 Algorithm Q。**Quicksort** 的平均时间复杂度为 O(N lg N)。此实现使用中位数选择以避免其 O(N²) 的最坏情况行为。

`heapsort` 函数是 J.W.J. William 的 "heapsort" 算法的实现，该算法是选择排序的一种变体；具体参见 D.E. Knuth 的 Algorithm H。**Heapsort** 的最坏情况时间复杂度为 O(N lg N)。与 `qsort` 相比，它的*唯一*优势是几乎不使用额外内存；虽然 `qsort` 不分配内存，但它使用递归实现。

`mergesort` 函数需要大小为 `nmemb * size` 字节的额外内存；仅当空间不紧张时才应使用。`mergesort` 函数针对已有顺序的数据进行了优化；其最坏情况时间为 O(N lg N)，最佳情况为 O(N)。

通常，`qsort` 快于 `mergesort` 快于 `heapsort`。内存可用性和数据中已有的顺序可能使此情况不成立。

`qsort_s` 函数的行为与 `qsort_r` 相同，区别在于若 `nmemb` 或 `size` 大于 `RSIZE_MAX`，或 `nmemb` 不为零且 `compar` 为 `NULL` 或 `size` 为零，则调用运行时约束处理程序，且 `qsort_s` 返回错误。注意，处理程序在 `qsort_s` 返回错误之前被调用，且处理程序函数可能不返回。

## 返回值

`qsort` 和 `qsort_r` 函数不返回值。`qsort_s` 函数成功时返回零，失败时返回非零。

成功完成时，`heapsort` 和 `mergesort` 函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 实例

以下示例程序使用 `qsort` 就地对 `int` 值数组进行排序，然后将排序后的数组输出到标准输出：

```c
#include <stdio.h>
#include <stdlib.h>
/*
 * 自定义比较函数，通过 qsort(3) 传递的指针比较 'int' 值
 */
static int
int_compare(const void *p1, const void *p2)
{
	int left = *(const int *)p1;
	int right = *(const int *)p2;
	return ((left > right) - (left < right));
}
/*
 * 对 'int' 值数组进行排序并输出到标准输出
 */
int
main(void)
{
	int int_array[] = { 4, 5, 9, 3, 0, 1, 7, 2, 8, 6 };
	size_t array_size = sizeof(int_array) / sizeof(int_array[0]);
	size_t k;
	qsort(&int_array, array_size, sizeof(int_array[0]), int_compare);
	for (k = 0; k < array_size; k++)
		printf(" %d", int_array[k]);
	puts("");
	return (EXIT_SUCCESS);
}
```

## 兼容性

`qsort_r` 所用比较函数的参数顺序历史上与 `qsort_s` 和 GNU libc 实现的 `qsort_r` 不同。然而，自 FreeBSD 14.0 起，`qsort_r` 已更新，使 `thunk` 参数出现在最后，以匹配 IEEE Std 1003.1-2024 ("POSIX.1")。现在通过 C11 泛型选择和 C++ 多态同时接受历史接口和更新后的接口，但对于可移植应用程序推荐使用更新后的接口。

`qsort_s` 是 ISO/IEC 9899:2011 ("ISO C11") 中*可选的* Annex K 部分的一部分，可能无法移植到其他遵循标准的平台。

先前版本的 `qsort` 不允许比较例程自身调用 qsort(3)。此限制不再存在。

## 错误

`heapsort` 和 `mergesort` 函数在以下情况下失败：

**[`EINVAL`]** `size` 参数为零、`mergesort` 的 `size` 参数小于 `sizeof(void *) / 2`，或 `mergesort` 的 `nmemb` 和 `size` 参数描述了无法表示的缓冲区大小。

**[`ENOMEM`]** `heapsort` 或 `mergesort` 函数无法分配内存。

## 参见

[sort(1)](../man1/sort.1.md), [radixsort(3)](radixsort.3.md)

> Hoare, C.A.R., "Quicksort", *The Computer Journal*, 5:1, pp. 10-15, 1962.

> Williams, J.W.J, "Heapsort", *Communications of the ACM*, 7:1, pp. 347-348, 1964.

> Knuth, D.E., "Sorting and Searching", *The Art of Computer Programming*, Vol. 3, pp. 114-123, 145-149, 1968.

> McIlroy, P.M., "Optimistic Sorting and Information Theoretic Complexity", *Fourth Annual ACM-SIAM Symposium on Discrete Algorithms*, January 1992.

> Bentley, J.L., McIlroy, M.D., "Engineering a Sort Function", *Software--Practice and Experience*, Vol. 23(11), pp. 1249-1265, November 1993.

## 标准

`qsort` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`qsort_r` 函数遵循 IEEE Std 1003.1-2024 ("POSIX.1")。`qsort_s` 函数遵循 ISO/IEC 9899:2011 ("ISO C11") K.3.6.3.2。

## 历史

接受 block 作为参数的这些函数变体首次出现于 Mac OS X。此实现由 David Chisnall 创建。

在 FreeBSD 14.0 中，`qsort_r` 的原型已更新以匹配 IEEE Std 1003.1-2024 ("POSIX.1")。
