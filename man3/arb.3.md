# arb(3)

`ARB_PROTOTYPE` — 基于数组的红黑树

## 名称

`ARB_PROTOTYPE`, `ARB_PROTOTYPE_STATIC`, `ARB_PROTOTYPE_INSERT`, `ARB_PROTOTYPE_INSERT_COLOR`, `ARB_PROTOTYPE_REMOVE`, `ARB_PROTOTYPE_REMOVE_COLOR`, `ARB_PROTOTYPE_FIND`, `ARB_PROTOTYPE_NFIND`, `ARB_PROTOTYPE_NEXT`, `ARB_PROTOTYPE_PREV`, `ARB_PROTOTYPE_MINMAX`, `ARB_PROTOTYPE_REINSERT`, `ARB_GENERATE`, `ARB_GENERATE_STATIC`, `ARB_GENERATE_INSERT`, `ARB_GENERATE_INSERT_COLOR`, `ARB_GENERATE_REMOVE`, `ARB_GENERATE_REMOVE_COLOR`, `ARB_GENERATE_FIND`, `ARB_GENERATE_NFIND`, `ARB_GENERATE_NEXT`, `ARB_GENERATE_PREV`, `ARB_GENERATE_MINMAX`, `ARB_GENERATE_REINSERT`, `ARB8_ENTRY`, `ARB16_ENTRY`, `ARB32_ENTRY`, `ARB8_HEAD`, `ARB16_HEAD`, `ARB32_HEAD`, `ARB_ALLOCSIZE`, `ARB_INITIALIZER`, `ARB_ROOT`, `ARB_EMPTY`, `ARB_FULL`, `ARB_CURNODES`, `ARB_MAXNODES`, `ARB_NEXT`, `ARB_PREV`, `ARB_MIN`, `ARB_MAX`, `ARB_FIND`, `ARB_NFIND`, `ARB_LEFT`, `ARB_LEFTIDX`, `ARB_RIGHT`, `ARB_RIGHTIDX`, `ARB_PARENT`, `ARB_PARENTIDX`, `ARB_GETFREE`, `ARB_FREEIDX`, `ARB_FOREACH`, `ARB_FOREACH_FROM`, `ARB_FOREACH_SAFE`, `ARB_FOREACH_REVERSE`, `ARB_FOREACH_REVERSE_FROM`, `ARB_FOREACH_REVERSE_SAFE`, `ARB_INIT`, `ARB_INSERT`, `ARB_REMOVE`, `ARB_REINSERT`, `ARB_RESET_TREE`

## 概要

`#include <sys/arb.h>`

```c
ARB_PROTOTYPE(NAME, TYPE, FIELD, CMP);
ARB_PROTOTYPE_STATIC(NAME, TYPE, FIELD, CMP);
ARB_PROTOTYPE_INSERT(NAME, TYPE, ATTR);
ARB_PROTOTYPE_INSERT_COLOR(NAME, TYPE, ATTR);
ARB_PROTOTYPE_REMOVE(NAME, TYPE, ATTR);
ARB_PROTOTYPE_REMOVE_COLOR(NAME, TYPE, ATTR);
ARB_PROTOTYPE_FIND(NAME, TYPE, ATTR);
ARB_PROTOTYPE_NFIND(NAME, TYPE, ATTR);
ARB_PROTOTYPE_NEXT(NAME, TYPE, ATTR);
ARB_PROTOTYPE_PREV(NAME, TYPE, ATTR);
ARB_PROTOTYPE_MINMAX(NAME, TYPE, ATTR);
ARB_PROTOTYPE_REINSERT(NAME, TYPE, ATTR);
ARB_GENERATE(NAME, TYPE, FIELD, CMP);
ARB_GENERATE_STATIC(NAME, TYPE, FIELD, CMP);
ARB_GENERATE_INSERT(NAME, TYPE, FIELD, CMP, ATTR);
ARB_GENERATE_INSERT_COLOR(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_REMOVE(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_REMOVE_COLOR(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_FIND(NAME, TYPE, FIELD, CMP, ATTR);
ARB_GENERATE_NFIND(NAME, TYPE, FIELD, CMP, ATTR);
ARB_GENERATE_NEXT(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_PREV(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_MINMAX(NAME, TYPE, FIELD, ATTR);
ARB_GENERATE_REINSERT(NAME, TYPE, FIELD, CMP, ATTR);
ARB<8|16|32>_ENTRY(ENTRYNAME);
ARB<8|16|32>_HEAD(HEADNAME, TYPE);
size_t ARB_ALLOCSIZE(ARB_HEAD *head, int<8|16|32>_t maxnodes, struct TYPE *elm);
ARB_INITIALIZER(ARB_HEAD *head, int<8|16|32>_t maxnodes);
struct TYPE *ARB_ROOT(ARB_HEAD *head);
bool ARB_EMPTY(ARB_HEAD *head);
bool ARB_FULL(ARB_HEAD *head);
int<8|16|32>_t ARB_CURNODES(ARB_HEAD *head);
int<8|16|32>_t ARB_MAXNODES(ARB_HEAD *head);
struct TYPE *ARB_NEXT(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_PREV(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_MIN(NAME, ARB_HEAD *head);
struct TYPE *ARB_MAX(NAME, ARB_HEAD *head);
struct TYPE *ARB_FIND(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_NFIND(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_LEFT(struct TYPE *elm, ARB_ENTRY NAME);
int<8|16|32>_t ARB_LEFTIDX(struct TYPE *elm, ARB_ENTRY NAME);
struct TYPE *ARB_RIGHT(struct TYPE *elm, ARB_ENTRY NAME);
int<8|16|32>_t ARB_RIGHTIDX(struct TYPE *elm, ARB_ENTRY NAME);
struct TYPE *ARB_PARENT(struct TYPE *elm, ARB_ENTRY NAME);
int<8|16|32>_t ARB_PARENTIDX(struct TYPE *elm, ARB_ENTRY NAME);
struct TYPE *ARB_GETFREE(ARB_HEAD *head, FIELD);
int<8|16|32>_t ARB_FREEIDX(ARB_HEAD *head);
ARB_FOREACH(VARNAME, NAME, ARB_HEAD *head);
ARB_FOREACH_FROM(VARNAME, NAME, POS_VARNAME);
ARB_FOREACH_SAFE(VARNAME, NAME, ARB_HEAD *head, TEMP_VARNAME);
ARB_FOREACH_REVERSE(VARNAME, NAME, ARB_HEAD *head);
ARB_FOREACH_REVERSE_FROM(VARNAME, NAME, POS_VARNAME);
ARB_FOREACH_REVERSE_SAFE(VARNAME, NAME, ARB_HEAD *head, TEMP_VARNAME);
void ARB_INIT(struct TYPE *elm, FIELD, ARB_HEAD *head, int<8|16|32>_t maxnodes);
struct TYPE *ARB_INSERT(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_REMOVE(NAME, ARB_HEAD *head, struct TYPE *elm);
struct TYPE *ARB_REINSERT(NAME, ARB_HEAD *head, struct TYPE *elm);
void ARB_RESET_TREE(ARB_HEAD *head, NAME, int<8|16|32>_t maxnodes);
```

## 描述

这些宏定义了基于数组的红黑树所使用的数据结构。它们使用单块连续内存，在需要在用户空间与内核之间传递树时尤为有用。

在宏定义中，`TYPE` 是用户定义结构体的名称标签，该结构体必须包含一个类型为 `ARB_ENTRY`、名为 `ENTRYNAME` 的字段。参数 `HEADNAME` 是用户定义结构体的名称标签，必须通过 `ARB_HEAD` 宏声明。参数 `NAME` 必须是每个已定义树的唯一名称前缀。

函数原型通过 `ARB_PROTOTYPE` 或 `ARB_PROTOTYPE_STATIC` 声明。函数体由 `ARB_GENERATE` 或 `ARB_GENERATE_STATIC` 生成。关于如何使用这些宏的进一步说明，参见下文示例。

红黑树是一种以节点颜色作为附加属性的二叉搜索树。它满足一组条件：

- 从根到叶子的每条搜索路径都包含相同数量的黑色节点。
- 每个红色节点（根除外）都有黑色父节点。
- 每个叶子节点都是黑色的。

红黑树上的每个操作的时间复杂度为 `O(lg n)`。红黑树的最大高度为 `2lg n + 1`。

`ARB_*` 树要求条目以数组形式分配，并使用数组索引将条目链接在一起。因此，`ARB_*` 树条目的最大数量受数组大小与用于存储数组索引的有符号整数数据类型选择的最小值限制。使用 `ARB_ALLOCSIZE` 计算需分配的内存块大小。

红黑树由 `ARB_HEAD` 宏定义的结构体作为头部。该结构体可通过以下任一方式声明：

> `ARB<8|16|32>_HEAD(HEADNAME, TYPE)`
> `head`;

其中 `HEADNAME` 是要定义的结构体名称，而 struct `TYPE` 是要插入树中的元素类型。

`ARB_HEAD` 变体包含一个后缀，表示用于存储数组索引的有符号整数数据类型大小（以位为单位）。例如，`ARB_HEAD8` 创建一个使用 8 位有符号数组索引的红黑树头结构体，最多可索引 128 个条目。

`ARB_ENTRY` 宏声明一个结构体，使元素能够在树中相互连接。与 `ARB<8|16|32>_HEAD` 宏类似，`ARB_ENTRY` 变体包含一个后缀，表示用于存储数组索引的有符号整数数据类型大小（以位为单位）。条目应使用与其所链接的树头结构体相同的位数。

要使用操作树结构的函数，需通过 `ARB_PROTOTYPE` 或 `ARB_PROTOTYPE_STATIC` 宏声明其原型，其中 `NAME` 是该特定树的唯一标识符。`TYPE` 参数是树所管理结构体的类型。`FIELD` 参数是由 `ARB_ENTRY` 定义的元素名称。如果并非所有函数都需要，可使用 `ARB_PROTOTYPE_INSERT`、`ARB_PROTOTYPE_INSERT_COLOR`、`ARB_PROTOTYPE_REMOVE`、`ARB_PROTOTYPE_REMOVE_COLOR`、`ARB_PROTOTYPE_FIND`、`ARB_PROTOTYPE_NFIND`、`ARB_PROTOTYPE_NEXT`、`ARB_PROTOTYPE_PREV`、`ARB_PROTOTYPE_MINMAX` 和 `ARB_PROTOTYPE_REINSERT` 单独声明各个原型。各个原型宏接受 `NAME`、`TYPE` 和 `ATTR` 参数。对于全局函数，`ATTR` 参数必须为空；对于静态函数，必须为 `static`。

函数体由 `ARB_GENERATE` 或 `ARB_GENERATE_STATIC` 宏生成。这些宏接受的参数与 `ARB_PROTOTYPE` 和 `ARB_PROTOTYPE_STATIC` 宏相同，但只能使用一次。也可以使用 `ARB_GENERATE_INSERT`、`ARB_GENERATE_INSERT_COLOR`、`ARB_GENERATE_REMOVE`、`ARB_GENERATE_REMOVE_COLOR`、`ARB_GENERATE_FIND`、`ARB_GENERATE_NFIND`、`ARB_GENERATE_NEXT`、`ARB_GENERATE_PREV`、`ARB_GENERATE_MINMAX` 和 `ARB_GENERATE_REINSERT` 宏单独生成各个函数体。

最后，`CMP` 参数是用于比较树节点的函数名称。该函数接受两个 `struct TYPE *` 类型的参数。如果第一个参数小于第二个，函数返回小于零的值。如果二者相等，函数返回零。否则应返回大于零的值。比较函数定义了树元素的顺序。

`ARB_INIT` 宏初始化由 `head` 引用的树，数组长度为 `maxnodes`。

红黑树也可以使用 `ARB_INITIALIZER` 宏进行静态初始化：

> `ARB<8|16|32>_HEAD(HEADNAME, TYPE)`
> `head`
> =
> `ARB_INITIALIZER(&head, maxnodes);`

`ARB_INSERT` 宏将新元素 `elm` 插入树中。

`ARB_REMOVE` 宏从 `head` 所指向的树中删除元素 `elm`。

`ARB_FIND` 和 `ARB_NFIND` 宏可用于在树中查找特定元素。

```c
struct TYPE find, *res;
find.key = 30;
res = ARB_FIND(NAME, head, &find);
```

`ARB_ROOT`、`ARB_MIN`、`ARB_MAX`、`ARB_NEXT` 和 `ARB_PREV` 宏可用于遍历树：

```c
for (np = ARB_MIN(NAME, &head); np != NULL; np = ARB_NEXT(NAME, &head, np))
```

或者为简便起见，可使用 `ARB_FOREACH` 或 `ARB_FOREACH_REVERSE` 宏：

> `ARB_FOREACH(np, NAME, head)`

`ARB_FOREACH_SAFE` 和 `ARB_FOREACH_REVERSE_SAFE` 宏分别按正向或反向遍历由 head 引用的树，依次将每个元素赋值给 np。但与不安全版本不同的是，它们允许在循环内安全地删除 np 并释放它，而不会干扰遍历。

`ARB_FOREACH_FROM` 和 `ARB_FOREACH_REVERSE_FROM` 都可用于在中断的遍历中分别按正向或反向继续。不需要 head 指针。应将恢复遍历的起始节点指针作为其最后一个参数传递，该指针会被覆盖以提供安全遍历。

应使用 `ARB_EMPTY` 宏检查红黑树是否为空。

由于 ARB 树对条目数量有固有的上限，因此定义了一些 ARB 特有的附加宏。`ARB_FULL` 宏返回一个布尔值，指示当前树条目数是否等于树的最大值。`ARB_CURNODES` 和 `ARB_MAXNODES` 宏分别返回当前和最大条目数。`ARB_GETFREE` 宏返回指向条目数组中下一个空闲条目的指针，该条目已准备好链接到树中。如果元素成功插入树中，`ARB_INSERT` 返回 `NULL`，否则返回指向键冲突元素的指针。

相应地，`ARB_REMOVE` 返回已删除元素的指针，否则返回 `NULL` 表示出错。

`ARB_REINSERT` 宏更新元素 `elm` 在树中的位置。当以影响比较的方式修改 `tree` 的成员（例如修改节点键）时，必须调用此宏。这是删除元素再重新插入的低开销替代方案。

`ARB_RESET_TREE` 宏丢弃树拓扑。它不修改嵌入的对象值或空闲链表。

## 参见

[queue(3)](queue.3.md), [tree(3)](tree.3.md)

## 历史

`ARB` 宏首次出现于 FreeBSD 13.0。

## 作者

`ARB` 宏由 Lawrence Stewart <lstewart@FreeBSD.org> 实现，基于 Niels Provos 编写的 [tree(3)](tree.3.md) 宏。
