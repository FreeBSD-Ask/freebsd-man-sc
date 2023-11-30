  FIND(1)  

FIND(1)

FreeBSD General Commands Manual

FIND(1)

[名称](#__u540D___u79F0_)
=======================

`find` —

遍历文件层次结构

[概要](#__u6982___u8981_)
=======================

`find` \[`-H` | `-L` | `-P`\] \[`-EXdsx`\] \[`-f` path\] path ... \[expression\] `find` \[`-H` | `-L` | `-P`\] \[`-EXdsx`\] `-f` path \[path ...\] \[expression\]

[综述](#__u7EFC___u8FF0_)
=======================

`find` 实用程序递归地向下列出每个 path 的目录树，根据树中的每个文件评估一个 expression (由下面列出的 “primaries” 和 “operands” 组成) 。

选项如下：

[`-E`](#E)

将后跟 `-regex` 和 `-iregex` 主表达式的正则表达式解释为扩展（现代）正则表达式，而不是基本正则表达式 (BRE)。 re\_format(7) 手册页完整地描述了这两种格式。

[`-H`](#H)

导致为命令行上指定的每个符号链接返回的文件信息和文件类型（请参阅 stat(2) ）是链接引用的文件的信息和文件类型，而不是链接本身。 如果引用的文件不存在，则文件信息和类型将用于链接本身。 所有不在命令行上的符号链接的文件信息都是链接本身的文件信息。

[`-L`](#L)

导致为每个符号链接返回的文件信息和文件类型（请参阅 stat(2) ）是链接引用的文件的信息和文件类型，而不是链接本身。 如果引用的文件不存在，则文件信息和类型将用于链接本身。

此选项等效于已弃用的 `-follow` 主选项。

[`-P`](#P)

导致为每个符号链接返回的文件信息和文件类型（参见 stat(2) ）是链接本身的信息和文件类型。 这是默认设置。

[`-X`](#X)

允许 `find` 与 xargs(1) 一起安全使用。 如果文件名包含 xargs(1) 使用的任何定界字符，则会在标准错误中显示诊断消息，并跳过该文件。 定界字符包括单引号 (“ `'` ”) 和双引号 (“ `"` ”) 、反斜杠 (“`\`”) 、空格、制表符和换行符。

但是，您可能希望将 `-print0` 主节点与 “`xargs` `-0`” 结合使用作为一种有效的替代方法。

[`-d`](#d)

导致 `find` 执行深度优先遍历。

此选项是 IEEE Std 1003.1-2001 (“POSIX.1”) 指定的 `-depth` primary 的 BSD 特定等效项。 有关详细信息，请参阅其在 [PRIMARIES](#PRIMARIES) 下的描述。

[`-s`](#s)

导致 `find` 按字典顺序（即每个目录中的字母顺序）遍历文件层次结构。 注意： ‘`find -s`’ 和 ‘`find | sort`’ 可能会给出不同的结果。

[`-x`](#x)

防止 `find` 下降到设备号不同于下降开始的文件的设备号的目录中。

此选项等效于已弃用的 `-xdev` 主选项。

[基元](#__u57FA___u5143_)
=======================

所有带数字参数的初选都允许数字前面有加号 (“`+`”) 或减号 (“`-`”) 。 前面的加号表示 “more than n”, ，前面的减号表示 “less than n” ，两者都不表示 “exactly n” 。

[`-Bmin`](#-Bmin) n

如果文件的 inode 创建时间与开始 `find` 的时间之间的差异（向上舍入到下一整分钟）为 n 分钟，则为真。

[`-Bnewer`](#-Bnewer) file

与 `-newerBm` 相同。

[`-Btime`](#-Btime) n\[`smhdw`\]

如果未指定单位，则如果文件的 inode 创建时间与开始 `find` 时间之间的差异（向上舍入到下一个完整的 24 小时周期）为 n 24 小时周期，则此主节点评估为 true。

如果指定了单位，则如果文件的 inode 创建时间与开始 `find` 的时间之间的差正好是 n 个单位，则此主节点的计算结果为 true。 有关支持的时间单位的信息，请参阅 `-atime` 主要描述。

[`-acl`](#-acl)

可以与其他主文件结合使用来定位具有扩展 ACL 的文件。 有关详细信息，请参阅 acl(3) 。

[`-amin`](#-amin) \[`-`|`+`\]n

如果文件上次访问时间和开始 `find` 时间之间的差异（向上舍入到下一个完整分钟）大于 n (+n) 、小于 n (-n) 或恰好在 n 分钟前，则为真。

[`-anewer`](#-anewer) file

与 `-neweram` 相同。

[`-atime`](#-atime) n\[`smhdw`\]

如果未指定单位，则如果文件上次访问时间与开始 `find` 时间之间的差值（向上舍入到下一个完整的 24 小时周期）为 n 个 24 小时周期，则此主要计算结果为 true。

如果指定了单位，则如果文件上次访问时间和开始 `find` 的时间之间的差正好是 n 个单位，则此主节点评估为真。 可能的时间单位如下：

[`s`](#s_2)

秒

[`m`](#m)

分钟（60 秒）

[`h`](#h)

小时（60 分钟）

[`d`](#d_2)

一天（24 小时）

[`w`](#w)

周（7天）

任意数量的单位可以组合在一个 `-atime` 参数中，例如， “`-atime -1h30m`” 。单位可能仅在与 `+` 或 `-` 修饰符一起使用时才有用。

[`-cmin`](#-cmin) \[`-`|`+`\]n

如果最后一次更改文件状态信息的时间与开始 `find` 的时间之间的差异（向上舍入到下一整分钟）大于 n (+n) 、小于 n (-n) 或恰好 n 分钟，则为真前。

[`-cnewer`](#-cnewer) file

与 `-newercm` 相同。

[`-ctime`](#-ctime) n\[`smhdw`\]

如果未指定单位，则如果文件状态信息的最后更改时间与开始 `find` 的时间之间的差值（向上舍入到下一个完整的 24 小时周期）为 n 个 24 小时周期，则此主要计算结果为 true。

如果指定了单位，则如果文件状态信息的最后一次更改时间与开始 `find` 的时间之间的差异正好是 n 个单位，则此主要计算结果为 true。 有关支持的时间单位的信息，请参阅 `-atime` 主要描述。

[`-d`](#-d)

不可移植的、特定于 BSD 的 `depth` 版本。 GNU find 在错误地模拟 FreeBSD `find` 时将其作为主要实现。

[`-delete`](#-delete)

删除找到的文件与/或目录。总是返回真。这从当前工作目录执行，因为 `find` 沿着树递归。 它不会尝试删除相对于 “.” 的路径名中带有 “/” 字符的文件名。出于安全原因。 此选项隐含深度优先遍历处理。 如果目录不为空， `-delete` primary 将无法删除目录。以下符号链接与此选项不兼容。

[`-depth`](#-depth)

永远正确；与不可移植的 `-d` 选项相同。导致 `find` 执行深度优先遍历，即以后序访问目录，并且目录中的所有条目将在目录本身之前执行。 默认情况下，按预定顺序 `find` 访问目录，即在其内容之前。 注意，默认 _不是_ 广度优先遍历。

当 `find` 与 cpio(1) 一起使用以处理包含在具有异常权限的目录中的文件时， `-depth` primary 会很有用。 它确保您在将文件放入目录时具有写权限，然后将目录的权限设置为最后一件事。

[`-depth`](#-depth_2) n

如果文件相对于遍历起点的深度为 n ，则为真。

[`-empty`](#-empty)

如果当前文件或目录为空，则为真。

[`-exec`](#-exec) utility \[argument ...\] `;`

如果名为 utility 的程序返回零值作为其退出状态，则为真。 可选 arguments 可以传递给实用程序。 表达式必须以分号 (“`;`”) 结束。 如果从 shell 调用 `find`-
，如果 shell 将其视为控制运算符，则可能需要引用分号。 如果字符串 “`{}`” 出现在实用程序名称或参数中的任何位置，则将其替换为当前文件的路径名。 Utility 将从执行 `find` 的目录中执行。 Utility 和 arguments 不受外壳模式和结构的进一步扩展。

[`-exec`](#-exec_2) utility \[argument ...\] `{} +`

与 `-exec` 相同，但每次调用 utility 时， “`{}`” 被尽可能多的路径名替换。 此行为类似于 xargs(1) 的行为。主节点始终返回 true；如果至少一次 utility 调用返回非零退出状态， `find` 将返回非零退出状态。

[`-execdir`](#-execdir) utility \[argument ...\] `;`

[`-execdir`](#-execdir_2) primary 与 `-exec` primary 相同，但 utility 将从保存当前文件的目录执行。 替换字符串 “`{}`” 的文件名不合格。

[`-execdir`](#-execdir_3) utility \[argument ...\] `{} +`

与 `-execdir` 相同，但每次调用 utility 时， “`{}`” 被尽可能多的路径名替换。 此行为类似于 xargs(1) 的行为。 主节点始终返回 true；如果至少一次 utility 调用返回非零退出状态， `find` 将返回非零退出状态。

[`-flags`](#-flags) \[`-`|`+`\]flags,notflags

使用符号名称指定标志（请参阅 chflags(1) ）。 带有 “`no`” 前缀的那些（ “`nodump`”) 除外）被称为 notflags 。 flags 中的标志被检查为已设置，而 notflags 中的标志被检查为未设置。 请注意，这与 `-perm` 不同，后者仅允许用户指定设置的模式位。

如果标志前面有一个破折号 (“`-`”) ，如果至少 flags 中的所有位和 notflags 中的任何位都未在文件的标志位中设置，则此主要计算结果为真。 如果 flags 前面有一个加号 (“`+`”) ，如果 flags 中的任何位在文件的标志位中被设置，或者 notflags 中的任何位在文件的标志位中没有被设置，则此主元计算为 true。 否则，如果 flags 中的位与文件的 flags 位完全匹配，并且没有一个 flags 位与 notflags 的位匹配，则此主要计算结果为 true。

[`-fstype`](#-fstype) type

如果文件包含在 type 类型的文件系统中，则为真。 lsvfs(1) 命令可用于找出系统上可用的文件系统类型。 此外，还有两种伪类型， “`local`” 和 “`rdonly`” 。 前者匹配任何物理安装在执行 `find` 的系统上的文件系统，后者匹配任何以只读方式安装的文件系统。

[`-gid`](#-gid) gname

与 `-group` gname 相同，用于与 GNU find 兼容。 GNU find 施加了一个限制，即 gname 是数字，而 `find` 没有。

[`-group`](#-group) gname

如果文件属于组 gname ，则为真。 如果 gname 是数字并且没有这样的组名，则 gname 被视为组 ID。

[`-ignore_readdir_race`](#-ignore_readdir_race)

忽略错误，因为从目录读取名称后文件或目录被删除。 此选项不影响起点上发生的错误。

[`-ilname`](#-ilname) pattern

与 `-lname` 类似，但匹配不区分大小写。 这是一个 GNU 查找扩展。

[`-iname`](#-iname) pattern

与 `-name` 类似，但匹配不区分大小写。

[`-inum`](#-inum) n

如果文件的 inode 编号为 n ，则为真。

[`-ipath`](#-ipath) pattern

与 `-path`-
类似，但匹配不区分大小写。

[`-iregex`](#-iregex) pattern

与 `-regex` 类似，但匹配不区分大小写。

[`-iwholename`](#-iwholename) pattern

与 `-ipath` 相同，为 GNU 找到兼容性。

[`-links`](#-links) n

如果文件有 n 个链接，则为真。

[`-lname`](#-lname) pattern

与 `-name` 类似，但匹配的是符号链接的内容而不是文件名。 请注意，这仅在遵循符号链接时才匹配损坏的符号链接。 这是一个 GNU 查找扩展。

[`-ls`](#-ls)

这个主要的总是评估为真。 当前文件的以下信息被写入标准输出：它的 inode 编号、512 字节块的大小、文件权限、硬链接数、所有者、组、字节大小、最后修改时间和路径名。 如果文件是块或字符特殊文件，将显示设备号而不是字节大小。 如果文件是符号链接，则链接到的文件的路径名将显示在 “`->`” 前面。 格式与 “`ls` `-dgils`” 生成的格式相同。

[`-maxdepth`](#-maxdepth) n

永远正确；在命令行参数下最多下降 n 个目录级别。 如果指定了任何 `-maxdepth` ，则它适用于整个表达式，即使它通常不会被计算。 “`-maxdepth` `0`” 将整个搜索限制为命令行参数。

[`-mindepth`](#-mindepth) n

永远正确；不要在低于 n 的级别上应用任何测试或操作。 如果指定了任何 `-mindepth` ，则它适用于整个表达式，即使它通常不会被计算。 “`-mindepth` `1`” 处理除命令行参数之外的所有参数。

[`-mmin`](#-mmin) \[`-`|`+`\]n

如果文件上次修改时间和开始 `find` 时间之间的差异（向上舍入到下一整分钟）大于 n (+n) 、小于 n (-n) 或恰好在 n 分钟前，则为真。

[`-mnewer`](#-mnewer) file

与 `-newer` 相同。

[`-mount`](#-mount)

与 `-xdev` 相同，用于 GNU 查找兼容性。

[`-mtime`](#-mtime) n\[`smhdw`\]

如果未指定单位，则如果文件上次修改时间和开始 `find` 时间之间的差值（向上舍入到下一个完整的 24 小时周期）为 n 个 24 小时周期，则此主要计算结果为 true。

如果指定了单位，则如果文件上次修改时间和开始 `find` 的时间之间的差正好是 n 个单位，则此主文件的计算结果为 true。 有关支持的时间单位的信息，请参阅 `-atime` 主要描述。

[`-name`](#-name) pattern

如果正在检查的路径名的最后一个组件与 pattern 匹配，则为真。 特殊的 shell 模式匹配字符 (“`[ 、`” “`] 、`” “`*`” 和 “`?`”) 可以用作 pattern 的一部分。 这些字符可以通过使用反斜杠 (“`\`”) 转义来显式匹配。

[`-newer`](#-newer) file

如果当前文件的最后修改时间比 file 更新，则为真。

[`-newer`](#-newer_2)XY file

如果当前文件的上次访问时间 (X\=`a`) 、inode 创建时间 (X\=`B`) 、更改时间 (X\=`c`) 或修改时间 (X\=`m`) 比上次访问时间 (Y\=`a`) 、inode 创建时间 (Y\=`B`) 、更改时间 (Y\=`c`) 或 file 修改时间 (Y\=`m`) 。 此外，如果 Y\=`t` ，则 file 被解释为 cvs(1) 所理解形式的直接日期规范。 请注意， `-newermm` 等效于 `-newer` 。

[`-nogroup`](#-nogroup)

如果文件属于未知组，则为真。

[`-noignore_readdir_race`](#-noignore_readdir_race)

关闭 `-ignore_readdir_race` 的效果。这是默认行为。

[`-noleaf`](#-noleaf)

此选项用于 GNU 查找兼容性。 在 GNU find 中，它禁用了与 `find` 无关的优化，因此它被忽略了。

[`-nouser`](#-nouser)

如果文件属于未知用户，则为真。

[`-ok`](#-ok) utility \[argument ...\] `;`

[`-ok`](#-ok_2) primary 与 `-exec` primary 相同，不同之处在于 `find` 通过向终端打印消息并读取响应来请求用户确认 utility 的执行。 如果响应不是肯定的（ “`POSIX`” 语言环境中的 ‘`y`’ ）, 则不执行命令并且 `-ok` 表达式的值为 false。

[`-okdir`](#-okdir) utility \[argument ...\] `;`

[`-okdir`](#-okdir_2) 主节点与 `-execdir` 主节点相同，但与 `-ok` 主节点的描述相同。

[`-path`](#-path) pattern

如果正在检查的路径名与 pattern 匹配，则为真。 特殊的 shell 模式匹配字符 (“`[ 、`” “`] 、`” “`*`” 和 “`?`”) 可以用作 pattern 的一部分。 这些字符可以通过使用反斜杠 (“`\`”) 转义来显式匹配。 斜杠 (“`/`”) 被视为普通字符，不必显式匹配。

[`-perm`](#-perm) \[`-`|`+`\]mode

mode 可以是符号（参见 chmod(1) ）或八进制数。 如果 mode 是符号模式，则假定起始值为零，并且 mode 设置或清除权限，而不考虑进程的文件模式创建掩码。 如果 mode 是八进制，则只有文件模式位的位 07777 (`S_ISUID` | `S_ISGID` | `S_ISTXT` | `S_IRWXU` | `S_IRWXG` | `S_IRWXO`) 参与比较。 如果 mode 前面有一个破折号 (“`-`”) ，那么如果 mode 中的至少所有位都在文件的模式位中设置，则此主要计算结果为真。 如果 mode 前面有一个加号 (“`+`”) ，如果 mode 中的任何位在文件的模式位中设置，则此主要计算结果为真。 否则，如果 mode 中的位与文件的模式位完全匹配，则此主要计算结果为真。 请注意，符号模式的第一个字符可能不是破折号 (“`-`”) 。

[`-print`](#-print)

这个主要的总是评估为真。 它将当前文件的路径名打印到标准输出。 如果没有指定 `-exec 、 -ls 、 -print0` 或 `-ok` ，则给定表达式应有效地替换为 `(` 给定表达式 `)` `-print` 。

[`-print0`](#-print0)

这个主要的总是评估为真。 它将当前文件的路径名打印到标准输出，后跟一个 ASCII `NUL` 字符（字符代码 0）。

[`-prune`](#-prune)

这个主要的总是评估为真。 它导致 `find` 不会下降到当前文件中。 请注意，如果指定了 `-d` 选项，则 `-prune` primary 无效。

[`-quit`](#-quit)

导致 `find` 立即终止。

[`-regex`](#-regex) pattern

如果文件的整个路径使用正则表达式匹配 pattern ，则为真。 要匹配名为 “./foo/xyzzy” 的文件，您可以使用正则表达式 “`.*/[xyz]*`” 或 “`.*/foo/.*`” 但不能使用 “`xyzzy`” 或 “`/foo/`” 。

[`-samefile`](#-samefile) name

如果文件是 name 的硬链接，则为真。 如果指定了命令选项 `-L` ，那么如果文件是符号链接并指向 name ，它也是如此。

[`-size`](#-size) n\[`ckMGTP`\]

如果文件的大小（以 512 字节块为单位，向上取整）为 n ，则为真。 如果 n 后跟 `c` ，则如果文件大小为 n 字节（字符），则主要为真。 类似地，如果 n 后跟一个比例指示符，则文件的大小与 n 进行比较，比例为：

[`k`](#k)

千字节（1024 字节）

[`M`](#M)

兆字节（1024 KB）

[`G`](#G)

千兆字节（1024 兆字节）

[`T`](#T)

太字节（1024 GB）

[`P`](#P_2)

PB（1024 TB）

[`-sparse`](#-sparse)

如果当前文件是稀疏的，即根据其字节大小分配的块少于预期，则为真。 这也可能匹配已被文件系统压缩的文件。

[`-type`](#-type) t

如果文件属于指定类型，则为真。 可能的文件类型如下：

[`b`](#b)

特殊块

[`c`](#c)

特殊字符

[`d`](#d_3)

目录

[`f`](#f)

常规文件

[`l`](#l)

符号链接

[`p`](#p)

FIFO

[`s`](#s_3)

套接字

[`-uid`](#-uid) uname

与 \-user uname 相同，用于与 GNU find 兼容。 GNU find 施加了一个限制，即 uname 是数字，而 `find` 不是。

[`-user`](#-user) uname

如果文件属于用户 uname ，则为真。 如果 uname 是数字并且没有这样的用户名，则 uname 被视为用户 ID。

[`-wholename`](#-wholename) pattern

与 `-path` 相同，为 GNU 找到兼容性。

[运算符](#__u8FD0___u7B97___u7B26_)
================================

可以使用以下运算符组合初选。 运算符按优先级降序排列。

[`(`](#() expression `)`

如果括号内的表达式计算结果为真，则计算结果为真。

[`!`](#!) expression

[`-not`](#-not) expression

这是一元 NOT 运算符。 如果表达式为假，则计算结果为真。

[`-false`](#-false)

总是假的。

[`-true`](#-true)

永远是真的。

expression `-and` expression

expression expression

[`-and`](#-and) 运算符是逻辑 AND 运算符。 由于两个表达式的并列暗示了它，因此不必指定它。 如果两个表达式都为真，则表达式的计算结果为真。 如果第一个表达式为假，则不计算第二个表达式。

expression `-or` expression

[`-or`](#-or) 运算符是逻辑 OR 运算符。 如果第一个或第二个表达式为真，则表达式的计算结果为真。 如果第一个表达式为真，则不计算第二个表达式。

所有操作数和主数必须是单独的参数来 `find` 。 初选,自己带参数希望每个参数是一个单独的参数 `find` 。

[环境](#__u73AF___u5883_)
=======================

`LANG 、 LC_ALL 、 LC_COLLATE 、 LC_CTYPE 、 LC_MESSAGES` 和 `LC_TIME` 环境变量会影响 `find` 实用程序的执行，如 environ(7) 中所述。

[实例](#__u5B9E___u4F8B_)
=======================

以下示例显示为给 shell:

[`find / \! -name "*.c" -print`](#find_/__e!_-name__(dq*.c_(dq_-print)

打印出名称不以 .c 结尾的所有文件的列表。

[`find / -newer ttt -user wnj -print`](#find_/_-newer_ttt_-user_wnj_-print)

打印出用户 “wnj” 拥有的比文件 ttt 更新的所有文件的列表。

[`find / \! \( -newer ttt -user wnj \) -print`](#find_/__e!__e(_-newer_ttt_-user_wnj__e)_-print)

打印出所有不比 ttt 新且属于 “wnj” 的文件的列表。

[`find / \( -newer ttt -or -user wnj \) -print`](#find_/__e(_-newer_ttt_-or_-user_wnj__e)_-print)

打印出属于 “wnj” 或比 ttt 更新的所有文件的列表。

[`find / -newerct '1 minute ago' -print`](#find_/_-newerct_'1_minute_ago'_-print)

打印出所有 inode 更改时间比当前时间减去一分钟的文件的列表。

[`find / -type f -exec echo {} \;`](#find_/_-type_f_-exec_echo_____e;)

使用 echo(1) 命令打印出所有文件的列表。

[`find -L /usr/ports/packages -type l -exec rm -- {} +`](#find_-L_/usr/ports/packages_-type_l_-exec_rm_--____+)

删除 /usr/ports/packages 中所有损坏的符号链接。

[`find /usr/src -name CVS -prune -o -depth +6 -print`](#find_/usr/src_-name_CVS_-prune_-o_-depth_+6_-print)

在工作目录 /usr/src 中查找至少七层深的文件和目录。

[`find /usr/src -name CVS -prune -o -mindepth 7 -print`](#find_/usr/src_-name_CVS_-prune_-o_-mindepth_7_-print)

不等同于前面的示例，因为 `-prune` 不会在七级以下进行评估。

[兼容性](#__u517C___u5BB9___u6027_)
================================

`-follow` 已弃用；应该使用 `-L`-
选项。 有关详细信息，请参阅下面的 [标准](#__u6807___u51C6_) 部分。

[参见](#__u53C2___u89C1_)
=======================

chflags(1) 、 chmod(1) 、 cvs(1) 、 locate(1) 、 lsvfs(1) 、 whereis(1) 、 which(1) 、 xargs(1) 、 stat(2) 、 acl(3) 、 fts(3) 、 getgrent(3) 、 getpwent(3) 、 strmode(3) 、 re\_format(7) 、 symlink(7)

[标准](#__u6807___u51C6_)
=======================

`find` 实用程序语法是 IEEE Std 1003.1-2001 (“POSIX.1”) 标准指定的语法的超集。

除了 `-H` 和 `-L` 以及 `-amin 、 -anewer 、 -cmin 、 -cnewer 、 -delete 、 -empty 、-fstype 、` `-iname 、 -inum 、 -iregex 、 -ls 、 -maxdepth 、 -mindepth 、 -mmin 、` `-path 、 -print0 、 -regex 、 -sparse` 和所有与 `-B*` 诞生时间相关的初选都是对 IEEE Std 1003.1-2001 (“POSIX.1”) 的扩展。

从历史上看， `-d` `-、` `-L` 和 `-x` 选项是使用初级 `-depth`, `-follow` 和 `-xdev` 实现的。 这些初选总是被评估为真。 由于它们实际上是在遍历开始之前生效的全局变量，因此某些合法表达式可能会产生意想不到的结果。 一个例子是表达式 `-print` `-o` `-depth` 。 由于 `-print` 始终评估为 true，因此标准的评估顺序意味着永远不会评估 `-depth` 。 不是这种情况。

运算符 `-or` 实现为 `-o`, 运算符 `-and` 实现为 `-a` 。

`-exec` 和 `-ok` 主项的历史实现不会替换实用程序名称或实用程序参数中的字符串 “`{}`” （如果它前面或后面有非空白字符）。 无论它出现在实用程序名称或参数中的哪个位置，此版本都会替换它。

`-E` 选项的灵感来自等效的 grep(1) 和 sed(1) 选项。

[历史](#__u5386___u53F2_)
=======================

`find` 命令出现在 Version 1 AT&T UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

`find` 使用的特殊字符也是许多 shell 程序的特殊字符。 特别是字符 “`* 、`” “`[ 、`” “`] 、`” “`? 、`” “`( 、`” “`) 、`” “`! 、`” “`\`” 和 “`;`” 可能必须从 shell 中逃脱。

由于没有分隔选项和文件名或文件名和 expression 的分隔符，因此很难指定名为 \-xdev 或 ! 的文件。 这些问题由 `-f` 选项和 getopt(3) “`-``-`” 结构处理。

`-delete` primary 无法与导致文件系统树遍历选项更改的其他选项很好地交互。

`-mindepth` 和 `-maxdepth` primaries 实际上是全局选项（如上文所述）。 它们可能应该被看起来像选项的选项所取代。

April 18, 2020

FreeBSD 13.1-RELEASE