# VOP_READDIR.9

`VOP_READDIR` — 读取目录内容

## 名称

`VOP_READDIR`

## 概要

```c
#include <sys/param.h>
#include <sys/dirent.h>
#include <sys/vnode.h>
```

```c
int
VOP_READDIR(struct vnode *vp, struct uio *uio, struct ucred *cred,
    int *eofflag, int *ncookies, uint64_t **cookies)
```

## 描述

读取目录条目。

**`vp`** 目录的 vnode。

**`uio`** 读取目录内容的位置。

**`cred`** 调用者的凭证。

**`eofflag`** 返回文件末尾状态（如果不需要则为 `NULL`）。

**`ncookies`** 为 NFS 生成的目录 cookie 数量（如果不需要则为 `NULL`）。

**`cookies`** 为 NFS 生成的目录查找 cookie（如果不需要则为 `NULL`）。

目录内容被读取到 `struct dirent` 结构中。如果磁盘上的数据结构与此不同，则应进行转换。

## 锁定

目录应在进入时已锁定，并在退出时仍保持锁定。

## 返回值

成功时返回零，否则返回错误代码。

如果从 NFS 服务器调用，将提供额外参数 `eofflag`、`ncookies` 和 `cookies`。如果在读取时到达目录末尾，应将 `*eofflag` 的值设置为 TRUE。目录查找 cookie 返回给 NFS 客户端，可稍后用于从目录中间重新开始读取目录。每个目录条目应返回一个 cookie。cookie 的值应为相应目录条目磁盘版本在目录中开始的偏移量。cookie 的内存应使用以下方式分配：

```c
	...;
	*ncookies = number of entries read;
	*cookies = malloc(*ncookies * sizeof(**cookies), M_TEMP, M_WAITOK);
```

## 错误

[`EINVAL`] 试图从目录中的非法偏移位置读取。

[`EIO`] 读取目录时发生读取错误。

[`EINTEGRITY`] 读取目录时检测到损坏的数据。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
