# split.1

`split` — 将文件分割成多片

## 名称

`split`

## 概要

`split [-cd] [-l line_count] [-a suffix_length] [file [prefix]]`

`split [-cd] -b byte_count[K|k|M|m|G|g] [-a suffix_length] [file [prefix]]`

`split [-cd] -n chunk_count [-a suffix_length] [file [prefix]]`

`split [-cd] -p pattern [-a suffix_length] [file [prefix]]`

## 描述

`split` 工具读取指定的 `file` 并将其拆分为每个 1000 行的文件（若未指定选项），原 `file` 保持不变。如果 `file` 是单个短划线（“`-`”）或未提供，`split` 从标准输入读取。

选项如下：

**`-a`** `suffix_length` 使用 `suffix_length` 个字母组成文件名后缀。

**`-b`** `byte_count`[`K`|`k`|`M`|`m`|`G`|`g`] 创建长度为 `byte_count` 字节的拆分文件。如果数字后追加 `k` 或 `K`，文件按 `byte_count` 千字节拆分。如果追加 `m` 或 `M`，文件按 `byte_count` 兆字节拆分。如果追加 `g` 或 `G`，文件按 `byte_count` 吉字节拆分。

**`-c`** 继续创建文件，不覆盖已有的输出文件。

**`-d`** 使用数字后缀替代字母后缀。

**`-l`** `line_count` 创建长度为 `line_count` 行的拆分文件。

**`-n`** `chunk_count` 将文件拆分为 `chunk_count` 个较小的文件。前 n-1 个文件的大小为（`file` 的大小 / `chunk_count`），最后一个文件包含剩余的字节。

**`-p`** `pattern` 每当输入行匹配 `pattern` 时拆分文件，`pattern` 被解释为扩展正则表达式。匹配的行将作为下一个输出文件的第一行。此选项与 `-b` 和 `-l` 选项不兼容。

如果指定了额外参数，第一个参数作为待拆分输入文件的名称。如果指定了第二个额外参数，它作为文件拆分后所得文件名的前缀。此时，每个拆分后的文件以前缀加按词典序排列的后缀命名，后缀使用 `suffix_length` 个字符，范围从“`a`”到“`z`”。如果未指定 `-a`，初始后缀使用两个字母。如果输出无法容纳在所得文件数中且未指定 `-d` 标志，则后缀长度会按需自动扩展，使所有输出文件继续按词典序排序。

如果未指定 `prefix` 参数，文件拆分为以前缀“`x`”命名并带上述后缀的按词典序排列的文件。

默认情况下，`split` 会覆盖任何已有的输出文件。如果指定了 `-c` 标志，`split` 将改为创建尚未存在的名称的文件。

## 环境变量

`LANG`、`LC_ALL`、`LC_CTYPE` 和 `LC_COLLATE` 环境变量按 [environ(7)](../man7/environ.7.md) 中所述影响 `split` 的执行。

## 退出状态

`split` 工具成功时退出值为 0，发生错误时大于 0。

## 实例

将输入拆分为所需数量的文件，使每个文件最多包含 2 行：

```sh
$ echo -e "first line\nsecond line\nthird line\nforth line" | split -l2
```

使用数字前缀作为文件名，将输入按 10 字节分块。这会生成两个 10 字节的文件（x00 和 x01）以及包含剩余 2 字节的第三个文件（x02）：

```sh
$ echo -e "This is 22 bytes long" | split -d -b10
```

将输入拆分为 6 个文件：

```sh
$ echo -e "This is 22 bytes long" | split -n 6
```

每当行匹配“`t`”后跟“`a`”或“`u`”的正则表达式时创建新文件，从而创建两个文件：

```sh
$ echo -e "stack\nstock\nstuck\nanother line" | split -p 't[au]'
```

## 参见

csplit(1), re_format(7)

## 标准

`split` 工具遵循 IEEE Std 1003.1-2001（“POSIX.1”）规范。

## 历史

`split` 命令首次出现在 Version 3 AT&T UNIX 中。

在 FreeBSD 14 之前，模式和行匹配仅对短于 65,536 字节的行生效。
