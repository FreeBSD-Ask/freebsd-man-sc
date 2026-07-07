# rcorder(8)

`rcorder` — 打印相互依赖文件的依赖顺序

## 名称

`rcorder`

## 概要

`rcorder [-gp] [-k keep] [-s skip] file`

## 描述

`rcorder` 工具用于打印一组相互依赖文件的依赖顺序。通常用于为一组 shell 脚本查找执行序列，其中某些文件必须在其他文件之前执行。

传递给 `rcorder` 的每个文件必须用特殊行（对 shell 而言看起来像注释）标注，这些行指示文件对序列中某些点（称为“条件”）的依赖关系，并指示每个文件可期望由该文件满足哪些“条件”。

在每个文件中，必须出现一个包含一系列 `REQUIRE`、`PROVIDE`、`BEFORE` 和 `KEYWORD` 行的块。这些行的格式是严格的。每行必须以单个 `#` 开头，后跟一个空格，再后跟 `PROVIDE:`、`REQUIRE:`、`BEFORE:` 或 `KEYWORD:`。不允许有任何偏差。每个依赖行后跟一系列条件，以空白分隔。可以出现多个 `PROVIDE`、`REQUIRE`、`BEFORE` 和 `KEYWORD` 行，但所有此类行必须连续出现，因为一旦遇到不符合格式的行，解析就会停止。

选项如下：

**`-g`** 生成完整依赖图的 GraphViz（.dot）格式，而非纯文本调用顺序列表。

**`-k`** `keep` 将指定关键字添加到“保留列表”。如果给出了任何 `-k` 选项，则只列出包含匹配关键字的文件。此选项可多次指定。

**`-p`** 生成适合并行启动的顺序，将可同时执行的文件放在同一行。

**`-s`** `skip` 将指定关键字添加到“跳过列表”。如果给出了任何 `-s` 选项，则不列出包含匹配关键字的文件。此选项可多次指定。

以下是一个示例块：

```sh
# REQUIRE: networking syslog
# REQUIRE: usr
# PROVIDE: dns nscd
```

此块声明其所在的文件依赖于 `networking`、`syslog` 和 `usr` 条件，并提供 `dns` 和 `nscd` 条件。

一个文件可以包含零个 `PROVIDE` 行，此时它不提供任何条件；也可以包含零个 `REQUIRE` 行，此时它没有依赖关系。在传递给 `rcorder` 的参数集中，必须至少有一个没有依赖关系的文件，才能在依赖顺序中找到起始位置。

## 关键字

使用的 *KEYWORD* 有以下几种：

**firstboot, nojail, nojailvnet, nostart** 由 [rc(8)](rc.8.md) 使用。

**suspend, resume** 由 **/etc/rc.suspend** 和 **/etc/rc.resume** 使用（参见 acpiconf(8)）

**shutdown** 由 [rc.shutdown(8)](rc.shutdown.8.md) 使用。

## 实例

打印基本系统和 [ports(7)](../man7/ports.7.md) 中服务的依赖顺序：

```sh
$ rcorder /etc/rc.d/* /usr/local/etc/rc.d/*
```

计算基本系统中指定 **nostart** 关键字的服务数量，同时跳过带有 **firstboot** 和 **nojailvnet** 的服务：

```sh
$ rcorder -k nostart -s firstboot -s nojailvnet /etc/rc.d/*  | wc -l
       3
```

## 诊断

`rcorder` 工具在处理文件列表时遇到错误，可能会打印以下错误消息之一并以非零状态退出。

- Requirement %s in file %s has no providers.（文件 %s 中的需求 %s 没有提供者。）没有文件的 `PROVIDE` 行与另一个文件中 `REQUIRE` 行中存在的条件对应。

- Circular dependency on provision %s in file %s.（文件 %s 中的提供 %s 存在循环依赖。）一组文件在处理所述条件时检测到循环依赖。此消息后跟循环可视化。

- Circular dependency on file %s.（文件 %s 存在循环依赖。）一组文件在处理所述文件时检测到循环依赖。

- %s was seen in circular dependencies for %d times.（%s 在循环依赖中被发现 %d 次。）每个作为循环依赖循环一部分的节点报告此类遭遇的总数。处理损坏的依赖时，从计数器最大的文件开始。

## GraphViz 诊断

直接依赖以实线绘制，`BEFORE` 依赖以虚线绘制。图的每个节点代表 `PROVIDE` 行中的一项。如果有多个文件提供同一项，则显示以 basename(3) 缩短的文件名列表。如果 `PROVIDE` 项与文件名不匹配，也会显示缩短的文件名。

检测到循环依赖的边和节点以粗体红色绘制。如果文件在 `REQUIRE` 或 `BEFORE` 中有一项无法被提供，则此缺失的提供者和需求也会以粗体红色绘制。

## 参见

acpiconf(8), [rc(8)](rc.8.md), [rc.shutdown(8)](rc.shutdown.8.md), [service(8)](service.8.md)

## 历史

`rcorder` 工具出现于 NetBSD 1.5。`rcorder` 工具首次出现于 FreeBSD 5.0。

## 作者

由 Perry E. Metzger <perry@piermont.com> 和 Matthew R. Green <mrg@eterna.com.au> 编写。

## 缺陷

`REQUIRE` 关键字有误导性：它不描述脚本启动前必须运行哪些守护进程。它描述的是哪些脚本必须在依赖顺序中位于其之前。例如，如果你的脚本对 `sshd` 有 `REQUIRE`，意味着该脚本必须在依赖顺序中位于 `sshd` 脚本之后，而不一定要求 `sshd` 已启动或启用。
