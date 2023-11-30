  APROPOS(1)  

APROPOS(1)

FreeBSD General Commands Manual

APROPOS(1)

[名称](#__u540D___u79F0_)
=======================

`apropos`, `whatis` —

搜索手册页数据库

[概要](#__u6982___u8981_)
=======================

`apropos` \[`-afk`\] \[`-C` file\] \[`-M` path\] \[`-m` path\] \[`-O` outkey\] \[`-S` arch\] \[`-s` section\] expression ...

[描述](#__u63CF___u8FF0_)
=======================

`apropos` 和 `whatis` 实用程序查询由 makewhatis(8) 生成的手册页数据库，评估每个数据库中每个文件的 expression 。 默认情况下，它们显示所有匹配手册的名称、章节编号和描述行。

默认情况下， `apropos` 在 man(1) 规定的默认路径中搜索 makewhatis(8) 数据库，并使用不区分大小写的扩展正则表达式匹配手动名称和描述 (the `Nm` 和 `Nd` 宏键) 。 多个术语意味着成对 `-o` 。

`whatis` 是 `apropos` `-f` 的同义词。

选项如下：

[`-a`](#a)

不是只显示标题行，而是显示完整的手册页，就像 man(1) `-a` 一样。 如果标准输出是终端设备且未指定 `-c` ，则使用 more(1) 对其进行分页。 在 `-a` 模式下， mandoc(1) 手册中描述的选项 `-IKOTW` 也可用。

[`-C`](#C) file

以 man.conf(5) 格式指定替代配置 file 。

[`-f`](#f)

仅在手册页名称中搜索 expression 中的所有单词。 搜索不区分大小写，仅匹配整个单词。 在此模式下，宏键、比较运算符和逻辑运算符不可用。

[`-k`](#k)

支持完整的 expression 语法。 这是 `apropos` 的默认值。

[`-M`](#M) path

使用冒号分隔的路径而不是搜索 makewhatis(8) 数据库的默认路径列表。 无效路径或没有手动数据库的路径将被忽略。

[`-m`](#m) path

将冒号分隔的路径添加到搜索 makewhatis(8) 数据库的路径列表中。 无效路径或没有手动数据库的路径将被忽略。

[`-O`](#O) outkey

显示与键 outkey 关联的值，而不是手动描述。

[`-S`](#S) arch

将搜索限制在指定 machine(1) 架构的页面。 arch 不区分大小写。 默认情况下，会显示所有架构的页面。

[`-s`](#s) section

将搜索限制在手册的指定部分。 默认情况下，显示所有部分的页面。 请参阅 man(1) 以获取部分列表。

选项 `-chlw` 也受支持，并记录在 man(1) 中。 选项 `-fkl` 是互斥的并且相互覆盖。

expression 由逻辑运算符 `-a` (and) 和 `-o` (or) 连接的搜索词组成。 `-a` 运算符优先于 `-o` 并且两者都是从左到右计算的。

( expr )

如果子表达式 expr 为真，则为真。

expr1 `-a` expr2

如果 expr1 和 expr2 都为真（逻辑 ‘and’ ），则为真。

expr1 \[`-o`\] expr2

如果 expr1 和/或 expr2 评估为真（逻辑 ‘or’ ），则为真。

term

如果满足 term ，则为真。 这有语法 \[\[key\[,key...\]\](`=`|`~`)\]val, 其中 key 是要查询的 mdoc(7) 宏， val 是它的值。 有关可用键的列表，请参阅 [宏键](#__u5B8F___u952E_) 。运算符 `=` 计算子字符串，而 `~` 计算区分大小写的扩展正则表达式。

[`-i`](#i) term

如果 term 是正则表达式，则不区分大小写。 对子字符串项没有影响。

结果首先根据节号按数字升序排序，然后按页面名称按 ascii(7) 字母升序排序，不区分大小写。

每个输出行的格式为

name\[, name...\](sec) - description

其中 “name” 是手册的名称， “sec” 是手册部分， “description” 是手册的简短描述。 如果为手册指定了架构，则显示为

name(sec/arch) - description

生成的手册可以以

`$ man -s sec name`

如果在输出中指定了体系结构，请使用

`$ man -s sec -S arch name`

[宏键](#__u5B8F___u952E_)
-----------------------

查询评估由 makewhatis(8) 索引的 mdoc(7) 宏子集。 除了下面列出的宏键之外，特殊键 `any` 可用于匹配任何可用的宏键。

名称和描述：

[`Nm`](#Nm)

手册名称

[`Nd`](#Nd)

单行手册描述

[`arch`](#arch)

机器架构（不区分大小写）

[`sec`](#sec)

手册节号

节和交叉引用：

[`Sh`](#Sh)

节标题（不包括标准节）

[`Ss`](#Ss)

小节标题

[`Xr`](#Xr)

对另一个手册页的交叉引用

[`Rs`](#Rs)

书目参考

命令行实用程序的语义标记：

[`Fl`](#Fl)

命令行选项（标志）

[`Cm`](#Cm)

命令修饰符

[`Ar`](#Ar)

命令参数

[`Ic`](#Ic)

内部或交互式命令

[`Ev`](#Ev)

环境变量

[`Pa`](#Pa)

文件系统路径

函数库的语义标记:

[`Lb`](#Lb)

函数库名称

[`In`](#In)

包含文件

[`Ft`](#Ft)

函数返回类型

[`Fn`](#Fn)

函数名称

[`Fa`](#Fa)

函数参数类型和名称

[`Vt`](#Vt)

变量类型

[`Va`](#Va)

变量名称

[`Dv`](#Dv)

定义变量或预处理器常量

[`Er`](#Er)

错误常量

[`Ev`](#Ev_2)

环境变量

各种语义标记：

[`An`](#An)

作者姓名

[`Lk`](#Lk)

超链接

[`Mt`](#Mt)

“mailto”超链接

[`Cd`](#Cd)

内核配置声明

[`Ms`](#Ms)

数学符号

[`Tn`](#Tn)

商品名

物理标记：

[`Em`](#Em)

斜体或下划线

[`Sy`](#Sy)

粗体字体

[`Li`](#Li)

打字机字体

文本生成：

[`St`](#St)

参考标准文档

[`At`](#At)

AT&T UNIX 版本参考

[`Bx`](#Bx)

BSD 版本参考

[`Bsx`](#Bsx)

BSD/OS 版本参考

[`Nx`](#Nx)

NetBSD 版本参考

[`Fx`](#Fx)

FreeBSD 版本参考

[`Ox`](#Ox)

OpenBSD 版本参考

[`Dx`](#Dx)

DragonFly 版本参考

一般来说，宏键应该产生完整的结果，而不期望用户考虑实际的宏使用。 例如，结果包括：

[`Fa`](#Fa_2)

函数参数出现在 `Fn` 行中

[`Fn`](#Fn_2)

函数名用 `Fo` 宏标记

[`In`](#In_2)

include 文件名用 `Fd` 宏标记

[`Vt`](#Vt_2)

显示为函数返回类型的类型

SYNOPSIS 中函数参数中出现的类型

[环境](#__u73AF___u5883_)
=======================

[`MANPAGER`](#MANPAGER)

使用环境变量 `MANPAGER` 的任何非空值代替标准分页程序， more(1); 有关详细信息，请参见 man(1) 。 仅在指定 `-a` 或 `-l` 时使用。

[`MANPATH`](#MANPATH)

用于搜索手册页的以冒号分隔的目录列表；有关详细信息，请参见 man(1) 。 被 `-M` 覆盖，如果指定了 `-l` ，则忽略。

[`PAGER`](#PAGER)

指定未定义 `MANPAGER` 如果 PAGER 和 MANPAGER 均未定义，则使用 more(1) `-s` 。 仅在指定 `-a` 或 `-l` 时使用。

[文件](#__u6587___u4EF6_)
=======================

mandoc.db

makewhatis(8) 关键字数据库的名称

/etc/man.conf

默认 man(1) 配置文件

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `apropos` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

搜索 “.cf” 作为手册名称和描述的子字符串：

`$ apropos =.cf`

还包括 “.cnf” 和 “.conf” 的匹配项：

`$ apropos =.cf =.cnf =.conf`

使用区分大小写的正则表达式在名称和描述中搜索：

`$ apropos '~set.?[ug]id'`

在提及 “optind” 和 “optarg” 变量的库部分中搜索手册：

`$ apropos -s 3 Va=optind -a Va=optarg`

执行与使用参数 “ssh” 调用 `whatis` 完全相同的操作：

`$ apropos -- -i 'Nm~[[:<:]]ssh[[:>:]]'`

以下两个调用是等效的：

`$ apropos -S` arch `-s` section expression

`$ apropos \(` expression `\)` `-a arch~^(`arch`|any)$` `-a sec~^`section`$`

[参见](#__u53C2___u89C1_)
=======================

man(1), re\_format(7), makewhatis(8)

[标准](#__u6807___u51C6_)
=======================

`apropos` 实用程序符合 man(1) `-k` 的 IEEE Std 1003.1-2008 (“POSIX.1”) 规范。

所有选项、 `whatis` 命令、对逻辑运算符、宏键、子字符串匹配、结果排序、环境变量 `MANPAGER` 和 `MANPATH` 、数据库格式和配置文件的支持都是该规范的扩展。

[历史](#__u5386___u53F2_)
=======================

`whatis` 的部分功能已经由 1BSD 中的前 `manwhere` 实用程序提供。 `apropos` 和 `whatis` 实用程序首先出现在 2BSD 中。 它们是针对 OpenBSD 5.6 从头开始重写的。

`-M` 选项和 `MANPATH` 变量最早出现在 4.3BSD; `-m` 在 4.3BSD-Reno 中； `-C` 在 4.4BSD-Lite1 中；和 `-S` 和 `-s` 在 OpenBSD 4.5 中用于 `apropos` ，在 OpenBSD 5.6 中用于 `whatis` 。 选项 `-acfhIKklOTWw` 出现在 OpenBSD 5.7 中。

[作者](#__u4F5C___u8005_)
=======================

Bill Joy 于 1977 年写了 `manwhere` ，最初的 BSD `apropos` 和 `whatis` 写于 1979 年 2 月。当前版本由 Kristaps Dzonsons <[kristaps@bsd.lv](mailto:kristaps@bsd.lv)\> 和 Ingo Schwarze <[schwarze@openbsd.org](mailto:schwarze@openbsd.org)\> 编写。

November 22, 2018

FreeBSD 13.1-RELEASE