  WHO(1)  

WHO(1)

FreeBSD General Commands Manual

WHO(1)

[名称](#__u540D___u79F0_)
=======================

`who` —

显示谁在系统上

[概要](#__u6982___u8981_)
=======================

`who` \[`-abHmqsTu`\] \[`am I`\] \[file\]

[描述](#__u63CF___u8FF0_)
=======================

`who` 实用程序显示有关当前登录用户的信息。 默认情况下，这包括登录名、tty 名称、登录日期和时间以及远程主机名（如果不是本地主机名）。

选项如下：

[`-a`](#a)

等效于 `-bTu`, 但输出不限于上次系统重新启动的时间和日期。

[`-b`](#b)

写上最后一次系统重启的时间和日期。

[`-H`](#H)

在输出上方写列标题。

[`-m`](#m)

仅显示有关连接到标准输入的终端的信息。

[`-q`](#q)

“Quick mode”: 在列中列出登录用户的名称和数量。 所有其他命令行选项都被忽略。

[`-s`](#s)

仅显示名称、行和时间字段。 这是默认设置。

[`-T`](#T)

指示每个用户是否正在接受消息。 写入以下字符之一：

[`+`](#+)

用户正在接受消息。

[`-`](#-)

用户不接受消息。

[`?`](#?)

发生错误。

[`-u`](#u)

以 hh:mm, ‘`.`’ 的形式以小时和分钟显示每个用户的空闲时间 如果用户空闲不到一分钟， “`old`” 如果用户空闲超过 24 小时。

[`am I`](#am_I)

相当于 `-m` 。

默认情况下， `who` 从文件 /var/run/utx.active 收集信息。 可以指定一个备用 file ，通常是 /var/log/utx.log （或 /var/log/utx.log.\[0-6\] 取决于站点策略，因为 utx.log 可能会变得非常大，并且每日版本可能会或 ac(8) 压缩后可能无法保留。 utx.log 文件包含自上次截断或创建 utx.log-
以来每次登录、注销、崩溃、关闭和日期更改的记录。

如果 /var/log/utx.log 被用作文件，则用户名可能为空或特殊字符“|”、“}”和“~”之一。 注销会产生一个没有任何用户名的输出行。 有关特殊字符的更多信息，请参阅 getutxent(3) 。

[环境](#__u73AF___u5883_)
=======================

`COLUMNS`, `LANG`, `LC_ALL` 和 `LC_TIME` 环境变量影响 `who` 的执行，如 environ(7) 中所述。

[文件](#__u6587___u4EF6_)
=======================

/var/run/utx.active

/var/log/utx.log

/var/log/utx.log.\[0-6\]

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `who` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示登录者的简要摘要：

$ who -q fernape root root # users = 3 

显示谁登录以及行和时间字段（不带标题）：

$ who -s fernape ttyv0 Aug 26 16:23 root ttyv1 Aug 26 16:23 root ttyv2 Aug 26 16:23 

显示有关连接到标准输入的终端的信息：

$ who am i fernape Aug 26 16:24 

显示上次系统重新启动的时间和日期，用户是否接受消息以及每个用户的空闲时间：

$ who -a - system boot Aug 26 16:23 . fernape - ttyv0 Aug 26 16:23 . root - ttyv1 Aug 26 16:23 . root - ttyv2 Aug 26 16:23 . 

与上面相同，但显示标题：

$ who -aH NAME S LINE TIME IDLE FROM - system boot Aug 26 16:23 . fernape - ttyv0 Aug 26 16:23 . root - ttyv1 Aug 26 16:23 00:01 root - ttyv2 Aug 26 16:23 00:01 

[参见](#__u53C2___u89C1_)
=======================

last(1), users(1), w(1), getutxent(3)

[标准](#__u6807___u51C6_)
=======================

`who` 实用程序符合 IEEE Std 1003.1-2001 (“POSIX.1”) 。

[历史](#__u5386___u53F2_)
=======================

`who` 命令出现在 Version 1 AT&T UNIX 中。

August 30, 2020

FreeBSD 13.1-RELEASE