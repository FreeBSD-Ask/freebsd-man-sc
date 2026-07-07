# colrm(1)

`colrm` — 从文件中删除列

## 名称

`colrm`

## 概要

`colrm [start [stop]]`

## 描述

`colrm` 实用程序从文件的行中删除选定的列。列定义为行中的单个字符。输入从标准输入读取，输出写入标准输出。

如果仅指定了 `start` 列，则编号小于 `start` 列的列将被写入。如果同时指定了 `start` 和 `stop` 列，则编号小于 `start` 列或大于 `stop` 列的列将被写入。列编号从 1 开始，而非 0。

制表符将列计数增加到 8 的下一个倍数。退格符将列计数减 1。

## 环境变量

`LANG`、`LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `colrm` 的执行，如 [environ(7)](../man7/environ.7.md) 所述。

## 退出状态

`colrm` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示第 3 列（c）以下和第 5 列（e）以上的列：

```sh
$ echo -e "abcdefgh\n12345678" | colrm 3 5
abfgh
12678
```

指定一个大于文件中列数的起始列是被允许的，此时将显示所有列：

```sh
$ echo "abcdefgh" | colrm 100
abcdefgh
```

使用 1 作为起始列将不显示任何内容：

```sh
$ echo "abcdefgh" | colrm 1
```

## 参见

[awk(1)](awk.1.md), [column(1)](column.1.md), [cut(1)](cut.1.md), [paste(1)](paste.1.md)

## 历史

`colrm` 实用程序首次出现于 1BSD。

## 作者

Jeff Schriebman 于 1974 年 11 月编写了 `colrm` 的原始版本。
