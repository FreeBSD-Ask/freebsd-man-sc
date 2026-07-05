# w.1

`w` — 显示谁登录了系统以及他们在做什么

## 名称

`w`

## 概要

`w [--libxo] [-dhin] [-M core] [-N system] [user ...]`

## 描述

`w` 实用程序打印系统当前活动的摘要，包括每个用户正在做什么。第一行显示当前时间、系统已运行多久、登录到系统的用户数以及负载平均值。负载平均值给出在 1、5 和 15 分钟内运行队列中作业的平均数。

输出的字段依次为：用户登录名、用户所在的终端名、用户登录时使用的主机、用户登录的时间、自用户上次键入任何内容以来的时间，以及当前进程的名称和参数。

可用选项如下：

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。命令行参数的细节参见 xo_options(7)。

**`-d`** 按控制 tty 转储整个进程列表，而非仅顶层进程。

**`-h`** 抑制标题行。

**`-i`** 按空闲时间排序输出。

**`-M`** 从指定的 core 而非默认的 **/dev/kmem** 提取与名称列表关联的值。

**`-N`** 从指定的 system 而非默认的 **/boot/kernel/kernel** 提取名称列表。

**`-n`** 不尝试解析网络地址（通常 `w` 会解释地址并尝试以名称形式显示）。当 `-n` 指定多次时，会尝试解析 utmp 中存储的主机名，以网络地址形式显示。

如果指定了一个或多个 `user` 名称，输出将限于这些用户。

## 文件

**/var/run/utx.active** 系统上的用户列表

## 实例

显示系统的全局活动：

```sh
$ w
 8:05PM  up 35 mins, 3 users, load averages: 0.09, 0.35, 0.27
USER       TTY      FROM            LOGIN@  IDLE WHAT
fernape    v0       -               7:30PM     - tmux: client (/tmp/tmux-1001/default) (tmux)
root       v1       -               8:03PM     1 -bash (bash)
fernape    pts/0    tmux(1391).%0   8:04PM     - w
```

按 tty 显示整个进程列表：

```sh
$ w -d
 8:12PM  up 42 mins, 3 users, load averages: 0.01, 0.11, 0.17
USER       TTY      FROM            LOGIN@  IDLE WHAT
                1199      login [pam] (login)
                1207      -bash (bash)
                1507      tmux: client (/tmp/tmux-1001/default) (tmux)
fernape    v0       -               7:30PM     - tmux: client (/tmp/tmux-1001/default) (tmux)
                1488      login [pam] (login)
                1489      -bash (bash)
root       v1       -               8:08PM     3 -bash (bash)
                1510      -bash (bash)
                1515      w -d
fernape    pts/0    tmux(1509).%0   8:11PM     - w -d
```

同上，但仅针对 root 用户并省略标题行：

```sh
$ w -d -h root
		1183      login [pam] (login)
		1204      -bash (bash)
root       v1       -       7:15PM     - -bash (bash)
```

## 兼容性

`-f`、`-l`、`-s` 和 `-w` 标志不再受支持。

## 参见

finger(1), [ps(1)](ps.1.md), [uptime(1)](uptime.1.md), [who(1)](who.1.md), libxo(3), xo_options(7)

## 历史

`w` 命令出现于 3.0BSD。

## 缺陷

“当前进程”的概念模糊不清。当前算法是“终端上编号最大且不忽略中断的进程，若不存在则为终端上编号最大的进程”。这在某些情况下会失败，例如 shell 和编辑器等程序的关键区段中，或后台运行的有缺陷程序派生（fork）后未忽略中断时。（在找不到任何进程的情况下，`w` 打印 `-` `.`。）

CPU 时间仅为估计值，特别是如果有人在注销后仍让后台进程运行，当前在该终端上的用户会被“记入”该时间。

后台进程不予显示，尽管它们占了系统负载的很大一部分。

有时进程（通常是后台进程）打印出的参数为空或乱码。在这些情况下，命令名会用括号括起来打印。

`w` 实用程序不了解检测后台作业的新约定。它有时会找到后台作业而非正确的那个。
