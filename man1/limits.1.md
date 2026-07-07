# limits(1)

`limits` — set or display process resource limits

## 名称

`limits`

## 概要

`limits [-C class | -P pid | -U user] [-SHB] [-ea] [-bcdfklmnopstuVvwy [val]]`

`limits [-C class | -U user] [-SHB] [-bcdfklmnopstuVvwy [val]] [-E] [name=value ...] [command]`

## 描述

`limits` 实用程序可以打印或设置内核资源限制，还可以选择性地像 [env(1)](env.1.md) 一样设置环境变量，并以选定的资源运行程序。`limits` 实用程序有三种用法：

```sh
eval `limits -e -C daemon`
```

`limits` [`limitflags`] [`name`=`value` ...] `command`

此用法根据 `limitflags` 设置限制，可选择性地设置以 `name`=`value` 对形式给出的环境变量，然后运行指定的 `command`。

`limits` [`limitflags`]

此用法根据 `limitflags` 确定资源设置的值，不尝试设置它们，而是将这些值输出到标准输出。默认情况下，这将输出调用进程当前活动的内核资源设置。使用 `-C` `class` 或 `-U` `user` 选项，你还可以显示由 login.conf(5) 登录能力数据库中相应登录类别资源限制条目修改后的当前资源设置。

`limits` `-e` [`limitflags`]

此用法根据 `limitflags` 确定资源设置的值，但不设置它们。与上一种用法类似，它将这些值输出到标准输出，区别在于它会以 `eval` 格式输出，适用于调用 shell。如果 shell 是已知的（即 `sh`、`csh`、`bash`、`tcsh`、`ksh`、`pdksh` 或 `rc` 之一），`limits` 会以该 shell 能理解的格式输出 `limit` 或 `ulimit` 命令。如果无法确定 shell 的名称，则使用 [sh(1)](sh.1.md) 所使用的 `ulimit` 格式。这对于设置脚本使用的限制，或在启动守护进程和其他具有特定资源限制设置的后台任务之前设置限制非常有用，并且通过在登录类别数据库中维护设置的中央数据库，可以全局配置最大资源使用量。在 shell 脚本中，`limits` 通常会与反引号内的 eval 一起使用，如下所示：

```sh
eval `limits -e -C daemon`
```

这会使 `limits` 的输出被当前 shell 求值并设置。

上述中指定的 `limitflags` 的值包含以下一个或多个选项：

`-C` `class`

使用当前资源值，并按适用于登录类别 `class` 的资源条目进行修改。

`-U` `user`

使用当前资源值，并按适用于 `user` 所属登录类别的资源条目进行修改。如果用户不属于任何类别，则使用"`default`"类别的资源能力（如果存在），如果是超级用户账户则使用"`root`"类别。

`-P` `pid`

为 `pid` 标识的进程选择或设置限制。

`-S`

选择显示或设置"软"（即当前）资源限制。如果此开关后跟有特定的限制设置，则仅影响软限制，除非随后被 `-H` 或 `-B` 选项覆盖。

`-H`

选择显示或设置"硬"（即最大）资源限制。如果此开关后跟有特定的限制设置，则仅影响硬限制，直到随后被 `-S` 或 `-B` 选项覆盖。

`-B`

选择同时显示或设置"软"（当前）和"硬"（最大）资源限制。如果此开关后跟有特定的限制设置，则软限制和硬限制都受到影响，直到随后被 `-S` 或 `-H` 选项覆盖。

`-e`

选择输出的"eval 模式"格式。这仅在显示模式下有效，不能在运行命令时使用。输出的确切语法取决于调用 `limits` 的 shell 类型。

`-b` [`val`]

选择或设置 `sbsize` 资源限制。

`-c` [`val`]

选择或设置（如果指定了 `val`）`coredumpsize` 资源限制。值为 0 时禁用核心转储。

`-d` [`val`]

选择或设置（如果指定了 `val`）`datasize` 资源限制。

`-f` [`val`]

选择或设置 `filesize` 资源限制。

`-k` [`val`]

选择或设置 `kqueues` 资源限制。

`-l` [`val`]

选择或设置 `memorylocked` 资源限制。

`-m` [`val`]

选择或设置 `memoryuse` 大小限制。

`-n` [`val`]

选择或设置 `openfiles` 资源限制。每个进程最大打开文件数的系统范围限制可以通过查看 `kern.maxfilesperproc` [sysctl(8)](../man8/sysctl.8.md) 变量来查看。整个系统中同时打开的文件总数限于 `kern.maxfiles` [sysctl(8)](../man8/sysctl.8.md) 变量所显示的值。

`-o` [`val`]

选择或设置 `umtxp` 资源限制。此限制确定用户拥有的进程可以同时创建的进程共享锁的最大数量，参见 [pthread(3)](../man3/pthread.3.md)。

`-p` [`val`]

选择或设置 `pseudoterminals` 资源限制。

`-s` [`val`]

选择或设置 `stacksize` 资源限制。

`-t` [`val`]

选择或设置 `cputime` 资源限制。

`-u` [`val`]

选择或设置 `maxproc` 资源限制。每个 UID 允许的最大进程数的系统范围限制可以通过查看 `kern.maxprocperuid` [sysctl(8)](../man8/sysctl.8.md) 变量来查看。整个系统中可以同时运行的最大进程数限于 `kern.maxproc` [sysctl(8)](../man8/sysctl.8.md) 变量的值。

`-V` [`val`]

选择或设置 `vmms` 资源限制。

`-v` [`val`]

选择或设置 `virtualmem` 资源限制。此限制涵盖用户进程的整个 VM 空间，包括 text、data、bss、stack、brk(2)、sbrk(2) 和 mmap(2) 的空间。

`-w` [`val`]

选择或设置 `swapuse` 资源限制。

`-y` [`val`]

选择或设置 `pipebuf` 资源限制。

上述选项中 `val` 的有效值包括字符串"`infinity`"、"`inf`"、"`unlimited`"或"`unlimit`"（表示无限或内核定义的最大限制），或者一个数值后跟可选的后缀。与大小相关的值默认以字节为单位，也可以使用以下后缀之一作为乘数：

`b` — 512 字节块。

`k` — 千字节（1024 字节）。

`m` — 兆字节（1024\*1024 字节）。

`g` — 吉字节。

`t` — 太字节。

`cputime` 资源默认以秒数为单位，但可以使用乘数，并且与大小值一样，由有效后缀分隔的多个值会相加：

`s` — 秒。

`m` — 分。

`h` — 小时。

`d` — 天。

`w` — 周。

`y` — 365 天的年。

```sh
eval `limits -U news -aBec 0`
```

`-E`

使 `limits` 完全忽略其继承的环境。

`-a`

强制显示所有资源设置，即使已指定了其他特定资源设置。例如，如果你希望在启动 Usenet News 系统时禁用核心转储，但又希望设置适用于"`news`"账户的所有其他资源设置，可以使用：

与 setrlimit(2) 调用一样，只有超级用户可以提高进程的"硬"资源限制。但是，非 root 用户可以降低硬限制，或将"软"资源限制更改为低于硬限制的任何值。当被调用以执行程序时，`limits` 提高硬限制的失败被视为致命错误。

## 退出状态

如果使用方式有任何错误，即无效选项，或在同一次调用中同时选择了设置/显示选项，或在运行程序时使用了 `-e` 等，`limits` 实用程序将以 `EXIT_FAILURE` 退出。在显示或 eval 模式下运行时，`limits` 以 `EXIT_SUCCESS` 状态退出。在命令模式下运行且命令执行成功时，退出状态为所执行程序返回的状态。

## 实例

显示当前栈大小限制：

```sh
$ limits -s
Resource limits (current):
	  stacksize              524288 kB
```

尝试以 1 字节的 `datasize` 限制运行 [ls(1)](ls.1.md)：

```sh
$ limits -d 1b ls
Data segment size exceeds process limit
Abort trap
```

生成将 `sbsize` 限制为 1 字节的 `eval` 模式输出。从 [sh(1)](sh.1.md) 运行命令时获得的输出：

```sh
$ limits -e -b 1b
ulimit -b 512;
```

从 [csh(1)](csh.1.md) 运行时与上面相同：

```sh
% limits -e -b 1b
limit -h sbsize 512;
limit sbsize 512;
```

## 参见

[csh(1)](csh.1.md), [env(1)](env.1.md), limit(1), [sh(1)](sh.1.md), getrlimit(2), setrlimit(2), login_cap(3), login.conf(5), rctl(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`limits` 实用程序首次出现于 FreeBSD 2.1.7。

## 作者

`limits` 实用程序由 David Nugent <davidn@FreeBSD.org> 编写。

## 缺陷

由于显而易见的原因，`limits` 实用程序不处理名称中包含等号（`=`）的命令。

`limits` 实用程序不确保输出或显示的资源设置对当前用户有效且可设置。只有超级用户账户可以提高硬限制，并且在这样做时，如果给定的值过高，FreeBSD 内核会默默地将其降低到小于指定值的值。
