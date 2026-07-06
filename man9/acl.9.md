# acl.9

`acl` — 虚拟文件系统访问控制列表

## 名称

`acl`

## 概要

```c
#include <sys/param.h>

#include <sys/vnode.h>

#include <sys/acl.h>
```

在内核配置文件中：

```sh
options UFS_ACL
```

## 描述

访问控制列表（Access Control List，ACL）允许对表示文件和目录的 vnode 进行细粒度的权限指定。然而，由于存在大量具有不同 ACL 语义的文件系统，vnode 接口仅了解 ACL 的语法，而依赖底层文件系统实现细节。根据底层文件系统的不同，每个文件或目录可能关联零个或多个 ACL，通过相应 vnode ACL 调用的 `type` 字段命名：[VOP_ACLCHECK(9)](VOP_ACLCHECK.9.md)、[VOP_GETACL(9)](VOP_GETACL.9.md) 和 [VOP_SETACL(9)](VOP_SETACL.9.md)。

目前，每个 ACL 在内核中由固定大小的 `acl` 结构表示，定义如下：

```c
struct acl {
        unsigned int            acl_maxcnt;
        unsigned int            acl_cnt;
        int                     acl_spare[4];
        struct acl_entry        acl_entry[ACL_MAX_ENTRIES];
};
```

ACL 由固定大小的 ACL 条目数组构成，每个条目包含一组权限、主体命名空间和主体标识符。在本实现中，`acl_maxcnt` 字段始终设置为 `ACL_MAX_ENTRIES`。

每个单独的 ACL 条目类型为 `acl_entry_t`，这是一个包含以下成员的结构：

**`ACL_UNDEFINED_FIELD`** 未定义的 ACL 类型。

**`ACL_USER_OBJ`** 有效用户 ID 与文件所有者用户 ID 匹配的进程的自由访问权限。

**`ACL_USER`** 有效用户 ID 与 ACL 条目标识符匹配的进程的自由访问权限。

**`ACL_GROUP_OBJ`** 有效组 ID 或任意补充组与文件所有者组 ID 匹配的进程的自由访问权限。

**`ACL_GROUP`** 有效组 ID 或任意补充组与 ACL 条目标识符匹配的进程的自由访问权限。

**`ACL_MASK`** 可授予文件组类中进程的最大自由访问权限。仅对 POSIX.1e ACL 有效。

**`ACL_OTHER`** 不被任何其他 ACL 条目覆盖的进程的自由访问权限。仅对 POSIX.1e ACL 有效。

**`ACL_OTHER_OBJ`** 与 `ACL_OTHER` 相同。

**`ACL_EVERYONE`** 所有用户的自由访问权限。仅对 NFSv4 ACL 有效。

**`ACL_EXECUTE`** 进程可执行关联的文件。

**`ACL_WRITE`** 进程可写入关联的文件。

**`ACL_READ`** 进程可读取关联的文件。

**`ACL_PERM_NONE`** 进程对关联的文件没有读、写或执行权限。

**`ACL_READ_DATA`** 进程可读取关联的文件。

**`ACL_LIST_DIRECTORY`** 与 `ACL_READ_DATA` 相同。

**`ACL_WRITE_DATA`** 进程可写入关联的文件。

**`ACL_ADD_FILE`** 与 `ACL_WRITE_DATA` 相同。

**`ACL_APPEND_DATA`**

**`ACL_ADD_SUBDIRECTORY`** 与 `ACL_APPEND_DATA` 相同。

**`ACL_READ_NAMED_ATTRS`** 忽略。

**`ACL_WRITE_NAMED_ATTRS`** 忽略。

**`ACL_EXECUTE`** 进程可执行关联的文件。

**`ACL_DELETE_CHILD`**

**`ACL_READ_ATTRIBUTES`**

**`ACL_WRITE_ATTRIBUTES`**

**`ACL_DELETE`**

**`ACL_READ_ACL`**

**`ACL_WRITE_ACL`**

**`ACL_WRITE_OWNER`**

**`ACL_SYNCHRONIZE`** 忽略。

**`ACL_ENTRY_TYPE_ALLOW`**

**`ACL_ENTRY_TYPE_DENY`**

**`ACL_ENTRY_FILE_INHERIT`**

**`ACL_ENTRY_DIRECTORY_INHERIT`**

**`ACL_ENTRY_NO_PROPAGATE_INHERIT`**

**`ACL_ENTRY_INHERIT_ONLY`**

**`ACL_ENTRY_INHERITED`**

**`acl_tag_t`** `ae_tag` 以下是在 `ae_tag` 中设置的 ACL 类型定义列表：每个 POSIX.1e ACL 必须恰好包含一个 `ACL_USER_OBJ`、一个 `ACL_GROUP_OBJ` 和一个 `ACL_OTHER`。如果存在 `ACL_USER`、`ACL_GROUP` 或 `ACL_OTHER` 中的任何一个，则应恰好存在一个 `ACL_MASK` 条目。

**`uid_t`** `ae_id` 此 ACL 为其描述访问权限的用户 ID。对于 `ACL_USER` 和 `ACL_GROUP` 以外的条目，此字段应设置为 `ACL_UNDEFINED_ID`。

**`acl_perm_t`** `ae_perm` 此字段定义匹配此 ACL 的进程对关联文件的访问类型。对于 POSIX.1e ACL，以下值有效：对于 NFSv4 ACL，以下值有效：

**`acl_entry_type_t`** `ae_entry_type` 此字段定义 NFSv4 ACL 条目的类型。不用于 POSIX.1e ACL。以下值有效：

**`acl_flag_t`** `ae_flags` 此字段定义 NFSv4 ACL 条目的继承标志。不用于 POSIX.1e ACL。以下值有效：`ACL_ENTRY_INHERITED` 标志设置在从父项继承的 ACE 上。它也可以通过编程方式设置，在文件和目录上都有效。

## 参见

acl(3), [vaccess(9)](vaccess.9.md), [vaccess_acl_nfs4(9)](vaccess_acl_nfs4.9.md), [vaccess_acl_posix1e(9)](vaccess_acl_posix1e.9.md), [VFS(9)](VFS.9.md), [VOP_ACLCHECK(9)](VOP_ACLCHECK.9.md), [VOP_GETACL(9)](VOP_GETACL.9.md), [VOP_SETACL(9)](VOP_SETACL.9.md)

## 作者

本手册页由 Robert Watson 编写。
