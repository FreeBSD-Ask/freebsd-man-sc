  ADDUSER(8)  

ADDUSER(8)

FreeBSD System Manager's Manual

ADDUSER(8)

[名称](#__u540D___u79F0_)
=======================

`adduser` —

添加新用户的命令

[概要](#__u6982___u8981_)
=======================

`adduser` \[`-CDENShq`\] \[`-G` groups\] \[`-L` login\_class\] \[`-M` mode\] \[`-d` partition\] \[`-f` file\] \[`-g` login\_group\] \[`-k` dotdir\] \[`-m` message\_file\] \[`-s` shell\] \[`-u` uid\_start\] \[`-w` type\]

[描述](#__u63CF___u8FF0_)
=======================

`adduser` 实用程序是一个 shell 脚本，围绕 pw(8) 命令实现，用于添加新用户。 它创建密码/组条目、主目录、复制点文件并向新用户发送欢迎消息。 它支持两种操作模式。 它可以在命令行交互使用，一次添加一个用户，也可以直接从文件中获取新用户列表并以批处理模式操作，而无需任何用户交互。

[限制](#__u9650___u5236_)
=======================

username

登录名。 用户名仅限于 pw(8) 将接受的任何内容。 通常这意味着它可能只包含小写字符或数字，但不能以 ‘`-`’ 字符开头。 最大长度为 16 个字符。 这个限制的原因是历史性的。 鉴于人们传统上出于审美原因想要打破这个限制，在 UNIX 中打破这样一个基本的基本参数从来都不是很重要。 您可以更改 `<utmp.h>` 中的 `UT_NAMESIZE` 并重新编译世界；人们已经做到了这一点并且它有效，但是任何预编译程序或假定名称限制为 8 个字符的源（例如 NIS）都会出现问题。 NIS 协议要求使用 8 个字符的用户名。 如果您需要更长的电子邮件地址登录名，您可以在 /etc/mail/aliases 中定义一个别名。

full name

这通常称为 gecos 字段，通常包含用户的全名。 此外，它可能包含一个逗号分隔的值列表，例如办公室号码和工作电话和家庭电话。 如果名称包含 & 符号，则在其他程序显示时将替换为大写的登录名。 ‘`:`’ 字符是不允许的。

shell

除非提供了 `-S` 参数，否则只允许来自 shell 数据库 (/etc/shells) 的有效 shell。 此外，可以提供 shell 的基本名称或完整路径。

UID

自动生成或您的选择。 它必须小于 32000。

GID/login group

自动生成或您的选择。 它必须小于 32000。

password

您可以选择空密码、禁用密码、使用随机生成的密码或指定您自己的明文密码，这些密码在存储到用户数据库之前将被加密。

[UNIQUE GROUPS](#UNIQUE_GROUPS)
===============================

也许你错过了这个与大多数其他方案不同的方案 _can_ 做的事情。 对于他们自己组中的每个用户，他们可以安全地使用 002 而不是通常的 022 的 umask 运行，并在他们的主目录中创建文件，而不必担心其他人能够更改它们。

对于共享区域，您创建一个单独的 UID/GID，将应该能够访问该区域的每个人放置到该新组中。

这种 UID/GID 管理模型比将用户分组并在共享区域工作时不得不使用 umask 提供更大的灵活性。

我已经使用这个模型将近 10 年了，发现它适用于大多数情况，并且从未妨碍我。（罗德·格兰姆斯）

[配置](#__u914D___u7F6E_)
=======================

`adduser` 实用程序从 /etc/adduser.conf 读取其配置信息。 如果此文件不存在，它将使用预定义的默认值。 虽然可以手动编辑此文件，但更安全的选择是使用 `-C` 命令行参数。 使用此参数， `adduser` 将启动交互式输入，将其提示的答案保存在 /etc/adduser.conf 中，并在不修改用户数据库的情况下立即退出。 在命令行上指定的选项将优先于保存在此文件中的任何值。

[选项](#__u9009___u9879_)
=======================

[`-C`](#C)

创建新的配置文件并退出。 此选项与 `-f` 选项互斥。

[`-d`](#d) partition

家庭分区。 默认分区，所有用户目录都将位于该分区下。 /nonexistent 分区被认为是特殊的。 `adduser` 脚本不会使用该名称创建和填充主目录。 否则，默认情况下它会尝试创建主目录。

[`-D`](#D)

不要尝试创建主目录。

[`-E`](#E)

禁用该帐户。 此选项将通过在密码字段前添加字符串 “`*LOCKED*`” 来锁定帐户。 超级用户可以使用 pw(8) 命令解锁该帐户：

`pw` `unlock` \[name | uid\]

[`-f`](#f) file

获取要从 file 创建的帐户列表。 如果 file 为 “`-`”, 则从标准输入中获取列表。 如果指定了此选项， `adduser` 将以批处理模式运行，并且不会搜索任何用户输入。 如果在处理帐户时遇到错误，它将向标准错误写入消息并移至下一个帐户。 输入文件的格式如下所述。

[`-g`](#g) login\_group

通常，如果没有指定登录组，则假定它与用户名相同。 此选项使 login\_group 成为默认值。

[`-G`](#G) groups

其他组的空格分隔列表。 此选项允许用户指定要添加用户的其他组。 除了登录组之外，用户还是这些组的成员。

[`-h`](#h)

打印选项摘要并退出。

[`-k`](#k) directory

将文件从 directory 复制到新用户的主目录； dot.foo 将重命名为 .foo 。

[`-L`](#L) login\_class

设置默认登录类。

[`-m`](#m) file

从 file 中向新用户发送欢迎消息。 为 `no` 指定值 file 会导致不会向新用户发送消息。 请注意，消息文件可以引用 `adduser` 脚本的内部变量。

[`-M`](#M) mode

创建权限设置为 mode 的主目录。

[`-N`](#N)

不要读取默认配置文件。

[`-q`](#q)

最少的用户反馈。 特别是，随机密码不会回显到标准输出。

[`-s`](#s) shell

新用户的默认 shell 。 shell 参数可以是 shell 的基本名称或完整路径。 除非提供了 `-S` 参数，否则 shell 必须存在于 /etc/shells 中或者是特殊的 shell _nologin_ 才能被视为有效的 shell。

[`-S`](#S)

将不检查指定 shell 的存在或有效性。

[`-u`](#u) uid

从 uid 开始使用 UID。

[`-w`](#w) type

密码类型。 `adduser` 实用程序允许用户指定要创建的密码类型。 type 参数可能具有以下值之一：

[`no`](#no)

禁用密码。 密码字段将包含单个 ‘`*`’ 字符，而不是加密字符串。 在超级用户手动启用密码之前，用户可能无法登录。

[`none`](#none)

使用空字符串作为密码。

[`yes`](#yes)

使用用户提供的字符串作为密码。 在交互模式下，将提示用户输入密码。 在批处理模式下，假定行中的最后（第 10 个）字段是密码。

[`random`](#random)

生成一个随机字符串并将其用作密码。 密码将回显到标准输出。 此外，它还可以包含在 randompass 变量的消息文件中。

[格式](#__u683C___u5F0F_)
=======================

使用 `-f` 选项时，帐户信息必须以特定格式存储。 所有空行或以 ‘`#`’ 开头的行都将被忽略。 所有其他行必须包含十个冒号 (‘`:`’) 分隔的字段，如下所述。 命令行选项不优先于字段中的值。 只有密码字段可以包含一个 ‘`:`’ 字符作为字符串的一部分。

name:uid:gid:class:change:expire:gecos:home\_dir:shell:password

name

登录名。此字段不能为空。

uid

数字登录用户 ID。 如果该字段留空，它将自动生成。

gid

数字主要组 ID。 如果此字段留空，将创建一个与用户名同名的组，并使用其 GID 代替。

class

登录类。此字段可留空。

change

密码老化。 此字段表示帐户的密码更改日期。 该字段的格式与 pw(8) 的 `-p` 参数的格式相同。 它可能是 dd\-mmm\-yy\[yy\], ，其中 dd 表示日期， mmm 表示月份，数字或字母格式： “`10`” 或 “`Oct`”, yy\[yy\] 是四位或两位数的年份. 要表示相对于当前日期的时间，格式为： +n\[mhdwoy\], 其中 n 表示一个数字，后跟必须更改密码的分钟、小时、天、周、月或年。 此字段可以留空以将其关闭。

expire

帐户到期。 此字段表示帐户的到期日期。 在指定日期之后，该帐户可能无法使用。 该字段的格式与密码老化的格式相同。 此字段可以留空以将其关闭。

gecos

关于用户的全名和其他额外信息。

home\_dir

主目录。 如果该字段留空，它将通过将用户名附加到主分区来自动创建。 /nonexistent 主目录被认为是特殊的，并且被理解为意味着不会为用户创建主目录。

shell

登录外壳。 此字段应包含有效登录 shell 的基本名称或完整路径。

password

用户密码。 该字段应包含一个明文字符串，在放入用户数据库之前将对其进行加密。 如果密码类型为 `yes` 且此字段为空，则假定该帐户的密码为空。 如果密码类型为 `random` 且该字段 _not_ 为空，则其内容将作为密码。 如果 `-w` 选项与 `no` 或 `none` 参数一起使用，则该字段将被忽略。 请注意不要以结束的 ‘`:`’ 终止此字段，因为它将被视为密码的一部分。

[文件](#__u6587___u4EF6_)
=======================

/etc/master.passwd

用户数据库

/etc/group

组数据库

/etc/shells

shell 数据库

/etc/login.conf

登录类数据库

/etc/adduser.conf

`adduser` 的配置文件

/etc/adduser.message

`adduser` 的消息文件

/usr/share/skel

骨架登录目录

/var/log/adduser

`adduser` 的日志文件

[参见](#__u53C2___u89C1_)
=======================

chpass(1), passwd(1), adduser.conf(5), aliases(5), group(5), login.conf(5), passwd(5), shells(5), pw(8), pwd\_mkdb(8), rmuser(8), vipw(8), yp(8)

[历史](#__u5386___u53F2_)
=======================

`adduser` 命令出现在 FreeBSD 2.1 中。

[作者](#__u4F5C___u8005_)
=======================

本手册页和 Perl 的原始脚本由 Wolfram Schneider <[wosch@FreeBSD.org](mailto:wosch@FreeBSD.org)\> 编写。 替换脚本编写为带有一些增强功能的 Bourne shell 脚本，以及随附的手册页修改由 Mike Makonnen <[mtm@identd.net](mailto:mtm@identd.net)\> 完成。

[缺陷](#__u7F3A___u9677_)
=======================

为了使 `adduser` 在发送给新用户的消息中正确扩展 $username 和 $randompass 等变量，它必须让 shell 评估消息文件的每一行。 这意味着 shell 命令也可以嵌入到消息文件中。 `adduser` 实用程序试图通过拒绝评估该文件（如果该文件不是仅由 root 用户拥有和可写）来降低攻击者使用此功能的可能性。

此外，shell 特殊字符和运算符在消息文件中使用时必须进行转义。 此外，目前只能在批处理模式下或在 /etc/adduser.conf 中指定密码时效和帐户到期时间。 用户也应该能够将它们设置为交互模式。

September 15, 2012

FreeBSD 13.1-RELEASE