# tarfs.4

`tarfs` — tarball 文件系统

## 名称

`tarfs`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options TARFS

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
tarfs_load="YES"
```

## 描述

`tarfs` 驱动实现由 tar(5) 文件支撑的只读文件系统。目前仅支持 POSIX 归档，可选择使用 zstd(1) 压缩。

可使用 `vfs.tarfs.ioshift` sysctl 设置和可调参数调整 `tarfs` 文件系统的首选 I/O 大小。将其设为 0 会重置为默认值。注意，对此设置的更改仅应用于更改后挂载的文件系统。

当支撑 tar 文件使用 zstd(1) 压缩时，通过确保压缩数据被分割为多个帧，可以提高 I/O 性能。这有助于最小化不必要的解压工作。使用 [bsdtar(1)](../man1/bsdtar.1.md) 创建 tar 文件时，可使用 `zstd:max-frame-size` 和 `zstd:frame-per-file` 选项实现此目的。合理的帧大小是系统的基本页大小（参见 [arch(7)](../man7/arch.7.md)）与 **kern.maxphys** sysctl 值之间的 2 的幂。较小的帧通常会产生较差的压缩比，并需要额外的内核内存来维护索引；较大的帧在执行随机 I/O 时平均需要更多 CPU 时间来访问数据。

## 诊断

如果通过 `TARFS_DEBUG` 内核选项启用，`vfs.tarfs.debug` sysctl 设置可用于控制 `tarfs` 驱动的调试输出。可通过将下表中的相关值相加来启用驱动各部分的调试输出。

| 0x01 | 内存分配 |
| --- | --- |
| 0x02 | 校验和计算 |
| 0x04 | 文件系统操作（vfsops） |
| 0x08 | 路径查找 |
| 0x10 | 文件操作（vnops） |
| 0x20 | 通用 I/O |
| 0x40 | 解压 |
| 0x80 | 解压索引 |
| 0x100 | 稀疏文件映射 |
| 0x200 | 跳转缓冲区使用 |

## 参见

[tar(1)](../man1/tar.1.md), zstd(1), [fstab(5)](../man5/fstab.5.md), tar(5), [mount(8)](../man8/mount.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`tarfs` 驱动由 Stephen J. Kiernan <stevek@FreeBSD.org> 和 Dag-Erling Smørgrav <des@FreeBSD.org> 为 Juniper Networks 和 Klara Systems 开发。本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 为 Juniper Networks 和 Klara Systems 编写。
