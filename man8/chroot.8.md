# chroot.8

`chroot` — 更改根目录

## 名称

`chroot`

## 概要

`chroot [-G group[,group ...]] [-g group] [-u user] [-n] newroot [command [arg ...]]`

## 描述

`chroot` 工具将其当前目录和根目录更改为指定的目录 `newroot`，然后使用提供的参数执行 `command`（如果提供了的话），或执行用户登录 shell 的交互式副本。

可用选项如下：

**`-G`** `group`[`,``group ...`] 以指定的组作为附加组运行命令。

**`-g`** `group` 以指定的 `group` 作为实际、有效和保存的组运行命令。

**`-u`** `user` 以指定的 `user` 作为实际、有效和保存的用户运行命令。

**`-n`** 在执行 chroot 之前使用 `PROC_NO_NEW_PRIVS_CTL` procctl(2) 命令，有效地为调用进程及其子进程禁用 SUID/SGID 位。如果将 `security.bsd.unprivileged_chroot` sysctl 设置为 1，则可以在没有超级用户权限的情况下执行 chroot。

## 环境变量

`chroot` 会引用以下环境变量：

**`SHELL`** 如果已设置，则将 `SHELL` 指定的字符串解释为要执行的 shell 名称。如果未设置 `SHELL` 变量，则使用 **/bin/sh**。

## 实例

**示例 1：** 进入新的根目录

以下命令在 chroot 到标准根目录后打开 [csh(1)](../man1/csh.1.md) shell。

```sh
# chroot / /bin/csh
```

**示例 2：** 在更改的根目录中执行命令

以下命令使用 `chroot` 更改根目录，然后运行 [ls(1)](../man1/ls.1.md) 列出 **/sbin** 的内容。

```sh
# chroot /tmp/testroot ls /sbin
```

## 参见

chdir(2), chroot(2), setgid(2), setgroups(2), setuid(2), getgrnam(3), [environ(7)](../man7/environ.7.md), [jail(8)](jail.8.md)

## 历史

`chroot` 工具首次出现于 AT&T System III UNIX 和 4.3BSD。
