# batch(1)

`at` — 排队、查看或删除待稍后执行的作业

## 名称

`at`, `batch`, `atq`, `atrm`

## 概要

`at [-q queue] [-f file] [-mldbv] time at [-q queue] [-f file] [-mldbv] -t [[CC ]YY]] MM DD hh mm [. SS] at -c job [job ...] at -l [job ...] at -l -q queue at -r job [job ...]`

`atq [-q queue] [-v]`

`atrm job [job ...]`

`batch [-q queue] [-f file] [-mv] [time]`

## 描述

`at` 和 `batch` 实用程序从标准输入或指定文件读取命令，以便在稍后时间使用 [sh(1)](sh.1.md) 执行。

**`at`** 在指定时间执行命令；

**`atq`** 列出用户的待处理作业，除非用户是超级用户；在那种情况下，列出所有人的作业；

**`atrm`** 删除作业；

**`batch`** 在系统负载水平允许时执行命令；换言之，当负载平均值降至活动 CPU 数量的 _LOADAVG_MX 倍以下，或在调用 `atrun` 时指定的值以下时执行。

`at` 实用程序允许一些中等复杂的 `time` 规范。它接受 `HHMM` 或 `HH:MM` 形式的时间，以在一天中的特定时刻运行作业。（如果该时间已过，则假定为第二天。）或者，可以指定以下关键字：`midnight`、`noon` 或 `teatime`（4pm），时间后可加 `AM` 或 `PM` 后缀以在上午或下午运行。运行作业的日期也可通过以 `month-name day` 形式给出日期（可选 `year`）来指定，或使用 `DD.MM.YYYY`、`DD.MM.YY`、`MM/DD/YYYY`、`MM/DD/YY`、`MMDDYYYY` 或 `MMDDYY` 形式的日期。日期的指定必须跟在时间指定之后。时间也可指定为：[`now`] `+` `count time-units`，其中 time-units 可以是 `minutes`、`hours`、`days`、`weeks`、`months` 或 `years`，并且可以通过在时间后加 `today` 后缀告诉 `at` 今天运行作业，通过加 `tomorrow` 后缀告诉 `at` 明天运行作业。

`at` 实用程序还支持 POSIX 时间格式（参见 `-t` 选项）。

对于 `at` 和 `batch`，命令从标准输入或通过 `-f` 选项指定的文件中读取并执行。工作目录、环境（除 `TERM`、`TERMCAP`、`DISPLAY` 和 `_` 变量外）以及 `umask` 从调用时保留。从 [su(1)](su.1.md) shell 调用的 `batch` 或 `batch` 命令将保留当前用户 ID。如果命令产生了标准错误和标准输出，将通过邮件发送给用户。邮件使用 sendmail(8) 命令发送。如果 `batch` 从 [su(1)](su.1.md) shell 执行，登录 shell 的所有者将收到邮件。

超级用户在任何情况下都可以使用这些命令。对于其他用户，使用 `batch` 的权限由文件 **`_PERM_PATH/at.allow`** 和 **`_PERM_PATH/at.deny`** 决定。

如果文件 **`_PERM_PATH/at.allow`** 存在，则只有其中提及的用户名被允许使用 `batch`。在这两个文件中，只有当用户名在其所在行之前没有空格或其他字符、且名称后紧跟换行符（即使在文件末尾）时，才认为该用户已被列出。其他行被忽略，可用作注释。

如果 **`_PERM_PATH/at.allow`** 不存在，则检查 **`_PERM_PATH/at.deny`**，其中未提及的每个用户名都被允许使用 `batch`。

如果两者都不存在，则只有超级用户被允许使用 `batch`。这是默认配置。

## 实现说明

注意，`batch` 通过 cron(8) 守护进程实现，每五分钟调用一次 atrun(8)。这意味着 `batch` 的粒度可能不适用于所有部署场景。如果需要更细的粒度，可以编辑 **`/etc/cron.d/at`** 文件，该文件会被系统 crontab 读取，并从中继承 `SHELL` 和 `PATH` 环境变量。

## 选项

**`CC`** 年份的前两位数字（世纪）。

**`YY`** 年份的后两位数字。

**`MM`** 一年中的月份，从 1 到 12。

**`DD`** 一月中的日期，从 1 到 31。

**`hh`** 一天中的小时，从 0 到 23。

**`mm`** 一小时中的分钟，从 0 到 59。

**`SS`** 一分钟中的秒数，从 0 到 60。

**`-q`** `queue` 使用指定的队列。队列标识由单个字母组成；有效的队列标识范围为 `a` 到 `z` 和 `A` 到 `Z`。`_DEFAULT_AT_QUEUE` 队列是 `batch` 的默认队列，`_DEFAULT_BATCH_QUEUE` 队列是 `batch` 的默认队列。字母越靠后的队列以更高的 nice 值运行。如果作业被提交到以大写字母标识的队列，则被视为在当时提交到了 batch。如果给 `atq` 指定了特定队列，则仅显示该队列中待处理的作业。

**`-m`** 即使没有输出，也在作业完成时向用户发送邮件。

**`-f`** `file` 从 `file` 而非标准输入读取作业。

**`-l`** 不带参数时，列出调用用户的所有作业。如果给定一个或多个作业号，则仅列出那些作业。

**`-d`** 是 `atrm` 的别名（此选项已弃用；请改用 `-r`）。

**`-b`** 是 `batch` 的别名。

**`-v`** 对于 `atq`，显示队列中已完成但尚未删除的作业；否则显示作业将要执行的时间。

**`-c`** 将命令行上列出的作业输出到标准输出。

**`-r`** 删除指定的作业。

**`-t`** 使用时间格式指定作业时间。参数应为 [[`CC` ]`YY`]] `MM DD hh mm` [. `SS`] 形式，其中每对字母代表以下含义：如果未指定 `CC` 和 `YY` 字母对，则值默认为当前年份。如果未指定 `SS` 字母对，则值默认为 0。

## 文件

**`_ATJOB_DIR`** 包含作业文件的目录

**`_ATSPOOL_DIR`** 包含输出假脱机文件的目录

**`/var/run/utx.active`** 登录记录

**`_PERM_PATH/at.allow`** 允许权限控制

**`_PERM_PATH/at.deny`** 拒绝权限控制

**`_ATJOB_DIR/_LOCKFILE`** 作业创建锁文件

## 实例

要在三天后的下午 4 点运行作业，使用：

```sh
at 4pm + 3 days
```

要在 7 月 31 日上午 10:00 运行作业，使用：

```sh
at 10am Jul 31
```

要在明天凌晨 1 点运行作业，使用：

```sh
at 1am tomorrow
```

## 参见

[nice(1)](nice.1.md), [sh(1)](sh.1.md), umask(2), atrun(8), cron(8), sendmail(8)

## 作者

at 主要由 Thomas Koenig <ig25@rz.uni-karlsruhe.de> 编写。时间解析例程由 David Parsons <orc@pell.chi.il.us> 编写，Joe Halpin <joe.halpin@attbi.com> 做了少量增强。

## 缺陷

如果文件 **`/var/run/utx.active`** 不可用或已损坏，或者在调用 `atq` 时用户未登录，则邮件将发送到环境变量 `LOGNAME` 中找到的用户 ID。如果该变量未定义或为空，则假定为当前用户 ID。

当前实现的 `at` 和 `batch` 实用程序在用户竞争资源时并不适用。如果是这种情况，其他批处理系统（如 *nqs*）可能更合适。

指定 2038 年之后的日期在某些系统上可能无法工作。
