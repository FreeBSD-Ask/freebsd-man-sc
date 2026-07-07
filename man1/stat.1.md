# stat(1)

`stat` — 显示文件状态

## 名称

`stat`, `readlink`

## 概要

`stat [-FHhLnq] [-f format | -l | -r | -s | -x] [-t timefmt] [file ...]`

`readlink [-fn] [file ...]`

## 描述

`stat` 实用程序显示 `file` 所指向文件的信息。不需要对该命名文件的读、写或执行权限，但路径名中通向该文件的所有目录都必须可搜索。如果未提供参数，`stat` 显示标准输入文件描述符的相关信息。

当以 `readlink` 名称调用时，仅打印符号链接的目标。如果给定参数不是符号链接且未指定 `-f` 选项，`readlink` 将不打印任何内容并以错误退出。如果指定了 `-f` 选项，输出会通过递归跟踪给定路径中每个组件的每个符号链接进行规范化。`readlink` 会同时解析绝对路径和相对路径，并返回与 `file` 对应的绝对路径名。此时参数不必是符号链接。

显示的信息通过以给定参数调用 lstat(2) 并评估返回的结构来获取。默认格式按顺序显示 `st_dev`、`st_ino`、`st_mode`、`st_nlink`、`st_uid`、`st_gid`、`st_rdev`、`st_size`、`st_atime`、`st_mtime`、`st_ctime`、`st_birthtime`、`st_blksize`、`st_blocks` 和 `st_flags` 字段。

选项如下：

**`-F`** 与 [ls(1)](ls.1.md) 相同，在每个是目录的路径名后紧跟斜杠（`/`），在每个可执行文件后紧跟星号（`*`），在每个符号链接后紧跟 at 符号（`@`），在每个 whiteout 后紧跟百分号（`%`），在每个套接字后紧跟等号（`=`），在每个 FIFO 后紧跟竖线（`|`）。使用 `-F` 隐含 `-l`。

**`-H`** 将每个参数视为 NFS 文件句柄的十六进制表示，并使用 fhstat(2) 而非 lstat(2)。此选项需要 root 权限。

**`-h`** 对于每个文件参数，打印一行，由逗号分隔的孔列表、一个空格和文件名组成。每个孔以其起始偏移量（十进制数）报告，后跟连字符和结束偏移量（孔后数据区域的起始偏移量减一，十进制数）。如果文件以孔结尾，最后一个孔的结束偏移量是文件大小减一。否则，列表中的最后一项（实际上，如果文件不是稀疏文件，则是列表中的唯一一项），是与文件大小对应的单个十进制数，表示文件末尾的虚拟孔。如果参数是目录，则不打印孔列表，而是打印一个数字，对应于 pathconf(2) 报告的该目录的最小孔大小，后跟空格和目录名。请注意，获取文件中孔信息的唯一方法是打开它并使用 lseek(2) 遍历孔和数据区域列表。如果在 `stat` 检查文件时另一个进程正在修改该文件，结果可能不一致。此选项不能与 `-F`、`-f`、`-H`、`-L`、`-l`、`-r`、`-s`、`-t` 或 `-x` 选项组合使用。

**`-L`** 使用 stat(2) 而非 lstat(2)。`stat` 报告的信息将指向 `file` 的目标（如果 file 是符号链接），而非 `file` 本身。如果链接断开或目标不存在，则回退到 lstat(2) 并报告该链接的信息。

**`-n`** 不在每段输出的末尾强制换行。

**`-q`** 如果调用 stat(2) 或 lstat(2) 失败，则抑制失败消息。以 `readlink` 运行时，错误消息会自动抑制。

**`-f`** `format` 使用指定格式显示信息。有效格式的描述参见“格式”小节。

**`-l`** 以 `ls` `-lT` 格式显示输出。

**`-r`** 显示原始信息。即对于 `stat` 结构中的所有字段，显示原始数值（例如，以自纪元以来的秒数表示时间等）。

**`-s`** 以“shell 输出”格式显示信息，适合用于初始化变量。

**`-t`** `timefmt` 使用指定格式显示时间戳。此格式直接传递给 strftime(3)。

**`-x`** 以一些 Linux 发行版中已知的更详细方式显示信息。

### 格式

格式字符串类似于 printf(3) 格式：以 `%` 开头，后跟一系列格式化字符，并以一个选择 `struct stat` 中待格式化字段字符结尾。如果 `%` 后紧跟 `n`、`t`、`%` 或 `@` 之一，则打印换行符、制表符、百分号或当前文件编号；否则按以下方式检查字符串：

任意以下可选标志：

**`#`** 为八进制和十六进制输出选择替代输出形式。非零八进制输出会有前导零，非零十六进制输出会前置“`0x`”。

**`+`** 断言应始终打印指示数字正负的符号。非负数通常不带符号打印。

**`-`** 将字符串输出左对齐到字段中，而非右对齐。

**`0`** 将左填充字符设置为 `0` 字符，而非空格。

**space** 在非负有符号输出字段前保留一个空格。如果同时使用 `+` 和空格，`+` 优先。

然后是以下字段：

**`size`** 一个可选的十进制数字字符串，指定最小字段宽度。

**`prec`** 一个可选精度，由小数点“`.`”和十进制数字字符串组成，指示最大字符串长度、浮点输出中小数点后出现的数字位数，或数值输出中出现的最小数字位数。

**`fmt`** 一个可选的输出格式说明符，为 `D`、`O`、`U`、`X`、`F` 或 `S` 之一。分别表示有符号十进制输出、八进制输出、无符号十进制输出、十六进制输出、浮点输出和字符串输出。某些输出格式不适用于所有字段。浮点输出仅适用于 `timespec` 字段（`a`、`m` 和 `c` 字段）。特殊输出说明符 `S` 可用于指示输出（如适用）应为字符串格式。可与以下组合使用：

**`amc`** 以 strftime(3) 格式显示日期。

**`dr`** 显示实际设备名。

**`f`** 以 `ls` `-lTdo` 格式显示 `file` 的标志。

**`gu`** 显示组名或用户名。

**`p`** 以 `ls` `-lTd` 格式显示 `file` 的模式。

**`N`** 显示 `file` 的名称。

**`T`** 显示 `file` 的类型。

**`Y`** 在输出中插入“` - `”。注意 `Y` 的默认输出格式是字符串，但显式指定时，这四个字符会前置。

**`sub`** 一个可选子字段说明符（high、middle、low）。仅适用于 `p`、`d`、`r` 和 `T` 输出格式。可以是以下之一：

**`H`** “High”——指定 `r` 或 `d` 中设备的主设备号，`p` 字符串形式中的“user”权限位，`p` 数值形式中的文件“type”位，以及 `T` 的长输出形式。

**`L`** “Low”——指定 `r` 或 `d` 中设备的次设备号，`p` 字符串形式中的“other”权限位，`p` 数值形式中的“user”、“group”和“other”位，以及与 `T` 一起使用时 `ls` `-F` 风格的文件类型输出字符（此用途使用 `L` 是可选的）。

**`M`** “Middle”——指定 `p` 字符串输出形式中的“group”权限位，或 `p` 数值形式中的“suid”、“sgid”和“sticky”位。

**`datum`** 一个必填字段说明符，为以下之一：

**`d`** `file` 所在设备（`st_dev`）。

**`i`** `file` 的 inode 编号（`st_ino`）。

**`p`** 文件类型和权限（`st_mode`）。

**`l`** 指向 `file` 的硬链接数（`st_nlink`）。

**`u , g`** `file` 属主的用户 ID 和组 ID（`st_uid , st_gid`）。

**`r`** 字符设备和块设备特殊文件的设备号（`st_rdev`）。

**`a , m , c , B`** `file` 上次访问或修改的时间，inode 上次更改的时间，或 inode 的创建时间（`st_atime , st_mtime , st_ctime , st_birthtime`）。

**`z`** `file` 的字节大小（`st_size`）。

**`b`** 为 `file` 分配的块数（`st_blocks`）。

**`k`** 最优文件系统 I/O 操作块大小（`st_blksize`）。

**`f`** `file` 的用户定义标志。

**`v`** inode 生成号（`st_gen`）。

以下五个字段说明符并不直接取自 `struct stat` 中的数据，而是：

**`N`** 文件名。

**`R`** 与文件对应的绝对路径名。

**`T`** 文件类型，与 `ls` `-F` 相同，或在给定 `sub` 字段说明符 `H` 时以更具描述性的形式显示。

**`Y`** 符号链接的目标。

**`Z`** 对于字符或块特殊设备，从 `rdev` 字段展开为“major,minor”；对于其他所有设备，给出大小输出。

只有 `%` 和字段说明符是必填的。大多数字段说明符默认以 `U` 作为输出形式，但 `p` 默认为 `O`；`a`、`m` 和 `c` 默认为 `D`；`Y`、`T` 和 `N` 默认为 `S`。

## 退出状态

`stat` 实用程序成功时退出状态为 0，发生错误时大于 0。

## 实例

如果未指定选项，默认格式为 "%d %i %Sp %l %Su %Sg %r %z \"%Sa\" \"%Sm\" \"%Sc\" \"%SB\" %k %b %#Xf %N"。

```sh
stat /tmp/bar
0 78852 -rw-r--r-- 1 root wheel 0 0 "Jul  8 10:26:03 2004" "Jul  8 10:26:03 2004" "Jul  8 10:28:13 2004" "Jan  1 09:00:00 1970" 16384 0 0 /tmp/bar
```

假设有一个从 **/tmp/foo** 指向 **/** 的符号链接“foo”，可以如下使用 `stat`：

```sh
stat -F /tmp/foo
lrwxrwxrwx 1 jschauma cs 1 Apr 24 16:37:28 2002 /tmp/foo@ -> /

stat -LF /tmp/foo
drwxr-xr-x 16 root wheel 512 Apr 19 10:57:54 2002 /tmp/foo/
```

要初始化一些 shell 变量，可以如下使用 `-s` 标志：

```sh
csh
% eval set `stat -s .cshrc`
% echo $st_size $st_mtimespec
1148 1015432481

sh
$ eval $(stat -s .profile)
$ echo $st_size $st_mtimespec
1148 1015432481
```

要获取文件类型列表（包括当文件是符号链接时所指向的文件），可以使用以下格式：

```sh
$ stat -f "%N: %HT%SY" /tmp/*
/tmp/bar: Symbolic Link -> /tmp/foo
/tmp/output25568: Regular File
/tmp/blah: Directory
/tmp/foo: Symbolic Link -> /
```

要获取设备列表、它们的类型以及主次设备号，并使用制表符和换行符格式化，可以使用以下格式：

```sh
stat -f "Name: %N%n%tType: %HT%n%tMajor: %Hr%n%tMinor: %Lr%n%n" /dev/*
[...]
Name: /dev/wt8
        Type: Block Device
        Major: 3
        Minor: 8

Name: /dev/zero
        Type: Character Device
        Major: 2
        Minor: 12
```

要分别确定文件上设置的权限，可以使用以下格式：

```sh
stat -f "%Sp -> owner=%SHp group=%SMp other=%SLp" .
drwxr-xr-x -> owner=rwx group=r-x other=r-x
```

要确定最近修改的三个文件，可以使用以下格式：

```sh
stat -f "%m%t%Sm %N" /tmp/* | sort -rn | head -3 | cut -f2-
Apr 25 11:47:00 2002 /tmp/blah
Apr 25 10:36:34 2002 /tmp/bar
Apr 24 16:47:35 2002 /tmp/foo
```

显示文件的修改时间：

```sh
stat -f %m /tmp/foo
1177697733
```

以可读格式显示同一修改时间：

```sh
stat -f %Sm /tmp/foo
Apr 27 11:15:33 2007
```

以可读且可排序的格式显示同一修改时间：

```sh
stat -f %Sm -t %Y%m%d%H%M%S /tmp/foo
20070427111533
```

以 UTC 显示：

```sh
sh
$ TZ= stat -f %Sm -t %Y%m%d%H%M%S /tmp/foo
20070427181533
```

## 参见

file(1), [ls(1)](ls.1.md), lstat(2), [readlink(2)](../sys/readlink.2.md), [stat(2)](../sys/stat.2.md), [printf(3)](../stdio/printf.3.md), [strftime(3)](../stdtime/strftime.3.md)

## 历史

`stat` 实用程序出现在 NetBSD 1.6 和 FreeBSD 4.10 中。

## 作者

`stat` 实用程序由 Andrew Brown <atatat@NetBSD.org> 编写。本手册页由 Jan Schaumann <jschauma@NetBSD.org> 编写。
