# procstat(1)

`procstat` — 获取详细进程信息

## 名称

`procstat`

## 概要

`procstat [--libxo] [-h] [-M core] [-N system] [-w interval] command [pid ... | core ...] procstat [--libxo] -a [-h] [-M core] [-N system] [-w interval] command procstat [--libxo] [-h] [-M core] [-N system] [-w interval] [-b | -c | -e | -f [-C] | -i [-n] | -j [-n] | -k [-k] | -l | -r [-H] | -s | -S | -t | -v | -x] [pid ... | core ...] procstat [--libxo] -a [-h] [-M core] [-N system] [-w interval] [-b | -c | -e | -f [-C] | -i [-n] | -j [-n] | -k [-k] | -l | -r [-H] | -s | -S | -t | -v | -x] procstat [--libxo] -L [-h] [-M core] [-N system] [-w interval] core ... pargs [--libxo] pid ... penv [--libxo] pid ... pwdx [--libxo] pid ...`

## 描述

`procstat` 实用程序显示由 `pid` 参数标识的进程的详细信息，或在使用 `-a` 标志时显示所有进程的信息。它还可以显示从进程 core 文件中提取的信息，如果将 core 文件指定为参数。

`pargs`、`penv` 和 `pwdx` 实用程序分别显示由 `pid` 参数指定进程的参数、环境和当前工作目录。它们模仿 Solaris 中同名实用程序的行为。

如果指定了 `--libxo` 标志，输出将通过 [libxo(3)](../man3/libxo.3.md) 以多种人类和机器可读格式生成。有关命令行参数的详细信息，参见 [xo_options(7)](../man7/xo_options.7.md)。

`procstat` 可用以下命令：

**`advlock`** 打印文件上的咨询锁信息。列出所有三种类型的锁：BSD 风格的 lockf(2)、POSIX 风格的 [fcntl(2)](../sys/fcntl.2.md) `F_SETLK`，以及 NFSv3 使用的远程 lockd(8) 锁。注意，`-a` 选项和 `pid` 列表都不能用于限制锁的显示，主要是因为某些类型的锁没有本地（或任何）拥有进程。

**`argument(s)`** | **`-c`** 显示进程的命令行参数。接受子串命令。

**`auxv`** | **`-x`** 显示进程的 ELF 辅助向量。

**`basic`** 打印基本进程统计信息（默认）。

**`binary`** | **`-b`** 显示进程的二进制信息。接受子串命令。

**`credential(s)`** | **`-s`** 显示进程的安全凭证信息。接受子串命令。

**`cpuset`** | **`cs`** | **`-S`** 显示线程的 cpuset 信息。

**`environment`** | **`-e`** 显示进程的环境变量。接受子串命令。

**`file(s)`** | **`fd(s)`** | **`-f`** 显示进程的文件描述符信息。如果使用 `-C` 子命令标志，则打印额外的能力信息。

**`kqueue(s)`** [`-v`] 显示进程 kqueue 中注册的事件。显示过滤器名称、过滤器特定标识符、标志、过滤器特定标志、系统和用户数据，以及事件状态。如果为子命令提供 `-v` 冗余标志，还会显示 ext 数组的值。对于标志，打印由以下符号组成的字符串，对应已设置的标志：

| 符号 | 标志 |
| :--- | :--- |
| **O** | `EV_ONESHOT` |
| **C** | `EV_CLEAR` |
| **\`** | `EV_RECEIPT` |
| **D** | `EV_DISPATCH` |
| **d** | `EV_DROP` |
| **1** | `EV_FLAG1` |
| **2** | `EV_FLAG2` |

对于状态：

| 符号 | 状态 |
| :--- | :--- |
| **A** | `KNOTE_STATUS_ACTIVE` |
| **Q** | `KNOTE_STATUS_QUEUED` |
| **D** | `KNOTE_STATUS_DISABLED` |
| **d** | `KNOTE_STATUS_DETACHED` |
| **K** | `KNOTE_STATUS_KQUEUE` |

**`kstack`** | **`-k`** 显示进程中内核线程的堆栈，不包括当前在 CPU 上以用户空间运行的线程堆栈。如果使用 `-v` 子命令选项（或重复命令标志），则打印函数偏移和函数名。

**`pargs`** 显示进程的参数。

**`penv`** 显示进程的环境变量。

**`ptlwpinfo`** | **`-L`** 显示进程有关其信号驱动退出的 LWP 信息。

**`pwdx`** 显示进程的当前工作目录。

**`rlimit`** | **`-l`** 显示进程的资源限制。

**`rlimitusage`** 显示进程的资源限制使用情况。

**`rusage`** | **`-r`** 显示进程的资源使用信息。如果使用 `-v`（或 `-H`）子命令标志，则打印每线程统计信息而非每进程统计信息。表中的第二个字段将列出信息行对应的线程 ID。

**`signal(s)`** | **`-i`** 显示进程的信号待处理和处置信息。如果使用 `-n` 子命令选项，则显示信号编号而非信号名称。接受子串命令。

**`thread(s)`** | **`-t`** 显示进程的线程信息。

**`tsignal(s)`** | **`-j`** 显示进程线程的信号待处理和阻塞信息。如果使用 `-n` 子命令选项，则显示信号编号而非信号名称。接受子串命令。

**`vm`** | **`-v`** 显示进程的虚拟内存映射。

所有选项以表格格式生成输出，第一个字段是信息行对应的进程 ID。`-h` 标志可用于抑制表头。

`-w` 标志可用于指定重复打印所请求进程信息的等待间隔。如果未指定 `-w` 标志，输出将不会重复。

VM、文件描述符和 cpuset 选项的信息仅对进程所有者或超级用户可用。显示为 -1 的 cpuset 值表示信息无效或不可用。

### 二进制信息

显示进程 ID、命令和进程二进制文件路径：

**PID** 进程 ID

**COMM** 命令

**OSREL** 进程二进制文件的 osreldate

**PATH** 进程二进制文件路径（如果可用）

### 命令行参数

显示进程 ID、命令和命令行参数：

**PID** 进程 ID

**COMM** 命令

**ARGS** 命令行参数（如果可用）

### 环境变量

显示进程 ID、命令和环境变量：

**PID** 进程 ID

**COMM** 命令

**ENVIRONMENT** 环境变量（如果可用）

### 文件描述符

显示进程引用的每个文件描述符的详细信息，包括进程 ID、命令、文件描述符编号和每个文件描述符的对象信息（如对象类型和文件系统路径）。默认情况下，将打印以下信息：

**PID** 进程 ID

**COMM** 命令

**FD** 文件描述符编号或 cwd/root/jail

**T** 文件描述符类型

**V** vnode 类型

**FLAGS** 文件描述符标志

**REF** 文件描述符引用计数

**OFFSET** 文件描述符偏移

**PRO** 网络协议

**NAME** 文件路径或套接字地址（如果可用）

以下文件描述符类型可能显示：

**e** POSIX 信号量

**E** eventfd

**f** fifo

**h** 共享内存

**i** inotify 描述符

**k** kqueue

**m** 消息队列

**P** 进程描述符

**p** 管道

**s** 套接字

**t** 伪终端主端

**v** vnode

以下 vnode 类型可能显示：

**-** 非 vnode

**b** 块设备

**c** 字符设备

**d** 目录

**f** fifo

**l** 符号链接

**r** 常规文件

**s** 套接字

**x** 已撤销设备

以下文件描述符标志可能显示：

**r** 读

**w** 写

**a** 追加

**s** 异步

**f** fsync

**n** 非阻塞

**d** 直接 I/O

**l** 持有锁

如果指定了 `-C` 标志，vnode 类型、引用计数和偏移字段将被省略，并包含新的能力字段，列出每个能力描述符存在的能力，如 [cap_rights_limit(2)](../sys/cap_rights_limit.2.md) 中所述。

以下网络协议可能显示（按地址族分组）：

`AF_INET`, `AF_INET6`

**ICM** `IPPROTO_ICMP`；参见 [icmp(4)](../man4/icmp.4.md)。

**IP?** 未知协议。

**RAW** `IPPROTO_RAW`；参见 [ip(4)](../man4/ip.4.md)。

**SCT** `IPPROTO_SCTP`；参见 [sctp(4)](../man4/sctp.4.md)。

**TCP** `IPPROTO_TCP`；参见 [tcp(4)](../man4/tcp.4.md)。

**UDP** `IPPROTO_UDP`；参见 [udp(4)](../man4/udp.4.md)。

`AF_LOCAL`

**UDD** 数据报套接字。

**UDS** 流套接字。

**UDQ** 顺序包流套接字。

**UD?** 未知协议。

`AF_DIVERT`

**IPD** Divert 套接字；参见 [divert(4)](../man4/divert.4.md)。

**?** 未知地址族。

### 信号处置信息

显示进程的信号待处理和处置：

**P** 如果信号在全局进程队列中待处理；否则为 -。

**\*** 如果信号传递处置为 `SIG_IGN`；否则为 -。

**C** 如果信号将被捕获；否则为 -。

**PID** 进程 ID

**COMM** 命令

**SIG** 信号名称

**FLAGS** 进程信号处置详情，三个符号

如果指定了 `-n` 开关，则显示信号编号而非信号名称。

### 线程信号信息

显示进程线程的信号待处理和阻塞：

**P** 如果信号在线程中待处理；否则为 -

**\*** 如果信号在线程信号掩码中被阻塞；如果未阻塞则为 -

**PID** 进程 ID

**TID** 线程 ID

**COMM** 命令

**SIG** 信号名称

**FLAGS** 线程信号传递状态，两个符号

`-n` 开关与 `-i` 开关效果相同：显示信号编号而非信号名称。

### 内核线程堆栈

显示进程的内核线程堆栈，允许进一步解释线程等待通道。如果重复 `-k` 标志，则打印函数偏移，而非仅函数名。

此功能需要内核编译时包含 `options STACK` 或 `options DDB`。

**PID** 进程 ID

**TID** 线程 ID

**COMM** 命令

**TDNAME** 线程名

**KSTACK** 内核线程调用栈

### 资源限制

显示进程的资源限制：

**PID** 进程 ID

**COMM** 命令

**RLIMIT** 资源限制名称

**SOFT** 软限制

**HARD** 硬限制

### 资源使用

显示进程的资源使用情况。如果指定了 `-H` 标志，则显示各个线程的资源使用情况。

**PID** 进程 ID

**TID** 线程 ID（如果指定了 `-H`）

**COMM** 命令

**RESOURCE** 资源名称

**VALUE** 当前使用量

### 安全凭证

显示进程凭证信息：

**PID** 进程 ID

**COMM** 命令

**EUID** 有效用户 ID

**RUID** 实际用户 ID

**SVUID** 保存的用户 ID

**EGID** 有效组 ID

**RGID** 实际组 ID

**SVGID** 保存的组 ID

**UMASK** 文件创建模式掩码

**FLAGS** 凭证标志

**GROUPS** 组集

以下凭证标志可能显示：

**C** 能力模式

### 线程信息

显示每线程信息，包括进程 ID、每线程 ID、名称、CPU 和执行状态：

**PID** 进程 ID

**TID** 线程 ID

**COMM** 命令

**TDNAME** 线程名

**CPU** 当前或最近运行的 CPU

**PRI** 线程优先级

**STATE** 线程状态

**WCHAN** 线程等待通道

### 虚拟内存映射

显示进程虚拟内存映射，包括地址、映射元数据和映射对象信息：

**PID** 进程 ID

**START** 映射起始地址

**END** 映射结束地址

**PRT** 保护标志

**RES** 常驻页面

**PRES** 私有常驻页面

**REF** 引用计数

**SHD** 影子页面计数

**FLAG** 映射标志

**TP** VM 对象类型

以下保护标志可能显示：

**r** 读

**w** 写

**x** 执行

以下 VM 对象类型可能显示：

**--** 无

**dd** dead

**df** default

**dv** device

**md** 具有受管理页面的设备（GEM/TTM）

**ph** physical

**sg** scatter/gather

**sw** swap

**vn** vnode

**gd** guard（伪类型）

以下映射标志可能显示：

**C** 写时复制

**N** 需要复制

**S** 使用一个或多个超级页面映射

**D** 向下增长（自顶向下栈）

**U** 向上增长（自底向上栈

**W** 此范围内的页面被 [mlock(2)](../sys/mlock.2.md) 或 [mlockall(2)](../sys/mlockall.2.md) 锁定

### ELF 辅助向量

显示 ELF 辅助向量值：

**PID** 进程 ID

**COMM** 命令

**AUXV** 辅助向量名称

**VALUE** 辅助向量值

### 咨询锁信息

**RW** 读/写类型，`RO` 为读锁，`RW` 为写锁

**TYPE** 锁类型，`FLOCK` 表示 [flock(2)](../sys/flock.2.md)、`FCNTL` 表示 [fcntl(2)](../sys/fcntl.2.md)、`LOCKD` 表示远程锁

**PID** 拥有者进程 ID，用于 `FCNTL` 和远程类型

**SYSID** 远程系统 ID（如适用）

**FSID** 锁定文件所在文件系统 ID

**RDEV** 文件系统的 rdev

**INO** 锁定文件在文件系统上的唯一文件标识符（inode 编号）

**START** 锁定范围的起始偏移

**LEN** 锁定范围的长度。零表示到 EOF

**PATH** 锁定文件的路径（如果可用）

## 退出状态

`procstat` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示当前 shell 的二进制信息：

```sh
$ procstat binary $$
  PID COMM                OSREL PATH
46620 bash              1201000 /usr/local/bin/bash
```

与上述相同，但显示打开文件描述符的信息：

```sh
$ procstat files $$
  PID COMM                FD T V FLAGS    REF  OFFSET PRO NAME
46620 bash              text v r r-------   -       - -   /usr/local/bin/bash
46620 bash              ctty v c rw------   -       - -   /dev/pts/12
46620 bash               cwd v d r-------   -       - -   /tmp
46620 bash              root v d r-------   -       - -   /
46620 bash                 0 v c rw------   7  372071 -   /dev/pts/12
46620 bash                 1 v c rw------   7  372071 -   /dev/pts/12
46620 bash                 2 v c rw------   7  372071 -   /dev/pts/12
46620 bash               255 v c rw------   7  372071 -   /dev/pts/12
```

显示用于启动 [init(8)](../man8/init.8.md) 的参数：

```sh
$ procstat arguments 1
  PID COMM             ARGS
    1 init             /sbin/init --
```

从 core 转储中提取二进制信息：

```sh
$ procstat binary core.36642
  PID COMM                OSREL PATH
36642 top               1201000 /usr/bin/top
```

尝试从不同主 FreeBSD 版本生成的 core 文件中提取信息时，可能显示如下错误：

```sh
$ procstat mplayer.core
procstat: kinfo_proc structure size mismatch
procstat: procstat_getprocs()
```

## 参见

[fstat(1)](fstat.1.md), [ps(1)](ps.1.md), [sockstat(1)](sockstat.1.md), [cap_enter(2)](../sys/cap_enter.2.md), [cap_rights_limit(2)](../sys/cap_rights_limit.2.md), [inotify(2)](../sys/inotify.2.md), [mlock(2)](../sys/mlock.2.md), [mlockall(2)](../sys/mlockall.2.md), libprocstat(3), [libxo(3)](../man3/libxo.3.md), [signal(3)](../gen/signal.3.md), [xo_options(7)](../man7/xo_options.7.md), [ddb(4)](../man4/ddb.4.md), [divert(4)](../man4/divert.4.md), [icmp(4)](../man4/icmp.4.md), [ip(4)](../man4/ip.4.md), [sctp(4)](../man4/sctp.4.md), [tcp(4)](../man4/tcp.4.md), [udp(4)](../man4/udp.4.md), [stack(9)](../man9/stack.9.md)

## 作者

Robert N M Watson <rwatson@FreeBSD.org>。[libxo(3)](../man3/libxo.3.md) 支持由 Allan Jude <allanjude@FreeBSD.org> 添加。Juraj Lutter <juraj@lutter.sk> 添加了 pargs、penv 和 pwdx 功能。

## 缺陷

打开文件或内存映射路径名的显示使用内核的名称缓存实现。如果文件系统不使用名称缓存，或文件路径不在缓存中，则不会显示路径。

`procstat` 目前仅支持从活动内核提取数据，不支持从内核崩溃转储中提取。
