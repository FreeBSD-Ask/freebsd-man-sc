# getgrent(3)

`getgrent` — 组数据库操作

## 名称

`getgrent`, `getgrent_r`, `getgrnam`, `getgrnam_r`, `getgrgid`, `getgrgid_r`, `setgroupent`, `setgrent`, `endgrent`

## 库

Lb libc

## 概要

`#include <grp.h>`

`Ft struct group * Fn getgrent void Ft int Fn getgrent_r struct group *grp char *buffer size_t bufsize struct group **result Ft struct group * Fn getgrnam const char *name Ft int Fn getgrnam_r const char *name struct group *grp char *buffer size_t bufsize struct group **result Ft struct group * Fn getgrgid gid_t gid Ft int Fn getgrgid_r gid_t gid struct group *grp char *buffer size_t bufsize struct group **result Ft int Fn setgroupent int stayopen Ft void Fn setgrent void Ft void Fn endgrent void`

## 描述

这些函数对组数据库文件 **/etc/group** 进行操作，该文件在 [group(5)](../man5/group.5.md) 中描述。数据库的每一行由头文件

`#include <grp.h>`

中的 `group` 结构定义：

```c
struct group {
	char	*gr_name;	/* 组名 */
	char	*gr_passwd;	/* 组密码 */
	gid_t	gr_gid;		/* 组 ID */
	char	**gr_mem;	/* 组成员 */
};
```

`getgrnam` 和 `getgrgid` 函数分别在组数据库中搜索由 `name` 所指向的组名或 `gid` 所指向的组 ID，返回第一个匹配项。相同的组名或组 ID 可能导致未定义行为。

`getgrent` 函数顺序读取组数据库，适用于希望遍历完整组列表的程序。

`getgrent_r`、`getgrnam_r` 和 `getgrgid_r` 函数分别是 `getgrent`、`getgrnam` 和 `getgrgid` 的线程安全版本。调用者必须通过 `grp`、`buffer`、`bufsize` 和 `result` 参数为搜索结果提供存储空间。这些函数成功时，`grp` 参数将被填充，指向该参数的指针将存储在 `result` 中。若未找到条目或发生错误，`result` 将被设置为 `NULL`。

这些函数在需要时会打开组文件以读取。

`setgroupent` 函数打开文件，若文件已打开则将其重绕。若 `stayopen` 非零，文件描述符保持打开，可显著加速后续调用。此功能对 `getgrent` 而言并非必要，因为它默认不关闭文件描述符。还需注意，长时间运行的程序使用此功能是危险的，因为组文件可能被更新。

`setgrent` 函数等同于以零为参数调用的 `setgroupent`。

`endgrent` 函数关闭所有打开的文件。

## 返回值

`getgrent`、`getgrnam` 和 `getgrgid` 函数成功时返回指向 group 结构的指针，若未找到条目或发生错误则返回 `NULL`。若发生错误，`errno` 将被设置。注意，若程序需要区分不存在的条目和错误，必须在调用这些函数之前显式将 `errno` 设置为零。`getgrent_r`、`getgrnam_r` 和 `getgrgid_r` 函数在未发生错误时返回 0，发生错误时返回错误号以指示失败。未找到匹配条目不算错误。（因此，若 `result` 被设置为 `NULL` 且返回值为 0，则表示不存在匹配条目。）

`setgroupent` 函数成功时返回 1，否则返回 0。`endgrent`、`setgrent` 和 `setgrfile` 函数没有返回值。

## 文件

**/etc/group** 组数据库文件

## 兼容性

历史函数 `setgrfile` 允许指定替代的密码数据库，现已弃用且不再可用。

## 参见

[getpwent(3)](getpwent.3.md), [group(5)](../man5/group.5.md), [nsswitch.conf(5)](../man5/nsswitch.conf.5.md), [yp(8)](../man8/yp.8.md)

## 标准

`getgrent`、`getgrnam`、`getgrnam_r`、`getgrgid`、`getgrgid_r` 和 `endgrent` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。`setgrent` 函数与该标准的区别在于其返回类型为 `int` 而非 `void`。

## 历史

`endgrent`、`getgrent`、`getgrnam`、`getgrgid` 和 `setgrent` 函数出现于 Version 7 AT&T UNIX。`setgrfile` 和 `setgroupent` 函数出现于 4.3BSD。`getgrent_r`、`getgrnam_r` 和 `getgrgid_r` 函数出现于 FreeBSD 5.1。

## 缺陷

`getgrent`、`getgrnam`、`getgrgid`、`setgroupent` 和 `setgrent` 函数将结果留在内部静态对象中，并返回指向该对象的指针。对同一函数的后续调用将修改同一对象。

`getgrent`、`getgrent_r`、`endgrent`、`setgroupent` 和 `setgrent` 函数在网络环境中相当无用，应尽量避免使用。若在 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 中指定了多个来源，`getgrent` 和 `getgrent_r` 函数不会尝试抑制重复信息。
