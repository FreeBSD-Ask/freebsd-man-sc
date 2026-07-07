# zmore(1)

`zmore` — 查看压缩文件

## 名称

`zmore`, `zless`

## 概要

`zmore [flags] [file]`

`zless [flags] [file]`

## 描述

`zless` 是一个过滤器，允许查看使用 Lempel-Ziv 编码压缩的文件。此类文件通常具有 "Z" 或 "gz" 扩展名（同时支持 compress(1) 和 [gzip(1)](gzip.1.md) 格式）。指定的任何 `flags` 都会传递给用户首选的 `PAGER`（默认为 **/usr/bin/more**）。

`zless` 等同于 `zmore`，但使用 [less(1)](less.1.md) 作为分页器，而非 more(1)。

当指定多个文件时，`zmore` 会在每个文件结束时暂停，并向用户显示以下提示：

```sh
prev_file (END) - Next: next_file
```

其中 **prev_file** 是刚刚显示的文件，**next_file** 是下一个要显示的文件。提示时识别以下按键：

**`e`** 或 `q` 退出 `zmore`。

**`s`** 跳过下一个文件（如果下一个文件是最后一个，则退出）。

如果未指定文件，`zmore` 将从标准输入读取。在此模式下，`zmore` 会假定使用 [gzip(1)](gzip.1.md) 风格的压缩，因为没有可据以判断的后缀。

## 环境变量

**`PAGER`** 用于显示文件的程序。如果未设置，则使用 **/usr/bin/more**（`zmore`）或 **/usr/bin/less**（`zless`）。

## 参见

compress(1), [less(1)](less.1.md), more(1)
