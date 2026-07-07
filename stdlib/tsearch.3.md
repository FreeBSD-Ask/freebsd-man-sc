# tsearch(3)

`tsearch` — 操作二叉搜索树

## 名称

`tsearch`, `tfind`, `tdelete`, `twalk`

## 概要

`#include <search.h>`

```c
void *
tdelete(const void * restrict key, posix_tnode ** restrict rootp,
    int (*compar)(const void *, const void *));

void
tdestroy(posix_tnode *root, void (*node_free)(void *));

posix_tnode *
tfind(const void *key, posix_tnode * const *rootp,
    int (*compar)(const void *, const void *));

posix_tnode *
tsearch(const void *key, posix_tnode **rootp,
    int (*compar)(const void *, const void *));

void
twalk(const posix_tnode *root,
    void (*action)(const posix_tnode *, VISIT, int));
```

## 描述

`tdelete`、`tdestroy`、`tfind`、`tsearch` 和 `twalk` 函数用于管理二叉搜索树。本实现使用平衡 AVL 树，由于其对树高度有严格的理论限制，因此具有调用比较函数次数相对较少的优势。

用户传入的比较函数具有与 strcmp(3) 相同风格的返回值。

`tfind` 函数在以 `rootp` 为根的二叉树中搜索与参数 `key` 匹配的数据项，找到时返回指向该数据项的指针，未找到时返回 NULL。

`tsearch` 函数与 `tfind` 相同，区别在于若未找到匹配项，`key` 将被插入树中并返回指向它的指针。若 `rootp` 指向 NULL 值，则创建一棵新的二叉搜索树。

`tdelete` 函数从指定的二叉搜索树中删除一个节点，并返回指向被删除节点父节点的指针。它接受与 `tfind` 和 `tsearch` 相同的参数。若被删除的节点是二叉搜索树的根节点，`rootp` 将被调整。

`tdestroy` 函数销毁整棵搜索树，释放所有已分配的节点。若树键在释放时需要特殊处理，可以提供 `node_free` 函数，该函数将对每个键调用。

`twalk` 函数遍历以 `root` 为根的二叉搜索树，并对每个节点调用 `action` 函数。`action` 函数以三个参数调用：指向当前节点的指针、一个来自枚举 `typedef enum { preorder, postorder, endorder, leaf } VISIT;` 的值（指定遍历类型）、以及一个节点层级（其中层级零为树的根）。

## 返回值

`tsearch` 函数在新节点分配失败时返回 NULL（通常由于可用内存不足）。

`tfind`、`tsearch` 和 `tdelete` 函数在 `rootp` 为 NULL 或找不到数据项时返回 NULL。

`twalk` 和 `tdestroy` 函数不返回值。

## 实例

本示例使用 `tsearch` 在 `root` 中搜索四个字符串。由于这些字符串尚不存在，它们会被添加。对第四个字符串调用 `tsearch` 两次，以演示当字符串已存在时不会被重复添加。使用 `tfind` 查找第四个字符串的唯一实例，再用 `tdelete` 将其删除。最后，使用 `twalk` 返回并显示生成的二叉搜索树。

```c
#include <stdio.h>
#include <search.h>
#include <string.h>

int
comp(const void *a, const void *b)
{

	return strcmp(a, b);
}

void
printwalk(const posix_tnode * node, VISIT v, int __unused0)
{

	if (v == postorder || v == leaf) {
		printf("node: %s\n", *(char **)node);
	}
}

int
main(void)
{
	posix_tnode *root = NULL;

	char one[] = "blah1";
	char two[] = "blah-2";
	char three[] = "blah-3";
	char four[] = "blah-4";

	tsearch(one, &root, comp);
	tsearch(two, &root, comp);
	tsearch(three, &root, comp);
	tsearch(four, &root, comp);
	tsearch(four, &root, comp);
	printf("four: %s\n", *(char **)tfind(four, &root, comp));
	tdelete(four, &root, comp);

	twalk(root, printwalk);
	tdestroy(root, NULL);
	return 0;
}
```

## 参见

[bsearch(3)](bsearch.3.md), hsearch(3), [lsearch(3)](lsearch.3.md)

## 标准

`tdelete`、`tfind`、`tsearch` 和 `twalk` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。`tdestroy` 函数是 glibc 扩展。

`posix_tnode` 类型不属于 IEEE Std 1003.1-2008 ("POSIX.1")，但预计将由未来版本的标准予以标准化。它被定义为 `void` 以实现源码级兼容。使用 `posix_tnode` 可以更方便地区分节点和键。
