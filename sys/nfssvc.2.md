# nfssvc(2)

`nfssvc` — NFS 服务

## 名称

`nfssvc`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`#include <sys/time.h>`

`#include <nfs/rpcv2.h>`

`#include <nfsserver/nfs.h>`

`#include <unistd.h>`

```c
int
nfssvc(int flags, void *argstructp);
```

## 描述

`nfssvc()` 系统调用供 NFS 守护进程使用，用于将信息传入和传出内核，也可用于作为服务器守护进程进入内核。`flags` 参数由若干位组成，表示进入内核后要采取的操作，`argstructp` 根据 flags 中设置的位指向三种结构之一。

在客户端，[nfsiod(8)](../man8/nfsiod.8.md) 调用 `nfssvc()` 时将 `flags` 参数设置为 `NFSSVC_BIOD`，`argstructp` 设置为 `NULL`，以作为块 I/O 服务器守护进程进入内核。对于 NQNFS，[mount_nfs(8)](../man8/mount_nfs.8.md) 调用 `nfssvc()` 时使用 `NFSSVC_MNTD` 标志，可选择与 `NFSSVC_GOTAUTH` 和 `NFSSVC_AUTHINFAIL` 标志按位或，同时附带一个指向以下结构的指针：

```c
struct nfsd_cargs {
        char            *ncd_dirp;      /* 挂载目录路径 */
        uid_t           ncd_authuid;    /* 有效 uid */
        int             ncd_authtype;   /* 认证器类型 */
        int             ncd_authlen;    /* 认证器字符串长度 */
        u_char          *ncd_authstr;   /* 认证器字符串 */
        int             ncd_verflen;    /* 以及验证器 */
        u_char          *ncd_verfstr;
        NFSKERBKEY_T    ncd_key;        /* 会话密钥 */
};
```

初始调用仅设置 `NFSSVC_MNTD` 标志，以指定对该挂载点的服务。如果挂载点使用 Kerberos，则当客户端需要为用户获取“rcmd”认证票据时，[mount_nfs(8)](../man8/mount_nfs.8.md) 工具将从 `nfssvc()` 返回，且 `errno` == `ENEEDAUTH`。[mount_nfs(8)](../man8/mount_nfs.8.md) 工具将尝试获取 Kerberos 票据，如果成功，则在将票据填入 ncd_authstr 字段并设置 nfsd_cargs 结构的 ncd_authlen 和 ncd_authtype 字段后，以 `NFSSVC_MNTD` 和 `NFSSVC_GOTAUTH` 标志调用 `nfssvc()`。如果 [mount_nfs(8)](../man8/mount_nfs.8.md) 获取票据失败，则以 `NFSSVC_MNTD`、`NFSSVC_GOTAUTH` 和 `NFSSVC_AUTHINFAIL` 标志调用 `nfssvc()`，表示认证尝试失败。

在服务器端，调用 `nfssvc()` 时使用 `NFSSVC_NFSD` 标志和指向以下结构的指针：

```c
struct nfsd_srvargs {
        struct nfsd     *nsd_nfsd;      /* 指向内核内 nfsd 结构的指针 */
        uid_t           nsd_uid;        /* 映射到凭证的有效 uid */
        uint32_t        nsd_haddr;      /* 客户端的 IP 地址 */
        struct ucred    nsd_cr;         /* uid 映射到的凭证 */
        int             nsd_authlen;    /* 认证字符串长度（返回） */
        u_char          *nsd_authstr;   /* 认证字符串（返回） */
        int             nsd_verflen;    /* 以及验证器 */
        u_char          *nsd_verfstr;
        struct timeval  nsd_timestamp;  /* 来自验证器的时间戳 */
        uint32_t        nsd_ttl;        /* 凭证 TTL（秒） */
        NFSKERBKEY_T    nsd_key;        /* 会话密钥 */
};
```

以作为 [nfsd(8)](../man8/nfsd.8.md) 守护进程进入内核。每当 [nfsd(8)](../man8/nfsd.8.md) 守护进程收到 Kerberos 认证票据时，它将从 `nfssvc()` 返回，且 `errno` == `ENEEDAUTH`。[nfsd(8)](../man8/nfsd.8.md) 工具将尝试认证票据，并为 nsd_uid 字段中指定的“用户 ID”在服务器上生成一组凭证。这通过首先认证 Kerberos 票据，然后将 Kerberos 主体映射到本地名称，并通过 [getpwnam(3)](../gen/getpwent.3.md) 和 [getgrouplist(3)](../gen/getgrouplist.3.md) 获取该用户的一组凭证来完成。如果成功，[nfsd(8)](../man8/nfsd.8.md) 工具将以 `NFSSVC_NFSD` 和 `NFSSVC_AUTHIN` 标志调用 `nfssvc()`，将 nsd_cr 中的凭证映射传入内核，缓存到该客户端的服务器套接字上。如果认证失败，[nfsd(8)](../man8/nfsd.8.md) 以 `NFSSVC_NFSD` 和 `NFSSVC_AUTHINFAIL` 标志调用 `nfssvc()`，表示认证失败。

主 [nfsd(8)](../man8/nfsd.8.md) 服务器守护进程调用 `nfssvc()` 时使用 `NFSSVC_ADDSOCK` 标志和指向以下结构的指针：

```c
struct nfsd_args {
        int     sock;   /* 要服务的套接字 */
        caddr_t name;   /* 基于连接的套接字的客户端地址 */
        int     namelen;/* name 的长度 */
};
```

将服务器端 NFS 套接字传入内核，交由 [nfsd(8)](../man8/nfsd.8.md) 守护进程服务。

## 返回值

通常 `nfssvc()` 不会返回，除非服务器被信号终止，此时返回值 0。否则返回 -1，并设置全局变量 `errno` 以指定错误。

## 错误

**[`ENEEDAUTH`]** 此特殊错误值实际上用于认证支持，特别是 Kerberos，如上文所述。

**[`EPERM`]** 调用者不是超级用户。

## 参见

[mount_nfs(8)](../man8/mount_nfs.8.md), [nfsd(8)](../man8/nfsd.8.md), [nfsiod(8)](../man8/nfsiod.8.md)

## 历史

`nfssvc()` 系统调用首次出现于 4.4BSD。

## 缺陷

`nfssvc()` 系统调用是专门为 NFS 支持守护进程设计的，因此特定于它们的需求。它确实应该返回值来指示需要认证支持，因为 `ENEEDAUTH` 并不真正是一个错误。参数结构的某些字段被假定为有效，有时被假定为与上次调用相比未更改，因此必须极其谨慎地使用 `nfssvc()`。
