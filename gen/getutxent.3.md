# getutxent.3

`endutxent` — 用户记账数据库函数

## 名称

`endutxent`, `getutxent`, `getutxid`, `getutxline`, `getutxuser`, `pututxline`, `setutxdb`, `setutxent`

## 库

Lb libc

## 概要

`#include <utmpx.h>`

`Ft void Fn endutxent void Ft struct utmpx * Fn getutxent void Ft struct utmpx * Fn getutxid const struct utmpx *id Ft struct utmpx * Fn getutxline const struct utmpx *line Ft struct utmpx * Fn getutxuser const char *user Ft struct utmpx * Fn pututxline const struct utmpx *utmpx Ft int Fn setutxdb int type const char *file Ft void Fn setutxent void`

## 描述

这些函数操作用户记账数据库，该数据库存储各种系统活动的记录，例如用户登录和登出，以及系统启动和关机和对系统时钟的修改。系统将这些记录存储在三个数据库中，每个数据库有不同的用途：

**/var/run/utx.active** 当前活动用户登录会话的日志。此文件类似于传统的 `utmp` 文件。此文件仅包含与进程相关的条目，例如用户登录和登出记录。

**/var/log/utx.lastlogin** 每个用户的最后登录条目日志。此文件类似于传统的 `lastlog` 文件。此文件仅包含至少登录过一次的用户的登录记录。

**/var/log/utx.log** 所有条目的日志，按添加日期排序。此文件类似于传统的 `wtmp` 文件。此文件可能包含下述任何类型的记录。

这些数据库中的每个条目由包含在以下头文件中的 `utmpx` 结构定义：

`#include <utmpx.h>`

```c
struct utmpx {
	short           ut_type;    /* 条目类型。 */
	struct timeval  ut_tv;      /* 条目创建时间。 */
	char            ut_id[];    /* 记录标识符。 */
	pid_t           ut_pid;     /* 进程 ID。 */
	char            ut_user[];  /* 用户登录名。 */
	char            ut_line[];  /* 设备名。 */
	char            ut_host[];  /* 远程主机名。 */
};
```

`ut_type` 字段指示日志条目的类型，可以有以下值之一：

**`EMPTY`** 无有效的用户记账信息。

**`BOOT_TIME`** 标识系统启动时间。

**`SHUTDOWN_TIME`** 标识系统关机时间。

**`OLD_TIME`** 标识系统时钟更改前的时间。

**`NEW_TIME`** 标识系统时钟更改后的时间。

**`USER_PROCESS`** 标识一个进程。

**`INIT_PROCESS`** 标识由 init 进程派生的进程。

**`LOGIN_PROCESS`** 标识已登录用户的会话领导者。

**`DEAD_PROCESS`** 标识已退出的会话领导者。

类型为 `INIT_PROCESS` 和 `LOGIN_PROCESS` 的条目在此实现中不被处理。

结构中的其他字段：

**`ut_tv`** 事件发生的时间。此字段用于所有类型的条目，`EMPTY` 除外。

**`ut_id`** 用于引用条目的标识符。此标识符可用于通过向数据库写入一个 `ut_id` 值相同的新条目来删除或替换登录条目。此字段仅适用于类型为 `USER_PROCESS`、`INIT_PROCESS`、`LOGIN_PROCESS` 和 `DEAD_PROCESS` 的条目。

**`ut_pid`** 登录会话的会话领导者的进程标识符。此字段仅适用于类型为 `USER_PROCESS`、`INIT_PROCESS`、`LOGIN_PROCESS` 和 `DEAD_PROCESS` 的条目。

**`ut_user`** 与登录会话对应的用户登录名。此字段仅适用于类型为 `USER_PROCESS` 和 `INIT_PROCESS` 的条目。对于 `INIT_PROCESS` 条目，此字段通常包含登录进程的名称。

**`ut_line`** TTY 字符设备的名称，不含 **/dev/** 前缀，对应于用于实现用户登录会话的设备。如果未使用 TTY 字符设备，此字段留空。此字段仅适用于类型为 `USER_PROCESS` 和 `LOGIN_PROCESS` 的条目。

**`ut_host`** 远程系统的网络主机名，该远程系统连接以执行用户登录。如果用户登录会话不是通过网络进行的，此字段留空。此字段仅适用于类型为 `USER_PROCESS` 的条目。

此实现保证所有不适用的字段被丢弃。在此实现中，还保证库函数返回的结构的 `ut_user`、`ut_line` 和 `ut_host` 字段以空字符结尾。

`getutxent` 函数可用于从用户记账数据库中读取下一个条目。

`getutxid` 函数在数据库中搜索下一个条目，其行为基于 `id` 的 `ut_type` 字段。如果 `ut_type` 的值为 `BOOT_TIME`、`SHUTDOWN_TIME`、`OLD_TIME` 或 `NEW_TIME`，它将返回下一个 `ut_type` 值相等的条目。如果 `ut_type` 的值为 `USER_PROCESS`、`INIT_PROCESS`、`LOGIN_PROCESS` 或 `DEAD_PROCESS`，它将返回下一个 `ut_type` 值为前述值之一且 `ut_id` 相等的条目。

`getutxline` 函数在数据库中搜索下一个 `ut_type` 值为 `USER_PROCESS` 或 `LOGIN_PROCESS` 且 `ut_line` 与 `line` 中同名字段相等的条目。

`getutxuser` 函数在数据库中搜索下一个 `ut_type` 值为 `USER_PROCESS` 且 `ut_user` 等于 `user` 的条目。

前述函数在尚未打开用户记账数据库时会自动尝试打开它。`setutxdb` 和 `setutxent` 函数允许手动打开数据库，使用户记账数据库内的偏移量回绕到开头。`endutxent` 函数关闭数据库。

`setutxent` 函数总是打开活动会话数据库。`setutxdb` 函数打开由 `type` 标识的数据库，其值为 `UTXDB_ACTIVE`、`UTXDB_LASTLOGIN` 或 `UTXDB_LOG`。如果 `file` 非空，它将打开文件名为 `file` 的自定义文件而非系统默认文件。使用自定义文件名时必须注意，`type` 仍须与实际格式匹配，因为每个数据库可能使用自己的文件格式。

`pututxline` 函数将记录 `utmpx` 写入系统默认的用户记账数据库。`ut_type` 的值决定修改哪些数据库。

类型为 `SHUTDOWN_TIME`、`OLD_TIME` 和 `NEW_TIME` 的条目仅写入 **/var/log/utx.log**。

类型为 `USER_PROCESS` 的条目还会写入 **/var/run/utx.active** 和 **/var/log/utx.lastlogin**。

类型为 `DEAD_PROCESS` 的条目仅在后者中找到 `ut_id` 相等的对应 `USER_PROCESS`、`INIT_PROCESS` 或 `LOGIN_PROCESS` 条目时，才会写入 **/var/log/utx.log** 和 **/var/run/utx.active**。

此外，类型为 `BOOT_TIME` 和 `SHUTDOWN_TIME` 的条目将导致 **/var/run/utx.active** 中的所有现有条目被丢弃。

所有类型未在前文提及的条目，会被此 `pututxline` 实现丢弃。此实现还忽略 `ut_tv` 的值。

## 返回值

`getutxent`、`getutxid`、`getutxline` 和 `getutxuser` 函数成功时返回一个指向满足前述约束的 `utmpx` 结构的指针，到达文件末尾或发生错误时返回 `NULL`。

`pututxline` 函数成功时返回一个指向 `utmpx` 结构的指针，该结构包含已写入磁盘的结构的副本。当提供的 `utmpx` 无效，或 `ut_type` 的值为 `DEAD_PROCESS` 且未找到 `ut_id` 字段值相等的条目时，返回 `NULL`；全局变量 `errno` 被设置为指示错误。

`setutxdb` 函数在用户记账数据库成功打开时返回 0。否则返回 -1，全局变量 `errno` 被设置为指示错误。

## 错误

除了 [open(2)](../man2/open.2.md)、fdopen(3)、[fopen(3)](fopen.3.md)、[fseek(3)](fseek.3.md) 中描述的错误条件外，`pututxline` 函数还可能产生以下错误：

**`ESRCH`** `ut_type` 的值为 `DEAD_PROCESS`，且找不到进程条目。

**`EINVAL`** `ut_type` 的值不被此实现支持。

除了 [fopen(3)](fopen.3.md) 中描述的错误条件外，`setutxdb` 函数还可能产生以下错误：

**`EINVAL`** `type` 参数包含此实现不支持的值。

**`EFTYPE`** 文件格式无效。

## 参见

[last(1)](../man1/last.1.md), write(1), [getpid(2)](../man2/getpid.2.md), [gettimeofday(2)](../man2/gettimeofday.2.md), [tty(4)](../man4/tty.4.md), ac(8), newsyslog(8), utx(8)

## 标准

`endutxent`、`getutxent`、`getutxid`、`getutxline` 和 `setutxent` 函数预期遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准。

`pututxline` 函数偏离了标准，它根据 `ut_type` 将记录写入多个数据库文件。这避免了对更新其他数据库的特殊实用函数的需求，例如其他实现中可用的 `updlastlogx` 和 `updwtmpx` 函数。它还在存储 `USER_PROCESS` 条目且未找到 `ut_id` 值相同的条目时，尝试替换活动会话数据库中的 `DEAD_PROCESS` 条目。标准总是要求分配新条目，这可能导致数据库无限增长。

`getutxuser` 和 `setutxdb` 函数、`utmpx` 结构的 `ut_host` 字段以及 `SHUTDOWN_TIME` 是扩展。

## 历史

这些函数出现于 FreeBSD 9.0。它们替代了 `#include <utmp.h>` 接口。

## 作者

Ed Schouten <ed@FreeBSD.org>
