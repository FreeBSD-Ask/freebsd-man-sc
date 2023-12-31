  MTREE(8)  

MTREE(8)

FreeBSD System Manager's Manual

MTREE(8)

[名称](#__u540D___u79F0_)
=======================

`mtree` —

映射目录层次结构

[概要](#__u6982___u8981_)
=======================

`mtree` \[`-bCcDdejLlMnPqrStUuWx`\] \[`-i` | `-m`\] \[`-E` tags\] \[`-F` flavor\] \[`-f` spec\] \[`-I` tags\] \[`-K` keywords\] \[`-k` keywords\] \[`-N` dbdir\] \[`-O` onlyfile\] \[`-p` path\] \[`-R` keywords\] \[`-s` seed\] \[`-X` exclude-file\]

[描述](#__u63CF___u8FF0_)
=======================

`mtree` 实用程序将文件层次结构与规范进行比较，为文件层次结构创建规范，或修改规范。

默认操作（如果没有被命令行选项覆盖）是将当前目录中的文件层次结构与从标准输入读取的规范进行比较。对于特征与规范不匹配或文件层次结构或规范中缺失的任何文件，消息将写入标准输出。

选项如下：

[`-b`](#b)

在进入目录之前和退出目录之后禁止空行。

[`-C`](#C)

将规范转换为更易于使用各种工具解析的格式。 输入规范从标准输入或 `-f` spec 给出的文件中读取。 在输出中，每个文件或目录都用一行表示（可能很长）。 完整的路径名（以 “./” 开头）总是打印为第一个字段； `-K`, `-k` 和 `-R` 可用于控制打印哪些其他关键字； `-E` 和 `-I` 可用于控制打印哪些文件； `-S` 选项可用于对输出进行排序。

[`-c`](#c)

将源自当前工作目录（或 `-p` path 提供的目录）的文件层次结构的规范打印到标准输出。 输出是使用相对路径名的样式。

[`-D`](#D)

根据 `-C`, 除了路径名始终打印为最后一个字段而不是第一个字段。

[`-d`](#d)

忽略除目录类型文件之外的所有内容。

[`-E`](#E) tags

将逗号分隔的标签添加到 “exclusion” 列表中。带有排除列表中标签的非目录不使用 `-C` 和 `-D` 打印。

[`-e`](#e)

不要抱怨文件层次结构中的文件，但规范中没有的文件。

[`-F`](#F) flavor

设置 `mtree` 实用程序的兼容性风格。 flavor 可以是 **mtree**, **freebsd9** 或 **netbsd6** 之一。 默认为 **mtree** 。 **freebsd9** 和 **netbsd6** 版本试图分别保持与 FreeBSD 9.0 和 NetBSD 6.0 的输出兼容性和命令行选项向后兼容性。

[`-f`](#f) spec

从 file 中读取规范，而不是从标准输入中读取。

如果此选项指定了两次，则将两个规范相互比较，而不是与文件层次结构进行比较。 规范将像使用 `-c` 生成的输出一样进行排序。这种情况下的输出格式有点让人联想到 comm(1), 具有“仅在第一个规范中”、“仅在第二个规范中”和“不同”列，分别以零、一个和两个 TAB 字符为前缀。 “不同”列中的每个条目占用两行，一个来自每个规范。

[`-I`](#I) tags

将逗号分隔的标签添加到 “inclusion” 列表中。 包含列表中带有标签的非目录使用 `-C` 和 `-D` 打印。 如果未提供包含列表，则默认显示所有文件。

[`-i`](#i)

如果指定，设置 schg 和/或 sappnd 标志。

[`-j`](#j)

使用 `-c` 选项创建规范时，每次降低目录级别时将输出缩进 4 个空格。 这不会影响 /set 语句或每个目录之前的注释。 但是，它确实会影响每个目录关闭之前的评论。 这相当于 FreeBSD 版本的 `mtree` 中的 `-i` 选项。

[`-K`](#K) keywords

将指定的（空格或逗号分隔）关键字添加到当前关键字集中。 如果指定了 ‘`all`’ ，则添加所有其他关键字。

[`-k`](#k) keywords

使用 **type** 关键字加上指定的（空格或逗号分隔）关键字，而不是当前的一组关键字。 如果指定了 ‘`all`’ ，则使用所有其他关键字。 如果不需要 **type** 关键字，请使用 `-R` type 禁止它。

[`-L`](#L)

遵循文件层次结构中的所有符号链接。

[`-l`](#l)

进行 “loose” 的权限检查，其中更严格的权限将匹配不太严格的权限。 例如，标记为模式 0444 的文件将通过模式 0644 的检查。 “Loose” 检查仅适用于读取、写入和执行权限——特别是，如果在规范或文件中设置了其他位（如粘滞位或 suid/sgid 位），将执行精确检查。 此选项不能与 `-U` 或 `-u` 选项同时设置。

[`-M`](#M)

允许合并具有不同类型的规范条目，最后一个条目优先。

[`-m`](#m)

如果指定了 schg 和/或 sappnd 标志，请重置这些标志。 请注意，这仅适用于安全级别小于 1 的情况（即，在单用户模式下或系统在不安全模式下运行时）。 有关安全级别的信息，请参见 init(8) 。

[`-n`](#n)

创建规范时不要发出路径名注释。 通常，使用 `-c` 选项时，会在每个目录之前和关闭该目录之前发出注释。

[`-N`](#N) dbdir

使用来自 dbdir 的用户数据库文本文件 master.passwd 和组数据库文本文件 group ，而不是使用系统的 getpwnam(3) 和 getgrnam(3) （及相关）库调用的结果。

[`-O`](#O) onlypaths

仅包含此路径名列表中包含的文件。

[`-P`](#P)

不要遵循文件层次结构中的符号链接，而是在任何比较中考虑符号链接本身。 这是默认设置。

[`-p`](#p) path

使用以 path 为根的文件层次结构，而不是当前目录。

[`-q`](#q)

静音模式。 当一个 “missing” 的目录因为它已经存在而无法创建时，不要抱怨。 当目录是符号链接时会发生这种情况。

[`-R`](#R) keywords

从当前关键字集中删除指定的（空格或逗号分隔）关键字。 如果指定了 ‘`all`’ ，则删除所有其他关键字。

[`-r`](#r)

删除文件层次结构中未在规范中描述的任何文件。

[`-S`](#S)

将规范读入内部数据结构时，对条目进行排序。 排序将影响 `-C` 或 `-D` 选项产生的输出的顺序，并且还会影响在根据规范检查目录树时创建或报告缺失条目的顺序。

排序顺序与 `-c` 选项使用的相同，即同一目录中的条目按照 strcmp(3) 使用的顺序排序，只是子目录的条目排在其他条目之后。 默认情况下，如果不使用 `-S` 选项，则将同一目录中的条目收集在一起（与其他目录的条目分开），但不排序。

[`-s`](#s) seed

向标准错误输出显示一个校验和，该校验和代表指定了关键字 **cksum** 的所有文件。 校验和以指定值作为种子。

[`-t`](#t)

修改现有文件的修改时间、设备的设备类型和符号链接目标，以匹配规范。

[`-U`](#U)

与 `-u` 相同，但如果不匹配已被纠正，则不将其视为错误。

[`-u`](#u)

修改现有文件的所有者、组、权限和标志、设备的设备类型和符号链接目标，以匹配规范。 创建任何缺少的目录、设备或符号链接。 必须为要创建的缺失目录指定用户、组和权限。 请注意，除非给出 `-i` 选项，否则不会设置 schg 和 sappnd 标志，即使已指定。 如果给出 `-m` ，这些标志将被重置。 成功时退出状态为 0，如果文件层次结构与规范不匹配，则为 2，如果发生任何其他错误，则为 1。

[`-W`](#W)

在创建新目录或更改现有条目时，不要尝试设置各种文件属性，例如所有权、模式、标志或时间。 此选项在与 `-U` 或 `-u` 结合使用时最有用。

[`-X`](#X) exclude-file

指定的文件包含 fnmatch(3) 模式匹配要从规范中排除的文件，一个到一行。 如果模式包含 ‘`/`’ 字符，它将与整个路径名匹配（相对于起始目录）；否则，它将仅与基本名称匹配。 exclude-list 文件中允许注释。

[`-x`](#x)

不要下降到文件层次结构中的挂载点以下。

规范主要由 “keywords” 组成，即指定与文件相关的值的字符串。 没有关键字具有默认值，如果关键字没有设置值，则不会执行基于它的检查。

目前支持的关键字如下：

**cksum**

使用 cksum(1) 实用程序指定的默认算法的文件校验和。

**device**

用于 **block** 或 **char** 文件类型的设备号。 参数必须是以下形式之一：

format,major,minor

具有 major 和 minor 字段的设备，用于以 format 指定的操作系统。 请参阅下面的有效格式。

format,major,unit,subunit

具有 major, unit 和 subunit 字段的设备，用于以 format 指定的操作系统。（目前只有 **bsdos** 格式支持。）

number

不透明数字（存储在文件系统上）。

可以识别以下 format 值： **native**, **386bsd**, **4bsd**, **bsdos**, **freebsd**, **hpux**, **isc**, **linux**, **netbsd**, **osf1**, **sco**, **solaris**, **sunos**, **svr3**, **svr4**, 和 **ultrix。**

有关详细信息，请参阅 mknod(8) 。

**flags**

文件标记为符号名称。 有关这些名称的信息，请参见 chflags(1) 。 如果不设置标志，则可以使用字符串 ‘`none`’ 覆盖当前默认值。 请注意， schg 和 sappnd 标志被特殊处理（请参阅 `-i` 和 `-m` 选项）。

**ignore**

忽略此文件下的任何文件层次结构。

**gid**

作为数值的文件组。

**gname**

文件组作为符号名。

**link**

符号链接应该引用的文件。

**md5**

文件的 MD5 加密消息摘要。

**md5digest**

**md5**-
的同义词。

**mode**

当前文件的权限为数字（八进制）或符号值。

**nlink**

文件预期具有的硬链接数。

**nochange**

确保此文件或目录存在，否则忽略所有属性。

**optional**

该文件是可选的；如果文件不在文件层次结构中，请不要抱怨文件。

**ripemd160digest**

**rmd160** 的同义词。

**rmd160**

文件的 RMD-160 加密消息摘要。

**rmd160digest**

**rmd160** 的同义词。

**sha1**

文件的 SHA-1 加密消息摘要。

**sha1digest**

**sha1** 的同义词。

**sha256**

文件的 256 位 SHA-2 加密消息摘要。

**sha256digest**

**sha256** 的同义词。

**sha384**

文件的 384 位 SHA-2 加密消息摘要。

**sha384digest**

**sha384** 的同义词。

**sha512**

文件的 512 位 SHA-2 加密消息摘要。

**sha512digest**

**sha512** 的同义词。

**size**

文件的大小（以字节为单位）。

**tags**

要与 `-E` 和 `-I` 匹配的逗号分隔标记。 这些可以在没有前导或尾随逗号的情况下指定，但将与它们一起存储在内部。

**time**

文件的最后修改时间，以秒和纳秒为单位。 该值应包含句点字符和句点后的九位数字。

**type**

文件的类型；可以设置为以下任何一项：

**block**

块特殊装置

**char**

字符特殊装置

**dir**

目录

**fifo**

先进先出

**file**

常规文件

**link**

符号链接

**socket**

socket

**uid**

文件所有者作为数值。

**uname**

文件所有者作为符号名称。

默认的关键字集是 **flags**, **gid**, **link**, **mode**, **nlink**, **size**, **time**, **type** 和 **uid** 。

规范中有四种类型的行：

1.  为关键字设置全局值。 这由字符串 ‘`/set`’ 后跟空格组成，然后是关键字/值对集，以空格分隔。 关键字/值对包含一个关键字，后跟一个等号 (‘`=`’), 然后是一个值，没有空格字符。 设置关键字后，其值将保持不变，直到重置或取消设置。
2.  取消设置关键字的全局值。 这包括字符串 ‘`/unset`’, 后跟空格，后跟一个或多个关键字，用空格分隔。 如果指定了 ‘`all`’ ，则取消设置所有关键字。
3.  文件规范，由路径名、后跟空格、零个或多个空格分隔的关键字/值对组成。
    
    路径名前面可以有空格字符。 路径名可以包含任何标准路径名匹配字符 (‘`[`’, ‘`]`’, ‘`?`’ 或 ‘`*`’), 在这种情况下，层次结构中的文件将与它们匹配的第一个模式相关联。 `mtree` 使用 strsvis(3) （以 VIS\_CSTYLE 格式）对包含不可打印字符的路径名进行编码。 空白字符编码为 ‘`\s`’ (空格), ‘`\t`’ (制表符)和 ‘`\n`’ (换行符)。 路径名称中的 ‘`#`’ 字符由前面的反斜杠 ‘`\`’ 转义，以将它们与注释区分开来。
    
    每个关键字/值对都包含一个关键字，后跟一个等号 (‘`=`’), 然后是关键字的值，没有空格字符。 这些值会覆盖而不更改相应关键字的全局值。
    
    列出的第一个路径名条目必须是名为 ‘`.`’ 的目录，因为这样可以确保混合完整路径名和相对路径名能够始终如一且正确地工作。 名为 ‘`.`’ 的目录的多个条目 被允许；最后一个此类条目的设置会覆盖现有条目的设置。
    
    包含不是第一个字符的斜杠 (‘`/`’) 的路径名将被视为完整路径（相对于树的根）。 路径名中引用的所有父目录都必须存在。 相对路径名使用的当前目录路径将适当更新。 如果类型相同，则允许同一完整路径的多个条目（除非给出 `-M` ，在这种情况下类型可能不同）；在这种情况下，最后一个条目的设置优先。
    
    不包含斜杠的路径名将被视为相对路径。 指定目录将导致在该目录层次结构中搜索后续文件。
    
4.  仅包含字符串 ‘`..`’ 的行，它导致当前目录路径（由相对路径使用）提升一级。

空行和第一个非空白字符是井号 (‘`#`’) 的行将被忽略。

`mtree` 实用程序在成功时退出，状态为 0，如果发生任何错误，则返回 1，如果文件层次结构与规范不匹配，则返回 2。

[文件](#__u6587___u4EF6_)
=======================

/etc/mtree

系统规范目录

[实例](#__u5B9E___u4F8B_)
=======================

要检测已被 “trojan horsed” 攻击的系统二进制文件，建议在文件系统上运行 `mtree` ，并将结果的副本存储在不同的机器上，或者至少以加密形式存储。 `-s` 选项的种子不应该是一个明显的值，并且最终校验和在任何情况下都不应该在线存储！然后，应定期根据在线规范运行 `mtree` ，并将最终校验和与之前的值进行比较。 虽然坏人可以更改在线规范以符合他们修改后的二进制文件，但他们不应该使其产生相同的最终校验和值。 如果最终校验和值发生变化，则可以使用规范的离线副本来检测哪些二进制文件实际上已被修改。

`-d` 选项可以与 `-U` 或 `-u` 结合使用来创建目录层次结构，例如，分发。

[兼容性](#__u517C___u5BB9___u6027_)
================================

`-F` 选项提供的兼容性填充程序在设计上是不完整的。 已知限制如下所述。

**freebsd9** 风格保留了对 **uname** 和 **group** 关键字查找失败的默认处理，方法是将它们替换为适当的 **uid** 和 **gid** 关键字，而不是失败并报告错误。 相关的 `-w` 标志是一个无操作，而不是导致打印警告并且不发出任何关键字。 后一种行为没有被模拟，因为它在面对 /set 语句时具有潜在的危险。

**netbsd6** 风格不会复制将时间报告为 seconds.nanoseconds 的历史错误，而零填充纳秒值小于 100000000。

[参见](#__u53C2___u89C1_)
=======================

chflags(1), chgrp(1), chmod(1), cksum(1), stat(2), fnmatch(3), fts(3), strsvis(3), mtree(5), chown(8), mknod(8)

[历史](#__u5386___u53F2_)
=======================

`mtree` 实用程序出现在 4.3BSD-Reno 中。 **optional** 关键字出现在 NetBSD 1.2 中。 `-U` 选项出现在 NetBSD 1.3 中。 **flags** 和 **md5** 关键字，以及 `-i` 和 `-m` 选项出现在 NetBSD 1.4 中。 **device**, **rmd160**, **sha1**, **tags**, 和 **all** 关键字, `-D`, `-E`, `-I`, `-L`, `-l`, `-N`, `-P`, `-R`, `-W`, 和 `-X` 选项，并支持完整路径出现在 NetBSD 1.6 中。 **sha256**, **sha384** 和 **sha512** 关键字出现在 NetBSD 3.0 中。 `-S` 选项出现在 NetBSD 6.0 中。

February 3, 2013

FreeBSD 13.1-RELEASE