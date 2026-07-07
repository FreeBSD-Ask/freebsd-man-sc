# acl_valid(3)

`acl_valid` — 验证 ACL

## 名称

`acl_valid`, `acl_valid_fd_np`, `acl_valid_file_np`, `acl_valid_link_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_valid(acl_t acl);

int
acl_valid_fd_np(int fd, acl_type_t type, acl_t acl);

int
acl_valid_file_np(const char *path_p, acl_type_t type, acl_t acl);

int
acl_valid_link_np(const char *path_p, acl_type_t type, acl_t acl);
```

## 描述

这些函数检查参数 `acl` 所引用的 ACL 是否有效。POSIX.1e 例程 `acl_valid` 仅根据 POSIX.1e ACL 语义检查此有效性，而不考虑 ACL 的使用上下文。非可移植形式 `acl_valid_fd_np`、`acl_valid_file_np` 和 `acl_valid_link_np` 允许在特定 ACL 类型 `type` 和文件系统对象的上下文中检查 ACL。在除 POSIX.1e 外还支持其他 ACL 类型的环境中，这更有意义。当指定路径指向符号链接时，`acl_valid_file_np` 会跟随符号链接，而 `acl_valid_link_np` 则不会。

对于 POSIX.1e 语义，检查包括：

- 三个必需条目（`ACL_USER_OBJ`、`ACL_GROUP_OBJ` 和 `ACL_OTHER`）必须在 ACL 中恰好各出现一次。如果 ACL 包含任何 `ACL_USER`、`ACL_GROUP` 或文件组类中任何其他实现定义的条目，则还需要一个 `ACL_MASK` 条目。ACL 最多包含一个 `ACL_MASK` 条目。
- 限定符字段在同一 POSIX.1e ACL 设施所定义标签类型的所有条目中必须唯一。标签类型字段必须包含有效值，包括任何实现定义的值。限定符字段值的验证由实现定义。

POSIX.1e `acl_valid` 函数可能出于验证目的重新排序 ACL；非可移植验证函数不会这样做。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，这些函数返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

若发生以下任一情况，这些函数将返回 -1，并将 `errno` 设置为相应值：

`[EACCES]` 拒绝对路径前缀中某组件的搜索权限，或对象存在但进程没有适当的访问权限。

`[EBADF]` `fd` 参数不是有效的文件描述符。

`[EINVAL]` 参数 `acl` 未指向有效的 ACL。`acl` 中缺少一个或多个必需的 ACL 条目。ACL 包含不唯一的条目。文件系统因特定于文件系统的语义问题而拒绝该 ACL。

`[ENAMETOOLONG]` 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

`[ENOENT]` 指定名称的对象不存在，或 `path_p` 参数指向空字符串。

`[ENOMEM]` 内存不足，无法满足请求。

`[EOPNOTSUPP]` 文件系统不支持 ACL 检索。

## 参见

[acl(3)](acl.3.md), [acl_get(3)](acl_get.3.md), [acl_init(3)](acl_init.3.md), [acl_set(3)](acl_set.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson
