# who.1

`who` — 显示系统上的用户

## 名称

`who`

## 概要

`who [-abHmqsTu] [am i] [file]`

## 描述

`who` 实用程序显示当前已登录用户的信息。默认情况下，包括登录名、tty 名、登录的日期和时间，以及非本地时的远程主机名。

选项如下：

**`-a`** 等同于 `-bTu`，但输出不限于最后一次系统重启的日期和时间。

**`-b`** 输出最后一次系统重启的日期和时间。

**`-H`** 在输出上方输出列标题。

**`-m`** 仅显示连接到标准输入的终端的信息。

**`-q`** “快速模式”：以列形式列出已登录用户的名称和数量。忽略所有其他命令行选项。

**`-s`** 仅显示名称、线路和时间字段。这是默认值。

**`-T`** 指示每个用户是否接收消息。将写入以下字符之一：

- `+` 用户接收消息。
- `-` 用户不接收消息。
- `?` 发生错误。

**`-u`** 以 `hh`:`mm` 形式显示每个用户的空闲时间（小时和分钟），若用户空闲不足一分钟则显示 `.`，若用户空闲超过 24 小时则显示 “`old`”。

**`am i`** 等同于 `-m`。

默认情况下，`who` 从文件 **/var/run/utx.active** 中收集信息。可以指定备用 `file`，通常是 **/var/log/utx.log** （或 **/var/log/utx.log.[0-6]** ，具体取决于站点策略，因为 `utx.log` 可能变得很大，且被 ac(8) 压缩后每日版本可能保留也可能不保留）。`utx.log` 文件包含自 `utx.log` 上次被截断或创建以来每次登录、注销、崩溃、关机和日期更改的记录。

如果使用 **/var/log/utx.log** 作为文件，用户名可能为空或为特殊字符 ‘|’、‘}’ 和 ‘~’ 之一。注销会产生一个没有任何用户名的输出行。有关特殊字符的更多信息，请参见 getutxent(3)。

## 环境变量

`COLUMNS`、`LANG`、`LC_ALL` 和 `LC_TIME` 环境变量按 [environ(7)](../man7/environ.7.md) 中所述影响 `who` 的执行。

## 文件

**/var/run/utx.active**

**/var/log/utx.log**

**/var/log/utx.log.[0-6]**

## 退出状态

`who` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

显示已登录用户的简要摘要：

```sh
$ who -q
fernape          root             root
# users = 3
```

显示已登录用户及其线路和时间字段（不带标题）：

```sh
$ who -s
fernape          ttyv0        Aug 26 16:23
root             ttyv1        Aug 26 16:23
root             ttyv2        Aug 26 16:23
```

显示连接到标准输入的终端的信息：

```sh
$ who am i
fernape                       Aug 26 16:24
```

显示最后一次系统重启的日期和时间、用户是否接收消息以及每个用户的空闲时间：

```sh
$ who -a
                 - system boot  Aug 26 16:23   .
fernape          - ttyv0        Aug 26 16:23   .
root             - ttyv1        Aug 26 16:23   .
root             - ttyv2        Aug 26 16:23   .
```

与上相同，但显示标题：

```sh
$ who -aH
NAME             S LINE         TIME         IDLE  FROM
                 - system boot  Aug 26 16:23   .
fernape          - ttyv0        Aug 26 16:23   .
root             - ttyv1        Aug 26 16:23 00:01
root             - ttyv2        Aug 26 16:23 00:01
```

## 参见

[last(1)](last.1.md), [users(1)](users.1.md), [w(1)](w.1.md), getutxent(3)

## 标准

`who` 实用程序遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`who` 命令出现于 Version 1 AT&T UNIX。
