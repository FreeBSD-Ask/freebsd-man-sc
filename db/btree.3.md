# btree(3)

`btree` — btree 数据库访问方法

## 名称

`btree`

## 概要

`#include <sys/types.h>`

`#include <db.h>`

## 描述

`dbopen` 例程是数据库文件的库接口。其中一种支持的文件格式是 `btree` 文件。数据库访问方法的总体描述参见 [dbopen(3)](dbopen.3.md)，本手册页面仅描述 `btree` 特有的信息。

`btree` 数据结构是一种有序的、平衡的树结构，用于存储关联的键/数据对。

提供给 `dbopen` 的 `btree` 访问方法专有数据结构定义在 `#include <db.h>` 头文件中，如下所示：

```c
typedef struct {
	u_long flags;
	u_int cachesize;
	int maxkeypage;
	int minkeypage;
	u_int psize;
	int (*compare)(const DBT *key1, const DBT *key2);
	size_t (*prefix)(const DBT *key1, const DBT *key2);
	int lorder;
} BTREEINFO;
```

该结构的各元素如下：

**`R_DUP`** 允许树中存在重复键，即允许在要插入的键已存在于树中时仍然进行插入。如 [dbopen(3)](dbopen.3.md) 中所述的默认行为是，在插入新键时覆盖匹配的键，或者如果指定了 `R_NOOVERWRITE` 标志则失败。`R_DUP` 标志会被 `R_NOOVERWRITE` 标志覆盖，如果指定了 `R_NOOVERWRITE` 标志，尝试向树中插入重复键将失败。如果数据库包含重复键，使用 `get` 例程时键/数据对的检索顺序未定义，但是，设置了 `R_CURSOR` 标志的 `seq` 例程调用将始终返回任何重复键组中逻辑上的“第一个”键。

**`flags`** 标志值由以下任意值按位或指定：

**`cachesize`** 建议的内存缓存最大大小（以字节为单位）。此值*仅*是建议性的，访问方法会分配更多内存而不是失败。由于每次搜索都会检查树的根页面，缓存最近使用的页面能显著改善访问时间。此外，物理写入会尽可能延迟，因此适度的缓存可以显著减少 I/O 操作次数。显然，使用缓存会增加（但仅会增加）在修改树期间系统崩溃导致损坏或数据丢失的可能性。如果 `cachesize` 为 0（未指定大小），则使用默认缓存。

**`maxkeypage`** 任何单个页面上将存储的最大键数。目前未实现。

**`minkeypage`** 任何单个页面上将存储的最小键数。此值用于确定哪些键将存储在溢出页面上，即如果键或数据项的长度大于 pagesize 除以 minkeypage 的值，则将其存储在溢出页面上而不是页面本身中。如果 `minkeypage` 为 0（未指定最小键数），则使用值 2。

**`psize`** 页面大小是树中节点所用页面的字节大小。最小页面大小为 512 字节，最大页面大小为 64K。如果 `psize` 为 0（未指定页面大小），则根据底层文件系统 I/O 块大小选择页面大小。

**`compare`** compare 是键比较函数。如果第一个键参数分别小于、等于或大于第二个键参数，它必须返回一个小于、等于或大于零的整数。每次打开给定树时必须使用相同的比较函数。如果 `compare` 为 `NULL`（未指定比较函数），则按词典序比较键，较短的键被认为小于较长的键。

**`prefix`** `prefix` 元素是前缀比较函数。如果指定，此例程必须返回第二个键参数中为确定它大于第一个键参数所必需的字节数。如果键相等，则应返回键长度。注意，此例程的实用性非常依赖于数据，但是，在某些数据集中可以显著减小树的大小和搜索时间。如果 `prefix` 为 `NULL`（未指定前缀函数），*且*未指定比较函数，则使用默认的词典比较例程。如果 `prefix` 为 `NULL` 且指定了比较例程，则不进行前缀比较。

**`lorder`** 存储数据库元数据中整数的字节顺序。该数字应以整数形式表示顺序；例如，大端序将是数字 4,321。如果 `lorder` 为 0（未指定顺序），则使用当前主机顺序。

如果文件已存在（且未指定 `O_TRUNC` 标志），则为 `flags`、`lorder` 和 `psize` 参数指定的值将被忽略，转而使用创建树时使用的值。

树的正向顺序扫描从最小的键到最大的键。

从树中删除键/数据对所释放的空间永远不会被回收，尽管通常会使其可供重用。这意味着 `btree` 存储结构是只增长的。唯一的解决方案是避免过多的删除，或者定期从现有树的扫描中创建新树。

`btree` 中的搜索、插入和删除都将在 O(lg_base N) 时间内完成，其中 base 是平均填充因子。通常，将有序数据插入 `btree` 会导致低填充因子。此实现经过修改，使有序插入成为最佳情况，从而产生比正常情况好得多的页面填充因子。

## 错误

`btree` 访问方法例程可能失败并为库例程 [dbopen(3)](dbopen.3.md) 所指定的任何错误设置 `errno`。

## 参见

[dbopen(3)](dbopen.3.md), [hash(3)](hash.3.md), [mpool(3)](mpool.3.md), [recno(3)](recno.3.md)

> Douglas Comer, "The Ubiquitous B-tree", *ACM Comput. Surv. 11*, 2, pp. 121-138, June 1979.

> Bayer, Unterauer, "Prefix B-trees", *ACM Transactions on Database Systems*, Vol. 2, 1, pp. 11-26, March 1977.

> D. E. Knuth, *The Art of Computer Programming Vol. 3: Sorting and Searching*, pp. 471-480, 1968.

## 缺陷

仅支持大端和小端字节顺序。
