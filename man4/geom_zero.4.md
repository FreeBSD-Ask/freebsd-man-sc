# geom_zero.4

`gzero` — 基于 GEOM 的零磁盘/块设备

## 名称

`gzero`, `geom_zero`

## 概要

`options GEOM_ZERO`

`在 loader.conf(5) 或 sysctl.conf(5) 中： kern.geom.zero.byte kern.geom.zero.clear`

## 描述

`geom_zero` 是一个 GEOM(4) 设备，模拟一个一艾字节（exabyte）的磁盘。它丢弃任何写入其中的数据，并为从其中读取的每个字节返回 `kern.geom.zero.byte` 的值。

`geom_zero` 与 [zero(4)](zero.4.md) 不同，后者是常规字符设备且长度无限，而 **/dev/gzero** 是 GEOM(4) 提供程序，大小大但有限。

有关如何使用 GEOM(4) `ZERO` 类支持的命令的说明，请参见 geom(8)。

`ZERO` 适用于对 GEOM 和 GEOM 类进行性能基准测试，前提是数据压缩不影响结果（来自 **/dev/gzero** 的块压缩效果极好）。此类基准测试的示例包括比较两种磁盘加密算法的速度，以及比较单个加密算法的硬件实现与软件实现。

## MIB 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`kern.geom.zero.byte`** 此变量设置 `ZERO` 设备的填充字节。默认值：`0`。

**`kern.geom.zero.clear`** 此变量控制读取数据缓冲区的清除。如果设置为 `0`，`ZERO` 不会将任何数据复制到读取数据缓冲区，而是按原样返回读取数据缓冲区而不作修改。特别地，它不会用 `kern.geom.zero.byte` 的值填充读取缓冲区。这对于读取基准测试非常有用，可以减少由额外内存初始化引起的测量噪声。默认值：`1`。

## 文件

**/dev/gzero** `ZERO` 设备。

## 实例

通过加载 `geom_zero` 内核模块创建 **/dev/gzero** 设备：

```sh
# geom zero load
```

显示 `geom_zero` 设备的信息：

```sh
# geom zero list
Geom name: gzero
Providers:
1. Name: gzero
   Mediasize: 1152921504606846976 (1.0E)
   Sectorsize: 512
   Mode: r0w0egzero0
```

将 `geom_zero` 设备的填充字节设置为 70（[ascii(7)](../man7/ascii.7.md) 中字母“F”的十进制值）

```sh
# sysctl kern.geom.zero.byte=70
kern.geom.zero.byte: 0 -> 70
# head -c 1 /dev/gzero
F
```

对 geli(8) 默认加密算法在 4 KiB 扇区大小下的读写吞吐量进行基准测试：

```sh
# geom zero load
# geli onetime -s 4096 gzero
# sysctl kern.geom.zero.clear=0
# dd if=/dev/gzero.eli of=/dev/zero bs=4k count=$((1024 * 256))
262144+0 records in
262144+0 records out
1073741824 bytes transferred in 1.258195 secs (853398307 bytes/sec)
# dd if=/dev/zero of=/dev/gzero.eli bs=4k count=$((1024 * 256))
262144+0 records in
262144+0 records out
1073741824 bytes transferred in 1.663118 secs (645619658 bytes/sec)
```

## 参见

GEOM(4), [zero(4)](zero.4.md), geom(8), [sysctl(8)](../man8/sysctl.8.md), bio(9)

## 历史

`geom_zero` 设备首次出现于 FreeBSD 6。

## 作者

`geom_zero` 设备由 Paweł Jakub Dawidek <pjd@FreeBSD.org> 编写。

`geom_zero` 手册页最初由 Greg White <gkwhite@gmail.com> 编写，在进入 FreeBSD 之前由 Mateusz Piotrowski <0mp@FreeBSD.org> 重写。
