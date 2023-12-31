  ee(1)  

ee(1)

ee(1)

[名称](#__u540D___u79F0_)
=======================

ee - 简单的编辑器

[概要](#__u6982___u8981_)
=======================

ee \[-e\] \[-i\] \[-h\] \[+#\] \[_file_ ...\] ree \[-e\] \[-i\] \[-h\] \[+#\] \[_file_ ...\] 

[描述](#__u63CF___u8FF0_)
=======================

描述 _ee_ 是一个简单的面向屏幕的文本编辑器。 它始终处于文本插入模式，除非终端底部有提示，或者存在菜单（在终端中间的框中）。 命令 _ree_ 与 _ee,_ 相同，但仅限于编辑命名文件（不允许文件操作或 shell 转义）。

具有类似用户友好品质但功能更多的编辑器可用，称为 _aee_ 。

为了使 _ee_ 正常工作，必须设置环境变量 TERM 来指示正在使用的终端类型。 例如，对于 HP 700/92 终端， TERM 变量应设置为 "70092" 。 如果您需要更多信息，请咨询您的系统管理员。

[选项](#__u9009___u9879_)
-----------------------

命令行提供以下选项：

**\-e**

关闭制表符到空格的扩展。

**\-i**

关闭终端顶部信息窗口的显示。

**\-h**

关闭窗口和菜单边框的突出显示（提高某些终端的性能）。

**+#**

启动时将光标移动到 '#' 行。-

[控制键](#__u63A7___u5236___u952E_)
--------------------------------

要执行插入文本以外的任何操作，用户必须使用控制键（ **Control** 键，由 "^"表示，与字母键一起按下，例如，^a）和键盘上可用的功能键（例如 **Next Page**、 **Prev Page**、 箭头键等）。

由于并非所有终端都具有功能键，因此 _ee_ 具有分配给控制键的基本光标移动功能以及键盘上更直观的键（如果可用）。 例如，要向上移动光标，用户可以使用向上箭头键或 **^u** 。

^a 提示输入要插入的字符的十进制值。 ^b 移动到文本底部。 ^c 获取命令提示符。 ^d 向下移动光标。 ^e 提示输入要搜索的字符串。 ^f 取消删除最后一个删除的字符。 ^g 移动到行首。 ^h 退格。 ^i 制表符。 ^j 插入换行符。 ^k 删除光标所在的字符。 ^l 向左移动光标。 ^m 插入换行符。 ^n 移至下一页。 ^o 移动到行尾。 ^p 移至上一页。 ^r 向右移动光标。 ^t 移动到文本的顶部。 ^u 向上移动光标。 ^v 取消删除最后一个删除的单词。 ^w 删除从光标位置开始的单词。 ^x 搜索。 ^y 从光标位置删除到行尾。 ^z 取消删除最后删除的行。 ^\[ (ESC) 弹出菜单。 

[EMACS 键模式](#EMACS___u952E___u6A21___u5F0F_)
--------------------------------------------

由于许多 shell 提供 Emacs 模式（用于光标移动和其他编辑操作），因此提供了一些可能对熟悉这些绑定的人更有用的绑定。 这些可通过 **settings** 菜单或初始化文件（见下文）访问。 映射如下：

^a 移动到行首。 ^b 后退 1 个字符。 ^c 命令提示符。 ^d 删除光标所在的字符。 ^e 行尾。 ^f 向前 1 个字符。 ^g 返回上一页。 ^h 退格。 ^i 制表符。 ^j 取消删除最后删除的字符。 ^k 删除行。 ^l 取消删除最后删除的行。 ^m 插入换行符。 ^n 移动到下一行。 ^o 提示输入要插入的字符的十进制值。 ^p 上一行。 ^r 恢复最后删除的单词。 ^t 移动到文本的顶部。 ^u 移动到文本的底部。 ^v 移至下一页。 ^w 删除从光标位置开始的单词。 ^y 提示输入要搜索的字符串。 ^z 下一个词。 ^\[ (ESC) 弹出菜单。 

[功能键](#__u529F___u80FD___u952E_)
--------------------------------

**Next Page**

移至下一页。

**Prev Page**

移至上一页。

**Delete Char**

删除光标所在的字符。

**Delete Line**

从光标处删除到行尾。

**Insert line**

在光标位置插入换行符。

**Arrow keys**

沿指示的方向移动光标。

[命令](#__u547D___u4EE4_)
-----------------------

某些操作需要的信息多于单次击键所能提供的信息。 对于最基本的操作，有一个菜单可以通过按 **ESC** 键获得。 通过获取命令提示符 (^c) 并键入以下命令之一，可以执行相同的操作以及更多操作。

!**cmd**

在 shell 中执行 **cmd** 。

**0-9**

移动到指示的行。

**case**

使搜索区分大小写。

**character**

显示光标处字符的 ascii 值。

**exit**

保存编辑的文本，然后离开编辑器。

**expand**

将制表符扩展到空格。

**file**

打印文件名。

**help**

显示帮助屏幕。

**line**

显示当前行号。

**nocase**

使搜索不区分大小写（默认）。

**noexpand**

按下 TAB 键时不要将制表符展开为空格。

**quit**

离开编辑器而不保存更改。

**read** _file_

读取命名 _file_ 。

**write** _file_

将文本写入指定 _file_ 。

[菜单操作](#__u83DC___u5355___u64CD___u4F5C_)
-----------------------------------------

可以通过按 **escape** 键（或 **^\[** 如果没有 **escape** 键）来获得弹出菜单。 在菜单中时，可以使用退出键离开菜单而不进行任何操作。 使用向上和向下箭头键，或 **^u** 向上移动和 **^d** 向下移动以移动到菜单中的所需项目，然后按 **return** 键执行指示的任务。

每个菜单项的左侧是一个字母，如果在键盘上按下相应的字母，则选择该菜单项。

_ee_ 中的主菜单如下：

**leave editor**

如果进行了更改，用户将获得一个菜单，提示是否应保存更改。

**help**

显示一个帮助屏幕，其中包含所有键盘操作和命令。

**file operations**

弹出一个菜单，用于选择是否读取文件、写入文件或保存编辑器的当前内容，以及将编辑器的内容发送到打印命令（参见 **从文件初始化 ee** 部分）。

**redraw screen**

如果屏幕已损坏，则提供一种重新绘制屏幕的方法。

**settings**

显示操作模式的当前值和右边距。 当光标在特定项目上时按回车键，可以更改值。 要离开此菜单，请按 **escape** 键。 （请参阅下面的 **Modes** 。）

**search**

-
弹出一个菜单，用户可以在其中选择输入要搜索的字符串，或者搜索已经输入的字符串。

**miscellaneous**

弹出一个菜单，允许用户设置当前段落的格式、执行 shell 命令或检查编辑器中文本的拼写。

[段落格式](#__u6BB5___u843D___u683C___u5F0F_)
-----------------------------------------

段落由以下文本块为 _ee_ 定义：

*   文件开始或结束。
*   没有字符或只有空格和/或制表符的行。
*   以句点 ('.') 或右尖括号 ('>') 开头的行。

可以通过两种方式格式化段落：通过选择 **format paragraph** 菜单项，或通过设置 _ee_ 来自动格式化段落。 自动模式可以通过菜单设置，也可以通过初始化文件设置。

_ee_ 中的文本操作分为三种状态：自由格式、边距、自动格式化。

"Free-form" 最适合用于编程之类的事情。 对行的长度没有限制，也不会进行格式化。

"Margins" 允许用户输入文本而不必担心超出右边距（右边距可以在 **settings** 菜单中设置，默认为终端的右边距）。 这是允许 **format paragraph** 菜单项工作的模式。

"Automatic formatting" 提供类似文字处理器的行为。 用户可以输入文本，而 _ee_ 将确保每次用户在输入或删除文本后插入空格时，整个段落都适合终端的宽度。 为了进行自动格式化，还必须启用边距观察。

[模式](#__u6A21___u5F0F_)
-----------------------

是一个“无模式”编辑器（它一直处于文本插入模式），但它所做的一些事情还是有模式的。 这些包括：

**tab expansion**

制表符可以作为单个制表符插入，也可以替换为空格。

**case sensitivity**

搜索操作可以对字符是大写还是小写敏感，或者完全忽略大小写。

**margins observed**

线条可以在右边距被截断，也可以永远延伸。

**auto paragraph formatting**

在输入文本时，编辑器可以尝试使其在屏幕宽度内看起来相当不错。

**eightbit characters**

切换八位字符是显示为尖括号中的值（例如 "<220>"）还是字符。

**info window**

可以显示或不显示显示可以执行的键盘操作的窗口。

**emacs keys**

控制键可以被赋予类似于 emacs 的绑定，也可以不被赋予。

**16 bit characters**

切换 16 位字符是作为一个 16 位数量还是两个 8 位数量处理。 这主要适用于中国大 5 代码集。

您可以通过初始化文件（见下文）或菜单（见上文）设置这些模式。

[拼写检查](#__u62FC___u5199___u68C0___u67E5_)
-----------------------------------------

有两种方法可以从 _ee_ 检查文本中的拼写。 一种是使用传统的 _spell_(1) 命令，另一种是使用可选的 _ispell_(1) 命令。

一种是使用传统的 _spell_ 命令，另一种是使用可选的 _ispell_ 命令。 使用拼写，无法识别的单词将被放置在文件的顶部。 对于 _ispell_ 选项，文件被写入磁盘，然后在文件上运行 _ispell_ ，一旦 ispell 完成对文件的更改，文件就会读回。

[打印编辑器的内容](#__u6253___u5370___u7F16___u8F91___u5668___u7684___u5185___u5BB9_)
-----------------------------------------------------------------------------

用户可以选择打印编辑器内容的菜单项。 _ee_ 通过管道将编辑器中的文本传递给初始化命令 **printcommand** 指定的命令（请参阅下面的 **从文件初始化 ee** 部分）。默认是将内容发送到 "lp"。

用户分配给 **printcommand** 的任何内容都必须从标准输入中获取输入。 有关详细信息，请咨询您的系统管理员。

[Shell 操作](#Shell___u64CD___u4F5C_)
-----------------------------------

可以通过在 **miscellaneous** 菜单中选择 **shell command** 项，或通过在 **command:** 提示符下在要执行的命令前放置感叹号（"!"）从 _ee_ 中执行 shell 命令。 此外，用户可以使用左尖括号 (">") 将编辑缓冲区的内容引导到 shell 操作（通过管道），然后使用 "!" 以及要执行的 shell 命令。 shell 操作的输出也可以通过在感叹号前使用右尖括号 ("<") 定向到编辑缓冲区。 这些甚至可以一起用于将输出发送到 shell 操作并将结果读回编辑器。 因此，如果编辑器包含要排序的单词列表，则可以通过在命令提示符下键入以下内容来对它们进行排序：

\><!sort

这会将编辑器的内容通过管道发送到 _sort_ 实用程序，结果将被放置到当前光标位置的编辑缓冲区中。 用户必须删除旧信息。

[从文件初始化 ee](#__u4ECE___u6587___u4EF6___u521D___u59CB___u5316__ee)
-----------------------------------------------------------------

由于不同的用户有不同的偏好， _ee_ 允许一些轻微的可配置性。 ee 的初始化文件有三个可能的位置：文件 _/usr/share/misc/init.ee_ 、用户主目录中的文件 _.init.ee_ 或当前目录中的文件 _.init.ee_ 如果不同于主目录）。 这允许系统管理员在系统范围内为用户设置一些首选项（例如， **print** 命令），并且用户可以自定义特定目录的设置（例如用于通信的目录和用于编程的不同目录）。

首先读取文件 _usr/share/misc/init.ee_ ，然后是 _$HOME/.init.ee_ ，然后是 _.init.ee_ ，其中最近读取的文件指定的设置优先。

在初始化文件中可以输入以下项目：

**case**

将搜索设置为区分大小写。

**nocase**

将搜索设置为不区分大小写（默认）。

**expand**

使 _ee_ 将制表符扩展到空格（默认）。

**noexpand**

使 _ee_ 将制表符作为单个字符插入。

**info**

终端顶部会显示一个小信息窗口（默认）。

**noinfo**

关闭信息窗口的显示。

**margins**

当光标超出用户在插入文本时设置的右边距时，使 _ee_ 截断右边距处的行（默认）。

**nomargins**

允许线条超出右边距。

**autoformat**

导致 _ee_ 在文本插入时自动尝试格式化当前段落。

**noautoformat**

关闭自动段落格式（默认）。

**printcommand**

允许设置打印命令（默认值： "lp")。

**rightmargin**

用户可以为右边距选择一个值（屏幕上的第一列为零）。

**highlight**

打开突出显示信息窗口和菜单的边框（默认）。

**nohighlight**

关闭信息窗口和菜单边框的突出显示。

**eightbit**

打开八位字符的显示。

**noeightbit**

关闭八位字符的显示（它们在尖括号内显示为十进制值，例如 "<220>")。

**16bit**

打开对 16 位字符的处理。

**no16bit**

关闭对 16 位字符的处理。

**emacs**

打开 emacs 键绑定。

**noemacs**

关闭 emacs 键绑定。

[保存编辑器配置](#__u4FDD___u5B58___u7F16___u8F91___u5668___u914D___u7F6E_)
--------------------------------------------------------------------

在 **settings** 菜单中使用此条目时，用户可以选择将编辑器的当前配置（请参阅上面的 **从文件初始化 ee** ）保存到当前目录或用户主目录中名为 _.init.ee_ 的文件中。 如果名为 _.init.ee_ 的文件已经存在，它将被重命名为 _.init.ee.old_ 。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

本材料按“原样”提供。 对本材料不提供任何形式的保证，包括但不限于对适销性和特定用途适用性的默示保证。 Hewlett-Packard 和 Hugh Mahon 均不对此处包含的错误负责，也不对与提供、执行或使用本材料有关的附带或间接损害负责。 Hewlett-Packard 和 Hugh Mahon 均不对本软件或文档的使用或可靠性承担任何责任。 该软件和文档完全不受支持。 没有可用的支持合同。 Hewlett-Packard 未对任何程序或文档进行任何质量保证。 您可能会发现材料的质量不如支持的材料

始终在编辑之前制作不易复制的文件副本。 尽早保存文件，并经常保存。

[国际代码集支持](#__u56FD___u9645___u4EE3___u7801___u96C6___u652F___u6301_)
--------------------------------------------------------------------

_ee_ 支持单字节字符代码集（八位干净），或中文 Big-5 代码集。 （其他多字节代码集也可能起作用，但 Big-5 起作用的原因是一个两字节字符在屏幕上也占据了两列。）

[警告](#__u8B66___u544A_)
=======================

对于较慢的系统，自动段落格式化操作可能太慢。

[文件](#__u6587___u4EF6_)
=======================

_/usr/share/misc/init.ee_-
_$HOME/.init.ee_-
_.init.ee_

[作者](#__u4F5C___u8005_)
=======================

_ee_ 软件由 Hugh Mahon 开发。

本软件和文档包含受版权保护的专有信息。 保留所有权利。

版权所有 (c) 1990, 1991, 1992, 1993, 1995, 1996, 2001 Hugh Mahon.

[参见](#__u53C2___u89C1_)
=======================

termcap(4), terminfo(4), environ(5), spell(1), ispell(1), lp(1), aee(1)