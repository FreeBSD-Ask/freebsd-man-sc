# bsdcat(1)

`bsdcat` — 将文件展开到标准输出

## 名称

`bsdcat`

## 概要

`bsdcat [options] [files]`

## 描述

`bsdcat` 将文件展开到标准输出。

## 选项

`bsdcat` 通常以文件名作为参数，或在管道中使用时读取标准输入。两种情况下，解压后的数据都会写入标准输出。

## 实例

解压文件：

```sh
bsdcat example.txt.gz > example.txt
```

在管道中解压标准输入：

```sh
cat example.txt.gz | bsdcat > example.txt
```

两条命令效果相同——通过重定向输出得到解压后的文件。

## 参见

bzcat(1), uncompress(1), [xzcat(1)](xz.1.md), [zcat(1)](gzip.1.md), libarchive-formats(5)
