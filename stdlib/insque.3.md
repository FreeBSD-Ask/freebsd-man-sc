# insque.3

`insque` — 双向链表管理

## 名称

`insque`, `remque`

## 库

Lb libc

## 概要

`#include <search.h>`

```c
void
insque(void *element1, void *pred);

void
remque(void *element);
```

## 描述

`insque` 和 `remque` 函数封装了在双向链表上进行插入和删除操作这一反复出现的任务。这些函数要求其参数指向一个结构，该结构的第一个和第二个成员分别是指向下一个和上一个元素的指针。`insque` 函数还允许 `pred` 参数为 `NULL` 指针，用于初始化新链表的头元素。

## 标准

`insque` 和 `remque` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`insque` 和 `remque` 函数首次出现于 4.2BSD。在 FreeBSD 5.0 中，它们重新出现并遵循 IEEE Std 1003.1-2001 ("POSIX.1")。
