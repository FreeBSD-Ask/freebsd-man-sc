# df(1)

`df` — 显示可用磁盘空间

## 名称

`df`

## 概要

`df [--libxo] [-b | -g | -H | -h | -k | -m | -P] [-acilnT] [-,] [-t type] [file | filesystem ...]`

## 描述

`df` 实用程序显示指定已挂载 `file system` 或 `file` 所在文件系统上可用磁盘空间的相关统计信息。默认情况下，块计数以 512 字节为假定块大小显示。如果未指定文件或文件系统操作数，则显示所有已挂载文件系统的统计信息（受下文 `-t` 选项约束）。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。有关命令行参数的详细信息，请参见 xo_options(7)。

**`-a`** 显示所有挂载点，包括那些以 `MNT_IGNORE` 标志挂载的挂载点。对于命令行中指定的文件系统，此选项为隐含选项。

**`-b`** 显式使用 512 字节块，覆盖环境中的任何 `BLOCKSIZE` 设置。这与 `-P` 选项相同。`-k` 选项会覆盖此选项。

**`-c`** 显示总计。

**`-g`** 使用 1073741824 字节（1 Gibibyte）块而非默认值。这会覆盖环境中的任何 `BLOCKSIZE` 设置。

**`-h`** “Human-readable”输出。使用单位后缀：Byte、Kibibyte、Mebibyte、Gibibyte、Tebibyte 和 Pebibyte（基于 1024 的幂），以将数字位数减少到四位或更少。

**`-H`**, **`--si`** 与 `-h` 相同，但基于 1000 的幂。

**`-i`** 包含可用和已用 inode 数量的统计信息。与 `-h` 或 `-H` 选项结合使用时，inode 数量按 1000 的幂进行缩放。如果文件系统没有 inode，则显示 “-” 而非使用百分比。

**`-k`** 使用 1024 字节（1 Kibibyte）块而非默认值。这会覆盖 `-P` 选项和环境中的任何 `BLOCKSIZE` 设置。

**`-l`** 仅选择本地挂载的文件系统进行显示。如果与 `-t` `type` 选项结合使用，文件系统类型将根据该选项的参数进行添加或排除。

**`-m`** 使用 1048576 字节（1 Mebibyte）块而非默认值。这会覆盖环境中的任何 `BLOCKSIZE` 设置。

**`-n`** 打印先前从文件系统获取的统计信息。如果某些文件系统可能处于无法在不长时间延迟的情况下提供统计信息的状态，应使用此选项。指定此选项时，`df` 不会向文件系统请求新的统计信息，而是返回先前获取的可能已过期的统计信息。

**`-P`** 显式使用 512 字节块，覆盖环境中的任何 `BLOCKSIZE` 设置。这与 `-b` 选项相同。`-k` 选项会覆盖此选项。

**`-t`** `type` 选择要显示的文件系统。可在以逗号分隔的列表中指定多种类型。文件系统类型列表可以加 “no” 前缀，以指定*不*应对其执行操作的文件系统类型。如果与 `-l` 选项结合使用，此选项的参数将修改由 `-l` 选项选择的本地挂载文件系统列表。例如，`df` 命令：

```sh
df -t nonfs,nullfs
```

列出除 NFS 和 NULLFS 类型之外的所有文件系统。可使用 [lsvfs(1)](lsvfs.1.md) 命令查找系统上可用的文件系统类型。

**`-T`** 包含文件系统类型。

**`,`**（逗号）使用 localeconv(3) 返回的非货币分隔符（通常为逗号或句点）按千位分组并分隔打印大小。如果未设置 locale，或 locale 没有非货币分隔符，此选项无效。

## 环境变量

**`BLOCKSIZE`** 指定报告块计数的单位。此选项使用 getbsize(3)，允许使用字节单位或以字母 *k*（1024 字节的倍数）、*m*（1048576 字节的倍数）或 *g*（gibibyte）缩放的数字。允许范围为 512 字节到 1 GB。如果值超出范围，将被设置为相应的限制值。

## 实例

显示所有挂载点（包括文件系统类型）的易读可用磁盘空间：

```sh
$ df -ahT
Filesystem   Type        Size    Used   Avail Capacity  Mounted on
/dev/ada1p2  ufs         213G    152G     44G    78%    /
devfs        devfs       1.0K    1.0K      0B   100%    /dev
/dev/ada0p1  ufs         1.8T    168G    1.5T    10%    /data
linsysfs     linsysfs    4.0K    4.0K      0B   100%    /compat/linux/sys
/dev/da0     msdosfs     7.6G    424M    7.2G     5%    /mnt/usb
```

显示先前收集的数据，包括除 devfs 和 linsysfs 文件系统外的 inode 统计信息。注意，“no” 前缀影响列表中的所有文件系统，且 `-t` 选项只能指定一次：

```sh
$ df -i -n -t nodevfs,linsysfs
Filesystem   1K-blocks      Used      Avail Capacity iused     ifree %iused
Mounted on
/dev/ada1p2  223235736 159618992   45757888    78% 1657590  27234568    6%   /
/dev/ada0p1 1892163184 176319420 1564470712    10% 1319710 243300576    1%
/data
/dev/da0       7989888    433664    7556224     5%       0         0  100%
/mnt/usb
```

显示包含文件 **/etc/rc.conf** 的文件系统的易读信息：

```sh
$ df -h /etc/rc.conf
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/ada1p2    213G    152G     44G    78%    /
```

与上相同，但指定某个文件系统：

```sh
$ df -h /dev/ada1p2
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/ada1p2    213G    152G     44G    78%    /
```

## 注释

对于非 Unix 文件系统，已用和可用 inode 的报告值可能与已用和可用文件及目录的含义不同。以 msdosfs 为例，在 FAT12 或 FAT16 文件系统的情况下，它报告的是可用和空闲的根目录条目数而非 inode（其中每个文件或目录名或磁盘标签需要 1 到 21 个此类目录条目来存储）。

## 参见

[lsvfs(1)](lsvfs.1.md), [quota(1)](quota.1.md), fstatfs(2), [getfsstat(2)](../sys/getfsstat.2.md), [statfs(2)](../sys/statfs.2.md), [getbsize(3)](../gen/getbsize.3.md), [getmntinfo(3)](../gen/getmntinfo.3.md), [libxo(3)](../man3/libxo.3.md), [localeconv(3)](../locale/localeconv.3.md), [xo_options(7)](../man7/xo_options.7.md), [fstab(5)](../man5/fstab.5.md), [mount(8)](../man8/mount.8.md), pstat(8), [quot(8)](../man8/quot.8.md), swapinfo(8)

## 标准

除大多数选项外，`df` 实用程序符合 IEEE Std 1003.1-2004 ("POSIX.1")，该规范仅定义了 `-k`、`-P` 和 `-t` 选项。

## 历史

`df` 命令首次出现于 Version 1 AT&T UNIX。

## 缺陷

如果指定了文件或文件系统，`-n` 标志将被忽略。此外，如果用户无法访问某个挂载点，文件系统信息可能已过期。

`-b` 和 `-P` 选项是相同的。前者源自 BSD 传统，后者是为符合 IEEE Std 1003.1-2004 ("POSIX.1") 规范而要求。
