  PKG(8)  

PKG(8)

FreeBSD System Manager's Manual

PKG(8)

[名称](#__u540D___u79F0_)
=======================

`pkg`, `pkg-static` —

操作包

[概要](#__u6982___u8981_)
=======================

`pkg` \[`-v`\] \[`-d`\] \[`-l`\] \[`-N`\] \[`-j` ⟨jail name or id⟩ | `-c` ⟨chroot path⟩ | `-r` ⟨root directory⟩\] \[`-C` ⟨configuration file⟩\] \[`-R` ⟨repository configuration directory⟩\] \[`-4` | `-6`\] ⟨command⟩ ⟨flags⟩

`pkg` \[`--version`\] \[`--debug`\] \[`--list`\] \[`-N`\] \[`--jail` ⟨jail name or id⟩ | `--chroot` ⟨chroot path⟩ | `--rootdir` ⟨root directory⟩\] \[`--config` ⟨configuration file⟩\] \[`--repo-conf-dir` ⟨repository configuration directory⟩\] \[`-4` | `-6`\] ⟨command⟩ ⟨flags⟩

[描述](#__u63CF___u8FF0_)
=======================

`pkg` 提供了一个操作包的接口：注册、添加、删除和升级包。 `pkg-static` 是 `pkg` 的静态链接变体，通常仅用于 `pkg` 的初始安装。 功能上存在一些差异。有关详细信息，请参阅 pkg.conf(5) 。

[选项](#__u9009___u9879_)
=======================

`pkg` 支持以下选项：

[`-v`](#v), `--version`

显示当前版本的 `pkg` 。

[`-d`](#d), `--debug`

显示调试信息。

[`-l`](#l), `--list`

列出所有可用的命令名称，然后退出而不执行任何其他操作。 `-v` 选项优先于 `-l` 但 `-l` 将覆盖任何其他命令行参数。

[`-o`](#o) ⟨option=value⟩, `--option` ⟨option=value⟩

从命令行设置 `pkg` 的配置选项。 从环境中设置的选项被重新定义。 允许多次指定此选项。

[`-N`](#N)

激活状态检查模式。 防止 `pkg` 自动创建或初始化 /var/db/pkg/local.sqlite 中的 SQLite 数据库（如果它不存在）。

如果当前没有安装任何包，则防止 `pkg` 执行任何操作，因为使用 `pkg` 正确初始化的系统将始终至少注册 `pkg` 包本身。

如果在没有任何其他参数的情况下使用， `pkg` `-N` 将运行健全性测试，如果成功则打印出一条短消息，显示当前安装了多少包。 退出状态应该是系统是否配置为使用 `pkg` 作为其包管理系统的可靠指示。

示例用法：

 if pkg -N >/dev/null 2>&1; then # pkgng-specifics else # pkg\_install-specifics fi 

`-N`-
标志最初是在-
.Fx 8.4-
的 /usr/sbin/pkg 引导程序中发布的，但在 FreeBSD 9.1 中没有。 仅仅调用 `pkg` `-N` 可能是不够的，因为可能会调用引导程序，或者从 `pkg` 返回错误。 以下脚本是检测 `pkg` 是否已安装和激活的最安全方法：

 if TMPDIR=/dev/null ASSUME\_ALWAYS\_YES=yes \\ PACKAGESITE=file:///nonexistent \\ pkg info -x 'pkg(-devel)?$' >/dev/null 2>&1; then # pkgng-specifics else # pkg\_install-specifics fi 

[`-j`](#j) ⟨jail name or id⟩, `--jail` ⟨jail name or id⟩

`pkg` 将在给定的 ⟨jail name or id⟩, 中执行，其中 _name_ 匹配 “`jls` name” ， _id_ 匹配 “`jls` jid” 。 参见 jail(8) 和 jls(8) 。

[`-c`](#c) ⟨chroot path⟩, `--chroot` ⟨chroot path⟩

`pkg` 将在 ⟨chroot path⟩ 环境中 chroot。

[`-r`](#r) ⟨root directory⟩, `--rootdir` ⟨root directory⟩

`pkg` 将安装指定的 ⟨root directory⟩ 中的所有包。

[`-C`](#C) ⟨configuration file⟩, `--config` ⟨configuration file⟩

`pkg` 将使用指定的文件作为配置文件。

[`-R`](#R) ⟨repo conf dir⟩, `--repo-conf-dir` ⟨repo conf dir⟩

`pkg` 将在目录中搜索每个存储库的配置文件。 这会覆盖主配置文件中指定的任何 `REPOS_DIR` 值。

[`-4`](#4)

`pkg` 将使用 IPv4 来获取存储库和包。

[`-6`](#6)

`pkg` 将使用 IPv6 来获取存储库和包。

[命令](#__u547D___u4EE4_)
=======================

`pkg` 支持以下命令（或其明确的缩写）：

[`help`](#help) command

显示指定命令的使用信息。

[`add`](#add)

从本地源或远程源安装包。

从远程源安装时，您需要指定获取包时使用的协议。

目前支持的协议有 FTP、HTTP 和 HTTPS。

[`annotate`](#annotate)

添加、修改或删除包上的标记值样式注释。

[`alias`](#alias)

列出命令行别名。

[`audit`](#audit)

针对已知漏洞审核已安装的软件包。

[`autoremove`](#autoremove)

删除作为依赖项自动安装且不再需要的软件包。

[`backup`](#backup)

将本地包数据库转储到命令行上指定的文件。

[`bootstrap`](#bootstrap)

这是为了与 pkg(7) 引导程序兼容。如果已经安装了 `pkg` ，则什么也不做。

如果使用 `-f` 标志调用，将尝试从远程存储库重新安装 `pkg` 。

[`check`](#check)

健全性检查已安装的软件包。

[`clean`](#clean)

清理获取的远程包的本地缓存。

[`convert`](#convert)

与旧的 pkg\_add(1) 格式相互转换。

[`create`](#create)

创建一个包。

[`delete`](#delete)

从数据库和系统中删除一个包。

[`fetch`](#fetch)

从远程存储库中获取包。

[`info`](#info)

显示有关已安装包和包文件的信息。

[`install`](#install)

从远程包存储库安装包。如果在多个远程存储库中找到一个包，则从第一个存储库开始安装。依次尝试从每个包存储库下载包，直到成功获取包。

[`lock`](#lock)

防止修改或删除包。

[`plugins`](#plugins)

列出可用的插件。

[`query`](#query)

查询已安装包和包文件的信息。

[`register`](#register)

在数据库中注册一个包。

[`repo`](#repo)

创建本地包存储库以供远程使用。

[`rquery`](#rquery)

查询远程存储库的信息。

[`search`](#search)

在远程包存储库中搜索给定的模式。

[`set`](#set)

修改已安装数据库中的信息。

[`shell`](#shell)

打开本地或远程数据库的 SQLite shell。使用此命令时应格外小心。

[`shlib`](#shlib)

显示哪些包链接到特定的共享库。

[`stats`](#stats)

显示包数据库统计信息。

[`unlock`](#unlock)

解锁包，允许修改或删除它们。

[`update`](#update)

更新 pkg.conf(5) 中列出的可用远程存储库。

[`updating`](#updating)

显示已安装包的更新条目。

[`upgrade`](#upgrade)

将软件包升级到较新的版本。

[`version`](#version)

总结已安装的软件包版本。

[`which`](#which)

在数据库中查询安装了特定文件的包。

[环境](#__u73AF___u5883_)
=======================

pkg.conf(5) 中的所有配置选项都可以作为环境变量传递。

额外的环境变量是：

INSTALL\_AS\_USER

允许以普通用户身份进行所有操作，而不是在适当的时候检查 root 凭据。-
预计用户将确保 `pkg`-
操作的每个文件和目录都是用户可读的 (或在适当的情况下可写) 。

[文件](#__u6587___u4EF6_)
=======================

请参阅 pkg.conf(5) 。

[实例](#__u5B9E___u4F8B_)
=======================

搜索包：

`$ pkg search perl`

安装一个包：

`安装必须指定唯一的来源或版本，否则它将尝试安装所有匹配项。`

`% pkg install perl-5.14`

列出已安装的软件包：

`$ pkg info`

从远程存储库升级：

`% pkg upgrade`

更改已安装包的来源：

`% pkg set -o lang/perl5.12:lang/perl5.14`

`% pkg install -Rf lang/perl5.14`

列出非自动包：

`$ pkg query -e '%a = 0' %o`

列出自动包：

`$ pkg query -e '%a = 1' %o`

删除已安装的包：

`% pkg delete perl-5.14`

删除不需要的依赖项：

`% pkg autoremove`

将包从自动更改为非自动，这将阻止 `autoremove` 删除它：

`% pkg set -A 0 perl-5.14`

将包从非自动更改为自动，这将使 `autoremove` 允许在没有任何依赖项时将其删除：

`% pkg set -A 1 perl-5.14`

从已安装的包创建包文件：

`% pkg create -o /usr/ports/packages/All perl-5.14`

确定哪个软件包安装了文件：

`$ pkg which /usr/local/bin/perl`

审核已安装的软件包以获取安全建议：

`$ pkg audit`

检查已安装的软件包是否存在校验和不匹配：

`# pkg check -s -a`

检查缺少的依赖项：

`# pkg check -d -a`

显示一个包的 pkg-message：

`# pkg info -D perl-5.14`

[参见](#__u53C2___u89C1_)
=======================

pkg\_create(3), pkg\_printf(3), pkg\_repos(3), pkg-keywords(5), pkg-lua-script(5), pkg-repository(5), pkg-script(5), pkg-triggers(5), pkg.conf(5), pkg-add(8), pkg-alias(8), pkg-annotate(8), pkg-audit(8), pkg-autoremove(8), pkg-backup(8), pkg-check(8), pkg-clean(8), pkg-config(8), pkg-create(8), pkg-delete(8), pkg-fetch(8), pkg-info(8), pkg-install(8), pkg-lock(8), pkg-query(8), pkg-register(8), pkg-repo(8), pkg-rquery(8), pkg-search(8), pkg-set(8), pkg-shell(8), pkg-shlib(8), pkg-ssh(8), pkg-stats(8), pkg-triggers(8), pkg-update(8), pkg-updating(8), pkg-upgrade(8), pkg-version(8), pkg-which(8)

要为一台或多台服务器构建您自己的软件包集，请参阅 poudriere(8) (**ports/**ports-mgmt/poudriere) 。

[FreeBSD pkg mirror](https://pkg.freebsd.org)

您最近的基于 MaxMind GeoLite geo-DNS 的 pkg 镜像。

[历史](#__u5386___u53F2_)
=======================

`pkg` 命令最早出现在 FreeBSD 9.1 中。

[作者和贡献者](#__u4F5C___u8005___u548C___u8D21___u732E___u8005_)
===========================================================

Baptiste Daroussin ⟨bapt@FreeBSD.org⟩, Julien Laffaye ⟨jlaffaye@FreeBSD.org⟩, Philippe Pepiot ⟨phil@philpep.org⟩, Will Andrews ⟨will@FreeBSD.org⟩, Marin Atanasov Nikolov ⟨dnaeon@gmail.com⟩, Yuri Pankov ⟨yuri.pankov@gmail.com⟩, Alberto Villa ⟨avilla@FreeBSD.org⟩, Brad Davis ⟨brd@FreeBSD.org⟩, Matthew Seaman ⟨matthew@FreeBSD.org⟩, Bryan Drewery ⟨bryan@shatow.net⟩, Eitan Adler ⟨eadler@FreeBSD.org⟩, Romain Tarti\`ere ⟨romain@FreeBSD.org⟩, Vsevolod Stakhov ⟨vsevolod@FreeBSD.org⟩, Alexandre Perrin ⟨alex@kaworu.ch⟩

[作者](#__u4F5C___u8005_)
=======================

请参阅 _https://github.com/freebsd/pkg/issues_ 上的问题跟踪器。

请将问题和问题直接发送到 pkg@FreeBSD.org 邮件列表。

June 29, 2020

FreeBSD 13.1-RELEASE