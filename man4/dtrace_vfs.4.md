# dtrace_vfs.4

`dtrace_vfs` — 用于虚拟文件系统（VFS）的 DTrace 提供者

## 名称

`dtrace_vfs`

## 概要

`vfs : fplookup: function : name vfs : namecache: function : name vfs : namei: function : name vfs : vop: function : name`

## 描述

DTrace `vfs` 提供者允许用户跟踪 [VFS(9)](../man9/vfs.9.md) 层中的事件，该层是 FreeBSD 中文件系统的内核接口。

运行 `dtrace -l -P vfs` 可列出所有 `vfs` 探测。添加 `-v` 可生成程序稳定性报告，其中包含探测参数数量及其类型的信息。

`fplookup` 模块定义了单个探测 Fn vfs:fplookup:lookup:done struct nameidata *ndp int line bool status_code，用于插桩 [VFS(9)](../man9/vfs.9.md) 中的快速路径查找代码。

`namecache` 模块提供与 [VFS(9)](../man9/vfs.9.md) 缓存相关的探测。更多详情请参阅 `src/sys/kern/vfs_cache.c` 中的源代码。

`namei` 模块管理与路径名转换和查找操作相关的探测。更多信息请参见 [namei(9)](../man9/namei.9.md)。

`vop` 模块包含与负责 [vnode(9)](../man9/vnode.9.md) 操作的函数相关的探测。

## 兼容性

此提供者为 FreeBSD 专有。

## 实例

检查哪些查找未能以无锁方式处理：

```sh
# dtrace -n 'vfs:fplookup:lookup:done { @[arg1, arg2] = count(); }'
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [d(7)](../man7/d.7.md), [SDT(9)](../man9/sdt.9.md), [namei(9)](../man9/namei.9.md), [VFS(9)](../man9/vfs.9.md)

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, pp. pp. 335-351, Prentice Hall, 2011.

## 作者

FreeBSD `vfs` 提供者由 Robert Watson <rwatson@FreeBSD.org> 编写。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
