  AWK(1)  

AWK(1)

FreeBSD General Commands Manual

AWK(1)

[名称](#__u540D___u79F0_)
=======================

`awk` —

模式导向的扫描和处理语言

[概要](#__u6982___u8981_)
=======================

`awk` \[`-safe`\] \[`-version`\] \[`-d`\[n\]\] \[`-F` fs\] \[`-v` var\=value\] \[prog | `-f` progfile\] file ...

[描述](#__u63CF___u8FF0_)
=======================

`awk` 扫描每个输入 file 以查找与 prog 或一个或多个指定为 `-f` progfile 的文件中指定的一组模式中的任何一个匹配的行。 对于每个模式，当 file 的一行与模式匹配时，将执行一个关联的操作。 每一行都与每个模式动作语句的模式部分匹配；为每个匹配的模式执行相关的操作。 文件名 ‘-’ 表示标准输入。 任何 var\=value 形式的 file 都被视为一个赋值，而不是一个文件名，如果它是一个文件名，它会在它被打开的时候被执行。

选项如下：

[`-d`](#d)\[n\]

调试模式。 将调试级别设置为 n, 如果未指定 n ，则设置为 1。 大于 1 的值会导致 `awk` 在发生致命错误时转储核心。

[`-F`](#F) fs

将输入字段分隔符定义为正则表达式 fs 。

[`-f`](#f) progfile

从指定的文件 progfile 而不是从命令行读取程序代码。

[`-safe`](#safe)

禁用文件输出 (`print` \> 、 `print` \>>) 、 进程创建 (cmd | `getline 、` `print` | `、` `system`) 和对环境的访问 (ENVIRON; 请参阅下面的变量部分）。 这是 `awk` 的 “safe” 版本的第一个 (但不是非常可靠的) 近似值。

[`-version`](#version)

将 `awk` 的版本号打印到标准输出并退出。

[`-v`](#v) var\=value

在执行 prog 之前为变量 var 赋 value ；可以存在任意数量的 `-v` 选项。

输入通常由由换行符或 RS 值分隔的输入行 (records) 组成。 如果 RS 为空，则使用任意数量的空行作为记录分隔符，并使用换行符作为字段分隔符（除了 FS 的值）。 这在处理多行记录时很方便。

输入行通常由由空格或正则表达式 FS 分隔的字段组成。 字段表示为 $1, $2, ..., 而 $0 表示整行。 如果 FS 为空，则输入行被拆分为每个字符一个字段。

通常，任意数量的空白分隔字段。 要将字段分隔符设置为单个空白，请使用值为 ‘\[ \]’ 的 `-F` 选项。 如果指定了 ‘t’ 的字段分隔符，则 `awk` 将其视为已指定 ‘\\t’ 并使用 ⟨TAB⟩ 作为字段分隔符。 为了使用文字 ‘t’ 作为字段分隔符，请使用 `-F` 选项，其值为 ‘\[t\]’ 。

模式动作语句具有以下形式

pattern `{` action `}`

缺少 `{` action `}` 表示打印该行；缺失的模式总是匹配的。 模式操作语句由换行符或分号分隔。

允许在终止语句之后或逗号 (‘,’) 、左大括号 (‘{’) 、逻辑 AND (‘&&’) 、逻辑 OR (‘||’) 和 ‘do’ 之后使用换行符或 ‘else’ 关键字，或在 ‘if 、’ ‘for’ 或 ‘while’ 语句的右括号之后。 此外，反斜杠 (‘\\’) 可用于转义标记之间的换行符。

动作是一系列语句。 语句可以是以下之一：

[`if`](#if) (expression) statement \[`else` statement\]

[`while`](#while) (expression) statement

[`for`](#for) (expression; expression; expression) statement

[`for`](#for_2) (var `in` array) statement

[`do`](#do) statement `while` (expression)

[`break`](#break)

[`continue`](#continue)

[`{`](#_) \[statement ...\] `}`

expression \# commonly var \= expression

[`print`](#print) \[expression-list\] \[>expression\]

[`printf`](#printf) format \[..., expression-list\] \[>expression\]

[`return`](#return) \[expression\]

[`next`](#next) \# skip remaining patterns on this input line

[`nextfile`](#nextfile) \# skip rest of this file, open next, start at top

[`delete`](#delete) array`[`expression`]` \# delete an array element

[`delete`](#delete_2) array \# delete all elements of array

[`exit`](#exit) \[expression\] \# exit immediately; status is expression

语句以分号、换行符或右大括号结束。 一个空的 expression-list 代表 $0 。 字符串常量用 `""` 引用，其中识别出通常的 C 转义（请参阅 printf(1) 以获取这些转义的完整列表）。 表达式根据需要采用字符串或数值，并使用运算符 `+ - * / % ^` (求幂) 和连接 (由空格表示) 构建。 运算符 `! ++ -- += -= *= /= %= ^=` `> >= < <= == != ?:` 也可用于表达式。 变量可以是标量、数组元素（表示为 `x[i]`) 或字段。 变量被初始化为空字符串。 数组下标可以是任意字符串，不一定是数字；这允许一种形式的联想记忆。 允许使用多个下标，例如 `[i,j,k]` ；成分是连接的，由 SUBSEP 的值分隔 (请参阅下面的变量部分) 。

`print` 语句将其参数打印在标准输出上（如果存在 >file 或 >>file 则打印在文件上；如果存在 | cmd ，则打印在管道上），由当前输出字段分隔符分隔，并由输出记录分隔符终止. file 和 cmd 可以是文字名称或带括号的表达式；不同语句中的相同字符串值表示相同的打开文件。 `printf` 语句根据格式格式化其表达式列表（请参阅 printf(1) )。

模式是正则表达式和关系表达式的任意布尔组合（带有 `! || &&`) 。 `awk` 支持扩展正则表达式 (ERE) 。 有关正则表达式的更多信息，请参阅 re\_format(7) 。 模式中的独立正则表达式适用于整行。 正则表达式也可能出现在关系表达式中，使用运算符 `~` 和 `!~` 。 /re/ 是一个常量正则表达式；任何字符串（常量或变量）都可以用作正则表达式，但模式中孤立正则表达式的位置除外。

一个模式可能由两个用逗号分隔的模式组成；在这种情况下，对从第一个模式的出现到第二个模式的出现的所有行执行该动作。

关系表达式是以下之一：

expression matchop regular-expression

expression relop expression

expression `in` array-name

[`(`](#()expr, expr, ...`) in` array-name

其中 relop 是 C 中六个关系运算符中的任何一个，而 matchop 是 `~` （匹配）或 `!~` 不匹配）。 条件是算术表达式、关系表达式或它们的布尔组合。

特殊模式 `BEGIN` 和 `END` 可用于在读取第一个输入行之前和最后一个输入行之后捕获控制。 `BEGIN` 和 `END` 不与其他模式组合。

具有特殊含义的变量名：

ARGC

参数计数，可分配。

ARGV

参数数组，可赋值；非空成员被视为文件名。

CONVFMT

转换数字时的转换格式（默认 “`%.6g`” ）。

ENVIRON

环境变量数组；下标是名称。

FILENAME

当前输入文件的名称。

FNR

当前文件中当前记录的序号。

FS

用于分隔字段的正则表达式；也可以通过选项 `-F` fs 设置。

NF

当前记录中的字段数。 $NF 可用于获取当前记录中最后一个字段的值。

NR

当前记录的序号。

OFMT

数字的输出格式（默认 “`%.6g`” 数字的输出格式（默认

OFS

输出字段分隔符（默认为空白）。

ORS

输出记录分隔符（默认换行符）。

RLENGTH

`match`() 函数匹配的字符串的长度。

RS

输入记录分隔符（默认换行符）。

RSTART

`match`() 函数匹配的字符串的起始位置。

SUBSEP

分隔多个下标（默认 034）。

[函数](#__u51FD___u6570_)
=======================

awk 语言有多种内置函数：算术、字符串、输入/输出、通用和位操作。

可以这样定义函数（在模式动作语句的位置）：

`function foo(a, b, c) { ...; return x }`

如果是标量，参数按值传递，如果是数组名，则按引用传递；函数可以递归调用。 参数是函数的本地参数；所有其他变量都是全局的。 因此，可以通过在函数定义中提供多余的参数来创建局部变量。

[算术函数](#__u7B97___u672F___u51FD___u6570_)
-----------------------------------------

`atan2`(y, x)

以弧度返回 y/x 的反正切。

`cos`(x)

返回 x 的余弦，其中 x 以弧度为单位。

`exp`(x)

返回 x 的指数。

`int`(x)

返回 x 截断为整数值。

`log`(x)

返回 x 的自然对数。

`rand`()

返回一个随机数 n ，满足 0≤n <1 。

`sin`(x)

返回 x 的正弦值，其中 x 以弧度为单位。

`sqrt`(x)

返回 x 的平方根。

`srand`(expr)

将 `rand`() 的种子设置为 expr 并返回前一个种子。 如果省略 expr ，则使用一天中的时间。

[字符串函数](#__u5B57___u7B26___u4E32___u51FD___u6570_)
--------------------------------------------------

`gsub`(r, t, s)

与 `sub`() 相同，只是替换了所有出现的正则表达式。 `gsub`() 返回替换的数量。

`index`(s, t)

s 中字符串 t 出现的位置，如果没有出现，则为 0。

`length`(s)

s 作为字符串的长度，如果没有给出参数，则为 $0 。

`match`(s, r)

正则表达式 r 在 s 中出现的位置，如果没有出现，则为 0。 变量 RSTART 设置为匹配字符串的起始位置 (与返回值相同) ，如果未找到匹配项，则设置为零。 变量 RLENGTH 设置为匹配字符串的长度，如果没有找到匹配项，则设置为 -1 。

`split`(s, a, fs)

将字符串 s 拆分为数组元素 a\[1\], a\[2\], ..., a\[n\]-
并返回 n 。 如果没有给出 fs ，则使用正则表达式 FS 或字段分隔符 fs 进行分隔。 一个空字符串作为字段分隔符将字符串拆分为每个字符一个数组元素。

`sprintf`(fmt, expr, ...)

根据 printf(1) 格式 fmt 格式化 expr, ... 产生的字符串。

`sub`(r, t, s)

用 t 代替字符串 s 中第一次出现的正则表达式 r 。 如果没有给出 s ，则使用 $0 。 t 中的 & 符号 (‘&’) 在字符串 s 中被替换为正则表达式 r 。 可以通过在其前面加上两个反斜杠 (‘\\\\’) 来指定文字 & 符号。 可以通过在其前面加上另一个反斜杠 (‘\\\\’) 来指定文字反斜杠。 `sub`() 返回替换的数量。

`substr`(s, m, n)

最多返回从位置 m 开始的 s 的 n 个字符的子字符串，从 1 开始计数。 如果省略 n ，或者如果 n 指定的字符多于字符串中剩余的字符，则子字符串的长度受 s 长度的限制。

`tolower`(str)

返回 str 的副本，其中所有大写字符都转换为对应的小写字符。

`toupper`(str)

返回 str 的副本，其中所有小写字符都转换为对应的大写字符。

[输入/输出和一般功能](#__u8F93___u5165_/__u8F93___u51FA___u548C___u4E00___u822C___u529F___u80FD_)
----------------------------------------------------------------------------------------

`close`(expr)

关闭文件或管道 expr 。 expr 应该与用于打开文件或管道的字符串匹配。

cmd | [`getline`](#getline) \[var\]

从 cmd 的输出通过管道传输的流中读取输入记录。 如果省略 var ，则设置变量 $0 和 NF 。 否则设置 var 。 如果流未打开，则将其打开。 只要流保持打开状态，后续调用就会从流中读取后续记录。 流保持打开状态，直到通过调用 `close`() 显式关闭。 `getline` 返回 1 表示输入成功，0 表示文件结束， -1 表示错误。

`fflush`(\[expr\])

刷新文件或管道 expr 的任何缓冲输出，或者如果省略 expr ，则刷新所有打开的文件或管道。 expr 应该与用于打开文件或管道的字符串匹配。

[`getline`](#getline_2)

将 $0 设置为当前输入文件中的下一个输入记录。 这种形式的 `getline` 设置变量 NF 、 NR 和 FNR 。 `getline` 返回 1 表示输入成功，0 表示文件结束， -1 表示错误。

[`getline`](#getline_3) var

将 $0 设置为变量 var 。 这种形式的 `getline` 设置变量 NR 和 FNR 。 `getline` 返回 1 表示输入成功，0 表示文件结束， -1 表示错误。

[`getline`](#getline_4) \[var\] <file

将 $0 设置为 file 中的下一条记录。 如果省略 var ，则设置变量 $0 和 NF 。否则设置 var 。 如果 file 未打开，则将其打开。 只要流保持打开状态，后续调用就会从 file 中读取后续记录。 file 保持打开状态，直到通过调用 `close`() 显式关闭。

`system`(cmd)

执行 cmd 并返回其退出状态。

[比特运算函数](#__u6BD4___u7279___u8FD0___u7B97___u51FD___u6570_)
-----------------------------------------------------------

`compl`(x)

返回整数参数 x 的按位补码。

`and`(v1, v2, ...)

对提供的所有参数执行按位与，作为整数。 必须至少有两个值。

`or`(v1, v2, ...)

对提供的所有参数执行按位或，作为整数。 必须至少有两个值。

`xor`(v1, v2, ...)

对提供的所有参数执行按位异或，作为整数。 必须至少有两个值。

`lshift`(x, n)

返回向左移动 n 位的整数参数 x。

`rshift`(x, n)

返回整数参数 x 向右移动 n 位。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `awk` utility exits 0 on success, and >0 if an error occurs.

但请注意， `exit` 表达式可以修改退出状态。

[实例](#__u5B9E___u4F8B_)
=======================

打印长度超过 72 个字符的行：

`length($0) > 72`

以相反的顺序打印前两个字段：

`{ print $2, $1 }`

同样，输入字段由逗号和/或空格和制表符分隔：

BEGIN { FS = ",\[ \\t\]\*|\[ \\t\]+" } { print $2, $1 } 

将第一列相加，打印总和和平均值：

{ s += $1 } END { print "sum is", s, " average is", s/NR } 

打印开始/停止对之间的所有行：

`/start/, /stop/`

模拟 echo(1):

BEGIN { # Simulate echo(1) for (i = 1; i < ARGC; i++) printf "%s ", ARGV\[i\] printf "\\n" exit } 

将错误消息打印到标准错误：

{ print "error!" > "/dev/stderr" } 

[参见](#__u53C2___u89C1_)
=======================

cut(1), lex(1), printf(1), sed(1), re\_format(7) A. V. Aho, B. W. Kernighan, and P. J. Weinberger, The AWK Programming Language, _Addison-Wesley_, 1988, ISBN 0-201-07981-X.

[标准](#__u6807___u51C6_)
=======================

`awk` 实用程序符合 IEEE Std 1003.1-2008 (“POSIX.1”) 规范，但 `awk` 不支持 {n,m} 模式匹配。

标志 `-d` `-、` `-safe` 和 `-version` 以及命令 `fflush`, `compl`, `and`, `or`, `xor`, `lshift`, `rshift` 是对该规范的扩展。

[历史](#__u5386___u53F2_)
=======================

`awk` 实用程序出现在 Version 7 AT&T UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

数字和字符串之间没有显式转换。 要强制将表达式视为数字，请向其添加 0；强制将其视为将 `""` 连接到它的字符串。

函数中变量的范围规则很糟糕；语法更糟。

June 6, 2020

FreeBSD 13.1-RELEASE