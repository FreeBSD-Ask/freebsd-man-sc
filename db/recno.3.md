# recno(3)

`recno` — 记录号数据库访问方法

## 名称

`recno`

## 概要

`#include <sys/types.h>`

`#include <db.h>`

## 描述

`dbopen` 例程是数据库文件的库接口。其中一种支持的文件格式是记录号文件。数据库访问方法的总体描述参见 [dbopen(3)](dbopen.3.md)，本手册页面仅描述 `recno` 特有的信息。

记录号数据结构是以平面文件格式存储的可变或固定长度记录，通过逻辑记录号访问。记录号五的存在意味着记录一到四的存在，而删除记录号一会使记录号五重新编号为记录号四，同时如果游标定位在记录号一之后，游标也会向下移动一条记录。

提供给 `dbopen` 的 `recno` 访问方法专有数据结构定义在 `#include <db.h>` 头文件中，如下所示：

```c
typedef struct {
	u_long flags;
	u_int cachesize;
	u_int psize;
	int lorder;
	size_t reclen;
	u_char bval;
	char *bfname;
} RECNOINFO;
```

该结构的各元素定义如下：

**`R_FIXEDLEN`** 记录为固定长度，不以字节分隔。结构元素 `reclen` 指定记录的长度，结构元素 `bval` 用作填充字符。插入数据库的任何长度小于 `reclen` 字节的记录都会自动填充。

**`R_NOKEY`** 在 `dbopen` 指定的接口中，顺序记录检索会同时填充调用者的键和数据结构。如果指定了 `R_NOKEY` 标志，*游标*例程不需要填充键结构。这允许应用程序检索文件末尾的记录而无需读取所有中间记录。

**`R_SNAPSHOT`** 此标志要求在调用 `dbopen` 时获取文件的快照，而不是允许从原始文件读取任何未修改的记录。

**`flags`** 标志值由以下任意值按位或指定：

**`cachesize`** 建议的内存缓存最大大小（以字节为单位）。此值*仅*是建议性的，访问方法会分配更多内存而不是失败。如果 `cachesize` 为 0（未指定大小），则使用默认缓存。

**`psize`** `recno` 访问方法将其记录的内存副本存储在 btree 中。此值是该树中节点所用页面的字节大小。如果 `psize` 为 0（未指定页面大小），则根据底层文件系统 I/O 块大小选择页面大小。更多信息参见 [btree(3)](btree.3.md)。

**`lorder`** 存储数据库元数据中整数的字节顺序。该数字应以整数形式表示顺序；例如，大端序将是数字 4,321。如果 `lorder` 为 0（未指定顺序），则使用当前主机顺序。

**`reclen`** 固定长度记录的长度。

**`bval`** 用于标记可变长度记录结尾的分隔字节，以及固定长度记录的填充字符。如果未指定值，则使用换行符（`\n`）标记可变长度记录的结尾，固定长度记录以空格填充。

**`bfname`** `recno` 访问方法将其记录的内存副本存储在 btree 中。如果 `bfname` 为非 `NULL`，它指定 btree 文件的名称，如同指定为 btree 文件的 `dbopen` 的文件名一样。

`recno` 访问方法使用的键/数据对的数据部分与其他访问方法相同。键不同。键的 `data` 字段应是指向 `#include <db.h>` 头文件中定义的 `recno_t` 类型内存位置的指针。此类型通常是实现可用的最大无符号整数类型。键的 `size` 字段应为该类型的大小。

由于底层 `recno` 访问方法文件不能关联任何元数据，因此每次打开文件时都必须显式指定对默认值的任何更改（例如固定记录长度或字节分隔符值）。

在 `dbopen` 指定的接口中，如果记录号比数据库中当前最大记录大超过一，使用 `put` 接口创建新记录将导致创建多个空记录。

## 错误

`recno` 访问方法例程可能失败并为库例程 [dbopen(3)](dbopen.3.md) 所指定的任何错误或以下错误设置 `errno`：

**`EINVAL`** 试图向固定长度数据库添加太大而无法容纳的记录。

## 参见

[btree(3)](btree.3.md), [dbopen(3)](dbopen.3.md), [hash(3)](hash.3.md), [mpool(3)](mpool.3.md)

> Michael Stonebraker, Heidi Stettner, Joseph Kalash, Antonin Guttman, Nadene Lynn, "Document Processing in a Relational Database System", May 1982.

## 缺陷

仅支持大端和小端字节顺序。
