# VFS\_CHECKEXP.9

`VFS_CHECKEXP` — 检查文件系统是否导出给客户端

## 名称

`VFS_CHECKEXP`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>

int
VFS_CHECKEXP(struct mount *mp, struct sockaddr *nam, uint64_t *exflagsp,
    struct ucred **credanonp, int *numsecflavor, int *secflavors)
```

## 描述

`VFS_CHECKEXP` 宏由 NFS 服务器用来检查一个挂载点是否导出给某个客户端。

它所需的参数为：

**`mp`** 要检查的挂载点。

**`nam`** 包含客户端网络地址的 mbuf。

**`exflagsp`** 返回该客户端导出标志的返回参数。

**`credanonp`** 返回该客户端匿名凭证的返回参数。

**`numsecflavors`** 返回该客户端安全风格数量的返回值。

**`secflavors`** 必须是大小为 MAXSECFLAVORS 的数组，用于返回该客户端的安全风格。

应在文件系统的挂载结构上调用 `VFS_CHECKEXP` 宏，以确定它是否导出给地址包含在 `nam` 中的客户端。

它在 NFS 服务器中，一旦获取了文件句柄对应的 vnode 就会被调用，以确定客户端在 vnode 所在文件系统上被允许的访问权限。对于 NFSv4，每当查找操作跨越服务器文件系统挂载点时也会调用它，以更新访问信息。

该操作是文件系统特定的，但通常由默认的 ``vfs_stdcheckexp'' 处理。

## 返回值

特定于客户端的导出标志、匿名凭证和安全风格将通过 `*exflagsp`、`*credanonp`、`*numsecflavors` 和 `*secflavors` 返回。

## 参见

[VFS(9)](vfs.9.md), [VFS_FHTOVP(9)](vfs_fhtovp.9.md), [vnode(9)](vnode.9.md), [VOP_VPTOFH(9)](vop_vptofh.9.md)

## 作者

本手册页由 Alfred Perlstein 编写。
