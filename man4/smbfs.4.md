# smbfs(4)

`smbfs` — 服务器消息块（SMB1/CIFS）文件系统

## 名称

`smbfs`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> option NETSMB

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
smbfs_load="YES"
```

## 描述

SMB 驱动是 CIFS（Common Internet Filesystem）网络协议的实现。

`smbfs` 文件系统驱动仅支持已过时的 SMBv1 协议。`smbfs` 存在已知缺陷，可能有安全漏洞。`smbfs` 及其用户空间对应物 smbutil(1) 和 mount_smbfs(8) 可能会在未来版本的 FreeBSD 中移除。建议用户改用 `filesystems/smbnetfs` port。

## 参见

smbutil(1), mount_smbfs(8)

## 标准

> "Common Internet File System (CIFS) Protocol", December 2018.

> I. Heizer, P. Leach, D. Perry, "Common Internet File System Protocol (CIFS/1.0)", June 13, 1996.

## 历史

`smbfs` 设备驱动最早出现于 FreeBSD 4.4。

## 作者

`smbfs` 设备驱动由 Boris Popov <bp@FreeBSD.org> 编写。手册页由 Gordon Bergling <gbe@FreeBSD.org> 贡献。
