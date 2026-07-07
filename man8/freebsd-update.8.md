# freebsd-update(8)

`freebsd-update` — 抓取并安装 FreeBSD 的二进制更新

## 名称

`freebsd-update`

## 概要

`freebsd-update [-F] [-b basedir] [--currently-running release] [-d workdir] [-f conffile] [-j jail] [-k KEY] [--not-running-from-cron] [-r newrelease] [-s server] [-t address] [-v level] command ...`

## 描述

`freebsd-update` 工具用于抓取、安装和回滚 FreeBSD 基本系统的二进制更新。

## 二进制更新可用性

并非每个 FreeBSD 版本和架构都提供二进制更新。

通常，二进制更新适用于 FreeBSD 的 ALPHA、BETA、RC 和 RELEASE 版本，例如：

- FreeBSD 13.1-ALPHA3
- FreeBSD 13.1-BETA2
- FreeBSD 13.1-RC1
- FreeBSD 13.1-RELEASE

不适用于 PRERELEASE、STABLE 和 CURRENT 等分支，例如：

- FreeBSD 13.0-PRERELEASE
- FreeBSD 13.1-STABLE
- FreeBSD 14.0-CURRENT

特别是，FreeBSD 安全团队仅为 FreeBSD 发布工程团队以二进制形式发布的版本构建更新。

## 选项

支持以下选项：

**`-b`** `basedir` 对挂载在 `basedir` 的系统进行操作。（默认：**/**，或配置文件中指定的值。）

**`-d`** `workdir` 将工作文件存储在 `workdir` 中。（默认：**/var/db/freebsd-update/**，或配置文件中指定的值。）

**`-f`** `conffile` 从 `conffile` 读取配置选项。（默认：**/etc/freebsd-update.conf**）

**`-F`** 在存在未完成升级的情况下，强制 `freebsd-update` `fetch` 继续执行。

**`-j`** `jail` 对由 `jid` 或 `name` 指定的 jail 进行操作。（会检测已安装用户空间的版本，因此不再需要 `--currently-running` 选项。）

**`-k`** `KEY` 信任 SHA256 值为 `KEY` 的 RSA 密钥。（默认：从配置文件读取值。）

**`-r`** `newrelease` 指定 `freebsd-update` 应升级到的新版本（例如 11.2-RELEASE）（仅用于 `upgrade` 命令）。

**`-s`** `server` 从指定的服务器或服务器池抓取文件。（默认：从配置文件读取值。）

**`-t`** `address` 将 `cron` 命令的输出（如果有）邮寄到 `address`。（默认：root，或配置文件中指定的值。）

**`-v`** `level` 设置输出的详细程度。`level` 必须是 `stats`（抓取文件时显示进度统计；默认值）、`nostats`（不显示进度统计）或 `debug`（显示内部工具的所有输出）之一。

**`--not-running-from-cron`** 当没有控制 [tty(4)](../man4/tty.4.md) 时，强制 `freebsd-update` `fetch` 继续执行。此选项供自动化脚本和编排工具使用。请勿使用此标志从 crontab(5) 或类似方式运行 `freebsd-update` `fetch`，参见：`freebsd-update` `cron`

**`--currently-running`** `release` 不检测当前正在运行的版本；而是假设系统正在运行指定的 `release`。这在升级 jail 时最有用。

## 命令

`command` 可以是以下任意一个：

**`fetch`** 根据当前安装的 world 和已设置的配置选项，抓取所有可用的二进制更新。

**`cron`** 随机休眠 1 到 3600 秒，然后像使用 `fetch` 命令一样下载更新。如果下载了更新，将发送电子邮件（到 root 或通过 `-t` 选项或配置文件指定的其他地址）。正如其名，此命令专为从 cron(8) 运行而设计；随机延迟用于最大程度地减少大量机器同时尝试抓取更新的概率。

**`upgrade`** 抓取升级到新版本所需的文件。使用此命令前，请确保阅读新版本的公告和发行说明，以防升级需要任何特殊步骤。注意，根据已安装的 FreeBSD 基本系统组件，此命令可能需要在 `workdir` 中多达 500 MB 的空间。

**`updatesready`** 检查是否有已抓取待安装的更新。如果没有可安装的更新，返回退出码 2。

**`install`** 安装最近抓取的更新或升级。如果没有可安装的更新，并且在同一调用的早期参数中未传递 `fetch` 命令，则返回退出码 2。

**`rollback`** 卸载最近安装的更新。

**`IDS`** 将系统与已安装版本的“已知良好”索引进行比较。

**`showconfig`** 解析配置文件和命令行选项后显示配置选项。

## 提示

```sh
0 3 * * * root /usr/sbin/freebsd-update cron
```

- 如果你的时钟设置为本地时间，将上述行添加到 **/etc/crontab** 可每晚检查更新。如果你的时钟设置为 UTC，请选择 3AM 以外的随机时间，以避免对托管更新的服务器造成不均匀的负载。
- 尽管名字如此，`freebsd-update IDS` 不应被当作“入侵检测系统”来依赖，因为如果系统已被篡改，则不能信任它能正确运行。如果你打算将此命令用于入侵检测目的，请确保从安全磁盘（如 CD）启动。

## 环境变量

**`PAGER`** 用于在执行期间呈现各种报告的分页程序。（默认：“**/usr/bin/less**”。）当需要非交互式分页程序时，可将 `PAGER` 设置为“cat”。

## 文件

**`/etc/freebsd-update.conf`** `freebsd-update` 配置文件的默认位置。

**`/var/db/freebsd-update/`** `freebsd-update` 存储临时文件、已下载更新和回滚所需文件的默认位置。如果升级未在进行中且不需要回滚，**/var/db/freebsd-update/** 下的所有文件都可以删除。

## 参见

freebsd-version(1), [uname(1)](../man1/uname.1.md), [freebsd-update.conf(5)](../man5/freebsd-update.conf.5.md), nextboot(8)

## 作者

Colin Percival <cperciva@FreeBSD.org>

## 缺陷

在补丁级别情况下——例如从 13.2-RELEASE-p1 升级到 13.2-RELEASE-p2：如果对 **/etc/** 中某个文件的任何先前修改与可用更新冲突，则 `freebsd-update` 不会尝试合并。而是：`freebsd-update` 会打印受影响的本地修改文件列表。
