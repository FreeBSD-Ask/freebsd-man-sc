# style.Makefile(5)

`style.Makefile` — FreeBSD Makefile 风格指南

## 名称

`style.Makefile`

## 描述

本文件规定了 FreeBSD 源码树中 makefile 的首选风格。

`.include <bsd.prog.mk>`

```sh
SRCS+=<SP>\
<TAB>main.c<SP>\
<TAB>trace.c<SP>\
<TAB>zoo.c \

```

- `.PATH`：如果需要，应放在最前面，写作 “`.PATH: `”，冒号后跟一个 ASCII 空格。不要使用 `VPATH` 变量。
- 特殊变量（即 `LIB`、`SRCS`、`MLINKS` 等）按 “产物”、然后构建和安装二进制文件的顺序排列。特殊变量也可以按 “构建” 顺序排列：即主程序（或库）的变量排在前面。一般的 “产物” 顺序是：`PROG`/[`SH` ]`LIB`/`SCRIPTS`] `FILES` `LINKS` `MAN` `MLINKS` `INCS` `SRCS` `WARNS` `CSTD` `CFLAGS` `DPADD` `LDADD`。一般的 “构建” 顺序是：`PROG`/[`SH` ]`LIB`/`SCRIPTS`] `SRCS` `WARNS` `CSTD` `CFLAGS` `DPADD` `LDADD` `INCS` `FILES` `LINKS` `MAN` `MLINKS`。
- 当只有一个与 `PROG` 同名的源文件时，省略 `SRCS`。
- 当手册页与 `PROG` 同名且位于第 1 节时，省略 `MAN`。
- 所有变量赋值都写作 “`VAR``=`”，即变量名与 `=` 之间没有空格。尽可能保持值按字母顺序排序。
- 变量使用 **{}** 而非 **()** 展开。例如 `${VARIABLE}`。
- 不要使用 `+=` 设置只赋值一次的变量（或首次设置变量）。
- 在简单的 makefile 中不要使用垂直空白，但在更复杂/更长的 makefile 中可以用它来对局部相关的内容分组。
- `WARNS` 位于 `CFLAGS` 之前，因为它基本上是 `CFLAGS` 的修饰符。它放在 `CFLAGS` 之前而不是之后，这样就不会在大量 `CFLAGS` 语句中丢失，因为 `WARNS` 是一项重要的设置。`WARNS` 的用法写作 “`WARNS?= `”，以便可以在命令行或 [make.conf(5)](make.conf.5.md) 中覆盖。
- 不应使用 “`MK_WERROR=no`”，这违背了 `WARNS` 的目的。它只应在命令行中和特殊情况下使用。
- `CFLAGS` 写作 “`CFLAGS+= `”。
- 在 `CFLAGS` 中，`-D` 选项排在 `-I` 选项之前更好，便于字母顺序排列和更容易查看 `-D` 选项。`-D` 选项通常影响条件编译，而 `-I` 选项往往相当长。在 `-D` 选项和 `-I` 选项之间分割过长的 `CFLAGS` 设置。
- 跨越多行的列表应按以下方式格式化：具体而言，列表中的最后一项应带有尾部的 '\'。这是为了避免在末尾追加新项时产生 “假差异” 或 “假追责”。通常，列表应按英语字母顺序排列。库列表或头文件包含路径列表如果为了正确构建所必需，则是显著的例外。
- 不要在 `CFLAGS` 中使用 GCC 特定语法（如 `-g` 和 `-Wall`）。
- 通常，`VAR``=` 与值之间有一个 ASCII 制表符，以便从第 9 列开始放置值。对于超出第 9 列的变量名，允许使用 ASCII 空格。对于非常长的变量名，也允许没有空白字符。
- `.include` bsd.*.mk 放在最后。
- 不要使用过时的语法如 `$<` 和 `$@`。而应使用 `${.IMPSRC}` 或 `${.ALLSRC}` 和 `${.TARGET}`。
- 要不构建基本系统中的 “foo” 部分，使用 `NO_FOO`，而不是 `NOFOO`。
- 要在基本系统中可选地构建某内容，将开关写作 `WITH_FOO`，而不是 `WANT_FOO` 或 `USE_FOO`。后者保留给 FreeBSD Ports Collection 使用。
- 对于仅用 `defined` 函数检查的变量，不要提供任何假值。

## 实例

最简单的程序 `Makefile` 是：

```sh
PROG=	foo
.include <bsd.prog.mk>
```

最简单的库 `Makefile` 是：

```sh
LIB=	foo
SHLIB_MAJOR= 1
MAN=	libfoo.3
SRCS=	foo.c
.include <bsd.lib.mk>
```

## 参见

[make(1)](../man1/make.1.md), [make.conf(5)](make.conf.5.md), [style(9)](../man9/style.9.md)

## 历史

本手册页受 [style(9)](../man9/style.9.md) 手册页启发，首次出现于 FreeBSD 5.1。

## 作者

David O'Brien <deo@NUXI.org>

## 缺陷

这里很少有硬性的风格规则。表达逻辑分组的需要有时意味着不遵守上述某些规则。许多事物的风格过于依赖于整个 makefile 的上下文或其周围的行。
