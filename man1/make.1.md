  MAKE(1)  

MAKE(1)

FreeBSD General Commands Manual

MAKE(1)

[名称](#__u540D___u79F0_)
=======================

`make` —

维护程序依赖

[概要](#__u6982___u8981_)
=======================

`make` \[`-BeikNnqrSstWwX`\] \[`-C` directory\] \[`-D` variable\] \[`-d` flags\] \[`-f` makefile\] \[`-I` directory\] \[`-J` private\] \[`-j` max\_jobs\] \[`-m` directory\] \[`-T` file\] \[`-V` variable\] \[`-v` variable\] \[variable=value\] \[target ...\]

[描述](#__u63CF___u8FF0_)
=======================

`make` 是一个旨在简化其他程序维护的程序。它的输入是关于程序和其他文件所依赖的文件的规范列表。 如果没有给出 `-f` makefile 选项， `make` 尝试打开 ‘`makefile`’ 然后打开 ‘`Makefile`’ 以找到规范。 如果文件 ‘`.depend`’ 存在，则读取它（请参阅 mkdep(1) ）。

本手册页仅供参考。有关 `make` 和 makefiles 的更详细描述，请参阅 PMake - A Tutorial 。

`make` 将在解析之前将 MAKEFLAGS 环境变量的内容添加到命令行参数中。

选项如下：

[`-B`](#B)

通过对每个命令执行一个 shell 并通过执行命令来按顺序生成依赖行的源，尝试向后兼容。

[`-C`](#C) directory

在读取 makefile 或执行任何其他操作之前切换到 directory 。 如果指定多个 `-C` 选项，则每个选项都相对于前一个选项进行解释： `-C` / `-C` etc 等效于 `-C` /etc 。

[`-D`](#D) variable

在全局上下文中将 variable 定义为 1。

[`-d`](#d) \[-\]flags

打开调试，并指定 `make` 的哪些部分要打印调试信息。除非标志前面有 ‘`-`’ ，否则它们将被添加到 MAKEFLAGS 环境变量中，并且将由任何子 make 进程处理。默认情况下，调试信息打印到标准错误，但这可以使用 F 调试标志进行更改。调试输出总是无缓冲的；此外，如果启用调试但调试输出未定向到标准输出，则标准输出为行缓冲。 Flags 是以下一项或多项：

A

打印所有可能的调试信息；相当于指定所有的调试标志。

a

打印有关存档搜索和缓存的调试信息。

C

打印有关当前工作目录的调试信息。

c

打印有关条件评估的调试信息。

d

打印有关目录搜索和缓存的调试信息。

e

打印有关失败命令和目标的调试信息。

F\[**+**\]filename

指定写入调试输出的位置。这必须是最后一个标志，因为它消耗参数的其余部分。如果 ‘`F`’ 标志后面的字符是 ‘`+`’, 那么文件将以追加模式打开；否则文件将被覆盖。如果文件名是 ‘`stdout`’ 或 ‘`stderr`’ 则调试输出将分别写入标准输出或标准错误输出文件描述符（并且 ‘`+`’ 选项无效）。否则，输出将被写入指定文件。如果文件名以 ‘`.%d`’ 结尾，则 ‘`%d`’ 将替换为 pid。

f

打印有关循环评估的调试信息。

g1

在做任何事情之前打印输入图。

g2

在完成所有操作后或在出错退出之前打印输入图。

g3

在出错退出之前打印输入图。

h

打印有关哈希表操作的调试信息。

j

打印有关运行多个 shell 的调试信息。

L

打开 lint 检查。这将在分配时为未正确解析的变量分配引发错误，以便文件和行号可用。

l

打印 Makefile 中的命令，无论它们是否以 ‘`@`’ 或其他 "quiet" flags. 标志为前缀。也称为 "loud" 行为。

M

打印有关目标的 "meta" 模式决策的调试信息。

m

打印有关制作目标的调试信息，包括修改日期。

n

不要删除运行命令时创建的临时命令脚本。这些临时脚本在 `TMPDIR` 环境变量引用的目录中创建，如果 `TMPDIR` 未设置或设置为空字符串，则在 /tmp 中创建。临时脚本由 mkstemp(3) 创建，名称格式为 makeXXXXXX 。 _注意_: 这会在 `TMPDIR` 或 /tmp, 中创建许多文件，因此请小心使用。

p

打印有关 makefile 解析的调试信息。

s

打印有关后缀转换规则的调试信息。

t

打印有关目标列表维护的调试信息。

V

强制 `-V` 选项打印变量的原始值，覆盖通过 .MAKE.EXPAND\_VARIABLES 设置的默认行为。

v

打印有关变量分配的调试信息。

x

使用 `-x` 运行 shell 命令，以便在执行实际命令时打印它们。

[`-e`](#e)

指定环境变量覆盖 makefiles 中的宏分配。

[`-f`](#f) makefile

指定要读取的 makefile ，而不是默认的 ‘`makefile 。`’ 如果 makefile 是 ‘``` `-` ```’, 则读取标准输入。可以指定多个 makefile，并按指定的顺序读取。

[`-I`](#I) directory

指定要在其中搜索 makefile 和包含的 makefile 的目录。系统 makefile 目录（或目录，请参阅 `-m` 选项）自动包含在此列表中。

[`-i`](#i)

忽略 makefile 中 shell 命令的非零退出。等效于在 makefile 中的每个命令行之前指定 ‘``` `-` ```’ 。

[`-J`](#J) private

此选项 _不_ 应由用户指定。

当 j 选项在递归构建中使用时，此选项由 make 传递给子 make，以允许构建中的所有 make 进程协作以避免系统过载。

[`-j`](#j) max\_jobs

指定 `make` 可以在任何时候运行的最大作业数。该值保存在 .MAKE.JOBS 中。关闭兼容模式，除非还指定 B 标志。当兼容模式关闭时，与目标关联的所有命令都在单个 shell 调用中执行，而不是传统的每行一个 shell 调用。这可以打破在每次命令调用时更改目录的传统脚本，然后期望在下一行从新环境开始。更正脚本比打开向后兼容性更有效。

[`-k`](#k)

遇到错误后继续处理，但仅限于那些不依赖于其创建导致错误的目标的目标。

[`-m`](#m) directory

指定一个目录，在其中搜索 sys.mk 和通过 `<`file`>`\-style-
include 语句包含的 makefiles。 `-m` 选项可以多次使用以形成搜索路径。此路径将覆盖默认系统包含路径： /usr/share/mk。 此外，系统包含路径将附加到用于 `"`file`"`\-style 包含语句的搜索路径（请参阅 `-I` 选项）。

如果 `-m` 参数（或 `MAKESYSPATH` 环境变量）中的文件或目录名称以字符串 “.../” 开头，则 `make` 将搜索在参数字符串的剩余部分中命名的指定文件或目录。搜索从 Makefile 的当前目录开始，然后向上到文件系统的根目录。如果搜索成功，则生成的目录将替换 `-m` 参数中的 “.../” 规范。如果使用，此功能允许 `make` 在当前源代码树中轻松搜索自定义 sys.mk files 文件（例如，通过使用 “.../mk/sys.mk” 作为参数）。

[`-n`](#n)

显示将执行的命令，但不实际执行它们，除非目标依赖于 .MAKE 特殊源（见下文）或命令以 ‘``` `+` ```’ 为前缀。

[`-N`](#N)

显示本应执行但实际上并未执行的命令；可用于调试顶级 makefile 而无需进入子目录。

[`-q`](#q)

不执行任何命令，但如果指定的目标是最新的则退出 0，否则退出 1。

[`-r`](#r)

不要使用系统 makefile 中指定的内置规则。

[`-S`](#S)

如果遇到错误，则停止处理。这是默认行为，与 `-k` 相反。

[`-s`](#s)

不要在执行任何命令时回显它们。相当于在 makefile 中的每个命令行之前指定 ‘``` `@` ```’ 。

[`-T`](#T) tracefile

当与 `-j` 标志一起使用时，在 tracefile 中附加一个跟踪记录，为每个开始和完成的作业添加一个跟踪记录。

[`-t`](#t)

与其按照 makefile 中的指定重新构建目标，不如创建它或更新其修改时间以使其看起来是最新的。

[`-V`](#V) variable

打印 variable 的值。 不要构建任何目标。可以指定此选项的多个实例；变量将每行打印一个，每个空或未定义变量都有一个空行。在读取所有 makefile 后，从全局上下文中提取打印的值。默认情况下，会显示原始变量内容（可能包括其他未扩展的变量引用）。如果 variable 包含 ‘`$`’ ，则该值将在打印之前递归扩展为其完整的结果文本。如果 .MAKE.EXPAND\_VARIABLES 设置为 true 并且未使用 `-dV` 选项覆盖它，则扩展值也将被打印。请注意，循环局部变量和目标局部变量，以及在 makefile 处理期间由全局变量临时获取的值，无法通过此选项访问。 `-dv` 调试模式可以用来查看这些，但代价是生成大量的额外输出。

[`-v`](#v) variable

与 `-V` 类似，但变量始终扩展为其完整值。

[`-W`](#W)

将 makefile 解析期间的任何警告视为错误。

[`-w`](#w)

打印进入和离开目录消息，前后处理。

[`-X`](#X)

不要将命令行上传递的变量单独导出到环境中。在命令行上传递的变量仍然通过 MAKEFLAGS 环境变量导出。此选项在对命令参数大小有较小限制的系统上可能很有用。

variable=value

将变量变量的值 variable 设置为 value 。 通常，命令行上传递的所有值也会导出到环境中的子组件。 `-X` 标志禁用此行为。变量分配应遵循 POSIX 兼容性的选项，但不强制执行排序。

makefile 中有七种不同类型的行：文件依赖规范、shell 命令、变量赋值、包含语句、条件指令、for 循环和注释。

通常，可以通过以反斜杠 (‘`\`’) 结束行从一行继续到下一行。下一行的尾随换行符和初始空格被压缩为一个空格。

[文件依赖规范](#__u6587___u4EF6___u4F9D___u8D56___u89C4___u8303_)
===========================================================

依赖线由一个或多个目标、一个运算符和零个或多个源组成。这创建了一种关系，其中目标 “depend” 源并且通常是从它们创建的。如果目标不存在，或者其修改时间小于其任何源的修改时间，则认为该目标已过期。将重新创建一个过时的目标，但直到所有源都经过检查并根据需要重新创建它们自己之后。可以使用三个运算符：

[`:`](#:)

许多依赖行可能会命名这个目标，但只有一个可能附加 shell 命令。所有依赖行中命名的所有源都被一起考虑，如果需要，运行附加的 shell 命令来创建或重新创建目标。如果 `make` 被中断，则目标被删除。

[`!`](#!)

相同，但无论是否过期，都会重新创建目标。

[`::`](#::)

任何依赖行都可能附加 shell 命令，但每一个都是独立处理的：如果目标相对于（仅）那些源过期，则考虑其源并运行附加的 shell 命令。因此，可以根据情况运行不同组的附加 shell 命令。此外，与 `:` 不同的是，对于没有源的依赖行，附加的 shell 命令总是运行。与 `:` 不同的是，如果 `make` 被中断，目标不会被删除。

所有提及特定目标的依赖行必须使用相同的运算符。

目标和源可能包含 shell 通配符值 ‘`? 、`’ ‘`* 、`’ ‘`[]`’ 和 ‘`{} 。`’ 值 ‘`? 、`’ ‘`*`’ 和 ‘`[]`’ 只能用作目标或源的最终组件的一部分，并且必须用于描述现有文件。值 ‘`{}`’ 不一定用于描述现有文件。扩展是按目录顺序进行的，而不是像在 shell 中那样按字母顺序。

[SHELL 命令](#SHELL___u547D___u4EE4_)
===================================

每个目标都可能与一行或多行 shell 命令相关联，通常用于创建目标。此脚本中的每一行之前都 _必须_ 有一个制表符。（由于历史原因，不接受空格。）如果需要，目标可以出现在许多依赖行中，但默认情况下，创建脚本只能遵循这些规则之一。但是，如果使用 ‘``` `::` ```’ 运算符，则所有规则都可能包含脚本，并且脚本会按照找到的顺序执行。

每一行都被视为一个单独的 shell 命令，除非行尾用反斜杠 (‘`\`’) 转义，在这种情况下，该行和下一行被合并。 如果命令的第一个字符是 ‘``` `@ 、` ```’ ‘``` `+` ```’ 或 ‘``` `-` ```’ 的任意组合，则对该命令进行特殊处理。 ‘``` `@` ```’ 导致命令在执行之前不被回显。即使给出 `-n` ， ‘``` `+` ```’ 也会导致执行命令。这类似于 .MAKE 特殊源的效果，不同之处在于该效果可以限制为脚本的单行。兼容模式下的 ‘``` `-` ```’ 会导致命令行的任何非零退出状态被忽略。

当使用 `-j` max\_jobs 在作业模式下运行 `make` 时，目标的整个脚本将被馈送到 shell 的单个实例。在兼容（非作业）模式下，每个命令都在单独的进程中运行。如果命令包含任何 shell 元字符 (‘``#=|^(){};&<>*?[]:$`\\n``’) ，它将被传递给 shell；否则 `make` 将尝试直接执行。如果一行以 ‘``` `-` ```’ 开头并且 shell 启用 ErrCtl，则命令行失败将被忽略，因为在兼容模式下。否则 ‘``` `-` ```’ 会影响整个工作；脚本将在第一个失败的命令行处停止，但目标不会被视为失败。

应编写 Makefile 以使 `make` 操作模式不会改变其行为。例如，任何需要使用 “cd” 或 “chdir” 而不可能为后续命令更改目录的命令都应该放在括号中，以便在子shell中执行。要强制使用一个 shell，请转义换行符，以使整个脚本成为一个命令。例如：

avoid-chdir-side-effects: @echo Building $@ in \`pwd\` @(cd ${.CURDIR} && ${MAKE} $@) @echo Back in \`pwd\` ensure-one-shell-regardless-of-mode: @echo Building $@ in \`pwd\`; \\ (cd ${.CURDIR} && ${MAKE} $@); \\ echo Back in \`pwd\` 

由于 `make` 在执行任何目标之前会将 chdir(2) 转换为 ‘`.OBJDIR`’ ，因此每个子进程都以它作为其当前工作目录开始。

[变量赋值](#__u53D8___u91CF___u8D4B___u503C_)
=========================================

make 中的变量与 shell 中的变量非常相似，并且按照传统，由所有大写字母组成。

[变量赋值修饰符](#__u53D8___u91CF___u8D4B___u503C___u4FEE___u9970___u7B26_)
--------------------------------------------------------------------

可用于为变量赋值的五个运算符如下：

[`=`](#=)

将值分配给变量。任何先前的值都会被覆盖。

[`+=`](#+=)

将值附加到变量的当前值。

[`?=`](#?=)

如果尚未定义变量，则将值分配给该变量。

[`:=`](#:=)

扩展赋值，即在将值赋给变量之前扩展它。通常，在引用变量之前不会进行扩展。 _注意_: _未_ 扩展对未定义变量的引用。 当使用变量修饰符时，这可能会导致问题。

[`!=`](#!=)

展开该值并将其传递给 shell 执行并将结果分配给变量。结果中的任何换行符都将替换为空格。

删除分配 value 之前的任何空白；如果要附加值，则在变量的先前内容和附加值之间插入一个空格。

通过用花括号 (‘`{}`’) 或圆括号 (‘`()`’) 将变量名括起来并在其前面加上美元符号 (‘`$`’) 来扩展变量。如果变量名仅包含一个字母，则不需要大括号或圆括号。不推荐使用这种较短的形式。

如果变量名称包含一个美元，则名称本身首先被扩展。这允许几乎任意的变量名称，但是最好避免使用包含美元、大括号、括号或空格的名称！

如果扩展变量的结果包含美元符号 (‘`$`’) ，则再次扩展字符串。

变量替换发生在三个不同的时间，具体取决于变量的使用位置。

1.  依赖行中的变量在读取行时被扩展。
2.  当 shell 命令执行时，shell 命令中的变量会被扩展。
3.  “.for” 循环索引变量在每次循环迭代时扩展。请注意，其他变量不会在循环内展开，因此以下示例代码：
    
        .for i in 1 2 3
        
    
    将打印：
    
    1 2 3 3 3 3 
    
    因为在循环执行后 ${a} 包含 “1 2 3” 而 ${b} 包含 “${j} ${j} ${j}” ，然后扩展为 “3 3 3” ，因为在循环结束后， ${j} 包含 “3 。”

[变量类](#__u53D8___u91CF___u7C7B_)
--------------------------------

四种不同类别的变量（按优先级递增的顺序）是：

环境变量

定义为 `make`环境的一部分的变量。

全局变量

在 makefile 或包含的 makefile 中定义的变量。

命令行变量

定义为命令行一部分的变量。

局部变量

特定于特定目标定义的变量。

局部变量都是内置的，它们的值因目标而异。目前无法定义新的局部变量。七个局部变量如下：

.ALLSRC

此目标的所有来源列表；也称为 ‘`>`’.

.ARCHIVE

存档文件的名称；也称为 ‘`! 。`’

.IMPSRC

在后缀转换规则中，要转换目标的源的名称/路径（ “implied” 源）；也称为 ‘`<`’ 。它没有在明确的规则中定义。

.MEMBER

档案成员的姓名；也称为 ‘`% 。`’

.OODATE

该目标的被视为过时的来源列表；也称为 ‘`? 。`’

.PREFIX

目标的文件前缀，只包含文件部分，没有后缀或前面的目录组件；也称为 ‘`* 。`’ 后缀必须是用 `.SUFFIXES` 声明的已知后缀之一，否则将无法识别。

.TARGET

目标名称；也称为 ‘`@ 。`’ 。为了与其他品牌兼容，这是存档成员规则中 `.ARCHIVE` 的别名。

较短的形式 (‘`> 、`’ ‘`! 、`’ ‘`< 、`’ ‘`% 、`’ ‘`? 、`’ ‘`*`’ 和 ‘`@`’) 允许向后兼容历史 makefile 和遗留 POSIX make，但不推荐使用。

标点符号后面紧跟 ‘`D`’ 或 ‘`F`’ 的这些变量的变体，例如 ‘`$(@D)`’ ，是等效于使用 ‘`:H`’ 和 ‘`:T`’ 修饰符的传统形式。接受这些形式是为了与 AT&T System V UNIX 和 POSIX 兼容，但不推荐使用。

四个局部变量可以在依赖行的源中使用，因为它们扩展为行上每个目标的正确值。这些变量是 ‘`.TARGET 、`’ ‘`.PREFIX 、`’ ‘`.ARCHIVE`’ 和 ‘`.MEMBER 。`’

[其他内置变量](#__u5176___u4ED6___u5185___u7F6E___u53D8___u91CF_)
-----------------------------------------------------------

此外， `make` 设置或知道以下变量：

$

单个美元符号 ‘`$`’ ，即 ‘`$$`’ 扩展为单个美元符号。

.ALLTARGETS

Makefile 中遇到的所有目标的列表。如果在 Makefile 解析期间进行评估，则仅列出迄今为止遇到的那些目标。

.CURDIR

执行 `make` 的目录的路径。有关详细信息，请参阅 ‘``` `PWD` ```’ 的描述。

.INCLUDEDFROMDIR

包含此 Makefile 的文件的目录。

.INCLUDEDFROMFILE

包含此 Makefile 的文件的文件名。

[`MAKE`](#MAKE)

使用 (argv\[0\]) 执行 `make` 的名称。为了兼容性， `make` 还将 .MAKE 设置为相同的值。首选使用的变量是环境变量 `MAKE` 因为它与其他版本的 `make` 更兼容，并且不会与同名的特殊目标混淆。

.MAKE.ALWAYS\_PASS\_JOB\_QUEUE

告诉 `make` 是否传递作业令牌队列的描述符，即使目标没有用 `.MAKE` 标记。默认为 ‘`yes`’ 以向后兼容 FreeBSD 9.0 和更早版本。

.MAKE.DEPENDFILE

命名从中读取生成的依赖项的生成文件（默认为 ‘`.depend`’ ）。

.MAKE.EXPAND\_VARIABLES

一个布尔值，用于控制 `-V` 选项的默认行为。如果为 true，则使用 `-V` 打印的变量值将完全展开；如果为 false，则显示原始变量内容（可能包括其他未扩展的变量引用）。

.MAKE.EXPORTED

`make` 导出的变量列表。

.MAKE.JOBS

[`-j`](#j_2) 选项的参数。

.MAKE.JOB.PREFIX

如果使用 j 运行 `make` ，则每个目标的输出都以标记 ‘`--- target ---`’ 为前缀，其第一部分可以通过 .MAKE.JOB.PREFIX 控制。如果 .MAKE.JOB.PREFIX 为空，则不打印任何标记。-
例如： `.MAKE.JOB.PREFIX=${.newline}---${.MAKE:T}[${.MAKE.PID}]` 会产生类似 ‘`---make[1234] target ---`’ 使得更容易跟踪正在实现的并行度。

[`MAKEFLAGS`](#MAKEFLAGS)

环境变量 ‘``` `MAKEFLAGS` ```’ 可能包含任何可以在 `make`命令行中指定的内容。在 `make`的命令行上指定的任何内容都附加到 ‘``` `MAKEFLAGS` ```’ 变量中，然后将其输入到 `make` 执行的所有程序的环境中。

.MAKE.LEVEL

`make` 的递归深度。 `make` 的初始实例将为 0，并将递增的值放入环境中以供下一代看到。这允许像这样的测试： `.if ${.MAKE.LEVEL} == 0` 来保护应该只在 `make` 的初始实例中评估的东西。

.MAKE.MAKEFILE\_PREFERENCE

`make` 将查找的 makefile 名称的有序列表（默认为 ‘`makefile 、`’ ‘`Makefile`’) 。

.MAKE.MAKEFILES

`make` 读取的 makefile 列表，这对于跟踪依赖关系很有用。每个 makefile 只记录一次，与读取的次数无关。

.MAKE.MODE

读取所有 makefile 后处理。可以影响 `make` 运行的模式。它可以包含许多关键字：

兼容

与 `-B` 一样，将 `make` 置于“兼容”模式。

meta

将 `make` 放置到“meta”模式中，为每个目标创建meta文件，以捕获命令运行、生成的输出，如果 filemon(4) 可用，则对 `make` 感兴趣的系统调用。 在诊断错误时，捕获的输出非常有用。

curdirOk= bf

通常 `make` 不会在 ‘`.CURDIR`’ 中创建 .meta 文件。这可以通过将 bf 设置为代表 True 的值来覆盖。

missing-meta= bf

如果 bf 为 True，则缺少 .meta 文件会使目标过期。

missing-filemon= bf

如果 bf 为 True，则缺少 filemon 数据会使目标过期。

nofilemon

不要使用 filemon(4) 。

env

对于调试，将环境包含在 .meta 文件中会很有用。

verbose

如果处于 "meta" 模式，则打印有关正在构建的目标的线索。如果构建以其他方式静默运行，这将很有用。该消息打印了以下值 .MAKE.META.PREFIX 。

ignore-cmd

一些 makefile 的命令根本不稳定。此关键字导致它们被忽略以确定目标是否在 "meta" 模式下过时。另请参见 `.NOMETA_CMP 。`

silent= bf

如果 bf 为 True，则在创建 .meta 文件时，将目标标记为 `.SILENT 。`

.MAKE.META.BAILIWICK

在 "meta" 模式下，提供与 `make` 控制的目录匹配的前缀列表。如果在 .OBJDIR 之外但在所述辖区内生成的文件丢失，则当前目标被视为已过期。

.MAKE.META.CREATED

在 "meta" 模式下，此变量包含更新的所有元文件的列表。如果不为空，则可用于触发对 .MAKE.META.FILES 的处理。

.MAKE.META.FILES

在 "meta" 模式下，此变量包含所有使用的元文件的列表（更新与否）。该列表可用于处理元文件以提取依赖信息。

.MAKE.META.IGNORE\_PATHS

提供应忽略的路径前缀列表；因为内容预计会随着时间而改变。默认列表包括 ‘`/dev /etc /proc /tmp /var/run /var/tmp`’

.MAKE.META.IGNORE\_PATTERNS

提供与路径名匹配的模式列表。忽略任何匹配

.MAKE.META.IGNORE\_FILTER

提供要应用于每个路径名的变量修饰符列表。如果扩展是空字符串，则忽略。

.MAKE.META.PREFIX

定义为在 "meta verbose" 模式下更新的每个元文件打印的消息。默认值为：

`Building ${.TARGET:H:tA}/${.TARGET:T}`

.MAKEOVERRIDES

此变量用于记录分配给命令行的变量的名称，以便它们可以作为 ‘``` `MAKEFLAGS` ```’ 的一部分导出。可以通过在生成文件中为 ‘`.MAKEOVERRIDES`’ 分配一个空值来禁用此行为。额外的变量可以通过将它们的名称附加到 ‘`.MAKEOVERRIDES`’ 来从生成文件中导出。每当修改 ‘`.MAKEOVERRIDES`’ 时，都会重新导出 ‘``` `MAKEFLAGS` ```’ 。

.MAKE.PATH\_FILEMON

如果 `make` 是使用 filemon(4) 支持构建的，则将其设置为设备节点的路径。这允许 makefile 测试这种支持。

.MAKE.PID

`make` 的进程 ID。

.MAKE.PPID

`make` 的父进程 ID。

.MAKE.SAVE\_DOLLARS

值应该是一个布尔值，用于控制在执行 ‘`:=`’ 分配时是否保留 ‘`$$`’ 为了向后兼容，默认值为 false。设置为 true 以与其他品牌兼容。如果设置为 false，则根据正常评估规则， ‘`$$`’ 将变为 ‘`$`’ 。

.MAKE.UID

运行 `make` 的用户 ID。

.MAKE.GID

运行 `make` 的组 ID。

MAKE\_PRINT\_VAR\_ON\_ERROR

当 `make` 由于错误而停止时，它会将 ‘`.ERROR_TARGET`’ 设置为失败目标的名称，将 ‘`.ERROR_CMD`’ 设置为失败目标的命令，在 "meta" 模式下，它还将 ‘`.ERROR_CWD`’ 设置为 getcwd(3) 和 ‘`.ERROR_META_FILE`’ 指向描述失败目标的元文件（如果有）的路径。然后它会打印其名称和 ‘`.CURDIR`’ 的值以及 ‘`MAKE_PRINT_VAR_ON_ERROR`’ 中命名的任何变量的值。

.newline

这个变量被简单地分配一个换行符作为它的值。这允许使用 `:@` 修饰符在循环的迭代之间放置换行符而不是空格。例如， ‘`MAKE_PRINT_VAR_ON_ERROR`’ 的打印可以作为 ${MAKE\_PRINT\_VAR\_ON\_ERROR:@v@$v='${$v}'${.newline}@} 完成。

.OBJDIR

构建目标的目录的路径。它的值是通过尝试 chdir(2) 按顺序访问以下目录并使用第一个匹配项来确定的：

1.  [`${MAKEOBJDIRPREFIX}${.CURDIR}`](#$_MAKEOBJDIRPREFIX_$_.CURDIR_)
    
    (仅当在环境或命令行中设置 ‘``` `MAKEOBJDIRPREFIX` ```’ 时。)
    
2.  [`${MAKEOBJDIR}`](#$_MAKEOBJDIR_)
    
    (仅当在环境或命令行中设置 ‘``` `MAKEOBJDIR` ```’ 时。)
    
3.  [`${.CURDIR}`](#$_.CURDIR_)/obj.`${MACHINE}`
4.  [`${.CURDIR}`](#$_.CURDIR__2)/obj
5.  /usr/obj/`${.CURDIR}`
6.  [`${.CURDIR}`](#$_.CURDIR__3)

变量扩展在使用之前对值执行，因此表达式如

`${.CURDIR:S,^/usr/src,/var/obj,}`

可能用过。这对 ‘``` `MAKEOBJDIR` ```’ 特别有用。

‘`.OBJDIR`’ 可以通过特殊目标 ‘``` `.OBJDIR` ```’ 在makefile 中修改。在所有情况下，如果指定目录存在， `make` 会将 chdir(2) 设置到该目录，并在执行任何目标之前将 ‘`.OBJDIR`’ 和 ‘``` `PWD` ```’ 设置为该目录。

除了显式的 ‘``` `.OBJDIR` ```’ 目标， `make` 将检查指定的目录是否可写，如果不是，则忽略它。可以通过将环境变量 ‘``` `MAKE_OBJDIR_CHECK_WRITABLE` ```’ 设置为 "no" 来跳过此检查。

.PARSEDIR

正在解析的当前 ‘`Makefile`’ 目录的路径。

.PARSEFILE

正在解析的当前 ‘`Makefile`’ 的基本名称。此变量和 ‘`.PARSEDIR`’ 都仅在解析 ‘`Makefiles`’ 时设置。如果要保留它们的当前值，请使用扩展赋值将它们分配给变量： (‘``` `:= 。` ```’)

.PATH

表示 `make` 的目录列表的变量将搜索文件。应使用目标 ‘`.PATH`’ 而不是变量来更新搜索列表。

[`PWD`](#PWD)

当前目录的备用路径。 `make` 通常将 ‘`.CURDIR`’ 设置为 getcwd(3) 给出的规范路径。但是，如果设置环境变量 ‘``` `PWD` ```’ 被设置并给出当前目录的路径，那么 `make` 将 ‘`.CURDIR`’ 设置为 ‘``` `PWD` ```’ 的值。 如果设置 ‘``` `MAKEOBJDIRPREFIX` ```’ 或 ‘``` `MAKEOBJDIR` ```’ 包含变量转换，则会禁用此行为。对于 `make` 执行的所有程序， ‘``` `PWD` ```’ 设置为 ‘`.OBJDIR`’ 的值。

[`.SHELL`](#.SHELL)

用于运行目标脚本的 shell 的路径名。它是只读的。

[`.TARGETS`](#.TARGETS)

命令行上明确指定的目标列表（如果有）。

[`VPATH`](#VPATH)

用冒号分隔 (“:”) 的目录列表， `make` 将搜索文件。该变量仅支持与旧的 make 程序兼容，请改用 ‘`.PATH`’ 。

[变量修饰符](#__u53D8___u91CF___u4FEE___u9970___u7B26_)
--------------------------------------------------

可以修改变量扩展以选择或修改变量的每个单词（其中 “word” 是空格分隔的字符序列）。变量展开的一般格式如下：

`${variable[:modifier[:...]]}`

每个修饰符都以冒号开头，可以用反斜杠 (‘`\`’) 转义。

可以通过变量指定一组修饰符，如下所示：

`modifier_variable=modifier[:...]`

`${variable:${modifier_variable}[:...]}`

在这种情况下，modifier\_variable 中的第一个修饰符不以冒号开头，因为它必须出现在引用变量中。如果modifier\_variable 中的任何修饰符包含美元符号 (‘`$`’), 则必须将它们加倍以避免早期扩展。

支持的修饰符有：

[`:E`](#:E)

将变量中的每个单词替换为其后缀。

[`:H`](#:H)

将变量中的每个单词替换为除最后一个组件之外的所有内容。

[`:M`](#:M)pattern

只选择那些匹配 pattern 的单词。可以使用标准的 shell 通配符 (‘`*`’, ‘`?`’, 和 ‘`[]`’) 。通配符可以用反斜杠 (‘`\`’) 转义。由于值被拆分为单词，匹配，然后连接的方式，一个类似的结构

`${VAR:M*}`

将规范字间距，删除所有前导和尾随空格，并将多个连续空格转换为单个空格。

[`:N`](#:N)pattern

这与 ‘``` `:M` ```’ 相同，但会选择所有不匹配 pattern 的单词。

[`:O`](#:O)

按字母顺序对变量中的每个单词进行排序。

[`:Or`](#:Or)

以相反的字母顺序对变量中的每个单词进行排序。

[`:Ox`](#:Ox)

随机播放变量中的单词。每次引用修改后的变量时，结果都会有所不同；使用扩展赋值 (‘``` `:=` ```’) 来防止这种行为。例如，

LIST= uno due tre quattro RANDOM\_LIST= ${LIST:Ox} STATIC\_RANDOM\_LIST:= ${LIST:Ox} 全部： @echo "${RANDOM\_LIST}" @echo "${RANDOM\_LIST}" @echo "${STATIC\_RANDOM\_LIST}" @echo "${STATIC\_RANDOM\_LIST}" 

可能会产生类似于以下内容的输出：

quattro due tre uno tre due quattro uno due uno quattro tre due uno quattro tre 

[`:Q`](#:Q)

引用变量中的每个 shell 元字符，以便可以安全地将其传递给 shell。

[`:q`](#:q)

引用变量中的每个 shell 元字符，并将 ‘$’ 字符加倍，以便可以通过 `make` 的递归调用安全地传递它。这相当于： ‘:S/\\$/&&/g:Q 。’

[`:R`](#:R)

将变量中的每个单词替换为除其后缀之外的所有单词。

[`:range[=count]`](#:range_=count_)

该值是一个整数序列，表示原始值的单词或提供的 count 。

[`:gmtime[=utc]`](#:gmtime_=utc_)

该值是 strftime(3) 的格式字符串，使用 gmtime(3) 。如果未提供 utc 值或为 0，则使用当前时间。

[`:hash`](#:hash)

计算值的 32 位散列并将其编码为十六进制数字。

[`:localtime[=utc]`](#:localtime_=utc_)

该值是 strftime(3) 的格式字符串，使用 localtime(3) 。如果未提供 utc 值或为 0，则使用当前时间。

[`:tA`](#:tA)

尝试使用 realpath(3) 将变量转换为绝对路径，如果失败，则值不变。

[`:tl`](#:tl)

将变量转换为小写字母。

[`:ts`](#:ts)c

变量中的单词通常在展开时用空格分隔。此修饰符将分隔符设置为字符 c 。如果省略 c ，则不使用分隔符。常见的转义（包括八进制数字代码）按预期工作。

[`:tu`](#:tu)

将变量转换为大写字母。

[`:tW`](#:tW)

使值被视为单个单词（可能包含嵌入的空格）。也可以看看 ‘``` `:[*] 。` ```’

[`:tw`](#:tw)

使值被视为由空格分隔的单词序列。也可以看看 ‘``` `:[@] 。` ```’

[`:S`](#:S)/old\_string/new\_string/\[`1gW`\]

修改变量值的每个单词中第一次出现的 old\_string 将其替换为 new\_string 。 如果将 ‘`g`’ 附加到模式的最后一个分隔符，则每个单词中的所有出现都将被替换。如果将 ‘`1`’ 附加到模式的最后一个分隔符，则仅影响第一次出现。如果将 ‘`W`’ 附加到模式的最后一个分隔符，则该值将被视为单个单词（可能包含嵌入的空白）。 如果 old\_string 以插入符号 (‘`^`’) 开头，则 old\_string 锚定在每个单词的开头。如果 old\_string 以美元符号 (‘`$`’) 结尾，则它锚定在每个单词的末尾。在 new\_string 中，与号 (‘`&`’) 被 old\_string 替换（没有任何 ‘`^`’ 或 ‘`$`’ ）。 任何字符都可以用作修饰符字符串部分的分隔符。 锚定符、和符和分隔符可以用反斜杠 (‘`\`’) 转义。

变量扩展在 old\_string 和 new\_string 中以正常方式发生，唯一的例外是使用反斜杠来防止美元符号 (‘`$`’) 的扩展，而不是通常的前面的美元符号。

[`:C`](#:C)/pattern/replacement/\[`1gW`\]

`:C` 修饰符与 `:S` 修饰符类似，只是新旧字符串不是简单的字符串，而是扩展的正则表达式（参见 regex(3) ）字符串 pattern 和 ed(1)\-style 的字符串 replacement 。 通常情况下，模式 pattern 在值的每个单词中第一次出现时被替换为 replacement 。 ‘`1`’-
修饰符导致替换最多应用于一个单词； ‘`g`’ 修饰语使替换应用于搜索模式 pattern 实例数量与出现在该词或该词中的实例数量相同; ‘`W`’ 修饰符会将该值视为单个单词(可能包含嵌入的空格)。

至于 `:S` 修饰符， pattern 和 replacement 在被解析为正则表达式之前要经过变量扩展。

[`:T`](#:T)

将变量中的每个单词替换为其最后一个路径组件。

[`:u`](#:u)

删除相邻的重复词（如 uniq(1) ）。

[`:?`](#:_&?)true\_string`:`false\_string

如果变量名（不是它的值）在解析为 .if 条件表达式时计算为 true，则返回 true\_string 作为其值，否则返回 false\_string 。 由于变量名用作表达式， :? 必须是变量名本身之后的第一个修饰符——当然，它通常包含变量扩展。一个常见的错误是尝试使用类似的表达式

`${NUMBERS:M42:?match:no}`

实际测试定义 defined(NUMBERS), 以确定是否有任何单词匹配 "42" ，你需要使用类似的东西：

`${"${NUMBERS:M42}" != "":?match:no}.`

:old\_string=new\_string

这是 AT&T System V UNIX 风格的变量替换。它必须是指定的最后一个修饰符。如果 old\_string 或 new\_string 不包含模式匹配字符 % 则假定它们锚定在每个单词的末尾，因此只能替换后缀或整个单词。否则 % 是 old\_string 的子字符串，要在 new\_string 中替换。如果只有 old\_string 包含模式匹配字符 %, 并且 old\_string 匹配，那么结果就是 new\_string 。如果只有 new\_string 包含模式匹配字符 %, 则不会对其进行特殊处理，并且在匹配时将其打印为文字 % 。如果在 new\_string 或 old\_string 中有多个模式匹配字符 (%) ，则只有第一个实例被特殊处理（作为模式字符）； 所有后续实例都被视为正则字符。

变量扩展在 old\_string 和 new\_string 中以正常方式发生，唯一的例外是使用反斜杠来防止美元符号 (‘`$`’)-
的扩展，而不是通常的前面的美元符号。

[`:@`](#:@)temp`@`string`@`

这是来自 OSF 开发环境 (ODE) 的循环扩展机制。与 `.for` 循环不同，扩展发生在引用时。将 temp 分配给变量中的每个单词并计算 string 。 ODE 约定是 temp 应该以句点开头和结尾。例如。

`${LINKS:@.LINK.@${LN} ${TARGET} ${.LINK.}@}`

然而，单个字符变量通常更具可读性：

`${MAKE_PRINT_VAR_ON_ERROR:@v@$v='${$v}'${.newline}@}`

[`:_[=var]`](#:__=var_)

将当前变量值保存在 ‘`$_`’ 或命名的 var 中以供以后参考。示例用法：

M\_cmpv.units = 1 1000 1000000 M\_cmpv = S,., ,g:\_:range:@i@+ $${\_:\[-$$i\]} \\ \\\* $${M\_cmpv.units:\[$$i\]}@:S,^,expr 0 ,1:sh `.if ${VERSION:${M_cmpv}} < ${3.1.12:L:${M_cmpv}}`  

这里 ‘`$_`’ 用于保存 ‘`:S`’ 修饰符的结果，稍后使用来自 ‘`:range`’ 的索引值引用该修饰符。

[`:U`](#:U)newval

如果变量未定义，则 newval 为值。如果定义变量，则返回现有值。这是另一个 ODE 制作功能。例如，设置每个目标 CFLAGS 很方便：

`${_${.TARGET:T}_CFLAGS:U${DEF_CFLAGS}}`

如果仅在变量未定义时才需要值，请使用：

`${VAR:D:Unewval}`

[`:D`](#:D)newval

如果定义变量，则 newval 是值。

[`:L`](#:L)

变量的名称就是值。

[`:P`](#:P)

与变量同名的节点的路径就是值。如果不存在这样的节点或其路径为空，则使用变量的名称。为了使此修饰符起作用，名称（节点）必须至少出现在依赖项的 rhs 上。

[`:!`](#:_&!)cmd`!`

运行 cmd 的输出是值。

[`:sh`](#:sh)

如果变量不为空，它将作为命令运行，并且输出变为新值。

[`::=`](#::=)str

变量在替换后被赋值为 str 。此修饰符及其变体在一些晦涩的情况下很有用，例如在解析 shell 命令时想要设置一个变量。 这些赋值修饰符总是没有扩展，所以如果单独出现在规则行中，应该在前面加上一些东西以保持 `make` 愉快。

‘``` `::` ```’ 有助于避免与 AT&T System V UNIX 样式 `:=` 修饰符的错误匹配，并且由于总是发生替换，因此 `::=` 形式是模糊的合适的。

[`::?=`](#::?=)str

至于 `::=` 但前提是变量还没有值。

[`::+=`](#::+=)str

将 str 附加到变量。

[`::!=`](#::!=)cmd

将 cmd 的输出分配给变量。

[`:[`](#:_&_)range`]`

从值中选择一个或多个单词，或执行与将值划分为单词的方式相关的其他操作。

通常，值被视为由空格分隔的单词序列。一些修饰符会抑制这种行为，导致值被视为单个单词（可能包含嵌入的空格）。空值或完全由空格组成的值被视为单个单词。出于 ‘``` `:[]` ```’ 修饰符的目的，单词使用正整数（其中索引 1 表示第一个单词）向前索引，并且使用负整数向后索引（其中索引 -1 表示最后一个单词）。

range 进行变量扩展，扩展结果随后解释如下：

index

从值中选择一个单词。

start`..`end

选择从 start 到 end 的所有单词，包括在内。例如， ‘``` `:[2..-1]` ```’ 选择从第二个单词到最后一个单词的所有单词。如果 start 大于 end ，则以相反的顺序输出单词。例如， ‘``` `:[-1..1]` ```’ 选择从最后到第一个的所有单词。如果列表已经排序，那么这将有效地反转列表，但使用 ‘``` `:Or` ```’ 而不是 ‘``` `:O:[-1..1]` ```’ 更有效。

[`*`](#*)

导致后续修饰符将该值视为单个单词（可能包含嵌入的空格）。类似于 Bourne shell 中 "$\*" 的效果。

0

与 ‘``` `:[*]` ```’ 的含义相同。

[`@`](#@)

导致后续修饰符将该值视为由空格分隔的单词序列。类似于 Bourne shell 中 "$@" 的效果。

[`#`](#_)

返回值中的单词数。

[包括语句、条件和 for 循环](#__u5305___u62EC___u8BED___u53E5___u3001___u6761___u4EF6___u548C__for___u5FAA___u73AF_)
=========================================================================================================

Makefile 包含、条件结构和让人想起 C 编程语言的 for 循环在 `make` 中提供。所有此类结构都由以单个点 (‘`.`’) 字符开头的行标识。文件包含在 `.include <`file`>` 或 `.include "`file`"`. 中。尖括号或双引号之间的变量被扩展以形成文件名。如果使用尖括号，则包含的 makefile 应位于系统 makefile 目录中。如果使用双引号，则在系统 makefile 目录之前搜索包含 makefile 的目录和使用 `-I` 选项指定的任何目录。为了与其他版本的 `make` ‘`include file ...`’ 兼容，也可以接受。

如果包含语句写为 `.-include` 或 `.sinclude` ，则忽略定位和/或打开包含文件的错误。

如果将 include 语句写为 `.dinclude` ，则不仅会忽略定位和/或打开包含文件的错误，而且会忽略包含文件中的陈旧依赖项，就像 .MAKE.DEPENDFILE 一样。

条件表达式前面也有一个点作为行的第一个字符。可能的条件如下：

[`.error`](#.error) message

该消息与 makefile 的名称和行号一起打印，然后 `make` 将立即退出。

[`.export`](#.export) variable ...

导出指定的全局变量。如果未提供变量列表，则导出所有全局变量，内部变量除外（以 ‘`.`’ 开头的变量）。这不受 `-X` 标志的影响，因此应谨慎使用。为了与其他 `make` 程序兼容， ‘`export variable=value`’ 也被接受。

将变量名称附加到 .MAKE.EXPORTED 相当于导出变量。

[`.export-env`](#.export-env) variable ...

与 ‘`.export`’ 相同，只是变量未附加到 .MAKE.EXPORTED 。 这允许将值导出到与 `make` 内部使用的不同的环境中。

[`.export-literal`](#.export-literal) variable ...

与 ‘`.export-env`’ 相同，只是值中的变量不展开。

[`.info`](#.info) message

该消息与生成文件的名称和行号一起打印。

[`.undef`](#.undef) variable ...

取消定义指定的全局变量。只有全局变量可以未定义。

[`.unexport`](#.unexport) variable ...

与 ‘`.export`’ 相反。指定的全局 variable 将从 .MAKE.EXPORTED 中删除。如果没有提供变量列表，则所有全局变量都不会导出，并且 .MAKE.EXPORTED 会被删除。

[`.unexport-env`](#.unexport-env)

取消导出之前导出的所有全局变量并清除从父级继承的环境。此操作会导致原始环境内存泄漏，应谨慎使用。测试 .MAKE.LEVEL 为 0 是有意义的。另请注意，如果需要，应明确保留源自父环境的任何变量。例如：

    .if ${.MAKE.LEVEL} == 0
    

将导致仅包含 ‘``` `PATH` ```’ 的环境，这是最小的有用环境。实际上 ‘``` `.MAKE.LEVEL` ```’ 也将被推入新环境。

[`.warning`](#.warning) message

以 ‘`warning:`’ 为前缀的消息与生成文件的名称和行号一起打印。

[`.if`](#.if) \[!\]expression \[operator expression ...\]

测试表达式的值。

[`.ifdef`](#.ifdef) \[!\]variable \[operator variable ...\]

测试变量的值。

[`.ifndef`](#.ifndef) \[!\]variable \[operator variable ...\]

测试变量的值。

[`.ifmake`](#.ifmake) \[!\]target \[operator target ...\]

测试正在构建的目标

[`.ifnmake`](#.ifnmake) \[!\] target \[operator target ...\]

测试正在构建的目标。

[`.else`](#.else)

颠倒最后一个条件的意义。

[`.elif`](#.elif) \[!\] expression \[operator expression ...\]

‘``` `.else` ```’ 后跟 ‘``` `.if` ```’ 的组合。

[`.elifdef`](#.elifdef) \[!\]variable \[operator variable ...\]

‘``` `.else` ```’ 后跟 ‘``` `.ifdef` ```’ 的组合。

[`.elifndef`](#.elifndef) \[!\]variable \[operator variable ...\]

‘``` `.else` ```’ 后跟 ‘``` `.ifndef` ```’ 的组合。

[`.elifmake`](#.elifmake) \[!\]target \[operator target ...\]

‘``` `.else` ```’ 后跟 ‘``` `.ifmake` ```’ 的组合。

[`.elifnmake`](#.elifnmake) \[!\]target \[operator target ...\]

‘``` `.else` ```’ 后跟 ‘``` `.ifnmake` ```’ 的组合。

[`.endif`](#.endif)

结束条件的主体。

operator 可以是以下任何一种：

[`||`](#__&_)

逻辑或。

[`&&`](#&&)

逻辑与；优先级高于 “|| 。”

与在 C 中一样， `make` 只会在确定其值所需的范围内评估条件。括号可用于更改评估顺序。布尔运算符 ‘``` `!` ```’ 可用于逻辑否定整个条件。它的优先级高于 ‘``` `&& 。` ```’

expression 的值可以是以下任何一种：

[`defined`](#defined)

将变量名称作为参数，如果已定义变量，则计算结果为 true。

[`make`](#make)

将目标名称作为参数，如果目标被指定为 `make`命令行的一部分或在包含条件的行之前被声明为默认目标（隐式或显式，请参阅 .MAIN ），则计算结果为 true。

[`empty`](#empty)

接受一个带有可能修饰符的变量，如果变量的扩展将导致一个空字符串，则计算结果为 true。

[`exists`](#exists)

将文件名作为参数，如果文件存在，则计算结果为真。在系统搜索路径上搜索该文件（请参阅 .PATH ）。

[`target`](#target)

将目标名称作为参数，如果已定义目标，则计算结果为 true。

[`commands`](#commands)

将目标名称作为参数，如果目标已定义且具有与之关联的命令，则计算结果为 true。

Expression 也可以是算术或字符串比较。在比较的两侧进行变量扩展，然后比较数值。如果值前面有 0x，则将其解释为十六进制，否则为十进制；不支持八进制数。标准的 C 关系运算符都受支持。如果在变量扩展之后， ‘``` `==` ```’ 或 ‘``` `!=` ```’ 运算符的左侧或右侧不是数值，则在扩展变量之间执行字符串比较。如果没有给出关系运算符，则假定扩展变量与 0 进行比较，或者在字符串比较的情况下为空字符串。

当 `make` 正在评估这些条件表达式之一时，它遇到一个它无法识别的（空格分隔的）单词， “make” 或 “defined” 表达式将应用于它，具体取决于条件的形式。如果形式是 ‘``` `.ifdef 、` ```’ ‘``` `.ifndef` ```’ 或 ‘``` `.if` ```’ ，则应用 “defined” 表达式。同样，如果形式是 ‘``` `.ifmake` ```’ 或 ‘``` `.ifnmake` ```’, 则应用 “make” 表达式。

如果条件评估为真，则生成文件的解析将像以前一样继续。如果计算结果为 false，则跳过以下行。在这两种情况下，这一直持续到找到 ‘``` `.else` ```’ 或 ‘``` `.endif` ```’ 为止。

For 循环通常用于将一组规则应用于文件列表。for 循环的语法是：

[`.for`](#.for) variable \[variable ...\] `in` expression

⟨make-lines⟩

[`.endfor`](#.endfor)

在对 for `expression` 求值后，将其拆分为单词。在循环的每次迭代中，按顺序将一个单词分配给每个 `variable`, 然后将这些 `variables` 替换到 for 循环体内的 `make-lines` 中。字数必须是偶数；也就是说，如果有三个迭代变量，则提供的字数必须是三的倍数。

[注释](#__u6CE8___u91CA_)
=======================

注释以井号 (‘`#`’) 字符开始，在 shell 命令行以外的任何位置，并继续到未转义的新行的末尾。

[特殊来源（属性）](#__u7279___u6B8A___u6765___u6E90___uFF08___u5C5E___u6027___uFF09_)
=============================================================================

[`.EXEC`](#.EXEC)

Target 远不会过时，但始终执行命令。

[`.IGNORE`](#.IGNORE)

忽略与此目标关联的命令中的任何错误，就像它们都以破折号 (‘`-`’) 开头一样。

[`.MADE`](#.MADE)

将此目标的所有来源标记为最新。

[`.MAKE`](#.MAKE)

即使指定 `-n` 或 `-t` 选项，也要执行与此目标关联的命令。通常用于标记递归的 `make`。

[`.META`](#.META)

为目标创建一个元文件，即使它被标记为 `.PHONY 、` `.MAKE` 或 `.SPECIAL 。` 最有可能与 `.MAKE` 结合使用。在 "meta" 模式下，如果元文件丢失，则目标已过期。

[`.NOMETA`](#.NOMETA)

不要为目标创建元文件。也不会为 `.PHONY 、` `.MAKE` 或 `.SPECIAL` 目标创建元文件。

[`.NOMETA_CMP`](#.NOMETA_CMP)

在确定目标是否已过期时，请忽略命令中的差异。如果命令包含始终更改的值，这将很有用。但是，如果命令的数量发生变化，目标仍然会过时。相同的效果适用于使用变量 .OODATE的任何命令行，即使在不需要或不需要时也可用于该目的：

skip-compare-for-some: @echo this will be compared @echo this will not ${.OODATE:M.NOMETA\_CMP} @echo this will also be compared 

`:M` 模式抑制了不需要的变量的任何扩展。

[`.NOPATH`](#.NOPATH)

不要在 `.PATH` 指定的目录中搜索目标。

[`.NOTMAIN`](#.NOTMAIN)

如果没有指定目标，通常 `make` 会选择它遇到的第一个目标作为要构建的默认目标。此源可防止选择此目标。

[`.OPTIONAL`](#.OPTIONAL)

如果一个目标被标记这个属性并且 `make` 无法弄清楚如何创建它，它将忽略这个事实并假设该文件不需要或已经存在。

[`.PHONY`](#.PHONY)

目标与实际文件不对应；它总是被认为是过时的，并且不会使用 `-t` 选项创建。后缀转换规则不适用于 `.PHONY` 目标。

[`.PRECIOUS`](#.PRECIOUS)

当 `make` 被中断时，它通常会删除任何部分生成的目标。此源可防止目标被移除。

[`.RECURSIVE`](#.RECURSIVE)

[`.MAKE`](#.MAKE_2) 的同义词。

[`.SILENT`](#.SILENT)

不要回显与此目标关联的任何命令，就像它们都以 at 符号 (‘`@`’) 开头一样。

[`.USE`](#.USE)

将目标变成 `make`的宏版本。当目标用作另一个目标的源时，另一个目标获取源的命令、源和属性（ `.USE` 除外）。如果目标已经有命令，则将 `.USE` 目标的命令附加到它们。

[`.USEBEFORE`](#.USEBEFORE)

与 `.USE` 完全一样，但将 `.USEBEFORE` 目标命令添加到目标。

[`.WAIT`](#.WAIT)

如果 `.WAIT` 出现在依赖行中，则在它之前的源将在该行中后续的源之前生成。由于文件的依赖项是在文件本身可以生成之前才生成的，因此这也会停止生成依赖项，除非依赖项树的另一个分支需要它们。所以给出：

x: a .WAIT b echo x a: echo a b: b1 echo b b1: echo b1 

输出总是 ‘`a 、`’ ‘`b1 、`’ ‘`b 、`’ ‘`x 。`’-
`.WAIT` 强加的排序仅与并行 makes 有关。

[特殊目标](#__u7279___u6B8A___u76EE___u6807_)
=========================================

特殊目标可能不包含在其他目标中，即它们必须是唯一指定的目标。

[`.BEGIN`](#.BEGIN)

附加到此目标的任何命令行都会在执行任何其他操作之前执行。

[`.DEFAULT`](#.DEFAULT)

这是一种 `.USE` 规则，适用于任何 `make` 无法找到其他方法创建的目标(仅用作源)。 仅使用 shell 脚本。继承 `.DEFAULT` 命令的目标的 `.IMPSRC` 变量设置为目标自己的名称。

[`.DELETE_ON_ERROR`](#.DELETE_ON_ERROR)

如果此目标存在于 makefile 中，它将全局导致 make 删除命令失败的目标。（默认情况下，仅删除其命令在执行期间被中断的目标。这是历史行为。）此设置可用于帮助防止半成品或格式错误的目标被遗弃并破坏未来的重建。

[`.END`](#.END)

附加到此目标的任何命令行都将在其他所有操作完成后执行。

[`.ERROR`](#.ERROR)

当另一个目标失败时，将执行附加到该目标的任何命令行 `.ERROR_TARGET` 变量设置为失败的目标。另请参见 `MAKE_PRINT_VAR_ON_ERROR 。`

[`.IGNORE`](#.IGNORE_2)

使用 `.IGNORE` 属性标记每个源。如果未指定源，则这等效于指定 `-i` 选项。

[`.INTERRUPT`](#.INTERRUPT)

如果 `make` 被中断，将执行此目标的命令。

[`.MAIN`](#.MAIN)

如果调用 `make` 时未指定目标，则将构建此目标。

[`.MAKEFLAGS`](#.MAKEFLAGS)

此目标提供一种在使用 makefile 时为 `make` 指定标志的方法。这些标志就像是在 shell 中键入的一样，尽管 `-f` 选项不起作用。

[`.NOPATH`](#.NOPATH_2)

将 `.NOPATH` 属性应用于任何指定的源。

[`.NOTPARALLEL`](#.NOTPARALLEL)

禁用并行模式。

[`.NO_PARALLEL`](#.NO_PARALLEL)

[`.NOTPARALLEL`](#.NOTPARALLEL_2) 的同义词，用于与其他 pmake 变体兼容。

[`.OBJDIR`](#.OBJDIR)

源是 ‘`.OBJDIR`’ 的新值。如果存在， `make` 将对它进行 chdir(2) 并更新 ‘`.OBJDIR`’ 的值。

[`.ORDER`](#.ORDER)

命名的目标是按顺序制作的。此排序不会将目标添加到要制作的目标列表中。由于在可以构建目标本身之前不会构建目标的依赖项，除非 ‘`a`’ 由依赖关系图的另一部分构建，否则以下是依赖循环：

.ORDER: b a b: a 

`.ORDER` 强加的排序仅与并行制造有关。

[`.PATH`](#.PATH)

源是要搜索当前目录中未找到的文件的目录。如果未指定源，则删除任何先前指定的目录。如果源是特殊的 `.DOTLAST` 目标，则最后搜索当前工作目录。

[`.PATH.`](#.PATH.)suffix

与 `.PATH` 类似，但仅适用于具有特定后缀的文件。后缀必须先前已用 `.SUFFIXES` 声明。

[`.PHONY`](#.PHONY_2)

将 `.PHONY` 属性应用于任何指定的源。

[`.PRECIOUS`](#.PRECIOUS_2)

将 `.PRECIOUS` 属性应用于任何指定的源。如果未指定源，则 `.PRECIOUS` 属性将应用于文件中的每个目标。

[`.SHELL`](#.SHELL_2)

设置 `make` 将用于执行命令的 shell。源是一组 field=value 对。

name

这是最小规范，用于选择内置 shell 规范之一； sh 、 ksh 和 csh 。

path

指定外壳的路径。

hasErrCtl

指示 shell 是否支持出错时退出。

check

打开错误检查的命令。

ignore

禁用错误检查的命令。

echo

打开执行命令的回显的命令。

quiet

关闭执行命令的回显的命令。

filter

发出 quiet 命令后要过滤的输出。它通常与 quiet 相同。

errFlag

传递 shell 以启用错误检查的标志。

echoFlag

传递 shell 以启用命令回显的标志。

newline

传递给 shell 的字符串文字，当在任何引用字符之外使用时会产生单个换行符。

例子：

.SHELL: name=ksh path=/bin/ksh hasErrCtl=true \\ check="set -e" ignore="set +e" \\ echo="set -v" quiet="set +v" filter="set +v" \\ echoFlag=v errFlag=e newline="'\\n'" 

[`.SILENT`](#.SILENT_2)

将 `.SILENT` 属性应用于任何指定的源。如果未指定源，则 `.SILENT` 属性将应用于文件中的每个命令。

[`.STALE`](#.STALE)

当依赖文件包含陈旧的条目时，此目标将运行，并将 .ALLSRC 设置为该依赖文件的名称。

[`.SUFFIXES`](#.SUFFIXES)

每个源文件都指定 `make` 的后缀。 如果未指定源，则删除任何先前指定的后缀。它允许创建后缀转换规则。

例子：

.SUFFIXES: .o .c.o: cc -o ${.TARGET} -c ${.IMPSRC} 

[环境](#__u73AF___u5883_)
=======================

`make` 使用以下环境变量（如果存在） `MACHINE 、` `MACHINE_ARCH 、` `MAKE 、` `MAKEFLAGS 、` `MAKEOBJDIR 、` `MAKEOBJDIRPREFIX 、` `MAKESYSPATH 、` `PWD` 和 `TMPDIR 。`

`MAKEOBJDIRPREFIX` 和 `MAKEOBJDIR` 只能在环境或命令行中设置为 `make` 而不是作为 makefile 变量；有关详细信息，请参阅 ‘`.OBJDIR`’ 的描述。

[文件](#__u6587___u4EF6_)
=======================

.depend

依赖项列表

Makefile

依赖项列表

makefile

依赖项列表

sys.mk

系统生成文件

/usr/share/mk

系统makefile目录

[兼容性](#__u517C___u5BB9___u6027_)
================================

基本的 make 语法在不同版本的 make 之间是兼容的；但是特殊变量、变量修饰符和条件不是

[旧版本](#__u65E7___u7248___u672C_)
--------------------------------

旧版本 `make` 的不完整更改列表:

在 NetBSD 5.0 之后，替换 .for 循环变量的方式发生了变化，因此它们看起来仍然是变量扩展。特别是，这阻止了它们被视为语法，并消除了在 .if 语句中使用它们的一些晦涩问题。

在 NetBSD 4.0 中，并行生成的调度方式发生了变化，因此 .ORDER 和 .WAIT 递归地应用于依赖节点。使用的算法将来可能会再次改变。

[其他 make 方言](#__u5176___u4ED6__make___u65B9___u8A00_)
-----------------------------------------------------

其他 make 方言 (GNU make、 SVR4 make、 POSIX make 等）不支持本手册中描述的大部分 `make` 功能。最为显着地：

*   [`.WAIT`](#.WAIT_2) 和 `.ORDER` 声明以及与并行化有关的大部分功能。（GNU make 支持并行化，但缺乏有效控制并行化所需的这些功能。）
*   指令，包括 for 循环和条件以及大多数形式的包含文件。（GNU make 有它自己的不兼容且不太强大的条件句语法。）
*   所有以点开头的内置变量。
*   大多数以点开头的特殊源和目标 `.PHONY 、` `.PRECIOUS` 和 `.SUFFIXES` 除外。
*   变量修饰符，除了
    
    `:old=new`
    
    字符串替换，它不支持使用 ‘`%`’ 进行通配，并且历史上仅适用于声明的后缀。
*   [`$>`](#$_) 变量即使是简写形式；大多数品牌都支持此功能，但名称各不相同。

有些功能更便于移植，例如使用 `+= 、` `?=` 和 `!=` 进行赋值。 `.PATH` 功能基于 GNU make 和许多版本的 SVR4 make 中的旧功能 `VPATH` ；然而，从历史上看，它的行为定义太不明确（而且错误太多）而无法依赖。

`$@` 和 `$<` 变量或多或少是普遍可移植的， `$(MAKE)` 变量也是如此。后缀规则的基本使用（仅适用于当前目录中的文件，不尝试将转换链接在一起等）也是相当可移植的。

[参见](#__u53C2___u89C1_)
=======================

mkdep(1) 、 style.Makefile(5)

[历史](#__u5386___u53F2_)
=======================

在版本 Version 7 AT&T UNIX 中出现一个 `make` 命令。这个 `make` 实现基于 Adam De Boor 为伯克利的 Sprite 编写的 pmake 程序。它被设计为使用名为 “customs” 的守护进程在不同机器上并行分布式 make 运行作业。

从历史上看， target/dependency “FRC” 已用于强制重建（因为目标/依赖不存在......除非有人创建 “FRC” 文件）。

[缺陷](#__u7F3A___u9677_)
=======================

如果不对数据进行实际操作， `make` 语法很难解析。 例如，查找变量使用的结束应该涉及扫描每个修饰符，为每个字段使用正确的终止符。 在许多地方 `make` 只计算 {} 和 () 以便找到变量扩展的结尾。

无法转义文件名中的空格字符。

December 22, 2020

FreeBSD 13.1-RELEASE