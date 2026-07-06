# style.9

`style` — 内核源文件风格指南

## 描述

本文件指定了 FreeBSD 源码树中内核源文件的首选风格。它也是首选用户态代码风格的指南。首选行宽为 80 个字符，但当稍长的行更清晰或更易读时，会有一些例外。任何经常被 grep 搜索的内容，如诊断、错误或 panic 消息，不应因此规则而跨多行拆分。许多风格规则隐含在示例中。在假设 `style` 对某个问题保持沉默之前，请仔细检查示例。

```sh
/*
 * FreeBSD 风格指南。基于 CSRG 的 KNF（Kernel Normal Form）。
 */
/*
 * 非常重要的单行注释看起来像这样。
 */
/* 大多数单行注释看起来像这样。 */
// 虽然它们可能看起来像这样。
/*
 * 多行注释看起来像这样。把它们写成真正的句子。
 * 填充它们，使其看起来像真正的段落。
 */
```

C++ 注释可用于 C 和 C++ 代码。单行注释在文件内应一致地使用 C 或 C++ 风格。多行注释也应一致地使用 C 或 C++ 风格，但可以与单行注释不同。

版权头部应是如下所示的多行注释：

```sh
/*
 * Copyright (c) 1984-2025 John Q. Public
 *
 * SPDX-License-Identifier: BSD-2-Clause
 */
```

从非第一列开始的注释从不被视为许可证声明。在适当的 SPDX-License-Identifier 之前写版权行。如果版权声明包含"`All Rights Reserved`"短语，它应与"`Copyright`"一词在同一行。不应在旧版权行和此短语之间插入新版权行。相反，应在已有的"`All Rights Reserved`"行之后插入新版权短语。进行更改时，将"`All Rights Reserved`"行与每个"`Copyright`"行折叠是可以接受的。对于"`All Rights Reserved`"行与"`Copyright`"一词在同一行上的文件，新版权声明应最后添加。仅在进行实质性更改时才应添加新的"`Copyright`"行，而不是为琐碎的更改添加。

在任何版权和许可证注释之后，有一个空行。非 C/C++ 源文件遵循上面的示例，而 C/C++ 源文件遵循下面的示例。版本控制系统 ID 标签在文件中只应存在一次（不像本文件）。从其他地方获取的文件中的所有 VCS（版本控制系统）修订标识都应保留，包括在适用的情况下显示文件历史的多个 ID。通常，不要编辑外来的 ID 或其基础设施。除非另有包装（如"`#if defined(LIBC_SCCS)`"），否则将两者都包含在"`#if 0 ... #endif`"中以隐藏任何不可编译的位，并使 ID 不出现在目标文件中。仅在文件被重命名时才在外来 VCS ID 前添加"`From: `"。如果文件派生自另一个 FreeBSD 文件，则添加"`From: `"和 FreeBSD git 哈希及完整路径名，并包含原始文件的相关版权信息。

在头文件之前留一个空行。

内核包含文件（`sys/*.h`）排在最前面。如果需要

```c
#include <sys/types.h>
```

或

```c
#include <sys/param.h>
```

则在其他包含文件之前包含它。（

```c
#include <sys/param.h>
```

包含了

```c
#include <sys/types.h>
```

不要两者都包含。）接下来，如果需要，包含

```c
#include <sys/systm.h>
```

其余的内核头文件应按字母顺序排序。

```sh
#include <sys/types.h>	/* 尖括号中的非本地包含。 */
#include <sys/systm.h>
#include <sys/endian.h>
#include <sys/lock.h>
#include <sys/queue.h>
```

对于网络程序，将网络包含文件放在接下来。

```sh
#include <net/if.h>
#include <net/if_dl.h>
#include <net/route.h>
#include <netinet/in.h>
#include <protocols/rwhod.h>
```

不要在内核中包含 **`/usr/include`** 中的文件。

在下一组之前留一个空行，即 **`/usr/include`** 文件，应按名称字母顺序排序。

```sh
#include <stdio.h>
```

全局路径名定义在

```c
#include <paths.h>
```

程序本地的路径名放在本地目录中 "" `pathnames.h` 的双引号中。

```sh
#include <paths.h>
```

在本地包含文件之前留另一个空行。

```sh
#include "pathnames.h"		/* 双引号中的本地包含。 */
```

除非是实现应用程序接口，否则不要在实现命名空间中 `#define` 或声明名称。

"不安全"宏（有副作用的宏）的名称和用于明显常量的宏名称都使用大写。类表达式的宏的展开要么是单个标记，要么有外层括号。在 `#define` 和宏名称之间放一个空格或制表符，但在文件内保持一致。如果宏是函数的内联展开，函数名全小写，宏同名全大写。右对齐反斜杠；这使阅读更容易。如果宏封装了复合语句，将其包含在 `do` 循环中，以便可以安全地在 `if` 语句中使用。任何最终的语句终止分号应由宏调用提供而不是宏本身，以便于美化打印器和编辑器解析。

```sh
#define	MACRO(x, y) do {						e
	variable = (x) + (y);						e
	(y) += 2;							e
} while (0)
```

当代码使用 `#ifdef` 或 `#if` 条件编译时，可以在匹配的 `#endif` 或 `#else` 之后添加注释，以使读者能够轻松辨别条件编译代码区域的结束。此注释仅应用于（主观上）较长的区域、大于 20 行的区域，或一系列嵌套的 `#ifdef` 可能令读者困惑的地方。注释应与 `#endif` 或 `#else` 用单个空格分隔。对于较短的条件编译区域，不应使用结束注释。

`#endif` 的注释应匹配相应 `#if` 或 `#ifdef` 中使用的表达式。`#else` 和 `#elif` 的注释应匹配前面 `#if` 和/或 `#elif` 语句中使用的表达式的逆。在注释中，子表达式"`defined(FOO)`"缩写为"`FOO`"。就注释而言，"`#ifndef` `FOO`"被视为"`#if` `!defined(FOO)`"。

```sh
#ifdef KTRACE
#include <sys/ktrace.h>
#endif
#ifdef COMPAT_43
/* 这里是一个大区域，或其他条件代码。 */
#else /* !COMPAT_43 */
/* 或者这里。 */
#endif /* COMPAT_43 */
#ifndef COMPAT_43
/* 这里是另一个大区域，或其他条件代码。 */
#else /* COMPAT_43 */
/* 或者这里。 */
#endif /* !COMPAT_43 */
```

项目偏好使用 ISO/IEC 9899:1999（"ISO C99"）形式的 `uintXX_t` 无符号整数标识符，而不是旧 BSD 风格的 `u_intXX_t` 形式的整数标识符。新代码应使用前者，如果在该区域正在进行其他重大工作且没有优先选择旧 BSD 风格的压倒性理由，旧代码应转换为新形式。与空白提交一样，应注意仅进行 `uintXX_t` 转换的提交。

类似地，项目偏好使用 ISO C99 的 `bool` 而不是旧的 `int` 或 `boolean_t`。新代码应使用 `bool`，旧代码在合理的情况下可以转换。字面值命名为 `true` 和 `false`。这些比旧拼写 `TRUE` 和 `FALSE` 更受偏好。用户态代码应包含

```c
#include <stdbool.h>
```

而内核代码应包含

```c
#include <sys/types.h>
```

同样，项目在有意义时偏好使用 ISO C99 指定初始化器。

枚举值全部大写。

```sh
enum enumtype { ONE, TWO } et;
```

在标识符中偏好使用内部下划线而不是 camelCase 或 TitleCase。

在声明中，不要在星号和相邻标记之间放置任何空白，但与类型相关的标记除外。（这些标记是基本类型的名称、类型限定符和除正在声明的 `typedef` 名称以外的 `typedef` 名称。）使用单个空格将这些标识符与星号分隔。

在结构中声明变量时，按用途排序，然后按大小（从大到小），再按字母顺序声明它们。第一个类别通常不适用，但也有例外。每个变量占一行。尝试使用一个或两个制表符（根据你的判断）对齐成员名称，使结构可读。仅当用一个制表符足以对齐至少 90% 的成员名称时才应使用一个制表符。跟随极长类型的名称应用单个空格分隔。

主要结构应在其使用的文件顶部声明，或者在多个源文件中使用时放在单独的头文件中。结构的使用应通过单独的声明，如果在头文件中声明则应为 `extern`。

```sh
struct foo {
	struct foo	*next;		/* 活动 foo 的列表。 */
	struct mumble	amumble;	/* mumble 的注释。 */
	int		bar;		/* 尝试对齐注释。 */
	struct verylongtypename *baz;	/* 不适合 2 个制表符。 */
};
struct foo *foohead;			/* 全局 foo 列表的头。 */
```

尽可能使用 [queue(3)](../man3/queue.3.md) 宏而不是自己编写列表。因此，前面的示例最好写成：

```sh
#include <sys/queue.h>
struct foo {
	LIST_ENTRY(foo)	link;		/* 对 foo 列表使用队列宏。 */
	struct mumble	amumble;	/* mumble 的注释。 */
	int		bar;		/* 尝试对齐注释。 */
	struct verylongtypename *baz;	/* 不适合 2 个制表符。 */
};
LIST_HEAD(, foo) foohead;		/* 全局 foo 列表的头。 */
```

避免对结构类型使用 typedef。typedef 有问题，因为它们不能正确隐藏其底层类型；例如你需要知道 typedef 是结构本身还是指向结构的指针。此外，它们必须声明一次，而不完整的结构类型可以根据需要多次提及。typedef 在独立头文件中难以使用：定义 typedef 的头文件必须在使用它的头文件之前包含，或者由使用它的头文件包含（这会导致命名空间污染），或者必须有获取 typedef 的后门机制。

当约定需要 `typedef` 时，使其名称与结构标签匹配。避免以"`_t`"结尾的 typedef，除非 Standard C 或 POSIX 指定。

```sh
/* 使结构名称匹配 typedef。 */
typedef	struct bar {
	int	level;
} BAR;
typedef	int		foo;		/* 这是 foo。 */
typedef	const long	baz;		/* 这是 baz。 */
```

所有函数都在某处有原型。

私有函数（即不在其他地方使用的函数）的函数原型放在第一个源模块的顶部。一个源模块本地的函数应声明为 `static`。

从内核其他部分使用的函数在相关的包含文件中有原型。函数原型应按逻辑顺序列出，最好按字母顺序，除非有令人信服的理由使用不同的顺序。

在多个模块中本地使用的函数放在单独的头文件中，例如 "" `extern.h`。

内核有与参数类型关联的名称，例如，在内核中使用：

```sh
void	function(int fd);
```

在对用户态应用程序可见的头文件中，可见的原型必须使用"受保护"的名称（以下划线开头的名称）或使用不带名称的类型。优先使用受保护的名称。例如，使用：

```sh
void	function(int);
```

或：

```sh
void	function(int _fd);
```

原型在制表符后可以有额外的空格，以使函数名称对齐：

```sh
static char	*function(int _arg, const char *_arg2, struct foo *_arg3,
		    struct bar *_arg4);
static void	 usage(void);
/*
 * 所有主要例程都应有注释，简要描述它们做什么。
 * "main" 例程之前的注释应描述程序做什么。
 */
int
main(int argc, char *argv[])
{
	char *ep;
	long num;
	int ch;
```

为保持一致性，应使用 getopt(3) 解析选项。选项应在 getopt(3) 调用和 `switch` 语句中排序，除非 `switch` 的部分级联。`switch` 语句中执行一些代码然后级联到下一个 case 的元素应有 `FALLTHROUGH` 注释。数值参数应检查准确性。由于非显而易见的原因不可达的代码可以标记 /* `NOTREACHED` */。

```sh
	while ((ch = getopt(argc, argv, "abNn:")) != -1)
		switch (ch) {		/* 缩进 switch。 */
		case 'a':		/* 不缩进 case。 */
			aflag = 1;	/* case 体缩进一个制表符。 */
			/* FALLTHROUGH */
		case 'b':
			bflag = 1;
			break;
		case 'N':
			Nflag = 1;
			break;
		case 'n':
			num = strtol(optarg, &ep, 10);
			if (num <= 0 || *ep != 'e0') {
				warnx("illegal number, -n argument -- %s",
				    optarg);
				usage();
			}
			break;
		case '?':
		default:
			usage();
		}
	argc -= optind;
	argv += optind;
```

关键字（`if`、`while`、`for`、`return`、`switch`）后加空格。单行语句允许两种花括号（`{` 和 `}`）风格。要么用于所有单语句，要么仅在需要清晰度时使用。函数内的使用应一致。无限循环使用 `for` 而不是 `while`。

```sh
	for (p = buf; *p != 'e0'; ++p)
		;	/* nothing */
	for (;;)
		stmt;
	for (;;) {
		z = a + really + long + statement + that + needs +
		    two + lines + gets + indented + four + spaces +
		    on + the + second + and + subsequent + lines;
	}
	for (;;) {
		if (cond)
			stmt;
	}
	if (val != NULL)
		val = realloc(val, newsize);
```

`for` 循环的某些部分可以留空。

```sh
	for (; cnt < 15; cnt++) {
		stmt1;
		stmt2;
	}
```

`for` 循环可以声明并初始化其计数变量。

```sh
	for (int i = 0; i < 15; i++) {
		stmt1;
	}
```

缩进是 8 字符制表符。第二级缩进是四个空格。如果必须换行长语句，将运算符放在行尾。

```sh
	while (cnt < 20 && this_variable_name_is_too_long &&
	    ep != NULL)
		z = a + really + long + statement + that + needs +
		    two + lines + gets + indented + four + spaces +
		    on + the + second + and + subsequent + lines;
```

不要在行尾添加空白，仅使用制表符后跟空格来形成缩进。不要使用比制表符产生的更多空格，也不要在制表符前使用空格。

闭合和开花括号与 `else` 在同一行。不必要的花括号可以省略。

```sh
	if (test)
		stmt;
	else if (bar) {
		stmt;
		stmt;
	} else
		stmt;
```

函数名后无空格。逗号后有空格。`(` 或 `[` 后无空格，`]` 或 `)` 前无空格。

```sh
	error = function(a1, a2);
	if (error != 0)
		exit(error);
```

一元运算符不需要空格，二元运算符需要。除非为了优先级需要或语句没有它们会令人困惑，否则不要使用括号。记住其他人可能比你更容易困惑。你理解以下内容吗？

```sh
	a = b->c[0] + ~d == (e || f) || g && h ? i : j >> 1;
	k = !(l & FLAGS);
```

退出应在成功时为 0，失败时为 1。

```sh
	exit(0);	/*
			 * 避免明显的注释，如
			 * "成功时退出 0。"
			 */
}
```

函数类型应单独一行，位于函数之前。函数体的开花括号应单独一行。

```sh
static char *
function(int a1, int a2, float fl, int a4, struct bar *bar)
{
```

在函数中声明变量时，按大小排序，然后按字母顺序；每行多个可以。如果行溢出，重用类型关键字。变量可以在声明时初始化，特别是当它们在作用域的其余部分是常量时。声明可以在任何块中，但必须放在语句之前。初始化变量时应避免调用复杂函数。

```sh
	struct foo one, *two;
	struct baz *three = bar_get_baz(bar);
	double four;
	int *five, six;
	char *seven, eight, nine, ten, eleven, twelve;
	four = my_complicated_function(a1, f1, a4);
```

不要在其他函数内声明函数；ANSI C 说此类声明具有文件作用域，无论声明的嵌套如何。在看似本地作用域中隐藏文件声明是不可取的，会引起好的编译器的投诉。

类型转换和 `sizeof` 后不跟空格。`sizeof` 总是带括号编写。冗余括号规则不适用于 `sizeof var` 实例。

`NULL` 是首选的空指针常量。在编译器知道类型的上下文中（例如在赋值中），使用 `NULL` 而不是 `(type *)0` 或 `(type *)NULL`。在其他上下文中，特别是对于所有函数参数，使用 `(type *)NULL`。（对于可变参数，类型转换是必需的，如果函数原型可能不在作用域内，对于其他参数也是必需的。）用 `NULL` 测试指针，例如，使用：

```sh
(p = f()) == NULL
```

而不是：

```sh
!(p = f())
```

不要在没有比较的情况下测试，或使用一元 `!`（布尔值除外）。例如，使用：

```sh
if (*p == 'e0')
```

而不是：

```sh
if (!*p)
```

偏好：

```sh
if (count != 0)
```

而不是：

```sh
if (count)
```

返回 `void *` 的例程不应将其返回值转换为任何指针类型。

`return` 语句中的值应括在括号中。

使用 err(3) 或 warn(3)，不要自己编写。

```sh
	if ((four = malloc(sizeof(struct foo))) == NULL)
		err(1, (char *)NULL);
	if ((six = (int *)overflow()) == NULL)
		errx(1, "number overflowed");
	return (eight);
}
```

不要使用 K&R 风格的声明或定义，它们已过时，在 C23 中被禁止。编译器会警告它们的使用，一些默认将它们视为错误。将 K&R 风格定义转换为 ANSI 风格时，保留关于参数的任何注释。

长参数列表使用正常的四空格缩进换行。

可变数量参数应如下所示：

```sh
#include <stdarg.h>
void
vaf(const char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);
	STUFF;
	va_end(ap);
	/* void 函数不需要返回。 */
}
static void
usage(void)
{
```

函数应先有局部变量声明，后跟一个空行，然后是第一条语句。如果没有声明局部变量，第一行应为语句。旧版本的此 `style` 文档要求代码前有空行。在对代码进行重大更改时，应删除此类行。

使用 printf(3)，而不是 fputs(3)、puts(3)、putchar(3) 等；它更快且通常更干净，更不用说避免愚蠢的错误。

用法语句应看起来像手册页的 SYNOPSIS。用法语句应按以下顺序构造：

- 没有操作数的选项排在前面，按字母顺序，在单组方括号（`[` 和 `]`）中。
- 带操作数的选项接下来，也按字母顺序，每个选项及其参数在自己的方括号对中。
- 必需参数（如果有）接下来，按在命令行上应指定的顺序列出。
- 最后，任何可选参数应列出，按应指定的顺序列出，全部在方括号中。

竖线（`|`）分隔"二选一"选项/参数，多个一起指定的选项/参数放在单组方括号中。

```sh
"usage: f [-aDde] [-b b_arg] [-m m_arg] req1 req2 [opt1 [opt2]]en"
"usage: f [-a | -b] [-c [-dEe] [-n number]]en"
```

```sh
	(void)fprintf(stderr, "usage: f [-ab]en");
	exit(1);
}
```

注意，手册页选项描述应按纯字母顺序列出选项。也就是说，不考虑选项是否接受参数。字母顺序应考虑上述大小写顺序。

只要可能，代码应通过代码检查器（例如各种静态分析器或 `cc` `-Wall`）运行，并产生最少的警告。

新代码应使用 `_Static_assert` 而不是旧的 `CTASSERT`。

`__predict_true` 和 `__predict_false` 仅应在使代码可测量地更快时用于频繁执行的代码。对不频繁运行的代码（如子系统初始化）进行预测是浪费的。使用分支预测提示时，非典型错误条件应使用 `__predict_false`（记录例外）。几乎总是成功的操作使用 `__predict_true`。仅对整个 if 语句使用注释，而不是单个子句。没有分支可能性的经验证据，不要添加这些注释。

新的核心内核代码应符合 `cc` 指南。第三方维护的模块和设备驱动程序的指南更宽松。预期它们的代码至少在风格上内部一致。

风格更改（包括空白更改）会使下游消费者的工作复杂化，并可能损害开发者跟踪某些更改历史的能力。必须避免此类独立更改，并且不应跨越不相关的目录，因为这会增加合并到 stable 和 release 分支（MFC）时冲突的机会。另一方面，当某个逻辑代码单元（无论是函数、函数组、文件或文件组）的很大一部分（通常约一半）将被修改时，鼓励开发者按照本文档所述修改整个单元的风格。在这种情况下，对其他未修改代码的风格更改应单独提交。仅风格的提交应添加到源码仓库顶部的 `.git-blame-ignore-revs` 文件中，以将它们从 `git blame` 中隐藏。此文件中的注释指示如何使用它。仓库中大约符合 FreeBSD KNF `cc` 的代码不得偏离合规性。

### C++

KNF 风格最初定义为 C 的风格。C++ 引入了几个新习惯用法，这些在 KNF C 中没有现成的对应，例如类中的内联函数定义。C++ 也不总是与某些 KNF 指南兼容，例如将返回值括在括号中。对于 C++ 代码，FreeBSD 旨在遵循广泛接受的 C++ 实践，同时遵循 KNF 的一般形状。本节列举了与 KNF C 不同的 C++ 特定指南。

C++ 源文件的首选后缀是".cc"和".hh"。头文件应始终使用后缀，与 C++ 标准库的头文件不同。

返回值不应括在括号中。将现有 C 代码转换为 C++ 时，现有返回值可以保留在括号中。

命名空间声明的开花括号应在第一行，类似于结构和类定义。嵌套命名空间应使用单个命名空间声明声明。

```sh
namespace foo::bar {
}
```

成员函数声明应遵循与独立函数原型相同的风格，但函数返回类型和名称之间应使用空格。

顶层的函数定义应在函数类型后使用换行，类似于 C 函数定义。

类、结构或联合内的嵌套成员函数定义不应在函数类型后使用换行。相反，这些应遵循成员函数声明的风格。这是更常见的 C++ 风格，对于小方法（如 getter 和 setter）更紧凑。

体由单个语句组成的内联函数可以为函数体使用单行。体为空的内联函数应始终使用单行。

```sh
struct widget {
	int foo() { return 4; }
	int bar();
};
int
widget::bar()
{
	return 6;
}
```

默认和删除的方法应声明为单行。

```sh
class box {
	~box() = default;
};
```

在模板声明中，`template` 关键字和模板参数列表后应在模板声明之前换行。

```sh
template <typename T>
class box {
	T data;
};
```

引用变量的 `&` 应放在变量名上而不是类型上，类似于指针使用 `*` 的风格。

```sh
	int x;
	int &xp = x;
```

变量可以在函数内的任何位置声明，而不仅仅在块的开头。

应优先使用标准库容器而不是 [queue(3)](../man3/queue.3.md) 或 [tree(3)](../man3/tree.3.md) 宏。

应使用 `nullptr` 而不是 `NULL` 或 0。

使用标准库类型管理字符串，如 `std::string` 和 `std::string_view`，而不是 `char *` 和 `const char *`。与 C 代码交互时可以使用 C 类型。

`auto` 关键字可以在各种提高可读性的上下文中使用。示例包括迭代器、范围 for 值的非平凡类型以及明显类型的返回值，如 `static_cast` 或 `std::make_unique`。将任何限定符放在 `auto` 之前，例如：`const auto`。

使用 `std::unique_ptr` 和 `std::shared_ptr` 智能指针管理动态分配对象的生命周期，而不是 `new` 和 `delete`。使用 `std::make_unique` 或 `std::make_shared` 构造智能指针。除非必要与 C 代码交互，否则不要使用 malloc(3)。

不要在头文件的全局作用域中使用 `using` 导入任何命名空间。除 `std` 命名空间（例如 `std::literals`）以外的命名空间可以在源文件和头文件的函数作用域中导入。

使用 `using` 而不是 `typedef` 定义类型别名。

## 文件

**`/usr/src/tools/build/checkstyle9.pl`** 检查源文件中 `cc` 违规的脚本。

**`/usr/src/tools/tools/editing/freebsd.el`** 遵循 FreeBSD `cc` 缩进规则的 Emacs 插件。

**`/usr/src/tools/tools/editing/freebsd.vim`** 遵循 FreeBSD `cc` 缩进规则的 Vim 插件。

## 参见

indent(1), err(3), warn(3), [style.Makefile(5)](../man5/style.Makefile.5.md), [style.mdoc(5)](../man5/style.mdoc.5.md), [style.lua(9)](style.lua.9.md)

## 历史

本手册页最初基于 4.4BSD 发行版中的 `src/admin/style/style` 文件，并经常更新以反映 FreeBSD 项目的当前实践和愿望。`src/admin/style/style` 是 CSRG 对 Ken Thompson 和 Dennis Ritchie 在 Version 6 AT&T UNIX 中编程风格的编纂。
