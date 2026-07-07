# man(1)

`man` — 显示在线手册文档页

## 名称

`man`

## 概要

`man [-adhlo] [-t | -w] [-M manpath] [-P pager] [-S mansect] [-m arch[:machine]] [-p [eprtv]] [mansect] page | file`

`man -K | -f | -k expression ...`

## 描述

`man` 实用程序查找并显示在线手册文档页。如果提供了 `mansect`，`man` 将搜索限制在手册的指定章节。

手册的章节如下：

- FreeBSD General Commands Manual（通用命令手册）
- FreeBSD System Calls Manual（系统调用手册）
- FreeBSD Library Functions Manual（库函数手册）
- FreeBSD Kernel Interfaces Manual（内核接口手册）
- FreeBSD File Formats Manual（文件格式手册）
- FreeBSD Games Manual（游戏手册）
- FreeBSD Miscellaneous Information Manual（杂项信息手册）
- FreeBSD System Manager's Manual（系统管理员手册）
- FreeBSD Kernel Developer's Manual（内核开发者手册）

`man` 可识别的选项：

**`-K`** `expression` 在所有手册页的全文中搜索扩展正则 `expression`，详见 re_format(7)。此选项需要 [mandoc(1)](mandoc.1.md)。此操作较慢。

**`-M`** `manpath` 强制使用特定的以冒号分隔的手册路径，而非默认搜索路径。参见 “环境变量” 中的 `MANPATH`。

**`-P`** `pager` 使用指定的分页器。如果启用颜色支持，默认为 `less -sR`，否则为 `less -s`。覆盖 `MANPAGER` 环境变量，后者又覆盖 `PAGER` 环境变量。

**`-S`** `mansect` 将搜索的手册章节限制为指定的以冒号分隔的列表。默认为 `1:8:2:3:3lua:n:4:5:6:7:9:l`。覆盖 `MANSECT` 环境变量。

**`-a`** 显示所有手册页，而非每个 `page` 参数仅显示找到的第一个。

**`-d`** 打印额外的调试信息。重复指定以增加详细程度。不显示手册页。

**`-f`** `expression` 在所有手册页的名称中搜索扩展正则 `expression`，模拟 [whatis(1)](whatis.1.md)。

**`-h`** 显示简短帮助信息并退出。

**`-k`** `expression` 在所有手册页的名称和描述中搜索扩展正则 `expression`，模拟 [apropos(1)](apropos.1.md) 的基本功能。

**`-l`** 将所有参数解释为要显示的手册页的绝对或相对文件名。不进行搜索，且 `-M`、`-m` 和 `-S` 选项被忽略。

**`-m`** `arch`[:`machine`] 覆盖默认的架构和机器设置，允许查找其他平台特定的手册页。参见 “实现说明” 了解此选项如何更改默认行为。覆盖 `MACHINE_ARCH` 和 `MACHINE` 环境变量。

**`-o`** 强制使用非本地化的手册页。参见 “实现说明” 了解本地化特定搜索的工作方式。覆盖 `LC_ALL`、`LC_CTYPE` 和 `LANG` 环境变量。

**`-p`** [`eprtv`] 在运行 nroff(1)（`ports/textproc/groff`）或 troff(1)（`ports/textproc/groff`）之前，使用给定的预处理器列表。有效的预处理器参数：覆盖 `MANROFFSEQ` 环境变量。

**`-t`** 通过 troff(1)（`ports/textproc/groff`）发送手册页源码，允许将手册页转换为其他格式。

**`-w`** 显示手册页的位置，而非手册页的内容。

**`e`** eqn(1)（`ports/textproc/groff`）

**`p`** pic(1)（`ports/textproc/groff`）

**`r`** refer(1)（`ports/textproc/groff`）

**`t`** tbl(1)（`ports/textproc/groff`）

## 实现说明

### 本地化特定搜索

`man` 实用程序支持不同本地化的手册页。搜索行为由三个环境变量中第一个非空字符串决定：`LC_ALL`、`LC_CTYPE` 或 `LANG`。如果设置，`man` 将使用以下逻辑搜索本地化特定的手册页：

- `lang`_`country`.`charset`
- `lang`.`charset`
- `en`.`charset`

例如，如果 `LC_ALL` 设置为 `ja_JP.eucJP`，当考虑 **`/usr/share/man`** 中的第 1 章手册页时，`man` 将搜索以下路径：

- **`/usr/share/man/ja_JP.eucJP/man1`**
- **`/usr/share/man/ja.eucJP/man1`**
- **`/usr/share/man/en.eucJP/man1`**
- **`/usr/share/man/man1`**

### 平台特定搜索

`man` 实用程序支持平台特定的手册页。搜索行为由 `-m` 选项或 `MACHINE_ARCH` 和 `MACHINE` 环境变量决定。例如，如果 `MACHINE_ARCH` 设置为 `aarch64` 且 `MACHINE` 设置为 `arm64`，当考虑 **`/usr/share/man`** 中的第 4 章手册页时，`man` 将搜索以下路径：

- **`/usr/share/man/man4/aarch64`**
- **`/usr/share/man/man4/arm64`**
- **`/usr/share/man/man4`**

### 显示特定手册文件

出于兼容性原因，`man` 会将任何包含至少一个 `/` 字符的参数解释为要显示的手册页的绝对或相对路径。这种启发式方法已被更广泛支持的 `-l` 选项所取代，现已弃用，可能在将来版本中移除。

## 环境变量

以下环境变量影响 `man` 的执行：

**`LC_ALL`**、`LC_CTYPE`、`LANG` 用于查找本地化特定的手册页。可通过运行 locale(1) 命令找到有效值。详见 “实现说明”。受 `-o` 选项影响。

**`MACHINE_ARCH`**、`MACHINE` 用于查找平台特定的手册页。如果未设置，则分别使用 `sysctl hw.machine_arch` 和 `sysctl hw.machine` 的输出。详见 “实现说明”。对应 `-m` 选项。

**`MANPATH`** 以冒号（`:`）分隔的目录列表，用于检查手册页。无效路径或不含手册数据库的路径将被忽略。被 `-M` 覆盖。如果 `MANPATH` 以冒号开头，则追加到默认列表之后；如果以冒号结尾，则前置于默认列表之前；如果包含两个相邻冒号，则在冒号之间插入标准搜索路径。如果以上条件均不满足，则覆盖标准搜索路径。参见 [manpath(1)](manpath.1.md)。

**`MANROFFSEQ`** 用于确定在运行 nroff(1)（`ports/textproc/groff`）或 troff(1)（`ports/textproc/groff`）之前使用的预处理器。如果未设置，默认为 tbl(1)（`ports/textproc/groff`）。对应 `-p` 选项。

**`MANSECT`** 将搜索的手册章节限制为指定的以冒号分隔的列表。对应 `-S` 选项。

**`MANWIDTH`** 如果设置为数值，则用作手册页显示的宽度。否则，如果设置为特殊值 `tty` 且输出到终端，手册页可跨整个屏幕宽度显示。

**`MANCOLOR`** 如果设置，则启用颜色支持。

**`MANPAGER`** 用于显示文件的程序。如果未设置且启用颜色支持，则使用 `less -sR`。如果未设置且禁用颜色支持，则使用 `PAGER`。如果两者都未设置，则使用 `less -s`。

## 文件

**`/etc/man.conf`** 系统配置文件

**`/usr/local/etc/man.d/*.conf`** 本地配置文件

## 退出状态

`man` 实用程序成功时退出 0，发生错误时退出 >0。

## 实例

显示 stat(2) 的手册页：

```sh
$ man 2 stat
```

显示 `stat` 的所有手册页：

```sh
$ man -a stat
```

列出标题或正文中匹配正则表达式的手册页：

```sh
$ man -k '\<copy\>.*archive'
```

使用 [cat(1)](cat.1.md) 作为分页器显示 [ls(1)](ls.1.md) 的手册页：

```sh
$ man -P cat ls
```

显示 [ls(1)](ls.1.md) 手册页的位置：

```sh
$ man -w ls
```

显示当前工作目录中的手册页：

```sh
$ man -l man.1
```

显示第 1 章和第 8 章中包含单词 `arm` 的手册页位置：

```sh
$ man -w -K '\<arm\>' -S 1:8
```

## 参见

[apropos(1)](apropos.1.md), [intro(1)](intro.1.md), [mandoc(1)](mandoc.1.md), [manpath(1)](manpath.1.md), [whatis(1)](whatis.1.md), intro(2), [intro(3)](../man3/intro.3.md), [intro(3lua)](../man3lua/intro.3lua.md), [intro(4)](../man4/intro.4.md), [intro(5)](../man5/intro.5.md), man.conf(5), [intro(6)](../man6/intro.6.md), [intro(7)](../man7/intro.7.md), mdoc(7), re_format(7), [intro(8)](../man8/intro.8.md), [intro(9)](../man9/intro.9.md)
