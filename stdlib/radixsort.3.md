# radixsort(3)

`radixsort` — 基数排序

## 名称

`radixsort`

## 库

Lb libc

## 概要

`#include <limits.h>`

`#include <stdlib.h>`

```c
int
radixsort(const unsigned char **base, int nmemb,
    const unsigned char *table, unsigned endbyte);

int
sradixsort(const unsigned char **base, int nmemb,
    const unsigned char *table, unsigned endbyte);
```

## 描述

`radixsort` 和 `sradixsort` 函数是基数排序的实现。

这些函数对由指向字节串的指针组成的数组进行排序，数组的初始成员由 `base` 引用。字节串可包含任何值；每个字符串的末尾由用户指定的值 `endbyte` 标记。

应用可通过提供 `table` 参数指定排序顺序。如果 `table` 非 `NULL`，它必须引用一个 `UCHAR_MAX` + 1 字节的数组，其中包含每个可能字节值的排序权重。字符串结束字节必须具有 0 或 255 的排序权重（用于逆序排序）。多个字节可具有相同的排序权重。`table` 参数对于希望将不同字符同等排序的应用非常有用，例如，提供一个将 A-Z 与 a-z 赋予相同权重的表将实现不区分大小写的排序。如果 `table` 为 NULL，数组内容按其引用的字节串的 ASCII 顺序升序排序，`endbyte` 的排序权重为 0。

`sradixsort` 函数是稳定的，即如果两个元素比较相等，它们在排序后数组中的顺序不变。`sradixsort` 函数使用足以容纳 `nmemb` 个指针的额外内存。

`radixsort` 函数不稳定，但不使用额外内存。

这些函数是最高有效位基数排序的变体；具体参见 D.E. Knuth 的 Algorithm R 和 5.2.5 节练习 10。它们相对于字符串中的字节数耗时为线性时间。

## 返回值

`radixsort` 和 `sradixsort` 函数成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**[`EINVAL`]** `table` 的 `endbyte` 元素的值不是 0 或 255。

此外，`sradixsort` 函数可能失败并设置 `errno` 为库例程 malloc(3) 所指定的任何错误。

## 参见

[sort(1)](../man1/sort.1.md), [qsort(3)](qsort.3.md)

> Knuth, D.E., "Sorting and Searching", *The Art of Computer Programming*, Vol. 3, pp. 170-178, 1968.

> Paige, R., "Three Partition Refinement Algorithms", *SIAM J. Comput.*, Vol. 16, No. 6, 1987.

> McIlroy, P., "Computing Systems", *Engineering Radix Sort*, Vol. 6:1, pp. 5-27, 1993.

## 历史

`radixsort` 函数首次出现于 4.4BSD。
