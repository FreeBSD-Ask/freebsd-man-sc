  STAT(1)  

STAT(1)

FreeBSD General Commands Manual

STAT(1)

[名称](#__u540D___u79F0_)
=======================

`stat`, `readlink` —

显示文件状态

[概要](#__u6982___u8981_)
=======================

`stat` \[`-FHLnq`\] \[`-f` format | `-l` | `-r` | `-s` | `-x`\] \[`-t` timefmt\] \[file ...\] `readlink` \[`-fn`\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`stat` 实用程序显示有关 file 指向的文件的信息。 指定文件的读、写或执行权限不是必需的，但指向该文件的路径名中列出的所有目录都必须是可搜索的。 如果没有给出参数， `stat` 显示有关标准输入的文件描述符的信息。

当作为 `readlink` 调用时，只打印符号链接的目标。 如果给定的参数不是符号链接并且未指定 `-f` 选项，则 `readlink` 将不打印任何内容并退出并出现错误。 如果指定了 `-f` 选项，则通过递归跟踪给定路径的每个组件中的每个符号链接来规范化输出。 `readlink` 将解析绝对路径和相对路径，并返回 file 对应的绝对路径名。 在这种情况下，参数不需要是符号链接。

显示的信息是通过使用给定参数调用 lstat(2) 并评估返回的结构来获得的。 默认格式按顺序显示 st\_dev, st\_ino, st\_mode, st\_nlink, st\_uid, st\_gid, st\_rdev, st\_size, st\_atime, st\_mtime, st\_ctime, st\_birthtime, st\_blksize, st\_blocks, 和 st\_flags 字段。

选项如下：

[`-F`](#F)

与 ls(1) 一样，在每个作为目录的路径名之后立即显示一个斜杠 (‘`/`’) ，在每个可执行文件之后显示一个星号 (‘`*`’) ，在每个符号链接之后显示一个 at 符号 (‘`@`’) ，每个白化后的百分号 (‘`%`’) ，每个套接字后的等号 (‘`=`’) ，每个后的竖线 (‘`|`’) 是 FIFO。 `-F` 的使用意味着 `-l` 。

[`-H`](#H)

将每个参数视为 NFS 文件句柄的十六进制表示，并使用 fhstat(2) 而不是 lstat(2) 。这需要 root 权限。

[`-L`](#L)

使用 stat(2) 代替 lstat(2) 。 `stat` 报告的信息将引用 file 的目标，如果文件是符号链接，而不是 file 本身。 如果链接断开或目标不存在，则返回 lstat(2) 并报告有关链接的信息。

[`-n`](#n)

不要强制在每段输出的末尾出现换行符。

[`-q`](#q)

如果对 stat(2) 或 lstat(2) 的调用失败，则禁止显示失败消息。 当作为 `readlink` 运行时，错误消息会被自动抑制。

[`-f`](#f) format

使用指定格式显示信息。 有关有效格式的说明，请参阅 [格式](#__u683C___u5F0F_) 部分。

[`-l`](#l)

以 `ls` `-lT` 格式显示输出。

[`-r`](#r)

显示原始信息。 也就是说，对于 stat 结构中的所有字段，显示原始的数值（例如，自纪元以来的秒数等）。

[`-s`](#s)

以 “shell output” 格式显示信息，适合初始化变量。

[`-t`](#t) timefmt

使用指定格式显示时间戳。 此格式直接传递给 strftime(3) 。

[`-x`](#x)

以某些 Linux 发行版中已知的更详细的方式显示信息。

[格式](#__u683C___u5F0F_)
-----------------------

格式字符串类似于 printf(3) 格式，它们以 `%` 开头，然后是一系列格式化字符，并以选择要格式化的 struct stat 字段的字符结束。 如果 `%` 后紧跟 `n`, `t`, `%` 或 `@` 之一，则打印换行符、制表符、百分号或当前文件号，否则检查字符串是否有以下内容：

以下任何可选标志：

[`#`](#_)

选择八进制和十六进制输出的替代输出形式。 非零八进制输出将有一个前导零，非零十六进制输出将在其前面加上 “`0x`” 。

[`+`](#+)

断言应始终打印指示数字是正数还是负数的符号。 非负数通常不印有符号。

[`-`](#-)

将字符串输出对齐到字段的左侧，而不是右侧。

[`0`](#0)

将左侧填充的填充字符设置为 ‘`0`’ 字符，而不是空格。

space

在非负符号输出字段的前面保留一个空格。 如果两者都使用，则 ‘`+`’ 会覆盖空格。

然后是以下字段：

size

一个可选的十进制数字字符串，指定最小字段宽度。

prec

由小数点 ‘`.`’ 组成的可选精度。和一个十进制数字字符串，指示最大字符串长度、浮点输出中小数点后出现的位数或数字输出中出现的最小位数。

fmt

可选的输出格式说明符，它是 `D`, `O`, `U`, `X`, `F` 或 `S` 之一。 它们分别代表有符号十进制输出、八进制输出、无符号十进制输出、十六进制输出、浮点输出和字符串输出。 某些输出格式不适用于所有字段。 浮点输出仅适用于 timespec 字段（ `a`, `m` 和 `c` 字段）。

特殊输出说明符 `S` 可用于指示输出（如果适用）应为字符串格式。 可以结合使用：

[`amc`](#amc)

以 strftime(3) 格式显示日期。

[`dr`](#dr)

显示实际设备名称。

[`f`](#f_2)

显示 file 的标志，如 `ls` `-lTdo` 。

[`gu`](#gu)

显示组或用户名。

[`p`](#p)

显示 file 的模式，如 `ls` `-lTd` 。

[`N`](#N)

显示 file 名。

[`T`](#T)

显示 file 的类型。

[`Y`](#Y)

在输出中插入 “ `->` ” 。 请注意， `Y` 的默认输出格式是字符串，但如果明确指定，则这四个字符会被附加。

sub

可选的子字段说明符（高、中、低）。 仅适用于 `p`, `d`, `r` 和 `T` 输出格式。 它可以是以下之一：

[`H`](#H_2)

“High” — 从 `r` 或 `d` 中指定设备的主设备号，从 `p` 的字符串形式中指定权限的 “user” 位，从 `p` 的数字形式中指定文件 “type” 位，以及 `T` 的长输出形式。

[`L`](#L_2)

“Low” — 从 `r` 或 `d` 中指定设备的次要编号，从 `p` 的字符串形式中指定权限的 “other” 位，从 `p` 的数字形式中指定 “user”, “group” 和 “other” 位，和与 `T` 一起使用时文件类型的 `ls` `-F` 样式输出字符（为此使用 `L` 是可选的）。

[`M`](#M)

“Middle” — 指定 `p` 的字符串输出形式的权限的 “group” 位，或数字形式的 `p` 的 “suid”, “sgid” 和 “sticky” 位。

datum

必需的字段说明符，是以下之一：

[`d`](#d)

file 所在的设备 (st\_dev) 。

[`i`](#i)

file 的 inode 编号 (st\_ino) 。

[`p`](#p_2)

文件类型和权限 (st\_mode) 。

[`l`](#l_2)

file 的硬链接数 (st\_nlink) 。

[`u`](#u), `g`

file 所有者的用户 ID 和组 ID (st\_uid, st\_gid) 。

[`r`](#r_2)

字符和块设备特殊文件的设备号 (st\_rdev) 。

[`a`](#a), `m`, `c`, `B`

上次访问或修改 file 的时间，或上次更改 inode 的时间，或 inode 的出生时间 (st\_atime, st\_mtime, st\_ctime, st\_birthtime) 。

[`z`](#z)

以字节为单位的 file 大小 (st\_size) 。

[`b`](#b)

为 file 分配的块数 (st\_blocks) 。

[`k`](#k)

最佳文件系统 I/O 操作块大小 (st\_blksize) 。

[`f`](#f_3)

用户定义的 file 标志。

[`v`](#v)

Inode 代号 (st\_gen) 。

以下五个字段说明符不是直接从 struct stat 中的数据中提取的，而是：

[`N`](#N_2)

文件的名称。

[`R`](#R)

文件对应的绝对路径名。

[`T`](#T_2)

文件类型，如 `ls` `-F` 或如果给定 sub 字段说明符 `H` 则以更具描述性的形式。

[`Y`](#Y_2)

符号链接的目标。

[`Z`](#Z)

从字符或块特殊设备的 rdev 字段扩展为 “major,minor” ，并为所有其他设备提供大小输出。

只有 `%` 和字段说明符是必需的。 大多数字段说明符默认为 `U` 作为输出形式，除了 `p` 默认为 `O`; `a`, `m` 和 `c` 默认为 `D`; ；以及默认为 `S` 的 `Y`, `T` 和 `N` 。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `stat` and `readlink` utilities exit 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

如果未指定选项，则默认格式为 "%d %i %Sp %l %Su %Sg %r %z \\"%Sa\\" \\"%Sm\\" \\"%Sc\\" \\"%SB\\" %k %b %#Xf %N" 。

\> stat /tmp/bar 0 78852 -rw-r--r-- 1 root wheel 0 0 "Jul 8 10:26:03 2004" "Jul 8 10:26:03 2004" "Jul 8 10:28:13 2004" "Jan 1 09:00:00 1970" 16384 0 0 /tmp/bar 

给定一个从 /tmp/foo 指向 / 的符号链接 “foo” ，可以按如下方式使用 `stat` :

\> stat -F /tmp/foo lrwxrwxrwx 1 jschauma cs 1 Apr 24 16:37:28 2002 /tmp/foo@ -> / > stat -LF /tmp/foo drwxr-xr-x 16 root wheel 512 Apr 19 10:57:54 2002 /tmp/foo/ 

要初始化一些 shell 变量，您可以使用 `-s` 标志，如下所示：

\> csh % eval set \`stat -s .cshrc\` % echo $st\_size $st\_mtimespec 1148 1015432481 > sh $ eval $(stat -s .profile) $ echo $st\_size $st\_mtimespec 1148 1015432481 

如果文件是符号链接，为了获取文件类型列表，包括指向的文件，您可以使用以下格式：

$ stat -f "%N: %HT%SY" /tmp/\* /tmp/bar: Symbolic Link -> /tmp/foo /tmp/output25568: Regular File /tmp/blah: Directory /tmp/foo: Symbolic Link -> / 

为了获取设备列表、它们的类型以及主要和次要设备编号，使用制表符和换行符格式化，您可以使用以下格式：

stat -f "Name: %N%n%tType: %HT%n%tMajor: %Hr%n%tMinor: %Lr%n%n" /dev/\* \[...\] Name: /dev/wt8 Type: Block Device Major: 3 Minor: 8 Name: /dev/zero Type: Character Device Major: 2 Minor: 12 

为了单独确定文件上设置的权限，您可以使用以下格式：

\> stat -f "%Sp -> owner=%SHp group=%SMp other=%SLp" . drwxr-xr-x -> owner=rwx group=r-x other=r-x 

为了确定最近修改的三个文件，您可以使用以下格式：

\> stat -f "%m%t%Sm %N" /tmp/\* | sort -rn | head -3 | cut -f2- Apr 25 11:47:00 2002 /tmp/blah Apr 25 10:36:34 2002 /tmp/bar Apr 24 16:47:35 2002 /tmp/foo 

要显示文件的修改时间：

\> stat -f %m /tmp/foo 1177697733 

要以可读格式显示相同的修改时间：

\> stat -f %Sm /tmp/foo Apr 27 11:15:33 2007 

以可读和可排序的格式显示相同的修改时间：

\> stat -f %Sm -t %Y%m%d%H%M%S /tmp/foo 20070427111533 

要在 UTC 中显示相同的内容：

\> sh $ TZ= stat -f %Sm -t %Y%m%d%H%M%S /tmp/foo 20070427181533 

[参见](#__u53C2___u89C1_)
=======================

file(1), ls(1), lstat(2), readlink(2), stat(2), printf(3), strftime(3)

[历史](#__u5386___u53F2_)
=======================

`stat` 实用程序出现在 NetBSD 1.6 和 FreeBSD 4.10 中。

[作者](#__u4F5C___u8005_)
=======================

`stat` 实用程序由 Andrew Brown <[atatat@NetBSD.org](mailto:atatat@NetBSD.org)\> 编写。本手册页由 Jan Schaumann <[jschauma@NetBSD.org](mailto:jschauma@NetBSD.org)\> 编写。

June 22, 2017

FreeBSD 13.1-RELEASE