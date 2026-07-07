# md(4)

`md` — 内存盘

## 名称

`md`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device md

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
geom_md_load="YES"
```

## 描述

`md` 驱动提供对四种内存支持的虚拟磁盘的支持：

**`malloc`** 使用 [malloc(9)](../man9/malloc.9.md) 分配后端存储。仅使用一个 malloc 桶，这意味着所有使用 `malloc` 后端的 `md` 设备必须共享 malloc 每桶配额。此配额的确切大小会变化，特别是会随系统中的 RAM 量而变化。可以使用 [vmstat(8)](../man8/vmstat.8.md) 确定确切值。

**`preload`** 由 [loader(8)](../man8/loader.8.md) 加载的类型为‘md_image’的模块用作后端存储。为向后兼容，类型‘mfs_root’也被识别。参见 loader.conf(5) 中模块加载指令的描述，注意模块名称将是映像文件的绝对路径或 `module_path` 中文件的名称。如果内核使用选项 `MD_ROOT` 创建，则找到的第一个预加载映像将成为根文件系统。

**`vnode`** 使用常规文件作为后端存储。这允许挂载 ISO 映像，而无需通过实际物理介质这一繁琐过程。

**`swap`** 后端存储从缓冲区内存中分配。在系统内存紧张时，页面会被推送到 swap，否则它们会保留在操作内存中。使用 `swap` 后端通常比使用 `malloc` 后端更可取。

更多信息请参见 mdconfig(8)。

## 实例

要创建带有 ramdisk 或 MD 文件系统的内核，你的内核配置需要以下选项：

```sh
options 	MD_ROOT			# MD 是潜在的根设备
options 	MD_ROOT_READONLY	# 禁止以可写方式挂载根文件系统
options 	MD_ROOT_SIZE=8192	# 8MB 内存盘
makeoptions	MFS_IMAGE=/h/foo/ARM-MD
options 	ROOTDEVNAME=\"ufs:md0\"
```

**`/h/foo/ARM-MD`** 中的映像将在每次引导时作为初始映像加载。要创建要使用的映像，请按照 mdconfig(8) 手册页中创建文件支持磁盘的步骤操作。其他工具（如 NanoBSD）也会创建这些映像。

## ARM 内核选项

在 armv7 架构上，大于约 55 MiB 的 MD_ROOT 映像可能需要使用几个与内核内存使用相关的调优选项来构建自定义内核。

**`options LOCORE_MAP_MB=<num>`** 配置在早期初始化阶段为内核映射的内存量。该值必须至少与内核加上所有预加载模块（包括根映像）一样大。将此值设置得过大没有副作用，只要不超过物理内存量即可。默认值为 64 MiB。

**`options NKPT2PG=<num>`** 配置内核初始化期间预分配的内核 L2 页表页数。每个 L2 页可以映射 4 MiB 内核空间。该值必须足够大以映射内核加上所有预加载模块（包括根映像）。默认值为 32，足以映射 128 MiB。

**`options VM_KMEM_SIZE_SCALE=<num>`** 配置专用于 kmem_arena 映射的内核虚拟地址（KVA）空间量。比例值是物理页与虚拟页的比率。默认值 3 为系统中每 3 页物理 RAM 分配 1 页 KVA。内核和模块（包括根映像）也会消耗 KVA。大的根映像与默认缩放的组合可能会预分配过多 KVA，导致没有足够的剩余地址空间来分配内核栈、IO 缓冲区和其他不属于 kmem_arena 的资源。kmem_arena 空间过度分配可能表现为无法启动用户空间进程，并出现“cannot allocate kernel stack” 消息。将比例值设置得过高可能导致内核无法分配内存，因为 kmem_arena 太小，且此故障可能需要大量运行时间才会显现。根据经验，对于具有 2 GiB 物理 RAM 的系统上的 200 MiB 根映像，值为 5 效果良好。

## 参见

[gpart(8)](../man8/gpart.8.md), [loader(8)](../man8/loader.8.md), mdconfig(8), mdmfs(8), newfs(8), [vmstat(8)](../man8/vmstat.8.md)

## 历史

`md` 驱动首次出现于 FreeBSD 4.0，作为对 PicoBSD 和 FreeBSD 安装过程中先前使用的 MFS 功能的更整洁替代。

`md` 驱动在 FreeBSD 5.0 中强制接管了 **vn** 驱动。

## 作者

`md` 驱动由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。
