# queue(3)

`SLIST_CLASS_ENTRY` — 单链表、单链尾队列、列表和尾队列的实现

## 名称

`SLIST_CLASS_ENTRY`, `SLIST_CLASS_HEAD`, `SLIST_CONCAT`, `SLIST_EMPTY`, `SLIST_EMPTY_ATOMIC`, `SLIST_ENTRY`, `SLIST_FIRST`, `SLIST_FOREACH`, `SLIST_FOREACH_FROM`, `SLIST_FOREACH_FROM_SAFE`, `SLIST_FOREACH_SAFE`, `SLIST_HEAD`, `SLIST_HEAD_INITIALIZER`, `SLIST_INIT`, `SLIST_INSERT_AFTER`, `SLIST_INSERT_HEAD`, `SLIST_NEXT`, `SLIST_REMOVE`, `SLIST_REMOVE_AFTER`, `SLIST_REMOVE_HEAD`, `SLIST_SPLIT_AFTER`, `SLIST_SWAP`, `STAILQ_CLASS_ENTRY`, `STAILQ_CLASS_HEAD`, `STAILQ_CONCAT`, `STAILQ_EMPTY`, `STAILQ_EMPTY_ATOMIC`, `STAILQ_ENTRY`, `STAILQ_FIRST`, `STAILQ_FOREACH`, `STAILQ_FOREACH_FROM`, `STAILQ_FOREACH_FROM_SAFE`, `STAILQ_FOREACH_SAFE`, `STAILQ_HEAD`, `STAILQ_HEAD_INITIALIZER`, `STAILQ_INIT`, `STAILQ_INSERT_AFTER`, `STAILQ_INSERT_HEAD`, `STAILQ_INSERT_TAIL`, `STAILQ_LAST`, `STAILQ_NEXT`, `STAILQ_REMOVE`, `STAILQ_REMOVE_AFTER`, `STAILQ_REMOVE_HEAD`, `STAILQ_REVERSE`, `STAILQ_SPLIT_AFTER`, `STAILQ_SWAP`, `LIST_CLASS_ENTRY`, `LIST_CLASS_HEAD`, `LIST_CONCAT`, `LIST_EMPTY`, `LIST_EMPTY_ATOMIC`, `LIST_ENTRY`, `LIST_FIRST`, `LIST_FOREACH`, `LIST_FOREACH_FROM`, `LIST_FOREACH_FROM_SAFE`, `LIST_FOREACH_SAFE`, `LIST_HEAD`, `LIST_HEAD_INITIALIZER`, `LIST_INIT`, `LIST_INSERT_AFTER`, `LIST_INSERT_BEFORE`, `LIST_INSERT_HEAD`, `LIST_NEXT`, `LIST_PREV`, `LIST_REMOVE`, `LIST_REPLACE`, `LIST_SPLIT_AFTER`, `LIST_SWAP`, `TAILQ_CLASS_ENTRY`, `TAILQ_CLASS_HEAD`, `TAILQ_CONCAT`, `TAILQ_EMPTY`, `TAILQ_EMPTY_ATOMIC`, `TAILQ_ENTRY`, `TAILQ_FIRST`, `TAILQ_FOREACH`, `TAILQ_FOREACH_FROM`, `TAILQ_FOREACH_FROM_SAFE`, `TAILQ_FOREACH_REVERSE`, `TAILQ_FOREACH_REVERSE_FROM`, `TAILQ_FOREACH_REVERSE_FROM_SAFE`, `TAILQ_FOREACH_REVERSE_SAFE`, `TAILQ_FOREACH_SAFE`, `TAILQ_HEAD`, `TAILQ_HEAD_INITIALIZER`, `TAILQ_INIT`, `TAILQ_INSERT_AFTER`, `TAILQ_INSERT_BEFORE`, `TAILQ_INSERT_HEAD`, `TAILQ_INSERT_TAIL`, `TAILQ_LAST`, `TAILQ_NEXT`, `TAILQ_PREV`, `TAILQ_REMOVE`, `TAILQ_REPLACE`, `TAILQ_SPLIT_AFTER`, `TAILQ_SWAP`

## 概要

`#include <sys/queue.h>`

## 描述

这些宏定义并操作四种类型的数据结构，可在 C 和 C++ 源代码中使用：

- 列表
- 单链表
- 单链尾队列
- 尾队列

所有四种结构都支持以下功能：

- 在列表头部插入新条目。
- 在列表中的任何元素之后插入新条目。
- O(1) 时间从列表头部删除条目。
- 正向遍历列表。
- 在列表中的任何元素之后将列表拆分为两个。
- 交换两个列表的内容。

单链表是四种数据结构中最简单的，仅支持上述功能。单链表适用于具有大型数据集且很少或没有删除操作的应用，或者用于实现 LIFO 队列。单链表还增加以下功能：

- O(n) 时间删除列表中的任何条目。
- O(n) 时间连接两个列表。

单链尾队列增加以下功能：

- 可以在列表末尾添加条目。
- O(n) 时间删除列表中的任何条目。
- 可以进行连接。

但是：

- 所有列表插入操作都必须指定列表头。
- 每个头条目需要两个指针而非一个。
- 代码量大约增加 15%，操作速度比单链表慢约 20%。

单链尾队列适用于具有大型数据集且很少或没有删除操作的应用，或者用于实现 FIFO 队列。

所有双向链式数据结构类型（列表和尾队列）还允许：

- 在列表中的任何元素之前插入新条目。
- O(1) 时间删除列表中的任何条目。

但是：

- 每个元素需要两个指针而非一个。
- 操作的代码量和执行时间（删除操作除外）大约是单链数据结构的两倍。

链表是双向链式数据结构中最简单的。在上述功能之上，它们还增加以下功能：

- O(n) 时间连接两个列表。
- 可以反向遍历。

但是：

- 要反向遍历，必须指定开始遍历的条目及其所在的列表。

尾队列增加以下功能：

- 可以在列表末尾添加条目。
- 可以从尾到头反向遍历。
- 可以进行连接。

但是：

- 所有列表插入和删除操作都必须指定列表头。
- 每个头条目需要两个指针而非一个。
- 代码量大约增加 15%，操作速度比单链表慢约 20%。

在宏定义中，`TYPE` 是用户定义结构的名称。该结构必须包含一个名为 `NAME` 的字段，其类型为 `SLIST_ENTRY`、`STAILQ_ENTRY`、`LIST_ENTRY` 或 `TAILQ_ENTRY`。在宏定义中，`CLASSTYPE` 是用户定义类的名称。该类必须包含一个名为 `NAME` 的字段，其类型为 `SLIST_CLASS_ENTRY`、`STAILQ_CLASS_ENTRY`、`LIST_CLASS_ENTRY` 或 `TAILQ_CLASS_ENTRY`。参数 `HEADNAME` 是用户定义结构的名称，必须使用宏 `SLIST_HEAD`、`SLIST_CLASS_HEAD`、`STAILQ_HEAD`、`STAILQ_CLASS_HEAD`、`LIST_HEAD`、`LIST_CLASS_HEAD`、`TAILQ_HEAD` 或 `TAILQ_CLASS_HEAD` 声明。有关这些宏使用方法的进一步说明，请参见下面的示例。

## 单链表

单链表以由 `SLIST_HEAD` 宏定义的结构作为头部。此结构包含一个指向列表第一个元素的单个指针。元素以单链方式连接，以最小化空间和指针操作开销，但代价是任意元素的删除为 O(n)。可以向列表中现有元素之后或列表头部添加新元素。`SLIST_HEAD` 结构声明如下：

```c
SLIST_HEAD(HEADNAME, TYPE) head;
```

其中 `HEADNAME` 是要定义的结构名称，`TYPE` 是要链接到列表中的元素类型。稍后可以这样声明指向列表头的指针：

```c
struct HEADNAME *headp;
```

（名称 `head` 和 `headp` 可由用户选择。）

宏 `SLIST_HEAD_INITIALIZER` 求值为列表 `head` 的初始化器。

宏 `SLIST_CONCAT` 将由 `head2` 作为头的列表连接到由 `head1` 作为头的列表末尾，并移除前者中的所有条目。应避免使用此宏，因为它会遍历整个 `head1` 列表。如果此宏需要用于高使用率的代码路径或操作长列表，应使用单链尾队列。

宏 `SLIST_EMPTY` 在列表中没有元素时求值为真。`SLIST_EMPTY_ATOMIC` 变体行为相同，但可以安全地用于可能有其他线程同时更新列表的上下文中。

宏 `SLIST_ENTRY` 声明连接列表中元素的结构。

宏 `SLIST_FIRST` 返回列表中的第一个元素，如果列表为空则返回 NULL。

宏 `SLIST_FOREACH` 正向遍历由 `head` 引用的列表，依次将每个元素赋值给 `var`。

宏 `SLIST_FOREACH_FROM` 在 `var` 为 NULL 时行为与 `SLIST_FOREACH` 相同，否则将 `var` 视为先前找到的 SLIST 元素，并从 `var` 而非 `head` 引用的 SLIST 中的第一个元素开始循环。

宏 `SLIST_FOREACH_SAFE` 正向遍历由 `head` 引用的列表，依次将每个元素赋值给 `var`。然而，与 `SLIST_FOREACH` 不同，这里允许在循环内安全地删除 `var` 并释放它，而不会干扰遍历。

宏 `SLIST_FOREACH_FROM_SAFE` 在 `var` 为 NULL 时行为与 `SLIST_FOREACH_SAFE` 相同，否则将 `var` 视为先前找到的 SLIST 元素，并从 `var` 而非 `head` 引用的 SLIST 中的第一个元素开始循环。

宏 `SLIST_INIT` 初始化由 `head` 引用的列表。

宏 `SLIST_INSERT_HEAD` 在列表头部插入新元素 `elm`。

宏 `SLIST_INSERT_AFTER` 在元素 `listelm` 之后插入新元素 `elm`。

宏 `SLIST_NEXT` 返回列表中的下一个元素。

宏 `SLIST_REMOVE_AFTER` 从列表中删除 `elm` 之后的元素。与 `SLIST_REMOVE` 不同，此宏不会遍历整个列表。

宏 `SLIST_REMOVE_HEAD` 从列表头部删除元素 `elm`。为了获得最佳效率，从列表头部删除的元素应显式使用此宏而非通用的 `SLIST_REMOVE` 宏。

宏 `SLIST_REMOVE` 从列表中删除元素 `elm`。应避免使用此宏，因为它会遍历整个列表。如果此宏需要用于高使用率的代码路径或操作长列表，应使用双向链表。

宏 `SLIST_SPLIT_AFTER` 拆分由 `head` 引用的列表，使 `rest` 引用由 `head` 中 `elm` 之后的元素形成的列表。

宏 `SLIST_SWAP` 交换 `head1` 和 `head2` 的内容。

## 单链表示例

```c
SLIST_HEAD(slisthead, entry) head =
    SLIST_HEAD_INITIALIZER(head);
struct slisthead *headp;		/* 单链表头。 */
struct entry {
	...
	SLIST_ENTRY(entry) entries;	/* 单链表。 */
	...
} *n1, *n2, *n3, *np;
SLIST_INIT(&head);			/* 初始化列表。 */
n1 = malloc(sizeof(struct entry));	/* 在头部插入。 */
SLIST_INSERT_HEAD(&head, n1, entries);
n2 = malloc(sizeof(struct entry));	/* 在其后插入。 */
SLIST_INSERT_AFTER(n1, n2, entries);
SLIST_REMOVE(&head, n2, entry, entries);/* 删除。 */
free(n2);
n3 = SLIST_FIRST(&head);
SLIST_REMOVE_HEAD(&head, entries);	/* 从头部删除。 */
free(n3);
					/* 正向遍历。 */
SLIST_FOREACH(np, &head, entries)
	np-> ...
					/* 安全的正向遍历。 */
SLIST_FOREACH_SAFE(np, &head, entries, np_temp) {
	np->do_stuff();
	...
	SLIST_REMOVE(&head, np, entry, entries);
	free(np);
}
while (!SLIST_EMPTY(&head)) {		/* 删除列表。 */
	n1 = SLIST_FIRST(&head);
	SLIST_REMOVE_HEAD(&head, entries);
	free(n1);
}
```

## 单链尾队列

单链尾队列以由 `STAILQ_HEAD` 宏定义的结构作为头部。此结构包含一对指针，一个指向尾队列中的第一个元素，另一个指向最后一个元素。元素以单链方式连接，以最小化空间和指针操作开销，但代价是任意元素的删除为 O(n)。可以向尾队列中现有元素之后、尾队列头部或尾队列末尾添加新元素。`STAILQ_HEAD` 结构声明如下：

```c
STAILQ_HEAD(HEADNAME, TYPE) head;
```

其中 `HEADNAME` 是要定义的结构名称，`TYPE` 是要链接到尾队列中的元素类型。稍后可以这样声明指向尾队列头的指针：

```c
struct HEADNAME *headp;
```

（名称 `head` 和 `headp` 可由用户选择。）

宏 `STAILQ_HEAD_INITIALIZER` 求值为尾队列 `head` 的初始化器。

宏 `STAILQ_CONCAT` 将由 `head2` 作为头的尾队列连接到由 `head1` 作为头的尾队列末尾，并移除前者中的所有条目。

宏 `STAILQ_EMPTY` 在尾队列中没有条目时求值为真。`STAILQ_EMPTY_ATOMIC` 变体行为相同，但可以安全地用于可能有其他线程同时更新队列的上下文中。

宏 `STAILQ_ENTRY` 声明连接尾队列中元素的结构。

宏 `STAILQ_FIRST` 返回尾队列中的第一个条目，如果尾队列为空则返回 NULL。

宏 `STAILQ_FOREACH` 正向遍历由 `head` 引用的尾队列，依次将每个元素赋值给 `var`。

宏 `STAILQ_FOREACH_FROM` 在 `var` 为 NULL 时行为与 `STAILQ_FOREACH` 相同，否则将 `var` 视为先前找到的 STAILQ 元素，并从 `var` 而非 `head` 引用的 STAILQ 中的第一个元素开始循环。

宏 `STAILQ_FOREACH_SAFE` 正向遍历由 `head` 引用的尾队列，依次将每个元素赋值给 `var`。然而，与 `STAILQ_FOREACH` 不同，这里允许在循环内安全地删除 `var` 并释放它，而不会干扰遍历。

宏 `STAILQ_FOREACH_FROM_SAFE` 在 `var` 为 NULL 时行为与 `STAILQ_FOREACH_SAFE` 相同，否则将 `var` 视为先前找到的 STAILQ 元素，并从 `var` 而非 `head` 引用的 STAILQ 中的第一个元素开始循环。

宏 `STAILQ_INIT` 初始化由 `head` 引用的尾队列。

宏 `STAILQ_INSERT_HEAD` 在尾队列头部插入新元素 `elm`。

宏 `STAILQ_INSERT_TAIL` 在尾队列末尾插入新元素 `elm`。

宏 `STAILQ_INSERT_AFTER` 在元素 `listelm` 之后插入新元素 `elm`。

宏 `STAILQ_LAST` 返回尾队列中的最后一个条目。如果尾队列为空，返回值为 `NULL`。

宏 `STAILQ_NEXT` 返回尾队列中的下一个条目，如果此条目是最后一个则返回 NULL。

宏 `STAILQ_REMOVE_AFTER` 从尾队列中删除 `elm` 之后的元素。与 `STAILQ_REMOVE` 不同，此宏不会遍历整个尾队列。

宏 `STAILQ_REMOVE_HEAD` 删除尾队列头部的元素。为了获得最佳效率，从尾队列头部删除的元素应显式使用此宏而非通用的 `STAILQ_REMOVE` 宏。

宏 `STAILQ_REMOVE` 从尾队列中删除元素 `elm`。应避免使用此宏，因为它会遍历整个列表。如果此宏需要用于高使用率的代码路径或操作长尾队列，应使用双向链式尾队列。

宏 `STAILQ_REVERSE` 原地反转队列。

宏 `STAILQ_SPLIT_AFTER` 拆分由 `head` 引用的尾队列，使 `rest` 引用由 `head` 中 `elm` 之后的元素形成的尾队列。

宏 `STAILQ_SWAP` 交换 `head1` 和 `head2` 的内容。

## 单链尾队列示例

```c
STAILQ_HEAD(stailhead, entry) head =
    STAILQ_HEAD_INITIALIZER(head);
struct stailhead *headp;		/* 单链尾队列头。 */
struct entry {
	...
	STAILQ_ENTRY(entry) entries;	/* 尾队列。 */
	...
} *n1, *n2, *n3, *np;
STAILQ_INIT(&head);			/* 初始化队列。 */
n1 = malloc(sizeof(struct entry));	/* 在头部插入。 */
STAILQ_INSERT_HEAD(&head, n1, entries);
n1 = malloc(sizeof(struct entry));	/* 在尾部插入。 */
STAILQ_INSERT_TAIL(&head, n1, entries);
n2 = malloc(sizeof(struct entry));	/* 在其后插入。 */
STAILQ_INSERT_AFTER(&head, n1, n2, entries);
					/* 删除。 */
STAILQ_REMOVE(&head, n2, entry, entries);
free(n2);
					/* 从头部删除。 */
n3 = STAILQ_FIRST(&head);
STAILQ_REMOVE_HEAD(&head, entries);
free(n3);
					/* 正向遍历。 */
STAILQ_FOREACH(np, &head, entries)
	np-> ...
					/* 安全的正向遍历。 */
STAILQ_FOREACH_SAFE(np, &head, entries, np_temp) {
	np->do_stuff();
	...
	STAILQ_REMOVE(&head, np, entry, entries);
	free(np);
}
					/* 删除尾队列。 */
while (!STAILQ_EMPTY(&head)) {
	n1 = STAILQ_FIRST(&head);
	STAILQ_REMOVE_HEAD(&head, entries);
	free(n1);
}
					/* 更快的尾队列删除。 */
n1 = STAILQ_FIRST(&head);
while (n1 != NULL) {
	n2 = STAILQ_NEXT(n1, entries);
	free(n1);
	n1 = n2;
}
STAILQ_INIT(&head);
```

## 列表

列表以由 `LIST_HEAD` 宏定义的结构作为头部。此结构包含一个指向列表第一个元素的单个指针。元素以双向链式连接，因此可以在不遍历列表的情况下删除任意元素。可以向列表中现有元素之后、现有元素之前或列表头部添加新元素。`LIST_HEAD` 结构声明如下：

```c
LIST_HEAD(HEADNAME, TYPE) head;
```

其中 `HEADNAME` 是要定义的结构名称，`TYPE` 是要链接到列表中的元素类型。稍后可以这样声明指向列表头的指针：

```c
struct HEADNAME *headp;
```

（名称 `head` 和 `headp` 可由用户选择。）

宏 `LIST_HEAD_INITIALIZER` 求值为列表 `head` 的初始化器。

宏 `LIST_CONCAT` 将由 `head2` 作为头的列表连接到由 `head1` 作为头的列表末尾，并移除前者中的所有条目。应避免使用此宏，因为它会遍历整个 `head1` 列表。如果此宏需要用于高使用率的代码路径或操作长列表，应使用尾队列。

宏 `LIST_EMPTY` 在列表中没有元素时求值为真。`LIST_EMPTY_ATOMIC` 变体行为相同，但可以安全地用于可能有其他线程同时更新列表的上下文中。

宏 `LIST_ENTRY` 声明连接列表中元素的结构。

宏 `LIST_FIRST` 返回列表中的第一个元素，如果列表为空则返回 NULL。

宏 `LIST_FOREACH` 正向遍历由 `head` 引用的列表，依次将每个元素赋值给 `var`。

宏 `LIST_FOREACH_FROM` 在 `var` 为 NULL 时行为与 `LIST_FOREACH` 相同，否则将 `var` 视为先前找到的 LIST 元素，并从 `var` 而非 `head` 引用的 LIST 中的第一个元素开始循环。

宏 `LIST_FOREACH_SAFE` 正向遍历由 `head` 引用的列表，依次将每个元素赋值给 `var`。然而，与 `LIST_FOREACH` 不同，这里允许在循环内安全地删除 `var` 并释放它，而不会干扰遍历。

宏 `LIST_FOREACH_FROM_SAFE` 在 `var` 为 NULL 时行为与 `LIST_FOREACH_SAFE` 相同，否则将 `var` 视为先前找到的 LIST 元素，并从 `var` 而非 `head` 引用的 LIST 中的第一个元素开始循环。

宏 `LIST_INIT` 初始化由 `head` 引用的列表。

宏 `LIST_INSERT_HEAD` 在列表头部插入新元素 `elm`。

宏 `LIST_INSERT_AFTER` 在元素 `listelm` 之后插入新元素 `elm`。

宏 `LIST_INSERT_BEFORE` 在元素 `listelm` 之前插入新元素 `elm`。

宏 `LIST_NEXT` 返回列表中的下一个元素，如果这是最后一个则返回 NULL。

宏 `LIST_PREV` 返回列表中的前一个元素，如果这是第一个则返回 NULL。列表 `head` 必须包含元素 `elm`。

宏 `LIST_REMOVE` 从列表中删除元素 `elm`。

宏 `LIST_REPLACE` 在列表中用 `new` 替换元素 `elm`。元素 `new` 不能已经在某个列表上。

宏 `LIST_SPLIT_AFTER` 拆分由 `head` 引用的列表，使 `rest` 引用由 `head` 中 `elm` 之后的元素形成的列表。

宏 `LIST_SWAP` 交换 `head1` 和 `head2` 的内容。

## 列表示例

```c
LIST_HEAD(listhead, entry) head =
    LIST_HEAD_INITIALIZER(head);
struct listhead *headp;			/* 列表头。 */
struct entry {
	...
	LIST_ENTRY(entry) entries;	/* 列表。 */
	...
} *n1, *n2, *n3, *np, *np_temp;
LIST_INIT(&head);			/* 初始化列表。 */
n1 = malloc(sizeof(struct entry));	/* 在头部插入。 */
LIST_INSERT_HEAD(&head, n1, entries);
n2 = malloc(sizeof(struct entry));	/* 在其后插入。 */
LIST_INSERT_AFTER(n1, n2, entries);
n3 = malloc(sizeof(struct entry));	/* 在其前插入。 */
LIST_INSERT_BEFORE(n2, n3, entries);
LIST_REMOVE(n2, entries);		/* 删除。 */
free(n2);
					/* 正向遍历。 */
LIST_FOREACH(np, &head, entries)
	np-> ...
					/* 安全的正向遍历。 */
LIST_FOREACH_SAFE(np, &head, entries, np_temp) {
	np->do_stuff();
	...
	LIST_REMOVE(np, entries);
	free(np);
}
while (!LIST_EMPTY(&head)) {		/* 删除列表。 */
	n1 = LIST_FIRST(&head);
	LIST_REMOVE(n1, entries);
	free(n1);
}
n1 = LIST_FIRST(&head);			/* 更快的列表删除。 */
while (n1 != NULL) {
	n2 = LIST_NEXT(n1, entries);
	free(n1);
	n1 = n2;
}
LIST_INIT(&head);
```

## 尾队列

尾队列以由 `TAILQ_HEAD` 宏定义的结构作为头部。此结构包含一对指针，一个指向尾队列中的第一个元素，另一个指向最后一个元素。元素以双向链式连接，因此可以在不遍历尾队列的情况下删除任意元素。可以向尾队列中现有元素之后、现有元素之前、尾队列头部或尾队列末尾添加新元素。`TAILQ_HEAD` 结构声明如下：

```c
TAILQ_HEAD(HEADNAME, TYPE) head;
```

其中 `HEADNAME` 是要定义的结构名称，`TYPE` 是要链接到尾队列中的元素类型。稍后可以这样声明指向尾队列头的指针：

```c
struct HEADNAME *headp;
```

（名称 `head` 和 `headp` 可由用户选择。）

宏 `TAILQ_HEAD_INITIALIZER` 求值为尾队列 `head` 的初始化器。

宏 `TAILQ_CONCAT` 将由 `head2` 作为头的尾队列连接到由 `head1` 作为头的尾队列末尾，并移除前者中的所有条目。

宏 `TAILQ_EMPTY` 在尾队列中没有条目时求值为真。`TAILQ_EMPTY_ATOMIC` 变体行为相同，但可以安全地用于可能有其他线程同时更新队列的上下文中。

宏 `TAILQ_ENTRY` 声明连接尾队列中元素的结构。

宏 `TAILQ_FIRST` 返回尾队列中的第一个条目，如果尾队列为空则返回 NULL。

宏 `TAILQ_FOREACH` 正向遍历由 `head` 引用的尾队列，依次将每个元素赋值给 `var`。如果循环正常完成或没有元素，`var` 被设置为 `NULL`。

宏 `TAILQ_FOREACH_FROM` 在 `var` 为 NULL 时行为与 `TAILQ_FOREACH` 相同，否则将 `var` 视为先前找到的 TAILQ 元素，并从 `var` 而非 `head` 引用的 TAILQ 中的第一个元素开始循环。

宏 `TAILQ_FOREACH_REVERSE` 反向遍历由 `head` 引用的尾队列，依次将每个元素赋值给 `var`。

宏 `TAILQ_FOREACH_REVERSE_FROM` 在 `var` 为 NULL 时行为与 `TAILQ_FOREACH_REVERSE` 相同，否则将 `var` 视为先前找到的 TAILQ 元素，并从 `var` 而非 `head` 引用的 TAILQ 中的最后一个元素开始反向循环。

宏 `TAILQ_FOREACH_SAFE` 和 `TAILQ_FOREACH_REVERSE_SAFE` 分别正向和反向遍历由 `head` 引用的列表，依次将每个元素赋值给 `var`。然而，与它们的不安全对应版本 `TAILQ_FOREACH` 和 `TAILQ_FOREACH_REVERSE` 不同，它们允许在循环内安全地删除 `var` 并释放它，而不会干扰遍历。

宏 `TAILQ_FOREACH_FROM_SAFE` 在 `var` 为 NULL 时行为与 `TAILQ_FOREACH_SAFE` 相同，否则将 `var` 视为先前找到的 TAILQ 元素，并从 `var` 而非 `head` 引用的 TAILQ 中的第一个元素开始循环。

宏 `TAILQ_FOREACH_REVERSE_FROM_SAFE` 在 `var` 为 NULL 时行为与 `TAILQ_FOREACH_REVERSE_SAFE` 相同，否则将 `var` 视为先前找到的 TAILQ 元素，并从 `var` 而非 `head` 引用的 TAILQ 中的最后一个元素开始反向循环。

宏 `TAILQ_INIT` 初始化由 `head` 引用的尾队列。

宏 `TAILQ_INSERT_HEAD` 在尾队列头部插入新元素 `elm`。

宏 `TAILQ_INSERT_TAIL` 在尾队列末尾插入新元素 `elm`。

宏 `TAILQ_INSERT_AFTER` 在元素 `listelm` 之后插入新元素 `elm`。

宏 `TAILQ_INSERT_BEFORE` 在元素 `listelm` 之前插入新元素 `elm`。

宏 `TAILQ_LAST` 返回尾队列中的最后一个条目。如果尾队列为空，返回值为 `NULL`。

宏 `TAILQ_NEXT` 返回尾队列中的下一个条目，如果此条目是最后一个则返回 NULL。

宏 `TAILQ_PREV` 返回尾队列中的前一个条目，如果此条目是第一个则返回 NULL。

宏 `TAILQ_REMOVE` 从尾队列中删除元素 `elm`。

宏 `TAILQ_REPLACE` 在尾队列中用 `new` 替换元素 `elm`。元素 `new` 不能已经在某个列表上。

宏 `TAILQ_SPLIT_AFTER` 拆分由 `head` 引用的尾队列，使 `rest` 引用由 `head` 中 `elm` 之后的元素形成的尾队列。

宏 `TAILQ_SWAP` 交换 `head1` 和 `head2` 的内容。

## 尾队列示例

```c
TAILQ_HEAD(tailhead, entry) head =
    TAILQ_HEAD_INITIALIZER(head);
struct tailhead *headp;			/* 尾队列头。 */
struct entry {
	...
	TAILQ_ENTRY(entry) entries;	/* 尾队列。 */
	...
} *n1, *n2, *n3, *n4, *np;
TAILQ_INIT(&head);			/* 初始化队列。 */
n1 = malloc(sizeof(struct entry));	/* 在头部插入。 */
TAILQ_INSERT_HEAD(&head, n1, entries);
n1 = malloc(sizeof(struct entry));	/* 在尾部插入。 */
TAILQ_INSERT_TAIL(&head, n1, entries);
n2 = malloc(sizeof(struct entry));	/* 在其后插入。 */
TAILQ_INSERT_AFTER(&head, n1, n2, entries);
n3 = malloc(sizeof(struct entry));	/* 在其前插入。 */
TAILQ_INSERT_BEFORE(n2, n3, entries);
TAILQ_REMOVE(&head, n2, entries);	/* 删除。 */
free(n2);
n4 = malloc(sizeof(struct entry));	/* 替换。 */
TAILQ_REPLACE(&head, n3, n4, entries);
free(n3);
					/* 正向遍历。 */
TAILQ_FOREACH(np, &head, entries)
	np-> ...
					/* 安全的正向遍历。 */
TAILQ_FOREACH_SAFE(np, &head, entries, np_temp) {
	np->do_stuff();
	...
	TAILQ_REMOVE(&head, np, entries);
	free(np);
}
					/* 反向遍历。 */
TAILQ_FOREACH_REVERSE(np, &head, tailhead, entries)
	np-> ...
					/* 删除尾队列。 */
while (!TAILQ_EMPTY(&head)) {
	n1 = TAILQ_FIRST(&head);
	TAILQ_REMOVE(&head, n1, entries);
	free(n1);
}
					/* 更快的尾队列删除。 */
n1 = TAILQ_FIRST(&head);
while (n1 != NULL) {
	n2 = TAILQ_NEXT(n1, entries);
	free(n1);
	n1 = n2;
}
TAILQ_INIT(&head);
```

## 诊断

`queue(3)` 提供若干诊断和调试设施。

当使用 `INVARIANTS` 编译时，在内核中使用 queue 宏会自动插入执行基本完整性和 API 一致性检查的检查代码。可以通过在首次包含以下文件之前分别定义宏 `QUEUE_MACRO_DEBUG_ASSERTIONS` 或 `QUEUE_MACRO_NO_DEBUG_ASSERTIONS` 来请求插入或省略检查代码：

```c
#include <sys/queue.h>
```

当检查代码遇到异常时，它会使内核崩溃或中止程序。为此，在内核或 `_STANDALONE` 构建中，它默认调用 `panic()`，而在用户空间构建中，它会在 `stderr` 上打印诊断消息然后调用 `abort()`。可以通过在首次包含以下文件之前定义自定义 `QMD_PANIC` 宏来覆盖这些行为：

```c
#include <sys/queue.h>
```

诊断消息自动包含发生失败检查的源文件、行和函数。可以通过在首次包含以下文件之前定义自定义 `QMD_ASSERT` 宏来覆盖此行为：

```c
#include <sys/queue.h>
```

`SLIST_REMOVE_PREVPTR` 宏可用于辅助调试：

`SLIST_REMOVE_PREVPTR(TYPE *prev, TYPE *elm, SLIST_ENTRY NAME)` 删除元素 `elm`，该元素必须直接跟随其 `&SLIST_NEXT()` 为 `prev` 的元素，将其从列表中移除。在上述详述的条件下，此宏可能会插入检查代码，验证 `elm` 确实跟随列表中的 `prev`（通过 `QMD_SLIST_CHECK_PREVPTR` 宏）。

调试时，跟踪队列变更可能很有用。要启用跟踪，请定义宏 `QUEUE_MACRO_DEBUG_TRACE`。请注意，目前仅为常规尾队列的宏进行了插桩。

将已从队列中取消链接的指针置为垃圾值以检测删除后使用也可能很有用。要在编译时启用指针置垃圾，请定义宏 `QUEUE_MACRO_DEBUG_TRASH`。请注意，目前仅有有限数量的宏进行了插桩。宏 `QMD_IS_TRASHED(void *ptr)` 在 `ptr` 已被 `QUEUE_MACRO_DEBUG_TRASH` 选项置为垃圾值时返回真。

## 参见

[arb(3)](arb.3.md), [tree(3)](tree.3.md)

## 历史

`queue` 函数首次出现于 4.4BSD。
