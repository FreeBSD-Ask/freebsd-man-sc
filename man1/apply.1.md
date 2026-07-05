# apply.1

`apply` — 对一组参数应用命令

## 名称

`apply`

## 概要

`apply [-a c] [-d] [-#] command argument ...`

## 描述

`apply` 实用程序依次对每个参数 `argument` 执行指定的 `command`。

`command` 中形如“`%d`”的字符序列（其中“`d`”为 1 到 9 的数字）会被第 d 个后续未使用的 `argument` 替换。此时，每次执行 `command` 时会丢弃与最大数字对应数量的参数。

选项如下：

**`-`** `#` 通常参数是逐个取用的；可选数字 `#` 指定传递给 `command` 的参数数量。如果该数字为零，`command` 不带参数运行，每个 `argument` 运行一次。如果 `command` 中出现“`%d`”序列，则忽略 `-#` 选项。

**`-a`** `c` 可使用 `-a` 选项更改“`%`”作为特殊字符的用法。

**`-d`** 显示本应执行的命令，但实际并不执行。

## 环境变量

以下环境变量影响 `apply` 的执行：

**`SHELL`** 要使用的 shell 的路径名。如果未定义此变量，则使用 POSIX shell。

## 文件

**`/bin/sh`** 默认 shell

## 实例

**`apply echo *`** 类似于 [ls(1)](ls.1.md)；

**`apply -2 cmp a1 b1 a2 b2 a3 b3`** 将 `a` 文件与 `b` 文件进行比较；

**`apply -0 who 1 2 3 4 5`** 运行 [who(1)](who.1.md) 5 次；

**`apply 'ln %1 /usr/joe' *`** 将当前目录中的所有文件链接到目录 **`/usr/joe`**。

## 历史

`apply` 命令首次出现于 4.2BSD。

## 作者

Rob Pike

## 缺陷

`command` 中的 shell 元字符可能产生奇异的效果；最好将复杂命令用单引号（''）括起来。

`apply` 实用程序无法识别多字节字符。
