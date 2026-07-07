# geom_uzip(4)

`geom_uzip` — 基于 GEOM 的压缩磁盘映像和分区

## 名称

`geom_uzip`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device xz
> options zstd
> options GEOM_UZIP

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
geom_uzip_load="YES"
```

## 描述

`geom_uzip` 框架提供对压缩只读磁盘映像的支持。这可以节省大量存储空间，代价是每次读取时消耗一些 CPU 时间。写入 GEOM 标签区域的数据允许 `geom_uzip` 检测通过 mkuzip(8) 创建的压缩映像，并通过 [md(4)](md.4.md) 将其作为逻辑磁盘设备呈现给内核。`geom_uzip` 为每个映像创建唯一的 `md#.uzip` 设备。

`geom_uzip` 不仅限于支持 [md(4)](md.4.md) 映像。映像也可驻留在块设备上。（例如磁盘、USB 闪存盘、DVD-ROM 等）。相应的设备节点将以 `.uzip` 后缀出现。

```sh
# gpart show da0
=>      0  7833600  da0  BSD  (3.7G)
        0  2097152    1  freebsd-ufs  (1.0G)
  2097152  5736448       - free -  (2.7G)
# gpart add -t freebsd-ufs -s 1G da0
da0b added
# dd if=/tmp/20160217_dcomp_zcomp.uzip bs=256k of=/dev/da0b
3190+1 records in
3190+1 records out
836331008 bytes transferred in 111.021489 secs (7533055 bytes/sec)
# fsck -t ffs /dev/da0b.uzip
** /dev/da0b.uzip (NO WRITE)
** Last Mounted on /mnt
** Phase 1 - Check Blocks and Sizes
** Phase 2 - Check Pathnames
** Phase 3 - Check Connectivity
** Phase 4 - Check Reference Counts
** Phase 5 - Check Cyl groups
97455 files, 604242 used, 184741 free (2349 frags, 22799 blocks,
   0.3% fragmentation)
# mount -o ro /dev/da0b.uzip /mnt
# df /dev/da0b.uzip
Filesystem     1K-blocks    Used  Avail Capacity  Mounted on
/dev/da0b.uzip   3155932 2416968 738964    77%    /mnt
```

`geom_uzip` 设备随后由 FreeBSD 内核用于访问解压后的数据。`geom_uzip` 驱动程序不允许对底层磁盘映像进行写操作。要检查哪些“providers”与给定 `geom_uzip` 设备匹配：

```sh
# geom uzip list
Geom name: md1.uzip
Providers:
1. Name: md1.uzip
   Mediasize: 22003712 (21M)
   Sectorsize: 512
Consumers:
1. Name: md1
   Mediasize: 9563648 (9.1M)
   Sectorsize: 512
Geom name: da0b.uzip
Providers:
1. Name: da0b.uzip
   Mediasize: 3355443200 (3.1G)
   Sectorsize: 512
Consumers:
1. Name: da0b
   Mediasize: 1073741824 (1.0G)
   Sectorsize: 512
```

`geom_uzip` 允许通过设置 `vfs.root.mountfrom` 可调参数从压缩磁盘分区挂载根文件系统。详见 loader.conf(5)。

## 诊断

通过以下 sysctl 提供若干标志，用于跟踪 `geom_uzip` I/O 操作和 TOC 解析。

**`kern.geom.uzip.debug`** 日志级别。零禁用日志记录。较高的值为 `geom_uzip` 启用更详细的调试日志记录。支持的级别从 0（无日志记录）到 4（最大日志记录量）。

**`kern.geom.uzip.debug_block`** 记录涉及压缩簇号的操作。

## 参见

GEOM(4), [md(4)](md.4.md), geom(8), mkuzip(8)

## 历史

Zstd 支持在 FreeBSD 13.0 中添加。

## 作者

`geom_uzip` 驱动程序由 Max Khon <fjoe@FreeBSD.org> 编写。块去重代码以及一些 `geom_uzip` 驱动程序优化由 Maxim Sobolev <sobomax@FreeBSD.org> 贡献。LZMA 解压缩支持和 CLOOP 3.0 支持由 Aleksandr Rybalko <ray@FreeBSD.org> 添加。

本手册页由 Ceri Davies <ceri@FreeBSD.org> 编写。
