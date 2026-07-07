# sysrc(8)

`sysrc` — 安全地编辑系统 rc 文件

## 名称

`sysrc`

## 概要

`sysrc [-cdDeEFhinNqvx] [-s name] [-f file] [-j jail | -R dir] name[[+|-]=value] ...`
`sysrc [-cdDeEFhinNqvx] [-s name] [-f file] [-j jail | -R dir] -a | -A`
`sysrc [-E] [-s name] [-f file] -l`
`sysrc [-eEqv] -L [name ...]`

## 描述

`sysrc` 工具用于从系统 rc 文件集合中获取 [rc.conf(5)](../man5/rc.conf.5.md) 变量，并允许具有适当权限的进程以安全有效的方式更改值。

可用选项如下：

**`-a`** 转储所有非默认配置变量的列表。

**`-A`** 转储所有配置变量的列表（包含默认值）。

**`-c`** 仅检查。用于查询时，如果所有请求的变量都已设置（即使为 NULL），返回成功，否则返回错误状态。用于赋值时，如果不需要更改则返回成功，否则返回失败。如果启用详细模式（参见 “`-v`”），则打印一条消息说明变量是否已设置和/或是否需要更改。

**`-d`** 打印给定变量的描述。

**`-D`** 仅显示默认值（等同于将 RC_CONFS 设置为 NULL 或带 NULL 文件参数传递 `-f`）。

**`-e`** 以 [sh(1)](../man1/sh.1.md) 兼容语法打印查询结果（例如 `var=value`）。如果指定了 `-n` 或 `-F`，则忽略此选项。

**`-E`** 当与 `-l` 或 `-L` 一起使用以列出配置文件时，仅列实际存在的文件。更改设置时，优先修改已存在的文件。

**`-f`** `file` 操作指定文件，而非通过读取 `RC_DEFAULTS` 文件中的 ‘rc_conf_files’ 条目获得的文件。此选项可多次指定以添加更多文件。

**`-F`** 仅显示每个指令所在的最后一个 [rc.conf(5)](../man5/rc.conf.5.md) 文件。

**`-h`** 将简短用法消息打印到 stderr 并退出。

**`--help`** 将完整用法说明打印到 stderr 并退出。

**`-i`** 忽略未知变量。

**`-j`** `jail` 要在其中操作的 `jail` 的 `jid` 或名称（覆盖 `-R` `dir`；需要 [jexec(8)](jexec.8.md)）。

**`-l`** 在 stdout 上列出启动时使用的配置文件并退出。

**`-L`** 在 stdout 上列出所有配置文件（包括 rc.conf.d 条目）并退出。可与 `-v` 或 `-e` 组合以显示服务名称。如果所有指定的服务都已安装，`sysrc` 返回成功，否则返回失败。

**`-n`** 仅显示变量值，不显示变量名。

**`-N`** 仅显示变量名，不显示变量值。

**`-q`** 静默模式。禁用详细输出并隐藏某些错误。与 `-L` 及一个或多个 `name` 参数组合时，仅提供退出状态，无输出。

**`-R`** `dir` 在根目录 `dir` 而非 **/** 中操作。

**`-s`** `name` 如果存在名为 `name` 的 `rc.d` 脚本（位于 “/etc/rc.d” 或 `local_startup` 目录中），则处理其 “rc.conf.d” 条目作为 ‘rc_conf_files’ 的潜在覆盖。关于 “rc.conf.d” 的更多信息，参见 [rc.subr(8)](rc.subr.8.md)。可与 `-l` 组合以列出服务在启动时使用的配置文件。

**`-v`** 详细模式。打印找到指令的特定 [rc.conf(5)](../man5/rc.conf.5.md) 文件的路径名。

**`--version`** 将版本信息打印到 stdout 并退出。

**`-x`** 从指定文件中移除变量。

此工具的语法与 [sysctl(8)](sysctl.8.md) 类似。它共享 `-e` 和 `-n` 选项（详见上文），并且具有相同的 `name[=value]` 语法用于查询/赋值。此外（但与 [sysctl(8)](sysctl.8.md) 不同），`name+=value` 用于向值添加项（参见“追加值”章节），`name-=value` 用于从值中移除项（参见“移除值”章节）。

然而，[sysctl(8)](sysctl.8.md) 用于查询/修改进入内核的 MIB，而 `sysrc` 作用于系统 [rc.conf(5)](../man5/rc.conf.5.md) 配置文件中的值。

系统配置文件列表在文件 **/etc/defaults/rc.conf** 中的 `rc_conf_files` 变量中配置，默认包含一个以空格分隔的路径名列表。在所有 FreeBSD 系统上，此值默认为 “/etc/rc.conf /etc/rc.conf.local”。每个路径名在启动时按顺序加载。`sysrc` 以相同方式加载配置文件，然后返回给定变量的值。

提供变量名时，`sysrc` 返回该变量的值。如果变量未出现在任何已配置的 `rc_conf_files` 中，则打印错误并返回错误状态。

更改给定变量的值时，该变量是否出现在任何 `rc_conf_files` 中并不重要。如果变量未出现在任何文件中，则将其追加到 `rc_conf_files` 变量中第一个路径名的末尾。否则，`sysrc` 仅替换最后一个包含该变量的文件中最后一次出现的位置。这样可使值在下次启动时生效，而不会大量修改这些核心文件（同时也注意避免在反复调用 `sysrc` 时使文件变得臃肿）。

## 追加值

使用 `key+=value` 语法向现有值添加项时，值的第一个字符被用作分隔项的分隔符（通常是 “ ” 或 “,”）。例如，在以下语句中：

- `sysrc` cloned_interfaces+=" gif0"

第一个字符是空格，告知 `sysrc` 现有值以空白字符分隔。如果 `gif0` 未出现在 `cloned_interfaces` 的现有值中，则添加它（仅当现有值非 NULL 时才添加分隔符）。

为方便起见，如果第一个字符是字母数字（字母 A-Z、a-z 或数字 0-9）、点（`.`）或斜杠（`/`），`sysrc` 使用默认设置即空白字符作为分隔符。例如，由于 “gif0” 以字母数字字符（字母 `g`）开头，上述和以下语句是等效的：

- `sysrc` cloned_interfaces+=gif0

以以下序列为例：

- `sysrc` cloned_interfaces= # 以 NULL 开始
- `sysrc` cloned_interfaces+=gif0

```sh
# NULL -> `gif0'（注意：无前导分隔符）
```

- `sysrc` cloned_interfaces+=gif0 # 无变化
- `sysrc` cloned_interfaces+="tun0 gif0"

```sh
# `gif0' -> `gif0 tun0'（注意：无重复）
```

`sysrc` 防止添加已存在的相同值。

## 移除值

使用 `key-=value` 语法从现有值中移除项时，值的第一个字符被用作分隔项的分隔符（通常是 “ ” 或 “,”）。例如，在以下语句中：

```sh
sysrc cloned_interfaces-=" gif0"
```

第一个字符是空格，告知 `sysrc` 现有值以空白字符分隔。如果 `gif0` 出现在 `cloned_interfaces` 的现有值中，则移除它（移除多余的分隔符）。

为方便起见，如果第一个字符是字母数字（字母 A-Z、a-z 或数字 0-9）、点（`.`）或斜杠（`/`），`sysrc` 使用默认设置即空白字符作为分隔符。例如，由于 “gif0” 以字母数字字符（字母 `g`）开头，上述和以下语句是等效的：

- `sysrc` cloned_interfaces-=gif0

以以下序列为例：

- `sysrc` foo="bar baz" # 开始
- `sysrc` foo-=bar # `bar baz' -> `baz'
- `sysrc` foo-=baz # `baz' -> NULL

`sysrc` 移除所提供所有项的所有出现，并折叠项之间多余的分隔符。

## 环境变量

`sysrc` 引用以下环境变量：

**`RC_CONFS`** 覆盖默认的 `rc_conf_files`（即使设置为 NULL）。

**`RC_DEFAULTS`** **/etc/defaults/rc.conf** 文件的位置。

## 依赖

`sysrc` 需要以下标准命令：

[awk(1)](../man1/awk.1.md), [cat(1)](../man1/cat.1.md), [chmod(1)](../man1/chmod.1.md), [env(1)](../man1/env.1.md), [grep(1)](../man1/grep.1.md), mktemp(1), [mv(1)](../man1/mv.1.md), [rm(1)](../man1/rm.1.md), [sh(1)](../man1/sh.1.md), [stat(1)](../man1/stat.1.md), [tail(1)](../man1/tail.1.md), [chown(8)](chown.8.md), [chroot(8)](chroot.8.md), [jls(8)](jls.8.md), and [jexec(8)](jexec.8.md).

## 文件

**`/etc/defaults/rc.conf`**

**`/etc/rc.conf`**

**`/etc/rc.conf.local`**

**`/etc/rc.conf.d/name`**

**`/etc/rc.conf.d/name/*`**

**`/usr/local/etc/rc.conf.d/name`**

**`/usr/local/etc/rc.conf.d/name/*`**

## 实例

### 使用 rc.conf 文件

查询 `sshd_enable` 的值，通常为 YES 或 NO：

```sh
sysrc sshd_enable
```

返回默认路由器的 IP 地址（如果已配置）：

```sh
sysrc defaultrouter
```

### 使用其他文件

从 crontab(5) 返回 MAILTO 设置的值（如果已配置）：

```sh
sysrc -f /etc/crontab MAILTO
```

将 “gif0” 追加到 $cloned_interfaces（参见“追加值”章节）：

```sh
sysrc cloned_interfaces+=gif0
```

从 $cloned_interfaces 中移除 “gif0”（参见“移除值”章节）：

```sh
sysrc cloned_interfaces-=gif0
```

### 内联 shell 参数扩展

返回 $hostname 中第一个 `.` 之前的部分（不含 `.`）：

```sh
sysrc 'hostname%%.*'
```

返回 $network_interfaces 的第一个单词：

```sh
sysrc 'network_interfaces%%[$IFS]*'
```

返回 $ntpdate_flags（时间服务器地址）的最后一个单词：

```sh
sysrc 'ntpdate_flags##*[$IFS]'
```

返回 $usbd_flags，如果未设置或为 NULL 则返回 “default”：

```sh
sysrc usbd_flags-"default"
```

如果 $cloned_interfaces 已设置则返回 “alternate”：

```sh
sysrc cloned_interfaces+"alternate"
```

## 参见

[rc.conf(5)](../man5/rc.conf.5.md), [jail(8)](jail.8.md), [jexec(8)](jexec.8.md), [jls(8)](jls.8.md), [rc(8)](rc.8.md), [rc.subr(8)](rc.subr.8.md), [sysctl(8)](sysctl.8.md)

## 历史

`sysrc` 工具首次出现于 FreeBSD 9.2。

## 作者

Devin Teske <dteske@FreeBSD.org>

## 致谢

感谢 Brandon Gooch、Enji Cooper、Julian Elischer、Pawel Jakub Dawidek、Cyrille Lefevre、Ross West、Stefan Esser、Marco Steinbach、Jilles Tjoelker、Allan Jude 和 Lars Engels 提供的建议、帮助和测试。
