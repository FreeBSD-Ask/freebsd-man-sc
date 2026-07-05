# zdiff.1

`zcmp` — 比较压缩文件

## 名称

`zcmp`, `zdiff`

## 概要

`zcmp [options] file [file2]`

`zdiff [options] file [file2]`

## 描述

`zcmp` 和 `zdiff` 是过滤器，分别调用 [cmp(1)](cmp.1.md) 或 [diff(1)](diff.1.md) 来比较压缩文件。指定的任何 `options` 都会传递给 [cmp(1)](cmp.1.md) 或 [diff(1)](diff.1.md)。

如果只指定了 `file1`，则将其与同名但去除扩展名的文件进行比较。当同时指定了 `file1` 和 `file2` 时，任一文件都可以是压缩文件。

[gzip(1)](gzip.1.md) 处理的扩展名：

- z, Z,
- gz,
- taz,
- tgz.

bzip2(1) 处理的扩展名：

- bz,
- bz2,
- tbz,
- tbz2.

[xz(1)](xz.1.md) 处理的扩展名：

- lzma,
- xz,
- tlz,
- txz.

## 环境变量

**`TMPDIR`** 用于放置临时文件的目录。如果未设置，则使用 **/tmp**。

## 文件

**`/tmp/zcmp.XXXXXXXXXX`** `zcmp` 使用的临时文件。

**`/tmp/zdiff.XXXXXXXXXX`** `zdiff` 使用的临时文件。

## 参见

bzip2(1), [cmp(1)](cmp.1.md), [diff(1)](diff.1.md), [gzip(1)](gzip.1.md), [xz(1)](xz.1.md)

## 注意事项

`zcmp` 和 `zdiff` 完全依赖文件扩展名来判断一个文件是否为压缩文件。因此，以下内容不能作为参数：

- 目录
- 设备特殊文件
- 表示标准输入的文件名（"-"）
