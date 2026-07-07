# p9fs(4)

`p9fs` — 9P 文件系统

## 名称

`p9fs`, `virtio_p9fs`

## 概要

`要使用此文件系统，可在内核配置中加入以下内容：`

> options P9FS
> device virtio_p9fs

`或者，将驱动作为内核模块加载，可在引导时通过在 loader.conf(5) 中加入以下内容：`

```sh
virtio_p9fs_load="YES"
```

`或在系统启动时使用以下命令：`

```sh
# sysrc kld_list+=virtio_p9fs
```

## 描述

`virtio_p9fs` 文件系统使用 9P 协议将主机文件系统目录挂载到 [bhyve(8)](../man8/bhyve.8.md) 客户机中。可以使用 [bhyve(8)](../man8/bhyve.8.md) 的 virtio-9p 虚拟 PCI 设备访问多个主机目录。每个设备配置有一个共享名称和一个主机目录路径。共享名称可与 [mount(8)](../man8/mount.8.md) 一起使用，将主机目录挂载到客户机中：

```sh
# mount -t p9fs mysharename /mnt
```

可使用 [fstab(5)](../man5/fstab.5.md) 在系统启动时挂载主机目录，如下所示：

```sh
mysharename	/mnt	p9fs	rw	0	0
```

通过在 loader.conf(5) 中加入以下内容，支持将 `virtio_p9fs` 用作根文件系统：

```sh
vfs.root.mountfrom="p9fs:mysharename"
```

## 限制

9P 协议依赖于有状态的文件打开操作，将协议级 FID 映射到主机文件描述符。FreeBSD vnode 接口不支持这一点，`virtio_p9fs` 使用启发式方法来猜测文件操作要使用的正确 FID。

这可能会因权限降低而被混淆，并且不保证为某个文件打开操作创建的 FID 总是被使用，即使调用进程使用的是来自原始 open 调用的文件描述符。

特别是，使用打开的文件描述符访问未链接的文件可能无法正常工作。如果 `virtio_p9fs` 是根文件系统，建议与 tmpfs(5) 一起使用，以确保在 **/tmp** 或 **/var/tmp** 中创建的临时文件具有预期的语义。

## 参见

[fstab(5)](../man5/fstab.5.md), [mount(8)](../man8/mount.8.md)

## 历史

9P 协议最早出现于 Plan 9 操作系统。最近，该协议被广泛用于虚拟机中，以允许在客户机 VM 内使用主机文件资源。

## 作者

此文件系统派生自 Juniper Networks, Inc. 发布的软件，并由 Steve Wills 进行了许多改进和修复。

本手册页由 Doug Rabson <dfr@FreeBSD.org> 编写。

## 缺陷

此文件系统更合适的名称应为 `9pfs`，但由于技术原因，文件系统的名称必须是有效的 C 标识符。作为折中，该文件系统命名为 `virtio_p9fs`。
