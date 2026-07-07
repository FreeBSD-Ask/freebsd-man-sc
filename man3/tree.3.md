# tree(3)

`SPLAY_PROTOTYPE` — 伸展树和秩平衡（wavl）树的实现

## 名称

`SPLAY_PROTOTYPE`, `SPLAY_GENERATE`, `SPLAY_ENTRY`, `SPLAY_HEAD`, `SPLAY_INITIALIZER`, `SPLAY_ROOT`, `SPLAY_EMPTY`, `SPLAY_NEXT`, `SPLAY_MIN`, `SPLAY_MAX`, `SPLAY_FIND`, `SPLAY_LEFT`, `SPLAY_RIGHT`, `SPLAY_FOREACH`, `SPLAY_INIT`, `SPLAY_INSERT`, `SPLAY_REMOVE`, `RB_PROTOTYPE`, `RB_PROTOTYPE_STATIC`, `RB_PROTOTYPE_INSERT`, `RB_PROTOTYPE_INSERT_COLOR`, `RB_PROTOTYPE_REMOVE`, `RB_PROTOTYPE_REMOVE_COLOR`, `RB_PROTOTYPE_FIND`, `RB_PROTOTYPE_NFIND`, `RB_PROTOTYPE_NEXT`, `RB_PROTOTYPE_PREV`, `RB_PROTOTYPE_MINMAX`, `RB_PROTOTYPE_REINSERT`, `RB_GENERATE`, `RB_GENERATE_STATIC`, `RB_GENERATE_INSERT`, `RB_GENERATE_INSERT_COLOR`, `RB_GENERATE_REMOVE`, `RB_GENERATE_REMOVE_COLOR`, `RB_GENERATE_FIND`, `RB_GENERATE_NFIND`, `RB_GENERATE_NEXT`, `RB_GENERATE_PREV`, `RB_GENERATE_MINMAX`, `RB_GENERATE_REINSERT`, `RB_ENTRY`, `RB_HEAD`, `RB_INITIALIZER`, `RB_ROOT`, `RB_EMPTY`, `RB_NEXT`, `RB_PREV`, `RB_MIN`, `RB_MAX`, `RB_FIND`, `RB_NFIND`, `RB_LEFT`, `RB_RIGHT`, `RB_PARENT`, `RB_FOREACH`, `RB_FOREACH_FROM`, `RB_FOREACH_SAFE`, `RB_FOREACH_REVERSE`, `RB_FOREACH_REVERSE_FROM`, `RB_FOREACH_REVERSE_SAFE`, `RB_INIT`, `RB_INSERT`, `RB_INSERT_NEXT`, `RB_INSERT_PREV`, `RB_REMOVE`, `RB_REINSERT`, `RB_AUGMENT`, `RB_AUGMENT_CHECK`, `RB_UPDATE_AUGMENT`

## 概要

```c
#include <sys/tree.h>
```

## 描述

这些宏定义了不同类型的树数据结构：伸展树和秩平衡（wavl）树。

在宏定义中，`TYPE` 是用户定义结构的名称标签，该结构必须包含一个类型为 `SPLAY_ENTRY` 或 `RB_ENTRY`、名为 `ENTRYNAME` 的字段。参数 `HEADNAME` 是用户定义结构的名称标签，必须使用宏 `SPLAY_HEAD()` 或 `RB_HEAD()` 声明。参数 `NAME` 对于定义的每棵树必须是唯一的名称前缀。

函数原型通过 `SPLAY_PROTOTYPE()`、`RB_PROTOTYPE()` 或 `RB_PROTOTYPE_STATIC()` 声明。函数体通过 `SPLAY_GENERATE()`、`RB_GENERATE()` 或 `RB_GENERATE_STATIC()` 生成。有关这些宏使用方法的进一步说明，请参见下面的示例。

## 伸展树

伸展树是一种自组织数据结构。对树的每次操作都会导致伸展发生。伸展将请求的节点移动到树的根部，并部分重新平衡它。

这样做的好处是请求局部性会导致更快的查找，因为请求的节点会移动到树的顶部。另一方面，每次查找都会导致内存写入。

平衡定理将 `m` 次操作和 `n` 次插入在初始空树上的总访问时间限定为 O(m + n lg n)。对伸展树进行 `m` 次访问序列的摊还成本为 O(lg n)。

伸展树以由 `SPLAY_HEAD()` 宏定义的结构作为头部。结构声明如下：

`SPLAY_HEAD(HEADNAME, TYPE)` `head`;

其中 `HEADNAME` 是要定义的结构名称，struct `TYPE` 是要插入树中的元素类型。

`SPLAY_ENTRY()` 宏声明允许元素在树中连接的结构。

为了使用操作树结构的函数，需要使用 `SPLAY_PROTOTYPE()` 宏声明其原型，其中 `NAME` 是此特定树的唯一标识符。`TYPE` 参数是树管理的结构类型。`FIELD` 参数是由 `SPLAY_ENTRY()` 定义的元素名称。

函数体通过 `SPLAY_GENERATE()` 宏生成。它接受与 `SPLAY_PROTOTYPE()` 宏相同的参数，但只应使用一次。

最后，`CMP` 参数是用于比较树节点的函数名称。该函数接受两个 `struct TYPE *` 类型的参数。如果第一个参数小于第二个，函数返回小于零的值。如果相等，函数返回零。否则，应返回大于零的值。比较函数定义了树元素的顺序。

`SPLAY_INIT()` 宏初始化由 `head` 引用的树。

伸展树也可以使用 `SPLAY_INITIALIZER()` 宏静态初始化，如下所示：

`SPLAY_HEAD(HEADNAME, TYPE)` `head` = `SPLAY_INITIALIZER(&head)`;

`SPLAY_INSERT()` 宏将新元素 `elm` 插入树中。

`SPLAY_REMOVE()` 宏从 `head` 指向的树中删除元素 `elm`。

`SPLAY_FIND()` 宏可用于在树中查找特定元素。

```c
struct TYPE find, *res;
find.key = 30;
res = SPLAY_FIND(NAME, head, &find);
```

`SPLAY_ROOT()`、`SPLAY_MIN()`、`SPLAY_MAX()` 和 `SPLAY_NEXT()` 宏可用于遍历树：

```c
for (np = SPLAY_MIN(NAME, &head); np != NULL; np = SPLAY_NEXT(NAME, &head, np))
```

或者，为简便起见，可以使用 `SPLAY_FOREACH()` 宏：

`SPLAY_FOREACH(np, NAME, head)`

应使用 `SPLAY_EMPTY()` 宏检查伸展树是否为空。

## 秩平衡树

秩平衡（RB）树是定义高度平衡二叉搜索树（包括 AVL 和红黑树）的框架。每个树节点都有相关的秩。平衡条件通过任何节点与其子节点之间的秩差条件表示。秩差存储在每个树节点中。

RB 宏实现的平衡条件产生弱 AVL（wavl）树，结合了 AVL 和红黑树的最佳特性。wavl 树在插入后的重新平衡方式与 AVL 树相同，具有与红黑树相同的最坏情况时间，并且生成的树具有更好的平衡性。wavl 树在删除后的重新平衡方式所需的重构比 AVL 或红黑树都少。删除可能导致树几乎像红黑树一样不平衡；插入导致树变得像 AVL 树一样平衡。

秩平衡树以由 `RB_HEAD()` 宏定义的结构作为头部。结构声明如下：

`RB_HEAD(HEADNAME, TYPE)` `head`;

其中 `HEADNAME` 是要定义的结构名称，struct `TYPE` 是要插入树中的元素类型。

`RB_ENTRY()` 宏声明允许元素在树中连接的结构。

为了使用操作树结构的函数，需要使用 `RB_PROTOTYPE()` 或 `RB_PROTOTYPE_STATIC()` 宏声明其原型，其中 `NAME` 是此特定树的唯一标识符。`TYPE` 参数是树管理的结构类型。`FIELD` 参数是由 `RB_ENTRY()` 定义的元素名称。如果并非所有函数都需要，可以使用 `RB_PROTOTYPE_INSERT()`、`RB_PROTOTYPE_INSERT_COLOR()`、`RB_PROTOTYPE_REMOVE()`、`RB_PROTOTYPE_REMOVE_COLOR()`、`RB_PROTOTYPE_FIND()`、`RB_PROTOTYPE_NFIND()`、`RB_PROTOTYPE_NEXT()`、`RB_PROTOTYPE_PREV()`、`RB_PROTOTYPE_MINMAX()` 和 `RB_PROTOTYPE_REINSERT()` 声明单个原型。单个原型宏需要 `NAME`、`TYPE` 和 `ATTR` 参数。`ATTR` 参数对于全局函数必须为空，对于静态函数必须为 `static`。

函数体通过 `RB_GENERATE()` 或 `RB_GENERATE_STATIC()` 宏生成。这些宏接受与 `RB_PROTOTYPE()` 和 `RB_PROTOTYPE_STATIC()` 宏相同的参数，但只应使用一次。作为替代，可以通过 `RB_GENERATE_INSERT()`、`RB_GENERATE_INSERT_COLOR()`、`RB_GENERATE_REMOVE()`、`RB_GENERATE_REMOVE_COLOR()`、`RB_GENERATE_FIND()`、`RB_GENERATE_NFIND()`、`RB_GENERATE_NEXT()`、`RB_GENERATE_PREV()`、`RB_GENERATE_MINMAX()` 和 `RB_GENERATE_REINSERT()` 宏生成单个函数体。

最后，`CMP` 参数是用于比较树节点的函数名称。该函数接受两个 `struct TYPE *` 类型的参数。如果第一个参数小于第二个，函数返回小于零的值。如果相等，函数返回零。否则，应返回大于零的值。比较函数定义了树元素的顺序。

`RB_INIT()` 宏初始化由 `head` 引用的树。

秩平衡树也可以使用 `RB_INITIALIZER()` 宏静态初始化，如下所示：

`RB_HEAD(HEADNAME, TYPE)` `head` = `RB_INITIALIZER(&head)`;

`RB_INSERT()` 宏将新元素 `elm` 插入树中。

`RB_INSERT_NEXT()` 宏将新元素 `elm` 紧接在给定元素之后插入树中。

`RB_INSERT_PREV()` 宏将新元素 `elm` 紧接在给定元素之前插入树中。

`RB_REMOVE()` 宏从 `head` 指向的树中删除元素 `elm`。

`RB_FIND()` 和 `RB_NFIND()` 宏可用于在树中查找特定元素。

`RB_FIND()` 宏返回树中等于所提供键的元素，如果没有这样的元素则返回 `NULL`。

`RB_NFIND()` 宏返回大于或等于所提供键的最小元素，如果没有这样的元素则返回 `NULL`。

```c
struct TYPE find, *res, *resn;
find.key = 30;
res = RB_FIND(NAME, head, &find);
resn = RB_NFIND(NAME, head, &find);
```

`RB_ROOT()`、`RB_MIN()`、`RB_MAX()`、`RB_NEXT()` 和 `RB_PREV()` 宏可用于遍历树：

```c
for (np = RB_MIN(NAME, &head); np != NULL; np = RB_NEXT(NAME, &head, np))
```

或者，为简便起见，可以使用 `RB_FOREACH()` 或 `RB_FOREACH_REVERSE()` 宏：

`RB_FOREACH(np, NAME, head)`

`RB_FOREACH_SAFE()` 和 `RB_FOREACH_REVERSE_SAFE()` 宏分别正向和反向遍历由 head 引用的树，依次将每个元素赋值给 np。然而，与它们的不安全对应版本不同，它们允许在循环内安全地删除 np 并释放它，而不会干扰遍历。

`RB_FOREACH_FROM()` 和 `RB_FOREACH_REVERSE_FROM()` 都可用于在中断的正向或反向遍历中继续。不需要头指针。应将恢复遍历的节点指针作为它们的最后一个参数传递，该指针将被覆盖以提供安全遍历。

应使用 `RB_EMPTY()` 宏检查秩平衡树是否为空。

`RB_REINSERT()` 宏更新元素 `elm` 在树中的位置。如果以影响比较的方式修改了 `tree` 的成员（例如修改节点键），则必须调用此宏。这是删除元素并重新插入的更低开销替代方案。

`RB_AUGMENT()` 宏更新树中元素 `elm` 的增强数据。默认情况下，它没有任何效果。不打算由 RB 用户调用。如果 `RB_AUGMENT()` 由 RB 用户定义，则当从树中插入或删除元素时，它会被树中作为已更改子树根的每个元素调用，从树底部向上工作。它通常用于维护树元素的某些关联累积，如总和、最小值、最大值等。

`RB_AUGMENT_CHECK()` 宏更新树中元素 `elm` 的增强数据。默认情况下，它什么也不做并返回 false。如果 `RB_AUGMENT_CHECK()` 已定义，则当从树中插入或删除元素时，它会被树中作为已更改子树根的每个元素调用，从树底部向上工作，直到它返回 false 表示未更改元素，因此进一步向上工作树不会更改任何内容。它通常用于维护树元素的某些关联累积，如总和、最小值、最大值等。

`RB_UPDATE_AUGMENT()` 宏更新树中元素 `elm` 及其祖先的增强数据。如果 `RB_AUGMENT()` 由 RB 用户定义，则当树中的元素被更改（不改变树中项的顺序）时，对该元素调用此函数会恢复树增强状态的一致性，如同该元素已被删除并重新插入。

## 实例

以下示例演示如何声明一个持有整数的秩平衡树。向其中插入值，并按顺序打印树的内容。为维护树中值的总和，每个元素维护其值及其左右子树的总和。最后，打印树的内部结构。

```c
#define RB_AUGMENT(entry) sumaug(entry)
#include <sys/tree.h>
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
struct node {
	RB_ENTRY(node) entry;
	int i, sum;
};
int
intcmp(struct node *e1, struct node *e2)
{
	return (e1->i < e2->i ? -1 : e1->i > e2->i);
}
void
sumaug(struct node *e)
{
	e->sum = e->i;
	if (RB_LEFT(e, entry) != NULL)
		e->sum += RB_LEFT(e, entry)->sum;
	if (RB_RIGHT(e, entry) != NULL)
		e->sum += RB_RIGHT(e, entry)->sum;
}
RB_HEAD(inttree, node) head = RB_INITIALIZER(&head);
RB_GENERATE(inttree, node, entry, intcmp)
int testdata[] = {
	20, 16, 17, 13, 3, 6, 1, 8, 2, 4, 10, 19, 5, 9, 12, 15, 18,
	7, 11, 14
};
void
print_tree(struct node *n)
{
	struct node *left, *right;
	if (n == NULL) {
		printf("nil");
		return;
	}
	left = RB_LEFT(n, entry);
	right = RB_RIGHT(n, entry);
	if (left == NULL && right == NULL)
		printf("%d", n->i);
	else {
		printf("%d(", n->i);
		print_tree(left);
		printf(",");
		print_tree(right);
		printf(")");
	}
}
int
main(void)
{
	int i;
	struct node *n;
	for (i = 0; i < sizeof(testdata) / sizeof(testdata[0]); i++) {
		if ((n = malloc(sizeof(struct node))) == NULL)
			err(1, NULL);
		n->i = testdata[i];
		RB_INSERT(inttree, &head, n);
	}
	RB_FOREACH(n, inttree, &head) {
		printf("%d\n", n->i);
	}
	print_tree(RB_ROOT(&head));
	printf("\nSum of values = %d\n", RB_ROOT(&head)->sum);
	return (0);
}
```

## 注释

以下方式释放树是一个常见错误：

```c
SPLAY_FOREACH(var, NAME, head) {
	SPLAY_REMOVE(NAME, head, var);
	free(var);
}
free(head);
```

由于 `var` 被释放，`FOREACH()` 宏引用的指针可能已被重新分配。正确的代码需要第二个变量。

```c
for (var = SPLAY_MIN(NAME, head); var != NULL; var = nxt) {
	nxt = SPLAY_NEXT(NAME, head, var);
	SPLAY_REMOVE(NAME, head, var);
	free(var);
}
```

`RB_INSERT()` 和 `SPLAY_INSERT()` 在元素成功插入树中时返回 `NULL`，否则返回具有冲突键的元素指针。

相应地，`RB_REMOVE()` 和 `SPLAY_REMOVE()` 返回被删除元素的指针，否则返回 `NULL` 表示错误。

## 参见

[arb(3)](arb.3.md), [queue(3)](queue.3.md)

> Bernhard Haeupler, Siddhartha Sen, Robert E. Tarjan, "Rank-Balanced Trees", *ACM Transactions on Algorithms*, 11, 4, June 2015。

## 历史

树宏首次出现于 FreeBSD 4.6。

## 作者

树宏的作者是 Niels Provos。
