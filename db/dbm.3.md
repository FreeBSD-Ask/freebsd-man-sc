# dbm(3)

`dbm` — 数据库访问函数

## 名称

`dbm_clearerr`, `dbm_close`, `dbm_delete`, `dbm_dirfno`, `dbm_error`, `dbm_fetch`, `dbm_firstkey`, `dbm_nextkey`, `dbm_open`, `dbm_store`

## 概要

`#include <fcntl.h>`

`#include <ndbm.h>`

`Ft DBM * Fn dbm_open const char *base int flags mode_t mode Ft void Fn dbm_close DBM *db Ft int Fn dbm_store DBM *db datum key datum data int flags Ft datum Fn dbm_fetch DBM *db datum key Ft int Fn dbm_delete DBM *db datum key Ft datum Fn dbm_firstkey DBM *db Ft datum Fn dbm_nextkey DBM *db Ft int Fn dbm_error DBM *db Ft int Fn dbm_clearerr DBM *db Ft int Fn dbm_dirfno DBM *db`

## 描述

数据库访问函数。这些函数使用 [dbopen(3)](dbopen.3.md) 配合 [hash(3)](hash.3.md) 数据库实现。

`datum` 声明在 `#include <ndbm.h>` 头文件中：

```c
typedef struct {
	void *dptr;
	int dsize;
} datum;
```

`dbm_open` 函数打开或创建数据库。`base` 参数是包含数据库的文件的基本名；实际数据库带有 `.db` 后缀。即，如果 `base` 为 **/home/me/mystuff**，则实际数据库位于文件 **/home/me/mystuff.db** 中。`flags` 和 `mode` 参数传递给 [open(2)](../man2/open.2.md)。（`O_RDWR | O_CREAT`）是 `flags` 的典型值；`0660` 是 `mode` 的典型值。`dbm_open` 返回的指针标识数据库，并作为其他函数的 `db` 参数。如果出现任何错误，`dbm_open` 函数返回 `NULL` 并设置 `errno`。

`dbm_close` 函数关闭数据库。

`dbm_store` 函数在数据库中插入或替换条目。`flags` 参数为 `DBM_INSERT` 或 `DBM_REPLACE`。如果 `flags` 为 `DBM_INSERT` 且数据库已包含 `key` 的条目，则不替换该条目。否则替换或插入该条目。`dbm_store` 函数通常返回零，但如果无法插入条目（因为 `flags` 为 `DBM_INSERT` 且 `key` 的条目已存在）则返回 1，或者如果出现任何错误则返回 -1 并设置 `errno`。

`dbm_fetch` 函数返回 `NULL` 或与 `key` 对应的 `data`。

`dbm_delete` 函数删除 `key` 的条目。`dbm_delete` 函数通常返回零，或者如果出现任何错误则返回 -1 并设置 `errno`。

`dbm_firstkey` 函数返回数据库中的第一个键。`dbm_nextkey` 函数返回后续键。必须在调用 `dbm_nextkey` 之前调用 `dbm_firstkey`。键的返回顺序未指定，可能表现为随机。在所有键都已返回后，`dbm_nextkey` 函数返回 `NULL`。

`dbm_error` 函数返回最近错误的 `errno` 值。`dbm_clearerr` 函数将此值重置为 0 并返回 0。

`dbm_dirfno` 函数返回数据库的文件描述符。

## 参见

[open(2)](../man2/open.2.md), [dbopen(3)](dbopen.3.md), [hash(3)](hash.3.md)

## 标准

这些函数（`dbm_dirfno` 除外）包含在 SUSv2 中。

## 历史

函数 `dbminit`、`fetch`、`store`、`delete`、`firstkey` 和 `nextkey` 首次出现在 Version 7 AT&T UNIX 中。
