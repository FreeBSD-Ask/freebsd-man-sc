# sdiff.1

`sdiff` — 并排显示文件差异

## 名称

`sdiff`

## 概要

`sdiff [-abdilstHW] [-I regexp] [-o outfile] [-w width] file1 file2`

## 描述

`sdiff` 并排显示两个文件，两者之间的任何差异按如下方式高亮显示：新增行以“`>`”标记；删除行以“`<`”标记；更改行以“`|`”标记。

`sdiff` 还可用于交互式合并两个文件，在每组差异处提示用户。详见 `-o` 选项的说明。

选项如下：

**`-l`** **`--left-column`** 对于相同的行，仅打印左列。

**`-o`** **`--output`** `outfile` 将 `file1` 和 `file2` 交互式合并到 `outfile` 中。在此模式下，每组差异都会提示用户。关于调用哪个编辑器（如果有），参见下文的 `EDITOR` 和 `VISUAL`。命令如下：

**`l | 1`** 选择左侧的差异集合。

**`r | 2`** 选择右侧的差异集合。

**`s`** 静默模式——不打印相同的行。

**`v`** 详细模式——打印相同的行。

**`e`** 开始编辑一个空文件，退出编辑器时将其合并到 `outfile`。

**`e`** `l` 开始编辑包含左侧差异集合的文件。

**`e`** `r` 开始编辑包含右侧差异集合的文件。

**`e`** `b` 开始编辑包含两侧差异集合的文件。

**`q`** 退出 `sdiff`。

**`-s`** **`--suppress-common-lines`** 跳过相同的行。

**`-w`** **`--width`** `width` 每行最多打印 `width` 个字符。默认为 130 个字符。

传递给 [diff(1)](diff.1.md) 的选项：

**`-a`** **`--text`** 将 `file1` 和 `file2` 视为文本文件。

**`-b`** **`--ignore-space-change`** 忽略尾随空格。

**`-d`** **`--minimal`** 最小化 diff 大小。

**`-I`** **`--ignore-matching-lines`** `regexp` 忽略匹配 `regexp` 的行更改。更改中的所有行都必须匹配 `regexp` 才能被忽略。

**`-i`** **`--ignore-case`** 进行不区分大小写的比较。

**`-t`** **`--expand-tabs`** 将制表符扩展为空格。

**`-W`** **`--ignore-all-space`** 忽略所有空格。

**`-B`** **`--ignore-blank-lines`** 忽略空行。

**`-E`** **`--ignore-tab-expansion`** 将制表符和八个空格视为相同。

**`-H`** **`--speed-large-files`** 假定大文件中分散着小更改。

**`--ignore-file-name-case`** 忽略文件名的大小写。

**`--no-ignore-file-name-case`** 不忽略文件名的大小写。

**`--strip-trailing-cr`** 跳过相同的行。

**`--tabsize`** `NUM` 更改制表符的大小（默认为 8）。

## 环境变量

**`EDITOR , VISUAL`** 指定与 `-o` 选项一起使用的编辑器。如果同时设置了 `EDITOR` 和 `VISUAL`，`VISUAL` 优先。如果两者都未设置，默认使用 [vi(1)](vi.1.md)。

**`TMPDIR`** 指定创建临时文件的目录。默认为 **/tmp**。

## 参见

[cmp(1)](cmp.1.md), [diff(1)](diff.1.md), [diff3(1)](diff3.1.md), [vi(1)](vi.1.md), re_format(7)

## 作者

`sdiff` 由 Ray Lai <ray@cyth.net> 从头编写，属于公共领域。

## 注意事项

制表符被视为宽度从一到八个字符不等，具体取决于当前列。将制表符视为八个字符宽的终端显示效果最佳。
