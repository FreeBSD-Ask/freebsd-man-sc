# newfs_msdos(8)

`newfs_msdos` — 构造新的 MS-DOS（FAT）文件系统

## 名称

`newfs_msdos`

## 概要

`newfs_msdos [-N] [-@ offset] [-A] [-B boot] [-C create-size] [-F FAT-type] [-I VolumeID] [-L label] [-O OEM] [-S sector-size] [-T timestamp] [-a FAT-size] [-b block-size] [-c cluster-size] [-e DirEnts] [-f format] [-h heads] [-i info] [-k backup] [-m media] [-n FATs] [-o hidden] [-r reserved] [-s total] [-u track-size] special [disktype]`

## 描述

`newfs_msdos` 工具在名为 `special` 的设备或文件上创建 FAT12、FAT16 或 FAT32 文件系统，如果需要，使用 [disktab(5)](../man5/disktab.5.md) 条目 `disktype` 来确定几何参数。

如果 `special` 不包含 `/` 且未使用 `-C`，则假定它是设备名，并在名称前加上 **/dev/** 以构造实际设备名。要使用当前目录中的文件，请使用 `./filename`。

选项如下：

**`-N`** 不创建文件系统：仅打印参数。

**`-@`** `offset` 在设备或文件中以指定偏移量（字节）构建文件系统。附加到偏移量的后缀 s、k、m、g（小写或大写）分别指定数字以扇区、千字节、兆字节或吉字节为单位。

**`-A`** 尝试对数据区域进行簇对齐，对于基于闪存的存储有用。此选项默认启用，除非使用 `-r` 选项指定了保留扇区数。

**`-B`** `boot` 从文件获取引导程序。

**`-C`** `create-size` 创建指定大小的镜像文件。附加到大小后面的后缀字符的解释与 `-@` 选项相同。该文件通过截断任何同名的现有文件并将其调整为请求的大小来创建。如果文件系统支持稀疏文件，则磁盘上占用的空间可能小于指定为参数的大小。

**`-F`** `FAT-type` FAT 类型（12、16 或 32 之一）。

**`-I`** `VolumeID` 卷 ID，以十进制或十六进制（0x...）格式表示的 32 位数字。

**`-L`** `label` 卷标（最多 11 个字符）。卷标应仅包含常规 DOS（8+3）文件名中允许的字符。

**`-O`** `OEM` OEM 字符串（最多 8 个字符）。默认为 “`BSD4.4`”。

**`-S`** `sector-size` 每扇区字节数。可接受的值为 512 到 32768（含）范围内的 2 的幂。

**`-T`** `timestamp` 创建文件系统时如同当前时间为 `timestamp`。默认的文件系统卷 ID 派生自时间。`timestamp` 可以是路径名（时间戳从该文件派生）或解释为自 Epoch 以来秒数的整数值。

**`-a`** `FAT-size` 每个 FAT 的扇区数。

**`-b`** `block-size` 文件系统块大小（每簇字节数）。这应解析为可接受的每簇扇区数（见下文）。

**`-c`** `cluster-size` 每簇扇区数，也称为分配大小。可接受的值为 1 到 128 范围内的 2 的幂。如果未指定块或簇大小，代码根据文件系统大小使用 512 字节到 32K 之间的簇。

**`-e`** `DirEnts` 根目录条目数（仅 FAT12 和 FAT16）。

**`-f`** `format` 指定标准（软盘）格式。标准格式为（容量以千字节为单位）：160、180、320、360、640、720、1200、1232、1440、2880。

**`-h`** `heads` 磁头数。

**`-i`** `info` 文件系统信息扇区的位置（仅 FAT32）。值 0xffff 表示无信息扇区。

**`-k`** `backup` 备份引导扇区的位置（仅 FAT32）。值 0xffff 表示无备份扇区。

**`-m`** `media` 介质描述符（可接受范围 0xf0 到 0xff）。

**`-n`** `FATs` FAT 数量。可接受的值为 1 到 16（含）。默认为 2。

**`-o`** `hidden` 隐藏扇区数。

**`-r`** `reserved` 保留扇区数。如果未使用 `-r` 选项，保留扇区数将设置为一个使数据区域起始对齐到簇大小倍数的值。

**`-s`** `total` 文件系统大小。

**`-u`** `track-size` 每磁道扇区数。

## 注释

如果某些参数（如大小、扇区数等）未通过选项或 disktype 指定，程序会尝试自动生成它们。特别是，大小确定为设备或文件大小减去用 `-@` 选项指定的偏移量。当几何参数不可用时，假定为 63 扇区、255 磁头。然后将大小取整为磁道大小的倍数，以避免某些文件系统代码的抱怨。

FAT 文件系统参数占据实际文件系统之前的“保留”扇区中第一个扇区中的“Boot Sector BPB（BIOS Parameter Block）”。供参考，下面展示此结构。

```sh
struct bsbpb {
    uint16_t	bpbBytesPerSec;		/* [-S] 每扇区字节数 */
    uint8_t	bpbSecPerClust;		/* [-c] 每簇扇区数 */
    uint16_t	bpbResSectors;		/* [-r] 保留扇区数 */
    uint8_t	bpbFATs;		/* [-n] FAT 数量 */
    uint16_t	bpbRootDirEnts;		/* [-e] 根目录条目数 */
    uint16_t	bpbSectors;		/* [-s] 总扇区数 */
    uint8_t	bpbMedia;		/* [-m] 介质描述符 */
    uint16_t	bpbFATsecs;		/* [-a] 每 FAT 扇区数 */
    uint16_t	bpbSecPerTrack;		/* [-u] 每磁道扇区数 */
    uint16_t	bpbHeads;		/* [-h] 磁头数 */
    uint32_t	bpbHiddenSecs;		/* [-o] 隐藏扇区数 */
    uint32_t	bpbHugeSectors;		/* [-s] 大总扇区数 */
};
/* FAT32 扩展 */
struct bsxbpb {
    uint32_t	bpbBigFATsecs;		/* [-a] 大每 FAT 扇区数 */
    uint16_t	bpbExtFlags;		/* 控制标志 */
    uint16_t	bpbFSVers;		/* 文件系统版本 */
    uint32_t	bpbRootClust;		/* 根目录起始簇 */
    uint16_t	bpbFSInfo;		/* [-i] 文件系统信息扇区 */
    uint16_t	bpbBackup;		/* [-k] 备份引导扇区 */
};
```

## 限制

最大文件大小为 4GB，即使文件系统本身更大。

## 退出状态

成功时退出状态为 0，出错时为 1。

## 实例

使用默认参数在 **/dev/ada0s1** 上创建文件系统：

```sh
newfs_msdos /dev/ada0s1
```

在 **/dev/mmcsd0s1** 上创建具有 32K 分配大小的 FAT32 文件系统：

```sh
newfs_msdos -F 32 -A -c 64 /dev/mmcsd0s1
```

在 **/dev/fd0** 上创建标准的 1.44M 文件系统，卷标为 `foo`：

```sh
newfs_msdos -f 1440 -L foo fd0
```

创建一个 30MB 的镜像文件，FAT 分区从镜像文件内 63 扇区处开始：

```sh
newfs_msdos -C 30M -@63s ./somefile
```

## 参见

[msdosfs(4)](../man4/msdosfs.4.md), [gpart(8)](gpart.8.md), newfs(8)

## 历史

`newfs_msdos` 工具首次出现在 FreeBSD 3.0 中。

## 作者

Robert Nordier <rnordier@FreeBSD.org>
