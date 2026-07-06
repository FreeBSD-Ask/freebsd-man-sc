# vaccess\_acl\_nfs4.9

`vaccess_acl_nfs4` — 使用 vnode 参数生成 NFSv4 ACL 访问控制决策

## 名称

`vaccess_acl_nfs4`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`#include <sys/acl.h>`

`int vaccess_acl_nfs4(enum vtype type, uid_t file_uid, gid_t file_gid, struct acl *acl, accmode_t accmode, struct ucred *cred, int *privused)`

## 描述

此调用实现了具有 NFSv4 ACL 扩展的 UNIX 自主文件安全模型的逻辑。它接受 vnode 类型 `type`、所有者 UID `file_uid`、所有者 GID `file_gid`、文件的访问 ACL `acl`、所需的访问模式 `accmode`、请求凭证 `cred`，以及一个可选的按引用传递的 `int` 指针，用于返回成功评估调用是否需要特权；`privused` 指针可由调用者设为 `NULL` 以不接收特权信息，也可指向一个整数，如果使用了特权则设为 1，否则设为 0。

此调用旨在支持 [VOP_ACCESS(9)](VOP_ACCESS.9.md) 的实现，这些实现将使用自身的访问方法来检索 vnode 属性，然后调用 `vaccess_acl_nfs4()` 来执行实际检查。[VOP_ACCESS(9)](VOP_ACCESS.9.md) 的实现可以选择实现额外的安全机制，其结果将与返回值组合。

`vaccess_acl_nfs4()` 使用的算法基于 NFSv4 ACL 评估算法，如 NFSv4 Minor Version 1, draft-ietf-nfsv4-minorversion1-21.txt 中所述。该算法从访问 ACL 中选择一个*匹配*条目，然后可与可用的 ACL 掩码条目组合，提供 UNIX 安全兼容性。

为当前凭证选择适当的保护后，将把请求的访问模式与 vnode 类型结合，与凭证可用的自主权限进行比较。如果自主保护授予的权限不足，则还会考虑凭证可用的超级用户特权。

## 返回值

`vaccess_acl_nfs4()` 成功时返回 0，失败时返回非零错误值。

## 错误

**[`EACCES`]** 权限被拒绝。尝试以文件访问权限禁止的方式访问文件。

**[`EPERM`]** 操作不允许。尝试执行限于具有适当特权的进程或文件或其他资源所有者的操作。

## 参见

[vaccess(9)](vaccess.9.md), [vnode(9)](vnode.9.md), [VOP_ACCESS(9)](VOP_ACCESS.9.md)

## 作者

`vaccess_acl_nfs4()` 的当前实现由 Edward Tomasz Napierala <trasz@FreeBSD.org> 编写。

## 缺陷

本手册页应包含 NFSv4 ACL 评估算法的完整描述，或交叉引用另一页包含此描述的页面。
