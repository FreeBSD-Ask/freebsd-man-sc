  SYSRC(8)  

SYSRC(8)

FreeBSD System Manager's Manual

SYSRC(8)

[名称](#__u540D___u79F0_)
=======================

`sysrc` —

安全地编辑系统 rc 文件

[概要](#__u6982___u8981_)
=======================

`sysrc` \[`-cdDeEFhinNqvx`\] \[`-s` name\] \[`-f` file\] \[`-j` jail | `-R` dir\] name\[\[+|-\]=value\] ... `sysrc` \[`-cdDeEFhinNqvx`\] \[`-s` name\] \[`-f` file\] \[`-j` jail | `-R` dir\] `-a` | `-A` `sysrc` \[`-E`\] \[`-s` name\] \[`-f` file\] `-l` `sysrc` \[`-eEqv`\] `-L` \[name ...\]

[描述](#__u63CF___u8FF0_)
=======================

`sysrc` 实用程序从系统 rc 文件集合中检索 rc.conf(5) 变量，并允许具有适当权限的进程以安全有效的方式更改值。

可以使用以下选项：

[`-a`](#a)

转储所有非默认配置变量的列表。

[`-A`](#A)

转储所有配置变量的列表 (包括默认值) 。

[`-c`](#c)

仅检查。 对于查询，如果设置了所有请求的变量 (即使为 NULL) , 则返回成功，否则返回错误状态。 对于分配，如果不需要更改则返回成功，否则返回失败。 如果详细（请参阅 (see “`-v`”) ）打印一条消息，说明是否设置了变量和/或需要更改。

[`-d`](#d)

打印给定变量的描述。

[`-D`](#D)

仅显示默认值（这与将 RC\_CONFS 设置为 NULL 或使用 NULL 文件参数传递 \`-f' 相同）。

[`-e`](#e)

将查询结果打印为 sh(1) 兼容的语法 (例如， ‘`var=value`’) 。如果指定了 ‘``` `-n` ```’ 或 ‘``` `-F` ```’ ，则忽略。

[`-E`](#E)

当给出 ‘`-l`’ 或 ‘`-L`’ 来列出配置文件时，只列出那些存在的。 更改设置时，最好修改现有文件。

[`-f`](#f) file

对指定文件而不是通过读取 `RC_DEFAULTS` 文件中的 ‘rc\_conf\_files’ 条目获得的文件进行操作。 可以为其他文件多次指定此选项。

[`-F`](#F)

仅显示每个指令所在的最后一个 rc.conf(5) 文件。

[`-h`](#h)

将简短的使用消息打印到 stderr 并退出。

[`--help`](#-help)

将完整的使用语句打印到 stderr 并退出。

[`-i`](#i)

忽略未知变量。

[`-j`](#j) jail

要在其中运行的 jail 的 jid 或名称 (覆盖 ‘`-R` dir’; 需要 jexec(8)) 。

[`-l`](#l)

列出启动时在标准输出上使用的配置文件并退出。

[`-L`](#L)

列出所有配置文件，包括标准输出上的 rc.conf.d 条目并退出。 可以与 ‘`-v`’ 或 ‘`-e`’ 组合以显示服务名称。 如果安装了所有命名服务，则 `sysrc`-
成功退出，否则失败。

[`-n`](#n)

仅显示变量值，而不是它们的名称。

[`-N`](#N)

只显示变量名，而不是它们的值。

[`-q`](#q)

安静的。 禁用详细并隐藏某些错误。 当与 ‘`-L`’ 和一个或多个 name 参数结合使用时，只提供退出状态而不提供输出。

[`-R`](#R) dir

在根目录 ‘dir’ 而不是 ‘/’ 中操作。

[`-s`](#s) name

如果存在 name 为 `rc.d` 的脚本 (在 “/etc/rc.d” 或 `local_startup` 目录中), 则将其 “rc.conf.d” 条目处理为对 ‘rc\_conf\_files’ 的潜在覆盖。 有关 “rc.conf.d” 的更多信息，请参见 rc.subr(8) 。可以与 ‘`-l`’ 结合使用以列出服务在启动时使用的配置文件。

[`-v`](#v)

冗长。打印找到该指令的特定 rc.conf(5) 文件的路径名。

[`--version`](#-version)

将版本信息打印到标准输出并退出。

[`-x`](#x)

从指定文件中删除变量。

该实用程序具有与 sysctl(8) 类似的语法。 它共享 \`-e' 和 \`-n' 选项 (详见上文) ，并且还具有相同的 ‘`name[=value]`’ 语法来进行查询/分配。 此外 (但与 sysctl(8) 不同) ，支持 ‘`name+=value`’ 将项目添加到值 (请参阅附加值) ，并且支持 ‘`name-=value`’ 从值中删除项目 (请参阅减去值) 。

然而，虽然 sysctl(8) 用于查询/修改进入内核中的 MIB，但 `sysrc` 却对系统 rc.conf(5) 配置文件中的值起作用。

系统配置文件列表在变量 ‘`rc_conf_files`’ 中的文件 ‘`/etc/defaults/rc.conf`’ 中配置，默认情况下包含以空格分隔的路径名列表。 在所有 FreeBSD 系统上，默认值为 "/etc/rc.conf /etc/rc.conf.local" 。 每个路径名都是在启动时按顺序获取的。 `sysrc` 在返回给定变量的值之前以相同的方式获取配置文件。

当提供变量名时， `sysrc` 将返回变量的值。 如果该变量未出现在任何配置的 ‘`rc_conf_files`’ 中，则会打印错误并返回错误状态。

更改给定变量的值时，该变量是否出现在任何 ‘`rc_conf_files`’ 中都没有关系。 如果该变量未出现在任何文件中，则将其附加到 ‘`rc_conf_files`’ 变量中第一个路径名的末尾。 否则， `sysrc` 将仅替换最后一个文件中包含该变量的最后一次出现。 这使得值在下次启动时生效，而无需大量修改这些完整的文件（但要注意不要让文件变得笨拙，应该重复调用 `sysrc` ）。

[附加值](#__u9644___u52A0___u503C_)
================================

当使用 ‘`key+=value`’ 语法向现有值添加项目时，值的第一个字符被用作分隔项目的分隔符 (通常是 “ ” 或 “,”) 。例如，在以下语句中：

*   `sysrc` cloned\_interfaces+=" gif0"

第一个字符是空格，通知 `sysrc` 现有值将被视为由空格分隔。 如果在 cloned\_interfaces 的现有值中未找到 ‘`gif0`’ ，则添加它 (仅当现有值为非 NULL 时才使用分隔符) 。

为方便起见，如果第一个字符是字母数字 (字母 A-Z, a-z, 或数字 0-9) 、点 (`.`), 或斜杠 (`/`), 则 `sysrc` 使用默认设置的空白作为分隔符。 例如，上面和下面的语句是等价的，因为 “gif0” 以字母数字字符 (字母 `g`) 开头：

*   `sysrc` cloned\_interfaces+=gif0

以下面的顺序为例：

*   `sysrc` cloned\_interfaces= # start with NULL
*   `sysrc` cloned\_interfaces+=gif0
    
    ``# NULL -> `gif0' (NB: no preceding delimiter)``
    
*   `sysrc` cloned\_interfaces+=gif0 # no change
*   `sysrc` cloned\_interfaces+="tun0 gif0"
    
    ```# `gif0' -> `gif0 tun0' (NB: no duplication)```
    

`sysrc` 防止添加相同的值（如果已经存在）。

[减去值](#__u51CF___u53BB___u503C_)
================================

当使用 ‘`key-=value`’ 语法从现有值中删除项目时，值的第一个字符被用作分隔项目的分隔符 (通常是 “ ” 或 “,”) 。 例如，在以下语句中：

``` `cloned_interfaces-=" gif0"` ```

第一个字符是空格，通知 `sysrc` 现有值将被视为由空格分隔。 如果在 cloned\_interfaces 的现有值中找到 ‘`gif0`’ ，则将其删除 (删除额外的分隔符) 。

为方便起见，如果第一个字符是字母数字 (字母 A-Z, a-z, 或数字 0-9), 点 (`.`), 或斜杠 (`/`), 则 `sysrc` 使用默认设置的空白作为分隔符。 例如，上面和下面的语句是等价的，因为 “gif0” 以字母数字字符 (字母 `g`) 开头：

*   `sysrc` cloned\_interfaces-=gif0

以下面的顺序为例：

*   `sysrc` foo="bar baz" # start
*   `sysrc` foo-=bar # \`bar baz' -> \`baz'
*   `sysrc` foo-=baz # \`baz' -> NULL

`sysrc` 删除所有提供的所有项目的所有出现并折叠项目之间的额外分隔符。

[环境](#__u73AF___u5883_)
=======================

`sysrc` 引用了以下环境变量：

[`RC_CONFS`](#RC_CONFS)

覆盖默认的 ‘`rc_conf_files`’ (即使设置为 NULL) 。

[`RC_DEFAULTS`](#RC_DEFAULTS)

‘`/etc/defaults/rc.conf`’ 文件的位置。

[依赖项](#__u4F9D___u8D56___u9879_)
================================

`sysrc` 需要以下标准命令：

awk(1), cat(1), chmod(1), env(1), grep(1), mktemp(1), mv(1), rm(1), sh(1), stat(1), tail(1), chown(8), jls(8), 和 jexec(8) 。

[文件](#__u6587___u4EF6_)
=======================

/etc/defaults/rc.conf

/etc/rc.conf

/etc/rc.conf.local

/etc/rc.conf.d/name

/etc/rc.conf.d/name/\*

/usr/local/etc/rc.conf.d/name

/usr/local/etc/rc.conf.d/name/\*

[示例](#__u793A___u4F8B_)
=======================

下面是一些简单的示例，说明如何使用 `sysrc` 从系统配置文件的 rc.conf(5) 集合中查询某些值：

`sysrc` sshd\_enable

`返回 $sshd_enable 的值，通常是 YES 或 NO。`

`sysrc` defaultrouter

`返回默认路由器的 IP 地址（如果已配置）。`

处理其他文件，例如 crontab(5):

`sysrc` -f /etc/crontab MAILTO

`返回 MAILTO 设置的值（如果已配置）。`

附加到现有值：

`sysrc` cloned\_interfaces+=gif0

`将 “gif0” 附加到 $cloned_interfaces (请参阅附加值)`

。

`sysrc` cloned\_interfaces-=gif0

`从 $cloned_interfaces 中删除 “gif0” (参见减法值)`

。

除上述语法外， `sysrc` 还支持内联 sh(1) PARAMETER 扩展，用于更改值的报告方式，如下所示：

`sysrc` 'hostname%%.\*'

``返回 $hostname 直到（但不包括）第一个 `.'。``

`sysrc` 'network\_interfaces%%\[$IFS\]\*'

`返回 $network_interfaces 的第一个单词。`

`sysrc` 'ntpdate\_flags##\*\[$IFS\]'

`返回 $ntpdate_flags 的最后一个单词（时间服务器地址）。`

`sysrc` usbd\_flags-"default"

`如果未设置或为 NULL，则返回 $usbd_flags 或默认值。`

`sysrc` cloned\_interfaces+"alternate"

`如果设置了 $cloned_interfaces，则返回 alternate 。`

[参见](#__u53C2___u89C1_)
=======================

rc.conf(5), jail(8), jexec(8), jls(8), rc(8), rc.subr(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`sysrc` 实用程序首次出现在 FreeBSD 9.2 中。

[作者](#__u4F5C___u8005_)
=======================

Devin Teske <[dteske@FreeBSD.org](mailto:dteske@FreeBSD.org)\>

[谢谢](#__u8C22___u8C22_)
=======================

Brandon Gooch, Enji Cooper, Julian Elischer, Pawel Jakub Dawidek, Cyrille Lefevre, Ross West, Stefan Esser, Marco Steinbach, Jilles Tjoelker, Allan Jude, 和 Lars Engels 寻求建议、帮助和测试。

February 26, 2019

FreeBSD 13.1-RELEASE