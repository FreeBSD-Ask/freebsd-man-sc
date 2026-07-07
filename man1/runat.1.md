# runat(1)

`runat` — 在命名属性目录上运行 shell 命令

## 名称

`runat`

## 概要

`runat [file] [shell command]`

## 描述

`runat` 实用程序在 `file` 参数的命名属性目录上运行 shell 命令。它执行 fchdir(2) 系统调用，将当前工作目录更改为 `file` 参数的命名属性目录，然后通过 [sh(1)](sh.1.md) 执行 shell 命令。

如果 `file` 没有命名属性目录，将创建一个空目录。如果应用程序需要确定 `file` 是否存在命名属性，可以使用 [pathconf(2)](../sys/pathconf.2.md) 配合名称 `_PC_HAS_NAMEDATTR`。这不会在 `file` 不存在命名属性目录时创建空的命名属性目录。

## 实例

对于一个名为“myfile”的 `file`：

```sh
$ runat myfile ls -l			# 列出 myfile 的属性
$ runat myfile cp /etc/hosts attrhosts	# 创建 attrhosts
$ runat myfile cat attrhosts		# 显示 attrhosts 的内容
```

## 参见

[sh(1)](sh.1.md), fchdir(2), [pathconf(2)](../sys/pathconf.2.md), [open(2)](../sys/open.2.md), [named_attribute(7)](../man7/named_attribute.7.md)

## 历史

`runat` 实用程序首次出现在 FreeBSD 15.0 中。
