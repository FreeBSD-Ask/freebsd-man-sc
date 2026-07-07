# uniq(1)

`uniq` — 报告或过滤文件中重复的行

## 名称

`uniq` — 报告或过滤文件中重复的行

## 概要

`uniq [-cdiu] [-D[septype]] [-f num] [-s chars] [input_file [output_file]]`

## 描述

`uniq` 实用程序读取指定的 `input_file`，比较相邻的行，并将每个唯一输入行的副本写入 `output_file`。如果 `input_file` 是单个短划线（‘`-`’）或未指定，则读取标准输入。如果 `output_file` 未指定，则使用标准输出作为输出。相同的相邻输入行的第二份及后续副本不会被写入。如果输入中的重复行不相邻，则不会被检测到，因此可能需要先对文件排序。

可用选项如下：

**`-c`**, **`--count`** 在每行输出前加上该行在输入中出现次数的计数，后跟一个空格。

**`-d`**, **`--repeated`** 输出输入中重复的每行的一个副本。如果同时指定了 `-D`，则忽略此选项。

**`-D`**, **`--all-repeated`** [`septype`] 输出所有重复的行（类似于 `-d`，但重复行的每个副本都会写入）。可选的 `septype` 参数控制如何在输出中分隔重复行组；它必须是以下值之一：

**none** 不分隔行组（这是默认值）。

**prepend** 在每组行之前输出一个空行。

**separate** 在每组行之后输出一个空行。

**`-f`** `num`, **`--skip-fields`** `num` 比较时忽略每个输入行的前 `num` 个字段。字段是由空白字符与相邻字段分隔的非空白字符序列。字段编号从 1 开始，即第一个字段是字段一。

**`-i`**, **`--ignore-case`** 行的比较不区分大小写。

**`-s`** `chars`, **`--skip-chars`** `chars` 比较时忽略每个输入行的前 `chars` 个字符。如果与 `-f`、`--unique` 选项一起指定，则忽略前 `num` 个字段之后的前 `chars` 个字符。字符编号从 1 开始，即第一个字符是字符一。

**`-u`**, **`--unique`** 仅输出在输入中未重复的行。

## 环境变量

`LANG`、`LC_ALL`、`LC_COLLATE` 和 `LC_CTYPE` 环境变量影响 `uniq` 的执行，如 [environ(7)](../man7/environ.7.md) 中所述。

## 退出状态

`uniq` 实用程序成功时以 0 退出，发生错误时以 >0 退出。

## 实例

假设名为 cities.txt 的文件包含以下内容：

```sh
Madrid
Lisbon
Madrid
```

以下命令报告三行不同的内容，因为相同元素不相邻：

```sh
$ uniq -u cities.txt
Madrid
Lisbon
Madrid
```

对文件排序并计算相同行的数量：

```sh
$ sort cities.txt | uniq -c
	1 Lisbon
	2 Madrid
```

假设文件 cities.txt 包含以下内容：

```sh
madrid
Madrid
Lisbon
```

忽略大小写显示重复行：

```sh
$ uniq -d -i cities.txt
madrid
```

与上面相同，但显示整个重复行组：

```sh
$ uniq -D -i cities.txt
madrid
Madrid
```

忽略每行第一个字符报告相同行数：

```sh
$ uniq -s 1 -c cities.txt
	2 madrid
	1 Lisbon
```

## 兼容性

历史上的 `+number` 和 `-number` 选项已弃用，但在此实现中仍受支持。

## 参见

[sort(1)](sort.1.md)

## 标准

`uniq` 实用程序遵循 IEEE Std 1003.1-2001 ("POSIX.1")，经 Cor. 1-2002 修订。

## 历史

`uniq` 命令首次出现于 Version 3 AT&T UNIX。
