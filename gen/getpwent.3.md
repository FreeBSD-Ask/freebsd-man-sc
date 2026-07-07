# getpwent(3)

`getpwent` — 密码数据库操作

## 名称

`getpwent`, `getpwent_r`, `getpwnam`, `getpwnam_r`, `getpwuid`, `getpwuid_r`, `setpassent`, `setpwent`, `endpwent`

## 库

Lb libc

## 概要

`#include <pwd.h>`

```c
struct passwd *
getpwent(void);

int
getpwent_r(struct passwd *pwd, char *buffer, size_t bufsize,
    struct passwd **result);

struct passwd *
getpwnam(const char *login);

int
getpwnam_r(const char *name, struct passwd *pwd, char *buffer,
    size_t bufsize, struct passwd **result);

struct passwd *
getpwuid(uid_t uid);

int
getpwuid_r(uid_t uid, struct passwd *pwd, char *buffer,
    size_t bufsize, struct passwd **result);

int
setpassent(int stayopen);

void
setpwent(void);

void
endpwent(void);
```

## 描述

这些函数对密码数据库文件进行操作，该文件在 [passwd(5)](../man5/passwd.5.md) 中描述。数据库中的每个条目由 `passwd` 结构定义，该结构可在包含文件 `#include <pwd.h>` 中找到：

```c
struct passwd {
	char	*pw_name;	/* 用户名 */
	char	*pw_passwd;	/* 加密密码 */
	uid_t	pw_uid;		/* 用户 uid */
	gid_t	pw_gid;		/* 用户 gid */
	time_t	pw_change;	/* 密码修改时间 */
	char	*pw_class;	/* 用户访问类 */
	char	*pw_gecos;	/* Honeywell 登录信息 */
	char	*pw_dir;	/* 主目录 */
	char	*pw_shell;	/* 默认 shell */
	time_t	pw_expire;	/* 账户过期时间 */
	int	pw_fields;	/* 内部：已填写的字段 */
};
```

`getpwnam` 和 `getpwuid` 函数分别在密码数据库中搜索给定的登录名或用户 uid，始终返回找到的第一个条目。

`getpwent` 函数顺序读取密码数据库，供需要处理完整用户列表的程序使用。

`getpwent_r`、`getpwnam_r` 和 `getpwuid_r` 函数分别是 `getpwent`、`getpwnam` 和 `getpwuid` 的线程安全版本。调用者必须在 `pwd`、`buffer`、`bufsize` 和 `result` 参数中为搜索结果提供存储空间。当这些函数成功时，`pwd` 参数将被填充，而指向该参数的指针将存储在 `result` 中。如果未找到条目或发生错误，`result` 将被设置为 `NULL`。

`setpassent` 函数有两个作用。首先，它使 `getpwent` “回绕”到数据库的开头。此外，如果 `stayopen` 非零，则文件描述符保持打开状态，从而显著加快所有例程的后续访问速度。（后一功能对 `getpwent` 来说是不必要的，因为它默认不关闭其文件描述符。）

对于长时间运行的程序来说，保持文件描述符打开是危险的，因为如果在程序运行期间数据库被更新，数据库将变得过时。

`setpwent` 函数等同于参数为零的 `setpassent`。

`endpwent` 函数关闭所有打开的文件。

这些例程被编写用于“屏蔽”密码文件，即只允许某些程序访问加密密码。如果调用它们的进程的有效 uid 为 0，则返回加密密码，否则返回结构的密码字段将指向字符串 `*`。

## 返回值

`getpwent`、`getpwnam` 和 `getpwuid` 函数成功时返回指向 passwd 结构的有效指针，如果未找到条目或发生错误，则返回 `NULL`。如果确实发生错误，`errno` 将被设置。注意，如果程序需要区分不存在的条目和错误，则必须在调用这些函数之前显式地将 `errno` 设置为零。`getpwent_r`、`getpwnam_r` 和 `getpwuid_r` 函数在未发生错误时返回 0，或返回一个错误号以指示失败。如果未找到匹配的条目，这并不是一个错误。（因此，如果 `result` 为 `NULL` 且返回值为 0，则表示不存在匹配的条目。）

`setpassent` 函数失败时返回 0，成功时返回 1。`endpwent` 和 `setpwent` 函数没有返回值。

## 文件

**/etc/pwd.db** 非安全密码数据库文件

**/etc/spwd.db** 安全密码数据库文件

**/etc/master.passwd** 当前密码文件

**/etc/passwd** Version 7 格式的密码文件

## 兼容性

历史函数 setpwfile(3) 允许指定备用的密码数据库，现已弃用且不再可用。

## 错误

除了以下错误外，这些例程还可能因 [open(2)](../sys/open.2.md)、[dbopen(3)](../db/dbopen.3.md)、[socket(2)](../sys/socket.2.md) 和 [connect(2)](../sys/connect.2.md) 中指定的任何错误而失败：

**[`ERANGE`]** 由 `buffer` 和 `bufsize` 参数指定的缓冲区大小不足以存储结果。调用者应使用更大的缓冲区重试。

## 参见

[getlogin(2)](../sys/getlogin.2.md), [getgrent(3)](getgrent.3.md), [nsswitch.conf(5)](../man5/nsswitch.conf.5.md), [passwd(5)](../man5/passwd.5.md), [pwd_mkdb(8)](../man8/pwd_mkdb.8.md), [vipw(8)](../man8/vipw.8.md), [yp(8)](../man8/yp.8.md)

## 标准

`getpwent`、`getpwnam`、`getpwnam_r`、`getpwuid`、`getpwuid_r`、`setpwent` 和 `endpwent` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。

## 历史

`getpwent`、`getpwnam`、`getpwuid`、`setpwent` 和 `endpwent` 函数出现于 Version 7 AT&T UNIX。`setpassent` 函数出现于 4.3BSD-Reno。`getpwent_r`、`getpwnam_r` 和 `getpwuid_r` 函数出现于 FreeBSD 5.1。

## 缺陷

`getpwent`、`getpwnam` 和 `getpwuid` 函数将其结果留在内部静态对象中，并返回指向该对象的指针。对同一函数的后续调用将修改同一对象。

`getpwent`、`getpwent_r`、`endpwent`、`setpassent` 和 `setpwent` 函数在网络环境中相当无用，应尽可能避免使用。如果在 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 中指定了多个源，`getpwent` 和 `getpwent_r` 函数不会尝试抑制重复信息。
