# extattr.9

`extattr` — 虚拟文件系统命名扩展属性

## 名称

`extattr`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/extattr.h>
```

## 描述

命名扩展属性允许将额外的元数据与表示文件和目录的 vnode 关联。这些额外数据的语义为 "name=value" 对，其中名称可以定义或不定义，若已定义，则关联零个或多个字节的任意二进制数据。扩展属性名存在于一个命名空间集合中；对扩展属性的每个操作都要求提供该操作引用的命名空间。如果同一名称出现在多个命名空间中，与这些名称关联的扩展属性独立存储和操作。以下两个命名空间是通用的，但单个文件系统可以实现额外的命名空间，也可以不实现这些命名空间：`EXTATTR_NAMESPACE_USER`、`EXTATTR_NAMESPACE_SYSTEM`。这些属性的语义意图如下：用户属性数据按文件或目录中数据所适用的常规自主和强制访问控制进行保护；系统属性数据的保护要求具有适当权限才能直接访问或操作这些属性。默认情况下，[jail(8)](../man8/jail.8.md) 中的进程无法访问系统属性数据，除非指定了 `allow.extattr` 配置参数。

读取扩展属性数据可能返回元数据的特定连续区域，类似于 VOP_READ(9) 风格，但写入会替换与给定名称关联的整个当前 "value"。由于存在大量具有不同扩展属性的文件系统，这些函数的可用性和功能可能受限，应在了解支持文件系统的底层语义的情况下使用。扩展属性数据的授权方案以及最大属性大小、是否允许定义任何或特定新属性等，也可能因文件系统而异。

扩展属性使用以 null 结尾的字符串命名。根据底层文件系统语义，此名称可能区分也可能不区分大小写。相应的 vnode 扩展属性调用为：[VOP_GETEXTATTR(9)](VOP_GETEXTATTR.9.md)、[VOP_LISTEXTATTR(9)](VOP_LISTEXTATTR.9.md) 和 [VOP_SETEXTATTR(9)](VOP_SETEXTATTR.9.md)。

## 参见

[jail(8)](../man8/jail.8.md), [VFS(9)](VFS.9.md), [VOP_GETEXTATTR(9)](VOP_GETEXTATTR.9.md), [VOP_LISTEXTATTR(9)](VOP_LISTEXTATTR.9.md), [VOP_SETEXTATTR(9)](VOP_SETEXTATTR.9.md)

## 作者

本手册页由 Robert Watson 编写。

## 缺陷

此外，该接口未提供检索当前可用属性集合的机制；有人建议提供 `NULL` 属性名时应返回传入的文件或目录已定义的属性列表，但目前尚未实现该功能。
