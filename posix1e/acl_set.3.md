# acl_set(3)

`acl_set_fd` — 为文件设置 ACL

## 名称

`acl_set_fd`, `acl_set_fd_np`, `acl_set_file`, `acl_set_link_np`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

```c
int
acl_set_fd(int fd, acl_t acl);

int
acl_set_fd_np(int fd, acl_t acl, acl_type_t type);

int
acl_set_file(const char *path_p, acl_type_t type, acl_t acl);

int
acl_set_link_np(const char *path_p, acl_type_t type, acl_t acl);
```

## 描述

`acl_set_fd`、`acl_set_fd_np`、`acl_set_file` 和 `acl_set_link_np` 各自将 ACL 与 `fd` 或 `path_p` 所引用的对象关联。`acl_set_fd_np` 和 `acl_set_link_np` 函数不是 POSIX.1e 调用。`acl_set_fd` 函数仅允许设置 `ACL_TYPE_ACCESS` 类型的 ACL，而 `acl_set_fd_np` 允许设置任意类型的 ACL。当路径目标是符号链接时，`acl_set_link_np` 函数作用于符号链接本身而非其目标。

`type` 参数的有效值为：

| ACL_TYPE_ACCESS | POSIX.1e 访问 ACL |
| --------------- | ----------------- |
| ACL_TYPE_DEFAULT | POSIX.1e 默认 ACL |
| ACL_TYPE_NFS4 | NFSv4 ACL |

尝试以标记为 POSIX.1e 品牌的 `acl` 设置 `ACL_TYPE_NFS4`，或以标记为 NFSv4 品牌的 ACL 设置 `ACL_TYPE_ACCESS` 或 `ACL_TYPE_DEFAULT`，将导致错误。

## 实现说明

FreeBSD 对 POSIX.1e 接口和特性的支持目前仍在开发中。

## 返回值

成功完成时，这些函数返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

若发生以下任一情况，这些函数将返回 -1，并将 `errno` 设置为相应值：

`[EACCES]` 拒绝对路径前缀中某组件的搜索权限，或对象存在但进程没有适当的访问权限。

`[EBADF]` `fd` 参数不是有效的文件描述符。

`[EINVAL]` 参数 `acl` 未指向该对象的有效 ACL，或 `type` 中指定的 ACL 类型对该对象无效，或存在品牌不匹配。

`[ENAMETOOLONG]` 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

`[ENOENT]` 指定名称的对象不存在，或 `path_p` 参数指向空字符串。

`[ENOMEM]` 内存不足，无法满足请求。

`[ENOSPC]` 包含新 ACL 的目录或文件系统无法扩展，或文件系统的文件分配资源已耗尽。

`[EOPNOTSUPP]` 文件系统不支持 ACL 检索。

`[EROFS]` 此函数需要修改当前为只读的文件系统。

## 参见

[acl(3)](acl.3.md), [acl_delete(3)](acl_delete.3.md), [acl_get(3)](acl_get.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_valid(3)](acl_valid.3.md), [posix1e(3)](posix1e.3.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。关于该草案的讨论在跨平台 POSIX.1e 实现邮件列表上继续进行。要加入该列表，请参见 FreeBSD POSIX.1e 实现页面以获取更多信息。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0，开发仍在进行。

## 作者

Robert N M Watson
