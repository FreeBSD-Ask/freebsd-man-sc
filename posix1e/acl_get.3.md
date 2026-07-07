# acl_get(3)

`acl_get_fd` — 获取文件的 ACL

## 名称

`acl_get_fd`, `acl_get_fd_np`, `acl_get_file`, `acl_get_link_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
acl_t
acl_get_fd(int fd);

acl_t
acl_get_fd_np(int fd, acl_type_t type);

acl_t
acl_get_file(const char *path_p, acl_type_t type);

acl_t
acl_get_link_np(const char *path_p, acl_type_t type);
```

## 描述

`acl_get_fd`、`acl_get_file`、`acl_get_link_np` 和 `acl_get_fd_np` 均允许从文件中检索 ACL。`acl_get_fd` 是一个 POSIX.1e 调用，允许从文件描述符检索 `ACL_TYPE_ACCESS` 类型的 ACL。`acl_get_fd_np` 函数是 `acl_get_fd` 的非可移植形式，允许从文件描述符检索任意类型的 ACL。`acl_get_file` 函数是一个 POSIX.1e 调用，允许按名称从文件检索指定类型的 ACL；`acl_get_link_np` 是 `acl_get_file` 的非可移植变体，当调用目标是符号链接时不跟随该符号链接。

这些函数可能导致内存分配。当不再需要新 ACL 时，调用者应通过以 `(void *)acl_t` 为参数调用 [acl_free(3)](acl_free.3.md) 来释放可释放的内存。

工作存储中的 ACL 是与 `fd` 所引用对象关联的 ACL 的独立副本。工作存储中的 ACL 不参与任何访问控制决策。

`type` 参数的有效值为：

| ACL_TYPE_ACCESS | POSIX.1e 访问 ACL |
| --------------- | ----------------- |
| ACL_TYPE_DEFAULT | POSIX.1e 默认 ACL |
| ACL_TYPE_NFS4 | NFSv4 ACL |

返回的 ACL 将相应地标记品牌。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，该函数将返回指向所检索 ACL 的指针。否则，返回 `(acl_t)NULL`，并设置 `errno` 以指示错误。

## 错误

若发生以下任一情况，`acl_get_fd` 函数将返回 `(acl_t)NULL`，并将 `errno` 设置为相应值：

`[EACCES]` 拒绝对路径前缀中某组件的搜索权限，或对象存在但进程没有适当的访问权限。

`[EBADF]` `fd` 参数不是有效的文件描述符。

`[EINVAL]` 传入的 ACL 类型对该文件对象无效。

`[ENAMETOOLONG]` 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

`[ENOENT]` 指定名称的对象不存在，或 `path_p` 参数指向空字符串。

`[ENOMEM]` 内存不足，无法满足请求。

`[EOPNOTSUPP]` 文件系统不支持 ACL 检索。

## 参见

[acl(3)](acl.3.md), [acl_free(3)](acl_free.3.md), [acl_get(3)](acl_get.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_set(3)](acl_set.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0。

## 作者

Robert N M Watson
