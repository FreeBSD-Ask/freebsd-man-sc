# diff.1

`diff` — 文件和目录差异比较器

## 名称

`diff`

## 概要

`diff [-aBbdipTtw] [-c | -e | -f | -n | -q | -u | -y] [-A algo | --algorithm algo] [--brief] [--color=when] [--changed-group-format GFMT] [--ed] [--expand-tabs] [--forward-ed] [--ignore-all-space] [--ignore-case] [--ignore-space-change] [--initial-tab] [--minimal] [--no-dereference] [--no-ignore-file-name-case] [--normal] [--rcs] [--show-c-function] [--starting-file] [--speed-large-files] [--strip-trailing-cr] [--tabsize number] [--text] [--unified] [-I pattern | --ignore-matching-lines pattern] [-F pattern | --show-function-line pattern] [-L label | --label label] file1 file2`

`diff [-aBbdilpTtw] [-A algo | --algorithm algo] [-I pattern | --ignore-matching-lines pattern] [-F pattern | --show-function-line pattern] [-L label | --label label] [--brief] [--color=when] [--changed-group-format GFMT] [--ed] [--expand-tabs] [--forward-ed] [--ignore-all-space] [--ignore-case] [--ignore-space-change] [--initial-tab] [--minimal] [--no-dereference] [--no-ignore-file-name-case] [--normal] [--paginate] [--rcs] [--show-c-function] [--speed-large-files] [--starting-file] [--strip-trailing-cr] [--tabsize number] [--text] -C number | --context number file1 file2`

`diff [-aBbdiltw] [-A algo | --algorithm algo] [-I pattern | --ignore-matching-lines pattern] [--brief] [--color=when] [--changed-group-format GFMT] [--ed] [--expand-tabs] [--forward-ed] [--ignore-all-space] [--ignore-case] [--ignore-space-change] [--initial-tab] [--minimal] [--no-dereference] [--no-ignore-file-name-case] [--normal] [--paginate] [--rcs] [--show-c-function] [--speed-large-files] [--starting-file] [--strip-trailing-cr] [--tabsize number] [--text] -D string | --ifdef string file1 file2`

`diff [-aBbdilpTtw] [-A algo | --algorithm algo] [-I pattern | --ignore-matching-lines pattern] [-F pattern | --show-function-line pattern] [-L label | --label label] [--brief] [--color=when] [--changed-group-format GFMT] [--ed] [--expand-tabs] [--forward-ed] [--ignore-all-space] [--ignore-case] [--ignore-space-change] [--initial-tab] [--minimal] [--no-dereference] [--no-ignore-file-name-case] [--normal] [--paginate] [--rcs] [--show-c-function] [--speed-large-files] [--starting-file] [--strip-trailing-cr] [--tabsize number] [--text] -U number | --unified number file1 file2`

`diff [-aBbdilNPprsTtw] [-c | -e | -f | -n | -q | -u] [-A algo | --algorithm algo] [--brief] [--color=when] [--changed-group-format GFMT] [--context] [--ed] [--expand-tabs] [--forward-ed] [--ignore-all-space] [--ignore-case] [--ignore-space-change] [--initial-tab] [--minimal] [--new-file] [--no-dereference] [--no-ignore-file-name-case] [--normal] [--paginate] [--rcs] [--recursive] [--report-identical-files] [--show-c-function] [--speed-large-files] [--starting-file] [--strip-trailing-cr] [--tabsize number] [--text] [--unidirectional-new-file] [--unified] [-I pattern | --ignore-matching-lines pattern] [-F pattern | --show-function-line pattern] [-L label | --label label] [-S name | --starting-file name] [-X file | --exclude-from file] [-x pattern | --exclude pattern] dir1 dir2`

`diff [-aBbditwW] [--color=when] [--expand-tabs] [--ignore-all-space] [--ignore-blank-lines] [--ignore-case] [--minimal] [--no-dereference] [--no-ignore-file-name-case] [--strip-trailing-cr] [--suppress-common-lines] [--tabsize number] [--text] [--width] -y | --side-by-side file1 file2`

`diff [--help] [--version]`

## 描述

`diff` 实用程序比较 `file1` 和 `file2` 的内容，并将将一个文件转换为另一个文件所需的更改列表写入标准输出。如果文件相同，则不产生输出。

输出选项（互斥）：

**`-C`** `number` **`--context`** `number` 类似于 `-c`，但生成包含 `number` 行上下文的 diff。

**`-c`** 生成包含 3 行上下文的 diff。使用 `-c` 时，输出格式略有修改：输出以涉及文件的标识及其创建日期开始，然后每个更改由一行十五个 `*` 分隔。从 `file1` 中删除的行以“`-`”标记；添加到 `file2` 的行以“`+`”标记。在两个文件之间更改的行在两个文件中都以“`!`”标记。彼此相距 3 行以内的更改在输出中分组在一起。

**`-D`** `string` **`--ifdef`** `string` 在标准输出上创建 `file1` 和 `file2` 的合并版本，其中包含 C 预处理器控制，使得在未定义 `string` 时编译结果等同于编译 `file1`，而定义 `string` 将产生 `file2`。

**`-e`** **`--ed`** 生成适合作为编辑器实用程序 ed(1) 输入的形式，随后可用 ed(1) 将 file1 转换为 file2。使用 `-e` 比较目录时，输出中会添加额外的命令，使结果成为一个 [sh(1)](sh.1.md) 脚本，用于将两个目录中共同的文本文件从其在 `dir1` 中的状态转换到其在 `dir2` 中的状态。请注意，使用 `-e` 比较目录时，生成的文件可能不再被解释为 ed(1) 脚本。会添加输出以指示每组 ed(1) 命令应用于哪个文件。可以手动提取这些块来生成 ed(1) 脚本，也可以用 patch(1) 应用。

**`-f`** **`--forward-ed`** 输出与 `-e` 标志相同，但顺序相反。ed(1) 无法处理它。

**`--help`** 此选项向 stdout 打印摘要并以状态 0 退出。

**`-n`** 生成类似于 `-e` 的脚本，但顺序相反，并在每个插入或删除命令上附带更改行数的计数。这是 rcsdiff 使用的形式。

**`-q`** **`--brief`** 仅在文件不同时打印一行。不输出更改列表。

**`-U`** `number` **`--unified`** `number` 类似于 `-u`，但生成包含 `number` 行上下文的 diff。

**`-u`** 生成包含 3 行上下文的*统一* diff。统一 diff 类似于 `-c` 选项生成的上下文 diff。然而，与 `-c` 不同的是，所有要更改的行（添加和/或删除）都出现在单个部分中。

**`--version`** 此选项向 stdout 打印版本字符串并以状态 0 退出。

**`-y`** **`--side-by-side`** 以两列输出，中间带有标记。标记可以是以下之一：

**（空格）** 对应行相同。

**`'|'`** 对应行不同。

**`'<'`** 文件不同，且只有第一个文件包含该行。

**`'>'`** 文件不同，且只有第二个文件包含该行。

比较选项：

**`-A`** `algo`, **`--algorithm`** `algo` 配置比较文件时使用的算法。`diff` 支持 3 种算法：

**`myers`** Myers diff 算法找到一个输入转换为另一个的最短编辑。它通常在 O(N+D²) 时间内运行，需要 O(N) 空间，其中 N 是输入长度之和，D 是它们之间差异的长度，理论最坏情况为 O(N·D)。如果遇到最坏情况输入，`diff` 使用的实现会回退到一种次优但更快的算法。

**`patience`** Myers 算法的 Patience 变体尝试通过逻辑分组行来创建更美观的 diff 输出。

**`stone`** Stone 算法（通常称为 Hunt-McIlroy 或 Hunt-Szymanski）查找比较文件之间的最长公共子序列。当存在长公共子序列时，Stone 会遇到最坏情况性能。在大文件中，这可能导致显著的性能影响。保留 Stone 算法是为了兼容性。

`diff` 实用程序默认使用 Myers 算法，但如果输入或输出选项不被 Myers 实现支持，则回退到 Stone 算法。

**`-a`** **`--text`** 将所有文件视为 ASCII 文本。通常，如果文件包含二进制字符，`diff` 会直接打印“Binary files ... differ”。使用此选项强制 `diff` 生成 diff。

**`-B`** **`--ignore-blank-lines`** 使仅包含空行的块被忽略。

**`-b`** **`--ignore-space-change`** 使尾随空白（空格和制表符）被忽略，其他空白字符串比较相等。

**`--color=`**[`when`] 为添加着绿色，删除着红色，或使用 `DIFFCOLORS` 环境变量中的值。`when` 的可能值为“`never`”、“`always`”和“`auto`”。如果输出是 tty 且 `COLORTERM` 环境变量设置为非空字符串，`auto` 将使用颜色。

**`-d`** **`--minimal`** 尽力生成尽可能小的 diff。在处理具有许多更改的大文件时，这可能会消耗大量处理能力和内存。

**`-F`** `pattern`, **`--show-function-line`** `pattern` 类似于 `-p`，但显示与提供的模式匹配的最后一行。

**`-I`** `pattern` **`--ignore-matching-lines`** `pattern` 忽略其行匹配扩展正则表达式 `pattern` 的更改、插入和删除。可以指定多个 `-I` 模式。更改中的所有行都必须匹配某个模式，该更改才会被忽略。有关正则表达式模式的更多信息，请参见 re_format(7)。

**`-i`** **`--ignore-case`** 忽略字母大小写。例如，“A”与“a”比较相等。

**`-l`** **`--paginate`** 将输出通过 pr(1) 进行分页。

**`-L`** `label` **`--label`** `label` 在上下文或统一 diff 头中打印 `label` 而不是第一个（如果此选项指定两次，则还有第二个）文件名和时间。

**`-p`** **`--show-c-function`** 对于统一和上下文 diff，在每次更改时显示上下文之前最后一行中以字母、下划线或美元符号开头的前 40 个字符。对于遵循标准布局约定的 C 和 Objective-C 源代码，这将显示更改所适用的函数原型。

**`-T`** **`--initial-tab`** 对于正常、上下文或统一输出格式，在行的其余部分之前打印制表符而不是空格。这使得行中制表符的对齐一致。

**`-t`** **`--expand-tabs`** 在输出行中展开制表符。正常或 `-c` 输出会在每行前面添加字符，这可能会打乱原始源行的缩进，使输出列表难以解释。此选项将保留原始源的缩进。

**`-w`** **`--ignore-all-space`** 类似于 `-b` **`--ignore-space-change`**，但使空白（空格和制表符）被完全忽略。例如，“if ( a == b )”与“if(a==b)”比较相等。

**`-W`** `number` **`--width`** `number` 使用并排格式时最多输出 `number` 列。默认值为 130。请注意，除非指定了 `-t`，`diff` 始终将第二列对齐到制表位，因此小于 `--tabsize` 值约五倍的 `--width` 值可能产生意外结果。

**`--changed-group-format`** `GFMT` 以提供的格式格式化输入组。该格式是带有特殊关键字的字符串：

**`%<`** 来自 FILE1 的行

**`%<`** 来自 FILE2 的行

**`--ignore-file-name-case`** 比较文件名时忽略大小写。

**`--no-dereference`** 不跟随符号链接。

**`--no-ignore-file-name-case`** 比较文件名时不忽略大小写（默认）。

**`--normal`** 默认 diff 输出。

**`--speed-large-files`** 用于与 GNU diff 兼容的存根选项。

**`--strip-trailing-cr`** 在输入文件上剥离回车符。

**`--suppress-common-lines`** 使用并排格式时不输出公共行。

**`--tabsize`** `number` 表示制表符的空格数（默认 8）。

目录比较选项：

**`-N`** **`--new-file`** 如果一个文件仅在一个目录中找到，则视为在另一个目录中也找到但大小为零。

**`-P`** **`--unidirectional-new-file`** 如果一个文件仅在 `dir2` 中找到，则视为在 `dir1` 中也找到但大小为零。

**`-r`** **`--recursive`** 使 `diff` 递归地应用于遇到的公共子目录。

**`-S`** `name` **`--starting-file`** `name` 从文件 `name` 开始重新启动目录 `diff`。

**`-s`** **`--report-identical-files`** 使 `diff` 报告相同的文件，否则不会提及它们。

**`-X`** `file` **`--exclude-from`** `file` 从比较中排除其 basename 匹配 `file` 中行的文件和子目录。可以指定多个 `-X` 选项。

**`-x`** `pattern` **`--exclude`** `pattern` 从比较中排除其 basename 匹配 `pattern` 的文件和子目录。模式通过 fnmatch(3) 使用 shell 风格的通配匹配。可以指定多个 `-x` 选项。

如果两个参数都是目录，`diff` 按名称对目录内容进行排序，然后对不同的文本文件运行常规文件 `diff` 算法，生成更改列表。不同的二进制文件、公共子目录以及仅出现在一个目录中的文件会照此描述。在目录模式下，仅比较常规文件和目录。如果遇到非常规文件（如设备特殊文件或 FIFO），则打印诊断消息。

如果 `file1` 和 `file2` 中只有一个是目录，`diff` 应用于非目录文件和目录文件中包含的文件，该文件的文件名与非目录文件的最后一个组件相同。

如果 `file1` 或 `file2` 为“`-`”，则在其位置使用标准输入。

### 输出风格

默认输出（不使用 `-e`、`-c` 或 `-n` **`--rcs`** 选项）包含以下形式的行，其中 `XX`、`YY`、`ZZ`、`QQ` 是按文件顺序的行号。

**`XX`**`a``YY` 在 `file1` 的第 `XX` 行（末尾）追加 `file2` 第 `YY` 行的内容使它们相等。

**`XX`**`a``YY,ZZ` 同上，但追加 `file2` 中从 `YY` 到 `ZZ` 的行范围到 file1 的第 `XX` 行。

**`XX`**`d``YY` 在第 `XX` 行删除该行。`YY` 值指示该更改会使 `file1` 与 `file2` 在哪一行对齐。

**`XX,YY`**`d``ZZ` 删除 `file1` 中从 `XX` 到 `YY` 的行范围。

**`XX`**`c``YY` 将 `file1` 中的第 `XX` 行更改为 `file2` 中的第 `YY` 行。

**`XX,YY`**`c``ZZ` 用第 `ZZ` 行替换指定的行范围。

**`XX,YY`**`c``ZZ,QQ` 用 `file2` 中的 `ZZ`、`QQ` 范围替换 `file1` 中的 `XX`、`YY` 范围。

这些行类似于将 `file1` 转换为 `file2` 的 ed(1) 子命令。动作字母之前的行号属于 `file1`；之后的行号属于 `file2`。因此，通过将 `a` 与 `d` 交换并以相反顺序读取行，也可以确定如何将 `file2` 转换为 `file1`。如同在 ed(1) 中，相同的对（num1 = num2）缩写为单个数字。

## 环境变量

**`DIFFCOLORS`** 此变量的值形式为 `add`:`rm`，其中 `add` 是用于添加的 ASCII 转义序列，`rm` 是用于删除的 ASCII 转义序列。如果未设置，`diff` 使用绿色表示添加，红色表示删除。

## 文件

**/tmp/diff.XXXXXXXX** 比较设备或标准输入时使用的临时文件。请注意，临时文件在创建后立即被取消链接，因此它不会出现在目录列表中。

## 退出状态

`diff` 实用程序以以下值之一退出：

**0** 未发现差异。

**1** 发现差异。

**>1** 发生错误。

`--help` 和 `--version` 选项以状态 0 退出。

## 实例

递归比较 `old_dir` 和 `new_dir`，生成统一 diff，并将仅在一个目录中找到的文件视为新文件：

```sh
$ diff -ruN /path/to/old_dir /path/to/new_dir
```

与上例相同，但排除匹配表达式“*.h”和“*.c”的文件：

```sh
$ diff -ruN -x '*.h' -x '*.c' /path/to/old_dir /path/to/new_dir
```

显示一行指示文件是否不同：

```sh
$ diff -q /boot/loader.conf /boot/defaults/loader.conf
Files /boot/loader.conf and /boot/defaults/loader.conf differ
```

假设有一个名为 `example.txt` 的文件，内容如下：

```sh
FreeBSD is an operating system
Linux is a kernel
OpenBSD is an operating system
```

将标准输入与 `example.txt` 比较，从比较中排除包含“Linux”或“Open”的行：

```sh
$ echo "FreeBSD is an operating system" | diff -q -I 'Linux|Open' example.txt -
```

## 参见

[cmp(1)](cmp.1.md), [comm(1)](comm.1.md), [diff3(1)](diff3.1.md), ed(1), patch(1), pr(1), [sdiff(1)](sdiff.1.md)

> James W. Hunt, M. Douglas McIlroy, "An Algorithm for Differential File Comparison", *Computing Science Technical Report*, 1976 年 6 月。

## 标准

`diff` 实用程序符合 IEEE Std 1003.1-2008 ("POSIX.1") 规范。

标志 [`-AaDdIiLlNnPpqSsTtwXxy`] 是对该规范的扩展。

## 历史

`diff` 命令出现于 Version 6 AT&T UNIX。FreeBSD 中使用的 `diff` 实现直到 FreeBSD 11.4 都是 GNU diff。这在 FreeBSD 12.0 中被 Todd Miller 编写的 BSD 许可实现所取代。在此过程中失去了一些 GNU 特性。

libdiff 从 Game of Trees 版本控制系统导入，默认算法在 FreeBSD 15 中更改为 Myers。
