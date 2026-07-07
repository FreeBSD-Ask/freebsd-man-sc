# acl_delete(3)

`acl_delete_def_file` — 从文件中删除 ACL

## 名称

`acl_delete_def_file`, `acl_delete_def_link_np`, `acl_delete_fd_np`, `acl_delete_file_np`, `acl_delete_link_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_delete_def_file(const char *path_p);

int
acl_delete_def_link_np(const char *path_p);

int
acl_delete_fd_np(int filedes, acl_type_t type);

int
acl_delete_file_np(const char *path_p, acl_type_t type);

int
acl_delete_link_np(const char *path_p, acl_type_t type);
```

## 描述

`acl_delete_def_file`、`acl_delete_def_link_np`、`acl_delete_fd_np`、`acl_delete_file_np` 和 `acl_delete_link_np` 均允许从文件中删除 ACL。`acl_delete_def_file` 函数是一个 POSIX.1e 调用，用于按名称删除文件的默认 ACL（通常是目录）；其余调用是不可移植的扩展，允许按路径名或文件描述符从文件/目录中删除任意 ACL 类型。`_file` 变体在路径名的最后一段遇到符号链接时会跟随该链接；`_link` 变体则对符号链接本身进行操作。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，这些函数返回 0。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果发生以下任何情况，这些函数将返回 -1，并将 `errno` 设置为相应值：

`[EACCES]` 拒绝对路径前缀的某个组件的搜索权限，或对象存在且进程没有适当的访问权限。

`[EBADF]` `fd` 参数不是有效的文件描述符。

`[EINVAL]` 传递的 ACL 类型对该文件对象无效。

`[ENAMETOOLONG]` 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

`[ENOENT]` 命名的对象不存在，或 `path_p` 参数指向空字符串。

`[ENOMEM]` 可用内存不足以满足请求。

`[ENOTDIR]` 路径前缀的某个组件不是目录。参数 `path_p` 必须是目录，但实际不是。

`[EOPNOTSUPP]` 文件系统不支持 ACL 删除。

`[EPERM]` 进程没有执行删除 ACL 操作的适当权限。

`[EROFS]` 文件系统是只读的。

## 参见

[acl(3)](acl.3.md), [acl_get(3)](acl_get.3.md), [acl_set(3)](acl_set.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson
