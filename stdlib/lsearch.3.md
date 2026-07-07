# lsearch(3)

`lsearch` — 线性搜索与追加

## 名称

`lsearch`, `lfind`

## 库

Lb libc

## 概要

`#include <search.h>`

```c
void *
lsearch(const void *key, void *base, size_t *nelp, size_t width,
    int (*compar)(const void *, const void *));

void *
lfind(const void *key, const void *base, size_t *nelp, size_t width,
    int (*compar)(const void *, const void *));
```

## 描述

`lsearch` 和 `lfind` 函数线性地遍历一个数组，使用提供的比较函数将每个元素与待查找的元素进行比较。

`key` 参数指向一个与待查找元素相匹配的元素。数组在内存中的地址由 `base` 参数表示。一个元素的宽度（即 `sizeof` 返回的大小）作为 `width` 参数传递。数组中包含的有效元素数量（而非数组为之保留空间的元素数量）由 `nelp` 所指向的整数给出。`compar` 参数指向一个函数，该函数比较其两个参数，若匹配则返回零，否则返回非零值。

若在数组中未找到匹配元素，`lsearch` 会将 `key` 复制到最后一个元素之后的位置，并递增 `nelp` 所指向的整数。

## 返回值

`lsearch` 和 `lfind` 函数返回指向找到的第一个元素的指针。若未找到元素，`lsearch` 返回指向新添加元素的指针，而 `lfind` 返回 `NULL`。发生错误时，两个函数均返回 `NULL`。

## 实例

```c
#include <search.h>
#include <stdio.h>
#include <stdlib.h>

static int
element_compare(const void *p1, const void *p2)
{
	int left = *(const int *)p1;
	int right = *(const int *)p2;

	return (left - right);
}

int
main(int argc, char **argv)
{
	const int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	size_t element_size = sizeof(array[0]);
	size_t array_size = sizeof(array) / element_size;
	int key;
	void *element;

	printf("Enter a number: ");
	if (scanf("%d", &key) != 1) {
		printf("Bad input\n");
		return (EXIT_FAILURE);
	}

	element = lfind(&key, array, &array_size, element_size,
	    element_compare);

	if (element != NULL)
		printf("Element found: %d\n", *(int *)element);
	else
		printf("Element not found\n");

	return (EXIT_SUCCESS);
}
```

## 参见

[bsearch(3)](bsearch.3.md), hsearch(3), [tsearch(3)](tsearch.3.md)

## 标准

`lsearch` 和 `lfind` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`lsearch` 和 `lfind` 函数出现于 4.2BSD。在 FreeBSD 5.0 中，它们重新出现并遵循 IEEE Std 1003.1-2001 ("POSIX.1")。
