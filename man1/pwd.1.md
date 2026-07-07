# pwd(1)

`pwd` — 返回工作目录名

## 名称

`pwd`

## 概要

`pwd [-L | -P]`

## 描述

`pwd` 实用程序将当前工作目录的绝对路径名写入标准输出。

某些 shell 可能提供与本实用程序相似或相同的内建 `pwd` 命令。请参阅 [builtin(1)](builtin.1.md) 手册页。

选项如下：

**`-L`** 显示逻辑当前工作目录。

**`-P`** 显示物理当前工作目录（解析所有符号链接）。

如果未指定选项，则假定使用 `-L` 选项。

## 环境变量

`pwd` 使用的环境变量：

**`PWD`** 逻辑当前工作目录。

## 退出状态

`pwd` 实用程序成功时退出码为 0，发生错误时大于 0。

## 实例

显示当前工作目录并解析符号链接：

```sh
$ /bin/pwd
/usr/src/sys/kern
```

显示逻辑当前目录，然后使用 file(1) 检查 **`/sys`** 目录：

```sh
$ /bin/pwd -L
/sys/kern
$ file /sys
/sys: symbolic link to usr/src/sys
```

## 参见

[builtin(1)](builtin.1.md), cd(1), [csh(1)](csh.1.md), [realpath(1)](realpath.1.md), [sh(1)](sh.1.md), getcwd(3)

## 标准

`pwd` 实用程序遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`pwd` 命令首次出现于 Version 5 AT&T UNIX。

## 缺陷

在 [csh(1)](csh.1.md) 中，`dirs` 命令总是更快，因为它内建于该 shell。然而，在当前目录或其包含目录在 shell 进入之后被移动的罕见情况下，它可能给出不同的答案。

除非 shell 导出了 `PWD` 环境变量，否则 `-L` 选项不起作用。
