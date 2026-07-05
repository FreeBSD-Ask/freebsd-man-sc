# sysctl.8

`sysctl` — 获取或设置内核状态

## 名称

`sysctl`

## 概要

`sysctl [-j jail] [-bdeFhiJlNnoqTtVWx] [-B bufsize] [-f filename] name[=value[,value]] ...`
`sysctl [-j jail] [-bdeFhJlNnoqTtVWx] [-B bufsize] -a`

## 描述

`sysctl` 工具用于获取内核状态，并允许具有适当权限的进程设置内核状态。要获取或设置的状态使用 “管理信息库”（“MIB”）风格的名称描述，表示为以点分隔的组件集合。

可用选项如下：

**`-A`** 等同于 `-o -a`（为兼容性保留）。

**`-a`** 列出当前所有可用的值，但不透明变量或通过 `CTLFLAG_SKIP` 标志排除的变量除外。如果在命令行指定了一个或多个变量名，则忽略此选项。

**`-B`** `bufsize` 将从 `sysctl` 读取的缓冲区大小设置为 `bufsize`。对于长度可变且探测值 0 为有效长度的 `sysctl`（例如 `kern.arandom`），此选项是必需的。

**`-b`** 强制以原始二进制格式输出变量的值。不打印名称，也不输出结尾的换行符。此选项主要用于单个变量。

**`-d`** 打印变量的描述而非其值。

**`-e`** 用 `=` 分隔变量名和值。这适用于生成可重新输入给 `sysctl` 工具的输出。如果指定了 `-N` 或 `-n`，或正在设置变量，则忽略此选项。

**`-F`** 打印变量的格式。这是描述变量类型的附加信息，对于 struct 类型（如 clockinfo、timeval 和 loadavg）最有用。

**`-f`** `filename` 指定一个每行包含一对名称和值的文件。`sysctl` 先读取并处理指定文件，然后处理命令行参数中的名称和值对。注意，指定 `-j` `jail` 选项时，文件将在附加到 jail 之前打开，然后在 jail 内处理。

**`-h`** 格式化输出以便人类而非机器阅读。

**`-i`** 忽略未知的 OID。目的是便于使用 `sysctl` 从各种机器（并非所有机器都运行完全相同的软件）收集数据。

**`-J`** 仅显示 jail prison sysctl 变量（CTLFLAG_PRISON）。

**`-j`** `jail` 在 `jail` 内执行操作（通过 jail id 或 jail 名称）。

**`-l`** 显示变量的值及其长度。此选项不能与 `-N` 选项组合使用。

**`-N`** 仅显示变量名，不显示其值。这对于提供可编程补全的 shell 特别有用。要在 zsh(1)（`ports/shells/zsh`）中启用变量名补全，使用以下代码：

```sh
listsysctls () { set -A reply $(sysctl -AN ${1%.*}) }
compctl -K listsysctls sysctl
```

要在 [tcsh(1)](../man1/tcsh.1.md) 中启用变量名补全，使用：

```sh
complete sysctl 'n/*/`sysctl -Na`/'
```

**`-n`** 不显示变量名。此选项适用于设置 shell 变量。例如，要将 pagesize 保存到变量 `psize` 中，使用：

```sh
set psize=`sysctl -n hw.pagesize`
```

**`-o`** 显示不透明变量（通常被抑制）。打印格式和长度，以及值前 16 字节的十六进制转储。

**`-q`** 抑制 `sysctl` 向标准错误输出的一些警告。

**`-T`** 仅显示可通过 loader 设置的变量（CTLFLAG_TUN）。

**`-t`** 打印变量的类型。

**`-V`** 仅显示 VNET sysctl 变量（CTLFLAG_VNET）。

**`-W`** 仅显示非统计类的可写变量。适用于确定运行时可调 sysctl 的集合。

**`-X`** 等同于 `-x -a`（为兼容性保留）。

**`-x`** 与 `-o` 类似，但打印整个值的十六进制转储，而不仅仅是前几个字节。

`sysctl` 可用的信息包括整数、字符串和不透明类型。`sysctl` 工具仅了解少数不透明类型，其余的将以十六进制转储形式输出。不透明信息如果通过专用程序（如 [ps(1)](../man1/ps.1.md)、[systat(1)](../man1/systat.1.md) 和 [netstat(1)](../man1/netstat.1.md)）获取会更有用。

某些在正常系统运行期间无法修改的变量可通过 [loader(8)](loader.8.md) 可调参数进行初始化。例如，可以通过在 loader.conf(5) 中设置来完成。关于哪些可调参数可用以及如何设置它们，请参见 loader.conf(5)。

字符串和整数信息汇总如下。关于这些变量的详细描述，参见 sysctl(3) 和 [security(7)](../man7/security.7.md)。

“可更改”列表示具有适当权限的进程是否可以更改该值。字符串和整数值可通过 `sysctl` 设置。

| 名称 | 类型 | 可更改 |
| --- | --- | --- |
| `kern.ostype` | string | no |
| `kern.osrelease` | string | no |
| `kern.osrevision` | integer | no |
| `kern.version` | string | no |
| `kern.maxvnodes` | integer | yes |
| `kern.maxproc` | integer | no |
| `kern.maxprocperuid` | integer | yes |
| `kern.maxfiles` | integer | yes |
| `kern.maxfilesperproc` | integer | yes |
| `kern.argmax` | integer | no |
| `kern.securelevel` | integer | raise only |
| `kern.hostname` | string | yes |
| `kern.hostid` | integer | yes |
| `kern.clockrate` | struct | no |
| `kern.posix1version` | integer | no |
| `kern.ngroups` | integer | no |
| `kern.job_control` | integer | no |
| `kern.saved_ids` | integer | no |
| `kern.boottime` | struct | no |
| `kern.domainname` | string | yes |
| `kern.filedelay` | integer | yes |
| `kern.dirdelay` | integer | yes |
| `kern.metadelay` | integer | yes |
| `kern.osreldate` | integer | no |
| `kern.bootfile` | string | yes |
| `kern.corefile` | string | yes |
| `kern.logsigexit` | integer | yes |
| `security.bsd.suser_enabled` | integer | yes |
| `security.bsd.see_other_uids` | integer | yes |
| `security.bsd.see_other_gids` | integer | yes |
| `security.bsd.see_jail_proc` | integer | yes |
| `security.bsd.unprivileged_proc_debug` | integer | yes |
| `security.bsd.unprivileged_read_msgbuf` | integer | yes |
| `vm.loadavg` | struct | no |
| `hw.machine` | string | no |
| `hw.model` | string | no |
| `hw.ncpu` | integer | no |
| `hw.byteorder` | integer | no |
| `hw.physmem` | integer | no |
| `hw.usermem` | integer | no |
| `hw.pagesize` | integer | no |
| `hw.floatingpoint` | integer | no |
| `hw.machine_arch` | string | no |
| `hw.realmem` | integer | no |
| `machdep.adjkerntz` | integer | yes |
| `machdep.disable_rtc_set` | integer | yes |
| `machdep.guessed_bootdev` | string | no |
| `user.cs_path` | string | no |
| `user.bc_base_max` | integer | no |
| `user.bc_dim_max` | integer | no |
| `user.bc_scale_max` | integer | no |
| `user.bc_string_max` | integer | no |
| `user.coll_weights_max` | integer | no |
| `user.expr_nest_max` | integer | no |
| `user.line_max` | integer | no |
| `user.re_dup_max` | integer | no |
| `user.posix2_version` | integer | no |
| `user.posix2_c_bind` | integer | no |
| `user.posix2_c_dev` | integer | no |
| `user.posix2_char_term` | integer | no |
| `user.posix2_fort_dev` | integer | no |
| `user.posix2_fort_run` | integer | no |
| `user.posix2_localedef` | integer | no |
| `user.posix2_sw_dev` | integer | no |
| `user.posix2_upe` | integer | no |
| `user.stream_max` | integer | no |
| `user.tzname_max` | integer | no |
| `user.localbase` | string | no |

## 文件

**sys/sysctl.h** 顶层标识符、第二级内核和硬件标识符，以及用户级标识符的定义

**sys/socket.h** 第二级网络标识符的定义

**sys/gmon.h** 第三级性能分析标识符的定义

**vm/vm_param.h** 第二级虚拟内存标识符的定义

**netinet/in.h** 第三级 Internet 标识符和第四级 IP 标识符的定义

**netinet/icmp_var.h** 第四级 ICMP 标识符的定义

**netinet/udp_var.h** 第四级 UDP 标识符的定义

## 退出状态

`sysctl` 工具成功时退出状态为 0，出错时大于 0。

## 实例

例如，要获取系统中允许的最大进程数，使用以下请求：

```sh
sysctl kern.maxproc
```

要将每个 uid 允许的最大进程数设置为 1000，使用以下请求：

```sh
sysctl kern.maxprocperuid=1000
```

获取系统时钟速率信息：

```sh
sysctl kern.clockrate
```

获取负载平均值历史信息：

```sh
sysctl vm.loadavg
```

实际存在比上述更多的变量，而要查找它们更深层含义的最佳（可能也是唯一）去处无疑是定义它们的源代码。

## 兼容性

`-w` 选项废弃，被静默忽略。

## 参见

sysctl(3), [dtrace_mib(4)](../man4/dtrace_mib.4.md), loader.conf(5), [sysctl.conf(5)](../man5/sysctl.conf.5.md), [security(7)](../man7/security.7.md), [loader(8)](loader.8.md), [jail(8)](jail.8.md)

## 历史

`sysctl` 工具首次出现于 4.4BSD。

在 FreeBSD 2.2 中，`sysctl` 经过了重大改造。

## 缺陷

`sysctl` 工具目前利用未公开的接口访问内核 [sysctl(9)](../man9/sysctl.9.md) 设施，以遍历 sysctl 树并获取格式和名称信息。目前仍在考虑正确的接口。
