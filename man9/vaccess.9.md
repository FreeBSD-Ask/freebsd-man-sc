# vaccess.9

`vaccess` — 使用 vnode 参数生成访问控制决策

## 名称

`vaccess`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`int vaccess(enum vtype type, mode_t file_mode, uid_t file_uid, gid_t file_gid, accmode_t accmode, struct ucred *cred)`

## 描述

此调用实现了 FreeBSD 中许多文件系统通用的 UNIX 自主文件安全模型的逻辑。它接受 vnode 类型 `type`、通过 `file_mode` 给出的权限、所有者 UID `file_uid`、所有者 GID `file_gid`、所需的访问模式 `accmode` 以及请求凭证 `cred`。

此调用旨在支持 [VOP_ACCESS(9)](VOP_ACCESS.9.md) 的实现，这些实现将使用自身的访问方法来检索 vnode 属性，然后调用 `vaccess()` 来执行实际检查。[VOP_ACCESS(9)](VOP_ACCESS.9.md) 的实现可以选择实现额外的安全机制，其结果将与返回值组合。

`vaccess()` 使用的算法通过比较传递的凭证、文件所有者和文件组来选择文件权限位的一个组成部分。如果凭证的有效 UID 与文件所有者匹配，则选择权限位的所有者组成部分。如果 UID 不匹配，则将凭证的有效 GID 及其附加组与文件组进行比较——如果匹配，则选择权限位的组组成部分。如果凭证的 UID 和 GID 都不匹配传递的文件所有者和组，则选择权限位的其他组成部分。

为当前凭证选择适当的保护后，将把请求的访问模式与 vnode 类型结合，与凭证可用的自主权限进行比较。如果自主保护授予的权限不足，则还会考虑凭证可用的超级用户特权。

## 返回值

`vaccess()` 成功时返回 0，失败时返回非零错误值。

## 错误

**[`EACCES`]** 权限被拒绝。尝试以文件访问权限禁止的方式访问文件。

**[`EPERM`]** 操作不允许。尝试执行限于具有适当特权的进程或文件或其他资源所有者的操作。

## 参见

[vaccess_acl_nfs4(9)](vaccess_acl_nfs4.9.md), [vaccess_acl_posix1e(9)](vaccess_acl_posix1e.9.md), [vnode(9)](vnode.9.md), [VOP_ACCESS(9)](VOP_ACCESS.9.md)

## 作者

本手册页及 `vaccess()` 的当前实现由 Robert Watson 编写。
