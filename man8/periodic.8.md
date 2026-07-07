# periodic(8)

`periodic` — 运行周期性系统函数

## 名称

`periodic`

## 概要

`periodic daily | weekly | monthly | security | directory ...`

## 描述

`periodic` 工具旨在由 cron(8) 调用以执行位于指定目录中的 shell 脚本。

必须指定以下一个或多个参数：

**`daily`** 执行标准的每日周期性可执行运行。通常在清晨（本地时间）进行。

**`weekly`** 执行标准的每周周期性可执行运行。通常在星期六清晨进行。

**`monthly`** 执行标准的每月周期性可执行运行。通常在每月第一天进行。

**`security`** 执行标准的每日安全检查。通常由 `daily` 运行派生。

**`directory`** 包含一组要运行的可执行文件的任意目录。

如果参数是绝对目录名，则按原样使用；否则在 **/etc/periodic** 和 [periodic.conf(5)](../man5/periodic.conf.5.md) 中 `local_periodic` 设置指定的任何其他目录下搜索（见下文）。

`periodic` 工具将运行指定目录或多个目录中的每个可执行文件。如果文件未设置可执行位，则会被静默忽略。

每个脚本必须以以下值之一退出：

**0** 脚本输出中未产生值得注意的内容。`<basedir>_show_success` 变量控制此输出的屏蔽。

**1** 脚本输出中产生了一些值得注意的信息。`<basedir>_show_info` 变量控制此输出的屏蔽。

**2** 脚本由于无效的配置设置产生了一些警告。`<basedir>_show_badconfig` 变量控制此输出的屏蔽。

**>2** 脚本产生了不得屏蔽的输出。

如果相关变量（其中 `<basedir>` 是脚本所在的基础目录）在 `periodic.conf` 中设为“`NO`”，`periodic` 将屏蔽脚本输出。如果变量未设为“`YES`”或“`NO`”，则按 [periodic.conf(5)](../man5/periodic.conf.5.md) 中描述的赋予默认值。

所有剩余的脚本输出根据 `<basedir>_output` 设置的值进行传递。

如果此设置为路径名（以 `/` 字符开头），输出直接记录到该文件。newsyslog(8) 知道 **/var/log/daily.log**、**/var/log/weekly.log** 和 **/var/log/monthly.log** 这些文件，如果它们存在，会在适当的时候轮转它们。因此，如果你想记录 `periodic` 输出，这些是不错的值。

如果 `<basedir>_output` 值不以 `/` 开头且不为空，则假定其包含电子邮件地址列表，输出将邮寄给它们。如果 `<basedir>_show_empty_output` 设为“`NO`”，则输出为空时不发送邮件。

如果 `<basedir>_output` 未设置或为空，输出发送到标准输出。

## 环境变量

`periodic` 工具设置 `PATH` 环境以包含所有标准系统目录，但不包含额外目录，如 **/usr/local/bin**。如果添加了依赖其他路径组件的可执行文件，每个可执行文件必须负责配置自己合适的环境。

## 文件

- **/etc/crontab** `periodic` 工具通常通过系统默认 cron(8) 表中的条目调用
- **/etc/periodic** 顶层目录，包含 `daily`、`weekly`、`monthly` 和 `security` 子目录，这些子目录包含标准系统周期性可执行文件
- **/etc/defaults/periodic.conf** `periodic.conf` 系统注册表包含控制 `periodic` 和标准 `daily`、`weekly`、`monthly` 和 `security` 脚本行为的变量
- **/etc/periodic.conf, ${LOCALBASE}/etc/periodic.conf** 此文件包含默认 `periodic` 配置的本地覆盖

## 退出状态

成功时退出状态为 0，命令失败时为 1。

## 实例

系统 crontab 应有类似于以下示例的 `periodic` 条目：

```sh
# 执行每日/每周/每月维护
0      2       *       *       *       root    periodic daily
0      3       *       *       6       root    periodic weekly
0      5       1       *       *       root    periodic monthly
```

**/etc/defaults/periodic.conf** 系统注册表通常会有一个 `local_periodic` 变量，内容为：

```sh
local_periodic="${_localbase}/etc/periodic"
```

其中 **${_localbase}** 在 **/usr/sbin/periodic** 内设置。

要记录 `periodic` 输出而非通过电子邮件接收，在 **/etc/periodic.conf** 中添加以下行：

```sh
daily_output=/var/log/daily.log
weekly_output=/var/log/weekly.log
monthly_output=/var/log/monthly.log
```

要仅查看每日周期性作业的重要信息，在 **/etc/periodic.conf** 中添加以下行：

```sh
daily_show_success=NO
daily_show_info=NO
daily_show_badconfig=NO
```

## 诊断

命令可能因以下原因之一失败：

- `usage: periodic <directory of files to execute>` — 没有向 `periodic` 传递目录路径参数来指定脚本片段所在位置。
- `<directory> not found` — 不言自明。

## 参见

[sh(1)](../man1/sh.1.md), crontab(5), [periodic.conf(5)](../man5/periodic.conf.5.md), cron(8), newsyslog(8)

## 历史

`periodic` 工具首次出现于 FreeBSD 3.0。

## 作者

Paul Traina <pst@FreeBSD.org> Brian Somers <brian@Awfulhak.org>

## 缺陷

由于使用包含字符串 `<basedir>` 的 shell 变量指定目录信息，`<basedir>` 必须仅包含在 [sh(1)](../man1/sh.1.md) 变量名中有效的字符，即字母数字和下划线，且第一个字符不能为数字。
