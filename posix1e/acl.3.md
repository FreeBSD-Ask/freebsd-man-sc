# acl(3)

`acl` — POSIX.1e/NFSv4 ACL 安全 API 简介

## 名称

`acl`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

## 描述

FreeBSD 允许文件系统通过 VFS 导出访问控制列表（ACL），并提供一个库供用户空间访问和操作这些 ACL。FreeBSD 支持 POSIX.1e 和 NFSv4 ACL，但并非所有文件系统都支持 ACL，某些文件系统可能需要管理员显式启用 ACL 支持。库调用包括分配、复制、检索、设置和验证与文件对象关联的 ACL 的例程。除 POSIX.1e 例程外，还定义了若干非可移植扩展，允许使用替代于 POSIX.1e 的 ACL 语义，如 NFSv4。非标准例程以 `_np` 后缀标记，表示其不可移植。

POSIX.1e 描述了一组 ACL 操作例程，用于管理 ACL 的内容及其与文件的关系；这些支持例程中的几乎全部都在 FreeBSD 中实现。

按行为分类的可用函数包括：

**`acl_add_flag_np`** 此函数在 [acl_add_flag_np(3)](acl_add_flag_np.3.md) 中描述，可用于向标志集添加标志。

**`acl_add_perm`** 此函数在 [acl_add_perm(3)](acl_add_perm.3.md) 中描述，可用于向权限集添加权限。

**`acl_calc_mask`** 此函数在 [acl_calc_mask(3)](acl_calc_mask.3.md) 中描述，可用于计算并设置与 `ACL_MASK` 条目关联的权限。

**`acl_clear_flags_np`** 此函数在 [acl_clear_flags_np(3)](acl_clear_flags_np.3.md) 中描述，可用于清除标志集中的所有标志。

**`acl_clear_perms`** 此函数在 [acl_clear_perms(3)](acl_clear_perms.3.md) 中描述，可用于清除权限集中的所有权限。

**`acl_copy_entry`** 此函数在 [acl_copy_entry(3)](acl_copy_entry.3.md) 中描述，可用于复制 ACL 条目的内容。

**`acl_create_entry`**, **`acl_create_entry_np`** 这些函数在 [acl_create_entry(3)](acl_create_entry.3.md) 中描述，可用于在 ACL 中创建空条目。

**`acl_delete_def_file`**, **`acl_delete_def_link_np`**, **`acl_delete_fd_np`**, **`acl_delete_file_np`**, **`acl_delete_link_np`** 这些函数在 [acl_delete(3)](acl_delete.3.md) 中描述，可用于从文件系统对象删除 ACL。

**`acl_delete_entry`**, **`acl_delete_entry_np`** 这些函数在 [acl_delete_entry(3)](acl_delete_entry.3.md) 中描述，可用于从 ACL 中删除条目。

**`acl_delete_flag_np`** 此函数在 [acl_delete_flag_np(3)](acl_delete_flag_np.3.md) 中描述，可用于从标志集删除标志。

**`acl_delete_perm`** 此函数在 [acl_delete_perm(3)](acl_delete_perm.3.md) 中描述，可用于从权限集删除权限。

**`acl_dup`** 此函数在 [acl_dup(3)](acl_dup.3.md) 中描述，可用于复制 ACL 结构。

**`acl_free`** 此函数在 [acl_free(3)](acl_free.3.md) 中描述，可用于释放用户空间 ACL 工作存储。

**`acl_from_text`** 此函数在 [acl_from_text(3)](acl_from_text.3.md) 中描述，若 ACL 具有 POSIX.1e 或 NFSv4 语义，可用于将文本形式的 ACL 转换为工作 ACL 状态。

**`acl_get_brand_np`** 此函数在 [acl_get_brand_np(3)](acl_get_brand_np.3.md) 中描述，可用于确定 ACL 具有 POSIX.1e 还是 NFSv4 语义。

**`acl_get_entry`** 此函数在 [acl_get_entry(3)](acl_get_entry.3.md) 中描述，可用于从 ACL 中检索指定的 ACL 条目。

**`acl_get_fd`**, **`acl_get_fd_np`**, **`acl_get_file`**, **`acl_get_link_np`** 这些函数在 [acl_get(3)](acl_get.3.md) 中描述，可用于从文件系统对象检索 ACL。

**`acl_get_entry_type_np`** 此函数在 [acl_get_entry_type_np(3)](acl_get_entry_type_np.3.md) 中描述，可用于从 ACL 条目检索 ACL 类型。

**`acl_get_flagset_np`** 此函数在 [acl_get_flagset_np(3)](acl_get_flagset_np.3.md) 中描述，可用于从 ACL 条目检索标志集。

**`acl_get_perm_np`** 此函数在 [acl_get_perm_np(3)](acl_get_perm_np.3.md) 中描述，可用于检查权限集中是否设置了某权限。

**`acl_get_permset`** 此函数在 [acl_get_permset(3)](acl_get_permset.3.md) 中描述，可用于从 ACL 条目检索权限集。

**`acl_get_qualifier`** 此函数在 [acl_get_qualifier(3)](acl_get_qualifier.3.md) 中描述，可用于从 ACL 条目检索限定符。

**`acl_get_tag_type`** 此函数在 [acl_get_tag_type(3)](acl_get_tag_type.3.md) 中描述，可用于从 ACL 条目检索标签类型。

**`acl_init`** 此函数在 [acl_init(3)](acl_init.3.md) 中描述，可用于分配新的（空）ACL 结构。

**`acl_is_trivial_np`** 此函数在 [acl_is_trivial_np(3)](acl_is_trivial_np.3.md) 中描述，可用于查明 ACL 是否为平凡 ACL。

**`acl_set_fd`**, **`acl_set_fd_np`**, **`acl_set_file`**, **`acl_set_link_np`** 这些函数在 [acl_set(3)](acl_set.3.md) 中描述，可用于将 ACL 分配给文件系统对象。

**`acl_set_entry_type_np`** 此函数在 [acl_set_entry_type_np(3)](acl_set_entry_type_np.3.md) 中描述，可用于设置 ACL 条目的 ACL 类型。

**`acl_set_flagset_np`** 此函数在 [acl_set_flagset_np(3)](acl_set_flagset_np.3.md) 中描述，可用于从标志集设置 ACL 条目的标志。

**`acl_set_permset`** 此函数在 [acl_set_permset(3)](acl_set_permset.3.md) 中描述，可用于从权限集设置 ACL 条目的权限。

**`acl_set_qualifier`** 此函数在 [acl_set_qualifier(3)](acl_set_qualifier.3.md) 中描述，可用于设置 ACL 的限定符。

**`acl_set_tag_type`** 此函数在 [acl_set_tag_type(3)](acl_set_tag_type.3.md) 中描述，可用于设置 ACL 的标签类型。

**`acl_strip_np`** 此函数在 [acl_strip_np(3)](acl_strip_np.3.md) 中描述，可用于从 ACL 中移除扩展条目。

**`acl_to_text`**, **`acl_to_text_np`** 这些函数在 [acl_to_text(3)](acl_to_text.3.md) 中描述，可用于生成 POSIX.1e 或 NFSv4 语义 ACL 的文本形式。

**`acl_valid`**, **`acl_valid_fd_np`**, **`acl_valid_file_np`**, **`acl_valid_link_np`** 这些函数在 [acl_valid(3)](acl_valid.3.md) 中描述，可用于验证 ACL 为正确的 POSIX.1e 语义，或无论语义如何均适合特定文件系统对象。

支持这些调用的内部内核接口文档可在 [acl(9)](../man9/acl.9.md) 中找到。内部接口与公共库例程之间的系统调用可能随时间变化，因此未予记载。它们不打算在不通过库的情况下直接调用。

## 参见

getfacl(1), setfacl(1), [acl_add_flag_np(3)](acl_add_flag_np.3.md), [acl_add_perm(3)](acl_add_perm.3.md), [acl_calc_mask(3)](acl_calc_mask.3.md), [acl_clear_flags_np(3)](acl_clear_flags_np.3.md), [acl_clear_perms(3)](acl_clear_perms.3.md), [acl_copy_entry(3)](acl_copy_entry.3.md), [acl_create_entry(3)](acl_create_entry.3.md), [acl_delete_entry(3)](acl_delete_entry.3.md), [acl_delete_flag_np(3)](acl_delete_flag_np.3.md), [acl_delete_perm(3)](acl_delete_perm.3.md), [acl_dup(3)](acl_dup.3.md), [acl_free(3)](acl_free.3.md), [acl_from_text(3)](acl_from_text.3.md), [acl_get(3)](acl_get.3.md), [acl_get_brand_np(3)](acl_get_brand_np.3.md), [acl_get_entry_type_np(3)](acl_get_entry_type_np.3.md), [acl_get_flagset_np(3)](acl_get_flagset_np.3.md), [acl_get_perm_np(3)](acl_get_perm_np.3.md), [acl_get_permset(3)](acl_get_permset.3.md), [acl_get_qualifier(3)](acl_get_qualifier.3.md), [acl_get_tag_type(3)](acl_get_tag_type.3.md), [acl_init(3)](acl_init.3.md), [acl_is_trivial_np(3)](acl_is_trivial_np.3.md), [acl_set(3)](acl_set.3.md), [acl_set_entry_type_np(3)](acl_set_entry_type_np.3.md), [acl_set_flagset_np(3)](acl_set_flagset_np.3.md), [acl_set_permset(3)](acl_set_permset.3.md), [acl_set_qualifier(3)](acl_set_qualifier.3.md), [acl_set_tag_type(3)](acl_set_tag_type.3.md), [acl_strip_np(3)](acl_strip_np.3.md), [acl_to_text(3)](acl_to_text.3.md), [acl_valid(3)](acl_valid.3.md), [posix1e(3)](posix1e.3.md), [acl(9)](../man9/acl.9.md)

## 标准

POSIX.1e 为所有对象分配安全标签，扩展了 POSIX.1 中描述的安全功能。这些附加标签提供细粒度的自主访问控制、细粒度的能力，以及强制访问控制所需的标签。POSIX.2c 描述了一组用于操作这些标签的用户空间实用程序。

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0；FreeBSD 5.0 是首个包含基于 UFS 和 UFS2 文件系统扩展属性的完整 ACL 实现的版本。NFSv4 ACL 支持引入于 FreeBSD 8.0。

getfacl(1) 和 setfacl(1) 实用程序描述了允许直接操作完整文件 ACL 的用户工具。

## 作者

Robert N M Watson
