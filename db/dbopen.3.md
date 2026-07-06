# dbopen(3)

`dbopen` — 数据库访问方法

## 名称

`dbopen`

## 概要

`#include <sys/types.h>`

`#include <db.h>`

`#include <fcntl.h>`

`#include <limits.h>`

`Ft DB * Fn dbopen const char *file int flags int mode DBTYPE type const void *openinfo`

## 描述

`dbopen` 函数是数据库文件的库接口。支持的文件格式为 btree、哈希和面向 UNIX 文件。btree 格式是有序、平衡树结构的表示。哈希格式是一种可扩展的动态哈希方案。平面文件格式是具有固定或可变长度记录的字节流文件。各格式及文件格式专有信息在各自的手册页面 [btree(3)](btree.3.md)、[hash(3)](hash.3.md) 和 [recno(3)](recno.3.md) 中详细描述。

`dbopen` 函数以读和/或写方式打开 `file`。通过将 `file` 参数设置为 `NULL`，可以创建不打算保存到磁盘的文件。

`flags` 和 `mode` 参数如 [open(2)](../man2/open.2.md) 例程所指定，但是，只有 `O_CREAT`、`O_EXCL`、`O_EXLOCK`、`O_NOFOLLOW`、`O_NONBLOCK`、`O_RDONLY`、`O_RDWR`、`O_SHLOCK`、`O_SYNC`、`O_WRONLY` 和 `O_TRUNC` 标志有意义。

`type` 参数的类型为 `DBTYPE`（定义在 `#include <db.h>` 头文件中），可设置为 `DB_BTREE`、`DB_HASH` 或 `DB_RECNO`。

`openinfo` 参数是指向访问方法专有结构的指针，该结构在访问方法的手册页面中描述。如果 `openinfo` 为 `NULL`，每种访问方法将使用适合系统和访问方法的默认值。

`dbopen` 函数成功时返回指向 `DB` 结构的指针，出错时返回 `NULL`。`DB` 结构定义在 `#include <db.h>` 头文件中，至少包含以下字段：

```c
typedef struct {
	DBTYPE type;
	int (*close)(DB *db);
	int (*del)(const DB *db, const DBT *key, u_int flags);
	int (*fd)(const DB *db);
	int (*get)(const DB *db, const DBT *key, DBT *data, u_int flags);
	int (*put)(const DB *db, DBT *key, const DBT *data,
	     u_int flags);
	int (*sync)(const DB *db, u_int flags);
	int (*seq)(const DB *db, DBT *key, DBT *data, u_int flags);
} DB;
```

这些元素描述了数据库类型和一组执行各种操作的函数。这些函数接受一个指向 `dbopen` 返回结构的指针，有时还接受一个或多个指向键/数据结构的指针以及一个标志值。

**`R_CURSOR`** 删除游标所引用的记录。游标必须先前已初始化。

**`R_CURSOR`** 替换游标所引用的键/数据对。游标必须先前已初始化。

**`R_IAFTER`** 在 `key` 所引用的数据之后紧接追加数据，创建新的键/数据对。追加的键/数据对的记录号在 `key` 结构中返回。（仅适用于 `DB_RECNO` 访问方法。）

**`R_IBEFORE`** 在 `key` 所引用的数据之前紧接插入数据，创建新的键/数据对。插入的键/数据对的记录号在 `key` 结构中返回。（仅适用于 `DB_RECNO` 访问方法。）

**`R_NOOVERWRITE`** 仅当键先前不存在时才输入新的键/数据对。

**`R_SETCURSOR`** 存储键/数据对，并设置或初始化游标位置以引用它。（仅适用于 `DB_BTREE` 和 `DB_RECNO` 访问方法。）

**`R_CURSOR`** 返回与指定键关联的数据。这与 `get` 例程的不同之处在于它还设置或初始化游标到键的位置。（注意，对于 `DB_BTREE` 访问方法，返回的键不一定与指定键完全匹配。返回的键是大于或等于指定键的最小键，允许部分键匹配和范围搜索。）

**`R_FIRST`** 返回数据库的第一个键/数据对，并设置或初始化游标以引用它。

**`R_LAST`** 返回数据库的最后一个键/数据对，并设置或初始化游标以引用它。（仅适用于 `DB_BTREE` 和 `DB_RECNO` 访问方法。）

**`R_NEXT`** 检索游标之后紧接的键/数据对。如果游标尚未设置，则与 `R_FIRST` 标志相同。

**`R_PREV`** 检索游标之前紧接的键/数据对。如果游标尚未设置，则与 `R_LAST` 标志相同。（仅适用于 `DB_BTREE` 和 `DB_RECNO` 访问方法。）

**`R_RECNOSYNC`** 如果使用 `DB_RECNO` 访问方法，此标志使 `sync` 例程应用于 recno 文件底层的 btree 文件，而不是 recno 文件本身。（更多信息参见 [recno(3)](recno.3.md) 手册页面的 `bfname` 字段。）

**`type`** 底层访问方法（及文件格式）的类型。

**`close`** 指向用于将所有缓存信息刷新到磁盘、释放所有已分配资源并关闭底层文件的例程的指针。由于键/数据对可能被缓存在内存中，未通过 `close` 或 `sync` 函数同步文件可能导致信息不一致或丢失。`close` 例程出错时返回 -1（设置 `errno`），成功时返回 0。

**`del`** 指向用于从数据库中删除键/数据对的例程的指针。`flags` 参数可设置为以下值：`del` 例程出错时返回 -1（设置 `errno`），成功时返回 0，如果指定的 `key` 不在文件中则返回 1。

**`fd`** 指向返回代表底层数据库的文件描述符的例程的指针。所有以相同 `file` 名调用 `dbopen` 的进程都将获得引用同一文件的文件描述符。此文件描述符可安全地用作 [fcntl(2)](../man2/fcntl.2.md) 和 [flock(2)](../man2/flock.2.md) 锁定函数的参数。该文件描述符不一定与访问方法使用的任何底层文件关联。内存数据库没有可用的文件描述符。`fd` 例程出错时返回 -1（设置 `errno`），成功时返回文件描述符。

**`get`** 指向用于从数据库进行按键检索的接口例程的指针。与指定 `key` 关联的数据的地址和长度在 `data` 所引用的结构中返回。`get` 例程出错时返回 -1（设置 `errno`），成功时返回 0，如果 `key` 不在文件中则返回 1。

**`put`** 指向用于在数据库中存储键/数据对的例程的指针。`flags` 参数可设置为以下值之一：`R_SETCURSOR` 仅适用于 `DB_BTREE` 和 `DB_RECNO` 访问方法，因为它意味着键具有不变的固有顺序。`R_IAFTER` 和 `R_IBEFORE` 仅适用于 `DB_RECNO` 访问方法，因为它们各自意味着访问方法能够创建新键。只有当键有序且独立时才成立，例如记录号。`put` 例程的默认行为是输入新的键/数据对，替换任何先前存在的键。`put` 例程出错时返回 -1（设置 `errno`），成功时返回 0，如果设置了 `R_NOOVERWRITE` 标志且键已存在于文件中则返回 1。

**`seq`** 指向用于从数据库进行顺序检索的接口例程的指针。键的地址和长度在 `key` 所引用的结构中返回，数据的地址和长度在 `data` 所引用的结构中返回。顺序键/数据对检索可在任何时候开始，“游标”的位置不受 `del`、`get`、`put` 或 `sync` 例程调用的影响。顺序扫描期间对数据库的修改将反映在扫描中，即，插入到游标后面的记录不会返回，而插入到游标前面的记录会返回。`flags` 参数*必须*设置为以下值之一：`R_LAST` 和 `R_PREV` 仅适用于 `DB_BTREE` 和 `DB_RECNO` 访问方法，因为它们各自意味着键具有不变的固有顺序。`seq` 例程出错时返回 -1（设置 `errno`），成功时返回 0，如果没有小于或大于指定或当前键的键/数据对则返回 1。如果使用 `DB_RECNO` 访问方法，且数据库文件是字符特殊文件且当前没有完整的键/数据对可用，则 `seq` 例程返回 2。

**`sync`** 指向用于将所有缓存信息刷新到磁盘的例程的指针。如果数据库仅在内存中，`sync` 例程无效且始终成功。`flags` 参数可设置为以下值：`sync` 例程出错时返回 -1（设置 `errno`），成功时返回 0。

## 键/数据对

对所有文件类型的访问都基于键/数据对。键和数据都由以下数据结构表示：

```c
typedef struct {
	void *data;
	size_t size;
} DBT;
```

`DBT` 结构的各元素定义如下：

**`data`** 指向字节串的指针。

**`size`** 字节串的长度。

键和数据的字节串可以引用本质上无限长度的字符串，尽管任意两个字节串必须同时适合可用内存。应注意，访问方法不对字节串对齐提供保证。

## 错误

`dbopen` 例程可能失败并为库例程 [open(2)](../man2/open.2.md) 和 malloc(3) 所指定的任何错误或以下错误设置 `errno`：

**`EFTYPE`** 文件格式不正确。

**`EINVAL`** 指定了与当前文件规范不兼容或对该函数无意义的参数（哈希函数、填充字节等），（例如，未先初始化就使用游标），或者文件版本号与软件不匹配。

`close` 例程可能失败并为库例程 [close(2)](../man2/close.2.md)、[read(2)](../man2/read.2.md)、[write(2)](../man2/write.2.md)、free(3) 或 [fsync(2)](../man2/fsync.2.md) 所指定的任何错误设置 `errno`。

`del`、`get`、`put` 和 `seq` 例程可能失败并为库例程 [read(2)](../man2/read.2.md)、[write(2)](../man2/write.2.md)、free(3) 或 malloc(3) 所指定的任何错误设置 `errno`。

对于内存数据库，`fd` 例程将失败并将 `errno` 设置为 `ENOENT`。

`sync` 例程可能失败并为库例程 [fsync(2)](../man2/fsync.2.md) 所指定的任何错误设置 `errno`。

## 参见

[btree(3)](btree.3.md), [hash(3)](hash.3.md), [mpool(3)](mpool.3.md), [recno(3)](recno.3.md)

> Margo Seltzer, Michael Olson, "LIBTP: Portable, Modular Transactions for UNIX", Winter 1992.

## 缺陷

类型定义 `DBT` 是 “data base thang” 的助记符，使用它是因为没人能想出一个未被使用的合理名称。

文件描述符接口是个临时方案，将在接口的未来版本中删除。

所有访问方法均不提供任何形式的并发访问、锁定或事务。
