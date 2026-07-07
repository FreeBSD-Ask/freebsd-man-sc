# mac_get(3)

`mac_get_file` — 获取文件、套接字、套接字对端或进程的标签

## 名称

`mac_get_file`, `mac_get_link`, `mac_get_fd`, `mac_get_peer`, `mac_get_pid`, `mac_get_proc`

## 库

libc

## 概要

`#include <sys/mac.h>`

```c
int
mac_get_file(const char *path, mac_t label);

int
mac_get_link(const char *path, mac_t label);

int
mac_get_fd(int fd, mac_t label);

int
mac_get_peer(int fd, mac_t label);

int
mac_get_pid(pid_t pid, mac_t label);

int
mac_get_proc(mac_t label);
```

## 描述

`mac_get_file` 系统调用返回由路径名指定的文件所关联的标签。`mac_get_link` 函数与 `mac_get_file` 相同，区别在于它不跟随符号链接。

`mac_get_fd` 系统调用返回由指定文件描述符引用的对象所关联的标签。注意，对于文件系统套接字，返回的标签将是套接字标签，该标签可能与作为套接字会合点的磁盘上节点标签不同。`mac_get_peer` 系统调用返回套接字远程端点所关联的标签；此调用的确切语义取决于协议域、通信类型和端点；通常，该标签在面向连接的协议实例首次建立时缓存，对于数据报协议则未定义。

`mac_get_pid` 和 `mac_get_proc` 系统调用返回与任意进程 ID 或当前进程关联的进程标签。

用于这些调用的标签存储必须首先使用 [mac_prepare(3)](mac_prepare.3.md) 函数分配和准备。当应用程序使用完标签后，可使用 [mac_free(3)](mac_free.3.md) 释放内存。

## 错误

`[EACCES]` `path` 的某个组件不可搜索，或拒绝对该文件的 MAC 读访问。

`[EINVAL]` 请求的标签操作对 `fd` 引用的对象无效。

`[ENAMETOOLONG]` `path` 指向的路径名超过 `PATH_MAX`，或路径名的某个组件超过 `NAME_MAX`。

`[ENOENT]` `path` 的某个组件不存在。

`[ENOMEM]` 内存不足，无法分配新的 MAC 标签结构。

`[ENOTDIR]` `path` 的某个组件不是目录。

## 参见

[mac(3)](mac.3.md), [mac_free(3)](mac_free.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_set(3)](mac_set.3.md), [mac_text(3)](mac_text.3.md), [posix1e(3)](posix1e.3.md), [mac(4)](../man4/mac.4.md), [mac(9)](../man9/mac.9.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。
