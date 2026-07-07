# acl_extended_file_np(3)

`acl_extended_file_np` — 检查文件是否设置了扩展 ACL

## 名称

`acl_extended_file_np`, `acl_extended_file_nofollow_np`, `acl_extended_link_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_extended_file_np(const char* path_p);

int
acl_extended_file_nofollow_np(const char* path_p);

int
acl_extended_link_np(const char* path_p);
```

## 描述

`acl_extended_file_np` 函数是一个非可移植调用，用于检查参数 `path_p` 所引用的文件或目录是否包含扩展访问 ACL。`acl_extended_file_nofollow_np` 函数的工作方式相同，但不跟随符号链接。`acl_extended_link_np` 函数是 `acl_extended_file_nofollow_np` 的同义词，采用 FreeBSD 命名风格。如果 ACL 包含除 ACL_USER_OBJ、ACL_GROUP_OBJ 和 ACL_OTHER 这三种必需标签类型条目之外的其他条目，则该 ACL 被视为扩展访问 ACL。

## 返回值

成功完成时，如果文件对象不包含扩展访问 ACL，该函数返回 0；否则返回 1。否则，返回值 -1，并设置 `errno` 以指示错误。

## 错误

如果发生以下任一情况，`acl_extended_file_np` 函数将返回值 `-1`，并将 `errno` 设置为相应值：

`[EACCES]` 对路径前缀的某个组件拒绝搜索权限。

## 参见

[extattr_get_file(2)](../sys/extattr_get_file.2.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参阅 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在继续。

## 作者

Gleb Popov
