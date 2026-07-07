# nfsiod(8)

`nfsiod` — 本地 NFS 异步 I/O 服务器

## 名称

`nfsiod` NFS 异步 I/O 服务器

## 概要

`nfsiod [-n num_servers]`

## 描述

`nfsiod` 工具控制 NFS 客户端机器上运行的 `nfsiod` 内核进程的最大数量，以服务对其服务器的异步 I/O 请求。拥有 `nfsiod` 内核进程可提高性能，但不是正确操作所必需的。

选项如下：

**`-n`** 指定允许启动的进程数。

不带选项时，`nfsiod` 显示当前设置。客户端应允许足够数量的进程来处理其最大并发级别，通常为 4 到 6 个。

如果 `nfsiod` 检测到正在运行的内核不包含 NFS 支持，它将尝试使用 [kldload(2)](../sys/kldload.2.md) 加载包含 NFS 代码的内核模块。如果此操作失败或没有可用的 NFS 模块，`nfsiod` 将以错误退出。

## 退出状态

`nfsiod` 工具成功时退出 0，发生错误时退出 >0。

## 参见

[nfsstat(1)](../man1/nfsstat.1.md), [kldload(2)](../sys/kldload.2.md), [nfssvc(2)](../sys/nfssvc.2.md), mountd(8), [nfsd(8)](nfsd.8.md), rpcbind(8)

## 历史

`nfsiod` 工具首次出现在 4.4BSD 中。

从 FreeBSD 5.0 开始，该工具不再启动守护进程，而仅作为 vfs 加载器和 [sysctl(3)](../gen/sysctl.3.md) 包装器。
