# cmp(1)

`cmp` — 比较两个文件

## 名称

`cmp`

## 概要

`cmp [-l | -s | -x] [-bhz] [--ignore-initial=num1[:num2]] [--bytes=num] file1 file2 [skip1 [skip2]]`

## 描述

`cmp` 实用程序比较两个任意类型的文件，并将结果写入标准输出。默认情况下，如果文件相同，`cmp` 不输出任何内容；如果文件不同，则报告第一个差异出现的字节和行号。

字节和行号从 1 开始计数。

以下选项可用：

**`-b`**, **`--print-bytes`** 发现差异时打印每个字节。

**`-h`** 不跟随符号链接。

**`-i`** `num1[:num2]`, **`--ignore-initial=num1[:num2]`** 跳过 `file1` 的 `num1` 个字节，可选地跳过 `file2` 的 `num2` 个字节。如果未指定 `num2`，则 `num1` 同时应用于 `file1` 和 `file2`。

**`-l`**, **`--verbose`** 对每个差异打印字节号（十进制）和差异字节值（八进制）。

**`-n`** `num`, **`--bytes=num`** 仅比较最多 `num` 个字节。

**`-s`**, **`--silent`**, **`--quiet`** 对有差异的文件不打印任何内容；仅返回退出状态。

**`-x`** 类似于 `-l`，但以十六进制打印，并使用零作为文件中第一个字节的索引。

**`-z`** 对于常规文件，先比较文件大小，如果大小不等则比较失败。

可选参数 `skip1` 和 `skip2` 分别是 `file1` 和 `file2` 从开头起的字节偏移量，比较将从该处开始。偏移量默认为十进制，但可以通过前缀“`0x`”或“`0`”表示为十六进制或八进制值。

`skip1` 和 `skip2` 还可以使用 SI 大小后缀指定。

## 退出状态

`cmp` 实用程序以以下值之一退出：

**0** 文件相同。

**1** 文件不同；这包括一个文件与另一个文件的第一部分相同的情况。在后一种情况下，如果未指定 `-s` 选项，`cmp` 会向标准错误写入在较短的文件中已到达 EOF（在任何差异被发现之前）。

**>1** 发生错误。

## 实例

假设有一个名为 `example.txt` 的文件，内容如下：

```sh
a
b
c
```

将标准输入与 `example.txt` 比较：

```sh
$ echo -e "a\nb\nc" | cmp - example.txt
```

与上例相同，但在标准输入的第三个字节处引入一个更改。显示字节号（十进制）和差异字节（八进制）：

```sh
$ echo -e "a\nR\nc" | cmp -l - example.txt
     3 122 142
```

比较 `example.txt` 和 **/boot/loader.conf** 的文件大小，如果大小不等则返回 1。注意 `-z` 仅可用于常规文件：

```sh
$ cmp -z example.txt /boot/loader.conf
example.txt /boot/loader.conf differ: size
```

将标准输入与 `example.txt` 比较，省略标准输入的前 4 个字节和 `example.txt` 的前 2 个字节：

```sh
$ echo -e "a\nR\nb\nc" | cmp - example.txt 4 2
```

## 参见

[diff(1)](diff.1.md), [diff3(1)](diff3.1.md)

## 标准

`cmp` 实用程序预期与 IEEE Std 1003.2 ("POSIX.2") 兼容。`-b`、`-h`、`-i`、`-n`、`-x` 和 `-z` 选项是对标准的扩展。`skip1` 和 `skip2` 参数是对标准的扩展。

## 历史

`cmp` 命令首次出现于 Version 1 AT&T UNIX。

## 缺陷

上文中提到的“SI 大小后缀”指的是传统的二次幂约定，如 expand_number(3) 中所述。
