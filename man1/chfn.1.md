  CHPASS(1)  

CHPASS(1)

FreeBSD General Commands Manual

CHPASS(1)

[名称](#__u540D___u79F0_)
=======================

`chpass`, `chfn`, `chsh`, `ypchpass`, `ypchfn`, `ypchsh` —

添加或更改用户数据库信息

[概要](#__u6982___u8981_)
=======================

`chpass` \[`-a` list\] \[`-e` expiretime\] \[`-p` encpass\] \[`-s` newshell\] \[user\] `ypchpass` \[`-loy`\] \[`-a` list\] \[`-d` domain\] \[`-e` expiretime\] \[`-h` host\] \[`-p` encpass\] \[`-s` newshell\] \[user\]

[描述](#__u63CF___u8FF0_)
=======================

`chpass` 实用程序允许编辑与 user 关联的用户数据库信息，默认情况下，与当前用户关联。

`chfn`, `chsh`, `ypchpass`, `ypchfn` 和 `ypchsh` 实用程序的行为与 `chpass` 相同。 （只有一个程序。）

信息被格式化并提供给编辑器进行更改。

仅显示允许用户更改的信息。

选项如下：

[`-a`](#a) list

超级用户可以直接提供用户数据库条目，格式由 passwd(5) 指定，作为参数。 此参数必须是所有用户数据库字段的冒号 (“:”) 分隔列表，尽管它们可能为空。

[`-e`](#e) expiretime

更改帐户过期时间。 此选项用于设置脚本的过期时间，就像在交互式编辑器中完成一样。

[`-p`](#p) encpass

超级用户可以直接提供加密的密码字段，以 crypt(3) 使用的格式作为参数。

[`-s`](#s) newshell

尝试将用户的 shell 更改为 newshell 。

可能的显示项目如下：

Login:

用户的登录名

Password:

用户的加密密码

Uid:

用户登录

Gid:

用户登录组

Class:

用户的一般分类

Change:

密码更改时间

Expire:

账户到期时间

Full Name:

用户的真实姓名

Office Location:

用户办公地点 (1)

Office Phone:

用户办公电话 (1)

Home Phone:

用户家庭电话 (1)

Other Information:

为用户 (1) 定义的任何本地参数

Home Directory:

用户的主目录

Shell:

用户的登录外壳

NOTE(1) -

在实际的 master.passwd 文件中，这些字段是嵌入在 FullName 字段中的逗号分隔字段。

login 字段是用于访问计算机帐户的用户名。

password 字段包含用户密码的加密形式。

uid 字段是与 login 字段关联的数字。 这两个字段在系统中（并且通常在一组系统中）应该是唯一的，因为它们控制文件访问。

虽然可以有多个具有相同登录名和/或相同用户 ID 的条目，但这样做通常是错误的。 处理这些文件的例程通常只会返回多个条目中的一个，并且该条目是随机选择的。

gid 字段是用户在登录时将被放置的组。 由于 BSD 支持多个组（参见 groups(1) ），这个字段目前没有什么特殊意义。 该字段可以填写数字或组名（请参阅 group(5) ）。

class 字段引用 /etc/login.conf 中的类描述，通常用于在用户登录时初始化用户的系统资源限制。

change 字段是必须更改密码的日期。

expire 字段是帐户到期的日期。

change 和 expire 字段都应以 “month day year” 的形式输入，其中 month 为月名（前三个字符即可）， day 为月日， year 为年。

五个字段可用于存储用户的 full name 、 office location 、 work 和 home telephone ，最后是 other information ，这些信息是一个逗号分隔的字符串，表示任何附加的 gecos 字段（通常用于特定于站点的用户信息）。 请注意， finger(1) 将在标题 Office: 下一起显示办公室位置和办公室电话。

用户的 home directory 是用户登录时所在的完整 UNIX 路径名。

shell 字段是用户喜欢的命令解释器。 如果 shell 字段为空，则假定为 Bourne shell， /bin/sh 。 当更改登录 shell 而不是超级用户时，用户可能不会从非标准 shell 更改或更改为非标准 shell。 非标准定义为在 /etc/shells 中找不到的 shell。

验证信息后， `chpass` 使用 pwd\_mkdb(8) 更新用户数据库。

[环境](#__u73AF___u5883_)
=======================

除非环境变量 `EDITOR` 设置为备用编辑器，否则将使用 vi(1) 编辑器。 当编辑器终止时，信息会被重新读取并用于更新用户数据库本身。 只有用户或超级用户可以编辑与用户相关的信息。

有关设置 `PW_SCAN_BIG_IDS` 环境变量的影响的说明，请参见 pwd\_mkdb(8) 。

[NIS 交互](#NIS___u4EA4___u4E92_)
===============================

`chpass` 实用程序也可以与 NIS 一起使用，但是有一些限制。 目前， `chpass` 只能通过 rpc.yppasswdd(8) 更改 NIS passwd 映射，这通常只允许更改用户的密码、shell 和 GECOS 字段。 除非由 NIS 主服务器上的超级用户调用，否则 `chpass` (以及类似的 passwd(1)) 不能使用 rpc.yppasswdd(8) 服务器更改其他用户信息或向 NIS passwd 映射添加新记录。 此外， rpc.yppasswdd(8) 需要密码验证才能进行任何更改。 唯一允许在不提供密码的情况下提交更改的用户是 NIS 主服务器上的超级用户；所有其他用户，包括在 NIS 客户端（和 NIS 从属服务器）上具有 root 权限的用户，都必须输入密码。 （NIS 主服务器上的超级用户被允许绕过这些限制，主要是为了方便：对 NIS 主服务器具有 root 访问权限的用户已经拥有更新 NIS 映射所需的权限，但手动编辑映射源文件可能很麻烦。

注意：这些例外仅适用于 NIS 主服务器是 FreeBSD 系统时）。

因此，除非另有说明，当 `chpass` 与 NIS 一起使用时，以下限制适用：

1.  _只有外壳和 GECOS 信息可以更改。_ 所有其他字段都受到限制，即使超级用户调用了 `chpass` 。 虽然可以添加对更改其他字段的支持，但这会导致与其他支持 NIS 的系统的兼容性问题。 即使超级用户可以在编辑条目时为其他字段提供数据，额外的信息（除了密码 — 见下文）将被静默丢弃。
    
    例外：NIS 主服务器上的超级用户被允许更改任何字段。
    
2.  _需要密码验证。_ `chpass` 实用程序将在进行任何更改之前提示用户输入 NIS 密码。 如果密码无效，所有更改都将被丢弃。
    
    例外：NIS 主服务器上的超级用户可以在不提供密码的情况下提交更改。 （超级用户可以选择使用 `-o` 标志关闭此功能，如下所述。）
    
3.  _不鼓励向本地密码数据库添加新记录。_ `chpass` 实用程序将允许管理员在启用 NIS 时将新记录添加到本地密码数据库，但这可能会导致一些混乱，因为新记录附加到主密码文件的末尾，通常在特殊的 NIS '+ 之后' 条目。 NIS 运行时，管理员应使用 vipw(8) 修改本地密码文件。
    
    允许 NIS 主服务器上的超级用户向 NIS 密码映射添加新记录，前提是 rpc.yppasswdd(8) 服务器已使用 `-a` 标志启动以允许添加（默认情况下拒绝它们）。 `chpass` 实用程序默认尝试更新本地密码数据库；要改为更新 NIS 映射，请使用 `-y` 标志调用 chpass。
    
4.  _不允许更改密码。_ 用户应该使用 passwd(1) 或 yppasswd(1) 来更改他们的 NIS 密码。 超级用户可以指定新密码（即使 “Password:” 字段未显示在编辑器模板中，超级用户也可以手动添加），但即使是超级用户也必须提供用户的原始密码，否则 rpc.yppasswdd(8) 将拒绝更新 NIS 映射。
    
    例外：NIS 主服务器上的超级用户可以使用 `chpass` 更改用户的 NIS 密码。
    

当使用 NIS 支持编译 `chpass` 时，还有一些额外的选项标志可用：

[`-d`](#d) domain

指定特定的 NIS 域。 `chpass` 实用程序默认使用由 domainname(1) 实用程序设置的系统域名。 `-d` 选项可用于覆盖默认值，或在未设置系统域名时指定域。

[`-h`](#h) host

指定要查询的 NIS 服务器的名称或地址。 通常， `chpass` 将与在 master.passwd 或 passwd 映射中指定的 NIS 主控主机通信。 在尚未配置为 NIS 客户端的主机上，除非用户提供服务器的主机名，否则程序无法确定此信息。 请注意，指定的主机名不必是 NIS 主服务器的主机名；给定 NIS 域中的任何服务器（主服务器或从服务器）的名称都可以。

使用 `-d` 选项时，主机名默认为 “localhost” 。 `-h` 选项可以与 `-d` 选项一起使用，在这种情况下，用户指定的主机名将覆盖默认值。

[`-l`](#l)

如果用户同时存在于本地和 NIS 数据库中，则强制 `chpass` 修改用户密码信息的本地副本。

[`-o`](#o)

与 rpc.yppasswdd(8) (“old-mode”) 通信时强制使用基于 RPC 的更新。 当 NIS 主服务器上的超级用户调用时， `chpass` 允许使用专用的、非基于 RPC 的机制（在本例中为 UNIX 域套接字）对 NIS 密码映射进行无限制的更改。 `-o` 标志可用于强制 `chpass` 使用标准更新机制。 此选项主要用于测试目的。

[`-y`](#y)

[`-l`](#l_2) 的相反效果。 这个标志在很大程度上是多余的，因为如果启用了 NIS， `chpass` 默认会在 NIS 条目上运行。

[文件](#__u6587___u4EF6_)
=======================

/etc/master.passwd

用户数据库

/etc/passwd

版本 7 格式的密码文件

/etc/chpass.XXXXXX

密码文件的临时副本

/etc/shells

批准的 shell 列表

[实例](#__u5B9E___u4F8B_)
=======================

将当前用户的 shell 更改为 ‘`/usr/local/bin/zsh`’:

chsh -s /usr/local/bin/zsh 

[参见](#__u53C2___u89C1_)
=======================

finger(1), login(1), passwd(1), getusershell(3), login.conf(5), passwd(5), pw(8), pwd\_mkdb(8), vipw(8) Robert Morris and Ken Thompson, UNIX Password security.

[历史](#__u5386___u53F2_)
=======================

`chpass` 实用程序出现在 4.3BSD-Reno 中。

[缺陷](#__u7F3A___u9677_)
=======================

用户信息应该（并且最终将）存储在其他地方。

November 17, 2020

FreeBSD 13.1-RELEASE