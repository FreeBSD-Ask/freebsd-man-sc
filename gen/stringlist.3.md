# stringlist(3)

`stringlist` — stringlist 操作函数

## 名称

`stringlist`, `sl_init`, `sl_add`, `sl_free`, `sl_find` — stringlist 操作函数

## 库

Lb libc

## 概要

```c
#include <stringlist.h>

StringList *
sl_init(void);

int
sl_add(StringList *sl, char *item);

void
sl_free(StringList *sl, int freeall);

char *
sl_find(StringList *sl, const char *item);
```

## 描述

`stringlist` 函数操作 stringlist，即必要时会自动扩展的字符串列表。

`StringList` 结构定义如下：

```c
typedef struct _stringlist {
	char		**sl_str;
	size_t		  sl_max;
	size_t		  sl_cur;
} StringList;
```

**`sl_str`** 指向包含列表的数组基址的指针。

**`sl_max`** `sl_str` 的大小。

**`sl_cur`** `sl_str` 中当前元素的偏移量。

以下 stringlist 操作函数可用：

**`sl_init`** 创建 stringlist。返回指向 `StringList` 的指针，失败时返回 `NULL`。

**`sl_free`** 释放 `sl` 和 `sl->sl_str` 数组占用的内存。如果 `freeall` 非零，则 `sl->sl_str` 中的每个元素也会被释放。

**`sl_add`** 将 `item` 添加到 `sl->sl_str` 的 `sl->sl_cur` 位置，扩展 `sl->sl_str` 的大小。成功时返回零，失败时返回 -1。

**`sl_find`** 在 `sl` 中查找 `item`，未找到则返回 NULL。

## 参见

free(3), malloc(3)

## 历史

`stringlist` 函数出现于 FreeBSD 2.2.6 和 NetBSD 1.3。

