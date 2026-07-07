# locate(1)

`locate` — 快速查找文件名

## 名称

`locate`

## 概要

`locate [-0Scims] [-l limit] [-d database] pattern ...`

## 描述

`locate` 程序在数据库中搜索所有与指定 `pattern` 匹配的路径名。数据库会定期重新计算（通常每周或每天一次），其中包含所有可公开访问的文件的路径名。

Shell globbing 和 quoting 字符（"`*`"、"`?`"、"`\`"、"`[`" 和 "`]`"）可在 `pattern` 中使用，但需要对 shell 进行转义。在任何字符前加反斜杠（"`\`"）可消除其可能具有的特殊含义。匹配的不同之处在于，无需显式匹配任何字符，包括斜杠（"`/`"）。

作为一种特殊情况，不包含 globbing 字符的模式（"`foo`"）会按照 "`*foo*`" 的方式进行匹配。

历史上，locate 仅存储 32 到 127 之间的字符。当前的实现存储除换行符（`'\n'`）和 `NUL`（`'\0'`）之外的任何字符。8 位字符支持不会为纯 ASCII 文件名浪费额外空间。小于 32 或大于 127 的字符以 2 字节存储。

可用选项如下：

**`-0`** 以 ASCII `NUL` 字符（字符代码 0）分隔打印路径名，而非默认的 NL（换行符，字符代码 10）。

**`-S`** 打印有关数据库的一些统计信息并退出。

**`-c`** 抑制正常输出；改为打印匹配的文件名计数。

**`-d`** `database` 在 `database` 中搜索，而非使用默认的文件名数据库。允许指定多个 `-d` 选项。每个额外的 `-d` 选项将指定的数据库添加到要搜索的数据库列表中。`database` 选项可以是用冒号分隔的数据库列表。单个冒号表示引用默认数据库。

```sh
$ locate -d $HOME/lib/mydb: foo
```

将首先在 **$HOME/lib/mydb** 中搜索字符串 "`foo`"，然后在 **/var/db/locate.database** 中搜索。

```sh
$ locate -d $HOME/lib/mydb::/cdrom/locate.database foo
```

将首先在 **$HOME/lib/mydb** 中搜索字符串 "`foo`"，然后在 **/var/db/locate.database** 中搜索，最后在 **/cdrom/locate.database** 中搜索。

```sh
$ locate -d db1 -d db2 -d db3 pattern
```

等同于

```sh
$ locate -d db1:db2:db3 pattern
```

或

```sh
$ locate -d db1:db2 -d db3 pattern
```

如果将 `-` 作为数据库名称给出，则改为读取标准输入。例如，你可以压缩数据库并使用：

```sh
$ zcat database.gz | locate -d - pattern
```

这在 CPU 速度快、内存少且 I/O 慢的机器上可能有用。注意：标准输入只能使用*一个* pattern。

**`-i`** 在模式和数据库中忽略大小写差异。

**`-l`** `number` 将输出限制为 `number` 个文件名并退出。

**`-m`** 使用 [mmap(2)](../man2/mmap.2.md) 而非 [stdio(3)](../man3/stdio.3.md) 库。这是默认行为，在大多数情况下更快。

**`-s`** 使用 [stdio(3)](../man3/stdio.3.md) 库而非 [mmap(2)](../man2/mmap.2.md)。

## 环境变量

**`LOCATE_PATH`** locate 数据库的路径（若已设置且非空）；若指定了 `-d` 选项则忽略。

## 文件

**/var/db/locate.database** locate 数据库

**/usr/libexec/locate.updatedb** 更新 locate 数据库的脚本

**/etc/periodic/weekly/310.locate** 启动数据库重建的脚本

## 参见

[find(1)](find.1.md), [whereis(1)](whereis.1.md), [which(1)](which.1.md), [fnmatch(3)](../man3/fnmatch.3.md), [locate.updatedb(8)](../man8/locate.updatedb.8.md)

> Woods, James A., "Finding Files Fast", *;login*, 8:1, pp. pp. 8-10, 1983.

## 历史

`locate` 命令首次出现于 4.4BSD。许多新特性在 FreeBSD 2.2 中加入。

## 缺陷

`locate` 程序可能无法列出某些存在的文件，或者可能列出已从系统中移除的文件。这是因为 locate 仅报告数据库中存在的文件，而数据库通常仅由 **/etc/periodic/weekly/310.locate** 脚本每周重新生成一次。使用 [find(1)](find.1.md) 来查找更具临时性的文件。

`locate` 数据库通常由用户 "nobody" 构建，而 [locate.updatedb(8)](../man8/locate.updatedb.8.md) 实用程序会跳过对用户 "nobody"、组 "nobody" 或所有用户不可读的目录。例如，如果你的 HOME 目录不是对所有用户可读，则你的文件*一个也不会*出现在数据库中。

`locate` 数据库不独立于字节序。无法在不同字节序的机器之间共享数据库。当前的 `locate` 实现可以理解主机字节序或网络字节序的数据库，前提是两种架构使用相同的整数大小。因此，在 FreeBSD/i386 机器（小端序）上，你可以读取在 SunOS/sparc 机器（大端序，网络字节序）上构建的 locate 数据库。

`locate` 实用程序不识别多字节字符。
