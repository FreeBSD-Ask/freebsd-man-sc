# ftpd(8)

`ftpd` — Internet 文件传输协议服务器

## 名称

`ftpd`

## 概要

`ftpd [-a authmode] [-dilvU] [-g umask] [-p port] [-T maxtimeout] [-t timeout] [--gss-bindings] [-I | --no-insecure-oob] [-u default umask] [-B | --builtin-ls] [--good-chars=string]`

## 描述

`ftpd` 是 Internet 文件传输协议服务器进程。该服务器使用 TCP 协议，并在“ftp”服务规范中指定的端口上监听；参见 [services(5)](../man5/services.5.md)。

可用选项如下：

**`-a`** 选择所需的认证级别。Kerberos 认证登录无法关闭。默认仅允许 Kerberos 认证登录。可以通过向 `-a` 传入一个由逗号分隔的标志字符串来启用其他认证方式。可识别的标志如下：

**`plain`** 允许使用明文密码登录。密码可以是 OTP 或普通密码。

**`otp`** 与 `plain` 相同，但仅允许 OTP。

**`ftp`** 允许匿名登录。

以下组合模式为向后兼容而保留：

**`none`** 等同于 `plain,ftp`。

**`safe`** 等同于 `ftp`。

**`user`** 被忽略。

**`-d`** 调试信息通过 LOG_FTP 设施写入 syslog。

**`-g`** 匿名用户将获得 `umask` 指定的 umask。

**`--gss-bindings`** 要求对端使用 GSS-API 绑定（即确保 IP 地址匹配）。

**`-i`** 打开一个套接字并等待连接。这主要用于 `ftpd` 不是由 inetd 启动时的调试。

**`-l`** 每个成功和失败的 [ftp(1)](../man1/ftp.1.md) 会话都会通过 syslog 以 LOG_FTP 设施记录。如果此选项指定两次，还会记录 retrieve（get）、store（put）、append、delete、make directory、remove directory 和 rename 操作及其文件名参数。

**`-p`** 使用 `port`（服务名或端口号）代替默认的 `ftp/tcp`。

**`-T`** 客户端也可以请求不同的超时时长；通过 `-T` 选项可将允许的最大时长设置为 `timeout` 秒。默认限制为 2 小时。

**`-t`** 将不活动超时时长设置为 `timeout` 秒（默认为 15 分钟）。

**`-u`** 将初始 umask 设置为默认值 027 以外的值。

**`-U`** 在先前版本的 `ftpd` 中，当被动模式客户端向服务器请求数据连接时，服务器会使用 1024..4999 范围内的数据端口。现在默认情况下，如果系统支持 IP_PORTRANGE 套接字选项，服务器将使用 49152..65535 范围内的数据端口。指定此选项将恢复为旧行为。

**`-v`** 详细模式。

**`-B`**, **`--builtin-ls`** 使用内置 ls 列出文件

**`--good-chars=`**`string` 允许的匿名上传文件名字符

**`-I`**, **`--no-insecure-oob`** 不允许不安全的带外数据。0.6.3 之前的 Heimdal ftp 客户端不支持安全带外数据，因此启用此选项会使它们无法工作。

文件 `/etc/nologin` 可用于禁用 ftp 访问。如果该文件存在，`ftpd` 会显示它并退出。如果文件 `/etc/ftpwelcome` 存在，`ftpd` 会在发出“ready”消息之前打印它。如果文件 `/etc/motd` 存在，`ftpd` 会在成功登录后打印它。

ftp 服务器当前支持以下 ftp 请求。请求的大小写被忽略。

| Request | Description |
| --- | --- |
| ABOR | 中止上一个命令 |
| ACCT | 指定账户（被忽略） |
| ALLO | 分配存储空间（空操作） |
| APPE | 追加到文件 |
| CDUP | 切换到当前工作目录的父目录 |
| CWD | 更改工作目录 |
| DELE | 删除文件 |
| HELP | 提供帮助信息 |
| LIST | 列出目录中的文件（“`ls -lgA`”） |
| MKD | 创建目录 |
| MDTM | 显示文件的最后修改时间 |
| MODE | 指定数据传输 *mode* |
| NLST | 给出目录中文件的名称列表 |
| NOOP | 不执行任何操作 |
| PASS | 指定密码 |
| PASV | 为服务器到服务器的传输做准备 |
| PORT | 指定数据连接端口 |
| PWD | 打印当前工作目录 |
| QUIT | 终止会话 |
| REST | 重启未完成的传输 |
| RETR | 获取文件 |
| RMD | 删除目录 |
| RNFR | 指定重命名的源文件名 |
| RNTO | 指定重命名的目标文件名 |
| SITE | 非标准命令（见下一节） |
| SIZE | 返回文件大小 |
| STAT | 返回服务器状态 |
| STOR | 存储文件 |
| STOU | 以唯一名称存储文件 |
| STRU | 指定数据传输 *structure* |
| SYST | 显示服务器系统的操作系统类型 |
| TYPE | 指定数据传输 *type* |
| USER | 指定用户名 |
| XCUP | 切换到当前工作目录的父目录（已弃用） |
| XCWD | 更改工作目录（已弃用） |
| XMKD | 创建目录（已弃用） |
| XPWD | 打印当前工作目录（已弃用） |
| XRMD | 删除目录（已弃用） |

以下命令由 RFC2228 指定。

| AUTH | 认证/安全机制 |
| --- | --- |
| ADAT | 认证/安全数据 |
| PROT | 数据通道保护级别 |
| PBSZ | 保护缓冲区大小 |
| MIC | 完整性保护命令 |
| CONF | 机密性保护命令 |
| ENC | 隐私保护命令 |
| CCC | 清除命令通道 |

SITE 请求支持以下非标准或 UNIX 特定命令。

| UMASK | 更改 umask（例如 `SITE UMASK 002`） |
| --- | --- |
| IDLE | 设置空闲计时器（例如 `SITE IDLE 60`） |
| CHMOD | 更改文件模式（例如 `SITE CHMOD 755 filename`） |
| FIND | 使用 GNU [locate(1)](../man1/locate.1.md) 快速查找特定文件 |
| HELP | 提供帮助信息 |

以下与 Kerberos 相关的 site 命令也被支持。

| KAUTH | 获取远程票据 |
| --- | --- |
| KLIST | 显示远程票据 |

Internet RFC 959 中规定的其余 ftp 请求虽被识别，但未实现。MDTM 和 SIZE 未在 RFC 959 中规定，但会出现在下一次更新的 FTP RFC 中。

只有在 ABOR 命令之前在命令 Telnet 流中发送了 Telnet “Interrupt Process”（IP）信号和 Telnet “Synch”信号时，ftp 服务器才会中止活动的文件传输，如 Internet RFC 959 所述。如果在数据传输期间收到 STAT 命令，且其前有 Telnet IP 和 Synch 信号，将返回传输状态。

`ftpd` 按照 [csh(1)](../man1/csh.1.md) 所使用的“globbing”通配约定来解释文件名。这允许用户使用元字符“`*?[]{}~`”。

`ftpd` 根据以下规则对用户进行认证：

- 如果使用 Kerberos 认证，用户必须通过有效的票据，并且该主体必须被允许以远程用户身份登录。
- 登录名必须在密码数据库中，且不能具有空密码（如果使用 Kerberos 则不检查密码字段）。在这种情况下，客户端必须先提供密码，才能执行任何文件操作。如果用户具有 OTP 密钥，则成功 USER 命令的响应将包含 OTP 挑战。客户端可以选择以 PASS 命令回复标准密码或 OTP 一次性密码。服务器会自动判断所收到密码的类型，并尝试相应地进行认证。有关 OTP 认证的更多信息，参见 otp(1)。
- 登录名不得出现在文件 `/etc/ftpusers` 中。
- 用户必须具有 getusershell(3) 返回的标准 shell。
- 如果用户名出现在文件 `/etc/ftpchroot` 中，则该会话的根目录将通过 chroot(2) 更改为用户的登录目录，与“anonymous”或“ftp”账户相同（见下一条）。但是，用户仍须提供密码。此功能旨在作为完全匿名账户和完全特权账户之间的折中方案。该账户也应按匿名账户的方式设置。
- 如果用户名为“anonymous”或“ftp”，则密码文件中必须存在一个匿名 ftp 账户（用户“ftp”）。此时允许用户通过指定任意密码登录（按惯例应使用用户的电子邮件地址作为密码）。

在最后一种情况下，`ftpd` 采取特殊措施来限制客户端的访问权限。服务器对“ftp”用户的主目录执行 chroot(2)。为了不破坏系统安全，建议谨慎构建“ftp”子树，可参考以下匿名 ftp 指南。

一般来说，所有文件都应由“root”拥有，并具有不可写权限（644 或 755，取决于文件类型）。不应有文件由“ftp”拥有或可写（可能 `~ftp/incoming` 除外，如下所述）。

**`~ftp`** “ftp”主目录应由 root 拥有。

**`~ftp/bin`** 用于外部程序（如 [ls(1)](../man1/ls.1.md)）的目录。这些程序必须是静态链接的，或者在 chroot 环境下运行时必须为动态链接设置好环境。如果存在以下程序，则会被使用：

**ls** 列出文件时使用。

**compress** 当获取以 `.Z` 结尾的文件名，而该文件不存在时，`ftpd` 会尝试查找不带 `.Z` 的文件名并即时压缩。

**gzip** 与 compress 相同，只是针对以 `.gz` 结尾的文件。

**gtar** 允许将以 `.tar` 结尾的整个目录作为文件获取。也可以与压缩结合使用。必须使用 GNU Tar（或其他支持 `-z` 和 `-Z` 标志的工具）。

**locate** 将通过 `SITE FIND` 命令启用“fast find”。还必须在 `~ftp/etc` 中创建 `locatedb` 文件。

**`~ftp/etc`** 如果在此处放置 [passwd(5)](../man5/passwd.5.md) 和 [group(5)](../man5/group.5.md) 文件的副本，ls 将能够显示所有者名称而非数字。请记得从这些文件中删除密码。如果存在 `motd` 文件，会在成功登录后打印。

**`~ftp/dev`** 在此处放置 /dev/null(7) 的副本。

**`~ftp/pub`** 放置任何想要公开的内容的传统位置。

如果希望访客能够上传文件，请创建一个由“root”拥有、组为“ftp”且模式为 730 的 `~ftp/incoming` 目录（确保“ftp”是“ftp”组的成员）。以下限制适用于匿名用户：

- 创建的目录将具有模式 700。
- 上传的文件将以 umask 777 创建，除非使用 `-g` 选项更改。
- 以下命令不可用：`DELE`, `RMD`, `RNTO`, `RNFR`, `SITE UMASK` 和 `SITE CHMOD`。
- 文件名必须以字母数字字符开头，并由字母数字字符或以下任意字符组成：**`+`**（加号）、**`-`**（减号）、**`=`**（等号）、**`_`**（下划线）、**`.`**（句点）和 **`,`**（逗号）。

## 文件

**`/etc/ftpusers`** 用户访问列表。

**`/etc/ftpchroot`** 应被 chroot 的普通用户列表。

**`/etc/ftpwelcome`** 欢迎信息。

**`/etc/motd`** 登录后的欢迎信息。

**`/etc/nologin`** 显示并拒绝访问。

**`~/.klogin`** Kerberos 的登录访问。

## 参见

[ftp(1)](../man1/ftp.1.md), otp(1), [getusershell(3)](../gen/getusershell.3.md), ftpusers(5), syslogd(8)

## 标准

**`RFC 959`** FTP PROTOCOL SPECIFICATION

**`RFC 1938`** OTP Specification

**`RFC 2228`** FTP Security Extensions.

## 缺陷

服务器必须以超级用户身份运行才能创建具有特权端口号的套接字。它维护着已登录用户的有效用户 ID，仅在将地址绑定到套接字时才恢复为超级用户。可能存在的安全漏洞已经过仔细审查，但可能并不完整。

## 历史

`ftpd` 命令出现于 4.2BSD。
