# posix1e(3)

`posix1e` — POSIX.1e 安全 API 简介

## 名称

`posix1e`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/acl.h>`

`#include <sys/mac.h>`

## 描述

POSIX.1e 描述了 POSIX.1 API 的五个安全扩展：访问控制列表（ACL）、审计、能力（Capabilities）、强制访问控制和信息流标签。虽然 IEEE POSIX.1e D17 规范尚未标准化，但其若干接口已被广泛使用。

FreeBSD 实现了用于访问控制列表的 POSIX.1e 接口，在 [acl(3)](acl.3.md) 中描述，并支持 [ffs(4)](../man4/ffs.4.md) 文件系统上的 ACL；ACL 必须由管理员使用 tunefs(8) 启用。

FreeBSD 实现了类 POSIX.1e 的强制访问控制接口，在 [mac(3)](mac.3.md) 中描述，但存在若干扩展和重要的语义差异。

FreeBSD 未实现 POSIX.1e 审计、特权（能力）或信息流标签 API。但 FreeBSD 实现了 libbsm(3) 审计 API。它还提供 [capsicum(4)](../man4/capsicum.4.md)，一个轻量级 OS 能力和沙箱框架，实现混合能力系统模型。

## 环境变量

POSIX.1e 为所有对象分配安全属性，扩展了 POSIX.1 中描述的安全功能。这些附加属性存储细粒度的自主访问控制信息和强制访问控制标签；对于文件，它们存储在扩展属性中，在 [extattr(3)](extattr.3.md) 中描述。

POSIX.2c 描述了一组用于操作这些属性的用户空间实用程序，包括用于访问控制列表的 getfacl(1) 和 setfacl(1)，以及用于强制访问控制标签的 getfmac(8) 和 setfmac(8)。

## 参见

getfacl(1), setfacl(1), extattr(2), [acl(3)](acl.3.md), [extattr(3)](extattr.3.md), libbsm(3), libcasper(3), [mac(3)](mac.3.md), [capsicum(4)](../man4/capsicum.4.md), [ffs(4)](../man4/ffs.4.md), getfmac(8), setfmac(8), tunefs(8), [acl(9)](../man9/acl.9.md), [extattr(9)](../man9/extattr.9.md), [mac(9)](../man9/mac.9.md)

## 标准

POSIX.1e 在 IEEE POSIX.1e 草案 17 中描述。

## 历史

POSIX.1e 支持引入于 FreeBSD 4.0；大多数特性在 FreeBSD 5.0 时可用。

## 作者

Robert N M Watson Chris D. Faulhaber Thomas Moestl Ilmar S Habibulin
