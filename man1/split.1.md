  SPLIT(1)  

SPLIT(1)

FreeBSD General Commands Manual

SPLIT(1)

[名称](#__u540D___u79F0_)
=======================

`split` —

将一个文件分成几块

[概要](#__u6982___u8981_)
=======================

`split` `-d` \[`-l` line\_count\] \[`-a` suffix\_length\] \[file \[prefix\]\] `split` `-d` `-b` byte\_count\[`K` | `k` | `M`|`m` | `G` | `g`\] \[`-a` suffix\_length\] \[file \[prefix\]\] `split` `-d` `-n` chunk\_count \[`-a` suffix\_length\] \[file \[prefix\]\] `split` `-d` `-p` pattern \[`-a` suffix\_length\] \[file \[prefix\]\]

[描述](#__u63CF___u8FF0_)
=======================

`split` 实用程序读取给定 file 并将其分解为每个 1000 行的文件（如果未指定选项），保持 file 不变。 如果 file 是单个破折号 (‘`-`’)-
或不存在，则从标准输入 `split` 读取。

选项如下：

[`-a`](#a) suffix\_length

使用 suffix\_length 字母组成文件名的后缀。

[`-b`](#b) byte\_count\[`K`|`k`|`M`|`m`|`G`|`g`\]

创建长度为 byte\_count 个字节的拆分文件。 如果将 `k` 或 `K` 附加到数字，则文件将拆分为 byte\_count 千字节块。 如果将 `m` 或 `M`-
附加到数字，则文件将拆分为 byte\_count 兆字节块。 如果将 `g` 或 `G`-
附加到数字，则文件将拆分为 byte\_count 千兆字节块。

[`-d`](#d)

使用数字后缀而不是字母后缀。

[`-l`](#l) line\_count

创建拆分文件 line\_count 行的长度。

[`-n`](#n) chunk\_count

将文件拆分为 chunk\_count 个文件的大小为 file 大小 / chunk\_count ) ，最后一个文件将包含剩余字节。

[`-p`](#p) pattern

每当输入行匹配 pattern 时，文件就会被拆分，模式被解释为扩展的正则表达式。 匹配的行将是下一个输出文件的第一行。 此选项与 `-b` 和 `-l` 选项不兼容。

如果指定了其他参数，则第一个参数用作要拆分的输入文件的名称。 如果指定了第二个附加参数，它将用作文件被拆分成的文件名的前缀。 在这种情况下，文件被拆分成的每个文件都由前缀命名，后跟使用 suffix\_length 范围 “`a`\-`z`” 中的字符的词法排序后缀。 如果未指定 `-a` ，则使用两个字母作为后缀。

如果未指定 prefix 参数，则文件将按词法排序文件以前缀 “`x`” 命名，后缀如上。

[环境](#__u73AF___u5883_)
=======================

`LANG`, `LC_ALL`, `LC_CTYPE` 和 `LC_COLLATE` 环境变量会影响 `split` 的执行，如 environ(7) 中所述。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `split` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

根据需要将输入拆分为多个文件，以便每个文件最多包含 2 行：

$ echo -e "first line\\nsecond line\\nthird line\\nforth line" | split -l2 

使用文件名的数字前缀将输入拆分为 10 个字节的块。 这将生成两个 10 字节的文件（x00 和 x01）和第三个文件（x02），剩余 2 个字节：

$ echo -e "This is 22 bytes long" | split -d -b10 

拆分输入生成 6 个文件：

echo -e "This is 22 bytes long" | split -n 6 

每次一行匹配正则表达式 “t” 后跟 “a” 或 “u” 时，拆分输入创建一个新文件，从而创建两个文件：

$ echo -e "stack\\nstock\\nstuck\\nanother line" | split -p 't\[au\]' 

[参见](#__u53C2___u89C1_)
=======================

csplit(1), re\_format(7)

[标准](#__u6807___u51C6_)
=======================

`split` 实用程序符合 IEEE Std 1003.1-2001 (“POSIX.1”) 。

[历史](#__u5386___u53F2_)
=======================

A `split` 命令出现在 Version 3 AT&T UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

匹配模式的最大行长度为 65536。

May 9, 2013

FreeBSD 13.1-RELEASE