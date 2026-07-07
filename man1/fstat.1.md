# fstat(1)

`fstat` — 识别活动文件

## 名称

`fstat`

## 概要

`fstat [-fmnsv] [-M core] [-N system] [-p pid] [-u user] [file]`

## 描述

`fstat` 实用程序用于识别打开的文件。如果一个文件被进程显式打开、作为工作目录、根目录、Jail 根目录、活动可执行文本或该进程的内核跟踪文件，则该文件被视为已被该进程打开。如果未指定选项，`fstat` 将报告用户有权访问的进程中所有打开的文件。

以下选项可用：

**`-f`** 将检查范围限制为与指定文件参数在同一文件系统中打开的文件，如果没有额外的文件名参数，则限制为包含当前目录的文件系统。例如，要查找目录 **/usr/src** 所在文件系统中所有打开的文件，输入 `fstat -f /usr/src`。

**`-M`** `core` 从指定的 core 文件而非默认的 **/dev/kmem** 中提取与名称列表关联的值。

**`-m`** 在列表中包含内存映射文件；由于需要额外处理，通常这些会被排除。

**`-N`** `system` 从指定的 system 文件而非默认值中提取名称列表，默认值是系统启动时所用的内核映像。

**`-n`** 数值格式。打印文件所在文件系统的设备号 (maj,min) 而非挂载点名称；对于特殊文件，打印特殊设备所引用的设备号而非 **/dev** 中的文件名；并以八进制而非符号形式打印文件模式。

**`-p`** `pid` 报告指定进程打开的所有文件。

**`-s`** 打印套接字端点信息。

**`-u`** `user` 报告指定用户打开的所有文件。

**`-v`** 冗余模式。在无法定位特定系统数据结构时打印错误消息，而非静默忽略。这些数据结构大多是动态创建或删除的，在 `fstat` 运行时它们可能消失。这是正常且不可避免的，因为 `fstat` 运行时系统的其余部分也在运行。

**`file`** 将报告限制为指定文件。

以下字段将被打印：

**jail** Jail 根目录

**mmap** 内存映射文件

**root** 根 inode

**text** 可执行文本 inode

**tr** 内核跟踪文件

**wd** 当前工作目录

**USER** 进程所有者的用户名（有效 uid）。

**CMD** 进程的命令名。

**PID** 进程 ID。

**FD** 进程级打开文件表中的文件编号，或以下特殊名称之一：如果文件编号后跟星号（`*`），则该文件不是 inode，而是套接字、FIFO，或存在错误。在这种情况下，该行的其余部分不对应于剩余的表头——该行的格式在后面的套接字部分描述。

**MOUNT** 如果未指定 `-n` 标志，则显示此表头，表示文件所在文件系统的挂载路径名。

**DEV** 如果指定了 `-n` 标志，则显示此表头，表示该文件所在设备的编号。

**INUM** 文件的 inode 编号。

**MODE** 文件的模式。如果未指定 `-n` 标志，模式以符号格式打印（参见 [strmode(3)](../man3/strmode.3.md)）；否则，模式以八进制数打印。

**SZ|DV** 如果文件是信号量，打印信号量的当前值。如果文件不是字符或块特殊文件，打印文件的字节大小。否则，如果未指定 `-n` 标志，打印位于 **/dev** 中的特殊文件名。如果无法定位，或指定了 `-n` 标志，打印特殊设备所引用的主/次设备号。

**R/W** 此列描述文件允许的访问模式。字母 `r` 表示以读方式打开；字母 `w` 表示以写方式打开。此字段在查找阻止文件系统降级为只读的进程时很有用。

**NAME** 如果指定了文件名参数且未指定 `-f` 标志，则显示此字段，表示与给定文件关联的名称。通常无法确定名称，因为不存在从打开文件回到用于打开该文件的目录项的映射。此外，由于不同的目录项可能引用同一文件（通过 [ln(1)](ln.1.md)），打印的名称可能不是进程最初用于打开该文件的实际名称。

## 套接字

打开套接字的格式取决于协议域。在所有情况下，第一个字段是域名，第二个字段是套接字类型（stream、dgram 等），第三个是套接字标志字段（十六进制）。其余字段取决于协议。对于 TCP，是 tcpcb 的地址；对于 UDP，是 inpcb（套接字 pcb）。对于 UNIX 域套接字，是套接字 pcb 的地址和已连接 pcb 的地址（如果已连接）。否则打印套接字本身的协议号和地址。

例如，上述地址是 `netstat -A` 命令为 TCP、UDP 和 UNIX 域打印的地址。注意，由于管道使用套接字实现，管道显示为已连接的 UNIX 域流套接字。单向 UNIX 域套接字用箭头（`<-` 或 `->`）指示流向，全双工套接字显示双箭头（`<->`）。

使用 `-s` 标志时，套接字端点信息显示在套接字地址之后。对于 internet 套接字，显示本地和远程地址，以双箭头（`<->`）分隔。对于 UNIX/local 套接字，显示本地或远程地址，取决于哪个可用。

## 退出状态

`fstat` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示除 `fstat` 自身打开以外的所有打开文件：

```sh
$ fstat | awk '$2 != "fstat"'
USER     CMD          PID   FD MOUNT      INUM MODE         SZ|DV R/W
alice  bash         469 text /usr/local 143355 -rwxr-xr-x  1166448  r
alice  bash         469 ctty /dev        346 crw--w----  pts/81 rw
...
```

报告当前 shell 在 **/usr/local** 所在文件系统中打开的所有文件，包括内存映射文件：

```sh
$ fstat -m -p $$ -f /usr/local
USER     CMD          PID   FD MOUNT      INUM MODE         SZ|DV R/W
bob  bash         469 text /usr/local 143355 -rwxr-xr-x  1166448  r
bob  bash         469 mmap /usr/local 143355 -rwxr-xr-x  1166448  r
...
```

查询未打开文件的信息时，只输出表头行而非错误：

```sh
$ fstat /etc/rc.conf
USER     CMD          PID   FD MOUNT      INUM MODE         SZ|DV R/W NAME
```

`-f` 之后的所有参数都将被解释为文件，因此以下命令不会按预期工作：

```sh
$ fstat -f /usr/local -m -p $$
fstat: -m: No such file or directory
fstat: -p: No such file or directory
fstat: 469: No such file or directory
...
```

显示 firefox 进程打开的管道数量：

```sh
$ fstat | awk '$2=="firefox" && $5=="pipe"' | wc -l
```

显示用户 “bob” 中标准错误描述符在 ttyv0 中打开的进程：

```sh
$ fstat -u bob | awk '$4 == 2 && $8 == "ttyv0"'
bob  firefox    77842    2 /dev        103 crw-------   ttyv0 rw
bob  xinit       1194    2 /dev        103 crw-------   ttyv0 rw
...
```

显示已打开的 TCP 套接字。此输出类似于 `netstat -A -p tcp` 生成的输出：

```sh
$ fstat | awk '$7 == "tcp"'
alice  firefox    77991   32* internet stream tcp fffff800b7f147a0
alice  firefox    77991  137* internet stream tcp fffff800b7f12b70
...
```

显示在当前目录中打开文件的进程列表，模仿 [fuser(1)](fuser.1.md) 的输出：

```sh
$ fstat . | awk 'NR > 1 {printf "%d%s(%s) ", $3, $4, $1;}'
2133wd(alice) 2132wd(alice) 1991wd(alice)
```

创建按打开文件数量降序排列的进程列表：

```sh
$ fstat | awk 'NR > 1 {print $2;}' | sort | uniq -c | sort -r
 728 firefox
  23 bash
  14 sort
   8 fstat
   7 awk
```

## 参见

[fuser(1)](fuser.1.md), [netstat(1)](netstat.1.md), [nfsstat(1)](nfsstat.1.md), [procstat(1)](procstat.1.md), [ps(1)](ps.1.md), [sockstat(1)](sockstat.1.md), [systat(1)](systat.1.md), [tcp(4)](../man4/tcp.4.md), [unix(4)](../man4/unix.4.md), [iostat(8)](../man8/iostat.8.md), pstat(8), [vmstat(8)](../man8/vmstat.8.md)

## 历史

`fstat` 命令出现于 4.3BSD。

## 缺陷

由于 `fstat` 获取的是系统的快照，它只在很短的时间内是准确的。
