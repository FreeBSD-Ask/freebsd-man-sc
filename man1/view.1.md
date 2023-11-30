  VI(1)  

VI(1)

FreeBSD General Commands Manual

VI(1)

[名称](#__u540D___u79F0_)
=======================

`ex`, `vi`, `view` —

文本编辑器

[概要](#__u6982___u8981_)
=======================

`ex` \[`-FRrSsv`\] \[`-c` cmd\] \[`-t` tag\] \[`-w` size\] \[file ...\] `vi `\[`-eFRrS`\] \[`-c` cmd\] \[`-t` tag\] \[`-w` size\] \[file ...\] `view` \[`-eFrS`\] \[`-c` cmd\] \[`-t` tag\] \[`-w` size\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`vi` 是一个面向屏幕的文本编辑器。 `ex` 是一个面向行的文本编辑器。 `ex` 和 `vi` 是同一程序的不同接口，可以在编辑会话期间来回切换。 `view` 等效于使用 `vi` 的 `-R` (read-only) 选项。

本手册页是 `ex`/`vi` 文本编辑器的 `nex`/`nvi` 版本提供的手册页。 `nex`/`nvi` 旨在作为原始第四伯克利软件分发 (4BSD) `ex` 和 `vi` 程序的 bug-for-bug 兼容替代品。 对于本手册页的其余部分，仅在需要将其与 `nex`/`nvi` 的历史实现区分开来时才使用 `ex`/`vi 。`

本手册页适用于已经熟悉 `ex`/`vi` 的用户。 几乎可以肯定，其他任何人都应该在此手册页之前阅读有关编辑器的好教程。 如果您在一个不熟悉的环境中，并且您绝对必须立即完成工作，请阅读选项说明后面的部分，标题为 [快速启动 。](#__u5FEB___u901F___u542F___u52A8____u3002_) 这可能足以让你继续前进。

可以使用以下选项：

[`-c`](#c) cmd

在加载的第一个文件上执行 cmd 。对文件中的初始定位特别有用，虽然 cmd 不限于定位命令。 这是具有历史意义的 “+cmd” 语法的 POSIX 1003.2 接口。 `nex`/`nvi` 支持新旧语法。

[`-e`](#e)

在 ex 模式下开始编辑，就好像命令名称是 `ex 。`

[`-F`](#F)

首次开始编辑时不要复制整个文件。 （默认情况下制作副本以防其他人在您的编辑会话期间修改文件。）

[`-R`](#R)

以只读模式开始编辑，就好像命令名称是 `view` 一样，或者设置了 `readonly` 选项。

[`-r`](#r)

恢复指定的文件，或者，如果没有指定文件，则列出可以恢复的文件。 如果不存在指定名称的可恢复文件，则编辑该文件，就像未指定 `-r` 选项一样。

[`-S`](#S)

使用 `secure` 编辑选项集运行，禁止对外部程序的所有访问。

[`-s`](#s)

输入批处理模式;仅适用于 `ex` 编辑会话。 批处理模式在运行 `ex` 脚本时很有用。 提示、信息性消息和其他面向用户的消息被关闭，并且不会读取启动文件或环境变量。 这是历史 “-” 参数的 POSIX 1003.2 接口。 `nex`/`nvi` 支持新旧语法。

[`-t`](#t) tag

在指定的 tag 处开始编辑 (参见 ctags(1) 。)

[`-v`](#v)

在 vi 模式下开始编辑，就好像命令名称是 `vi 。`

[`-w`](#w) size

将初始窗口大小设置为指定的行数。

`ex`/`vi` 的命令输入从标准输入中读取。 在 `vi` 界面中，如果标准输入不是终端，则会出错。 在 `ex` 接口中，如果标准输入不是终端， `ex` 无论如何都会从中读取命令；但是，会话将是批处理模式会话，就像指定了 `-s` 选项一样。

[快速启动](#__u5FEB___u901F___u542F___u52A8_)
=========================================

本节将告诉您使用 `vi` 执行简单编辑任务所需的最少数量。 如果您以前从未使用过任何屏幕编辑器，那么即使是这个简单的介绍，您也可能会遇到问题。 在这种情况下，您应该找一个已经知道 `vi` 的人并让他们引导您完成本节。

`vi` 是一个屏幕编辑器。 这意味着它几乎占据了整个屏幕，在每个屏幕行上显示文件的一部分，除了屏幕的最后一行。 屏幕的最后一行用于您向 `vi`, 发出命令，以及 `vi` 向您提供信息。

您需要了解的另一个事实是 `vi` 是一个模式编辑器，即，您正在输入文本或正在执行命令，并且您必须处于正确的模式才能执行其中一个或另一个。 当您第一次开始编辑文件时，您将处于命令模式。 有一些命令可以将您切换到输入模式。 只有一个键可以让您退出输入模式，那就是 ⟨escape⟩ 键。

在本手册中，键名用 ⟨ 和 ⟩ 表示，例如， ⟨escape⟩ 表示 “退出” 键，通常在终端键盘上标记为 “Esc” 。 如果您对自己所处的模式感到困惑，请继续输入 ⟨escape⟩ 键，直到 `vi` 对您发出哔哔声。 通常，如果您尝试执行不允许的操作， `vi` 会向您发出哔哔声。 它还将显示错误消息。

要开始编辑文件，请输入以下命令：

`$ vi file`

开始编辑后应立即输入的命令是：

`:set verbose showmode`

这将使编辑器为您提供详细的错误消息并在屏幕底部显示当前模式。

在文件中移动的命令是：

[`h`](#h)

将光标向左移动一个字符。

[`j`](#j)

将光标下移一行。

[`k`](#k)

将光标向上移动一行。

[`l`](#l)

将光标向右移动一个字符。

⟨`cursor-arrows`⟩

光标箭头键也应该起作用。

[`/`](#/)text

在文件中搜索字符串 “text” ，并将光标移动到其第一个字符。

输入新文本的命令是：

[`a`](#a)

在光标后追加新文本。

[`i`](#i)

在光标前插入新文本。

[`o`](#o)

在光标所在行下方打开一个新行，然后开始输入文本。

[`O`](#O)

在光标所在的行上方打开一个新行，然后开始输入文本。

⟨`escape`⟩

使用 `a 、` `i 、` `o` 或 `O` 命令之一进入输入模式后，使用 ⟨`escape`⟩ 退出输入文本并返回命令模式。

复制文本的命令是：

[`yy`](#yy)

复制光标所在的行。

[`p`](#p)

在光标所在的行之后附加复制的行。

删除文本的命令是：

[`dd`](#dd)

删除光标所在的行。

[`x`](#x)

删除光标所在的字符。

写入文件的命令是：

[`:w`](#:w)

将文件写回文件，并使用您最初在 `vi` 命令行上用作参数的名称。

[`:w`](#:w_2) file\_name

将文件写回到名为 file\_name 的文件中。

退出编辑和退出编辑器的命令是：

[`:q`](#:q)

退出编辑并离开 `vi` （如果您修改了文件，但未保存更改， `vi` 将拒绝退出）。

[`:q!`](#:q!)

退出，放弃您可能所做的任何修改。

最后一个警告：不寻常的字符可能会在屏幕上占据多于一列，而长行可能会占据多于一个屏幕行。 上述命令作用于 “physical” 字符和行，即无论占用多少屏幕行，它们都会影响整行，无论占用多少屏幕列，它们都会影响整个字符。

[常用表达](#__u5E38___u7528___u8868___u8FBE_)
=========================================

`ex`/`vi` 支持正则表达式 (REs) ，如 re\_format(7), 中所述，用于行地址，作为 `ex` `substitute 、` `global` 和 `v` 命令的第一部分以及搜索模式。 默认启用基本正则表达式 (BRE) ；如果启用了 `extended` 选项，则使用扩展正则表达式 (ERE) 。 使用 `magic` 选项可以在很大程度上禁用正则表达式的使用。

以下字符串在 `ex`/`vi` 版本的正则表达式中具有特殊含义：

*   一个空的正则表达式等价于最后一个使用的正则表达式。
*   ‘\\<’ 匹配单词的开头。
*   ‘\\>’ 匹配单词的结尾。
*   ‘~’ 匹配最后一个 `substitute` 命令的替换部分。

[缓冲区](#__u7F13___u51B2___u533A_)
================================

缓冲区是命令可以保存更改或删除的文本以供以后使用的区域。 `vi` 缓冲区以单个字符命名，前面有双引号，例如 `"`⟨c⟩; `ex` 缓冲区是相同的，但没有双引号。 `nex`/`nvi` 允许在预期缓冲区名称的位置使用任何没有其他含义的字符。

所有缓冲区都处于 _行模式_ 和 _字符模式 。_ 将行模式下的缓冲区插入到文本中会为其包含的每一行创建新行，而字符模式下的缓冲区会为其包含的第一行和最后一行 _之外_ 任何行创建新行。 第一行和最后一行插入到当前光标位置，成为当前行的一部分。 如果缓冲区中有不止一行，则当前行本身将被拆分。 所有将文本存储到缓冲区的 `ex` 命令都以行模式执行。 `vi` 命令的行为取决于其关联的运动命令：

*   ⟨`control-A`⟩, `h`, `l`, `,`, `0`, `B`, `E`, `F`, `T`, `W`, `^`, `b`, `e`, `f` 和 `t` 使目标缓冲区面向字符。
*   [`j`](#j_2), ⟨`control-M`⟩, `k`, `'`, `-`, `G`, `H`, `L`, `M`, `_` 和 `|` 使目标缓冲区面向行。
*   [`$`](#$), `%`, `` ` ``, `(`, `)`, `/`, `?`, `[[`, `]]`, `{` 和 `}` 使目标缓冲区面向字符，除非开始和结束位置是一行中的第一个和最后一个字符。 在这种情况下，缓冲区是面向行的。

`ex` 命令 `display buffers` 显示每个缓冲区的当前模式。

命名为 ‘a’ 到 ‘z’ 的缓冲区可以使用它们的大写等效项来引用，在这种情况下，新内容将被附加到缓冲区，而不是替换它。

名为 ‘1’ 到 ‘9’ 的缓冲区是特殊的。 如果未指定其他缓冲区并且满足以下条件之一，则使用 `c` (change) 或 `d` (delete) 命令修改的文本区域将放入数字缓冲区 ‘1’ 中：

*   它包含多于一行的字符。
*   它是使用面向线的运动来指定的。
*   它使用以下运动命令之一指定： ⟨`control-A`⟩, `` ` ``⟨character⟩, `n`, `N`, `%`, `/`, `{`, `}`, `(`, `)` 和 `? 。`

在完成此复制之前，缓冲区 ‘1’ 的先前内容被移动到缓冲区 ‘2’ 中， ‘2’ 被移动到缓冲区 ‘3’ 中，依此类推。 缓冲区 ‘9’ 的内容被丢弃。 请注意， _无论_ 用户是否指定另一个缓冲区，都会发生这种旋转。 在 `vi` 中，文本可以显式存储到数字缓冲区中。 在这种情况下，缓冲区轮换发生在缓冲区内容的替换之前。 数字缓冲区仅在 `vi` 模式下可用。

[VI 命令](#VI___u547D___u4EE4_)
=============================

以下部分描述了 `vi` 编辑器的命令模式下可用的命令。 以下单词在命令描述中具有特殊含义：

bigword

一组非空白字符。

buffer

命令可以放置文本的临时区域。 如果未指定，则使用默认缓冲区。 另请参见上面的 [BUFFERS](#BUFFERS) 。

count

一个正数，用于指定命令的所需迭代次数。 如果未指定，则默认为 1。

motion

光标移动命令，指示受影响文本区域的另一端，第一个是当前光标位置。 重复命令字符使其影响整个当前行。

word

一系列字母、数字或下划线。

buffer 和 count （如果两者都存在）可以按任何顺序指定。 motion 和 count ，如果两者都存在，则有效地相乘并被视为运动的一部分。

⟨`control-A`⟩

向前搜索从光标位置开始的单词。

\[count\] ⟨`control-B`⟩

向后翻页 count 屏幕。 如果可能，保持两条重叠线。

\[count\] ⟨`control-D`⟩

向前滚动 count 行。 如果未给出 count ，则向前滚动最后一个 ⟨`control-D`⟩ 或 ⟨`control-U`⟩ 命令指定的行数。 如果这是第一个 ⟨`control-D`⟩ 命令，则在当前屏幕中滚动一半的行数。

\[count\] ⟨`control-E`⟩

如果可能，向前滚动 count 行，保持当前行和列不变。

\[count\] ⟨`control-F`⟩

页面转发 count 屏幕。 如果可能，保持两条重叠线。

⟨`control-G`⟩

显示以下文件信息：文件名 (给 `vi`); 自上次写入以来文件是否已被修改；如果文件是只读的；当前行号；文件中的总行数；以及当前行号占文件总行数的百分比。

\[count\] ⟨`control-H`⟩

\[count\] `h`

将光标向后移动当前行中的 count 字符。

\[count\] ⟨`control-J`⟩

\[count\] ⟨`control-N`⟩

\[count\] `j`

向下移动光标 count 行而不更改当前列。

⟨`control-L`⟩

⟨`control-R`⟩

重新绘制屏幕。

\[count\] ⟨`control-M`⟩

\[count\] `+`

将光标向下移动 count 行到该行的第一个非空白字符。

\[count\] ⟨`control-P`⟩

\[count\] `k`

将光标向上移动 count 行，而不更改当前列。

⟨`control-T`⟩

返回到最近的标签上下文。

\[count\] ⟨`control-U`⟩

向后滚动 count 行。 如果未给出 count ，则向后滚动最后一个 ⟨`control-D`⟩ 或 ⟨`control-U`⟩ 命令指定的行数。 如果这是第一个 ⟨`control-U`⟩ 命令，则在当前屏幕中滚动一半的行数。

⟨`control-W`⟩

切换到窗口中的下一个下一个屏幕，如果窗口中没有下一个屏幕，则切换到第一个屏幕。

\[count\] ⟨`control-Y`⟩

如果可能，向后滚动 count 行，保持当前行和列不变。

⟨`control-Z`⟩

暂停当前的编辑器会话。

⟨`escape`⟩

执行正在输入的 `ex` 命令，如果它只是部分的，则将其取消。

⟨`control-]`⟩

将标签引用推送到标签堆栈上。

⟨`control-^`⟩

切换到最近编辑的文件。

\[count\] ⟨`space`⟩

\[count\] `l`

向前移动光标 count 字符而不更改当前行。

\[count\] `!` motion shell-argument(s) ⟨`carriage-return`⟩

用 `shell` 选项命名的程序的输出 (标准输出和标准错误) 替换 count 和 motion 跨越的行，用 `-c` 标志后跟 shell-argument(s) 调用 (捆绑到单个参数中 。) 在 shell-argument(s) 中， ‘% 、’ ‘#’ 和 ‘!’ 字符扩展为当前文件名、前一个当前文件名和前一个 `!` 的命令文本 或者 `:!` 命令，分别。 ‘% 、’ ‘#’ 和 ‘!’ 的特殊含义 可以通过用反斜杠转义它们来覆盖。

\[count\] `#` `#` | [`+`](#+)|[`-`](#-)

从光标位置或在其后的第一个非空白字符开始，按 count 递增 (尾随 ‘#’ 或 ‘+’) 或递减 (随 ‘-’) 光标下的数字。 带有前导 ‘0x’ 或 ‘0X’ 的数字被解释为十六进制数字。 带有前导 ‘0’ 的数字被解释为八进制数字，除非它们包含非八进制数字。 其他数字可能以 ‘+’ 或 ‘-’ 符号为前缀。

\[count\] `$`

将光标移动到行尾。 如果指定了 count ，则另外将光标向下移动 count − 1 行。

[`%`](#_)

移动到与在光标位置或最靠近其右侧找到的字符匹配的 `matchchars` 字符。

[`&`](#&)

在当前行重复前面的替换命令。

[`'`](#_(aq)⟨character⟩

[`` ` ``](#__)⟨character⟩

返回到由字符 character 标记的光标位置，或者，如果 character 是 ‘'’ 或 ‘\`’, 则返回到以下命令最后一个之前的光标位置： ⟨`control-A`⟩, ⟨`control-T`⟩, ⟨`control-]`⟩, `%`, `'`, `` ` ``, `(`, `)`, `/`, `?`, `G`, `H`, `L`, `[[`, `]]`, `{`, `} 。` 第一种形式返回由 character 标记的行的第一个非空白字符。 第二种形式返回以 character 标记的行和列。

\[count\] `(`

\[count\] `)`

分别向后或向前移动 count 句子。 句子是一个文本区域，从前一个句子、段落或部分边界之后的第一个非空白字符开始，一直持续到下一个句号、感叹号或问号字符，后跟任意数量的右括号、方括号、双引号或单引号字符，后跟一个行尾字符或两个空格字符。 空行组 (或仅包含空白字符的行) 被视为一个句子。

\[count\] `,`

反向查找字符 (即最后的 `F`, `f`, `T` 或 `t` 命令) count 。

\[count\] `-`

移动到上一行的第一个非空白字符， count 次。

\[count\] `.`

重复上次修改文本的 `vi` 命令。 count 替换重复命令的 count 参数和相关 motion 的计数参数。 如果 `.` 命令重复 `u` 命令，更改日志向前或向后滚动，取决于 `u` 命令的操作。

/RE ⟨`carriage-return`⟩

/RE/ \[offset\] \[`z`\] ⟨`carriage-return`⟩

?RE ⟨`carriage-return`⟩

?RE? \[offset\] \[`z`\] ⟨`carriage-return`⟩

[`N`](#N)

[`n`](#n)

向前 (‘/’) 或向后 (‘?’) 搜索正则表达式。 `n` 和 `N` 分别以相同或相反的方向重复最后一次搜索。 如果 RE 为空，则使用最后一个搜索正则表达式。 如果指定了 offset ，则光标位于匹配的正则表达式之前或之后的 offset 行。 如果 `n` 或 `N` 命令用作 `!` 命令，将不会提示输入命令的文本和之前的 `!` 将被执行。 多个搜索模式可以通过用分号和零个或多个空白字符分隔来组合在一起。 这些模式从左到右评估，最终光标位置由最后一个搜索模式确定。 可以将 `z` 命令附加到封闭的搜索表达式以重新定位结果行。

[`0`](#0)

移动到当前行的第一个字符。

[`:`](#:_&)

执行 `ex` 命令。

\[count\] `;`

重复最后一个字符查找（即最后一个 `F`, `f`, `T` 或 `t` 命令) count 次。

\[count\] `<` motion

\[count\] `>` motion

将 count 线分别向左或向右移动一定量的 `shiftwidth 。`

[`@`](#@) buffer

将命名 buffer 作为 `vi` 命令执行。 缓冲区也可能包含 `ex` 命令，但它们必须表示为 `:` 命令。 如果 buffer 是 ‘@’ 或 ‘\*’, 则应使用最后执行的缓冲区。

\[count\] `A`

进入输入模式，在行尾追加文本。 如果给出了 count 参数，则在退出输入模式后，输入的字符将重复 count − 1 次。

\[count\] `B`

向后移动 count bigwords。

\[buffer\] `C`

将文本从当前位置更改为行尾。 如果指定了 buffer ，则将已删除的文本 “yank” 到 buffer 中。

\[buffer\] `D`

删除从当前位置到行尾的文本。 如果指定了 buffer ，则将已删除的文本 “yank” 到 buffer 中。

\[count\] `E`

向前 count end-of-bigwords。

\[count\] `F` ⟨character⟩

在当前行向后搜索 count ⟨character 。⟩

\[count\] `G`

如果未指定 count, 则移至 count 或文件的最后一行。

\[count\] `H`

移动到屏幕 count − 屏幕顶部下方的 1 行。

\[count\] `I`

进入输入模式，在行首插入文本。 如果给出了 count 参数，则输入的字符将重复 count − 1 次。

\[count\] `J`

将 count 行与当前行连接起来。 如果两条连接线以问号、句点或感叹号结尾，则将两条连接线之间的间距设置为两个空白字符。 否则设置为一个空白字符。

\[count\] `L`

移动到屏幕行 count − 屏幕底部上方的 1 行。

[`M`](#M)

移动到屏幕中间的屏幕行。

\[count\] `O`

进入输入模式，在当前行上方的新行中追加文本。 如果给出了 count 参数，则输入的字符将重复 count − 1 次。

\[buffer\] `P`

如果 buffer 是面向字符的，则在当前列之前插入 buffer 中的文本，如果是面向行的，则在当前行之前插入文本。

[`Q`](#Q)

退出 `vi` (或视图) 模式并切换到 `ex` 模式。

\[count\] `R`

进入输入模式，替换当前行中的字符。 如果给出了 count 参数，则在退出插入模式时，输入的字符将重复 count − 1 次。

\[buffer\] \[count\] `S`

替换 count 线。如果指定了 buffer ，则将已删除的文本 “yank” 到 buffer 中。

\[count\] `T` ⟨character⟩

向后搜索， count 次，通过当前行查找指定 ⟨character⟩ 之后的字符。

[`U`](#U)

将当前行恢复到光标上次移动到它之前的状态。

\[count\] `W`

向前 count bigwords。

\[buffer\] \[count\] `X`

在当前行删除光标前的 count 个字符。 如果指定了 buffer ，则将已删除的文本 “yank” 到 buffer 中。

\[buffer\] \[count\] `Y`

复制 (或 “yank”) count 行到 buffer 中。

[`ZZ`](#ZZ)

如果没有更多文件要编辑，则写入文件并退出 `vi` 。 连续输入两个 “quit” 命令会忽略任何剩余的要编辑的文件。

\[count\] `[[`

备份 count 部分边界。

\[count\] `]]`

向前移动 count 部分边界。

[`^`](#_(ha)

移动到当前行的第一个非空白字符。

\[count\] `_`

向下移动 count − 1 行，到第一个非空白字符。

\[count\] `a`

进入输入模式，在光标后追加文本。 如果给出了 count 参数，则输入的字符将重复 count 次。

\[count\] `b`

向后移动 count 单词。

\[buffer\] \[count\] `c` motion

更改 count 和 motion 描述的文本区域。 如果指定了 buffer ，则将更改的文本 “yank” 到 buffer 中。

\[buffer\] \[count\] `d` motion

删除由 count 和 motion 描述的文本区域。 如果指定了 buffer ，则将已删除的文本 “yank” 到 buffer 中。

\[count\] `e`

向前 count 词尾。

\[count\] `f` ⟨character⟩

向前搜索， count 次数，通过当前行的其余部分查找 ⟨character 。⟩

\[count\] `i`

进入输入模式，在光标前插入文本。 如果给出了 count 参数，则输入的字符将重复 count 次。

[`m`](#m) ⟨character⟩

将当前上下文 (行和列) 保存为 ⟨character 。⟩

\[count\] `o`

进入输入模式，在当前行下的新行中追加文本。 如果给出了 count 参数，则输入的字符将重复 count − 1 次。

\[buffer\] `p`

从 buffer 追加文本。如果 buffer 是面向字符的，则在当前列之后附加文本，否则在当前行之后。

\[count\] `r` ⟨character⟩

用 character 替换 count 字符。

\[buffer\] \[count\] `s`

从当前字符开始替换当前行中的 count 个字符。 如果指定了 buffer ，则将替换的文本 “yank” 到 buffer 中。

\[count\] `t` ⟨character⟩

向前搜索， count 次数，通过当前行查找 ⟨character⟩ 之前的字符。

[`u`](#u)

撤消对文件所做的最后更改。 如果重复， `u` 命令会在这两种状态之间交替。 `.` 命令在 `u` 之后立即使用时，会导致更改日志向前或向后滚动，具体取决于 `u` 命令的操作。

\[count\] `w`

向前 count 单词。

\[buffer\] \[count\] `x`

删除当前光标位置的 count 个字符，但不超过行尾。

\[buffer\] \[count\] `y` motion

将 count 和 motion 指定的文本区域复制 (或 “yank”) 到缓冲区中。

\[count1\] `z` \[count2\] `type`

重绘，可选择重新定位和调整屏幕大小。 如果指定了 count2 ，则将屏幕大小限制为 count2 行。 可以使用以下 `type` 字符：

[`+`](#+_2)

如果指定了 count1 ，则将行 count1 放在屏幕顶部。 否则，显示当前屏幕之后的屏幕。

⟨`carriage-return`⟩

将行 count1 放在屏幕顶部。

[`.`](#._&)

将行 count1 放在屏幕中央。

[`-`](#-_2)

将行 count1 放在屏幕底部。

[`^`](#_(ha_2)

如果给出了 count1 ，则显示 count1 之前的屏幕 (即之前的 2 个屏幕 。) 否则，显示当前屏幕之前的屏幕。

\[count\] `{`

向后移动 count 段落。

\[column\] `|`

移动到当前 column 的特定列位置。 如果省略 column ，则移动到当前行的开头。

\[count\] `}`

向前 count 段落。

\[count\] `~` motion

如果未设置 `tildeop` 选项，则反转下一个 count 字符的大小写，并且不能指定任何 motion 。 否则， motion 是强制性的，并且 `~` 反转由 count 和 motion 指定的文本区域中字符的大小写。

⟨`interrupt`⟩

中断当前操作。 ⟨interrupt⟩ 字符通常是 ⟨control-C 。⟩

[VI 文本输入命令](#VI___u6587___u672C___u8F93___u5165___u547D___u4EE4_)
=================================================================

以下部分描述了 `vi` 编辑器的文本输入模式下可用的命令。

⟨`nul`⟩

重播之前的输入。

⟨`control-D`⟩

擦除到前一个 shiftwidth 列边界。

[`^`](#_(ha_3)⟨`control-D`⟩

擦除所有自动缩进字符，并重置自动缩进级别。

[`0`](#0_2)⟨`control-D`⟩

擦除所有自动缩进字符。

⟨`control-T`⟩

插入足够的 ⟨tab⟩ 和 ⟨space⟩ 字符以向前移动到下一个 shiftwidth 列边界。 如果设置了 `expandtab` 选项，则只插入 ⟨space⟩ 字符。

⟨`erase`⟩

⟨`control-H`⟩

擦除最后一个字符。

⟨`literal next`⟩

从任何特殊含义中转义下一个字符。 ⟨literal next⟩ 字符通常是 ⟨control-V⟩.

⟨`escape`⟩

解析文件中的所有文本输入，并返回命令模式。

⟨`line erase`⟩

擦除当前行。

⟨`control-W`⟩

⟨`word erase`⟩

抹去最后一个字。 word 的定义取决于 `altwerase` 和 `ttywerase` 选项。

⟨`control-X`⟩\[`0-9A-Fa-f`\]`+`

在文本中插入具有指定十六进制值的字符。

⟨`interrupt`⟩

中断文本输入模式，返回命令模式。 ⟨interrupt⟩ 字符通常是 ⟨control-C 。⟩

[EX 命令](#EX___u547D___u4EE4_)
=============================

以下部分描述了 `ex` 编辑器中可用的命令。 在下面的每个条目中，标记行是该命令的用法概要。

⟨`end-of-file`⟩

滚动屏幕。

[`!`](#!_&) argument(s)

\[range\] `!` argument(s)

执行 shell 命令，或通过 shell 命令过滤行。

[`"`](#__2)

评论。

\[range\] `nu`\[`mber`\] \[count\] \[flags\]

\[range\] `#` \[count\] \[flags\]

显示选定的行，每行前面都有其行号。

[`@`](#@_2) buffer

[`*`](#*) buffer

执行缓冲区。

\[range\] `<`\[`< ...`\] \[count\] \[flags\]

向左移行。

\[line\] `=` \[flags\]

显示 line 的行号。 如果未指定 line ，则显示文件中最后一行的行号。

\[range\] `>`\[`> ...`\] \[count\] \[flags\]

右移行。

[`ab`](#ab)\[`breviate`\] lhs rhs

仅 `vi` 。 将 lhs 作为 rhs 的缩写添加到缩写列表中。

\[line\] `a`\[`ppend`\]\[`!`\]

输入文本附加在指定行之后。

[`ar`](#ar)\[`gs`\]

显示参数列表。

[`bg`](#bg)

仅 `vi` 。 背景当前屏幕。

\[range\] `c`\[`hange`\]\[`!`\] \[count\]

输入文本替换指定范围。

[`chd`](#chd)\[`ir`\]\[`!`\] \[directory\]

[`cd`](#cd)\[`!`\] \[directory\]

更改当前工作目录。

\[range\] `co`\[`py`\] line \[flags\]

\[range\] `t` line \[flags\]

复制目标行之后的指定行。 line.

[`cs`](#cs)\[`cope`\] `add` | [`find`](#find) | [`help`](#help) | [`kill`](#kill) | [`reset`](#reset)

执行 Cscope 命令。

\[range\] `d`\[`elete`\] \[buffer\] \[count\] \[flags\]

从文件中删除行。

[`di`](#di)\[`splay`\] `b`\[`uffers`\] | [`c`](#c_2)\[`onnections`\] | [`s`](#s_2)\[`creens`\] | [`t`](#t_2)\[`ags`\]

显示缓冲区、Cscope 连接、屏幕或标签。

\[`Ee`\]\[`dit`\]\[`!`\] \[+cmd\] \[file\]

\[`Ee`\]`x`\[`!`\] \[+cmd\] \[file\]

编辑不同的文件。

[`exu`](#exu)\[`sage`\] \[command\]

显示 `ex` 命令的用法。

[`f`](#f)\[`ile`\] \[file\]

显示并可选择更改文件名。

\[`Ff`\]`g` \[name\]

仅限 `vi` 模式。 前景指定的屏幕。

\[range\] `g`\[`lobal`\] /pattern/ \[commands\]

\[range\] `v` /pattern/ \[commands\]

将命令应用于匹配 (‘global’) 或不匹配 (‘v’) 模式的行。

[`he`](#he)\[`lp`\]

显示帮助消息

\[line\] `i`\[`nsert`\]\[`!`\]

输入文本插入到指定行之前。

\[range\] `j`\[`oin`\]\[`!`\] \[count\] \[flags\]

将文本行连接在一起。

\[range\] `l`\[`ist`\] \[count\] \[flags\]

清楚地显示行。

[`map`](#map)\[`!`\] \[lhs rhs\]

定义或显示地图 (仅适用于 `vi` 。)

\[line\] `ma`\[`rk`\] ⟨character⟩

\[line\] `k` ⟨character⟩

用标记 ⟨character⟩ 标记行。

\[range\] `m`\[`ove`\] line

将指定的行移到目标行之后。

[`mk`](#mk)\[`exrc`\]\[`!`\] file

将缩写、编辑器选项和映射写入指定 file 。

\[`Nn`\]\[`ext`\]\[`!`\] \[file ...\]

编辑参数列表中的下一个文件。

[`pre`](#pre)\[`serve`\]

将文件保存为以后可以使用 `ex` `-r` 选项恢复的格式。

\[`Pp`\]`rev`\[`ious`\]\[`!`\]

编辑参数列表中的前一个文件。

\[range\] `p`\[`rint`\] \[count\] \[flags\]

显示指定的行。

\[line\] `pu`\[`t`\] \[buffer\]

将缓冲区内容附加到当前行。

[`q`](#q)\[`uit`\]\[`!`\]

结束编辑会话。

\[line\] `r`\[`ead`\]\[`!`\] \[file\]

读取一个文件。

[`rec`](#rec)\[`over`\] file

恢复 file ，如果它以前保存。

[`res`](#res)\[`ize`\] \[`+`|`-`\]size

仅限 `vi` 模式。扩大或缩小当前屏幕。

[`rew`](#rew)\[`ind`\]\[`!`\]

倒回参数列表。

[`se`](#se)\[`t`\] \[option\[=\[value\]\] ...\] \[nooption ...\] \[option? ...\] \[all\]

显示或设置编辑器选项。

[`sh`](#sh)\[`ell`\]

运行 shell 程序。

[`so`](#so)\[`urce`\] file

从文件中读取并执行 `ex` 命令。

\[range\] `s`\[`ubstitute`\] \[/pattern/replace/\] \[options\] \[count\] \[flags\]

\[range\] `&` \[options\] \[count\] \[flags\]

\[range\] `~` \[options\] \[count\] \[flags\]

进行替换。 replace 字段可以包含以下任何序列：

‘&’

由 pattern 匹配的文本。

‘~’

前一个 `substitute` 命令的替换部分。

‘%’

如果这是整个 replace 模式，则前一个 `substitute` 命令的替换部分。

‘\\#’

其中 ‘#’ 是一个从 1 到 9 的整数，由 pattern 中的第 #个子表达式匹配的文本。

‘\\L’

将直到下一次出现 ‘\\E’ 或 ‘\\e’ 的行尾的字符转换为小写。

‘\\l’

使下一个字符转换为小写。

‘\\U’

将直到下一次出现 ‘\\E’ 或 ‘\\e’ 的行尾的字符转换为大写。

‘\\u’

使下一个字符转换为大写。

[`su`](#su)\[`spend`\]\[`!`\]

[`st`](#st)\[`op`\]\[`!`\]

⟨`suspend`⟩

暂停编辑会话。 ⟨suspend⟩ 字符通常是 ⟨control-Z⟩ 。

\[`Tt`\]`a`\[`g`\]\[`!`\] tagstring

编辑包含指定标签的文件。

[`tagn`](#tagn)\[`ext`\]\[`!`\]

编辑包含当前标记的下一个上下文的文件。

[`tagp`](#tagp)\[`op`\]\[`!`\] \[file | number\]

弹出到标签堆栈中的指定标签。

[`tagpr`](#tagpr)\[`ev`\]\[`!`\]

编辑包含当前标记的先前上下文的文件。

[`tagt`](#tagt)\[`op`\]\[`!`\]

弹出到标签堆栈上最近的标签，清除堆栈。

[`una`](#una)\[`bbreviate`\] lhs

仅 `vi` 。 删除缩写。

[`u`](#u_2)\[`ndo`\]

撤消对文件所做的最后更改。

[`unm`](#unm)\[`ap`\]\[`!`\] lhs

取消映射映射的字符串。

[`ve`](#ve)\[`rsion`\]

显示 `ex`/`vi` 编辑器的版本。

\[line\] `vi`\[`sual`\] \[type\] \[count\] \[flags\]

仅限 `ex` 模式。输入 `vi` 。

\[`Vi`\]`i`\[`sual`\]\[`!`\] \[+cmd\] \[file\]

仅限 `vi` 模式。编辑一个新文件。

[`viu`](#viu)\[`sage`\] \[command\]

显示 `vi` 命令的用法。

\[range\] `w`\[`rite`\]\[`!`\] \[>>\] \[file\]

\[range\] `w`\[`rite`\] \[`!`\] \[file\]

\[range\] `wn`\[`!`\] \[>>\] \[file\]

\[range\] `wq`\[`!`\] \[>>\] \[file\]

写文件。

\[range\] `x`\[`it`\]\[`!`\] \[file\]

退出编辑器，如果文件已被修改，则写入文件。

\[range\] `ya`\[`nk`\] \[buffer\] \[count\]

将指定的行复制到缓冲区。

\[line\] `z` \[type\] \[count\] \[flags\]

调整窗口。

[设置选项](#__u8BBE___u7F6E___u9009___u9879_)
=========================================

可以设置 (或取消设置) 大量选项来更改编辑器的行为。 本节介绍选项、它们的缩写和它们的默认值。

在下面的每个条目中，标签行的第一部分是选项的全名，后跟任何等效的缩写。 方括号中的部分是选项的默认值。 大多数选项都是布尔值，即它们不是开就是关，并且没有关联的值。

除非另有说明，否则选项适用于 `ex` 和 `vi` 模式。

[`altwerase`](#altwerase) \[off\]

仅 `vi` 。选择替代字擦除算法。

[`autoindent`](#autoindent), `ai` \[off\]

自动缩进新行。

[`autoprint`](#autoprint), `ap` \[on\]

仅限 `ex` 。自动显示当前行。

[`autowrite`](#autowrite), `aw` \[off\]

更改文件或暂停编辑器会话时自动写入修改后的文件。

[`backup`](#backup) \[""\]

在文件被覆盖之前备份它们。

[`beautify`](#beautify), `bf` \[off\]

丢弃控制字符。

[`cdpath`](#cdpath) \[environment variable `CDPATH`, `or current directory`\]

用作 `cd` 命令的路径前缀的目录路径。

[`cedit`](#cedit) \[no default\]

设置字符以编辑冒号命令行历史。

[`columns`](#columns), `co` \[80\]

设置屏幕中的列数。

[`comment`](#comment) \[off\]

仅 `vi` 。 跳过 shell、C 和 C++ 语言文件中的前导注释。

[`directory`](#directory), `dir` \[environment variable `TMPDIR`, `or` /tmp\]

创建临时文件的目录。

[`edcompatible`](#edcompatible), `ed` \[off\]

记住 `substitute` 命令的 ‘c’ and ‘g’ 后缀的值，而不是将它们初始化为每个新命令的未设置。

[`errorbells`](#errorbells), `eb` \[off\]

仅限 `ex` 。用铃宣布错误消息。

[`escapetime`](#escapetime) \[1\]

十分之一秒 `ex`/`vi` 等待后续键完成 ⟨escape⟩ 键映射。

[`expandtab`](#expandtab), `et` \[off\]

在插入、替换或移动文本、自动缩进、使用 ⟨`control-T`⟩ 缩进、使用 ⟨`control-D`⟩ 缩进或使用 `!` 过滤行时，将 ⟨tab⟩ 字符扩展为 ⟨space⟩ 命令。

[`exrc`](#exrc), `ex` \[off\]

读取本地目录中的启动文件。

[`extended`](#extended) \[off\]

使用扩展正则表达式 (ERE) 而不是基本正则表达式 (BRE) 。 有关正则表达式的更多信息，请参阅 re\_format(7) 。

[`filec`](#filec) \[⟨tab⟩\]

设置字符以在冒号命令行上执行文件路径完成。

[`fileencoding`](#fileencoding), `fe` \[auto detect\]

设置当前文件的编码。

[`flash`](#flash) \[on\]

闪烁屏幕而不是在错误时发出键盘蜂鸣声。

[`hardtabs, ht`](#hardtabs,_ht) \[0\]

设置硬件选项卡设置之间的间距。 此选项当前无效。

[`iclower`](#iclower) \[off\]

使所有正则表达式不区分大小写，只要搜索字符串中没有出现大写字母。

[`ignorecase`](#ignorecase), `ic` \[off\]

忽略正则表达式中的大小写差异。

[`inputencoding`](#inputencoding), `ie` \[locale\]

设置输入字符的编码。

[`keytime`](#keytime) \[6\]

十分之一秒 `ex`/`vi` 等待后续键完成键映射。

[`leftright`](#leftright) \[off\]

仅 `vi` 。进行左右滚动。

[`lines`](#lines), `li` \[24\]

仅 `vi` 。设置屏幕中的行数。

[`lisp`](#lisp) \[off\]

仅 `vi` 。 修改各种搜索命令和选项以使用 Lisp。此选项尚未实施。

[`list`](#list) \[off\]

以明确的方式显示行。

[`lock`](#lock) \[on\]

尝试对正在编辑、读取或写入的任何文件进行独占锁定。

[`magic`](#magic) \[on\]

关闭时，除 ‘^’ 和 ‘$’ 外的所有正则表达式字符都被视为普通字符。 在单个字符前面加上 ‘\\’ 会重新启用它们。

[`matchchars`](#matchchars) \[\[\]{}()\]

通过 `%` 命令查找的字符对。

[`matchtime`](#matchtime) \[7\]

仅 `vi` 。 当设置了 `showmatch` 选项时，十分之一秒 `ex`/`vi` 在匹配字符上暂停。

[`mesg`](#mesg) \[on\]

允许来自其他用户的消息。

[`msgcat`](#msgcat) \[/usr/share/vi/catalog/\]

选择用于以指定语言显示错误和信息性消息的消息目录。

[`modelines`](#modelines), `modeline` \[off\]

阅读每个文件的第一行和最后几行以获取 `ex` 命令。 此选项将永远不会实施。

[`noprint`](#noprint) \[""\]

从未作为可打印字符处理的字符。

[`number`](#number), `nu` \[off\]

在显示的每一行之前加上其当前行号。

[`octal`](#octal) \[off\]

将未知字符显示为八进制数字，而不是默认的十六进制。

[`open`](#open) \[on\]

仅限 `ex` 。 如果未设置此选项，则不允许 `open` 和 `visual` 命令。

[`optimize`](#optimize), `opt` \[on\]

仅 `vi` 。优化哑终端的文本吞吐量。此选项尚未实施。

[`paragraphs`](#paragraphs), `para` \[IPLPPPQPP LIpplpipbp\]

仅 `vi` 。 为 `{` 和 `}` 命令定义额外的段落边界。

[`path`](#path) \[""\]

定义其他目录以搜索正在编辑的文件。

[`print`](#print) \[""\]

始终作为可打印字符处理的字符。

[`prompt`](#prompt) \[on\]

仅限 `ex` 。 显示命令提示符。

[`readonly`](#readonly), `ro` \[off\]

将文件和会话标记为只读。

[`recdir`](#recdir) \[/var/tmp/vi.recover\]

存储恢复文件的目录。

[`redraw`](#redraw), `re` \[off\]

仅 `vi` 在一个愚蠢的终端上模拟一个智能终端。 此选项尚未实施。

[`remap`](#remap) \[on\]

重新映射键直到解决。

[`report`](#report) \[5\]

设置编辑器报告更改或抽出的行数。

[`ruler`](#ruler) \[off\]

仅 `vi` 。 在冒号命令行上显示行/列标尺。

[`scroll`](#scroll), `scr` \[window size / 2\]

设置滚动的行数。

[`searchincr`](#searchincr) \[off\]

使 `/` 和 `?` 命令增量。

[`sections`](#sections), `sect` \[NHSHH HUnhsh\]

仅 `vi` 。 为 `[[` 和 `]]` 命令定义额外的节边界。

[`secure`](#secure) \[off\]

关闭对外部程序的所有访问。

[`shell`](#shell), `sh` \[environment variable `SHELL`, `or` /bin/sh\]

选择编辑器使用的 shell 。

[`shellmeta`](#shellmeta) \[~{\[\*?$\`'"\\\]

设置元字符检查以确定是否需要扩展文件名。

[`shiftwidth`](#shiftwidth), `sw` \[8\]

设置 autoindent 和 shift 命令的缩进宽度。

[`showmatch`](#showmatch), `sm` \[off\]

仅 `vi` 。 插入右侧字符时，请注意左侧匹配字符。

[`showmode`](#showmode), `smd` \[off\]

仅 `vi` 。 显示当前编辑器模式和 “modified” 标志。

[`sidescroll`](#sidescroll) \[16\]

仅 `vi` 。 设置左右滚动将移动的量。

[`slowopen`](#slowopen), `slow` \[off\]

在文本输入期间延迟显示更新。 此选项尚未实施。

[`sourceany`](#sourceany) \[off\]

读取不属于当前用户的启动文件。 此选项将永远不会实施。

[`tabstop`](#tabstop), `ts` \[8\]

此选项设置编辑器显示的选项卡宽度。

[`taglength`](#taglength), `tl` \[0\]

设置标签名称中的有效字符数。

[`tags`](#tags), `tag` \[tags\]

设置标签文件列表。

[`term`](#term), `ttytype`, `tty` \[environment variable `TERM`\]

设置终端类型。

[`terse`](#terse) \[off\]

历史上，此选项使编辑器消息不那么冗长。 它在此实现中没有任何影响。

[`tildeop`](#tildeop) \[off\]

修改 `~` 命令以采取相关的动作。

[`timeout`](#timeout), `to` \[on\]

可能映射的键超时。

[`ttywerase`](#ttywerase) \[off\]

仅 `vi` 。 选择替代擦除算法。

[`verbose`](#verbose) \[off\]

仅 `vi` 。 为每个错误显示一条错误消息。

[`w300`](#w300) \[no default\]

仅 `vi` 。 如果波特率小于 1200 波特，请设置窗口大小。

[`w1200`](#w1200) \[no default\]

仅 `vi` 。 如果波特率等于 1200 波特，请设置窗口大小。

[`w9600`](#w9600) \[no default\]

仅 `vi` 。 如果波特率大于 1200 波特，请设置窗口大小。

[`warn`](#warn) \[on\]

仅限 `ex` 。如果文件自上次写入以来已被修改，此选项会导致在终端上打印一条警告消息，在 `!` 命令。

[`window`](#window), `w`, `wi` \[environment variable `LINES` − 1\]

设置屏幕的窗口大小。

[`windowname`](#windowname) \[off\]

将图标/窗口名称更改为当前文件名。

[`wraplen`](#wraplen), `wl` \[0\]

仅 `vi` 。 自动换行，从左边距指定的列数。 如果同时设置了 `wraplen` 和 `wrapmargin` 编辑选项，则使用 `wrapmargin` 值。

[`wrapmargin`](#wrapmargin), `wm` \[0\]

仅 `vi` 。 自动换行，从右边距指定的列数。 如果同时设置了 `wraplen` 和 `wrapmargin` 编辑选项，则使用 `wrapmargin` 值。

[`wrapscan`](#wrapscan), `ws` \[on\]

将搜索设置为环绕文件的结尾或开头。

[`writeany`](#writeany), `wa` \[off\]

关闭文件覆盖检查。

[环境变量](#__u73AF___u5883___u53D8___u91CF_)
=========================================

[`COLUMNS`](#COLUMNS)

屏幕上的列数。 此值覆盖任何系统或终端特定值。 如果在 `ex`/`vi` 运行时未设置 `COLUMNS` 环境变量，或者用户明确重置了 `columns` 选项， `ex`/`vi` 会将值输入到环境中。

[`EXINIT`](#EXINIT)

`ex` 动命令列表，在 /etc/vi.exrc 之后读取，除非还设置了变量 `NEXINIT` 。

[`HOME`](#HOME)

用户的主目录，用作启动 $HOME/.nexrc 和 $HOME/.exrc 文件的初始目录路径。 该值也用作 `cd` 命令的默认目录。

[`LINES`](#LINES)

屏幕上的行数。 此值覆盖任何系统或终端特定值。 如果在 `ex`/`vi` 运行时没有设置 `LINES` 环境变量，或者用户明确重置了 `lines` 选项， `ex`/`vi` 会将值输入到环境中。

[`NEXINIT`](#NEXINIT)

`ex` 启动命令列表，在 /etc/vi.exrc 之后阅读。

[`SHELL`](#SHELL)

用户选择的 shell (另请参见 `shell 选项`) 。

[`TERM`](#TERM)

用户的终端类型。 默认为 “unknown” 类型。 如果在 `ex`/`vi` 运行时没有设置 `TERM` 环境变量，或者用户明确地重置了 `term` 选项， `ex`/`vi` 会将值输入到环境中。

[`TMPDIR`](#TMPDIR)

用于存储临时文件的位置 (另请参见 `directory` 编辑选项) 。

[异步事件](#__u5F02___u6B65___u4E8B___u4EF6_)
=========================================

[`SIGALRM`](#SIGALRM)

`vi`/`ex` 使用此信号定期备份文件修改并在操作可能需要很长时间时显示 “busy” 消息。

[`SIGHUP`](#SIGHUP)

[`SIGTERM`](#SIGTERM)

如果当前缓冲区自上次完整写入后已更改，则编辑器会尝试保存修改后的文件，以便以后恢复。 有关详细信息，请参阅 `vi`/`ex` 参考手册 [Recovery](#Recovery) 部分。

[`SIGINT`](#SIGINT)

当中断发生时，当前操作停止，编辑器返回命令级。 如果在文本输入期间被中断，则已输入的文本将被解析到文件中，就好像文本输入已正常终止一样。

[`SIGWINCH`](#SIGWINCH)

屏幕已调整大小。有关详细信息，请参阅 `vi`/`ex` 参考手册部分 [Sizing the Screen](#Sizing_the_Screen) 。

[文件](#__u6587___u4EF6_)
=======================

/bin/sh

默认用户 shell 。

/etc/vi.exrc

系统范围的 `vi` 启动文件。 在启动序列中首先读取 `ex` 命令。 必须由 root 或用户拥有，并且只能由所有者写入。

/tmp

临时文件目录。

/var/tmp/vi.recover

默认恢复文件目录。

$HOME/.nexrc

用户主目录启动文件的首选，在 /etc/vi.exrc 之后读取 `ex` 命令，除非设置了 `NEXINIT` 或 `EXINIT` 。 必须由 root 或用户拥有，并且只能由所有者写入。

$HOME/.exrc

用户主目录启动文件的第二选择， `ex` 命令在与 $HOME/.nexrc 相同的条件下读取。

.nexrc

本地目录启动文件的首选，如果之前打开了 `exrc` 选项，则在启动序列结束时读取 `ex` 命令。 必须由用户拥有，并且只能由所有者写入。

.exrc

本地目录启动文件的第二选择，在与 .nexrc 相同的条件下读取 `ex` 命令。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`ex` 和 `vi` 实用程序在成功时退出 0，如果发生错误则退出 >0 。

[参见](#__u53C2___u89C1_)
=======================

ctags(1), iconv(1), re\_format(7) vi/ex 参考手册, [https://docs.freebsd.org/44doc/usd/13.viref/paper.pdf](https://docs.freebsd.org/44doc/usd/13.viref/paper.pdf).

[标准](#__u6807___u51C6_)
=======================

`nex`/`nvi` 接近 IEEE Std 1003.1-2008 (“POSIX.1”) 。 该文件在几个地方与历史上的 `ex`/`vi` 实践不同；双方都需要做出改变。

[历史](#__u5386___u53F2_)
=======================

`ex` 编辑器首次出现在 1BSD 中。 `ex`/`vi` 编辑器的 `nex`/`nvi` 替代品首次出现在 4.4BSD 中。

[作者](#__u4F5C___u8005_)
=======================

Bill Joy 在 1977 年编写了 `ex` 的原始版本。

September 25, 2020

FreeBSD 13.1-RELEASE