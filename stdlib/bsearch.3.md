# bsearch(3)

`bsearch` — 对已排序表进行二分查找

## 名称

`bsearch`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void *
bsearch(const void *key, const void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *));
```

## 描述

`bsearch` 函数在一个包含 `nmemb` 个对象的数组中查找与 `key` 所指对象匹配的成员，`base` 指向该数组的初始成员。数组中每个成员的大小由 `size` 指定。

数组的内容应按照 `compar` 所引用的比较函数以升序排列。`compar` 例程应有两个参数，分别指向 `key` 对象和一个数组成员（按此顺序），当 `key` 对象分别小于、匹配或大于该数组成员时，应返回一个小于、等于或大于零的整数。参见 [qsort(3)](qsort.3.md) 中的 `int_compare` 示例函数，它也是一个与 `bsearch` 兼容的比较函数。

## 返回值

`bsearch` 函数返回指向数组中匹配成员的指针，若未找到匹配项则返回空指针。如果两个成员比较结果相等，匹配哪一个成员是未指定的。

## 实例

以下示例程序在已排序数组中按年龄查找人员：

```c
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct person {
	const char 	*name;
	int 		age;
};

static int
compare(const void *a, const void *b)
{
	const int *age;
	const struct person *person;

	age = a;
	person = b;

	return (*age - person->age);
}

int
main(void)
{
	struct person *friend;
	int age;
	/* 已排序数组 */
	const struct person friends[] = {
		{ "paul", 22 },
		{ "anne", 25 },
		{ "fred", 25 },
		{ "mary", 27 },
		{ "mark", 35 },
		{ "bill", 50 }
	};
	const size_t len = sizeof(friends) / sizeof(friends[0]);

	age = 22;
	friend = bsearch(&age, friends, len, sizeof(friends[0]), compare);
	assert(strcmp(friend->name, "paul") == 0);
	printf("name: %s\nage: %d\n", friend->name, friend->age);

	age = 25;
	friend = bsearch(&age, friends, len, sizeof(friends[0]), compare);
	/*
	 * 对于具有相同键的多个元素，返回哪一个由实现定义
	 */
	assert(strcmp(friend->name, "fred") == 0 ||
	    strcmp(friend->name, "anne") == 0);
	printf("name: %s\nage: %d\n", friend->name, friend->age);

	age = 30;
	friend = bsearch(&age, friends, len, sizeof(friends[0]), compare);
	assert(friend == NULL);
	printf("friend aged 30 not found\n");
}
```

## 参见

db(3), [lsearch(3)](lsearch.3.md), [qsort(3)](qsort.3.md)

## 标准

`bsearch` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
