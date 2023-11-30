  JEXEC(8)  

JEXEC(8)

FreeBSD System Manager's Manual

JEXEC(8)

[名称](#__u540D___u79F0_)
=======================

`jexec` —

在现有的监狱中执行命令

[概要](#__u6982___u8981_)
=======================

`jexec` \[`-l`\] \[`-u` username | `-U` username\] jail \[command ...\]

[描述](#__u63CF___u8FF0_)
=======================

`jexec` 实用程序在由其 jid 或名称标识的 jail 内执行 command 。 如果未指定 command ，则使用用户的 shell。

可以使用以下选项：

[`-l`](#l)

在干净的环境中执行。 除了 `HOME`, `SHELL`, `TERM`, `USER` 和用户登录类能力数据库中的任何内容之外，环境将被丢弃。

[`-u`](#u) username

command 应该运行的主机环境中的用户名。 这是默认设置。

[`-U`](#U) username

command 应该运行的来自被监禁环境的用户名。

[参见](#__u53C2___u89C1_)
=======================

jail\_attach(2), jail(8), jls(8)

[历史](#__u5386___u53F2_)
=======================

`jexec` 实用程序是在 FreeBSD 5.1 中添加的。

[缺陷](#__u7F3A___u9677_)
=======================

如果 jid 未识别监狱，则在监狱的查找和在监狱内执行命令之间可能存在竞争。 给一个 jid 有一个类似的竞赛，因为另一个进程可以在用户查找 jid 后停止监狱并启动另一个进程。

April 24, 2016

FreeBSD 13.1-RELEASE