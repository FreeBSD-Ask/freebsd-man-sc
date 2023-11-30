  DIFF(1)  

DIFF(1)

FreeBSD General Commands Manual

DIFF(1)

[名称](#__u540D___u79F0_)
=======================

`diff` —

差异文件和目录比较器

[概要](#__u6982___u8981_)
=======================

`diff` \[`-aBbdipTtw`\] \[`-c` | `-e` | `-f` | `-n` | `-q` | `-u` | `-y`\] \[`--brief`\] \[`--changed-group-format` GFMT\] \[`--ed`\] \[`--expand-tabs`\] \[`--forward-ed`\] \[`--ignore-all-space`\] \[`--ignore-case`\] \[`--ignore-space-change`\] \[`--initial-tab`\] \[`--minimal`\] \[`--no-ignore-file-name-case`\] \[`--normal`\] \[`--rcs`\] \[`--show-c-function`\] \[`--starting-file`\] \[`--speed-large-files`\] \[`--strip-trailing-cr`\] \[`--tabsize` number\] \[`--text`\] \[`--unified`\] \[`-I` pattern | `--ignore-matching-lines` pattern\] \[`-L` label | `--label` label\] file1 file2 `diff` \[`-aBbdilpTtw`\] \[`-I` pattern | `--ignore-matching-lines` pattern\] \[`-L` label | `--label` label\] \[`--brief`\] \[`--changed-group-format` GFMT\] \[`--ed`\] \[`--expand-tabs`\] \[`--forward-ed`\] \[`--ignore-all-space`\] \[`--ignore-case`\] \[`--ignore-space-change`\] \[`--initial-tab`\] \[`--minimal`\] \[`--no-ignore-file-name-case`\] \[`--normal`\] \[`--paginate`\] \[`--rcs`\] \[`--show-c-function`\] \[`--speed-large-files`\] \[`--starting-file`\] \[`--strip-trailing-cr`\] \[`--tabsize` number\] \[`--text`\] `-C` number | \-context number file1 file2 `diff` \[`-aBbdiltw`\] \[`-I` pattern | `--ignore-matching-lines` pattern\] \[`--brief`\] \[`--changed-group-format` GFMT\] \[`--ed`\] \[`--expand-tabs`\] \[`--forward-ed`\] \[`--ignore-all-space`\] \[`--ignore-case`\] \[`--ignore-space-change`\] \[`--initial-tab`\] \[`--minimal`\] \[`--no-ignore-file-name-case`\] \[`--normal`\] \[`--paginate`\] \[`--rcs`\] \[`--show-c-function`\] \[`--speed-large-files`\] \[`--starting-file`\] \[`--strip-trailing-cr`\] \[`--tabsize` number\] \[`--text`\] `-D` string | `--ifdef` string file1 file2 `diff` \[`-aBbdilpTtw`\] \[`-I` pattern | `--ignore-matching-lines` pattern\] \[`-L` label | `--label` label\] \[`--brief`\] \[`--changed-group-format` GFMT\] \[`--ed`\] \[`--expand-tabs`\] \[`--forward-ed`\] \[`--ignore-all-space`\] \[`--ignore-case`\] \[`--ignore-space-change`\] \[`--initial-tab`\] \[`--minimal`\] \[`--no-ignore-file-name-case`\] \[`--normal`\] \[`--paginate`\] \[`--rcs`\] \[`--show-c-function`\] \[`--speed-large-files`\] \[`--starting-file`\] \[`--strip-trailing-cr`\] \[`--tabsize` number\] \[`--text`\] `-U` number | `--unified` number file1 file2 `diff` \[`-aBbdilNPprsTtw`\] \[`-c` | `-e` | `-f` | `-n` | `-q` | `-u`\] \[`--brief`\] \[`--changed-group-format` GFMT\] \[`--context`\] \[`--ed`\] \[`--expand-tabs`\] \[`--forward-ed`\] \[`--ignore-all-space`\] \[`--ignore-case`\] \[`--ignore-space-change`\] \[`--initial-tab`\] \[`--minimal`\] \[`--new-file`\] \[`--no-ignore-file-name-case`\] \[`--normal`\] \[`--paginate`\] \[`--rcs`\] \[`--recursive`\] \[`--report-identical-files`\] \[`--show-c-function`\] \[`--speed-large-files`\] \[`--strip-trailing-cr`\] \[`--tabsize` number\] \[`--text`\] \[`--unidirectional-new-file`\] \[`--unified`\] \[`-I` pattern | `--ignore-matching-lines` pattern\] \[`-L` label | `--label` label\] \[`-S` name | `--starting-file` name\] \[`-X` file | `--exclude-from` file\] \[`-x` pattern | `--exclude` pattern\] dir1 dir2 `diff` \[`-aBbditwW`\] \[`--expand-tabs`\] \[`--ignore-all-blanks`\] \[`--ignore-blank-lines`\] \[`--ignore-case`\] \[`--minimal`\] \[`--no-ignore-file-name-case`\] \[`--strip-trailing-cr`\] \[`--suppress-common-lines`\] \[`--tabsize` number\] \[`--text`\] \[`--width`\] `-y` | `--side-by-side` file1 file2

[描述](#__u63CF___u8FF0_)
=======================

`diff` 实用程序比较 file1 和 file2 的内容，并将将一个文件转换为另一个文件所需的更改列表写入标准输出。 如果文件相同，则不会产生输出。

输出选项（互斥）：

[`-C`](#C) number `--context` number

与 `-c` 类似，但会产生带有上下文 number 行的差异。

[`-c`](#c)

产生具有 3 行上下文的差异。 使用 `-c` 会稍微修改输出格式：输出以识别所涉及的文件及其创建日期开始，然后每个更改由带有 15 个 `*` 的行分隔。 从 file1 中删除的行标有 ‘- ’; 添加到 file2 的那些标记为 ‘+ ’ 。 从一个文件更改到另一个文件的行在两个文件中都标有 ‘! ’ 。 彼此相距 3 行以内的更改在输出时被组合在一起。

[`-D`](#D) string `--ifdef` string

在标准输出上创建 file1 和 file2 的合并版本，其中包含 C 预处理器控件，以便在不定义 string 的情况下编译结果等同于编译 file1, 而定义 string 将产生 file2 。

[`-e`](#e) `--ed`

以适合作为编辑器实用程序 ed(1) 输入的形式生成输出，然后可以使用该格式将 file1 转换为 file2。

使用 `-e` 比较目录时，会在输出中添加额外的命令，因此结果是一个 sh(1) 脚本，用于将两个目录共有的文本文件从它们在 dir1 中的状态转换为它们在 dir2 中的状态。

[`-f`](#f) `--forward-ed`

与 `-e` 标志的输出相同，但顺序相反。 它不能被 ed(1) 消化。

[`-n`](#n)

生成一个类似于 `-e` 的脚本，但顺序相反，并且在每个插入或删除命令上都有更改的行数。 这是 rcsdiff 使用的形式。

[`-q`](#q) `--brief`

当文件不同时，只需打印一行。 不输出更改列表。

[`-U`](#U) number `--unified` number

与 `-u` 类似，但会产生带有上下文 number 行的差异。

[`-u`](#u)

生成具有 3 行上下文的 _unified_ 差异。 统一差异类似于 `-c` 选项产生的上下文差异。 然而，与 `-c` 不同的是，所有要更改（添加和/或删除）的行都存在于单个部分中。

[`-y`](#y) `--side-by-side`

在两列中输出，它们之间有一个标记。 标记可以是以下之一：

space

对应的行是相同的。

'|'

对应的线路不同。

'<'

文件不同，只有第一个文件包含该行。

'>'

文件不同，只有第二个文件包含该行。

比较选项：

[`-a`](#a) `--text`

将所有文件视为 ASCII 文本。 如果文件包含二进制字符，通常 `diff` 将简单地打印 “Binary files ... differ” 。 使用此选项会强制 `diff` 产生差异。

[`-B`](#B) `--ignore-blank-lines`

导致只包含空行的块被忽略

[`-b`](#b) `--ignore-space-change`

导致尾随空格（空格和制表符）被忽略，其他空格字符串比较相等。

[`-d`](#d) `--minimal`

非常努力地产生尽可能小的差异。 在处理具有许多更改的大型文件时，这可能会消耗大量的处理能力和内存。

[`-I`](#I) pattern `--ignore-matching-lines` pattern

忽略行与扩展正则表达式 pattern 匹配的更改、插入和删除。 可以指定多个 `-I` 模式。 更改中的所有行都必须匹配某些模式才能忽略更改。 有关正则表达式模式的更多信息，请参阅 re\_format(7) 。

[`-i`](#i) `--ignore-case`

忽略字母的大小写。 例如， “A” 将等于 “a” 。

[`-l`](#l) `--paginate`

通过 pr(1) 传递输出以对其进行分页。

[`-L`](#L) label `--label` label

打印 label 而不是上下文或统一差异标头中的第一个（和第二个，如果此选项被指定两次）文件名和时间。

[`-p`](#p) `--show-c-function`

使用统一和上下文差异，每次更改时显示上下文前最后一行的前 40 个字符，以字母、下划线或美元符号开头。 对于遵循标准布局约定的 C 源代码，这将显示更改适用的函数的原型。

[`-T`](#T) `--initial-tab`

对于正常、上下文或统一的输出格式，在该行的其余部分之前打印一个制表符而不是一个空格。 这使得行中的制表符对齐一致。

[`-t`](#t) `--expand-tabs`

将展开输出行中的选项卡。 正常或 `-c` 输出将字符添加到每行的前面，这可能会破坏原始源代码行的缩进并使输出列表难以解释。 此选项将保留原始源的缩进。

[`-w`](#w) `--ignore-all-blanks`

类似于 `-b` `--ignore-space-change` 但会导致空格（空格和制表符）被完全忽略。 例如， “if ( a == b )” 将比较等于 “if(a==b)” 。

[`-W`](#W) number `--width` number

使用并排格式时最多输出 number 列。 默认值为 130。

[`--changed-group-format`](#-changed-group-format) GFMT

在提供的格式输入组

格式是带有特殊关键字的字符串：

%<

FILE1 中的行

%<

来自 FILE2 的行

[`--ignore-file-name-case`](#-ignore-file-name-case)

比较文件名时忽略大小写

[`--no-ignore-file-name-case`](#-no-ignore-file-name-case)

不要忽略大小写比较文件名（默认）

[`--normal`](#-normal)

默认差异输出

[`--speed-large-files`](#-speed-large-files)

与 GNU diff 兼容的存根选项

[`--strip-trailing-cr`](#-strip-trailing-cr)

删除输入文件上的回车

[`--suppress-common-lines`](#-suppress-common-lines)

使用并排格式时不输出公共行

[`--tabsize`](#-tabsize) number

代表制表符的空格数（默认 8）

目录比较选项：

[`-N`](#N) `--new-file`

如果一个文件只在一个目录中找到，就好像它也在另一个目录中找到但大小为零一样。

[`-P`](#P) `--unidirectional-new-file`

如果一个文件只在 dir2 中找到，就好像它也在 dir1 中找到但大小为零一样。

[`-r`](#r) `--recursive`

导致将 `diff` 递归应用到遇到的公共子目录。

[`-S`](#S) name `--starting-file` name

在中间重新启动一个目录 `diff` ，以文件 name 开头。

[`-s`](#s) `--report-identical-files`

导致 `diff` 报告相同的文件，否则未提及。

[`-X`](#X) file `--exclude-from` file

从比较中排除其基本名称与 file 中的行匹配的文件和子目录。 可以指定多个 `-X` 选项。

[`-x`](#x) pattern `--exclude` pattern

从比较中排除基本名称与 pattern 匹配的文件和子目录。 通过 fnmatch(3) 使用 shell 样式的通配符匹配模式。 可以指定多个 `-x` 选项。

如果两个参数都是目录，则 `diff` 按名称对目录的内容进行排序，然后对不同的文本文件运行常规文件 `diff` 算法，生成更改列表。 不同的二进制文件、公共子目录和只出现在一个目录中的文件都被这样描述。 在目录模式下，仅比较常规文件和目录。 如果遇到非常规文件，例如设备特殊文件或 FIFO，则会打印诊断消息。

如果 file1 和 file2 中只有一个是目录，则 `diff` 应用于非目录文件以及目录文件中包含的文件名与非目录文件的最后一个组件相同的文件。

如果 file1 或 file2 是 ‘-’, 则使用标准输入代替它。

[输出风格](#__u8F93___u51FA___u98CE___u683C_)
-----------------------------------------

默认（不带 `-e` `-、` `-c` 或 `-n` `--rcs` 选项）输出包含这些形式的行，其中 XX, YY, ZZ, QQ 分别是文件顺序的行号。

[`XX`](#XX)`a``YY`

在 file1 的第 XX 行（末尾）处，附加 file2 的第 YY 行的内容以使它们相等。

[`XX`](#XX_2)`a``YY,ZZ`

同上，但将 file2 的 YY 到 ZZ 的行范围附加到文件 1 的 XX 行。

[`XX`](#XX_3)`d``YY`

在第 XX 行删除该行。 值 YY 告诉哪一行更改将使 file1 与 file2 保持一致。

[`XX,YY`](#XX,YY)`d``ZZ`

删除 file1 中的 XX 到 YY 行范围。

[`XX`](#XX_4)`c``YY`

将 file1 中的 XX 行更改为 file2 中的 YY 行。

[`XX,YY`](#XX,YY_2)`c``ZZ`

用 ZZ 行替换指定行的范围。

[`XX,YY`](#XX,YY_3)`c``ZZ,QQ`

将 file1 中的 XX,YY 范围替换为 file2 中的 ZZ,QQ 范围。

这些行类似于将 file1 转换为 file2 的 ed(1) 子命令。 动作字母前的行号与 file1 相关；后面的属于 file2 。 因此，通过将 `a` 替换为 `d` 并以相反的顺序读取该行，还可以确定如何将 file2 转换为 file1 。 与 ed(1) 中一样，相同的对（其中 num1 = num2）被缩写为单个数字。

[文件](#__u6587___u4EF6_)
=======================

/tmp/diff.XXXXXXXX

比较设备或标准输入时使用的临时文件。 请注意，临时文件在创建后立即取消链接，因此它不会显示在目录列表中。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`diff` 实用程序以下列值之一退出：

0

没有发现差异。

1

发现了差异。

\>1

发生错误。

[实例](#__u5B9E___u4F8B_)
=======================

比较 old\_dir 和 new\_dir 递归生成统一差异并将仅在这些目录之一中找到的文件视为新文件：

$ diff -ruN /path/to/old\_dir /path/to/new\_dir 

同上，但不包括匹配表达式 “\*.h” 和 “\*.c” 的文件：

$ diff -ruN -x '\*.h' -x '\*.c' /path/to/old\_dir /path/to/new\_dir 

显示单行指示文件是否不同：

$ diff -q /boot/loader.conf /boot/defaults/loader.conf 文件 /boot/loader.conf 和 /boot/defaults/loader.conf 不同 

假设一个名为 example.txt 的文件具有以下内容：

FreeBSD 是一个操作系统 Linux是一个内核 OpenBSD 是一个操作系统 

将 stdin 与 example.txt 进行比较，从比较中排除包含 “Linux” 或 “Open” 的行：

$ echo "FreeBSD is an operating system" | diff -q -I 'Linux|Open' example.txt - 

[参见](#__u53C2___u89C1_)
=======================

cmp(1), comm(1), diff3(1), ed(1), patch(1), pr(1), sdiff(1) James W. Hunt and M. Douglas McIlroy, An Algorithm for Differential File Comparison, _Computing Science Technical Report_, Bell Laboratories 41, June 1976.

[标准](#__u6807___u51C6_)
=======================

`diff` 实用程序符合 IEEE Std 1003.1-2008 (“POSIX.1”) 规范。

标志 \[`-aDdIiLlNnPpqSsTtwXxy`\] 是对该规范的扩展。

[历史](#__u5386___u53F2_)
=======================

`diff` 命令出现在 Version 6 AT&T UNIX 中。

June 19, 2020

FreeBSD 13.1-RELEASE