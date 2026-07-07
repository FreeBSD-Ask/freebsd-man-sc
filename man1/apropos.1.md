# apropos(1)

`apropos` — 搜索手册页数据库

## 名称

`apropos`, `whatis`

## 概要

`whatis [-afk] [-C file] [-M path] [-m path] [-O outkey] [-S arch] [-s section] expression ...`

## 描述

`apropos` 和 `whatis` 实用程序查询由 makewhatis(8) 生成的手册页数据库，对每个数据库中的每个文件求值 `expression`。默认情况下，它们显示所有匹配手册的名称、章节号和描述行。

默认情况下，`whatis` 在 [man(1)](man.1.md) 规定的默认路径中搜索 makewhatis(8) 数据库，并在手册名称和描述（`Nm` 和 `Nd` 宏键）上使用不区分大小写的扩展正则表达式匹配。多个词之间隐含按 `-o`（或）组合。

`whatis` 是 `whatis` `-f` 的同义词。

选项如下：

**`-a`** 不只显示标题行，而是显示完整的手册页，如同 [man(1)](man.1.md) `-a` 那样。如果标准输出是终端设备且未指定 `-c`，则使用 [less(1)](less.1.md) 进行分页。在 `-a` 模式下，[mandoc(1)](mandoc.1.md) 手册中描述的 `-IKOTW` 选项也可用。

**`-C`** `file` 指定 man.conf(5) 格式的替代配置 `file`。

**`-f`** 仅在手册页名称中搜索 `expression` 中的所有词。搜索不区分大小写，且仅匹配整个词。在此模式下，宏键、比较运算符和逻辑运算符不可用。

**`-k`** 支持完整的 `expression` 语法。这是 `whatis` 的默认选项。

**`-M`** `path` 使用以冒号分隔的路径替代默认的 makewhatis(8) 数据库搜索路径列表。无效路径或不含手册数据库的路径将被忽略。

**`-m`** `path` 将以冒号分隔的路径前置于 makewhatis(8) 数据库搜索路径列表之前。无效路径或不含手册数据库的路径将被忽略。

**`-O`** `outkey` 显示与键 `outkey` 关联的值，而非手册描述。

**`-S`** `arch` 将搜索限制为指定 machine(1) 架构的页面。`arch` 不区分大小写。默认情况下，显示所有架构的页面。

**`-s`** `section` 将搜索限制为指定的手册章节。默认情况下，显示所有章节的页面。有关章节列表，参见 [man(1)](man.1.md)。

选项 `-chlw` 也受支持，详见 [man(1)](man.1.md) 文档。选项 `-fkl` 互斥，相互覆盖。

`expression` 由搜索项通过逻辑运算符 `-a`（与）和 `-o`（或）连接而成。`-a` 运算符的优先级高于 `-o`，两者均从左到右求值。

**(** `expr` ) 如果子表达式 `expr` 为真则为真。

**`expr1`** `-a` `expr2` 如果 `expr1` 和 `expr2` 均为真则为真（逻辑“与”）。

**`expr1`** [`-o` ]`expr2`] 如果 `expr1` 和/或 `expr2` 为真则为真（逻辑“或”）。

**`term`** 如果 `term` 得到满足则为真。其语法为 [] [`key` [, `key ...`]] (`= | (ti`) ] `val`，其中 `key` 是要查询的 mdoc(7) 宏，`val` 为其值。关于可用键的列表，参见“宏键”小节。运算符 `=` 求值子串，而 `(ti` 求值区分大小写的扩展正则表达式。

**`-i`** `term` 如果 `term` 是正则表达式，则以不区分大小写的方式求值。对子串项无效。

结果首先按章节号以数字升序排序，然后按页面名称以 [ascii(7)](../man7/ascii.7.md) 字母升序排序（不区分大小写）。

每行输出的格式为

> name[, name...](sec) - description

其中“name”为手册名称，“sec”为手册章节，“description”为手册的简短描述。如果为手册指定了架构，则显示为

> name(sec/arch) - description

查询到的手册可通过以下方式访问

```sh
$ man -s sec name
```

如果输出中指定了架构，使用

```sh
$ man -s sec -S arch name
```

### 宏键

查询在由 makewhatis(8) 索引的 mdoc(7) 宏子集上进行求值。除下面列出的宏键外，还可使用特殊键 `any` 匹配任何可用的宏键。

名称和描述：

| `Nm` | 手册名称 |
| --- | --- |
| `Nd` | 单行手册描述 |
| `arch` | 机器架构（不区分大小写） |
| `sec` | 手册章节号 |

章节和交叉引用：

| `Sh` | 章节标题（不包括标准章节） |
| --- | --- |
| `Ss` | 子章节标题 |
| `Xr` | 到其他手册页的交叉引用 |
| `Rs` | 文献引用 |

命令行工具的语义标记：

| `Fl` | 命令行选项（标志） |
| --- | --- |
| `Cm` | 命令修饰符 |
| `Ar` | 命令参数 |
| `Ic` | 内部或交互式命令 |
| `Ev` | 环境变量 |
| `Pa` | 文件系统路径 |

函数库的语义标记：

| `Lb` | 函数库名称 |
| --- | --- |
| `In` | 头文件 |
| `Ft` | 函数返回类型 |
| `Fn` | 函数名 |
| `Fa` | 函数参数类型和名称 |
| `Vt` | 变量类型 |
| `Va` | 变量名 |
| `Dv` | 已定义变量或预处理常量 |
| `Er` | 错误常量 |
| `Ev` | 环境变量 |

其他语义标记：

| `An` | 作者名 |
| --- | --- |
| `Lk` | 超链接 |
| `Mt` | “mailto” |
| `Cd` | 内核配置声明 |
| `Ms` | 数学符号 |
| `Tn` | 商标名 |

物理标记：

| `Em` | 斜体或下划线 |
| --- | --- |
| `Sy` | 粗体 |
| `Li` | 等宽字体 |

文本生成：

| `St` | 标准文档引用 |
| --- | --- |
| `At` | AT&T UNIX 版本引用 |
| `Bx` | BSD 版本引用 |
| `Bsx` | BSD/OS 版本引用 |
| `Nx` | NetBSD 版本引用 |
| `Fx` | FreeBSD 版本引用 |
| `Ox` | OpenBSD 版本引用 |
| `Dx` | Dx 版本引用 |

通常，宏键应能产生完整的结果，无需用户考虑实际的宏用法。例如，结果包括：

**`Fa`** 出现在 `Fn` 行上的函数参数

**`Fn`** 用 `Fo` 宏标记的函数名

**`In`** 用 `Fd` 宏标记的头文件名

**`Vt`** 作为函数返回类型出现的类型，以及出现在 SYNOPSIS 中函数参数里的类型

## 环境变量

**`MANPAGER`** 环境变量 `MANPAGER` 的任何非空值将用于替代标准分页程序 [less(1)](less.1.md)；详见 [man(1)](man.1.md)。仅在指定了 `-a` 或 `-l` 时使用。

**`MANPATH`** 以冒号分隔的目录列表，用于搜索手册页；详见 [man(1)](man.1.md)。被 `-M` 覆盖，在指定 `-l` 时忽略。

**`PAGER`** 指定在未定义 `MANPAGER` 时使用的分页程序。如果 `PAGER` 和 `MANPAGER` 均未定义，则使用 [less(1)](less.1.md)。仅在指定了 `-a` 或 `-l` 时使用。

## 文件

**`mandoc.db`** makewhatis(8) 关键字数据库的名称

**`/etc/man.conf`** 默认的 [man(1)](man.1.md) 配置文件

## 退出状态

`whatis` 实用程序成功时退出码为 0，发生错误时大于 0。

## 实例

在手册名称和描述中搜索子串“.cf”：

```sh
$ apropos =.cf
```

同时包含“.cnf”和“.conf”的匹配：

```sh
$ apropos =.cf =.cnf =.conf
```

使用区分大小写的正则表达式在名称和描述中搜索：

```sh
$ apropos (aq(tiset.?[ug]id(aq
```

搜索给定章节中的所有手册页：

```sh
$ apropos -s 9 .
```

在库章节中搜索同时提及“optind”和“optarg”变量的手册：

```sh
$ apropos -s 3 Va=optind -a Va=optarg
```

与以“ssh”为参数调用 `whatis` 的效果完全相同：

```sh
$ apropos -- -i (aqNm(ti[[:<:]]ssh[[:>:]](aq
```

以下两次调用等价：

> `$ apropos -S` `arch` `-s` `section expression`

> `$ apropos e(` `expression` `e)`
> `-a arch(ti^(``arch``|any)$`
> `-a sec(ti^``section``$`

## 参见

[man(1)](man.1.md), re_format(7), makewhatis(8)

## 标准

`whatis` 实用程序符合 IEEE Std 1003.1-2008 ("POSIX.1") 规范中关于 [man(1)](man.1.md) `-k` 的规定。

所有选项、`whatis` 命令、对逻辑运算符的支持、宏键、子串匹配、结果排序、环境变量 `MANPAGER` 和 `MANPATH`、数据库格式以及配置文件均为该规范的扩展。

## 历史

`whatis` 的部分功能在 1BSD 中已由先前的 `manwhere` 实用程序提供。`manwhere` 和 `whatis` 实用程序首次出现于 2BSD。它们在 OpenBSD 5.6 中被从头重写。

`-M` 选项和 `MANPATH` 变量首次出现于 4.3BSD；`-m` 出现于 4.3BSD；`-C` 出现于 4.4BSD；`-S` 和 `-s` 在 OpenBSD 4.5 中用于 `whatis`，在 OpenBSD 5.6 中用于 `whatis`。选项 `-acfhIKklOTWw` 出现于 OpenBSD 5.7。

## 作者

Bill Joy 于 1977 年编写了 `manwhere`，并于 1979 年 2 月编写了原始的 BSD `manwhere` 和 `whatis`。当前版本由 Kristaps Dzonsons <kristaps@bsd.lv> 和 Ingo Schwarze <schwarze@openbsd.org> 编写。
