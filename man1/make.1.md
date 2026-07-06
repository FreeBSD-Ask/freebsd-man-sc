# make.1

`make` — 维护程序依赖关系

## 名称

`make`

## 概要

`make [-BeikNnqrSstWwX] [-C directory] [-D variable] [-d flags] [-f makefile] [-I directory] [-J private] [-j max_jobs] [-m directory] [-T file] [-V variable] [-v variable] [variable=value ...] [target ...]`

## 描述

`make` 是一个旨在简化其他程序维护的程序。其输入是关于程序和其他文件所依赖文件的规格列表。如果未给出 `-f` `makefile` 选项，`make` 会查找 `.MAKE.MAKEFILE_PREFERENCE` 中列出的 makefile（默认 ‘`makefile`’、‘`Makefile`’），以找到规格。如果文件 ‘`.depend`’ 存在，则读取它，参见 mkdep(1)。

本手册页仅作为参考文档。有关 `make` 和 makefile 的更详尽描述，请参阅 PMake - A Tutorial（1993 年）。

`make` 在解析命令行参数之前，将 `MAKEFLAGS` 环境变量的内容前置于命令行参数。

选项如下：

**`-B`** 尝试向后兼容，方法是每条命令执行单个 shell，并按顺序生成依赖行的源。

**`-C`** `directory` 在读取 makefile 或执行任何其他操作之前更改到 `directory`。如果指定多个 `-C` 选项，每个相对于前一个解释：`-C` `/` `-C` `etc` 等价于 `-C` `/etc`。

**`-D`** `variable` 在全局作用域中将 `variable` 定义为 1。

**`-d`** [`-`]`flags` 开启调试，并指定 `make` 的哪些部分打印调试信息。除非 flags 前面有 `-`，否则它们被添加到 `MAKEFLAGS` 环境变量并传递给任何子 make 进程。默认情况下，调试信息打印到标准错误，但可使用 `F` 调试标志更改。调试输出始终是无缓冲的；此外，如果启用调试但调试输出未定向到标准输出，标准输出是行缓冲的。可用 `flags` 为：

**`A`** 打印所有可能的调试信息；等同于指定所有调试标志。

**`a`** 打印有关归档搜索和缓存的调试信息。

**`C`** 打印有关当前工作目录的调试信息。

**`c`** 打印有关条件求值的调试信息。

**`d`** 打印有关目录搜索和缓存的调试信息。

**`e`** 打印有关失败命令和目标的调试信息。

**`F`** [`+`]`filename` 指定调试输出的写入位置。这必须是最后一个标志，因为它消耗参数的其余部分。如果 `F` 标志后的字符紧跟 `+`，文件以追加模式打开；否则文件被覆盖。如果文件名为 `stdout` 或 `stderr`，调试输出分别写入标准输出或标准错误（`+` 选项无效果）。否则，输出写入命名文件。如果文件名以 `.%d` 结尾，`%d` 替换为 pid。

**`f`** 打印有关循环求值的调试信息。

**`g1`** 在制作任何内容之前打印输入图。

**`g2`** 在制作所有内容之后，或在出错退出之前打印输入图。

**`g3`** 在出错退出之前打印输入图。

**`h`** 打印有关哈希表操作的调试信息。

**`j`** 打印有关运行多个 shell 的调试信息。

**`L`** 开启 lint 检查。这会在赋值时对未正确解析的变量赋值抛出错误，因此文件和行号可用。

**`l`** 不管 Makefile 中的命令是否以 `@` 或其他 “安静” 标志为前缀，都打印命令。也称为 “大声” 行为。

**`M`** 打印有关目标的 “meta” 模式决策的调试信息。

**`m`** 打印有关制作目标的调试信息，包括修改日期。

**`n`** 不删除运行命令时创建的临时命令脚本。这些临时脚本在 `TMPDIR` 环境变量引用的目录中创建，如果 `TMPDIR` 未设置或设为空字符串则在 **`/tmp`** 中。临时脚本由 mkstemp(3) 创建，名称形式为 `makeXXXXXX`。*注意：* 这可能在 `TMPDIR` 或 **`/tmp`** 中创建许多文件，请谨慎使用。

**`p`** 打印有关 makefile 解析的调试信息。

**`s`** 打印有关后缀转换规则的调试信息。

**`t`** 打印有关目标列表维护的调试信息。

**`V`** 强制 `-V` 选项打印变量的原始值，覆盖通过 `.MAKE.EXPAND_VARIABLES` 设置的默认行为。

**`v`** 打印有关变量赋值和展开的调试信息。

**`x`** 以 `-x` 运行 shell 命令，使得实际命令在执行时打印。

**`-e`** 让环境变量覆盖 makefile 中的全局变量。

**`-f`** `makefile` 指定要读取的 makefile，而非 `.MAKE.MAKEFILE_PREFERENCE` 中列出的默认值之一。如果 `makefile` 为 `-`，读取标准输入。如果 `makefile` 以字符串 `.../` 开头，`make` 在当前目录及其父目录中搜索参数其余部分中指定的路径。可指定多个 makefile，按指定顺序读取。

**`-I`** `directory` 指定搜索 makefile 和所包含 makefile 的目录。系统 makefile 目录（或目录，参见 `-m` 选项）自动作为此列表的一部分包含。

**`-i`** 忽略 makefile 中 shell 命令的非零退出。等同于在 makefile 中的每个命令行前指定 `-`。

**`-J`** `private` 此选项 *不应* 由用户指定。当 `-j` 选项在递归构建中使用时，此选项由 make 传递给子 make，使构建中的所有 make 进程协作以避免系统过载。

**`-j`** `max_jobs` 指定 `make` 可同时运行的最大作业数。如果 `max_jobs` 是浮点数或以 `C` 结尾，则该值乘以 sysconf(3) 报告的在线 CPU 数。`max_jobs` 的值保存在 `.MAKE.JOBS` 中。除非也指定了 `-B` 选项，否则关闭兼容模式。关闭兼容模式时，与目标关联的所有命令在单个 shell 调用中执行，而非传统的每行一个 shell 调用。这可能破坏在每次命令调用时更改目录然后期望在下一行以全新环境开始的传统脚本。更正脚本比开启向后兼容更高效。使用 `max_jobs` 个令牌的作业令牌池控制运行中的作业总数。`make` 的每个实例在运行新作业前等待池中的令牌。

**`-k`** 遇到错误后继续处理，但仅针对不依赖于导致错误的目标的那些目标。

**`-m`** `directory` 指定搜索 `sys.mk` 和通过 `<``file``>` 风格 include 语句包含的 makefile 的目录。`-m` 选项可多次使用以形成搜索路径。此路径覆盖默认的系统包含路径 **`/usr/share/mk`**。此外，系统包含路径被追加到用于 `""file""` 风格 include 语句的搜索路径（参见 `-I` 选项）。系统包含路径可通过只读变量 `.SYSPATH` 引用。如果 `-m` 参数（或 `MAKESYSPATH` 环境变量）中的目录名以字符串 `.../` 开头，`make` 搜索参数字符串剩余部分中指定的文件或目录名。搜索从当前目录开始，然后向上朝文件系统根方向工作。如果搜索成功，结果目录替换 `-m` 参数中的 `.../` 规格。此功能允许 `make` 在当前源码树中轻松搜索自定义 `sys.mk` 文件（例如，使用 `.../mk/sys.mk` 作为参数）。

**`-n`** 显示本应执行的命令，但不实际执行，除非目标依赖于 `.MAKE` 特殊源（见下文）或命令以 ‘`+`’ 为前缀。

**`-N`** 显示本应执行的命令，但不实际执行任何命令；适用于在不进入子目录的情况下调试顶层 makefile。

**`-q`** 不执行任何命令，如果指定目标是最新的则退出 0，否则退出 1。

**`-r`** 不使用系统 makefile 中指定的内置规则。

**`-S`** 遇到错误时停止处理。这是默认行为，与 `-k` 相反。

**`-s`** 不回显执行的任何命令。等同于在 makefile 中的每个命令行前指定 ‘`@`’。

**`-T`** `tracefile` 与 `-j` 标志一起使用时，为每个启动和完成的作业向 `tracefile` 追加追踪记录。

**`-t`** 而非按 makefile 中指定的重新构建目标，创建它或更新其修改时间使其看起来是最新的。

**`-V`** `variable` 打印 `variable` 的值。不构建任何目标。此选项可多次指定；变量每行打印一个，每个空或未定义变量对应一个空行。打印的值在所有 makefile 读取后从全局作用域提取。默认情况下，显示原始变量内容（可能包括额外的未展开变量引用）。如果 `variable` 包含 `$`，它不被解释为变量名而是表达式。其值在打印前展开。如果 `.MAKE.EXPAND_VARIABLES` 设为 true 且未使用 `-dV` 选项覆盖，值也在打印前展开。注意，循环局部和目标局部变量，以及 makefile 处理期间全局变量临时取得的值，不能通过此选项访问。`-dv` 调试模式可用于查看这些，代价是产生大量额外输出。

**`-v`** `variable` 类似于 `-V`，但所有打印的变量始终展开为其完整值。`-V` 或 `-v` 的最后一次出现决定是否所有变量都展开。

**`-W`** 将 makefile 解析期间的任何警告视为错误。

**`-w`** 打印进入和离开目录的消息，处理前后。

**`-X`** 不单独将命令行上传递的变量导出到环境。命令行上传递的变量仍通过 `MAKEFLAGS` 环境变量导出。此选项在命令参数大小限制较小的系统上可能有用。

**`variable`** `=``value` 将变量 `variable` 的值设为 `value`。通常，命令行上传递的所有值也通过环境导出给子 make。`-X` 标志禁用此行为。变量赋值应遵循选项以兼容 POSIX，但不强制顺序。

makefile 中有几种不同类型的行：依赖规格、shell 命令、变量赋值、include 语句、条件指令、for 循环、其他指令和注释。

行可通过以反斜杠（`\`）结尾从一行继续到下一行。尾随换行符和下一行的初始空白压缩为单个空格。

## 文件依赖规格

依赖行由一个或多个目标、一个运算符和零个或多个源组成。这创建了一种关系：目标 “依赖于” 源，通常由源创建。如果目标不存在，或其修改时间小于其任何源，则认为目标过期。过期目标会被重新创建，但仅在所有源都已检查并按需重新创建之后。可使用三种运算符：

**`:`** 多个依赖行可命名此目标，但只有一个可附带 shell 命令。所有依赖行中命名的所有源一起考虑，如果需要，运行附带的 shell 命令创建或重新创建目标。如果 `make` 被中断，目标被删除。

**`!`** 相同，但无论是否过期，目标总是被重新创建。

**`::`** 任何依赖行都可附带 shell 命令，但每个独立处理：考虑其源，如果目标相对于（仅）那些源过期，则运行附带的 shell 命令。因此，根据情况，可运行不同组的附带 shell 命令。此外，与 `:` 不同，对于无源的依赖行，附带的 shell 命令总是运行。同样与 `:` 不同，如果 `make` 被中断，目标不被删除。

提到特定目标的所有依赖行必须使用相同的运算符。

目标和源可包含 shell 通配符值 `?`、`*`、`[]` 和 `{}`。值 `?`、`*` 和 `[]` 仅可用作目标或源最后组件的一部分，且仅匹配现有文件。值 `{}` 不必用于描述现有文件。展开按目录顺序，而非 shell 中按字母顺序。

## SHELL 命令

每个目标可关联一行或多行 shell 命令，通常用于创建目标。此脚本中的每行 *必须* 以制表符开头。（出于历史原因，不接受空格。）虽然目标可出现在多个依赖行中，但默认情况下这些规则中只有一个可后跟创建脚本。但如果使用 ‘`::`’ 运算符，所有规则都可包含脚本，各脚本按找到的顺序执行。

每行视为单独的 shell 命令，除非行尾以反斜杠 `\` 转义，这种情况下该行和下一行合并。如果命令的前几个字符是 ‘`@`’、‘`+`’ 或 ‘`-`’ 的任意组合，命令被特殊处理。

**`@`** 导致命令在执行前不回显。

**`+`** 导致命令即使在给出 `-n` 时也执行。这类似于 `.MAKE` 特殊源的效果，区别在于效果可限于脚本的单行。

**`-`** 在兼容模式下导致命令行的任何非零退出状态被忽略。当 `make` 以 `-j` `max_jobs` 作业模式运行时，目标的整个脚本提供给单个 shell 实例。在兼容（非作业）模式下，每个命令在单独进程中运行。如果命令包含任何 shell 元字符（`#=|^(){};&<>*?[]:$\n`），传递给 shell；否则 `make` 尝试直接执行。如果行以 ‘`-`’ 开头且 shell 启用了 ErrCtl，命令行失败被忽略，如同兼容模式。否则 ‘`-`’ 影响整个作业；脚本在第一个失败的命令行停止，但目标不被视为失败。

Makefile 应写得使 `make` 操作模式不改变其行为。例如，任何使用 “cd” 或 “chdir” 而无意为后续命令更改目录的命令应放在括号中使其在子 shell 中执行。要强制使用单个 shell，转义换行符使整个脚本成为一个命令。例如：

```sh
avoid-chdir-side-effects:
	@echo "Building $@ in $$(pwd)"
	@(cd ${.CURDIR} && ${MAKE} $@)
	@echo "Back in $$(pwd)"
ensure-one-shell-regardless-of-mode:
	@echo "Building $@ in $$(pwd)"; \
	(cd ${.CURDIR} && ${MAKE} $@); \
	echo "Back in $$(pwd)"
```

由于 `make` 在执行任何目标之前将当前工作目录更改为 ‘`.OBJDIR`’，每个子进程以此作为其当前工作目录开始。

## 变量赋值

make 中的变量行为很像 C 预处理器中的宏。

变量赋值形式为 ‘`NAME` `op` `value`’，其中：

**`NAME`** 是单字变量名，按传统由全大写字母组成，

**`op`** 是下面描述的变量赋值运算符之一，

**`value`** 根据变量赋值运算符解释。

`NAME`、`op` 和 `value` 周围的空白被丢弃。

### 变量赋值运算符

为变量赋值的五个运算符为：

**`=`** 将值赋给变量。任何先前的值被覆盖。

**`+=`** 将值追加到变量的当前值，以单个空格分隔。

**`?=`** 如果变量尚未定义，则将值赋给变量。

**`:=`** 展开值，然后赋给变量。*注意：* 对未定义变量的引用 *不* 展开。这在变量修饰符使用时可能引起问题。

**`!=`** 展开值并传递给 shell 执行，然后将子进程标准输出的输出赋给变量。结果中的任何换行符替换为空格。

### 变量的展开

在大多数展开变量的上下文中，`$$` 展开为单个美元符号。在其他上下文中（大多数变量修饰符，条件中的字符串字面量），`\$` 展开为单个美元符号。

对变量的引用形式为 `${` `name` [`:` `modifiers` ]`}` 或 `$(` `name` [`:` `modifiers` ]`)`。如果变量名仅由单个字符组成且表达式不含修饰符，则不需要周围的花括号或圆括号。不推荐使用此较短形式。

如果变量名包含美元符号，名称本身先展开。这允许几乎任意的变量名，但包含美元符号、花括号、圆括号或空格的名称最好避免。

如果展开嵌套变量表达式的结果包含美元符号（`$`），结果受进一步展开。

变量替换在四个不同时间发生，取决于变量在哪里使用。

```sh
.for i in 1 2 3
a+=     ${i}
j=      ${i}
b+=     ${j}
.endfor
all:
	@echo ${a}
	@echo ${b}
```

```sh
1 2 3
3 3 3
```

**`a`** 包含 `${:U1} ${:U2} ${:U3}`，展开为 `1 2 3`。

**`j`** 包含 `${:U3}`，展开为 `3`。

**`b`** 包含 `${j} ${j} ${j}`，展开为 `${:U3} ${:U3} ${:U3}`，进一步展开为 `3 3 3`。

- 依赖行中的变量在行读取时展开。
- 条件中的变量单独展开，但仅展开到确定条件结果所需的程度。
- shell 命令中的变量在 shell 命令执行时展开。
- `.for` 循环索引变量在每次循环迭代时展开。注意，组合循环体时不展开其他变量，因此以下示例代码：打印：循环执行后：

### 变量类别

四种不同的变量类别（按优先级递增）为：

**环境**变量 作为 `make` 环境一部分定义的变量。

**全局**变量 在 makefile 或包含的 makefile 中定义的变量。

**命令行**变量 作为命令行一部分定义的变量。

**局部**变量 专为特定目标定义的变量。

局部变量可在依赖行上设置，除非 `.MAKE.TARGET_LOCAL_VARIABLES` 设为 `false`。行的其余部分（已展开全局变量）是变量值。例如：

```sh
COMPILER_WRAPPERS= ccache distcc icecc
${OBJS}: .MAKE.META.CMP_FILTER=${COMPILER_WRAPPERS:S,^,N,}
```

只有目标 `${OBJS}` 受该过滤器影响（在 “meta” 模式中），简单启用/禁用任何编译器包装器不会使所有这些目标过期。

*注意：* 目标局部变量赋值行为不同：

**`+=`** 仅追加到同一目标和变量的先前局部赋值。

**`:=`** 对已展开的全局变量是冗余的。

内置局部变量为：

**`.ALLSRC`** 此目标的所有源列表；亦称 ‘`>`’ 或 ‘`^`’。

**`.ARCHIVE`** 归档文件名；亦称 ‘`!`’。

**`.IMPSRC`** 在后缀转换规则中，目标将从其转换的源的名称/路径（“隐含” 源）；亦称 ‘`<`’。在显式规则中未定义。

**`.MEMBER`** 归档成员名；亦称 ‘`%`’。

**`.OODATE`** 此目标中被认为过期的源列表；亦称 ‘`?`’。

**`.PREFIX`** 移除后缀（如果在 `.SUFFIXES` 中声明）的目标名；亦称 ‘`*`’。

**`.TARGET`** 目标名；亦称 ‘`@`’。为与其他 make 兼容，在归档成员规则中这是 `.ARCHIVE` 的别名。

较短形式（‘`>`’、‘`^`’、‘`!`’、‘`<`’、‘`%`’、‘`?`’、‘`*`’ 和 ‘`@`’）允许用于向后兼容历史 makefile 和传统 POSIX make，不推荐使用。

这些变量的变体，标点符号后紧跟 `D` 或 `F`，例如 `$(@D)`，是等同于使用 `:H` 和 `:T` 修饰符的传统形式。这些形式为兼容 AT&T System V UNIX makefile 和 POSIX 而接受，但不推荐。

四个局部变量可在依赖行的源中使用，因为它们展开为行上每个目标的适当值。这些变量为 ‘`.TARGET`’、‘`.PREFIX`’、‘`.ARCHIVE`’ 和 ‘`.MEMBER`’。

### 额外内置变量

此外，`make` 设置或知道以下变量：

```sh
--- `target` `---`
```

```sh
---make[1234] `target` `---`
```

```sh
Building ${.TARGET:H:tA}/${.TARGET:T}
```

**`compat`** 类似于 `-B`，将 `make` 置于 “compat” 模式。

**`meta`** 将 `make` 置于 “meta” 模式，其中为每个目标创建 meta 文件以捕获运行的命令、生成的输出，以及如果 [filemon(4)](../man4/filemon.4.md) 可用，`make` 感兴趣的系统调用。捕获的输出在诊断错误时很有用。当正常依赖规则表明目标未过期时，`make` 将使用 meta 文件中的信息帮助确定目标是否过期。首先，要执行的命令与先前捕获的命令比较，如果有任何不同，目标过期。这允许更新构建的可靠性和效率大幅提升。不再需要目标依赖于 makefile 以防它们设置可能相关的变量。诸如 `.MAKE.META.CMP_FILTER` 和 `.NOMETA_CMP` 的机制允许按目标限制或禁用该比较。对变量 `.OODATE` 的引用可用于阻止某些命令的比较。例如：`${.OODATE:M}` 展开为空且对目标无影响，但其副作用是防止其出现的任何命令行的比较。出于文档目的，`${.OODATE:MNOMETA_CMP}` 有用。如有必要，`make` 将使用 [filemon(4)](../man4/filemon.4.md) 捕获的信息检查生成目标时使用的任何文件的修改时间，如果有任何较新，目标过期。这种深度检查很容易导致目标 *总是* 被认为过期的情况，这就是为什么提供 `.MAKE.META.IGNORE_FILTER`、`.MAKE.META.IGNORE_PATHS` 和 `.MAKE.META.IGNORE_PATTERNS` 以在必要时限制该检查。

**`curdirOk=`** `bf` 默认情况下，`make` 不在 ‘`.CURDIR`’ 中创建 `.meta` 文件。这可通过将 `bf` 设为表示 true 的值覆盖。

**`missing-meta=`** `bf` 如果 `bf` 为 true，缺少 `.meta` 文件使目标过期。

**`missing-filemon=`** `bf` 如果 `bf` 为 true，缺少 filemon 数据使目标过期。

**`nofilemon`** 不使用 [filemon(4)](../man4/filemon.4.md)。

**`env`** 对于调试，将环境包含在 `.meta` 文件中可能有用。

**`verbose`** 如果在 “meta” 模式中，打印关于正在构建目标的线索。这在构建以其他方式静默运行时有用。打印的消息是 `.MAKE.META.PREFIX` 的展开值。

**`ignore-cmd`** 某些 makefile 有根本不稳定的命令。此关键字导致在 “meta” 模式中确定目标是否过期时忽略它们。另请参见 `.NOMETA_CMP`。

**`silent=`** `bf` 如果 `bf` 为 true，创建 .meta 文件时标记目标 `.SILENT`。

**`randomize-targets`** 在 compat 和并行模式中，不按通常顺序制作目标，而是随机化其顺序。此模式可用于检测文件之间未声明的依赖关系。

```sh
${MAKE_PRINT_VAR_ON_ERROR:@v@$v='${$v}'${.newline}@}
```

- `${MAKEOBJDIRPREFIX}``${.CURDIR}`（仅当 ‘`MAKEOBJDIRPREFIX`’ 在环境中或命令行上设置时。）
- `${MAKEOBJDIR}`（仅当 ‘`MAKEOBJDIR`’ 在环境中或命令行上设置时。）
- `${.CURDIR}``/obj.``${MACHINE}`
- `${.CURDIR}``/obj`
- `/usr/obj/``${.CURDIR}`
- `${.CURDIR}`

**`.ALLTARGETS`** makefile 中遇到的所有目标列表。如果在 makefile 解析期间求值，仅列出迄今为止遇到的目标。

**`.CURDIR`** `make` 执行所在目录的路径。有关更多详情，参见 ‘`PWD`’ 的描述。

**`.ERROR_CMD`** 用于错误处理，参见 `MAKE_PRINT_VAR_ON_ERROR`。

**`.ERROR_CWD`** 用于错误处理，参见 `MAKE_PRINT_VAR_ON_ERROR`。

**`.ERROR_EXIT`** 用于错误处理，参见 `MAKE_PRINT_VAR_ON_ERROR`。

**`.ERROR_META_FILE`** 在 “meta” 模式中用于错误处理，参见 `MAKE_PRINT_VAR_ON_ERROR`。

**`.ERROR_TARGET`** 用于错误处理，参见 `MAKE_PRINT_VAR_ON_ERROR`。

**`.INCLUDEDFROMDIR`** 此 makefile 被包含自的文件所在目录。

**`.INCLUDEDFROMFILE`** 此 makefile 被包含自的文件名。

**`MACHINE`** 机器硬件名，参见 [uname(1)](uname.1.md)。

**`MACHINE_ARCH`** 机器处理器架构名，参见 [uname(1)](uname.1.md)。

**`MAKE`** `make` 执行时使用的名称（`argv[0]`）。

**`.MAKE`** 与 `MAKE` 相同，用于兼容。首选使用环境变量 `MAKE`，因为它与其他 make 变体更兼容，且不能与同名的特殊目标混淆。

**`.MAKE.ALWAYS_PASS_JOB_QUEUE`** 告知 `make` 是否传递作业令牌队列的描述符，即使目标未标记 `.MAKE`。默认为 `yes`，用于向后兼容 FreeBSD 9.0 及更早版本。

**`.MAKE.DEPENDFILE`** 命名从其中读取生成的依赖关系的 makefile（默认 ‘`.depend`’）。

**`.MAKE.DIE_QUIETLY`** 如果设为 `true`，结束时不打印错误信息。

**`.MAKE.EXPAND_VARIABLES`** 控制 `-V` 选项默认行为的布尔值。如果为 true，`-V` 打印的变量值完全展开；如果为 false，显示原始变量内容（可能包括额外的未展开变量引用）。

**`.MAKE.EXPORTED`** `make` 导出的变量列表。

**`MAKE_VERSION`** 此变量指示 `make` 的版本。通常是上次从 NetBSD 导入的日期。用于检查某些功能是否可用。

**`MAKEFILE`** 当前读取的顶层 makefile，如命令行中给出。

**`.MAKEFLAGS`** 环境变量 ‘`MAKEFLAGS`’ 可包含可在 `make` 命令行上指定的任何内容。在 `make` 命令行上指定的任何内容追加到 `.MAKEFLAGS` 变量，然后添加到 `make` 执行的所有程序的环境中。

**`.MAKE.GID`** 运行 `make` 的用户的数字组 ID。只读。

**`.MAKE.JOB.PREFIX`** 如果 `make` 以 `-j` 运行，每个目标的输出以一个令牌为前缀，其第一部分可通过 `.MAKE.JOB.PREFIX` 控制。如果 `.MAKE.JOB.PREFIX` 为空，不打印令牌。例如，将 `.MAKE.JOB.PREFIX` 设为 `${.newline}---${.MAKE:T}[${.MAKE.PID}]` 会产生类似令牌，使跟踪所达到的并行度更容易。

**`.MAKE.JOBS`** `-j` 选项的参数。

**`.MAKE.JOBS.C`** 只读布尔值，指示 `-j` 选项是否支持使用 `C`。

**`.MAKE.LEVEL`** `make` 的递归深度。`make` 的顶层实例级别为 0，每个子 make 为其父级别加 1。这允许诸如 `.if ${.MAKE.LEVEL} == 0` 的测试保护应仅在 `make` 的顶层实例中求值的内容。

**`.MAKE.LEVEL.ENV`** 存储 `make` 嵌套调用级别的环境变量名。

**`.MAKE.MAKEFILE_PREFERENCE`** `make` 查找的有序 makefile 名称列表（默认 ‘`makefile`’、‘`Makefile`’）。

**`.MAKE.MAKEFILES`** `make` 读取的 makefile 列表，用于跟踪依赖关系。每个 makefile 仅记录一次，无论读取次数。

**`.MAKE.META.BAILIWICK`** 在 “meta” 模式中，提供匹配 `make` 所控制目录的前缀列表。如果生成的文件在 `.OBJDIR` 之外但在所述 bailiwick 内缺失，当前目标被认为过期。

**`.MAKE.META.CMP_FILTER`** 在 “meta” 模式中，（非常罕见地！）在比较前过滤命令行可能有用。此变量可设为一组修饰符，应用于不同的旧行和新命令的每一行，如果过滤后的命令仍不同，目标被认为过期。

**`.MAKE.META.CREATED`** 在 “meta” 模式中，此变量包含所有已更新 meta 文件的列表。如果非空，可用于触发 `.MAKE.META.FILES` 的处理。

**`.MAKE.META.FILES`** 在 “meta” 模式中，此变量包含所有使用的 meta 文件（更新与否）列表。此列表可用于处理 meta 文件以提取依赖信息。

**`.MAKE.META.IGNORE_FILTER`** 提供应用于每个路径名的变量修饰符列表。如果展开为空字符串则忽略。

**`.MAKE.META.IGNORE_PATHS`** 提供应忽略的路径前缀列表；因为内容预期随时间变化。默认列表包括：‘`/dev /etc /proc /tmp /var/run /var/tmp`’

**`.MAKE.META.IGNORE_PATTERNS`** 提供与路径名匹配的模式列表。忽略任何匹配的。

**`.MAKE.META.PREFIX`** 定义在 “meta verbose” 模式中为每个更新的 meta 文件打印的消息。默认值为：

**`.MAKE.MODE`** 在读取所有 makefile 后处理。影响 `make` 运行的模式。可包含这些关键字：

**`MAKEOBJDIR`** 用于在单独目录中创建文件，参见 `.OBJDIR`。

**`MAKE_OBJDIR_CHECK_WRITABLE`** 当为 true 时，`make` 检查 `.OBJDIR` 是否可写，如果不可写则发出警告。

**`MAKE_DEBUG_OBJDIR_CHECK_WRITABLE`** 当为 true 且 `make` 警告不可写的 `.OBJDIR` 时，报告 `MAKE_PRINT_VAR_ON_ERROR` 中列出的变量以帮助调试。

**`MAKEOBJDIRPREFIX`** 用于在单独目录中创建文件，参见 `.OBJDIR`。应为绝对路径。

**`.MAKE.OS`** 操作系统名，参见 [uname(1)](uname.1.md)。只读。

**`.MAKEOVERRIDES`** 此变量用于记录命令行上赋值的变量名，以便它们可作为 ‘`MAKEFLAGS`’ 的一部分导出。此行为可通过在 makefile 中将 ‘`.MAKEOVERRIDES`’ 赋为空值禁用。可通过将变量名追加到 ‘`.MAKEOVERRIDES`’ 从 makefile 导出额外变量。‘`MAKEFLAGS`’ 在 ‘`.MAKEOVERRIDES`’ 修改时重新导出。

**`.MAKE.PATH_FILEMON`** 如果 `make` 构建时支持 [filemon(4)](../man4/filemon.4.md)，此变量设为设备节点路径。这允许 makefile 测试此支持。

**`.MAKE.PID`** `make` 的进程 ID。只读。

**`.MAKE.PPID`** `make` 的父进程 ID。只读。

**`MAKE_PRINT_VAR_ON_ERROR`** 当 `make` 因错误停止时，将 ‘`.ERROR_TARGET`’ 设为失败目标的名称，‘`.ERROR_EXIT`’ 设为失败目标的退出状态，‘`.ERROR_CMD`’ 设为失败目标的命令，在 “meta” 模式中，还将 ‘`.ERROR_CWD`’ 设为 getcwd(3)，‘`.ERROR_META_FILE`’ 设为描述失败目标的 meta 文件路径（如果有）。然后打印其名称和 ‘`.CURDIR`’ 的值以及 ‘`MAKE_PRINT_VAR_ON_ERROR`’ 中命名的任何变量的值。

**`.MAKE.SAVE_DOLLARS`** 如果为 true，`$$` 在 `:=` 赋值时保留。默认为 false，用于向后兼容。设为 true 以与其他 make 兼容。如果设为 false，`$$` 按正常求值规则变为 `$`。

**`.MAKE.TARGET_LOCAL_VARIABLES`** 如果设为 `false`，依赖行中明显的变量赋值被视为正常源。

**`.MAKE.UID`** 运行 `make` 的用户的数字 ID。只读。

**`.newline`** 此变量值即为换行符。只读。这允许使用 `:@` 修饰符的展开在循环迭代之间放置换行符而非空格。例如，出错时，`make` 使用以下命令打印变量名及其值：

**`.OBJDIR`** 构建目标的目录路径。其值通过依次尝试 chdir(2) 到以下目录并使用第一个匹配来确定：值在使用前进行变量展开，因此可使用诸如 `${.CURDIR:S,^/usr/src,/var/obj,}` 的表达式。这在 ‘`MAKEOBJDIR`’ 中特别有用。‘`.OBJDIR`’ 可在 makefile 中通过特殊目标 ‘`.OBJDIR`’ 修改。在所有情况下，`make` 更改到指定目录（如果存在），并在执行任何目标之前将 ‘`.OBJDIR`’ 和 ‘`PWD`’ 设为该目录。除非显式 ‘`.OBJDIR`’ 目标，`make` 检查指定目录是否可写，如果不可写则忽略。可通过将环境变量 ‘`MAKE_OBJDIR_CHECK_WRITABLE`’ 设为 “no” 跳过此检查。

**`.PARSEDIR`** 正在解析的当前 makefile 的目录名。

**`.PARSEFILE`** 正在解析的当前 makefile 的基名。此变量和 ‘`.PARSEDIR`’ 仅在 makefile 被解析时设置。要保留其当前值，使用带展开 ‘`:=`’ 的赋值将其赋给变量。

**`.PATH`** `make` 搜索文件的以空格分隔的目录列表。要更新此搜索列表，使用特殊目标 ‘`.PATH`’ 而非直接修改变量。

**`%POSIX`** 在 POSIX 模式中设置，参见特殊目标 `.POSIX`。

**`PWD`** 当前目录的备用路径。`make` 通常将 ‘`.CURDIR`’ 设为 getcwd(3) 给出的规范路径。然而，如果环境变量 ‘`PWD`’ 已设置并给出到当前目录的路径，`make` 将 ‘`.CURDIR`’ 设为 ‘`PWD`’ 的值。如果 ‘`MAKEOBJDIRPREFIX`’ 已设置或 ‘`MAKEOBJDIR`’ 包含变量变换，此行为被禁用。‘`PWD`’ 设为 ‘`.OBJDIR`’ 的值，用于 `make` 执行的所有程序。

**`.SHELL`** 用于运行目标脚本的 shell 路径名。只读。

**`.SUFFIXES`** 已知后缀列表。只读。

**`.SYSPATH`** `make` 搜索 makefile 的以空格分隔的目录列表，称为系统包含路径。要更新此搜索列表，使用特殊目标 ‘`.SYSPATH`’ 而非修改变量（只读）。

**`.TARGETS`** 命令行上显式指定的目标列表（如果有）。

**`VPATH`** `make` 搜索文件的以冒号（“:”）分隔的目录列表。此变量仅为兼容旧 make 程序而支持，改用 ‘`.PATH`’。

### 变量修饰符

变量展开的一般格式为：

> `${` `variable` [`:` `modifier` [`:` ... ]]`}`

每个修饰符以冒号开头。要转义冒号，在其前加反斜杠 `\`。

间接修饰符列表可通过变量指定，如下：

```sh
`modifier_variable` `=` `modifier`[`:`... ]]
`${` `variable` `:${` `modifier_variable` `}` [`:` ... ]`}`
```

在这种情况下，`modifier_variable` 中的第一个修饰符不以冒号开头，因为该冒号已出现在引用变量中。如果 `modifier_variable` 中的任何修饰符包含美元符号（`$`），必须加倍以避免提前展开。

某些修饰符将表达式值解释为单个字符串，其他将表达式值视为以空格分隔的单词列表。将字符串拆分为单词时，空格可使用双引号、单引号和反斜杠转义，如同 shell 中。引号和反斜杠保留在单词中。

支持的修饰符为：

```sh
LIST=			uno due tre quattro
RANDOM_LIST=		${LIST:Ox}
STATIC_RANDOM_LIST:=	${LIST:Ox}
all:
	@echo "${RANDOM_LIST}"
	@echo "${RANDOM_LIST}"
	@echo "${STATIC_RANDOM_LIST}"
	@echo "${STATIC_RANDOM_LIST}"
```

```sh
quattro due tre uno
tre due quattro uno
due uno quattro tre
due uno quattro tre
```

**`1`** 仅第一次出现的单词受影响。

**`g`** 每个受影响单词中的所有出现都被替换。

**`W`** 表达式值视为单个单词。

**`1`** 仅第一次出现的单词受影响。

**`g`** 每个受影响单词中的所有出现都被替换。

**`W`** 表达式值视为单个单词。

```sh
${NUMBERS:M42:?match:no}
```

```sh
${"${NUMBERS:M42}" != "":?match:no} .
```

```sh
${LINKS:@.LINK.@${LN} ${TARGET} ${.LINK.}@}
```

```sh
${MAKE_PRINT_VAR_ON_ERROR:@v@$v='${$v}'${.newline}@}
```

```sh
M_cmpv.units = 1 1000 1000000
M_cmpv = S,., ,g:_:range:@i@+ $${_:[-$$i]} \
\* $${M_cmpv.units:[$$i]}@:S,^,expr 0 ,1:sh
`.if ${VERSION:${M_cmpv}} < ${3.1.12:L:${M_cmpv}}`
```

```sh
${_${.TARGET:T}_CFLAGS:U${DEF_CFLAGS}}
```

```sh
${VAR:D:Unewval}
```

**`index`** 从值中选择单个单词。

**`start`** `..``end` 选择从 `start` 到 `end`（含）的所有单词。例如，‘`:[2..-1]`’ 选择从第二个单词到最后一个单词的所有单词。如果 `start` 大于 `end`，单词以相反顺序输出。例如，‘`:[-1..1]`’ 选择从最后到第一个的所有单词。如果列表已排序，这实际上反转列表，但使用 ‘`:Or`’ 比 ‘`:O:[-1..1]`’ 更高效。

**`*`** 导致后续修饰符将值视为单个单词（可能包含嵌入空格）。类似于 Bourne shell 中 `$*` 的效果。

**0** 含义同 ‘`:[*]`’。

**`@`** 导致后续修饰符将值视为以空格分隔的单词序列。类似于 Bourne shell 中 `$@` 的效果。

**`#`** 返回值中的单词数。

**`:E`** 用每个单词的后缀替换。

**`:H`** 用每个单词的 dirname 替换。

**`:M`** `pattern` 仅选择匹配 `pattern` 的单词。可使用标准 shell 通配符（`*`、`?` 和 `[]`）。通配符可用反斜杠（`\`）转义。作为值拆分为单词、匹配然后连接方式的后果，构造 `${VAR:M*}` 移除所有前导和尾随空格并将单词间间距规范化为单个空格。

**`:N`** `pattern` 与 ‘`:M`’ 相反，选择 *不* 匹配 `pattern` 的所有单词。

**`:O`** 按字典顺序排序单词。

**`:On`** 按数字排序单词。后跟 `k`、`M` 或 `G` 之一的数字乘以适当因子，`k` 为 1024，`M` 为 1048576，`G` 为 1073741824。大小写字母均接受。

**`:Or`** 按相反字典顺序排序单词。

**`:Orn`** 按相反数字顺序排序单词。

**`:Ox`** 随机打乱单词。每次引用修改后的变量时结果不同；使用带展开 ‘`:=`’ 的赋值防止此行为。例如，可能产生类似输出：

**`:Q`** 引用值中的每个 shell 元字符，使其可安全传递给 shell。

**`:q`** 引用值中的每个 shell 元字符，并加倍 ‘$’ 字符，使其可安全通过 `make` 的递归调用。等同于 ‘`:S/\$/&&/g:Q`’。

**`:R`** 用每个单词除后缀外的所有内容替换。

**`:range`** [`=``count`]] 值为表示原始值单词或所提供 `count` 的整数序列。

**`:gmtime`** [`=``timestamp`]] 值被解释为 strftime(3) 的格式字符串，使用 gmtime(3)，产生格式化时间戳。注意：`%s` 格式仅应与 ‘`:localtime`’ 一起使用。如果未提供 `timestamp` 值或为 0，使用当前时间。

**`:hash`** 计算值的 32 位哈希并编码为 8 个十六进制数字。

**`:localtime`** [`=``timestamp`]] 值被解释为 strftime(3) 的格式字符串，使用 localtime(3)，产生格式化时间戳。如果未提供 `timestamp` 值或为 0，使用当前时间。

**`:mtime`** [`=``timestamp`]] 以每个单词为路径名调用 stat(2)；使用 `st_mtime` 作为新值。如果 stat(2) 失败；使用 `timestamp` 或当前时间。如果 `timestamp` 设为 `error`，则 stat(2) 失败将导致错误。

**`:tA`** 尝试使用 realpath(3) 将值转换为绝对路径。如果失败，值不变。

**`:tl`** 将值转换为小写字母。

**`:ts`** `c` 当连接将值视为单词的修饰符后的单词时，单词通常以空格分隔。此修饰符将分隔符更改为字符 `c`。如果省略 `c`，不使用分隔符。常见转义（包括八进制数字码）按预期工作。

**`:tt`** 将每个单词的首字母转换为大写，其余为小写字母。

**`:tu`** 将值转换为大写字母。

**`:tW`** 导致后续修饰符将值视为单个单词（可能包含嵌入空格）。另请参见 ‘`:[*]`’。

**`:tw`** 导致值被视为单词列表。另请参见 ‘`:[@]`’。

**`:S`** / [`^`]`old_string` [`$`]`new_string` / [`1gW`]]] 修改值中每个单词中 `old_string` 的第一次出现，替换为 `new_string`。如果 `old_string` 前加插入符（`^`），`old_string` 锚定在每个单词开头。如果 `old_string` 后加美元符号（`$`），锚定在每个单词末尾。在 `new_string` 中，与号（`&`）替换为 `old_string`。`old_string` 和 `new_string` 都可包含嵌套表达式。更多选项：任何字符可用作修饰符字符串各部分的分隔符。锚定、与号、美元和分隔符字符可用反斜杠（`\`）转义。

**`:C`** / `pattern` / `replacement` / [`1gW`] 修改值中每个单词中扩展正则表达式 `pattern`（参见 regex(3)）的第一次出现，替换为 ed(1) 风格的 `replacement`。`pattern` 和 `replacement` 都可包含嵌套表达式。更多选项：任何字符可用作修饰符字符串各部分的分隔符。锚定、与号、美元和分隔符字符可用反斜杠（`\`）转义。

**`:T`** 用每个单词的最后路径组件（basename）替换。

**`:u`** 移除相邻重复单词（如同 [uniq(1)](uniq.1.md)）。

**`:?`** `true_string` `:` `false_string` 如果变量名（非其值），解析为 `.if` 条件表达式时求值为 true，返回 `true_string` 作为其值，否则返回 `false_string`。由于变量名用作表达式，`:?` 必须是变量名本身之后的第一个修饰符——当然，变量名通常包含变量展开。常见错误是尝试使用类似表达式，实际上测试 defined(NUMBERS)。要确定是否有单词匹配 “42”，需使用类似：

**`:`** `old_string``=``new_string` 这是 AT&T System V UNIX 风格替换。它只能是指定的最后一个修饰符，因为 `old_string` 或 `new_string` 中的 `:` 被视为常规字符，而非修饰符结尾。如果 `old_string` 不包含模式匹配字符 `%`，且单词以 `old_string` 结尾或等于它，则该后缀替换为 `new_string`。否则，`old_string` 中第一个 `%` 匹配任意字符的可能为空的子串，如果在单词中找到整个模式，匹配部分替换为 `new_string`，`new_string` 中第一个 `%`（如果有）替换为 `%` 匹配的子串。`old_string` 和 `new_string` 都可包含嵌套表达式。要防止美元符号启动嵌套表达式，用反斜杠转义。

**`:@`** `varname` `@` `string` `@` 这是来自 OSF Development Environment (ODE) make 的循环展开机制。与 `.for` 循环不同，展开在引用时发生。对于值中的每个单词，将单词赋给名为 `varname` 的变量并求值 `string`。ODE 约定是 `varname` 应以句点开头和结尾，例如：然而，单字母变量通常更可读：

**`:_`** [`=``var`]] 将当前变量值保存在 `$_` 或命名的 `var` 中供以后引用。示例用法：此处 `$_` 用于保存 `:S` 修饰符的结果，稍后使用 `:range` 的索引值引用。

**`:U`** `newval` 如果变量未定义，可选的 `newval`（可为空）为值。如果变量已定义，返回现有值。这是另一个 ODE make 功能。它方便按目标设置 CFLAGS，例如：如果仅在变量未定义时需要值，使用：

**`:D`** `newval` 如果变量已定义，`newval`（可为空）为值。

**`:L`** 变量名为值。

**`:P`** 与变量同名的节点路径为值。如果不存在此类节点或其路径为空，使用变量名。要使此修饰符工作，名称（节点）必须至少出现在依赖关系的右侧。

**`:!`** `cmd` `!` 运行 `cmd` 的输出为值。

**`:sh`** 值作为命令运行，输出成为新值。

**`:sh1`** 值作为命令运行，仅第一次引用，输出缓存供后续引用。当结果预期不变时此修饰符有用。

**`::=`** `str` 替换后变量赋值为 `str`。此修饰符及其变体在晦涩情况下有用，例如想在解析目标 shell 命令时设置变量。这些赋值修饰符始终展开为空。‘`::`’ 有助于避免与 AT&T System V UNIX 风格 `:=` 修饰符的假匹配，由于替换总是发生，`::=` 形式大致合适。

**`::?=`** `str` 如 `::=`，但仅在变量尚无值时。

**`::+=`** `str` 将 `str` 追加到变量。

**`::!=`** `cmd` 将 `cmd` 的输出赋给变量。

**`:[`** `range``]` 从值中选择一个或多个单词，或执行与值拆分为单词方式相关的其他操作。空值或完全由空格组成的值视为单个单词。就 ‘`:[]`’ 修饰符而言，单词使用正整数向前索引（索引 1 表示第一个单词），使用负整数向后索引（索引 -1 表示最后一个单词）。`range` 受变量展开，展开结果按以下方式解释：

## 指令

`make` 提供用于包含 makefile、条件和 for 循环的指令。所有这些指令以单个点（`.`）字符开头的行标识，后跟指令关键字，如 `include` 或 `if`。

### 文件包含

文件通过 `.include <``file``>` 或 `.include ``file``` 包含。尖括号或双引号之间的变量展开以形成文件名。如果使用尖括号，包含的 makefile 预期在系统 makefile 目录中。如果使用双引号，在系统 makefile 目录之前搜索包含 makefile 的目录和使用 `-I` 选项指定的任何目录。

为与其他 make 变体兼容，也接受 ‘`include` `file` ...’（无前导点）。

如果 include 语句写为 `.-include` 或 `.sinclude`，定位和/或打开 include 文件的错误被忽略。

如果 include 语句写为 `.dinclude`，不仅忽略定位和/或打开 include 文件的错误，所包含文件中的过期依赖也忽略，如同 `.MAKE.DEPENDFILE` 中那样。

### 导出变量

导出和取消导出变量的指令为：

```sh
`.if ${.MAKE.LEVEL} == 0`
PATH := ${PATH}
`.unexport-env`
`.export PATH`
`.endif`
```

**`.export`** `variable` ... 导出指定的全局变量。为与其他 make 程序兼容，也接受 `export` `variable``=``value`（无前导点）。将变量名追加到 `.MAKE.EXPORTED` 等同于导出变量。

**`.export-all`** 导出除内部变量（以 `. ` 开头的那些）外的所有全局变量。这不受 `-X` 标志影响，应谨慎使用。

**`.export-env`** `variable` ... 与 `.export` 相同，区别在于变量不追加到 `.MAKE.EXPORTED`。这允许导出到环境的值与 `make` 内部使用的不同。

**`.export-literal`** `variable` ... 与 `.export-env` 相同，区别在于值中的变量不展开。

**`.unexport`** `variable` ... `.export` 的相反操作。指定的全局 `variable` 从 `.MAKE.EXPORTED` 移除。如果未提供变量列表，所有全局变量取消导出，并删除 `.MAKE.EXPORTED`。

**`.unexport-env`** 取消导出先前导出的所有全局变量并清除从父进程继承的环境。此操作导致原始环境的内存泄漏，应节制使用。测试 `.MAKE.LEVEL` 是否为 0 有意义。还注意，源自父环境的任何变量如需要应显式保留。例如：将产生仅包含 ‘`PATH`’ 的环境，这是最小有用环境。实际上 ‘`.MAKE.LEVEL`’ 也推入新环境。

### 消息

向输出打印消息的指令为：

**`.info`** `message` 消息与 makefile 名和行号一起打印。

**`.warning`** `message` 以 ‘`warning:`’ 为前缀的消息与 makefile 名和行号一起打印。

**`.error`** `message` 消息与 makefile 名和行号一起打印，`make` 立即退出。

### 条件

条件的指令为：

**`.if`** `expression` [`operator expression` ...] 测试表达式的值。

**`.ifdef`** `variable` [`operator variable` ...] 测试变量是否已定义。

**`.ifndef`** `variable` [`operator variable` ...] 测试变量是否未定义。

**`.ifmake`** `target` [`operator target` ...] 测试请求的目标。

**`.ifnmake`** `target` [`operator target` ...] 测试请求的目标。

**`.else`** 反转最后一个条件的含义。

**`.elif`** `expression` [`operator expression` ...] ‘`.else`’ 后跟 ‘`.if`’ 的组合。

**`.elifdef`** `variable` [`operator variable` ...] ‘`.else`’ 后跟 ‘`.ifdef`’ 的组合。

**`.elifndef`** `variable` [`operator variable` ...] ‘`.else`’ 后跟 ‘`.ifndef`’ 的组合。

**`.elifmake`** `target` [`operator target` ...] ‘`.else`’ 后跟 ‘`.ifmake`’ 的组合。

**`.elifnmake`** `target` [`operator target` ...] ‘`.else`’ 后跟 ‘`.ifnmake`’ 的组合。

**`.endif`** 结束条件体。

`operator` 可为以下之一：

**`||`** 逻辑或。

**`&&`** 逻辑与；优先级高于 ‘`||`’。

`make` 仅在确定其值所需的范围内求值条件。可使用括号覆盖运算符优先级。布尔运算符 ‘`!`’ 可用于逻辑否定表达式，通常是函数调用。其优先级高于 ‘`&&`’。

`expression` 的值可为以下任何函数调用表达式：

**`defined`** `(` `varname` `)` 如果变量 `varname` 已定义则求值为 true。

**`make`** `(` `target` `)` 如果目标作为 `make` 命令行的一部分指定或在包含条件的行之前声明为默认目标（显式或隐式，参见 `.MAIN`）则求值为 true。

**`empty`** `(` `varname` [: `modifiers` ]`)`] 如果变量展开后（应用修饰符后）结果为空字符串则求值为 true。

**`exists`** `(` `pathname` `)` 如果给定路径名存在则求值为 true。如果为相对路径，在系统搜索路径上搜索路径名（参见 `.PATH`）。

**`target`** `(` `target` `)` 如果目标已定义则求值为 true。

**`commands`** `(` `target` `)` 如果目标已定义且有关联命令则求值为 true。

`Expression` 也可为算术或字符串比较。比较两侧进行变量展开。如果两侧均为数字且均未加引号，按数字比较，否则按字典序比较。字符串如果以 `0x` 开头则解释为十六进制整数，否则解释为十进制浮点数；不支持八进制数。

所有比较可使用运算符 ‘`==`’ 和 ‘`!=`’。数字比较还可使用运算符 ‘`<`’、‘`<=`’、‘`>`’ 和 ‘`>=`’。

如果比较既无比较运算符也无右侧，表达式如果非空且其数字值（如果有）不为零则求值为 true。

当 `make` 求值这些条件表达式之一并遇到无法识别的（以空格分隔的）单词时，根据条件形式应用 “make” 或 “defined” 函数。如果形式为 ‘`.ifdef`’、‘`.ifndef`’ 或 ‘`.if`’，应用 “defined” 函数。类似地，如果形式为 ‘`.ifmake`’ 或 ‘`.ifnmake`’，应用 “make” 函数。

如果条件求值为 true，makefile 解析如前继续。如果求值为 false，跳过以下直到对应 ‘`.elif`’ 变体、‘`.else`’ 或 ‘`.endif`’ 的行。

### For 循环

For 循环通常用于将一组规则应用于文件列表。for 循环语法为：

**`.for`** `variable` [`variable` ... ]`in` `expression`]
**<`make-lines`>**
**`.endfor`**

`expression` 展开然后拆分为单词。在循环每次迭代中，取一个单词赋给每个 `variable`（按顺序），这些 `variables` 替换 for 循环体内 `make-lines` 中的内容。单词数必须均匀；即如果有三个迭代变量，提供的单词数必须是三的倍数。

如果在 `.for` 循环中遇到 ‘`.break`’，导致循环提前终止，否则为解析错误。

### 其他指令

**`.undef`** `variable` ... 取消定义指定的全局变量。仅全局变量可取消定义。

## 注释

注释以井号（`#`）字符开始，可在除 shell 命令行外的任何位置，持续到未转义新行末尾。

## 特殊源（属性）

```sh
skip-compare-for-some:
	@echo this is compared
	@echo this is not ${.OODATE:M.NOMETA_CMP}
	@echo this is also compared
```

```sh
x: a .WAIT b
	echo x
a:
	echo a
b: b1
	echo b
b1:
	echo b1
```

**`.EXEC`** 目标从不过期，但总是执行命令。

**`.IGNORE`** 忽略与此目标关联命令的任何错误，如同它们都以破折号（`-`）开头。

**`.MADE`** 标记此目标的所有源为最新。

**`.MAKE`** 即使指定了 `-n` 或 `-t` 选项也执行与此目标关联的命令。通常用于标记递归 `make`。

**`.META`** 为目标创建 meta 文件，即使标记为 `.PHONY`、`.MAKE` 或 `.SPECIAL`。与 `.MAKE` 一起使用是最可能的情况。在 “meta” 模式中，如果 meta 文件缺失，目标过期。

**`.NOMETA`** 不为目标创建 meta 文件。`.PHONY`、`.MAKE` 或 `.SPECIAL` 目标也不创建 meta 文件。

**`.NOMETA_CMP`** 在决定目标是否过期时忽略命令差异。如果命令包含总是变化的值则有用。但如果命令数变化，目标仍被认为过期。同样效果适用于使用变量 `.OODATE` 的任何命令行，即使其他情况下不需要或不希望，也可用于此目的：`:M` 模式抑制不需要变量的任何展开。

**`.NOPATH`** 不在 `.PATH` 指定的目录中搜索目标。

**`.NOTMAIN`** 通常 `make` 选择遇到的第一个目标作为未指定目标时构建的默认目标。此源阻止选择此目标。

**`.OPTIONAL`** 如果目标标记此属性且 `make` 无法弄清如何创建它，忽略此事实并假定文件不需要或已存在。

**`.PHONY`** 目标不对应实际文件；始终被认为过期，且不使用 `-t` 选项创建。后缀转换规则不应用于 `.PHONY` 目标。

**`.PRECIOUS`** 当 `make` 被中断时，通常删除任何部分制作的目标。此源阻止目标被删除。

**`.RECURSIVE`** `.MAKE` 的同义词。

**`.SILENT`** 不回显与此目标关联的任何命令，如同它们都以 at 符号（`@`）开头。

**`.USE`** 将目标变为 `make` 版本的宏。当目标用作另一目标的源时，另一目标获得源的命令、源和属性（`.USE` 除外）。如果目标已有命令，`.USE` 目标的命令追加到它们。

**`.USEBEFORE`** 类似于 `.USE`，但不是追加，而是将 `.USEBEFORE` 目标命令前置于目标。

**`.WAIT`** 如果 `.WAIT` 出现在依赖行中，它之前的源在它之后的源之前制作。由于文件的依赖物在文件本身可制作之前不制作，这也阻止依赖物构建，除非依赖树另一分支需要它们。因此给定：输出始终为 `a`、`b1`、`b`、`x`。`.WAIT` 施加的顺序仅与并行 make 相关。

## 特殊目标

特殊目标不可与其他目标一起包含，即它们必须是唯一指定的目标。

```sh
.ORDER: b a
b: a
```

**`name`** 这是最小规格，用于选择内置 shell 规格之一；`sh`、`ksh` 和 `csh`。

**`path`** 指定 shell 的绝对路径。

**`hasErrCtl`** 指示 shell 是否支持出错时退出。

**`check`** 开启错误检查的命令。

**`ignore`** 禁用错误检查的命令。

**`echo`** 开启执行命令回显的命令。

**`quiet`** 关闭执行命令回显的命令。

**`filter`** 发出 `quiet` 命令后要过滤的输出。通常与 `quiet` 相同。

**`errFlag`** 传递给 shell 以启用错误检查的标志。

**`echoFlag`** 传递给 shell 以启用命令回显的标志。

**`newline`** 传递给 shell 的字符串字面量，在引号字符外使用时产生单个换行符。

```sh
.SHELL: name=ksh path=/bin/ksh hasErrCtl=true \
	check="set -e" ignore="set +e" \
	echo="set -v" quiet="set +v" filter="set +v" \
	echoFlag=v errFlag=e newline="'\n'"
```

```sh
.SUFFIXES: .c .o
.c.o:
	cc -o ${.TARGET} -c ${.IMPSRC}
```

**`.BEGIN`** 附加到此目标的任何命令行在执行任何其他操作之前执行。

**`.DEFAULT`** 这类似于 `make` 无法以其他方式弄清如何创建的任何目标（仅用作源）的 `.USE` 规则。仅使用 shell 脚本。继承 `.DEFAULT` 命令的目标的 `.IMPSRC` 变量设为目标自身名。

**`.DELETE_ON_ERROR`** 如果此目标存在于 makefile 中，全局导致 make 删除命令失败的目标。（默认情况下，仅删除执行期间被中断命令的目标。这是历史行为。）此设置可用于帮助防止半成品或格式错误的目标残留并破坏未来重建。

**`.END`** 附加到此目标的任何命令行在所有其他操作成功完成后执行。

**`.ERROR`** 附加到此目标的任何命令行在另一目标失败时执行。参见 `MAKE_PRINT_VAR_ON_ERROR` 了解将设置的变量。

**`.IGNORE`** 用 `.IGNORE` 属性标记每个源。如果未指定源，等同于指定 `-i` 选项。

**`.INTERRUPT`** 如果 `make` 被中断，执行此目标的命令。

**`.MAIN`** 如果调用 `make` 时未指定目标，构建此目标。

**`.MAKEFLAGS`** 此目标提供在读取 makefile 时为 `make` 指定标志的方式。标志如同键入到 shell，但 `-f` 选项无效果。

**`.NOPATH`** 将 `.NOPATH` 属性应用于任何指定源。

**`.NOTPARALLEL`** 禁用并行模式。

**`.NO_PARALLEL`** `.NOTPARALLEL` 的同义词，用于与其他 pmake 变体兼容。

**`.NOREADONLY`** 清除指定为源的全局变量的只读属性。

**`.OBJDIR`** 源是 ‘`.OBJDIR`’ 的新值。如果存在，`make` 将当前工作目录更改为它并更新 ‘`.OBJDIR`’ 的值。

**`.ORDER`** 在并行模式中，命名目标按顺序制作。此排序不将目标添加到要制作的目标列表。由于目标的依赖物在目标本身可构建之前不构建，除非 `a` 由依赖图另一部分构建，以下是依赖循环：

**`.PATH`** 源是用于搜索当前目录中未找到的文件的目录。如果未指定源，从搜索路径移除任何先前指定的目录。如果源是特殊 `.DOTLAST` 目标，当前工作目录最后搜索。

**`.PATH.`** `suffix` 类似于 `.PATH`，但仅适用于具有特定后缀的文件。后缀必须先前用 `.SUFFIXES` 声明。

**`.PHONY`** 将 `.PHONY` 属性应用于任何指定源。

**`.POSIX`** 如果这是主 makefile 中的第一个非注释行，变量 `%POSIX` 设为值 `1003.2`，如果存在则包含 makefile `<posix.mk>`，以提供 POSIX 兼容的默认规则。如果 `make` 以 `-r` 标志运行，仅 `posix.mk` 贡献默认规则。在 POSIX 兼容模式中，AT&T System V UNIX 风格替换修饰符首先检查而非作为回退。

**`.PRECIOUS`** 将 `.PRECIOUS` 属性应用于任何指定源。如果未指定源，`.PRECIOUS` 属性应用于文件中的每个目标。

**`.READONLY`** 设置指定为源的全局变量的只读属性。

**`.SHELL`** 设置 `make` 用于执行命令的 shell。源是一组 `field``=``value` 对。示例：

**`.SILENT`** 将 `.SILENT` 属性应用于任何指定源。如果未指定源，`.SILENT` 属性应用于文件中的每个命令。

**`.STALE`** 当依赖文件包含过期条目时运行此目标，`.ALLSRC` 设为该依赖文件名。

**`.SUFFIXES`** 每个源指定 `make` 的后缀。如果未指定源，删除任何先前指定的后缀。它允许创建后缀转换规则。示例：

**`.SYSPATH`** 源是要添加到 `make` 搜索 makefile 的系统包含路径的目录。如果未指定源，从系统包含路径移除任何先前指定的目录。

## 环境变量

`make` 使用以下环境变量（如果存在）：`MACHINE`、`MACHINE_ARCH`、`MAKE`、`MAKEFLAGS`、`MAKEOBJDIR`、`MAKEOBJDIRPREFIX`、`MAKESYSPATH`、`MAKE_STACK_TRACE`、`PWD` 和 `TMPDIR`。

`MAKEOBJDIRPREFIX` 和 `MAKEOBJDIR` 应在环境中或 `make` 命令行上设置，而非作为 makefile 变量；详见 ‘`.OBJDIR`’ 的描述。可通过 makefile 变量设置这些，但除非很早完成且使用 ‘`.OBJDIR`’ 目标重置 ‘`.OBJDIR`’，可能有意外副作用。

如果 `MAKE_STACK_TRACE` 环境变量设为 “yes”，任何堆栈追踪包括父进程的调用链。

## 文件

**.depend** 依赖列表

**makefile** 未在命令行上指定 makefile 时的第一个默认 makefile

**Makefile** 未在命令行上指定 makefile 时的第二个默认 makefile

**sys.mk** 系统 makefile

**/usr/share/mk** 系统 makefile 目录

## 诊断

**`Invalid internal option -J in `directory`** 内部 `-J` 选项协调主 `make` 进程与子 make 进程以限制并行运行的作业数。该选项通过 `MAKEFLAGS` 环境变量传递给所有子进程。要变为有效，此选项要求运行子 make 的目标标记 `.MAKE` 特殊源，或目标的命令之一直接包含单词 “make” 或表达式 “${MAKE}”、“${.MAKE}”、“$(MAKE)”、“$(.MAKE)” 之一。如果不是这种情况，make 发出上述警告并回退到 compat 模式。要查看导致无效选项的子 make 链，将 `MAKE_STACK_TRACE` 环境变量设为 “yes”。要以并行模式运行子 make（即使在干运行模式中，参见 `-n` 选项），将 `.MAKE` 伪源添加到目标。这在子 make 在子目录中运行同一目标时合适。要以并行模式但非干模式运行子 make，将 “${:D make}” 标记添加到目标命令之一。此标记展开为空字符串，因此不影响执行的命令。要以 compat 模式运行子 make，将其调用添加 `-B` 选项。这在子 make 仅用于使用 `-v` 或 `-V` 选项打印变量值时合适。要使子 make 独立于父 make，在目标命令中取消设置 `MAKEFLAGS` 环境变量。

## 兼容性

基本 make 语法在不同 make 变体间兼容；但特殊变量、变量修饰符和条件不兼容。

### 旧版本

`make` 旧版本中变更的不完整列表：

NetBSD 5.0 之后，.for 循环变量替换方式更改，使其仍表现为变量展开。特别是这阻止它们被视为语法，并消除在 .if 语句中使用它们的一些晦涩问题。

NetBSD 4.0 中并行 make 调度方式更改，使 .ORDER 和 .WAIT 递归应用于依赖节点。所用算法未来可能再次更改。

### 其他 make 方言

其他 make 方言（GNU make、SVR4 make、POSIX make 等）不支持本手册中描述的大多数 `make` 功能。最显著的是：

- `.WAIT` 和 `.ORDER` 声明以及大多数与并行化相关的功能。（GNU make 支持并行化，但缺乏有效控制它所需的功能。）
- 指令，包括 for 循环和条件以及大多数形式的 include 文件。（GNU make 有自己不兼容且功能较弱的条件语法。）
- 所有以点开头的内置变量。
- 大多数以点开头的特殊源和目标，`.PHONY`、`.PRECIOUS` 和 `.SUFFIXES` 显著例外。
- 变量修饰符，`:old=new` 字符串替换除外，它不可移植地支持用 `%` 通配，历史上仅适用于声明后缀。
- `$>` 变量即使在其短形式中；大多数 make 支持此功能，但其名称各异。

某些功能更具可移植性，如 `+=`、`?=` 和 `!=` 赋值。`.PATH` 功能基于 GNU make 和许多 SVR4 make 版本中的较旧功能 `VPATH`；然而，历史上其行为定义不明确（且 bug 太多），无法依赖。

`$@` 和 `$<` 变量或多或少普遍可移植，`$(MAKE)` 变量也是如此。后缀规则的基本使用（仅当前目录中的文件，不试图将转换链接在一起等）也相当可移植。

## 参见

mkdep(1), [style.Makefile(5)](../man5/style.makefile.5.md)

## 历史

`make` 命令出现于 Version 7 AT&T UNIX。此 `make` 实现基于 Adam de Boor 为 Berkeley Sprite 编写的 pmake 程序。它设计为使用名为 “customs” 的守护进程在不同机器上运行作业的并行分布式 make。

历史上，目标/依赖 `FRC` 已用于强制重建（因为目标/依赖不存在……除非有人创建 `FRC` 文件）。

## 缺陷

`make` 语法难以解析。例如，查找变量使用结束应涉及扫描每个修饰符，对每个字段使用正确的终止符。在许多地方，`make` 仅通过计数 {} 和 () 来查找变量展开的结束。

无法在文件名中转义空格字符。

在作业模式中，当目标失败时；`make` 会将错误令牌放入作业令牌池。这将导致使用该令牌池的所有其他 `make` 实例中止构建并以错误码 6 退出。有时抑制不必要错误级联的尝试可能导致看似无法解释的 `*** Error code 6`
