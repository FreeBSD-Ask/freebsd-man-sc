  LOCATE(1)  

LOCATE(1)

FreeBSD General Commands Manual

LOCATE(1)

[名称](#__u540D___u79F0_)
=======================

`locate` —

快速查找文件名

[概要](#__u6982___u8981_)
=======================

`locate` \[`-0Scims`\] \[`-l` limit\] \[`-d` database\] pattern ...

[描述](#__u63CF___u8FF0_)
=======================

`locate` 程序在数据库中搜索与指定 pattern 匹配的所有路径名。 该数据库会定期（通常是每周或每天）重新计算，并包含所有可公开访问的文件的路径名。

Shell globbing 和引号字符 (“\*”, “?”, “\\”, “\[” 和 “\]”) 可以在 pattern 中使用，尽管它们必须从 shell 中转义。 在任何字符前加上反斜杠 (“\\”) 会消除它可能具有的任何特殊含义。 匹配的不同之处在于必须明确匹配任何字符，包括斜线 (“/”) 。

作为一种特殊情况，不包含通配符 (“foo”)-
的模式被匹配，就好像它是 “\*foo\*” 一样。

从历史上看，仅定位 32 到 127 之间的存储字符。 当前实现存储除换行符 (‘\\n’) 和 `NUL` (‘\\0’) 之外的任何字符。 8 位字符支持不会为纯 ASCII 文件名浪费额外的空间。 小于 32 或大于 127 的字符存储在 2 个字节中。

可以使用以下选项：

[`-0`](#0)

打印由 ASCII `NUL` 字符（字符代码 0）而不是默认 NL（换行符，字符代码 10）分隔的路径名。

[`-S`](#S)

打印一些关于数据库的统计信息并退出。

[`-c`](#c)

抑制正常输出；而是打印匹配文件名的计数。

[`-d`](#d) database

在 database 中搜索而不是在默认文件名数据库中搜索。 允许使用多个 `-d` 选项。 每个附加的 `-d` 选项都会将指定的数据库添加到要搜索的数据库列表中。

选项 database 可以是一个以冒号分隔的数据库列表。 单个冒号是对默认数据库的引用。

$ locate -d $HOME/lib/mydb: foo 

将首先在 $HOME/lib/mydb 中搜索字符串 “foo” ，然后在 /var/db/locate.database 中搜索。

$ locate -d $HOME/lib/mydb::/cdrom/locate.database foo 

将首先在 $HOME/lib/mydb 中搜索字符串 “foo” ，然后在 /var/db/locate.database 中，然后在 /cdrom/locate.database 中。

`$ locate -d db1 -d db2 -d db3 pattern`

与

`$ locate -d db1:db2:db3 pattern`

相同，或

`$ locate -d db1:db2 -d db3 pattern`

如果 `-` 作为数据库名称给出，则将读取标准输入。 例如，您可以压缩数据库并使用：

$ zcat database.gz | locate -d - pattern 

这在具有快速 CPU、少量 RAM 和慢 I/O 的机器上可能很有用。注意：标准输入只能使用 _one_ 模式。

[`-i`](#i)

忽略模式和数据库中的大小写区别。

[`-l`](#l) number

将输出限制为文件名的 number 并退出。

[`-m`](#m)

使用 mmap(2) 代替 stdio(3) 库。 这是默认行为，在大多数情况下速度更快。

[`-s`](#s)

使用 stdio(3) 库而不是 mmap(2) 。

[环境](#__u73AF___u5883_)
=======================

LOCATE\_PATH

如果设置且不为空，则定位数据库的路径，如果指定了 `-d` 选项则忽略。

[文件](#__u6587___u4EF6_)
=======================

/var/db/locate.database

定位数据库

/usr/libexec/locate.updatedb

更新定位数据库的脚本

/etc/periodic/weekly/310.locate

启动数据库重建的脚本

[参见](#__u53C2___u89C1_)
=======================

find(1), whereis(1), which(1), fnmatch(3), locate.updatedb(8) Woods, James A., Finding Files Fast, _;login_, 8:1, pp. 8-10, 1983.

[历史](#__u5386___u53F2_)
=======================

`locate` 命令最早出现在 4.4BSD 中。 FreeBSD 2.2 中添加了许多新功能。

[缺陷](#__u7F3A___u9677_)
=======================

`locate` 程序可能无法列出某些存在的文件，或者可能列出已从系统中删除的文件。 这是因为 locate 只报告数据库中存在的文件，通常每周只由 /etc/periodic/weekly/310.locate 脚本重新生成一次。 使用 find(1) 来定位更临时的文件。

`locate` 数据库通常由用户 “nobody” 构建， locate.updatedb(8) 实用程序会跳过对用户 “nobody” 、组 “nobody” 或 world 不可读的目录。 例如，如果您的 HOME 目录不是世界可读的，那么您的任何文件都 _不_ 在数据库中。

`locate` 数据库不是字节顺序独立的。 不能在不同字节顺序的机器之间共享数据库。 如果两种架构都使用相同的整数大小，则当前的 `locate` 实现以主机字节顺序或网络字节顺序理解数据库。 因此，在 FreeBSD/i386 机器（小端）上，您可以读取建立在 SunOS/sparc 机器（大端，网络）上的定位数据库。

`locate` 实用程序不能识别多字节字符。

December 11, 2020

FreeBSD 13.1-RELEASE