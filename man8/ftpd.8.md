  FTPD(8)  

FTPD(8)

FreeBSD System Manager's Manual

FTPD(8)

[名称](#__u540D___u79F0_)
=======================

`ftpd` —

Internet 文件传输协议服务器

[概要](#__u6982___u8981_)
=======================

`ftpd` \[`-468ABDdEhMmOoRrSUvW`\] \[`-l` \[`-l`\]\] \[`-a` address\] \[`-P` port\] \[`-p` file\] \[`-T` maxtimeout\] \[`-t` timeout\] \[`-u` umask\]

[描述](#__u63CF___u8FF0_)
=======================

`ftpd` 实用程序是 Internet 文件传输协议服务器进程。 服务器使用 TCP 协议并在使用 `-P` 选项或 “ftp” 服务规范中指定的端口进行侦听；见 services(5) 。

可用选项：

[`-4`](#4)

指定 `-D` 时，通过 `AF_INET` 套接字接受连接。

[`-6`](#6)

指定 `-D` 时，通过 `AF_INET6` 套接字接受连接。

[`-8`](#8)

启用透明 UTF-8 模式。 符合 RFC 2640 的客户端将被告知服务器使用的字符编码是 UTF-8，这是该选项的唯一效果。

此选项不启用服务器文件名的任何编码转换；相反，它意味着服务器上的文件名是用 UTF-8 编码的。 对于通过 FTP 上传的文件，符合 RFC 2640 的客户端有责任将其名称从客户端的本地编码转换为 UTF-8。 FTP 命令名称和自己的 `ftpd` 消息始终以 ASCII 编码，它是 UTF-8 的子集。 因此根本不需要服务器端转换。

[`-A`](#A)

只允许匿名 ftp 访问。

[`-a`](#a)

指定 `-D` 时，仅接受指定 address 上的连接。

[`-B`](#B)

设置此选项后， `ftpd` 将身份验证成功和失败消息发送到 blacklistd(8) 守护进程。 如果未指定此选项，则不会尝试与 blacklistd(8) 守护进程通信。

[`-D`](#D)

设置此选项后， `ftpd` 将分离并成为守护进程，接受 FTP 端口上的连接并派生子进程来处理它们。 这比从 inetd(8) 启动 `ftpd` 的开销要低，因此在繁忙的服务器上减少负载很有用。

[`-d`](#d)

使用 `LOG_FTP` 将调试信息写入 syslog。

[`-E`](#E)

禁用 EPSV 命令。 这对于旧防火墙后面的服务器很有用。

[`-h`](#h)

禁用在服务器消息中打印特定于主机的信息，例如服务器软件版本或主机名。

[`-l`](#l)

每个成功和失败的 ftp(1) 会话都使用带有 `LOG_FTP` 功能的 syslog 进行记录。 如果此选项指定了两次，则检索 (get)、存储 (put)、附加、删除、制作目录、删除目录和重命名操作及其文件名参数也会被记录。 默认情况下， syslogd(8) 将这些记录到 /var/log/xferlog 。

[`-M`](#M)

防止匿名用户创建目录。

[`-m`](#m)

如果文件系统权限允许，则允许匿名用户覆盖或修改现有文件。 默认情况下，匿名用户无法修改现有文件；特别是，要上传的文件将以唯一的名称创建。

[`-O`](#O)

只为匿名用户将服务器置于只写模式。 RETR 对匿名用户禁用，防止匿名下载。 如果还指定了 `-o` ，这将无效。

[`-o`](#o)

将服务器置于只写模式。 RETR 被禁用，阻止下载。

[`-P`](#P)

当指定 `-D` 时，在指定为数值或服务名称的 port 接受连接，而不是在默认的 “ftp” 端口。

[`-p`](#p)

当指定 `-D` 时，将守护进程的进程 ID 写入 file 而不是默认的 pid 文件 /var/run/ftpd.pid 。

[`-R`](#R)

设置此选项后， `ftpd` 将恢复有关对用户操作的安全检查和对 PORT 请求的限制的历史行为。 目前， `ftpd` 将只接受定向到远程用户主机上非特权端口的 PORT 命令（这违反了 FTP 协议规范，但关闭了一些安全漏洞）。

[`-r`](#r)

将服务器置于只读模式。 所有可能修改本地文件系统的命令都被禁用。

[`-S`](#S)

设置此选项后，当此文件存在时， `ftpd` 将所有匿名文件下载记录到文件 /var/log/ftpd 中。

[`-T`](#T)

客户端也可以请求不同的超时时间；可以使用 `-T` 选项将允许的最大时间段设置为 timeout 秒数。 默认限制为 2 小时。

[`-t`](#t)

不活动超时时间设置为 timeout 秒（默认为 15 分钟）。

[`-U`](#U)

此选项指示 ftpd 使用 `IP_PORTRANGE_DEFAULT` 范围内的数据端口，而不是 `IP_PORTRANGE_HIGH` 范围内的数据端口。 这样的更改可能对某些特定的防火墙配置有用；有关更多信息，请参见 ip(4) 。

请注意，选项在 FreeBSD 5.0 及更高版本中是一个虚拟空操作；默认情况下，两个端口范围相同。

[`-u`](#u)

默认文件创建模式掩码设置为 umask ，预计为八进制数值。 有关详细信息，请参阅 umask(2) 。 这个选项可能会被 login.conf(5) 覆盖。

[`-v`](#v)

[`-d`](#d_2) 的同义词。

[`-W`](#W)

不要将 FTP 会话记录到用户记帐数据库。

文件 /var/run/nologin 可用于禁用 ftp 访问。 如果文件存在， `ftpd` 将显示它并退出。 如果文件 /etc/ftpwelcome 存在， `ftpd` 在发出 “ready” 消息之前打印它。 如果文件 /etc/ftpmotd 存在， `ftpd` 会在成功登录后打印它。 请注意，使用的 motd 文件是与登录环境相关的文件。 在匿名用户的情况下，这意味着 ~ftp/etc 中的那个。

ftp 服务器目前支持以下 ftp 请求。 请求的大小写被忽略。 如果指定了 `-r` ，则禁用标记为 \[RW\] 的请求。

**请求**

**描述**

ABOR

中止上一个命令

ACCT

指定帐户（忽略）

ALLO

分配存储（空）

APPE

附加到文件 \[RW\]

CDUP

更改为当前工作目录的父级

CWD

更改工作目录

DELE

删除文件 \[RW\]

EPRT

指定数据连接端口，多协议

EPSV

为服务器到服务器传输做准备，多协议

FEAT

提供有关服务器扩展功能的信息

HELP

提供帮助信息

LIST

列出目录中的文件（“ls -lgA”）

LPRT

指定数据连接端口，多协议

LPSV

为服务器到服务器的传输做准备，多协议

MDTM

显示文件的最后修改时间

MODE

指定数据传输 _模式_

NLST

给出目录中文件的名称列表

NOOP

什么都不做

PASS

指定密码

PASV

为服务器到服务器的传输做准备

PORT

指定数据连接端口

PWD

打印当前工作目录

QUIT

终止会话

REST

重启不完整传输

RETR

检索文件

RMD

删除目录 \[RW\]

RNFR

指定 rename-from 文件名 \[RW\]

RNTO

指定重命名为文件名 \[RW\]

SITE

非标准命令（见下一节）

SIZE

返回文件大小

STAT

服务器返回状态

STOR

存储文件 \[RW\]

STOU

存储具有唯一名称的文件 \[RW\]

STRU

指定数据传输 _结构_

SYST

显示服务器系统的操作系统类型

TYPE

指定数据传输 _类型_

USER

指定用户名

XCUP

更改为当前工作目录的父级（已弃用）

XCWD

更改工作目录（已弃用）

XMKD

创建目录（已弃用）\[RW\]

XPWD

打印当前工作目录（已弃用）

XRMD

删除目录（已弃用）\[RW\]

SITE 请求支持以下非标准或 UNIX 特定命令。

**请求**

**描述**

UMASK

更改 umask，例如 \`\`SITE UMASK 002''

IDLE

设置空闲计时器，例如 \`\`SITE IDLE 60''

CHMOD

更改文件\[RW\]的模式，例如 \`\`SITE CHMOD 755 filename''

MD5

报告文件 MD5 校验和，例如 \`\`SITE MD5 filename''

HELP

提供帮助信息

注意：在匿名登录的情况下禁用 SITE 请求。

Internet RFC 959 中指定的其余 ftp 请求被识别，但未实现。 MDTM 和 SIZE 未在 RFC 959 中指定，但将出现在下一个更新的 FTP RFC 中。 为避免可能的拒绝服务攻击，如果当前传输类型为 ASCII，则针对大于 10240 字节的文件的 SIZE 请求将被拒绝。

如 Internet RFC 959 中所述，仅当 ABOR 命令前面有 Telnet "Interrupt Process" （IP）信号和命令 Telnet 流中的 Telnet "Synch" 信号时，ftp 服务器才会中止活动文件传输。 如果在数据传输过程中收到 STAT 命令，前面有 Telnet IP 和同步，将返回传输状态。

`ftpd` 实用程序根据 csh(1) 使用的 “globbing” 约定解释文件名。 这允许用户使用元字符 “`*?[]{}~`” 。

`ftpd` 实用程序根据六个规则对用户进行身份验证。

1.  登录名必须在密码数据库中，并且不能有空密码。 在这种情况下，客户端必须在执行任何文件操作之前提供密码。 如果用户有 OPIE 密钥，则成功的 USER 命令的响应将包括 OPIE 质询。 客户端可以选择使用 PASS 命令进行响应，给出标准密码或 OPIE 一次性密码。 服务器将自动确定已提供哪种类型的密码并尝试进行相应的身份验证。 有关 OPIE 身份验证的更多信息，请参阅 opie(4) 。
2.  登录名不得出现在文件 /etc/ftpusers 中。
3.  登录名不能是文件 /etc/ftpusers 中指定的组的成员。 此文件中解释为组名的条目以 "at" ‘`@`’ 符号为前缀。
4.  用户必须有一个由 getusershell(3) 返回的标准 shell。
5.  如果用户名出现在文件 /etc/ftpchroot 中，或者用户是该文件中具有组条目的组的成员，即以 ‘`@`’ 为前缀的组，则会话的根将更改为指定的目录 chroot(2) 将这个文件或用户的登录目录作为 “anonymous” 或 “ftp” 帐户（见下一项）。有关此文件格式的详细说明，请参见 ftpchroot(5) 。 此功能也可以通过在 login.conf(5) 中启用布尔 "ftp-chroot" 功能来触发。 但是，用户仍必须提供密码。 此功能旨在作为完全匿名帐户和完全特权帐户之间的折衷方案。 该帐户还应设置为匿名帐户。
6.  如果用户名为 “anonymous” 或 “ftp” ，则密码文件中必须存在匿名 ftp 帐户（用户 “ftp” ）。 在这种情况下，用户可以通过指定任何密码来登录（按照惯例，用户的电子邮件地址应该用作密码）。 当设置了 `-S` 选项时，所有的传输也会被记录下来。

在最后一种情况下， `ftpd` 采取了特殊措施来限制客户端的访问权限。 服务器对 “ftp” 用户的主目录执行 chroot(2) 。 作为一种特殊情况，如果 “ftp” 用户的主目录路径名包含 /./ 分隔符， `ftpd` 使用其左侧作为要执行 chroot(2) 的目录名称，并使用其右侧更改当前目录到之后。 这种情况的典型示例是 /usr/local/ftp/./pub 。 为了不破坏系统安全，建议按照以下规则小心构建 “ftp” 子树：

~ftp

使主目录归 “root” 所有，任何人都不可写。

~ftp/etc

使该目录归 “root” 所有，任何人都不可写（模式 555）。 必须存在文件 pwd.db（请参阅 passwd(5)) 和 group(5) ， ls(1) 命令才能生成所有者名称而不是数字。 passwd(5) 中的密码字段未使用，并且不应包含真实密码。 ftpmotd 文件（如果存在）将在成功登录后打印。 这些文件应该是模式 444。

~ftp/pub

该目录及其下的子目录应归负责在其中放置文件的用户和组所有，并且只能由他们写入（模式 755 或 775）。 它们 _not_ 应由 “ftp” 或其组拥有或可写，否则来宾用户可能会用不需要的文件填充驱动器。

如果系统有多个 IP 地址， `ftpd` 支持虚拟主机的概念，它提供了定义多个匿名 ftp 区域的能力，每个区域分配给不同的 Internet 地址。 文件 /etc/ftphosts 包含与每个虚拟主机有关的信息。 每个主机都在其自己的行上定义，其中包含许多由空格分隔的字段：

hostname

包含虚拟主机的主机名或 IP 地址。

user

包含系统密码文件中的用户记录。 与普通匿名 ftp 一样，该用户的访问 uid、gid 和组成员身份决定了对匿名 ftp 区域的文件访问。 匿名 ftp 区域（任何用户在登录时都会被 chroot）由为帐户定义的主目录决定。 任何 ftp 帐户的用户 id 和组可能与标准 ftp 用户相同。

statfile

记录所有文件传输的文件，默认为 /var/log/ftpd 。

welcome

该文件是在服务器就绪提示之前显示的欢迎消息。 它默认为 /etc/ftpwelcome 。

motd

该文件在用户登录后显示。 它默认为 /etc/ftpmotd 。

以“#”开头的行被忽略，可用于包含注释。

为主 IP 地址或主机名定义虚拟主机会更改 ftp 登录到该地址的默认值。

与任何匿名登录配置一样，必须对设置和维护给予应有的注意，以防止出现与安全相关的问题。

`ftpd` 实用程序对处理列出文件的远程请求具有内部支持，并且不会在 chrooted 或非 chrooted 环境中执行 /bin/ls 。 ~/bin/ls 可执行文件不需要放在 chrooted 树中，也不需要存在 ~/bin 目录。

[文件](#__u6587___u4EF6_)
=======================

/etc/ftpusers

不受欢迎/受限制的用户列表。

/etc/ftpchroot

应该被 chroot 的普通用户列表。

/etc/ftphosts

虚拟主机配置文件

/etc/ftpwelcome

欢迎通知。

/etc/ftpmotd

登录后欢迎通知。

/var/run/ftpd.pid

守护程序模式的默认 pid 文件。

/var/run/nologin

显示并拒绝访问。

/var/log/ftpd

匿名传输的日志文件。

/var/log/xferlog

会话日志的默认位置。

[参见](#__u53C2___u89C1_)
=======================

ftp(1), umask(2), getusershell(3), opie(4), ftpchroot(5), login.conf(5), inetd(8), syslogd(8)

[历史](#__u5386___u53F2_)
=======================

`ftpd` 实用程序出现在 4.2BSD 中。 WIDE Hydrangea IPv6 堆栈套件中添加了 IPv6 支持。

[缺陷](#__u7F3A___u9677_)
=======================

服务器必须以超级用户身份运行才能创建具有特权端口号的套接字。 它维护登录用户的有效用户ID，仅在将地址绑定到套接字时恢复为超级用户。 可能的安全漏洞已被广泛审查，但可能不完整。

January 21, 2010

FreeBSD 13.1-RELEASE