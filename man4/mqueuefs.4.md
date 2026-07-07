# mqueuefs(4)

`mqueuefs` — POSIX 消息队列文件系统

## 名称

`mqueuefs`

## 概要

`链接进内核：`

`options P1003_1B_MQUEUE`

`作为内核可加载模块加载：`

```sh
kldload mqueuefs
```

## 描述

`mqueuefs` 模块使 FreeBSD 内核支持 POSIX 消息队列。该模块包含用于操作 POSIX 消息队列的系统调用。它还包含一个文件系统，用于为系统中的所有消息队列实现视图。这有助于用户跟踪其消息队列，并使其更易于使用，而无需发明额外的工具。

最常见的用法如下：

```sh
mount -t mqueuefs null /mnt/mqueue
```

其中 `/mnt/mqueue` 是挂载点。

可以在 `/etc/fstab` 中定义一个条目，类似于：

```sh
null	/mnt/mqueue	mqueuefs	rw	0	0
```

这将在系统引导时将 `mqueuefs` 挂载到 `/mnt/mqueue` 挂载点。不建议使用 `/mnt/mqueue` 作为永久挂载点，因为它的初衷始终是作为临时挂载点。有关 FreeBSD 目录布局的更多信息，参见 [hier(7)](../man7/hier.7.md)。

某些常用工具可在此文件系统上使用，例如：[cat(1)](../man1/cat.1.md)、[chmod(1)](../man1/chmod.1.md)、[chown(8)](../man8/chown.8.md)、[ls(1)](../man1/ls.1.md)、[rm(1)](../man1/rm.1.md) 等。若仅使用消息队列系统调用，用户无需挂载文件系统，只需加载模块或将其编译进内核。手动创建文件，例如“`touch /mnt/mqueue/myqueue`”，将在内核中创建一个名为 `myqueue` 的消息队列，并将默认的消息队列属性应用于该队列。不建议使用此方法创建队列；最好使用 mq_open(2) 系统调用来创建队列，因为它允许用户指定不同的属性。

要查看队列的属性，只需读取该文件：

```sh
cat /mnt/mqueue/myqueue
```

## 参见

[mq_open(2)](../man2/mq_open.2.md), [nmount(2)](../man2/nmount.2.md), [unmount(2)](../man2/unmount.2.md), [mount(8)](../man8/mount.8.md), [umount(8)](../man8/umount.8.md)

## 作者

本手册页由 David Xu <davidxu@FreeBSD.org> 编写。
