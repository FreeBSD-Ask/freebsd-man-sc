  PERIODIC(8)  

PERIODIC(8)

FreeBSD System Manager's Manual

PERIODIC(8)

[名称](#__u540D___u79F0_)
=======================

`periodic` —

运行周期性系统函数

[概要](#__u6982___u8981_)
=======================

`periodic` `daily`|`weekly` | `monthly`|`security`|directory ...

[描述](#__u63CF___u8FF0_)
=======================

`periodic` 实用程序旨在由 cron(8) 调用以执行位于指定目录中的shell 脚本。

必须指定以下一个或多个参数：

[`daily`](#daily)

执行标准的每日定期可执行运行。这通常发生在清晨（当地时间）。

[`weekly`](#weekly)

执行标准的每周定期可执行运行。 这通常发生在星期六早上很早。

[`monthly`](#monthly)

执行标准的每月定期可执行运行。 这通常发生在每月的第一天。

[`security`](#security)

执行标准的日常安全检查。 这通常是由 `daily` 运行产生的。

directory

包含一组要运行的可执行文件的任意目录。

如果参数是绝对目录名，则按原样使用，否则将在 /etc/periodic 和由 periodic.conf(5) 中的 local\_periodic 设置指定的任何其他目录下搜索（见下文）。

`periodic` 实用程序将运行指定目录中的每个可执行文件。 如果一个文件没有设置可执行位，它会被静默忽略。

每个脚本都需要以下列值之一退出：

0

该脚本在其输出中没有产生任何值得注意的内容。 ⟨basedir⟩\_show\_success 变量控制此输出的屏蔽。

1

该脚本在其输出中产生了一些值得注意的信息。 ⟨basedir⟩\_show\_info 变量控制此输出的屏蔽。

2

由于配置设置无效，该脚本产生了一些警告。 ⟨basedir⟩\_show\_badconfig 变量控制此输出的屏蔽。

\>2

脚本产生了不能被屏蔽的输出。

如果相关变量（其中 ⟨basedir⟩ 是脚本所在的基本目录）在 periodic.conf 中设置为 “`NO`” ，则 `periodic` 将屏蔽脚本输出。 如果该变量未设置为 “`YES`” 或 “`NO`” ，它将被赋予一个默认值，如 periodic.conf(5) 中所述。

所有剩余的脚本输出都基于 ⟨basedir⟩\_output 设置的值。

如果将其设置为路径名（以 ‘`/`’ 字符开头），则输出会简单地记录到该文件中。 newsyslog(8) 知道文件 /var/log/daily.log, /var/log/weekly.log 和 /var/log/monthly.log, 如果它们存在，它将在适当的时间轮换它们。 因此，如果您希望记录 `periodic` 输出，这些都是很好的值。

如果 ⟨basedir⟩\_output 值不以 ‘`/`’ 开头且不为空，则假定它包含电子邮件地址列表，并将输出邮寄给他们。 如果 ⟨basedir⟩\_show\_empty\_output 设置为 “`NO`”, 则如果输出为空，则不会发送邮件。

如果 ⟨basedir⟩\_output 未设置或为空，则将输出发送到标准输出。

[环境](#__u73AF___u5883_)
=======================

`periodic` 实用程序将 `PATH` 环境设置为包括所有标准系统目录，但不包括其他目录，例如 /usr/local/bin 。 如果添加依赖于其他路径组件的可执行文件，则每个可执行文件必须负责配置自己的适当环境。

[文件](#__u6587___u4EF6_)
=======================

/etc/crontab

`periodic` 实用程序通常通过系统默认 cron(8) 表中的条目调用

/etc/periodic

包含 daily, weekly, monthly 和 security 子目录的顶级目录，其中包含标准系统定期可执行文件

/etc/defaults/periodic.conf

periodic.conf 系统注册表包含控制 `periodic` 和标准 daily, weekly, monthly 和 security 和安全脚本行为的变量

/etc/periodic.conf

此文件包含默认 `periodic` 配置的本地覆盖

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

成功时退出状态为 0如果命令失败，则为 1。

[实例](#__u5B9E___u4F8B_)
=======================

系统 crontab 应具有与以下示例类似的 `periodic` 条目：

\# do daily/weekly/monthly maintenance 0 2 \* \* \* root periodic daily 0 3 \* \* 6 root periodic weekly 0 5 1 \* \* root periodic monthly 

/etc/defaults/periodic.conf 系统注册表通常会有一个 local\_periodic 变量读取：

`local_periodic="/usr/local/etc/periodic"`

要记录 `periodic` 输出而不是作为电子邮件接收，请将以下行添加到 /etc/periodic.conf:

daily\_output=/var/log/daily.log weekly\_output=/var/log/weekly.log monthly\_output=/var/log/monthly.log 

要仅查看每日定期作业的重要信息，请将以下行添加到 /etc/periodic.conf:

daily\_show\_success=NO daily\_show\_info=NO daily\_show\_badconfig=NO 

[诊断](#__u8BCA___u65AD_)
=======================

命令可能因以下原因之一失败：

usage: periodic <directory of files to execute>

没有将目录路径参数传递给 `periodic` 以指定脚本片段所在的位置。

<directory> not found

言自明。

[参见](#__u53C2___u89C1_)
=======================

sh(1), crontab(5), periodic.conf(5), cron(8), newsyslog(8)

[历史](#__u5386___u53F2_)
=======================

`periodic` 实用程序首次出现在 FreeBSD 3.0 中。

[作者](#__u4F5C___u8005_)
=======================

Paul Traina <[pst@FreeBSD.org](mailto:pst@FreeBSD.org)\> Brian Somers <[brian@Awfulhak.org](mailto:brian@Awfulhak.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

由于使用包含字符串的 shell 变量指定有关目录的信息， ⟨basedir⟩, ⟨basedir⟩ 必须只包含在 sh(1) 变量名，字母数字和下划线，第一个字符不能是数字。

June 18, 2020

FreeBSD 13.1-RELEASE