# vfs_suser(9)

`vfs_suser` — 检查凭证是否对挂载点具有超级用户权限

## 名称

`vfs_suser`

## 概要

`#include <sys/param.h>`

`#include <sys/systm.h>`

`#include <sys/mount.h>`

`int vfs_suser(struct mount *mp, struct thread *td)`

## 描述

`vfs_suser()` 函数检查给定凭证是否对给定挂载点具有超级用户权限。它将检查传入的线程是否具有与挂载文件系统的用户相同的凭证。如果是，则返回 0，否则返回 priv_check(9) 将返回的值。

## 返回值

`vfs_suser()` 函数在用户具有超级用户权限时返回 0，否则返回 `EPERM`。这与 `suser()` 的某些其他实现相反，在那些实现中 TRUE 响应表示超级用户权限。

## 参见

chroot(2), jail(2)

## 历史

`vfs_suser()` 函数引入于 FreeBSD 5.2。

## 作者

本手册页由 Alfred Perlstein 编写。
