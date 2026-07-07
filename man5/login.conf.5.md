# login.conf(5)

`login.conf` — 登录类功能数据库

## 名称

`login.conf`

## 概要

**/etc/login.conf**, **~/.login_conf**

## 描述

`login.conf` 包含登录类的各种属性和功能。登录类（用户账户数据库 **/etc/master.passwd** 中每条记录的可选注释）决定会话记账、资源限制和用户环境设置。系统中的各种程序使用它来设置用户的登录环境并强制执行策略、记账和管理限制。它还提供了用户能够向系统进行身份验证以及可用身份验证类型的手段。除了此处描述的属性外，第三方软件包还提供其他属性。

系统用户类功能数据库 **/etc/login.conf** 中的特殊记录“default”会自动用于 **/etc/master.passwd** 中没有有效登录类的任何非 root 用户。uid 为 0 且没有有效登录类的用户将使用记录“root”（如果存在），否则使用“default”。

用户可以在其主目录中单独创建一个名为 `.login_conf` 的文件，使用相同格式，包含记录 ID 为“me”的单个条目。如果存在，[login(1)](../man1/login.1.md) 将使用此文件设置用户定义的环境设置，这些设置会覆盖系统登录功能数据库中指定的设置。只能覆盖一部分登录功能，通常是不涉及身份验证、资源限制和记账的功能。

类功能数据库中的记录由多个以冒号分隔的字段组成。每条记录的第一个条目给出一个或多个记录所用的名称，每个名称以 `|` 字符分隔。第一个名称是最常用的缩写。给出的最后一个名称应是更能描述功能条目的长名称，所有其他名称都是同义词。除最后一个名称外，所有名称都应使用小写且不包含空格；最后一个名称可以包含大写字符和空格以提高可读性。

注意，由于冒号（`:`）用于分隔功能条目，因此必须在功能值或名称中嵌入字面冒号时使用 `\:` 转义序列。

FreeBSD 附带的默认 **/etc/login.conf** 是开箱即用的配置。每当对此文件或用户的 `~/.login_conf` 文件进行更改时，在使用 cap_mkdb(1) 将文件编译为数据库之前，修改不会被采纳。此数据库文件将具有 `.db` 扩展名，并通过 cgetent(3) 访问。有关功能数据库格式的更深入描述，请参见 [getcap(3)](../gen/getcap.3.md)。

## 功能

数据库中每条记录内的字段遵循 [getcap(3)](../gen/getcap.3.md) 的布尔型、字符串型 `=` 和数字型 `#` 约定，但数字型已弃用，推荐使用字符串格式，两种形式都可用于数字数据。值分为以下类别：

**b** 显式选择 512 字节块

**k** 选择千字节（1024 字节）

**m** 指定 1 兆字节（1048576 字节）的乘数

**g** 指定千兆字节单位

**t** 表示太字节。

**y** 表示 365 天年数

**w** 表示周数

**d** 天数

**h** 小时数

**m** 分钟数

**s** 秒数

**bool** 如果名称存在，则布尔值为 true；否则为 false

**file** 数据文件的路径名

**program** 可执行文件的路径名

**list** 以逗号或空格分隔的值（或值对）列表

**path** 以空格或逗号分隔的路径名列表，遵循通常的 csh 约定（带和不带用户名的前导波浪号展开到主目录等）

**number** 数值，可以是十进制（默认）、十六进制（前导 0x）或八进制（前导 0）。对于数字类型，只允许一个数值。数字类型也可以以字符串格式指定（即功能标记与值之间用 `=` 而非 `#` 分隔）。无论使用哪种方法，数据库中的所有记录都必须使用相同的方法，以便在插值记录中正确覆盖值。数值可以是无限的。

**size** 表示大小的数字。值的默认解释是字节数，但后缀可以指定替代单位：大小值是数字量，后缀的大小写不重要。连接的值相加。大小值可以是无限的。

**time** 一段时间，默认以秒为单位。前缀可以指定不同的单位：连接的值相加。例如，2 小时 40 分钟可以写为 9600s、160m 或 2h40m。时间值可以是无限的。

“infinity”、“inf”、“unlimited”、“unlimit,”和 -1 被视为无限值。

通常可以使用特殊的 *tc=value* 表示法来插值功能条目。

默认值在 `Default` 列中指定。如果没有默认值，则从设置登录环境的进程继承该值。

## 资源限制

| **名称** | **类型** | **默认值** | **描述** |
| --- | --- | --- | --- |
| coredumpsize | size | | 最大核心转储大小限制。 |
| cputime | time | | CPU 使用限制。 |
| datasize | size | | 最大数据大小限制。 |
| filesize | size | | 最大文件大小限制。 |
| kqueues | number | | 最大内核事件队列数。 |
| maxproc | number | | 最大进程数。 |
| memorylocked | size | | 最大锁定在核心内存中的大小限制。 |
| memoryuse | size | | 最大核心内存使用大小限制。 |
| openfiles | number | | 每个进程的最大打开文件数。 |
| pipebuf | size | | 最大管道缓冲区大小。 |
| pseudoterminals | number | | 最大伪终端数。 |
| sbsize | size | | 最大允许的套接字缓冲区大小。 |
| stacksize | size | | 最大栈大小限制。 |
| swapuse | size | | 最大交换空间大小限制。 |
| umtxp | number | | 最大进程共享 pthread 锁数。 |
| vmemoryuse | size | | 每个进程最大允许的 VM 使用总量。 |

这些资源限制条目实际上同时指定了最大限制和当前限制（参见 [getrlimit(2)](../sys/getrlimit.2.md)）。当前（软）限制是通常使用的限制，尽管允许用户将当前限制增加到最大（硬）限制。可以通过在功能名称后附加 `-max` 或 `-cur` 来单独指定最大和当前限制。

## 环境变量

| **名称** | **类型** | **默认值** | **描述** |
| --- | --- | --- | --- |
| charset | string | | 将 $MM_CHARSET 环境变量设置为指定值。 |
| cpumask | string | | 要将用户绑定到的 CPU 列表。语法与 [cpuset(1)](../man1/cpuset.1.md) 的 `-l` 参数相同，或为单词 `default`。如果设置为 `default`，则不采取任何操作。 |
| hushlogin | bool | false | 与拥有 ~/.hushlogin 文件相同。 |
| ignorenologin | bool | false | 登录不被 nologin 阻止。 |
| ftp-chroot | bool | false | 通过 [chroot(2)](../sys/chroot.2.md) 到用户的 `HOME` 目录限制 FTP 访问。详见 [ftpd(8)](../man8/ftpd.8.md)。 |
| label | string | | 默认 MAC 策略；参见 [maclabel(7)](../man7/maclabel.7.md)。 |
| lang | string | | 将 $LANG 环境变量设置为指定值。 |
| mail | string | | 将 $MAIL 环境变量设置为指定值。 |
| manpath | path | | man 页面的默认搜索路径。 |
| nocheckmail | bool | false | 登录时显示邮件状态。 |
| nologin | file | | 如果文件存在，将显示它并终止登录会话。 |
| path | path | /bin /usr/bin | 默认搜索路径。 |
| priority | number | 0 | 初始优先级级别。一个在 nice 范围内（-20 到 20 含）的值，向下扩展 32 个实时类优先级（因此 -52 映射到实时类中的优先级 0，-51 映射到 1，依此类推直到 -21 映射到 31；参见 rtprio(1)），向上扩展 32 个空闲类优先级（因此 21 映射到空闲类中的优先级 0，22 映射到 1，依此类推直到 52 映射到 31；参见 idprio(1)）。特殊值 `inherit` 阻止重置优先级。 |
| requirehome | bool | false | 登录需要有效的主目录。 |
| setenv | list | | 以逗号分隔的环境变量及其要设置的值列表。包含逗号的值必须加引号。 |
| shell | prog | | 要执行的会话 shell，而非 passwd 文件中指定的 shell。SHELL 环境变量将包含密码文件中指定的 shell。 |
| term | string | | 无法从其他方式确定时的默认终端类型。 |
| timezone | string | | $TZ 环境变量的默认值。 |
| umask | number | | 初始 umask。应始终以 0 开头以确保八进制解释。特殊值 `inherit` 明确表示不更改 umask。 |
| welcome | file | /etc/motd | 包含欢迎消息的文件。 |

## 认证

| **名称** | **类型** | **默认值** | **描述** |
| --- | --- | --- | --- |
| host.allow | list | | 用户可从中访问的远程主机通配符列表。 |
| host.deny | list | | 用户不可从中访问的远程主机通配符列表。 |
| login_prompt | string | | [login(1)](../man1/login.1.md) 给出的登录提示。 |
| login-backoff | number | 3 | 在每次后续尝试后插入退避延迟之前允许的登录尝试次数。退避延迟是超过 *login-backoff* 的尝试次数乘以 5 秒。 |
| login-retries | number | 10 | 登录失败之前允许的登录尝试次数。 |
| passwd_format | string | sha512 | 新密码或更改密码将使用的加密格式。有效值包括“des”、“md5”、“blf”、“sha256”和“sha512”；详见 crypt(3)。使用非 FreeBSD NIS 服务器的 NIS 客户端可能应使用“des”。 |
| passwd_prompt | string | | [login(1)](../man1/login.1.md) 呈现的密码提示。 |
| passwordtime | time | | [passwd(1)](../man1/passwd.1.md) 用于设置下一个密码到期日期。 |
| times.allow | list | | 允许登录的时间段列表。 |
| times.deny | list | | 禁止登录的时间段列表。 |
| ttys.allow | list | | 类中用户可用于访问的 tty 和 ttygroup 列表。 |
| ttys.deny | list | | 类中用户不可用于访问的 tty 和 ttygroup 列表。 |
| warnexpire | time | | 待处理账户到期的预先通知。 |
| warnpassword | time | | 待处理密码到期的预先通知。 |

这些字段旨在供 [passwd(1)](../man1/passwd.1.md) 和登录身份验证系统中的其他程序使用。

设置环境变量的功能会扫描 `~` 和 `$` 字符，分别替换为用户的主目录和名称。要将这些字符字面传递到环境变量中，请在字符前加反斜杠 `\` 进行转义。

*host.allow* 和 *host.deny* 条目是用于检查对系统的远程访问的逗号分隔列表，由主机名和/或 IP 地址列表组成，远程网络登录将根据这些列表进行检查。这些列表中的项目可以包含 shell 程序用于通配符匹配的通配符形式（有关实现的详细信息，请参见 [fnmatch(3)](../gen/fnmatch.3.md)）。对主机的检查同时针对远程系统的 Internet 地址和主机名（如果可用）。如果两个列表都为空或未指定，则允许来自任何远程主机的登录。如果 host.allow 包含一个或多个主机，则只允许匹配该列表中任何项的远程系统登录。如果 host.deny 包含一个或多个主机，则来自任何匹配主机的登录将被拒绝。

*times.allow* 和 *times.deny* 条目由逗号分隔的时间段列表组成，在这些时间段内允许类中的用户登录。这些表示为一个或多个日期代码，后跟以 24 小时格式表示的开始和结束时间，以连字符或破折号分隔。例如，MoThSa0200-1300 转换为周一、周四和周六的凌晨 2 点到下午 1 点。如果这两个时间列表都为空，则类中的用户可以在任何时间访问。如果指定了 *times.allow*，则只允许在给定的时间段内登录。如果指定了 *times.deny*，则在给定的时间段内拒绝登录，无论 *times.allow* 中指定的某个时间段是否适用。

注意，[login(1)](../man1/login.1.md) 仅强制执行实际登录在这些条目允许的时间段内。在会话生命周期内的进一步强制执行需要单独的守护进程来监视从允许时间段到非允许时间段的转换。

*ttys.allow* 和 *ttys.deny* 条目包含逗号分隔的 tty 设备列表（不带 /dev/ 前缀），类中的用户可使用这些设备访问系统，和/或 ttygroup 列表（有关 ttygroup 的信息，请参见 [getttyent(3)](../gen/getttyent.3.md) 和 ttys(5)）。如果两个条目都不存在，则用户使用的登录设备选择不受限制。如果仅指定了 *ttys.allow*，则用户仅限于给定组或设备列表中的 tty。如果仅指定了 *ttys.deny*，则用户被阻止使用指定的设备或组中的设备。如果两个列表都给定且非空，则用户限于 ttys.allow 允许但 ttys.deny 不可用的那些设备。

用于强制执行密码质量限制的 *minpasswordlen* 和 *minpasswordcase* 功能（以前由 `login.conf` 支持）已被 pam_passwdqc(8) PAM 模块取代。

## 保留功能

以下功能保留用于指示的用途，可能由第三方软件支持。它们不在基本系统中实现。

| **名称** | **类型** | **默认值** | **描述** |
| --- | --- | --- | --- |
| accounted | bool | false | 为此类中的所有用户启用会话时间记账。 |
| auth | list | passwd | 允许的身份验证样式。第一项是默认样式。 |
| auth-`type` | list | | 身份验证 `type` 允许的身份验证样式。 |
| autodelete | time | | 到期后自动删除账户的时间。终止会话时。 |
| bootfull | bool | false | 启用“仅在 ttygroup 满时引导”策略，针对任意组中 tty 上的登录会话。 |
| daytime | time | | 每天最大登录时间。 |
| expireperiod | time | | 到期分配时间。 |
| graceexpire | time | | 过期账户的宽限天数。 |
| gracetime | time | | 允许的额外宽限登录时间。 |
| host.accounted | list | | 登录记账处于活动状态的远程主机通配符列表。 |
| host.exempt | list | | 登录会话记账被豁免的远程主机通配符列表。 |
| idletime | time | | 注销前的最大空闲时间。 |
| minpasswordlen | number | 6 | 本地密码的最小长度。 |
| mixpasswordcase | bool | true | [passwd(1)](../man1/passwd.1.md) 是否在输入全小写密码时警告用户。 |
| monthtime | time | | 每月最大登录时间。 |
| refreshtime | time | | 账户刷新时允许的新时间。 |
| refreshperiod | str | | 账户时间刷新的频率。 |
| sessiontime | time | | 每次会话最大登录时间。 |
| sessionlimit | number | | 最大并发登录会话数。 |
| ttys.accounted | list | | 登录会话将被记账的 tty 和 ttygroup 列表。 |
| ttys.exempt | list | | 登录会话记账被豁免的 tty 和 ttygroup 列表。 |
| warntime | time | | 待处理超时的预先通知。 |
| weektime | time | | 每周最大登录时间。 |

*ttys.accounted* 和 *ttys.exempt* 字段的操作方式与上述 *ttys.allow* 和 *ttys.deny* 类似。*host.accounted* 和 *host.exempt* 列表也是如此。

## 参见

cap_mkdb(1), [login(1)](../man1/login.1.md), [chroot(2)](../sys/chroot.2.md), [getcap(3)](../gen/getcap.3.md), [getttyent(3)](../gen/getttyent.3.md), login_cap(3), login_class(3), pam(3), [passwd(5)](passwd.5.md), ttys(5), [ftpd(8)](../man8/ftpd.8.md) (`ports/ftp/freebsd-ftpd`), pam_passwdqc(8)

## 历史

文件 `login.conf` 首次出现在 FreeBSD 2.1.5 中。
