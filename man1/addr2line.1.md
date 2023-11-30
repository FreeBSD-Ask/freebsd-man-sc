  ADDR2LINE(1)  

ADDR2LINE(1)

FreeBSD General Commands Manual

ADDR2LINE(1)

[命令](#__u547D___u4EE4_)
=======================

`addr2line` —

将程序地址转换为源文件名和行号

[概要](#__u6982___u8981_)
=======================

`addr2line` \[`-a` | `--addresses`\] \[`-b` target | `--target`\=target\] \[`-e` pathname | `--exe`\=pathname\] \[`-f` | `--functions`\] \[`-i` | `--inlines`\] \[`-j` sectionname | `--section`\=sectionname\] \[`-p` | `--pretty-print`\] \[`-s` | `--basename`\] \[`-C` | `--demangle`\] \[`-H` | `--help`\] \[`-V` | `--version`\] \[hexaddress...\]

[描述](#__u63CF___u8FF0_)
=======================

`addr2line` 实用程序将命令行参数 hexaddress 指定的程序地址转换为其相应的源文件名和行号。如果没有给 `addr2line`, 参数，它将从标准输入中读取这些地址。

由参数 hexaddress 指定的程序地址使用 strtoull(3) 接受的约定进行编码。

默认情况下， `addr2line` 将使用可执行文件 “a.out 。” `-e` 选项可用于指定不同的 ELF 对象。

`addr2line` 实用程序可识别以下选项：

[`-a`](#a) | [`--addresses`](#-addresses)

行号信息之前显示地址。

[`-b`](#b) target | [`--target`](#-target)\=target

此选项可被 `addr2line` 识别但被忽略。 支持它是为了与 GNU binutils 兼容。

[`-e`](#e) pathname | [`--exe`](#-exe)\=pathname

使用参数 pathname 指定的 ELF 对象来转换地址。 如果未指定此选项， `addr2line` 将使用文件 “a.out 。”

[`-f`](#f) | [`--functions`](#-functions)

除文件和行号信息外，还显示函数名称。

[`-i`](#i) | [`--inlines`](#-inlines)

如果指定的地址属于内联函数，则还显示其调用者的行号信息，递归直到第一个非内联调用者。

[`-j`](#j) sectionname | [`--section`](#-section)\=sectionname

由参数 hexaddress 指定的值将被视为在名为 sectionname 的部分中的偏移量。

[`-p`](#p) | [`--pretty-print`](#-pretty-print)

以人类可读的方式在一行中显示行号信息。

[`-s`](#s) | [`--basename`](#-basename)

仅显示每个文件名的基本名称。

[`-C`](#C) | [`--demangle`](#-demangle)

去除 C++ 名称。

[`-H`](#H) | [`--help`](#-help)

打印帮助信息。

[`-V`](#V) | [`--version`](#-version)

打印版本标识符并退出。

[输出格式](#__u8F93___u51FA___u683C___u5F0F_)
=========================================

如果未指定 `-f` 选项， `addr2line` 将在单独的行上为每个指定的地址打印文件名和行号。

如果指定 `-f` 选项， `addr2line` 将打印一行，其中包含对应于程序地址 hexaddress 的函数名称，然后是包含文件名和行号的行。

如果指定 `-p` 选项， `addr2line` 将以人类可读的方式在一行上打印行号信息和函数名称。如果还指定 `-i` 选项， `addr2line` 将打印以 “(inlined by) 为前缀的调用函数信息。”

`addr2line` 实用程序使用 “FILENAME:LINENUMBER 格式打印文件名和行号。”

如果无法确定文件或函数名， `addr2line` 将在其位置打印一个问号。如果无法确定行号， `addr2line` 将在其位置打印一个零。

[实例](#__u5B9E___u4F8B_)
=======================

要将默认可执行文件 a.out 中的地址 080483c4 映射到源文件名和行号，请使用：

% addr2line 080483c4

要在可执行的 helloworld 中映射地址 080483c4，请使用：

% addr2line -e helloworld 080483c4

要让 `addr2line` 充当从其标准输入中读取地址的过滤器，请使用：

% addr2line

除了源文件和行号之外，要打印与地址对应的函数名称，请使用：

% addr2line -f 080483c4

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `addr2line` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

nm(1), elfdump(1), elfcopy(1), strtoull(3)

[作者](#__u4F5C___u8005_)
=======================

`addr2line` 实用程序由 Kai Wang 编写 <[kaiwang27@users.sourceforge.net](mailto:kaiwang27@users.sourceforge.net) [。](mailto:。)\>

November 30, 2015

FreeBSD 13.1-RELEASE