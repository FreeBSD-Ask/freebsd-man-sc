# mac_set(3)

`mac_set_file` — 为文件或进程设置 MAC 标签

## 名称

`mac_set_file`, `mac_set_fd`, `mac_set_proc`

## 库

libc

## 概要

`#include <sys/mac.h>`

```c
int
mac_set_file(const char *path, mac_t label);

int
mac_set_link(const char *path, mac_t label);

int
mac_set_fd(int fd, mac_t label);

int
mac_set_proc(mac_t label);
```

## 描述

`mac_set_file` 和 `mac_set_fd` 函数将 `label` 所指定的 MAC 标签分别关联到 `path` 所引用的文件或文件描述符 `fd`。注意，当文件描述符引用套接字时，对文件描述符的标签操作作用于套接字，而非在绑定套接字时可能用作会合点的文件。`mac_set_link` 函数与 `mac_set_file` 相同，区别在于它不跟随符号链接。

`mac_set_proc` 函数将 `label` 所指定的 MAC 标签关联到调用进程。

仅当进程对该文件具有 MAC 写访问权限，且其有效用户 ID 等于文件所有者，或具有适当特权时，才允许为文件设置标签。

## 返回值

`mac_set_fd`、`mac_set_file`、`mac_set_link` 和 `mac_set_proc` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`[EACCES]` 拒绝对该文件的 MAC 写访问。

`[EBADF]` `fd` 参数不是有效的文件描述符。

`[EINVAL]` `label` 参数不是有效的 MAC 标签，或 `fd` 所引用的对象不适合进行标签操作。

`[EOPNOTSUPP]` `fd` 所引用的文件不支持设置 MAC 标签。

`[EPERM]` 调用进程没有足够的特权来更改 MAC 标签。

`[EROFS]` 所修改对象的文件系统为只读。

`[ENAMETOOLONG]` `path` 所指向路径名的长度超过 `PATH_MAX`，或路径名的某个组件超过 `NAME_MAX`。

`[ENOENT]` `path` 所引用的文件不存在。

`[ENOTDIR]` `path` 所引用路径名的某个组件不是目录。

## 参见

[mac(3)](mac.3.md), [mac_free(3)](mac_free.3.md), [mac_get(3)](mac_get.3.md), [mac_is_present(3)](mac_is_present.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_text(3)](mac_text.3.md), [posix1e(3)](posix1e.3.md), [mac(4)](../man4/mac.4.md), [mac(9)](../man9/mac.9.md)

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。
