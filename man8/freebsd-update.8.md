  FREEBSD-UPDATE(8)  

FREEBSD-UPDATE(8)

FreeBSD System Manager's Manual

FREEBSD-UPDATE(8)

[名称](#__u540D___u79F0_)
=======================

`freebsd-update` —

获取并安装 FreeBSD 的二进制更新

[概要](#__u6982___u8981_)
=======================

`freebsd-update` \[`-b` basedir\] \[`-d` workdir\] \[`-f` conffile\] \[`-F`\] \[`-k` KEY\] \[`-r` newrelease\] \[`-s` server\] \[`-t` address\] \[`--not-running-from-cron`\] `command ...`

[描述](#__u63CF___u8FF0_)
=======================

`freebsd-update` 工具用于获取、安装和回滚 FreeBSD 基本系统的二进制更新。 请注意，更新仅在为 FreeBSD 版本和正在使用的体系结构构建时可用；特别是， FreeBSD 安全团队仅为 FreeBSD 发布工程团队以二进制形式发布的版本构建更新，例如 FreeBSD 11.2-RELEASE 和 FreeBSD 12.0-RELEASE，但不构建 FreeBSD 11.2-STABLE 或 FreeBSD 13.0-CURRENT。

[选项](#__u9009___u9879_)
=======================

支持以下选项：

[`-b`](#b) basedir

在安装在 basedir 的系统上运行。 （默认值： /, 或在配置文件中给出。）

[`-d`](#d) workdir

将工作文件存储在 workdir 中。 （默认： /var/db/freebsd-update/, 或在配置文件中给出。）

[`-f`](#f) conffile

从 conffile 中读取配置选项。 （默认： /etc/freebsd-update.conf)

[`-F`](#F)

在升级未完成的情况下强制 `freebsd-update` `fetch` 继续。

[`-k`](#k) KEY

使用 KEY 的 SHA256 信任 RSA 密钥。 （默认值：从配置文件中读取值。）

[`-r`](#r) newrelease

指定 `freebsd-update` 应该升级到的新版本（例如 11.2-RELEASE）（仅升级命令）。

[`-s`](#s) server

从指定的服务器或服务器池中获取文件。 （默认值：从配置文件中读取值。）

[`-t`](#t) address

将 `cron` 命令的输出（如果有）发送到 address 。 （默认：root，或在配置文件中给出。）

[`--not-running-from-cron`](#-not-running-from-cron)

当没有控制 tty 时，强制 `freebsd-update` `fetch` 继续。 这是供自动化脚本和编排工具使用的。 请不要使用此标志运行 `freebsd-update` `fetch` 或类似内容，请参阅： `freebsd-update` `cron`

[`--currently-running`](#-currently-running) release

不检测当前运行的版本；相反，假设系统正在运行指定的 release 。 这在升级监狱时最有可能有用。

[命令](#__u547D___u4EE4_)
=======================

该 `command` 可以是以下任何一种：

[`fetch`](#fetch)

根据当前安装的世界和配置选项集，获取所有可用的二进制更新。

[`cron`](#cron)

休眠 1 到 3600 秒之间的随机时间，然后像使用 `fetch` 命令一样下载更新。 如果下载了更新，将发送一封电子邮件（如果通过 `-t` 选项或在配置文件中指定，则发送到 root 或其他地址）。 顾名思义，这个命令是为从 cron(8) 运行而设计的；随机延迟用于最小化大量机器同时尝试获取更新的概率。

[`upgrade`](#upgrade)

获取升级到新版本所需的文件。 在使用此命令之前，请确保您阅读了新版本的公告和发行说明，以防升级需要任何特殊步骤。 请注意，根据安装的 FreeBSD 基本系统的组件，此命令可能需要在 workdir 中最多 500 MB 的空间。

[`updatesready`](#updatesready)

检查是否有准备安装的更新。 如果没有要安装的更新，则返回退出代码 2。

[`install`](#install)

安装最近获取的更新或升级。 如果没有要安装的更新并且 `fetch` 命令未在同一调用中作为较早的参数传递，则返回退出代码 2。

[`rollback`](#rollback)

卸载最近安装的更新。

[`IDS`](#IDS)

将系统与已安装版本的 "known good" 索引进行比较。

[`showconfig`](#showconfig)

解析 conffile 和命令行选项后显示配置选项。

[提示](#__u63D0___u793A_)
=======================

*   如果您的时钟设置为当地时间，请添加该行
    
    `0 3 * * * root /usr/sbin/freebsd-update cron`
    
    到 /etc/crontab 将每晚检查更新。 如果您的时钟设置为 UTC，请选择凌晨 3 点以外的随机时间，以避免在托管更新的服务器上过度施加不均匀的负载。
    
*   尽管它的名字， `freebsd-update` 不应该被依赖为“入侵检测系统”，因为如果系统被篡改，它就不能被信任正常运行。 如果您打算使用此命令进行入侵检测，请确保从安全磁盘（例如 CD）引导。

[环境](#__u73AF___u5883_)
=======================

[`PAGER`](#PAGER)

寻呼程序用于在执行期间呈现各种报告。 (默认: “/usr/bin/less”) 。

当需要非交互式寻呼机时，可以将 `PAGER` 设置为 “cat” 。

[文件](#__u6587___u4EF6_)
=======================

/etc/freebsd-update.conf

`freebsd-update` 配置文件的默认位置。

/var/db/freebsd-update/

`freebsd-update` 存储临时文件和下载更新的默认位置。

[参见](#__u53C2___u89C1_)
=======================

freebsd-update.conf(5)

[作者](#__u4F5C___u8005_)
=======================

Colin Percival <[cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)\>

November 14, 2020

FreeBSD 13.1-RELEASE