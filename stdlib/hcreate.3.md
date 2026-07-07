# hcreate(3)

`hcreate` — 管理哈希搜索表

## 名称

`hcreate`, `hcreate_r`, `hdestroy`, `hdestroy_r`, `hsearch`, `hsearch_r`

## 库

Lb libc

## 概要

`#include <search.h>`

```c
int
hcreate(size_t nel);

int
hcreate_r(size_t nel, struct hsearch_data *table);

void
hdestroy(void);

void
hdestroy_r(struct hsearch_data *table);

ENTRY *
hsearch(ENTRY item, ACTION action);

int
hsearch_r(ENTRY item, ACTION action, ENTRY **itemp,
    struct hsearch_data *table);
```

## 描述

`hcreate`、`hcreate_r`、`hdestroy`、`hdestroy_r`、`hsearch` 和 `hsearch_r` 函数用于管理哈希搜索表。

`hcreate` 函数为表分配足够的空间，应用程序应确保在使用 `hsearch` 之前调用它。`nel` 参数是表中应包含的最大条目数的估计值。由于本实现会动态调整哈希表大小，该参数被忽略。

`hdestroy` 函数释放搜索表，之后可以再次调用 `hcreate`。调用 `hdestroy` 后，数据不再可访问。`hdestroy` 函数释放搜索表，但不会释放其中存储的比较键或数据项。调用者负责在调用 `hdestroy` 之前释放与表条目关联的任何内存。

`hsearch` 函数是一个哈希表搜索例程。它返回一个指向哈希表中可找到条目位置的指针。`item` 参数是一个 `ENTRY` 类型的结构（定义于 `search.h` 头文件中），包含两个指针：`item.key` 指向比较键（`char *`），`item.data`（`void *`）指向与该键关联的其他数据。`hsearch` 使用的比较函数是 strcmp(3)。`action` 参数是枚举类型 `ACTION` 的成员，指示当条目在表中找不到时的处理方式。`ENTER` 表示应将 `item` 插入表中适当位置。`FIND` 表示不应创建条目。返回 `NULL` 指针表示查找未成功。

若 `action` 为 `ENTER` 且调用了 `hdestroy`，则传给 `hsearch` 的比较键（作为 `item.key` 传递）必须使用 malloc(3) 分配。

`hcreate_r`、`hdestroy_r` 和 `hsearch_r` 函数是上述函数的可重入版本，可在用户提供的表上操作。`hsearch_r` 函数在 `action` 为 `ENTER` 且无法创建元素时返回 `0`，否则返回 `1`。若元素存在或可以创建，它将被置于 `itemp` 中，否则 `itemp` 将被设置为 `NULL`。

## 返回值

`hcreate` 和 `hcreate_r` 函数在表创建失败时返回 0，并设置全局变量 `errno` 以指示错误；否则返回非零值。

`hdestroy` 和 `hdestroy_r` 函数不返回值。

`hsearch` 和 `hsearch_r` 函数在 `action` 为 `FIND` 且找不到 `item`，或 `action` 为 `ENTER` 且表已满时返回 `NULL` 指针。

## 实例

以下示例读取字符串和随后的两个数字，将它们存入哈希表，丢弃重复项。然后读取字符串并在哈希表中查找匹配的条目并打印出来。

```c
#include <stdio.h>
#include <search.h>
#include <string.h>
#include <stdlib.h>
struct info {			/* 这是表中存储的信息 */
	int age, room;		/* 除键以外的数据 */
};
#define NUM_EMPL	5000	/* 搜索表中的元素数量 */
int
main(void)
{
	char str[BUFSIZ]; /* 读取字符串的空间 */
	struct info info_space[NUM_EMPL]; /* 存储员工信息的空间 */
	struct info *info_ptr = info_space; /* info_space 中的下一个位置 */
	ENTRY item;
	ENTRY *found_item; /* 要在表中查找的名称 */
	char name_to_find[30];
	int i = 0;
	/* 创建表；不执行错误检查 */
	(void) hcreate(NUM_EMPL);
	while (scanf("%s%d%d", str, &info_ptr->age,
	    &info_ptr->room) != EOF && i++ < NUM_EMPL) {
		/* 将信息放入结构，再将结构放入条目 */
		item.key = strdup(str);
		item.data = info_ptr;
		info_ptr++;
		/* 将条目放入表 */
		(void) hsearch(item, ENTER);
	}
	/* 访问表 */
	item.key = name_to_find;
	while (scanf("%s", item.key) != EOF) {
		if ((found_item = hsearch(item, FIND)) != NULL) {
			/* 若条目在表中 */
			(void)printf("found %s, age = %d, room = %d\n",
			    found_item->key,
			    ((struct info *)found_item->data)->age,
			    ((struct info *)found_item->data)->room);
		} else
			(void)printf("no such employee %s\n", name_to_find);
	}
	hdestroy();
	return 0;
}
```

## 错误

`hcreate`、`hcreate_r`、`hsearch` 和 `hsearch_r` 函数在以下情况下将失败：

**[`ENOMEM`]** 可用内存不足。

`hsearch` 和 `hsearch_r` 函数在 `action` 为 `FIND` 且未找到元素时还会失败：

**[`ESRCH`]** 未找到给定的 `item`。

## 参见

[bsearch(3)](bsearch.3.md), [lsearch(3)](lsearch.3.md), malloc(3), strcmp(3), [tsearch(3)](tsearch.3.md)

## 标准

`hcreate`、`hdestroy` 和 `hsearch` 函数遵循 -xpg4.2。

## 历史

`hcreate`、`hdestroy` 和 `hsearch` 函数首次出现于 AT&T System V UNIX。`hcreate_r`、`hdestroy_r` 和 `hsearch_r` 函数是 GNU 扩展。

## 缺陷

原始的非 GNU 接口一次只允许使用一个哈希表。
