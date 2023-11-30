  READELF(1)  

READELF(1)

FreeBSD General Commands Manual

READELF(1)

[名称](#__u540D___u79F0_)
=======================

`readelf` —

显示有关 ELF 对象的信息

[概要](#__u6982___u8981_)
=======================

`readelf` \[`-a` | `--all`\] \[`-c` | `--archive-index`\] \[`-d` | `--dynamic`\] \[`-e` | `--headers`\] \[`-g` | `--section-groups`\] \[`-h` | `--file-header`\] \[`-l` | `--program-headers`\] \[`-n` | `--notes`\] \[`-p` section | `--string-dump`\=section\] \[`-r` | `--relocs`\] \[`-t` | `--section-details`\] \[`-v` | `--version`\] \[`-w`\[afilmoprsFLR\] | `--debug-dump`\[=long-option-name,...\]\] \[`-x` section | `--hex-dump`\=section\] \[`-z` | `--decompress`\] \[`-A` | `--arch-specific`\] \[`-D` | `--use-dynamic`\] \[`-H` | `--help`\] \[`-I` | `--histogram`\] \[`-N` | `--full-section-name`\] \[`-S` | `--sections` | `--section-headers`\] \[`-V` | `--version-info`\] \[`-W` | `--wide`\] file...

[描述](#__u63CF___u8FF0_)
=======================

`readelf` 实用程序显示有关 ELF 对象和 ar(1) 档案的信息。

`readelf` 实用程序可识别以下选项：

[`-a`](#a) | [`--all`](#-all)

打开以下标志： `-d`, `-h`, `-I`, `-l`, `-r`, `-s`, `-A`, `-S` 和 `-V` 。

[`-c`](#c) | [`--archive-index`](#-archive-index)

打印档案的档案符号表。

[`-d`](#d) | [`--dynamic`](#-dynamic)

打印 ELF 对象中 `SHT_DYNAMIC` 部分的内容。

[`-e`](#e) | [`--headers`](#-headers)

打印 ELF 对象中的所有程序、文件和节标题。

[`-g`](#g) | [`--section-groups`](#-section-groups)

打印 ELF 对象中节组的内容。

[`-h`](#h) | [`--file-header`](#-file-header)

打印 ELF 对象的文件头。

[`-l`](#l) | [`--program-headers`](#-program-headers)

打印对象的程序头表的内容。

[`-n`](#n) | [`--notes`](#-notes)

打印 ELF 对象中存在的 `PT_NOTE` 段或 `SHT_NOTE` 部分的内容。

[`-p`](#p) section | [`--string-dump`](#-string-dump)\=section

将指定部分的内容打印为可打印字符串。 参数 section 应该是节的名称或数字节索引。

[`-r`](#r) | [`--relocs`](#-relocs)

打印重定位信息。

[`-s`](#s) | [`--syms`](#-syms) | [`--symbols`](#-symbols)

打印符号表。

[`-t`](#t) | [`--section-details`](#-section-details)

打印有关节的附加信息，例如节标题中的标志字段。暗示 `-S` 。

[`-v`](#v) | [`--version`](#-version)

打印 `readelf` 的版本标识符并退出。

[`-w`](#w)\[afilmoprsFLR\] | `--debug-dump`\[=long-option-name,...\]

显示 DWARF 信息。 `-w` 选项与下表中的短选项一起使用； `--debug-dump` 选项与相应长选项名称的逗号分隔列表一起使用：

_短选项_

_长选项_

_说明_

a

abbrev

显示缩写信息。

f

frames

显示帧信息，显示帧指令。

i

info

显示调试信息条目。

l

rawline

以原始形式显示行信息。

m

macro

显示宏信息。

o

loc

显示位置列表信息。

p

pubnames

显示全局名称。

r

aranges|ranges

显示地址范围信息。

s

str

显示调试字符串表。

F

frames-interp

显示帧信息，显示寄存器规则。

L

decodedline

以解码的形式显示线路信息。

R

Ranges

显示范围列表。

如果未指定子选项，则默认显示与 a, f, i, l, o, p, r, s 和 R 短选项对应的信息。

[`-x`](#x) section | [`--hex-dump`](#-hex-dump)\=section

以十六进制显示指定节的内容。 参数 section 应该是节的名称或数字节索引。

[`-z`](#z) | [`--decompress`](#-decompress)

在显示之前解压缩由 `-x` 或 `-p` 指定的部分的内容。 如果指定部分未压缩，则按原样显示。

[`-A`](#A) | [`--arch-specific`](#-arch-specific)

此选项已被接受，但当前未实现。

[`-D`](#D) | [`--use-dynamic`](#-use-dynamic)

打印由 “`.dynamic`” 部分中的 `DT_SYMTAB` 条目指定的符号表。

[`-H`](#H) | [`--help`](#-help)

打印帮助信息。

[`-I`](#I) | [`--histogram`](#-histogram)

打印 `SHT_HASH` 和 `SHT_GNU_HASH` 类型部分的桶列表长度信息。

[`-N`](#N) | [`--full-section-name`](#-full-section-name)

此选项已被接受，但当前未实现。

[`-S`](#S) | [`--sections`](#-sections) | [`--section-headers`](#-section-headers)

在每个 ELF 对象的节标题中打印信息。

[`-V`](#V) | [`--version-info`](#-version-info)

打印符号版本信息。

[`-W`](#W) | [`--wide`](#-wide)

每个结构使用一长行打印有关 ELF 结构的信息。 如果未指定此选项， `readelf` 将在两行单独的 64 位 ELF 对象的标头中列出信息。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `readelf` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

nm(1), addr2line(1), elfcopy(1),

[作者](#__u4F5C___u8005_)
=======================

`readelf` 实用程序由 Kai Wang <[kaiwang27@users.sourceforge.net](mailto:kaiwang27@users.sourceforge.net)\> 编写。

October 31, 2020

FreeBSD 13.1-RELEASE