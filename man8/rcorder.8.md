  RCORDER(8)  

RCORDER(8)

FreeBSD System Manager's Manual

RCORDER(8)

[名称](#__u540D___u79F0_)
=======================

`rcorder` —

打印相互依赖文件的依赖顺序

[概要](#__u6982___u8981_)
=======================

`rcorder` \[`-gp`\] \[`-k` keep\] \[`-s` skip\] file ...

[描述](#__u63CF___u8FF0_)
=======================

`rcorder` 实用程序旨在打印出一组相互依赖的文件的依赖顺序。 通常，它用于查找一组 shell 脚本的执行顺序，其中某些文件必须在其他文件之前执行。

传递给 `rcorder` 的每个文件都必须用特殊的行进行注释（看起来像 shell 的注释），这些行表明文件对序列中某些点的依赖关系，称为 “conditions” ，并且表明对于每个文件， “conditions” 可能会被该文件填充。

在每个文件中，必须出现一个包含一系列 ‘`REQUIRE`’, ‘`PROVIDE`’, ‘`BEFORE`’ 和 ‘`KEYWORD`’ 行的块。 线条的格式是刚性的。 每行必须以一个 ‘`#`’ 开头，后跟一个空格，然后是 ‘`PROVIDE:`’, ‘`REQUIRE:`’, ‘`BEFORE:`’ 或 ‘`KEYWORD:`’ 。 不允许有偏差。 然后每个依赖行后跟一系列条件，由空格分隔。 可能会出现多个 ‘`PROVIDE`’, ‘`REQUIRE`’, ‘`BEFORE`’ 和 ‘`KEYWORD`’ 行，但所有这些行必须按顺序出现，没有任何中间行，因为一旦到达不遵循格式的行，解析就会停止。

选项如下：

[`-g`](#g)

生成完整依赖图的 GraphViz (.dot)，而不是明文调用顺序列表。

[`-k`](#k) keep

将指定的关键字添加到 “keep list” 中。 如果给出任何 `-k` 选项，则仅列出包含匹配关键字的那些文件。 可以多次指定此选项。

[`-p`](#p)

生成适合并行启动的排序，将可以同时执行的文件放在同一行。

[`-s`](#s) skip

将指定的关键字添加到 “skip list” 中。 如果给出任何 `-s` 选项，则不列出包含匹配关键字的文件。 可以多次指定此选项。

下面是一个示例块：

\# REQUIRE: networking syslog # REQUIRE: usr # PROVIDE: dns nscd 

该块声明它出现的文件取决于 ‘`networking`’, ‘`syslog`’, 和 ‘`usr`’ 条件，并提供 ‘`dns`’ 和 ‘`nscd`’ 条件。

一个文件可能包含零个 ‘`PROVIDE`’ 行，在这种情况下它不提供条件，并且可能包含零个 ‘`REQUIRE`’ 行，在这种情况下它没有依赖关系。 在传递给 `rcorder` 的一组参数中必须至少有一个没有依赖关系的文件，以便它在依赖关系排序中找到起始位置。

[关键词](#__u5173___u952E___u8BCD_)
================================

有几个 _KEYWORDs_ 在使用：

**firstboot**, **nojail**, **nojailvnet**, **nostart**

由 rc(8) 使用。

**resume**

由 `/etc/rc.resume` 使用（参见 acpiconf(8))

**shutdown**

由 rc.shutdown(8) 使用。

[实例](#__u5B9E___u4F8B_)
=======================

从基础系统和 ports(7) 打印服务的依赖顺序：

$ rcorder /etc/rc.d/\* /usr/local/etc/rc.d/\* 

计算基本系统中指定 **shutdown** 关键字的服务数量，同时跳过带有 **firstboot** 和 **nojailvnet** 的服务：

$ rcorder -k nostart -s firstboot -s nojailvnet /etc/rc.d/\* | wc -l 3 

[诊断](#__u8BCA___u65AD_)
=======================

如果 `rcorder` 实用程序在处理文件列表时遇到错误，它可能会打印以下错误消息之一并以非零状态退出。

Requirement %s in file %s has no providers.

没有文件具有对应于另一个文件的 ‘`PROVIDE`’ 行中存在的条件的 ‘`REQUIRE`’ 行。

Circular dependency on provision %s in file %s.

一组文件具有在处理所述条件时检测到的循环依赖关系。 循环可视化遵循此消息。

Circular dependency on file %s.

一组文件具有循环依赖关系，在处理所述文件时检测到该循环依赖关系。

%s was seen in circular dependencies for %d times.

作为循环依赖循环一部分的每个节点都会报告此类遭遇的总数。 在与损坏的依赖项作斗争时，从具有最大计数器的文件开始。

[使用 GraphVIZ 进行诊断](#__u4F7F___u7528__GraphVIZ___u8FDB___u884C___u8BCA___u65AD_)
===============================================================================

直接依赖用实线绘制， ‘`BEFORE`’ 依赖用虚线绘制。 图表的每个节点代表 ‘`PROVIDE`’ 行中的一个项目。 如果有多个文件提供一个项目，则会显示用 basename(3) 缩短的文件名列表。 如果 ‘`PROVIDE`’ 项目与文件名不匹配，也会显示缩短的文件名。

检测到循环依赖关系的边缘和节点以粗体红色绘制。 如果文件在 ‘`REQUIRE`’ 或 ‘`BEFORE`’ 中有无法提供的项目，则此缺失的提供者和要求也将被绘制为红色粗体。

[参见](#__u53C2___u89C1_)
=======================

acpiconf(8), rc(8), rc.shutdown(8), service(8)

[历史](#__u5386___u53F2_)
=======================

`rcorder` 实用程序出现在 NetBSD 1.5 中。 `rcorder` 实用程序首次出现在 FreeBSD 5.0 中。

[作者](#__u4F5C___u8005_)
=======================

由 Perry E. Metzger <[perry@piermont.com](mailto:perry@piermont.com)\> 和 Matthew R. Green <[mrg@eterna.com.au](mailto:mrg@eterna.com.au)\> 撰写。

[缺陷](#__u7F3A___u9677_)
=======================

‘`REQUIRE`’ 关键字具有误导性：它没有描述在启动脚本之前必须运行哪些守护进程。 它描述了在依赖顺序中必须将哪些脚本放在它之前。 例如，如果您的脚本在 ‘`sshd`’ 上有一个 ‘`REQUIRE`’ ，这意味着该脚本必须按依赖顺序放置在 ‘`sshd`’ 脚本之后，而不一定需要启动或启用 `sshd` 。

September 8, 2020

FreeBSD 13.1-RELEASE