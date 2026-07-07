# getvfsbyname(3)

`getvfsbyname` — 获取关于文件系统的信息

## 名称

`getvfsbyname`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

```c
int
getvfsbyname(const char *name, struct xvfsconf *vfc);
```

## 描述

`getvfsbyname` 函数提供对内核中配置的文件系统模块信息的访问。如果成功，所请求的文件系统 `xvfsconf` 将返回到 `vfc` 所指向的位置。"`struct xvfsconf`" 中的字段定义如下：

**vfc_name** 文件系统的名称
**vfc_typenum** 内核分配的文件系统类型编号
**vfc_refcount** 使用该文件系统的活动挂载点数量
**vfc_flags** 标志位，如下所述

标志定义如下：

**`VFCF_STATIC`** 静态编译进内核
**`VFCF_NETWORK`** 可能通过网络获取数据
**`VFCF_READONLY`** 未实现写操作
**`VFCF_SYNTHETIC`** 数据并不代表真实文件
**`VFCF_LOOPBACK`** 别名指向某个已挂载的文件系统
**`VFCF_UNICODE`** 以 Unicode 存储文件名
**`VFCF_JAIL`** 如果设置了 `allow.mount` 和 `allow.mount.<vfc_name>` jail 参数，则可从 jail 内部挂载
**`VFCF_DELEGADMIN`** 如果 `vfs.usermount` sysctl 设置为 `1`，则支持委托管理

## 返回值

如果成功，`getvfsbyname` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

可能报告以下错误：

**[`ENOENT`]** `name` 参数指定了一个未知或未在内核中配置的文件系统。

## 参见

[lsvfs(1)](../man1/lsvfs.1.md), [jail(2)](../sys/jail.2.md), [mount(2)](../sys/mount.2.md), [sysctl(3)](sysctl.3.md), [jail(8)](../man8/jail.8.md), [mount(8)](../man8/mount.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`getvfsbyname` 函数的一个变体首次出现于 FreeBSD 2.0。
