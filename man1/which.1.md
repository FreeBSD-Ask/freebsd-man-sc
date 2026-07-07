# which(1)

`which` — 在用户路径中定位程序文件

## 名称

`which`

## 概要

`which [-as] program ...`

## 描述

`which` 实用程序接收一组命令名，并在路径中搜索每个本应在这些命令实际被调用时执行的可执行文件。

可用选项如下：

**`-a`** 列出找到的所有可执行文件实例（而非仅列出每个的第一实例）。

**`-s`** 无输出，仅当所有可执行文件都找到时返回 0，部分未找到时返回 1。

某些 shell 可能提供与本实用程序相似或相同的内建 `which` 命令。请参阅 [builtin(1)](builtin.1.md) 手册页。

## 实例

定位 [ls(1)](ls.1.md) 和 [cp(1)](cp.1.md) 命令：

```sh
$ /usr/bin/which ls cp
/bin/ls
/bin/cp
```

与上相同，但指定 `PATH` 并显示所有出现：

```sh
$ PATH=/bin:/rescue /usr/bin/which -a ls cp
/bin/ls
/rescue/ls
/bin/cp
/rescue/cp
```

如果同一个可执行文件被找到多次，`which` 会显示重复项：

```sh
$ PATH=/bin:/bin /usr/bin/which -a ls
/bin/ls
/bin/ls
```

不显示输出。仅以适当的返回码退出：

```sh
$ /usr/bin/which -s ls cp
$ echo $?
0
$ /usr/bin/which -s fakecommand
$ echo $?
1
```

## 参见

[builtin(1)](builtin.1.md), [csh(1)](csh.1.md), [find(1)](find.1.md), [locate(1)](locate.1.md), [whereis(1)](whereis.1.md)

## 历史

`which` 命令首次出现于 FreeBSD 2.1。

## 作者

`which` 实用程序最初由 Perl 编写，由 Wolfram Schneider <wosch@FreeBSD.org> 贡献。当前版本的 `which` 由 Daniel Papasian <dpapasia@andrew.cmu.edu> 用 C 重写。
