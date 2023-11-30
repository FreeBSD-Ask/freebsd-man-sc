  SDIFF(1)  

SDIFF(1)

FreeBSD General Commands Manual

SDIFF(1)

[名称](#__u540D___u79F0_)
=======================

`sdiff` —

并排差异

[概要](#__u6982___u8981_)
=======================

`sdiff` \[`-abdilstHW`\] \[`-I` regexp\] \[`-o` outfile\] \[`-w` width\] file1 file2

[描述](#__u63CF___u8FF0_)
=======================

`sdiff` 并排显示两个文件，两者之间的任何差异如下突出显示： 新行用 ‘>’ 标记；删除的行用 ‘<’ 标记；并且更改的行用 ‘|’ 标记。

`sdiff` 也可用于交互合并两个文件，在每组差异处进行提示。 有关说明，请参见 `-o` 选项。

选项包括：

[`-l`](#l) `--left-column`

仅打印相同行的左列。

[`-o`](#o) `--output` outfile

以交互方式将 file1 和 file2 合并到 outfile 中。 在这种模式下，提示用户每组差异。 有关调用哪个编辑器（如果有）的详细信息，请参见下面的 `EDITOR` 和 `VISUAL` 。

命令如下：

[`l`](#l_2) | [`1`](#1)

选择左侧的差异集。

[`r`](#r) | [`2`](#2)

选择正确的差异集。

[`s`](#s)

静音模式 – 不打印相同的行。

[`v`](#v)

详细模式 – 打印相同的行。

[`e`](#e)

开始编辑一个空文件，退出编辑器后将合并到 outfile 中。

[`e`](#e_2) `l`

开始编辑具有左侧差异集的文件。

[`e`](#e_3) `r`

使用正确的差异集开始编辑文件。

[`e`](#e_4) `b`

开始使用两组差异编辑文件。

[`q`](#q)

退出 `sdiff` 。

[`-s`](#s_2) `--suppress-common-lines`

跳过相同的行。

[`-w`](#w) `--width` width

每行最多打印 width 字符。 默认值为 130 个字符。

传递给 diff(1) 的选项是：

[`-a`](#a) `--text`

将 file1 和 file2 视为文本文件。

[`-b`](#b) `--ignore-space-change`

忽略尾随空格。

[`-d`](#d) `--minimal`

最小化差异大小。

[`-I`](#I) `--ignore-matching-lines` regexp

忽略匹配 regexp 的行更改。 更改中的所有行都必须匹配 regexp 才能忽略更改。

[`-i`](#i) `--ignore-case`

进行不区分大小写的比较。

[`-t`](#t) `--expand-tabs`

将制表符扩展到空格。

[`-W`](#W) `--ignore-all-space`

忽略所有空格。

[`-B`](#B) `--ignore-blank-lines`

忽略空行。

[`-E`](#E) `--ignore-tab-expansion`

将制表符和八个空格视为相同。

[`-t`](#t_2) `--ignore-tabs`

忽略制表符。

[`-H`](#H) `--speed-large-files`

假设一个大文件中分散的小改动。

[`--ignore-file-name-case`](#-ignore-file-name-case)

忽略文件名的大小写。

[`--no-ignore-file-name-case`](#-no-ignore-file-name-case)

不要忽略文件名大小写。

[`--strip-trailing-cr`](#-strip-trailing-cr)

跳过相同的行。

[`--tabsize`](#-tabsize) NUM

更改制表符的大小（默认为 8。）

[环境](#__u73AF___u5883_)
=======================

[`EDITOR`](#EDITOR), `VISUAL`

指定与 `-o` 选项一起使用的编辑器。 如果同时设置了 `EDITOR` 和 `VISUAL` ，则 `VISUAL` 优先。 如果 `EDITOR` 和 `VISUAL` 均未设置，则默认值为 vi(1) 。

[`TMPDIR`](#TMPDIR)

指定要创建的临时文件的目录。 默认为 /tmp 。

[参见](#__u53C2___u89C1_)
=======================

cmp(1), diff(1), diff3(1), vi(1), re\_format(7)

[作者](#__u4F5C___u8005_)
=======================

`sdiff` 由 Ray Lai ⟨ray@cyth.net⟩ 从头开始为公共领域编写。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

制表符被视为 1 到 8 个字符宽，具体取决于当前列。 将制表符视为八个字符宽的终端看起来最好。

April 8, 2017

FreeBSD 13.1-RELEASE