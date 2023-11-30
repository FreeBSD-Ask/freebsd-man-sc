  XARGS(1)  

XARGS(1)

FreeBSD General Commands Manual

XARGS(1)

[名称](#__u540D___u79F0_)
=======================

`xargs` —

构造参数列表并执行实用程序

[概要](#__u6982___u8981_)
=======================

`xargs` \[`-0oprt`\] \[`-E` eofstr\] \[`-I` replstr \[`-R` replacements\] \[`-S` replsize\]\] \[`-J` replstr\] \[`-L` number\] \[`-n` number \[`-x`\]\] \[`-P` maxprocs\] \[`-s` size\] \[utility \[argument ...\]\]

[描述](#__u63CF___u8FF0_)
=======================

`xargs` 实用程序从标准输入读取空格、制表符、换行符和文件结尾分隔的字符串，并以字符串作为参数执行 utility 。

命令行上指定的任何参数都会在每次调用时提供给 utility ，然后是从 `xargs` 的标准输入中读取的一些参数。 重复此操作，直到标准输入用尽。

空格、制表符和换行符可以使用单引号 (\`\` ' '') 或双引号 (\`\`"'') 或反斜杠 (\`\`\\'') 嵌入到参数中。单引号转义所有非单引号字符，不包括换行符，直到匹配的单引号。 双引号转义所有非双引号字符，不包括换行符，直到匹配的双引号。 任何单个字符，包括换行符，都可以用反斜杠转义。

选项如下：

[`-0`](#0), `--null`

更改 `xargs` 以期望 NUL (\`\`\\0'') 字符作为分隔符，而不是空格和换行符。 预计这将与 find(1) 中的 `-print0` 函数一起使用。

[`-E`](#E) eofstr

使用 eofstr 作为逻辑 EOF 标记。

[`-I`](#I) replstr

为每个输入行执行 utility ，用整行输入 replacements utility 的一个或多个 replstr 实例（如果没有指定 `-R` 标志，则最多替换 5 个）参数。 替换完成后，生成的参数将不允许超过 replsize （如果未指定 `-S` 标志，则为 255）字节；这是通过将尽可能多的包含 replstr 的参数连接到 utility 的构造参数来实现的，最多为 replsize 个字节。 大小限制不适用于不包含 replstr 的 utility 参数，此外，不会对 utility 本身进行替换。 暗示 `-x` 。

[`-J`](#J) replstr

如果指定了此选项， `xargs` 将使用从标准输入读取的数据来替换第一次出现的 replstr ，而不是在所有其他参数之后附加该数据。 此选项不会影响将从输入中读取的参数数量 (`-n`), 或者 `xargs` 将生成的命令的大小 (`-s`) 。 该选项只是移动这些参数将被放置在执行的命令中的位置。 replstr 必须显示为 `xargs` 的不同 argument 。 例如，如果它位于带引号的字符串的中间，则不会被识别。 此外，只会替换第一次出现的 replstr 。 例如，以下命令会将当前目录中以大写字母开头的文件和目录列表复制到 destdir:

`/bin/ls -1d [A-Z]* | xargs -J % cp -Rp % destdir`

[`-L`](#L) number

为读取的每个 number 行调用 utility 。 如果到达 EOF 并且读取的行数少于 number ，则将使用可用行调用 utility 。

[`-n`](#n) number, `--max-args=`number

设置每次调用 utility 时从标准输入获取的参数的最大数量。 如果累计的字节数(参见 `-s` 选项)超过了指定的 size ，或者对于 utility 的最后一次调用剩下的参数数少于 number ， utility 的调用将使用少于 number 的标准输入参数。 number 的当前默认值为 5000。

[`-o`](#o)

在执行命令之前，在子进程中将 stdin 作为 /dev/tty 重新打开。 如果您希望 `xargs` 运行交互式应用程序，这将很有用。

[`-P`](#P) maxprocs, `--max-procs=`maxprocs

并行模式：一次最多运行 maxprocs 次 utility 调用。 如果 maxprocs 设置为 0， `xargs` 将运行尽可能多的进程。

[`-p`](#p), `--interactive`

回显每个要执行的命令并询问用户是否应该执行。 POSIX 语言环境中的肯定响应 ‘`y`’ 会导致命令被执行，任何其他响应都会导致它被跳过。 如果进程未连接到终端，则不会执行任何命令。

[`-r`](#r), `--no-run-if-empty`

与 GNU `xargs` 的兼容性。 GNU 版本的 `xargs` 至少运行一次 utility 参数，即使 `xargs` 输入为空，它也支持 `-r` 选项来禁止此行为。 FreeBSD 版本的 `xargs` 不会在空输入上运行 utility 参数，但它支持 `-r` 选项以实现与 GNU `xargs` 的命令行兼容性，但 `-r` 选项在 FreeBSD 版本的 `xargs` 中没有任何作用。

[`-R`](#R) replacements

指定 `-I` 用于替换的最大参数数量。如果 replacements 为负数，则要替换的参数数是无限的。

[`-S`](#S) replsize

指定 `-I` 可用于替换的空间量（以字节为单位）。 replsize 的默认值为 255。

[`-s`](#s) size, `--max-chars=`size

设置提供给 utility 的命令行长度的最大字节数。 实用程序名称的长度、传递给 utility 的参数（包括 `NULL` 终止符）和当前环境的总和将小于或等于此数字。 size 的当前默认值为 `ARG_MAX` - 4096。

[`-t`](#t), `--verbose`

在执行之前立即将要执行的命令回显到标准错误。

[`-x`](#x), `--exit`

如果包含 number 参数的命令行不适合指定（或默认）的命令行长度，则强制 `xargs` 立即终止。

如果 utility 被省略，则使用 echo(1) 。

如果 utility 从标准输入读取，可能会发生未定义的行为。

如果无法组装或无法调用命令行，或者如果 utility 的调用被信号终止，或者 utility 的调用以 255 的值退出，则 `xargs` 实用程序将停止处理输入并在所有 utility 调用后退出完成加工。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

如果没有发生错误， `xargs` 实用程序会以 0 值退出。 如果找不到 utility ，则 `xargs` 以值 127 退出，否则如果无法执行 utility ，则 `xargs` 以值 126 退出。 如果发生任何其他错误，则 `xargs` 以值 1 退出。

[实例](#__u5B9E___u4F8B_)
=======================

创建一个数字从 1 到 9 的 3x3 矩阵。每个 echo(1) 实例接收三行作为参数：

$ seq 1 9 | xargs -L3 echo 1 2 3 4 5 6 7 8 9 

复制标准输入的每一行：

$ echo -e "one\\ntwo\\nthree" | xargs -I % echo % % one one two two three three 

使用标准输入中的目录之一执行最多 2 个 find(1) 并发实例：

echo -e "/usr/ports\\n/etc\\n/usr/local" | xargs -J % -P2 -n1 find % -name file 

[参见](#__u53C2___u89C1_)
=======================

echo(1), find(1), execvp(3)

[标准](#__u6807___u51C6_)
=======================

`xargs` 实用程序应符合 IEEE Std 1003.2 (“POSIX.2”) 标准。 `-J`, `-o`, `-P`, `-R` 和 `-S` 选项是非标准的 FreeBSD 扩展，在其他操作系统上可能不可用。

[历史](#__u5386___u53F2_)
=======================

`xargs` 实用程序出现在 PWB UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

如果 utility 尝试调用另一个命令以增加参数数量或环境大小，则可能会导致 execvp(3) 因 `E2BIG` 失败。

`xargs` 实用程序在对 `-I` 和 `-J` 选项执行字符串比较时不考虑多字节字符，这可能会导致某些语言环境中的结果不正确。

September 21, 2020

FreeBSD 13.1-RELEASE